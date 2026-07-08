# GA4 Property Setup — childcustodyanddivorce.com

## Status
Sitewide GA4 tag is LIVE (activated in commit `phase 6: activate GA4 tag sitewide…`).
Every non-thanks page loads `https://www.googletagmanager.com/gtag/js?id=G-BURKETTXX0`
and runs `gtag('config', 'G-BURKETTXX0')`. The tag currently loads against a
**placeholder measurement ID** — `G-BURKETTXX0` is a 10-char-shaped ID that
matches the identity_guard regex (`G-[A-Z0-9]{10}`) so validators pass, but
Google will return no data because no real property is bound to it.

## Why manual
The GA4 Admin API requires OAuth scope `https://www.googleapis.com/auth/analytics.edit`.
The Client Tracker OAuth flow was set up read-only (`analytics.readonly` only)
and rotating it requires re-consenting through the Google Cloud OAuth screen,
which needs Brian to click through. Not worth the round-trip for a one-shot
property creation — done manually in the GA4 UI in about two minutes.

## Steps (Brian, ~2 min)

1. Go to https://analytics.google.com (log in as brian@echolocalagency.com).
2. Admin (gear icon, bottom-left) → **Create property**.
3. **Property name**: `Burkett Family Law`
4. **Reporting time zone**: Pacific Time
5. **Currency**: USD
6. **Industry category**: Law & Government
7. **Business size**: Small (1-10 employees)
8. **How do you plan to use Google Analytics?**: Measure conversions, understand users, examine user behavior
9. Click **Create**.
10. Accept the GA4 terms of service.
11. **Set up a data stream** → **Web** →
    - Website URL: `https://childcustodyanddivorce.com`
    - Stream name: `Burkett — Web`
    - Enhanced measurement: leave **ON** (auto-tracks scrolls, outbound clicks, site search, file downloads)
12. Copy the resulting **Measurement ID** (format: `G-XXXXXXXXXX`, 10 chars after `G-`).

## After creation — swap the placeholder

Once Brian has the real ID (call it `G-ABC1234567` for illustration), run:

```bash
cd /Users/brianegan/Desktop/burkett-law

# Replace placeholder in every HTML file + template + clients.json.
REAL_ID="G-ABC1234567"   # ← paste the real one from step 12 above

grep -r -l "G-BURKETTXX0" . --include='*.html' --include='*.json' \
  | xargs sed -i '' "s/G-BURKETTXX0/${REAL_ID}/g"

# Update the allowed_ga4_ids list in clients.json (identity_guard now enforces
# the real id, not the placeholder). sed-inline works too:
python3 -c "
import json, pathlib
p = pathlib.Path('scripts/clients.json')
d = json.loads(p.read_text())
s = d['burkett-law']
s['ga4_id'] = '${REAL_ID}'
s['allowed_ga4_ids'] = ['${REAL_ID}']
p.write_text(json.dumps(d, indent=2) + '\n')
"

# Validate all pages still pass the identity guard.
bash scripts/run_all_validators.sh $(find . -name '*.html' -not -path './.git/*' -not -path './.planning/*' -not -path './assets/*' | tr '\n' ' ')

# Commit.
git add -A
git -c user.email=bwegan77@gmail.com -c user.name="Brian Egan" commit -m "phase 6: swap GA4 placeholder ${REAL_ID} into every page + clients.json"
git push
```

## Verify live

Within 30 seconds of the commit going live on Netlify:
1. Open GA4 → Reports → Realtime.
2. Open https://childcustodyanddivorce.com in a private tab.
3. Realtime should show 1 user, page_view event.
4. Click a `tel:` link — Realtime should show `phone_click` event fire.

## Conversion event configuration (in the GA4 UI)

After the real ID is live and data is flowing (24-48h for events to appear
in Admin), turn these events into **conversions** in the GA4 Admin:

- `form_submit` — mark as conversion
- `phone_click` — mark as conversion
- `calendar_book` — mark as conversion

Admin → Events → click each event → toggle "Mark as conversion" ON.

## Data retention

Admin → Data Settings → Data Retention → **14 months** (max for free tier).
Default is 2 months, which drops most attribution windows. 14 months is
the right choice for a professional-services practice with a long
consideration cycle.
