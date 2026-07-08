# Cutover Runbook — childcustodyanddivorce.com

**Cutover target date**: BEFORE 2026-07-31 (Justia sunset). Recommended: **2026-07-29 09:00 PT** (Tuesday morning; buffer to fix issues before Justia dies).
**Today**: 2026-07-08.
**Owner**: Brian Egan (executing) + Brian Burkett (Network Solutions DNS clicks).

**Hard rule from CLAUDE.md**: All site changes go through `git push`. Never `netlify deploy` directly. The one exception in this phase is Netlify API calls to configure the custom domain (already done 2026-07-08).

---

## Success definition

- childcustodyanddivorce.com serves the Netlify site over HTTPS with a valid Let's Encrypt cert.
- Zero dark window — traffic flips from Justia to Netlify without any time when neither serves the domain.
- Every mapped Justia URL returns `301` to a real page on Netlify (verified via `curl -I`).
- GSC stays verified (DNS TXT survives).
- GA4 receives events (`form_submit`, `phone_click`, `calendar_book`) within 72h.
- Netlify form submissions land in Burkett + brian@echolocalagency.com inboxes.

---

## T-14 — 2026-07-15 (Wednesday)

**Goal**: Ready the DNS layer + get GSC verified early so the TXT propagates well before flip day.

- [ ] Confirm Burkett's Network Solutions login is working. Ask him to do a test login and confirm access to DNS management for `childcustodyanddivorce.com`.
- [ ] **Lower TTL** on the current apex A record and www CNAME to `300` seconds. This is the critical T-14 action — it takes ~1 TTL to propagate, so old-TTL (usually 3600 or 86400) needs to expire before cutover. Burkett clicks; Brian coaches over screen-share or text.
- [ ] Verify TTL is dropped: `dig childcustodyanddivorce.com @1.1.1.1 | grep -A1 ANSWER` → TTL should show `300`.
- [ ] Go to https://search.google.com/search-console → **Add Property** → **Domain** → type `childcustodyanddivorce.com` → copy the `google-site-verification=...` string.
- [ ] Give Burkett the TXT record to add (Type: `TXT`, Host: `@`, Value: the full string). See `DNS-RECORDS.md` §3.
- [ ] Verify TXT propagation: `dig +short TXT childcustodyanddivorce.com @1.1.1.1 | grep google-site-verification`.
- [ ] Click **Verify** in Search Console. Confirm "Ownership auto-verified" or "Ownership verified".
- [ ] In Netlify Dashboard → burkett-law site → **Domain management**, confirm both `childcustodyanddivorce.com` (primary) and `www.childcustodyanddivorce.com` (alias) show as configured (they should — added via API 2026-07-08). The DNS panel next to each will say "Awaiting external DNS" — that's the expected state until cutover day.

---

## T-7 — 2026-07-22 (Wednesday)

**Goal**: Full site QA on the Netlify preview URL. Nothing should be broken when the domain flips.

Run through `PRE-FLIGHT-QA.md` (in this directory) — every checkbox must be green.

Highlights:

- [ ] Every one of the 55 production HTML pages returns 200 on `https://burkett-law.netlify.app/<path>`.
- [ ] Every canonical URL in the page source is `https://childcustodyanddivorce.com/...` (verified — 168 references confirmed 2026-07-08).
- [ ] `scripts/run_all_validators.sh` passes on every production HTML file (identity guard + Cal Bar lint + fabrication check).
- [ ] Contact form submits and lands in Burkett + brian@ inboxes. Test submission using the actual `https://burkett-law.netlify.app/contact.html` form.
- [ ] Calendar embed on `/contact.html` and homepage loads Burkett's GHL calendar. Book a test slot to Brian's throwaway email; delete the test appointment after.
- [ ] Google Rich Results Test on 9 template samples (home, bio, contact, practice hub, one practice pillar, one location page, blog hub, blog category, one blog post) — zero errors.
- [ ] GA4 measurement ID injection: `grep -rn "G-XXXXXXXXXX\|G-PLACEHOLDER" *.html includes/ practice-areas/ san-diego/ blog/` returns nothing. If real GA4 ID is not yet issued, this is the last window to create the property and inject. See `06-technical-seo/GA4-setup.md`.
- [ ] PageSpeed Insights (mobile) on top 5 pages: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1.
- [ ] `robots.txt` at `https://burkett-law.netlify.app/robots.txt` does NOT contain `Disallow: /` and correctly lists AI crawlers as Allow.
- [ ] Sitemap at `https://burkett-law.netlify.app/sitemap.xml` returns 200 with 51+ URLs, all `https://childcustodyanddivorce.com/`.

---

## T-3 — 2026-07-26 (Sunday)

**Goal**: Redirect verification + Netlify HTTPS pre-provision.

- [ ] Verify the 63 redirect lines in `_redirects` all resolve correctly on Netlify preview. Spot-check with:
  ```bash
  for url in \
    /blog/divorce-mediation-lawyer-in-san-diego-a-smarter-path-to-separation/ \
    /blog/how-a-divorce-attorney-in-san-diego-can-help-you-navigate-the-legal-process/ \
    /blog/navigating-marital-property-division-with-a-skilled-attorney-in-san-diego/; do
    echo "=== $url ==="
    curl -sI "https://burkett-law.netlify.app$url" | head -3
  done
  ```
  Expected: `HTTP/2 301` and `location:` header pointing at a real new URL.
- [ ] Try to pre-provision HTTPS. In Netlify Dashboard → Domain management → HTTPS section, click **Verify DNS configuration** — it will say "not resolved yet" (expected). At cutover time this will flip to a "Provision certificate" button.
- [ ] Confirm the Netlify site is on the Pro plan (yes — `plan: nf_team_pro`) — this gives us instant cert provisioning and no propagation lag on the Netlify side.
- [ ] Notify Burkett of the exact cutover window: **Tuesday 2026-07-29 09:00 PT**. Get his ack.

---

## T-1 — 2026-07-28 (Monday)

**Goal**: Final smoke test + go/no-go call.

- [ ] Re-run every validator: `bash scripts/run_all_validators.sh $(find . -name "*.html" -not -path "./.planning/*" -not -path "./scripts/tests/*")` — exit code must be `0`.
- [ ] RRT on 5 sample pages one more time.
- [ ] Send a test contact form submission on `https://burkett-law.netlify.app/contact.html`. Confirm arrival in both inboxes.
- [ ] Confirm the sticky phone button `tel:6192502683` works on mobile (open on iPhone, tap → dial screen with correct number).
- [ ] Confirm GA4 realtime shows at least one event (phone_click test).
- [ ] Cert readiness: check `https://api.netlify.com/api/v1/sites/69d38c3a-fcb7-4424-877e-df9fcd884e71/ssl` — should show the domain queued for provisioning.
- [ ] **Go/no-go**: Brian + Burkett agree cutover proceeds tomorrow morning.

---

## Cutover Day — 2026-07-29 09:00 PT (Tuesday)

**Goal**: Flip DNS. Justia is still live at this point (dies 07-31); if anything catastrophically breaks, we can roll back.

**Sequence (execute in order; DO NOT skip verification steps)**:

1. **09:00** — Burkett logs into Network Solutions DNS panel.
2. **09:05** — Burkett updates records per `DNS-RECORDS.md`:
   - Delete existing apex A record (Justia IP)
   - Add new apex A: `75.2.60.5` (TTL `300`)
   - Delete existing www CNAME (pointing at Justia)
   - Add new www CNAME: `burkett-law.netlify.app` (TTL `300`)
   - Save changes
3. **09:10** — Brian starts propagation checks:
   ```bash
   watch -n 30 'dig +short A childcustodyanddivorce.com @1.1.1.1; echo ---; dig +short CNAME www.childcustodyanddivorce.com @8.8.8.8'
   ```
   Expected: within 5-15 minutes, both resolvers return the new Netlify values.
4. **09:20** — Once DNS shows Netlify: check Netlify Domain management panel. HTTPS section should now show **"Provision certificate"** — click it. (Netlify may auto-click if `custom_domain` is set.)
5. **09:25** — Wait for cert. Refresh Netlify Domain page every 60s. When status shows **"Let's Encrypt certificate active"**, proceed. Typical time: 2-30 min. Netlify Pro plan should be near-instant.
6. **09:30** — First HTTPS smoke test:
   ```bash
   curl -I https://childcustodyanddivorce.com
   curl -I https://www.childcustodyanddivorce.com
   ```
   Expected: `HTTP/2 200` on both. Cert issuer should show `Let's Encrypt`.
7. **09:35** — Force www→apex canonical (should already be handled by Netlify's Primary Domain config, but verify):
   ```bash
   curl -sI https://www.childcustodyanddivorce.com | grep -i location
   ```
   Expected: `location: https://childcustodyanddivorce.com/`.

**If HTTPS is not provisioning after 30 minutes**: In Netlify Dashboard → Domain management → HTTPS → click **Renew certificate**. If still failing after another 15 min, check that DNS actually resolves to Netlify from Netlify's own perspective (they use a public resolver). Escalate to Netlify support with the site ID if needed.

---

## +2h — Cutover Day 11:00 PT

**Goal**: Verify the fully-served site behaves like the preview did.

- [ ] `curl -I` every top-level template:
  ```bash
  for path in / /about.html /contact.html /blog/ /practice-areas/ \
              /practice-areas/divorce/ /practice-areas/child-custody/ \
              /san-diego/divorce-attorney/carlsbad/ \
              /blog/divorce-mediation-in-san-diego.html; do
    echo "=== $path ==="
    curl -sI "https://childcustodyanddivorce.com$path" | head -2
  done
  ```
  Every response must be `HTTP/2 200`.
- [ ] Spot-check 5 Justia redirects — they should now 301 on the live domain:
  ```bash
  curl -sI https://childcustodyanddivorce.com/blog/divorce-mediation-lawyer-in-san-diego-a-smarter-path-to-separation/ | head -4
  ```
- [ ] Load the homepage in an incognito browser. Confirm: no cert warning, footer NAP displays, phone button dials, calendar embed loads, form is visible.
- [ ] Submit a live contact form on `https://childcustodyanddivorce.com/contact.html`. Confirm arrival in both inboxes.
- [ ] Confirm sitemap loads: `curl https://childcustodyanddivorce.com/sitemap.xml | head -20`.
- [ ] Confirm robots.txt: `curl https://childcustodyanddivorce.com/robots.txt` — no `Disallow: /`.

---

## +24h — 2026-07-30 09:00 PT

**Goal**: Search Console re-verified, sitemap submitted, indexing kickstarted.

- [ ] Search Console → Property `childcustodyanddivorce.com`: confirm ownership is still verified (the DNS TXT survived). If somehow lost, re-verify — TXT is still in place.
- [ ] Search Console → Sitemaps → **Add a new sitemap** → `sitemap.xml` → Submit. Status should flip to "Success" within 24-48h.
- [ ] URL Inspection on top 5 pages (home, `/about.html`, `/practice-areas/divorce/`, `/practice-areas/child-custody/`, `/blog/`) → click **Request Indexing** on each. Google will queue for crawl.
- [ ] Verify Netlify HTTPS cert is auto-renewing (it's Let's Encrypt on the Netlify Pro plan; nothing to do — just spot-check the expiration date shows ~90 days out).
- [ ] Justia still live? Confirm with `curl -I` against Justia hosts you have on file. It should be — 24h before their sunset.

---

## +72h — 2026-08-01 09:00 PT

**Goal**: Sunset window closed. Justia is down. Confirm we have full replacement coverage.

- [ ] Confirm Justia is off: try loading Burkett's old Justia URL — should 404 or DNS fail (their end). Our redirects don't rely on Justia being live; they run at Netlify's edge.
- [ ] GA4: check Realtime + past-24h reports. Confirm at least one `form_submit`, one `phone_click`, and one `page_view` event has fired.
- [ ] Netlify Dashboard → Forms → verify at least one real form submission has landed (or a test submission from you). If Forms panel shows 0 submissions and you submitted a test, debug: probably the form has `data-netlify="true"` missing (already verified in Phase 2, but re-check `contact.html`).
- [ ] Netlify Dashboard → burkett-law → Domain management → HTTPS: cert healthy, expiry ~90 days.
- [ ] **Restore TTL** at Network Solutions. Have Burkett bump apex A + www CNAME TTL from `300` → `3600`. This reduces DNS query load and stabilizes future resolvers.
- [ ] Search Console: Coverage report — check for any spike in 404s (would indicate a Justia URL missed by the redirect map). Add missing redirects if found.
- [ ] Submit `sitemap.xml` in Bing Webmaster Tools too (bonus indexing).
- [ ] Send Burkett a "we're live, all systems green" summary email + calendar the Phase 8 kickoff (GBP + Ads takeover) for the following week.

---

## Rollback (only usable through 2026-07-30)

If cutover day reveals a critical issue and rollback is called:

1. Burkett restores the original Justia A record and www CNAME at Network Solutions.
2. Because TTL was lowered to `300`, resolvers refresh within 5 minutes.
3. Justia is still serving through 2026-07-31, so users see the old site again.
4. Fix the issue on Netlify. Re-schedule cutover before 2026-07-31.

**After 2026-07-31**: Justia is dead. Do not roll back. If a critical issue is found on the live Netlify site, fix forward with a `git push`.

---

## Human-owned actions summary

Only these steps require Burkett or Brian human action (everything else is automated / already done):

| When | Who | Action |
|------|-----|--------|
| T-14 | Burkett | Lower DNS TTL to 300s at Network Solutions |
| T-14 | Brian | Grab GSC TXT token, give to Burkett |
| T-14 | Burkett | Add GSC TXT record |
| T-14 | Brian | Click "Verify" in GSC |
| T-7 | Brian | Full site QA per `PRE-FLIGHT-QA.md` |
| T-3 | Brian | Verify redirects on Netlify preview |
| T-3 | Brian | Confirm cutover time with Burkett |
| T-1 | Brian | Final smoke test + go/no-go |
| Cutover 09:05 | Burkett | Flip A record + CNAME at Network Solutions |
| Cutover 09:20 | Brian | Click "Provision certificate" in Netlify (if not auto) |
| Cutover 09:30 | Brian | HTTPS smoke test |
| +2h | Brian | Full 200-check on live domain + live form test |
| +24h | Brian | Submit sitemap in GSC + request indexing on top 5 |
| +72h | Burkett | Restore DNS TTL to 3600s |
| +72h | Brian | Confirm GA4 + Netlify Forms both receiving |
