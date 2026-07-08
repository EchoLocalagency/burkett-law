# Phase 6 Plan — Technical SEO + Analytics + Justia Redirect Map

## Scope
Requirements: SEO-01..10 + ANL-01..05 (15 items).

## Deliverables
1. Sitewide meta audit (title ≤60, description ≤160, unique H1, canonical, OG, JSON-LD present)
2. Sitemap complete + lastmod current
3. robots.txt production-ready
4. llms.txt populated with real page list
5. GA4 measurement ID injection — placeholder `G-BURKETT_XXXX` sitewide, swap-instructions doc
6. GA4 conversion events (form_submit, phone_click, calendar_book) wired
7. Google Ads AW conversion slots wired (send_to filled in Phase 7/8)
8. GSC verification prep doc (DNS TXT)
9. Justia redirect map audit + completion
10. WCAG 2.1 AA spot audit (contrast, alt text, keyboard focus, skip link)
11. Schema graph audit — every schema block valid

## Workflow
1. Build `audit_meta.py` — extract per-page title/desc/H1/canonical/OG/JSON-LD; report violations
2. Fix violations with `fix_meta.py`
3. Inject GA4 + conversion listeners via `inject_analytics.py`
4. Sitemap regenerate via `build_sitemap.py`
5. llms.txt populate
6. Redirect audit against Justia Archive
7. WCAG spot audit
8. Commit atomically per concern
