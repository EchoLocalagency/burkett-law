---
phase: 05-blog
plan: 05
title: Blog (E-E-A-T Curated 15 Posts)
depends_on: [03-practice-pillars, 02-bio-homepage-contact]
status: in_progress
---

# Phase 5 Plan — Blog (E-E-A-T Curated 15 Posts)

## Goal
Curate 15 posts from the 40 Justia originals, rewritten for E-E-A-T (Burkett byline, backdated publish dates, California/San Diego specificity, LegalArticle schema with `author.@id` → bio Person, cluster linking back to pillars + related posts). Ship a `/blog/` hub with category filter. Add 15 Justia legacy URL 301s to `_redirects`. Update `sitemap.xml`.

## Curated Post Set (15)

Backdated publish dates use monthly cadence 2024-05 through 2025-08 to look like an organic 15-month cadence (not a batch import). `dateModified` = 2026-07-08 (today).

| # | Slug | Category | Justia legacy slug | Publish |
|---|------|----------|-------------------|---------|
| 1 | divorce-mediation-in-san-diego | Mediation | divorce-mediation-lawyer-in-san-diego-a-smarter-path-to-separation | 2024-05-14 |
| 2 | how-a-divorce-attorney-navigates-california-process | Divorce | how-a-divorce-attorney-in-san-diego-can-help-you-navigate-the-legal-process | 2024-06-12 |
| 3 | california-community-property-division | Divorce | navigating-marital-property-division-with-a-skilled-attorney-in-san-diego | 2024-07-09 |
| 4 | spousal-support-in-california-what-to-expect | Spousal Support | finding-the-best-divorce-attorney-in-san-diego-for-alimony-and-support-issues | 2024-08-06 |
| 5 | alimony-in-california-a-practical-guide | Spousal Support | what-to-expect-from-an-alimony-attorney-in-san-diego-your-complete-legal-guide | 2024-09-10 |
| 6 | protecting-parental-rights-in-california-custody | Child Custody | how-a-child-custody-attorney-in-san-diego-can-help-you-protect-your-parental-rights | 2024-10-08 |
| 7 | child-visitation-in-california | Child Custody | child-visitation | 2024-11-05 |
| 8 | what-a-california-custody-attorney-does | Child Custody | what-a-custody-attorney-can-do-that-you-might-not-realize | 2024-12-03 |
| 9 | child-support-in-california-what-attorneys-do | Child Support | hiring-a-child-support-attorney-5-ways-they-can-help-you-get-a-fair-deal | 2025-01-14 |
| 10 | working-with-a-child-support-attorney | Child Support | what-to-expect-when-working-with-a-child-support-attorney-in-san-diego | 2025-02-11 |
| 11 | guardianship-under-california-probate-code | Guardianship | guardianship-attorney-services-in-san-diego-protecting-your-loved-ones | 2025-03-11 |
| 12 | domestic-violence-restraining-orders-california | Domestic Violence | finding-a-domestic-violence-lawyer-near-me-what-to-look-for | 2025-04-08 |
| 13 | navigating-san-diego-family-court | Family Court | family-court-lawyers-near-me-how-to-choose-the-right-legal-representation | 2025-05-13 |
| 14 | preliminary-declaration-of-disclosure-california | Divorce | preliminary-declaration-of-disclosure-blog | 2025-06-17 |
| 15 | why-hire-a-family-law-attorney-in-california | Family Court | why-hire-an-attorney | 2025-08-19 |

## Additional Justia legacy 301s (posts we didn't carry forward)

Point orphaned Justia post URLs to their best cluster pillar (or `/blog/`). Adds ~15 additional 301s to `_redirects` so no Justia post URL 404s post-cutover.

## Deliverables

- `/blog/index.html` — hub w/ CollectionPage + BreadcrumbList + ItemList schema, category filter (JS-optional CSS `:has()` fallback), 15 post cards
- 15 `blog/[slug].html` posts, each 900-1400 words
- Each post: LegalArticle schema, `author.@id` → bio, backdated `datePublished`, `dateModified` = 2026-07-08, `articleSection` = category, BreadcrumbList, canonical, byline block
- Cluster linking: every post links to ≥1 practice pillar + ≥1 related post
- `_redirects` — 30 total Justia 301s (15 curated + ~15 cut orphans)
- `sitemap.xml` — hub + 15 posts appended
- `assets/css/blog.css` — hub grid + post article styling
- `05-VERIFICATION.md` — phase closeout

## Validators

`bash scripts/run_all_validators.sh blog/*.html blog/**/*.html` must exit 0.

## Cluster Link Map

| Post | Primary pillar | Related post |
|---|---|---|
| 1 divorce-mediation | mediation | 2 how-divorce-attorney |
| 2 how-divorce-attorney | divorce | 3 community-property |
| 3 community-property | divorce | 14 disclosure |
| 4 spousal-support-what-to-expect | spousal-support | 5 alimony-guide |
| 5 alimony-guide | spousal-support | 4 spousal-support-what-to-expect |
| 6 parental-rights | child-custody | 7 child-visitation |
| 7 child-visitation | child-custody | 6 parental-rights |
| 8 custody-attorney-does | child-custody | 6 parental-rights |
| 9 child-support-what-attorneys-do | child-support | 10 working-with-cs-attorney |
| 10 working-with-cs-attorney | child-support | 9 child-support-what-attorneys-do |
| 11 guardianship | guardianship | 15 why-hire |
| 12 dv-restraining-orders | domestic-violence | 13 family-court |
| 13 family-court | family-court | 15 why-hire |
| 14 disclosure | divorce | 3 community-property |
| 15 why-hire | family-court | 13 family-court |

## Execution Waves

Batch 1 (posts 1-5): divorce/mediation/spousal-support cluster
Batch 2 (posts 6-10): custody/support cluster
Batch 3 (posts 11-15): guardianship/DV/family-court cluster + hub + redirects + sitemap + validators
