# Phase 7 Verification — Cutover Prep

**Phase**: 7 — Cutover to childcustodyanddivorce.com
**Status**: **passed (prep complete)** — actual DNS flip executes on planned cutover day 2026-07-29.
**Verified**: 2026-07-08

Phase 7 is preparation. The atomic DNS-flip step at Network Solutions is Burkett's — his domain login. This verification confirms every prep artifact is in place so cutover day is checklist-driven, not discovery-driven.

---

## Requirements coverage

| Requirement | Description | Status | Evidence |
|-------------|-------------|--------|----------|
| CUT-01 | T-14 DNS TTL prep planned | passed | `CUTOVER-RUNBOOK.md` §T-14 |
| CUT-02 | T-7 full site QA checklist ready | passed | `PRE-FLIGHT-QA.md` (13 categories) |
| CUT-03 | T-3 redirect verification plan documented | passed | `CUTOVER-RUNBOOK.md` §T-3 |
| CUT-04 | T-1 pre-flight go/no-go documented | passed | `CUTOVER-RUNBOOK.md` §T-1 |
| CUT-05 | Cutover day sequence documented + Netlify custom domain configured | passed | `CUTOVER-RUNBOOK.md` §Cutover Day; Netlify API `custom_domain` set to `childcustodyanddivorce.com` + alias `www.childcustodyanddivorce.com` on 2026-07-08 |
| CUT-06 | +2h HTTPS + smoke test documented | passed | `CUTOVER-RUNBOOK.md` §+2h |
| CUT-07 | +24h GSC + +72h analytics/forms verification documented | passed | `CUTOVER-RUNBOOK.md` §+24h and §+72h |

## Netlify custom-domain status

Confirmed via `netlify api updateSite` call on 2026-07-08:

```json
{
  "custom_domain": "childcustodyanddivorce.com",
  "domain_aliases": ["www.childcustodyanddivorce.com"],
  "url": "http://childcustodyanddivorce.com",
  "ssl_url": "https://childcustodyanddivorce.com"
}
```

Netlify Dashboard will show "Awaiting external DNS" until Burkett flips the records on cutover day. Once DNS resolves, Let's Encrypt auto-provisions the cert (Netlify Pro plan — usually within minutes).

## DNS records documented

`DNS-RECORDS.md` in this directory contains:
- Apex A record: `75.2.60.5` (Netlify shared apex, primary) + `99.83.190.102` (backup, optional)
- ALIAS/ANAME fallback: `apex-loadbalancer.netlify.com` (only if Network Solutions UI exposes ALIAS)
- www CNAME: `burkett-law.netlify.app`
- GSC verification TXT: pattern documented, exact token from GSC UI at T-14
- Records to LEAVE alone: MX, existing SPF/DKIM/DMARC TXT

## Site content readiness

Verified 2026-07-08:

- Zero references to `burkett-law.netlify.app` in production HTML (grep returned nothing across `*.html`, `includes/`, `practice-areas/`, `san-diego/`, `blog/`).
- Zero references to `localhost` or `127.0.0.1`.
- Zero `http://` references except schema.org / w3.org namespace URIs.
- 168 `childcustodyanddivorce.com` references across production HTML/txt/xml — every canonical URL points at the target domain.
- `robots.txt` Sitemap directive points at `https://childcustodyanddivorce.com/sitemap.xml`.
- `sitemap.xml` — every `<loc>` starts with `https://childcustodyanddivorce.com/`.
- All 55 production HTML files pass `scripts/run_all_validators.sh` (exit 0):
  - `validate_fabrication.py` — clean
  - `lint_cal_bar.py` — clean
  - `identity_guard.py` — clean
- Sample canonicals verified on 6 template categories (home, bio, contact, blog hub, practice pillar, location page) — all correct.
- 63 redirect lines in `_redirects` — Justia legacy URLs → new blog / practice-area / category targets.

## Runbook artifacts

Under `.planning/phases/07-cutover/`:
1. `CUTOVER-RUNBOOK.md` — T-14 through +72h execution runbook with per-step commands
2. `DNS-RECORDS.md` — exact records for Burkett to add at Network Solutions
3. `PRE-FLIGHT-QA.md` — 13-category T-7 checklist (55 pages, schema, forms, GA4, PSI, WCAG)
4. `07-VERIFICATION.md` — this file

## Verification checklist

- [x] Netlify custom domain added via API
- [x] Zero preview-URL leaks in production HTML
- [x] All validators pass on production HTML
- [x] Canonical URLs on 6 sampled template categories all target production domain
- [x] `_redirects` populated with Justia legacy map
- [x] Runbook covers T-14 → +72h with verification commands
- [x] Human action items broken out for Burkett vs Brian
- [x] Rollback plan documented (usable through 2026-07-30, disabled after Justia sunset)

## Blocked-on-human items (execution-day only)

These will be checked at their respective T-X gates, not now:

- [ ] Burkett lowers Network Solutions TTL to 300s at T-14
- [ ] Burkett adds GSC TXT record at T-14 (Brian provides token)
- [ ] Brian verifies GSC ownership after TXT propagates
- [ ] Burkett flips A + CNAME at cutover start
- [ ] Brian confirms HTTPS provisioning within cutover window
- [ ] +2h through +72h checks per runbook

---

**Phase 7 preparation is complete.** All artifacts are in place. Cutover day execution follows the runbook.
