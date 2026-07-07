# Plan 03-02 SUMMARY — Wave 2: Spousal Support + Mediation + Domestic Violence

**Status**: Complete
**Commit**: `bb8574b`
**Pushed**: origin/main

## Shipped
- `/practice-areas/spousal-support/index.html` — 1223 words
- `/practice-areas/mediation/index.html` — 1278 words
- `/practice-areas/domestic-violence/index.html` — 1335 words
- `sitemap.xml` — 3 new URLs added

## Content-source note
None of these three areas had dedicated Justia archive pages. Copy is written from scratch as descriptive California family-law procedure — statutory and case-law anchors only, no fabricated outcomes or statistics.

## Statutory anchors used
- **Spousal Support**: Family Code §§ 3600 (temporary), 4320 (long-term factors), 4336 (long-duration marriages), 4337 (termination on remarriage/death); Gavron warning doctrine; DissoMaster guideline
- **Mediation**: Family Code § 3170 (mandatory FCS custody mediation), Evidence Code § 1119 (mediation confidentiality); three modes covered: FCS recommending mediation / private confidential mediation / attorney-as-neutral
- **Domestic Violence**: DVPA at Family Code §§ 6200-6460; § 6320 (coercive control 2020 amendments); § 3044 (rebuttable custody presumption); EPO/TRO/permanent DVRO procedure; firearm surrender under state + federal law

## Schema
Service + FAQPage + BreadcrumbList in single @graph on each pillar. FAQ text verbatim vs visible `<details>` answers. Author @id → `about.html#brian-burkett`.

## Validators
All three pages pass lint_cal_bar.py + validate_fabrication.py + identity_guard.py.

## Notes
- Homepage practice grid links `/practice-areas/spousal-support/`, `/mediation/`, `/domestic-violence/` now resolve.
- CTA trio present inline + at bottom on all three pages.
- Domestic Violence page carefully treats petitioner and respondent perspectives symmetrically — no advocacy language that would violate Cal Bar Rule 7.1.
