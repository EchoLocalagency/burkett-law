# Pre-Flight QA Checklist (T-7)

**Date**: To run on 2026-07-22 (T-7 from planned 2026-07-29 cutover).
**Preview URL**: https://burkett-law.netlify.app
**Production URL after cutover**: https://childcustodyanddivorce.com

Every checkbox must be green before Brian confirms T-3 to Burkett. If any fail, fix, `git push`, and re-run.

---

## 1. Repo & deploy health

- [ ] Working tree clean: `git status` shows no uncommitted files.
- [ ] Latest commit is deployed: `git log -1 --format=%H` matches the current deploy in Netlify dashboard.
- [ ] Netlify build is green (last deploy state = `ready`).

## 2. Validators (Cal Bar + fabrication + identity guard)

- [ ] Run: `bash scripts/run_all_validators.sh $(find . -name "*.html" -not -path "./.planning/*" -not -path "./scripts/tests/*" -not -path "./.git/*" -not -path "./node_modules/*")`
- [ ] Exit code = `0`.
- [ ] No files in `scripts/tests/fixtures/` are pulled into git (they're intentional failure fixtures).

## 3. Canonical domain hygiene

- [ ] `grep -rn "burkett-law.netlify.app" *.html includes/ practice-areas/ san-diego/ blog/` returns nothing.
- [ ] `grep -rn "localhost\|127.0.0.1" *.html includes/ practice-areas/ san-diego/ blog/` returns nothing.
- [ ] `grep -rn "http://" *.html` (excluding schema.org and w3.org namespace URIs) returns nothing.
- [ ] Every page ships `<link rel="canonical" href="https://childcustodyanddivorce.com/...">` — spot-check on 10 sample pages.

## 4. Page count & availability

- [ ] 55 production HTML pages exist (excluding fixtures + templates + includes).
- [ ] Every page returns `HTTP/2 200` on the preview URL. Run:
  ```bash
  for f in $(find . -name "*.html" -not -path "./.planning/*" -not -path "./scripts/*" -not -path "./includes/*" -not -path "./templates/*" -not -path "./.git/*"); do
    path=${f#.}
    # Convert /path/index.html -> /path/ for pretty URLs disabled config
    code=$(curl -sI -o /dev/null -w "%{http_code}" "https://burkett-law.netlify.app$path")
    [ "$code" != "200" ] && echo "FAIL $code $path"
  done
  echo "Scan complete."
  ```
- [ ] `/thanks.html` returns 200 (form success page).
- [ ] `/robots.txt` returns 200 and contains AI-crawler Allow rules.
- [ ] `/sitemap.xml` returns 200 with 51+ URLs.
- [ ] `/llms.txt` returns 200.

## 5. Redirects (Justia legacy URLs)

- [ ] Spot-check 5 Justia URLs from `_redirects` return `HTTP/2 301` with a `location:` pointing at a real blog / practice-area URL. Sample:
  ```bash
  for url in \
    /blog/divorce-mediation-lawyer-in-san-diego-a-smarter-path-to-separation/ \
    /blog/how-a-divorce-attorney-in-san-diego-can-help-you-navigate-the-legal-process/ \
    /blog/navigating-marital-property-division-with-a-skilled-attorney-in-san-diego/ \
    /blog/child-custody-lawyer-san-diego/ \
    /blog/what-a-family-law-attorney-does/; do
    echo "=== $url ==="
    curl -sI "https://burkett-law.netlify.app$url" | head -3
  done
  ```
- [ ] No redirect returns 200 (that would mean it's not being caught).
- [ ] No redirect returns 500 (bad target).

## 6. Schema (Rich Results Test)

Open https://search.google.com/test/rich-results for each. Zero errors, zero warnings that affect eligibility.

- [ ] `https://burkett-law.netlify.app/` — LegalService + LocalBusiness + WebSite
- [ ] `https://burkett-law.netlify.app/about.html` — Person + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/contact.html` — LocalBusiness + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/practice-areas/` — CollectionPage + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/practice-areas/divorce/` — Service + FAQPage + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/practice-areas/child-custody/` — Service + FAQPage + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/san-diego/divorce-attorney/carlsbad/` — Service (areaServed: City) + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/blog/` — CollectionPage / Blog + BreadcrumbList
- [ ] `https://burkett-law.netlify.app/blog/divorce-mediation-in-san-diego.html` — LegalArticle + BreadcrumbList (author.@id → bio)

Confirm on each: `author.@id` and `about.@id` and `publisher.@id` cross-references all resolve to nodes on their target pages.

## 7. Forms + CTA trio

- [ ] Homepage CTA trio visible above the fold on mobile (iPhone SE viewport) and desktop.
- [ ] Sticky phone button `tel:6192502683` present on every page; tap dials on real iPhone.
- [ ] Calendar embed on `/` and `/contact.html` loads without error (GHL widget).
- [ ] Book a test slot on the calendar → confirmation page appears → cancel/delete after.
- [ ] Contact form submits from `/contact.html` → redirects to `/thanks/` (or `/thanks.html`) → email arrives at both Burkett + brian@echolocalagency.com.
- [ ] Netlify Forms panel (Dashboard → Forms) shows the test submission.

## 8. Analytics + Ads wiring

- [ ] GA4 measurement ID is real (not `G-XXXXXXXXXX`), and identity guard confirms it's Burkett's ID — grep for `G-XXXXXXXXXX` or any placeholder and confirm zero matches:
  ```bash
  grep -rn "G-XXXXXXXXXX\|G-PLACEHOLDER" *.html includes/ practice-areas/ san-diego/ blog/
  ```
- [ ] GA4 realtime shows `page_view` on the preview URL as you browse.
- [ ] `phone_click` fires when you tap the phone button (GA4 realtime event).
- [ ] `form_submit` fires when you submit the contact form.
- [ ] `calendar_book` fires when you complete a test booking.
- [ ] Google Ads AW conversion actions are wired (see `06-technical-seo/GoogleAds-conversions.md`). Placeholder AW IDs replaced with real ones (or acknowledged pending; can be updated post-cutover without a redeploy risk if using GTM).

## 9. Search Console

- [ ] Domain property `childcustodyanddivorce.com` is verified (from T-14 TXT).
- [ ] Sitemap URL is ready to submit (do not submit yet — wait until cutover +24h when the sitemap is served from the target domain).

## 10. Performance (PageSpeed Insights, mobile)

Run https://pagespeed.web.dev on each. Metrics must hit:
- LCP ≤ 2.5s
- INP ≤ 200ms
- CLS ≤ 0.1

- [ ] `https://burkett-law.netlify.app/`
- [ ] `https://burkett-law.netlify.app/about.html`
- [ ] `https://burkett-law.netlify.app/practice-areas/divorce/`
- [ ] `https://burkett-law.netlify.app/san-diego/divorce-attorney/carlsbad/`
- [ ] `https://burkett-law.netlify.app/blog/divorce-mediation-in-san-diego.html`

## 11. Accessibility (WCAG 2.1 AA)

- [ ] Keyboard nav works on homepage: tab through hero → CTAs → nav → footer without traps.
- [ ] Skip-to-content link exists and is keyboard-focusable.
- [ ] Contrast ratio ≥ 4.5:1 for all body text (spot-check via browser devtools accessibility panel).
- [ ] Every `<img>` has meaningful `alt` (or `alt=""` if purely decorative). Spot-check on 5 pages.
- [ ] `<html lang="en">` on every page.

## 12. Legal disclaimers

- [ ] Cal Bar Rule 7.1 disclaimer band present in footer on every page (already validated by `identity_guard.py`).
- [ ] `/disclaimer.html`, `/privacy.html`, `/terms.html` all reachable from footer.
- [ ] Contact form has the "Submitting this form does not create an attorney-client relationship" text directly under the form.

## 13. Cross-client identity check

- [ ] `grep -rn "Mr Green\|Ecosystem Lands\|Arcadian\|SoCal Artificial\|Top Tier\|Tri City\|Primal Plates\|Chef Dorothy\|Integrity Pro\|Psychic Experience" *.html includes/ practice-areas/ san-diego/ blog/` returns nothing (identity guard already enforces this at pre-commit; this is belt-and-suspenders).
- [ ] Every GA4 ID and phone number matches Burkett's — no bleedover from other clients.

---

## Sign-off

- Brian Egan: ______________________ Date: ______________
- Brian Burkett notified of cutover date/time: ______________

Proceed to T-3 only if all checkboxes above are green.
