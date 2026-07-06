---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: in_progress
last_updated: "2026-07-06T18:15:00.000Z"
progress:
  total_phases: 8
  completed_phases: 2
  total_plans: 8
  completed_plans: 8
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-02)

**Core value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).
**Current focus:** Phase 2 COMPLETE (all 3 plans shipped). Phase 3 (practice pillar pages) is next and unblocked.

## Current Position

Phase: 2 of 8 (Bio + Homepage + Contact) — COMPLETE
Plan: 02-01 complete, 02-02 complete, 02-03 complete (Wave 2 shipped)
Status: All three E-E-A-T pillars of Phase 2 are live. `/about.html` carries the canonical Person `@id` = `https://childcustodyanddivorce.com/about.html#brian-burkett`. `/contact.html` + `/index.html` both carry the LegalService+LocalBusiness JSON-LD node with matching `@id` = `https://childcustodyanddivorce.com/#legalservice` (character-for-character single-entity resolution). founder + employee on both LegalService nodes reference the bio Person `@id` — full entity-graph loop closed across bio + homepage + contact. Homepage @graph adds WebSite + FAQPage. Sitewide nav paths cut over from Phase 1 placeholders (`/attorney-bio/`, `/contact/`) to real Phase 2 URLs (`/about.html`, `/contact.html`) across 9 HTML files in a single sweep commit.
Last activity: 2026-07-06 — Plan 02-03 complete: `index.html` (450 lines replacing Phase 1 placeholder; hero + CTA trio + 8-card practice-area grid linking to `/practice-areas/{slug}/` for Phase 3 to fulfill + Meet Brian teaser + 4-step how-it-works + 6-Q FAQ (visible details + FAQPage schema mirroring verbatim) + San Diego service-area block + bottom CTA trio on navy; @graph JSON-LD with WebSite + LegalService+LocalBusiness + FAQPage nodes), `assets/css/home.css` (487 lines, tokenized, prefers-reduced-motion gated), and sitewide nav-path sweep across 9 files (includes/header.html, includes/footer.html, templates/base.html, privacy.html, terms.html, disclaimer.html, about.html, contact.html, thanks.html). sitemap.xml root lastmod refreshed to 2026-07-06. Three validators pass on every touched HTML file. Commit `b7e22bb` pushed to main. Prior waves: 02-01 (`6776e4a` + `4477b65` + `1997228`) + 02-02 (`23df8f2` + `c647449` + `90a9067`).

Progress: [██████████] 100% of Phase 2 — 8/8 total plans complete (Phase 1 + Phase 2)

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

### Pending Todos

- **Human-verify checkpoint (Plan 05)**: 6-point manual QA on Netlify preview URL — privacy/terms/disclaimer render correctly with universal chrome, footer legal-links resolve without 404, California-specific language, calbar.ca.gov link works, "Prior results do not guarantee a similar outcome" verbatim on disclaimer.html. Type "approved" to close Phase 1.
- **Phase 2 blocker**: `scripts/content_facts.md` is deliberately empty. Phase 2 (bio) MUST fill it with Burkett's bar admission year, bar number, JD school, undergrad, and any verified experience claims before the bio page can pass the fabrication validator.
- **Phase 2 blocker**: `includes/footer.html` BIO-VERIFY comment slot in credentials column must be filled with verified bar admission year + CA Bar number in Phase 2. Both include file AND every consuming page (index.html + privacy.html + terms.html + disclaimer.html) must update in the same commit.
- **Phase 2 privacy refresh trigger**: If Phase 2+ wires any additional third-party (Segment, Hotjar, Facebook Pixel, retargeting pixel, etc.), privacy.html Third-Party Services + Information We Collect sections must be updated BEFORE the new tool ships.
- **Fresh clone bootstrap**: Every new local clone must run `bash scripts/install_hooks.sh` — `.git/hooks/` isn't tracked by git.
- **Post-Plan-02-02 Netlify UI step** (single, one-time, cannot be automated — `updateHook` 422 bug): After first Netlify deploy detects the `contact` form, configure email notification in the Netlify Dashboard → Forms → contact → Notifications with recipients `attorneyburkett@sbcglobal.net` + `brian@echolocalagency.com` and subject template `[{site_name}] New {form_name} submission` (variable-only — no `{{ field }}`). See `.planning/phases/02-bio-homepage-contact/02-02-SUMMARY.md` User Setup Required.
- **Phase 2 human-verify checkpoint**: 6-point manual QA on the Netlify preview URL after `b7e22bb` auto-deploys — homepage renders hero + CTA trio + practice grid + Meet Brian + how-it-works + FAQ + service-area + bottom CTA trio + universal chrome; all 3 CTA trios (hero + bottom) have working `tel:+16192502683` on mobile; Meet Brian link resolves to `/about.html`; header nav "About" and "Contact" resolve to `/about.html` + `/contact.html`; view-source shows the WebSite + LegalService+LocalBusiness + FAQPage @graph; Rich Results Test on the homepage passes with all three rich result types recognized (LocalBusiness/LegalService, FAQ, Website). Type "approved" to flip Phase 2 checkbox to [x] in ROADMAP.md.
- **Phase 3 unblocked**: practice pillar pages at the 8 URLs the homepage grid now links to. Slugs are locked (divorce, child-custody, child-support, spousal-support, mediation, domestic-violence, guardianship, family-court). Every pillar must ship Service + FAQPage + BreadcrumbList schema with `author.@id` -> bio Person node.

### Blockers/Concerns

- **Hard date: 2026-07-31 Justia sunset**. Phases 1-7 must complete before this. Work back from T-14 = 2026-07-17.
- **Open gaps to address during Phase 1**: Burkett's exact bar credentials (year, number, JD school, undergrad) for `hasCredential` schema; final city list for location matrix; GBP account choice (fresh vs. existing); Google Ads MCC access status; www vs. apex canonical decision before Phase 7 T-14.

## Session Continuity

Last session: 2026-07-06
Stopped at: **Phase 2 fully complete.** All 3 plans (02-01 bio, 02-02 contact/thanks/form, 02-03 homepage + nav cutover) shipped. 7 commits pushed to main across the phase (`6776e4a`, `4477b65`, `1997228`, `23df8f2`, `c647449`, `90a9067`, `b7e22bb`). Working tree clean. Entity graph closed sitewide: bio Person `@id` = `https://childcustodyanddivorce.com/about.html#brian-burkett`; LegalService+LocalBusiness `@id` = `https://childcustodyanddivorce.com/#legalservice` (duplicated character-for-character across index.html and contact.html so Google resolves one entity); homepage @graph adds WebSite + FAQPage. All 9 existing HTML files at repo root + includes + templates have the Phase 2 real URLs. Awaiting human-verify checkpoint on Netlify preview to flip Phase 2 checkbox to [x] in ROADMAP.md. Phase 3 (practice pillar pages) is next and unblocked — the 8 URLs the homepage grid points at are the URLs Phase 3 must fulfill.
Resume file: None
