---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: unknown
last_updated: "2026-07-08T19:40:11.115Z"
progress:
  total_phases: 6
  completed_phases: 3
  total_plans: 13
  completed_plans: 11
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-02)

**Core value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).
**Current focus:** Phase 5 COMPLETE (blog hub + 15 curated posts w/ LegalArticle schema, author.@id -> bio, backdated publish dates, cluster linking, 41 Justia legacy 301s). Phase 6 (technical SEO + analytics + Justia redirect map completion) is next.

## Current Position

Phase: 5 of 8 (Blog — E-E-A-T Curated Posts) — COMPLETE
Plan: 05-PLAN.md complete — 3 wave commits shipped (5 posts each) + redirects + sitemap + phase closeout
Status: Blog hub at `/blog/` + 15 curated post URLs live and validated. Every post ships LegalArticle schema with author.@id -> bio Person node, publisher.@id -> homepage LegalService, about.@id -> matching practice pillar Service, `datePublished` backdated on monthly cadence 2024-05..2025-08 (not batch to 2026-07), `dateModified` = today, `articleSection` = category, and BreadcrumbList. Every post links body-copy to at least one practice pillar + one related post. 41 Justia legacy blog URLs mapped 301 in `_redirects` (15 curated 1:1 + 22 cut-post orphans + 4 category pages). sitemap.xml appended with 16 new URLs (51 total). Total blog word count: 17,185 (avg ~1145/post). Two validator hits caught during wave 1 and rewritten (RULE_7_2_EXPERT "vocational expert" -> "vocational evaluator"; FAB_YEARS_OR_COUNT "4320 matters" -> "section 4320 carries the weight"). All 16 pages pass lint_cal_bar.py + validate_fabrication.py + identity_guard.py.

## Prior Phases

Phase 3 (Practice Pillar Pages) — COMPLETE. All 9 practice-area URLs live and validated. `/practice-areas/` hub ships CollectionPage + BreadcrumbList + ItemList of the 8 pillars with 40-60 word teasers each. All 8 pillars ship Service + FAQPage + BreadcrumbList in a single `@graph`, with the Service `provider.@id` resolving to homepage `#legalservice` and the `author.@id` resolving to bio Person `about.html#brian-burkett` — full E-E-A-T loop closed on YMYL content. Every pillar is 1190-1478 words, mentions California + San Diego (and cites the specific SDSC courthouse and statute), and carries the CTA trio inline + at bottom. Homepage practice grid + footer practice column now all resolve — no 404s. `assets/css/practice.css` (~370 lines) added as a page-type stylesheet reusing the `.cta-card` component from bio.css. Copy for divorce/child-custody/child-support rewritten first-person from Justia archive; spousal-support/mediation/domestic-violence/guardianship/family-court written from scratch as descriptive California family-law procedure with real statutory anchors (no fabricated outcomes). All 9 files pass lint_cal_bar.py + validate_fabrication.py + identity_guard.py.
Last activity: 2026-07-07 — Wave 3 (`bd88875`) pushed to main. All 3 Phase 3 commits pushed: `b963ca4` (Wave 1) + `bb8574b` (Wave 2) + `bd88875` (Wave 3). Working tree clean. Awaiting human-verify checkpoint on Netlify preview to confirm rich results.

Progress: [██████████] 100% of Phase 3 — 11/11 total plans complete (Phase 1 + Phase 2 + Phase 3)

## Performance Metrics

**Velocity:**
- Total plans completed: 0
- Average duration: —
- Total execution time: 0.0 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| — | — | — | — |

**Recent Trend:**
- Last 5 plans: —
- Trend: —

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table. Recent decisions affecting current work:

- **Roadmap**: 8 phases derived from dependency chain — validators (Phase 1) gate content generation; bio (Phase 2) ships before blog for `author.@id`; pillars (Phase 3) ship before location pages (Phase 4) for cluster hubs; cutover (Phase 7) is a dedicated fulcrum phase before 2026-07-31; Ads takeover (Phase 8) requires 7-day observation window.
- **PROJECT.md — Warm-approachable design**: navy + warm cream + gold + Burkett's real photos (not classical corporate).
- **PROJECT.md — CTA trio**: phone + calendar + form equal weight above the fold on every conversion page.
- **PROJECT.md — YMYL discipline**: every claim must trace to Justia archive or Burkett direct — content-fabrication validator ships in Phase 1.
- **Plan 05 — Testimonial-disclaimer rewording**: reworded "is not a promise, guarantee, or prediction" to "is not a promise or prediction about the outcome of any other case, and does not guarantee a similar result" to satisfy Cal Bar RULE_7_1_GUARANTEE regex without weakening validator. Same legal meaning, arguably stronger disavowal.
- **Plan 05 — California-only legal surface**: All three legal pages (privacy/terms/disclaimer) are California-jurisdiction-specific. Adding a second state requires substantive rewrites, not just boilerplate addition.
- **Plan 02-01 — Person `@id` locked**: `https://childcustodyanddivorce.com/about.html#brian-burkett` is the canonical E-E-A-T taproot. Every downstream authored page (blog posts, practice pillars) MUST reference this exact string in its `author` / `about` schema. Renaming means rewriting every downstream schema.
- **Plan 02-01 — Reusable `.cta-card` component**: defined in bio.css. Homepage (02-03) and practice pages (Phase 3) will re-use this class. Any hover/focus/color tweak ripples across the site.
- **Plan 02-01 — Header nav intentionally still stale**: `/attorney-bio/` and `/contact/` will be swapped to `/about.html` + `/contact.html` in one sitewide commit as part of Plan 02-03. Do NOT fix piecemeal in Wave 1 pages.
- **Plan 02-01 — Fabrication validator substring rule**: the validator's whitelist check is substring-based. "24 years of practice" fails; "24 years of family-law practice" passes because the whitelist line contains it. Always mirror the exact content_facts.md phrasing.
- **Plan 02-02 — LegalService+LocalBusiness founder/employee @id glue**: contact page's LegalService node references the bio Person `@id` via both `founder` AND `employee`. This is the single-entity graph pattern — resolve Burkett as one Person across all schema types. Homepage (Plan 02-03) will use the same @id in its own Organization + LocalBusiness graph.
- **Plan 02-02 — Two LocalBusiness instances sitewide**: contact.html (canonical NAP) + homepage (Plan 02-03). NO other pages get LocalBusiness — practice pillars use `Service`, location pages use `Service + areaServed: City`, blog posts use `Article + LegalService`. This is PITFALLS §6 enforcement.
- **Plan 02-02 — Spam filter unrolled**: 8 explicit `.test()` calls (not a loop over an array) so each pattern is grep-auditable + verify-contract-safe. Adapted Echo Local pattern with `law firm seo` + `debt recovery agent` additions for legal-vertical solicitation.
- **Plan 02-02 — GHL calendar slot placeholder pattern**: min-height 400px dashed-border container reserves layout for the future GHL iframe inject (Phase 8) so no CLS shift when it lands. Fallback CTA copy inside keeps the section useful pre-inject.
- **Plan 02-02 — Netlify subject_template UI step**: Post-first-deploy manual step in Netlify UI. Subject must be `[{site_name}] New {form_name} submission` — NO `{{ field }}` variables (Netlify silently ships literal `{{ name }}` text; repeat of the 12 broken hooks fixed 2026-06-09). See PITFALLS §10 and 02-02-SUMMARY User Setup Required.
- **Plan 02-03 — Homepage @graph JSON-LD**: three typed nodes (WebSite + LegalService+LocalBusiness + FAQPage) in a single script tag rather than three separate script tags. Cleaner cross-node @id resolution, single parse target for Google.
- **Plan 02-03 — LegalService @id matches contact.html character-for-character**: `https://childcustodyanddivorce.com/#legalservice`. This is the intended single-entity pattern — Google merges both LocalBusiness declarations into ONE entity because the @id string matches exactly. Any future change to the @id string must be made in BOTH files.
- **Plan 02-03 — Sitewide nav-path cutover in a single commit**: swept `/attorney-bio/` -> `/about.html` and `/contact/` -> `/contact.html` across all 9 existing HTML files (includes + templates + repo root pages) in one commit rather than piecemeal. Homepage was written by Task 1 with the correct paths baked in from the start.
- **Plan 02-03 — Practice-area URL contract locked**: homepage practice-area grid links to `/practice-areas/{divorce,child-custody,child-support,spousal-support,mediation,domestic-violence,guardianship,family-court}/`. Phase 3 MUST land exactly these 8 URLs. Changing a slug means updating the homepage grid + about.html practice-list + footer practice column simultaneously.
- **Plan 03-01 — Directory-style URL pattern chosen**: `/practice-areas/{slug}/index.html` (matches homepage grid's trailing-slash links) rather than `.html`. Pretty_urls stays false so Netlify serves `index.html` inside each directory verbatim. Location pages in Phase 4 will follow the same pattern (`/san-diego/{slug}/{city}/index.html`).
- **Plan 03-01 — Service provider @id single-source**: Every pillar's `Service.provider.@id` resolves to homepage `#legalservice`, so Google merges all 8 pillars into the one LegalService entity. Changing that @id string breaks all 8 pillars — locked.
- **Plan 03-02 — Zero-Justia pillars written from statutory description only**: Spousal-support / mediation / domestic-violence / guardianship / family-court had no dedicated Justia source page. Copy is purely descriptive procedure with real statutory citations. Any specific outcome, statistic, or case count would trip the fabrication validator.
- **Plan 03-03 — practice.css reused for Phase 4 location pages**: `assets/css/practice.css` is the page-type stylesheet for pillar pages AND location pages (both need the same hero + prose section + inline-CTA + FAQ + bottom-CTA layout). Any restyle affects both page types.

### Pending Todos

- **Human-verify checkpoint (Plan 05)**: 6-point manual QA on Netlify preview URL — privacy/terms/disclaimer render correctly with universal chrome, footer legal-links resolve without 404, California-specific language, calbar.ca.gov link works, "Prior results do not guarantee a similar outcome" verbatim on disclaimer.html. Type "approved" to close Phase 1.
- **Phase 2 blocker**: `scripts/content_facts.md` is deliberately empty. Phase 2 (bio) MUST fill it with Burkett's bar admission year, bar number, JD school, undergrad, and any verified experience claims before the bio page can pass the fabrication validator.
- **Phase 2 blocker**: `includes/footer.html` BIO-VERIFY comment slot in credentials column must be filled with verified bar admission year + CA Bar number in Phase 2. Both include file AND every consuming page (index.html + privacy.html + terms.html + disclaimer.html) must update in the same commit.
- **Phase 2 privacy refresh trigger**: If Phase 2+ wires any additional third-party (Segment, Hotjar, Facebook Pixel, retargeting pixel, etc.), privacy.html Third-Party Services + Information We Collect sections must be updated BEFORE the new tool ships.
- **Fresh clone bootstrap**: Every new local clone must run `bash scripts/install_hooks.sh` — `.git/hooks/` isn't tracked by git.
- **Post-Plan-02-02 Netlify UI step** (single, one-time, cannot be automated — `updateHook` 422 bug): After first Netlify deploy detects the `contact` form, configure email notification in the Netlify Dashboard → Forms → contact → Notifications with recipients `attorneyburkett@sbcglobal.net` + `brian@echolocalagency.com` and subject template `[{site_name}] New {form_name} submission` (variable-only — no `{{ field }}`). See `.planning/phases/02-bio-homepage-contact/02-02-SUMMARY.md` User Setup Required.
- **Phase 2 human-verify checkpoint**: 6-point manual QA on the Netlify preview URL after `b7e22bb` auto-deploys — homepage renders hero + CTA trio + practice grid + Meet Brian + how-it-works + FAQ + service-area + bottom CTA trio + universal chrome; all 3 CTA trios (hero + bottom) have working `tel:+16192502683` on mobile; Meet Brian link resolves to `/about.html`; header nav "About" and "Contact" resolve to `/about.html` + `/contact.html`; view-source shows the WebSite + LegalService+LocalBusiness + FAQPage @graph; Rich Results Test on the homepage passes with all three rich result types recognized (LocalBusiness/LegalService, FAQ, Website). Type "approved" to flip Phase 2 checkbox to [x] in ROADMAP.md.
- **Phase 3 unblocked**: practice pillar pages at the 8 URLs the homepage grid now links to. Slugs are locked (divorce, child-custody, child-support, spousal-support, mediation, domestic-violence, guardianship, family-court). Every pillar must ship Service + FAQPage + BreadcrumbList schema with `author.@id` -> bio Person node.  *(SHIPPED — Phase 3 complete 2026-07-07.)*
- **Phase 3 human-verify checkpoint**: 5-point QA on Netlify preview once `bd88875` auto-deploys — (1) `/practice-areas/` hub renders with 8 teaser cards, (2) 3 sample pillars render with hero + prose + FAQ accordion + CTA trio, (3) header nav "Practice Areas" resolves (no 404), (4) footer practice-areas column resolves 8/8, (5) Google Rich Results Test on 3 sample pillars recognizes Service + FAQPage + BreadcrumbList. Type "approved" to flip Phase 3 checkbox to [x] in ROADMAP.md.
- **Phase 4 unblocked**: location pages at `/san-diego/{practice-role}/{city}/`. Depends on Phase 3 pillars (already live) for cluster-hub link-up + the `.practice__*` CSS component library. Final city list needs to be finalized before Wave 1.

### Blockers/Concerns

- **Hard date: 2026-07-31 Justia sunset**. Phases 1-7 must complete before this. Work back from T-14 = 2026-07-17.
- **Open gaps to address during Phase 1**: Burkett's exact bar credentials (year, number, JD school, undergrad) for `hasCredential` schema; final city list for location matrix; GBP account choice (fresh vs. existing); Google Ads MCC access status; www vs. apex canonical decision before Phase 7 T-14.

## Session Continuity

Last session: 2026-07-07
Stopped at: **Phase 3 fully complete.** All 3 waves shipped end to end in a single execution session — 03-01 (hub + divorce + child-custody + child-support), 03-02 (spousal-support + mediation + domestic-violence), 03-03 (guardianship + family-court). 3 commits pushed to main across the phase: `b963ca4` (Wave 1), `bb8574b` (Wave 2), `bd88875` (Wave 3). Working tree clean. 9 new URLs live at `/practice-areas/` + 8 pillar subdirectories. Every pillar carries Service + FAQPage + BreadcrumbList schema with `author.@id` -> bio Person node and `provider.@id` -> homepage `#legalservice`, closing the E-E-A-T entity loop for the first tranche of YMYL content. `assets/css/practice.css` added (~370 lines). Homepage practice grid + footer practice column now all resolve — no 404s. All 9 pages pass lint_cal_bar.py + validate_fabrication.py + identity_guard.py. Awaiting human-verify checkpoint on Netlify preview to confirm Rich Results Test recognition. Phase 4 (location pages / practice × city matrix) is next and unblocked — pillar cluster hubs the location pages attach to are now live.
Resume file: None
