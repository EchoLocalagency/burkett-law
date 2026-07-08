#!/usr/bin/env python3
"""Activate the GA4 tag + wire conversion event listeners sitewide.

State before this script:
- Every page ships a GA4 <!-- GA4-BEGIN … GA4-END --> block (commented out)
  with placeholder id `G-BURKETT_ID`.
- thanks.html additionally has a form_submit event fire inside the same block.

State after this script:
- GA4 block is UNCOMMENTED on every non-thanks page — tag loads, config
  runs, page_view auto-fires.
- Placeholder swapped from `G-BURKETT_ID` to `G-BURKETTXXX0`. Reason: the
  underscore in the original placeholder is not a legal char in a real
  GA4 measurement id, and if the placeholder ever ships to production
  gtag would 400 with a validation error visible in DevTools. XXX0 mimics
  legal-looking chars so failed hits look like a normal misconfigured id
  in the network tab and don't polute JS console.
- Sitewide phone_click listener injected before </body> that fires
  gtag('event','phone_click', ...) on any tel: link click. Also fires a
  Google Ads `conversion` event with a placeholder send_to
  (`AW-BURKETTAWXXX0/PHONECLICKXX`) so the wire is in place — Phase 8
  swaps the real AW conversion id.
- calendar_book slot: fires on postMessage from the GHL calendar iframe
  (their embed posts an appointment-booked message). Same AW placeholder.
- Also updates clients.json ga4_id to G-BURKETTXXX0 + allowed_ga4_ids to
  the same, so the identity_guard now enforces the new placeholder.

Search-and-replace pattern for cutover (Phase 7):
  sed -i '' 's/G-BURKETTXXX0/G-YOURREAL01/g' **/*.html scripts/clients.json
  sed -i '' 's|AW-BURKETTAWXXX0/PHONECLICKXX|AW-YOURREALID/YOURLABEL|g' **/*.html
  sed -i '' 's|AW-BURKETTAWXXX0/CALBOOKXX|AW-YOURREALID/YOURLABEL|g' **/*.html
"""
from __future__ import annotations
import json
import pathlib
import re

ROOT = pathlib.Path("/Users/brianegan/Desktop/burkett-law")
EXCLUDE_DIRS = {".git", ".planning", ".netlify", "assets", "node_modules", "scripts", "templates", "includes"}

OLD_ID = "G-BURKETT_ID"
NEW_ID = "G-BURKETTXX0"
AW_PHONE = "AW-BURKETTAWXXX0/PHONECLICKXX"
AW_FORM = "AW-BURKETTAWXXX0/FORMSUBMITXX"
AW_CAL = "AW-BURKETTAWXXX0/CALBOOKXX"

# Sitewide event-listener block. Injected just before </body>.
EVENT_LISTENERS = """
<!-- GA4 + Google Ads conversion event listeners (sitewide).
     Fires on: tel: link click (phone_click), and GHL calendar embed
     postMessage (calendar_book). form_submit fires from thanks.html
     on page load. Phase 8 swaps the AW placeholder for the real
     Google Ads conversion IDs. -->
<script>
(function () {
  if (typeof gtag !== 'function') return;

  // phone_click — any <a href="tel:...">
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"]');
    if (!a) return;
    var loc = window.location.pathname || '/';
    gtag('event', 'phone_click', {
      link_url: a.getAttribute('href'),
      page_path: loc
    });
    gtag('event', 'conversion', {
      send_to: 'AW-BURKETTAWXXX0/PHONECLICKXX'
    });
  }, { capture: true });

  // calendar_book — GHL calendar iframe postMessage.
  // GHL embeds send messages of the form { type: 'appointment_booked', ... }
  // We accept anything that contains "appointment" (defensive; GHL varies).
  window.addEventListener('message', function (evt) {
    try {
      var d = evt.data;
      var payload = typeof d === 'string' ? d : JSON.stringify(d || '');
      if (payload && payload.toLowerCase().indexOf('appointment') !== -1) {
        gtag('event', 'calendar_book', { source: 'ghl_embed' });
        gtag('event', 'conversion', {
          send_to: 'AW-BURKETTAWXXX0/CALBOOKXX'
        });
      }
    } catch (err) { /* no-op */ }
  }, false);
})();
</script>
"""


def find_html_files():
    for p in sorted(ROOT.rglob("*.html")):
        parts = set(p.relative_to(ROOT).parts)
        if parts & EXCLUDE_DIRS:
            continue
        yield p


def activate_ga4(text: str) -> tuple[str, bool]:
    """Uncomment the GA4 block and swap placeholder id."""
    changed = False
    # Uncomment: <!-- GA4-BEGIN\n...\n  GA4-END -->
    def uncomment(m):
        nonlocal changed
        changed = True
        body = m.group(1)
        return body

    new = re.sub(
        r"<!--\s*GA4-BEGIN\s*(.*?)\s*GA4-END\s*-->",
        uncomment,
        text,
        flags=re.S,
    )
    if changed:
        new = new.replace(OLD_ID, NEW_ID)
    return new, changed


def inject_listeners(text: str) -> tuple[str, bool]:
    marker = "// phone_click — any <a href=\"tel:...\">"
    if marker in text:
        return text, False
    if "</body>" not in text:
        return text, False
    new = text.replace("</body>", EVENT_LISTENERS + "\n</body>", 1)
    return new, True


def bump_clients_json():
    p = ROOT / "scripts/clients.json"
    data = json.loads(p.read_text())
    site = data["burkett-law"]
    old = site.get("ga4_id")
    if old == NEW_ID and NEW_ID in site.get("allowed_ga4_ids", []):
        return False
    site["ga4_id"] = NEW_ID
    allowed = set(site.get("allowed_ga4_ids", []))
    allowed.discard(OLD_ID)
    allowed.discard("G-BURKETT_PLACEHOLDER")
    allowed.add(NEW_ID)
    site["allowed_ga4_ids"] = sorted(allowed)
    p.write_text(json.dumps(data, indent=2) + "\n")
    return True


def main():
    count_ga = 0
    count_listeners = 0
    for f in find_html_files():
        rel = str(f.relative_to(ROOT))
        text = f.read_text(encoding="utf-8")
        text, did_ga = activate_ga4(text)
        text, did_l = inject_listeners(text)
        if did_ga or did_l:
            f.write_text(text, encoding="utf-8")
            marks = []
            if did_ga:
                marks.append("GA4-activated")
                count_ga += 1
            if did_l:
                marks.append("listeners-injected")
                count_listeners += 1
            print(f"{rel}: {', '.join(marks)}")

    # Update template too so future pages inherit activated block.
    template = ROOT / "templates/base.html"
    if template.exists():
        t = template.read_text(encoding="utf-8")
        t, changed = activate_ga4(t)
        if changed:
            template.write_text(t, encoding="utf-8")
            print("templates/base.html: GA4-activated")

    changed = bump_clients_json()
    if changed:
        print(f"scripts/clients.json: ga4_id -> {NEW_ID}")
    print(f"\nTotals: GA4 activated on {count_ga} pages, listeners injected on {count_listeners} pages")


if __name__ == "__main__":
    main()
