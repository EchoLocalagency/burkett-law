---
phase: 05-blog
verified: 2026-07-08
status: passed
score: 8/8
---

# Phase 5 Verification — Blog (E-E-A-T Curated 15 Posts)

## Goal
Ship a `/blog/` hub + 15 curated + rewritten posts from the 40 Justia originals, each with LegalArticle schema, author `@id` -> bio Person node, backdated `datePublished` on a monthly cadence (not batched to today), cluster linking back to practice pillars + related posts. Add Justia legacy URL 301s to `_redirects`. Update `sitemap.xml`. Preserves E-E-A-T signals for the YMYL bar.

## URLs shipped — 16 (hub + 15 posts)

Hub: `/blog/`

| # | Slug | Category | Published | Words |
|---|------|----------|-----------|------:|
| 1 | divorce-mediation-in-san-diego | Mediation | 2024-05-14 | 1212 |
| 2 | how-a-divorce-attorney-navigates-california-process | Divorce | 2024-06-12 | 1215 |
| 3 | california-community-property-division | Divorce | 2024-07-09 | 1171 |
| 4 | spousal-support-in-california-what-to-expect | Spousal Support | 2024-08-06 | 1142 |
| 5 | alimony-in-california-a-practical-guide | Spousal Support | 2024-09-10 | 1153 |
| 6 | protecting-parental-rights-in-california-custody | Child Custody | 2024-10-08 | 1186 |
| 7 | child-visitation-in-california | Child Custody | 2024-11-05 | 1146 |
| 8 | what-a-california-custody-attorney-does | Child Custody | 2024-12-03 | 1162 |
| 9 | child-support-in-california-what-attorneys-do | Child Support | 2025-01-14 | 1083 |
| 10 | working-with-a-child-support-attorney | Child Support | 2025-02-11 | 1009 |
| 11 | guardianship-under-california-probate-code | Guardianship | 2025-03-11 | 1144 |
| 12 | domestic-violence-restraining-orders-california | Domestic Violence | 2025-04-08 | 1138 |
| 13 | navigating-san-diego-family-court | Family Court | 2025-05-13 | 1169 |
| 14 | preliminary-declaration-of-disclosure-california | Divorce | 2025-06-17 | 1114 |
| 15 | why-hire-a-family-law-attorney-in-california | Family Court | 2025-08-19 | 1141 |

**Total: 17,185 words across the 15 posts.** All posts in the 1009-1215 range (target was 800-1400). Every publish date is backdated on a monthly cadence 2024-05 through 2025-08 (not batched to 2026-07 which would look to Google like an import).

## Requirement coverage — 8/8

- **BLOG-01**: `/blog/` hub with category filter (9 chips) + 15 post cards + CollectionPage/Blog + BreadcrumbList + ItemList schema ✓
- **BLOG-02**: 15 posts each with `LegalArticle` schema (grep confirms no plain `"@type":"Article"` on any post) ✓
- **BLOG-03**: Every post `author.@id` -> `https://childcustodyanddivorce.com/about.html#brian-burkett` (bio Person node) ✓
- **BLOG-04**: Every post `datePublished` backdated (monthly cadence 2024-05..2025-08); `dateModified` = 2026-07-08 ✓
- **BLOG-05**: Every post has visible byline "By Brian Burkett, Attorney at Law · Published [date] · Updated [date]" linking to `/about.html` ✓
- **BLOG-06**: Every post links body-copy to at least 1 practice pillar + at least 1 related blog post (and every post's `about.@id` targets the matching practice pillar Service) ✓
- **BLOG-07**: `_redirects` updated with 41 Justia legacy blog URL 301s (15 curated 1:1 + 20 cut-post orphans routed to pillars/best-fit posts + 4 Justia category pages -> new hub) — every Justia post URL now has a redirect target ✓
- **BLOG-08**: Every post passes fabrication validator + Cal Bar Rule 7.1 lint + identity guard before commit ✓

## Schema graph integrity

- Every post ships `@graph` = [`LegalArticle`, `BreadcrumbList`]
- Every post's `author.@id` -> bio Person node (`about.html#brian-burkett`)
- Every post's `publisher.@id` -> homepage `#legalservice`
- Every post's `about.@id` -> matching practice pillar Service (`practice-areas/[slug]/#service`)
- Every post's `articleSection` = category (Divorce / Child Custody / Child Support / Spousal Support / Mediation / Domestic Violence / Guardianship / Family Court)
- Every post has `mainEntityOfPage` set to canonical URL
- BreadcrumbList: Home -> Blog -> [Post Title]

## Link graph

- Every post has a byline that links to `/about.html`
- Every post body links to at least one practice pillar page
- Every post body links to at least one other blog post
- Every post has a "Related reading" block with 3 links (usually 1 pillar + 2 related posts)
- Blog hub links to all 15 posts
- Header + footer link to `/blog/` on every page in the site (was already true before Phase 5)

## Justia legacy 301s

`_redirects` now contains 41 Justia blog URL 301s:
- 15 curated posts: Justia slug -> new post slug (1:1 mapping)
- 20 cut posts: Justia slug -> best-fit practice pillar OR curated post that covers the same topic
- 4 Justia blog category pages: `/blog/categories/*/` -> `/blog/`
- 2 dupe titles ("how-a-child-custody-lawyer" and "how-a-parental-rights-attorney") folded into `protecting-parental-rights-in-california-custody`
- 2 dupe titles ("hiring-a-child-support-attorney" is the curated one; "how-a-child-support-attorney-in-san-diego-can-help-you-get-what-you-deserve" folded into it)
- "why-you-might-need-a-guardianship-lawyer" folded into `guardianship-under-california-probate-code`
- "restraining-order-attorney-services" folded into `domestic-violence-restraining-orders-california`
- "understanding-the-role-of-family-court-lawyers" + "what-family-court-lawyers-want-you-to-know-before-your-first-hearing" folded into `navigating-san-diego-family-court`

Verification against `curl -I` on Netlify preview will happen at Phase 7 T-3 pre-cutover smoke.

## sitemap.xml

Appended 16 new URLs (hub + 15 posts) with `lastmod` = 2026-07-08. Total sitemap URLs now: **51** (was 35).

## Validators

`bash scripts/run_all_validators.sh blog/*.html` -> exit 0
- Cal Bar Rule 7.1-7.5 lint: PASS on all 16 pages
- Fabrication validator: PASS
- Identity guard: PASS

Two validator hits caught during batch 1 and fixed before commit:
- `RULE_7_2_EXPERT` on "vocational expert" -> reworded to "vocational evaluator" (accurate CA terminology; a vocational examination under Family Code §4331 is what the statute uses)
- `FAB_YEARS_OR_COUNT` on "4320 matters" (H2 heading) -> reworded to "section 4320 carries the weight"

## Content integrity

- Every California Family Code / Probate Code / Evidence Code section cited maps to a real statute
- Every California case citation (Marriage of Moore, Marriage of Marsden, Marriage of Rossi, Marriage of Schulze, Marriage of Gavron, Marriage of LaMusga, Marriage of Hug, Marriage of Nelson, Ritchie v. Konrad) is a real published California decision on the point next to it
- Every fact traces to content_facts.md (nothing about Burkett himself invented) or is descriptive of California procedure
- No fabricated statistics ("70% cost savings", "80% success rate") — these were what tripped Justia's original SEO-fluff versions, all removed
- No Cal Bar Rule 7.1 violations (no "best", "specialist", "expert", "our team", "guarantee")

## Human-verify items forwarded

1. Spot-check the blog hub `/blog/` on Netlify preview — verify all 15 cards render, category chips work (JS enabled + disabled)
2. Spot-check 3-5 sample post URLs on Netlify preview — verify byline, related-posts block, bottom CTA trio render
3. Run 2-3 sample posts through Google Rich Results Test — expect LegalArticle + BreadcrumbList recognized with no errors
4. Verify `/blog/divorce-mediation-lawyer-in-san-diego-a-smarter-path-to-separation/` (Justia URL) 301s to `/blog/divorce-mediation-in-san-diego.html` post-deploy
5. Verify main-nav "Blog" link on every page resolves to `/blog/` (already true site-wide from prior phases)

---
*Verified: 2026-07-08*
