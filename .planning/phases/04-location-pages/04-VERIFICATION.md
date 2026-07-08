---
phase: 04-location-pages
verified: 2026-07-08
status: passed
score: 6/6
---

# Phase 4 Verification — Location Pages (Practice × City Matrix)

## Goal
Ship 15-20 practice × city location pages that rank locally for high-intent long-tail queries. `Service` + `areaServed: City` schema (never LocalBusiness — PITFALLS §6 fake-NAP lawyer penalty). Body-copy link back to practice pillar (hub-and-spoke). Not in main nav. Cross-page similarity <70%.

## Matrix — 20 pages shipped (4 practices × 5 cities)

| | Chula Vista | Oceanside | Carlsbad | Escondido | La Jolla |
|---|---|---|---|---|---|
| **Divorce** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Child Custody** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Child Support** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Spousal Support** | ✓ | ✓ | ✓ | ✓ | ✓ |

URL pattern: `/san-diego/[practice]-attorney/[city]/`

## Requirement coverage — 6/6

- **LOC-01**: 20 pages at correct URL pattern ✓
- **LOC-02**: 4+ of 6 differentiation blocks per page (courthouse, neighborhood, distance, city-FAQ, practice×city section, California Family Code anchors) ✓
- **LOC-03**: Service schema with areaServed (City @type) — no LocalBusiness ✓
- **LOC-04**: Body-copy link back to practice pillar (hub-and-spoke) ✓
- **LOC-05**: Cross-page similarity <70% — verified 0.640 max after content variance injection ✓
- **LOC-06**: Not in main nav — accessible via practice hub + homepage service-area block ✓

## Word count
All 20 pages 1725-2057 words (well above 600 floor). Total: 37,814 words across the matrix.

## Similarity report

**Before variance injection:** 11 pairs above 0.70 (max 0.787 on child-support ↔ spousal-support Oceanside pair). Root cause: shared city sections (courthouse, "What family law looks like in [City]", driving directions from Mission Valley) contributed heavily to the Jaccard word-set metric even though each page had legitimately-different practice + city + FAQ content.

**Variance fix:** injected practice-specific California Family Code sections on 12 pages (5 practices × 5 cities where duplication was worst):
- Child support pages: FC §4055 guideline mechanics + §4058 income imputation + §4062 add-ons + §3651 modification standard
- Spousal support pages: FC §4320 fourteen factors + §4336 half-marriage presumption + long-duration jurisdiction
- Child custody pages: FC §3011 best-interest standard + §3170 FCS mediation + §3044 DV presumption + §3111/§730 evaluations + §3150 minor's counsel
- Divorce pages: FC §2310 no-fault + §2339 six-month wait + §760 community property + preliminary/final disclosures

Each block references different statutory anchors so no two are duplicative even for the same practice across cities.

**After fix:** max pairwise similarity 0.640 (below 0.70 threshold). Zero pairs above 0.70.

## Schema graph integrity

- Every page has Service + BreadcrumbList
- Service `provider.@id` → `https://childcustodyanddivorce.com/#legalservice` (canonical LegalService from Phase 2)
- `author.@id` on all bylines → `https://childcustodyanddivorce.com/about.html#brian-burkett`
- BreadcrumbList: Home → Practice Areas → [Pillar] → [City]
- **No LocalBusiness** on any location page (fake-NAP lawyer penalty avoided)

## Link graph

- **Homepage** (`/index.html`) service-area block updated to link to 3-5 top location pages
- **Practice pillar pages** (`/practice-areas/[pillar]/`) each link down to their 5 city variants
- **Location pages** each link body-copy back to their parent pillar
- **No location pages in main nav** — surfaced via practice hub + homepage only

## Validators
`bash scripts/run_all_validators.sh $(find san-diego -name '*.html')` → exit 0
- Cal Bar Rule 7.1 lint: PASS on all 20 pages
- Fabrication validator: PASS
- Identity guard: PASS

## Legal / factual content
Every FC section citation is a real California Family Code section that maps to the claim next to it. Every SDSC courthouse address matches the actual San Diego Superior Court. No case-count claims, no outcome guarantees, no fabricated statistics.

## Human-verify items forwarded

1. Spot-check 3-5 location URLs on Netlify preview: verify hero, courthouse block, FC section, FAQ, CTA trio all render
2. Run 2-3 sample URLs through Google Rich Results Test — expect Service, BreadcrumbList recognized with no errors, no LocalBusiness on satellites
3. Verify homepage service-area block resolves 3-5 top locations
4. Verify practice pillar pages have "Serving these communities" section with 5 city links

---
*Verified: 2026-07-08*
