# Plan 03-03 SUMMARY — Wave 3: Guardianship + Family Court

**Status**: Complete
**Commit**: `bd88875`
**Pushed**: origin/main

## Shipped
- `/practice-areas/guardianship/index.html` — 1410 words
- `/practice-areas/family-court/index.html` — 1478 words
- `sitemap.xml` — 2 new URLs added

## Statutory anchors used
- **Guardianship**: Probate Code §§ 1500-1611 (probate guardianship of a minor); § 1514(b) (best interest); § 1511 (notice); Family Code § 3041 (parental detriment); Welfare & Institutions Code § 360 (juvenile guardianship inside dependency); San Diego Probate Court Investigator role
- **Family Court**: California Rules of Court 5.151 (ex parte); Code of Civil Procedure § 1005 (noticed-hearing service timing); Form FL-300 (RFO); Form FL-180 (judgment); California 4th District Court of Appeal, Div One (San Diego appellate venue); all four SDSC family-law courthouses with addresses (Central 1100 Union St, Vista 325 South Melrose, El Cajon 250 East Main, Chula Vista 500 Third Ave)

## Schema
Service + FAQPage + BreadcrumbList in single @graph. FAQ verbatim vs `<details>`. Author @id → `about.html#brian-burkett`.

## Validators
Both pages pass lint_cal_bar.py + validate_fabrication.py + identity_guard.py.

## Notes
- Homepage practice grid links `/practice-areas/guardianship/` and `/practice-areas/family-court/` now resolve — grid is fully wired.
- Family Court page functions as a fallback/navigation pillar for matters that do not neatly fit any other pillar or span multiple. Explicit "which courthouse hears my case" section maps residential geography to courthouse jurisdiction.
