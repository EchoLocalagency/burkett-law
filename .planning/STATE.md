---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: in_progress
last_updated: "2026-07-06T17:15:00.000Z"
progress:
  total_phases: 8
  completed_phases: 1
  total_plans: 8
  completed_plans: 7
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-02)

**Core value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).
**Current focus:** Phase 2 in progress. Plans 02-01 (bio) + 02-02 (contact) shipped. Plan 02-03 (homepage) is Wave 2 next.

## Current Position

Phase: 2 of 8 (Bio + Homepage + Contact)
Plan: 02-01 complete, 02-02 complete, 02-03 next (Wave 2 — homepage + sitewide nav-path cutover)
Status: Bio taproot + contact/thanks conversion surface shipped. `/about.html` live with canonical Person `@id` = `https://childcustodyanddivorce.com/about.html#brian-burkett`. `/contact.html` carries the canonical LegalService+LocalBusiness JSON-LD (single NAP source) with `founder` + `employee` @id-referencing the bio Person node — entity-graph glue closed. Reusable `.cta-card` class shipped in both bio.css and contact.css (contact.css version acts as standalone fallback; bio.css loads first so cascade is safe).
Last activity: 2026-07-06 — Plan 02-02 complete: `contact.html` (391 lines, LegalService+LocalBusiness multi-type JSON-LD, canonical NAP block + map iframe + CTA trio + GHL calendar slot placeholder + Netlify form with 8 fields including honeypot + Cal Bar 7.1 disclaimer directly below submit), `thanks.html` (164 lines, noindex terminal + universal chrome + commented GA4 form_submit slot + commented AW conversion slot), `assets/js/form.js` (68 lines, 8 unrolled `.test()` spam checks + honeypot check, silent redirect to `/` on match), `assets/css/contact.css` (446 lines, tokenized, prefers-reduced-motion gated, includes standalone `.cta-card` fallback), sitemap.xml updated with `/contact.html`. Three validators pass on both new HTML files. Commits `23df8f2` + `c647449` + `90a9067` pushed to main. Prior wave 1: Plan 02-01 also complete (`6776e4a` + `4477b65` + `1997228`).

Progress: [███████░░░] 75%

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

### Pending Todos

- **Human-verify checkpoint (Plan 05)**: 6-point manual QA on Netlify preview URL — privacy/terms/disclaimer render correctly with universal chrome, footer legal-links resolve without 404, California-specific language, calbar.ca.gov link works, "Prior results do not guarantee a similar outcome" verbatim on disclaimer.html. Type "approved" to close Phase 1.
- **Phase 2 blocker**: `scripts/content_facts.md` is deliberately empty. Phase 2 (bio) MUST fill it with Burkett's bar admission year, bar number, JD school, undergrad, and any verified experience claims before the bio page can pass the fabrication validator.
- **Phase 2 blocker**: `includes/footer.html` BIO-VERIFY comment slot in credentials column must be filled with verified bar admission year + CA Bar number in Phase 2. Both include file AND every consuming page (index.html + privacy.html + terms.html + disclaimer.html) must update in the same commit.
- **Phase 2 privacy refresh trigger**: If Phase 2+ wires any additional third-party (Segment, Hotjar, Facebook Pixel, retargeting pixel, etc.), privacy.html Third-Party Services + Information We Collect sections must be updated BEFORE the new tool ships.
- **Fresh clone bootstrap**: Every new local clone must run `bash scripts/install_hooks.sh` — `.git/hooks/` isn't tracked by git.
- **Post-Plan-02-02 Netlify UI step** (single, one-time, cannot be automated — `updateHook` 422 bug): After first Netlify deploy detects the `contact` form, configure email notification in the Netlify Dashboard → Forms → contact → Notifications with recipients `attorneyburkett@sbcglobal.net` + `brian@echolocalagency.com` and subject template `[{site_name}] New {form_name} submission` (variable-only — no `{{ field }}`). See `.planning/phases/02-bio-homepage-contact/02-02-SUMMARY.md` User Setup Required.
- **Plan 02-03 nav-path cutover**: sitewide nav-link rewrite `/attorney-bio/` → `/about.html` and `/contact/` → `/contact.html` in `includes/header.html` + `includes/footer.html` + every deployed HTML page (index / privacy / terms / disclaimer / about / contact / thanks) in a SINGLE commit. Do not fix piecemeal.

### Blockers/Concerns

- **Hard date: 2026-07-31 Justia sunset**. Phases 1-7 must complete before this. Work back from T-14 = 2026-07-17.
- **Open gaps to address during Phase 1**: Burkett's exact bar credentials (year, number, JD school, undergrad) for `hasCredential` schema; final city list for location matrix; GBP account choice (fresh vs. existing); Google Ads MCC access status; www vs. apex canonical decision before Phase 7 T-14.

## Session Continuity

Last session: 2026-07-06
Stopped at: Completed BOTH Wave 1 plans of Phase 2 — Plan 02-01 (bio) and Plan 02-02 (contact + thanks + form). All 5 commits pushed to main (`6776e4a`, `4477b65`, `1997228`, `23df8f2`, `c647449`, `90a9067`). Working tree clean. Plan 02-03 (homepage + sitewide nav-path cutover from `/attorney-bio/` → `/about.html` and `/contact/` → `/contact.html`) is next — Wave 2, unblocked. Both Wave 1 pages ship with the correct Person `@id` anchor and the entity graph is now closed on the LegalService side (contact.html carries founder+employee references to about.html Person node).
Resume file: None
