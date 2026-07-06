---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: in_progress
last_updated: "2026-07-06T17:00:00.000Z"
progress:
  total_phases: 8
  completed_phases: 1
  total_plans: 8
  completed_plans: 6
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-02)

**Core value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).
**Current focus:** Phase 2 in progress. Plans 02-01 (bio) + 02-02 (contact) shipped. Plan 02-03 (homepage) is Wave 2 next.

## Current Position

Phase: 2 of 8 (Bio + Homepage + Contact)
Plan: 02-01 complete, 02-02 complete (parallel sibling), 02-03 next (Wave 2 — homepage + sitewide nav-path cutover)
Status: Bio taproot shipped. `/about.html` live with canonical Person `@id` = `https://childcustodyanddivorce.com/about.html#brian-burkett` — every future authored page (blog posts Phase 5, practice pillars Phase 3) will reference this exact @id. Reusable `.cta-card` component class shipped in bio.css.
Last activity: 2026-07-06 — Plan 02-01 complete: `about.html` (395 lines, real 800x800 Burkett headshot as LCP hero, Person JSON-LD with hasCredential [JD Thomas Jefferson + CA Bar 220343 admitted 2002] + alumniOf [Pepperdine + Thomas Jefferson] + memberOf [State Bar of California] + worksFor LegalService), `assets/css/bio.css` (346 lines, all values via tokens.css, reusable `.cta-card` component, prefers-reduced-motion honored), sitemap.xml updated with `/about.html` at lastmod 2026-07-06. All three validators pass. Commits `6776e4a` + `4477b65` + `1997228` pushed to main. One deviation: reworded three occurrences of "24 years of practice" → "24 years of family-law practice" to match the content_facts.md whitelist substring. Sibling agent Plan 02-02 shipped `/contact.html` + `/thanks.html` + form spam filter + contact.css concurrently (commit `c647449`).

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

### Pending Todos

- **Human-verify checkpoint (Plan 05)**: 6-point manual QA on Netlify preview URL — privacy/terms/disclaimer render correctly with universal chrome, footer legal-links resolve without 404, California-specific language, calbar.ca.gov link works, "Prior results do not guarantee a similar outcome" verbatim on disclaimer.html. Type "approved" to close Phase 1.
- **Phase 2 blocker**: `scripts/content_facts.md` is deliberately empty. Phase 2 (bio) MUST fill it with Burkett's bar admission year, bar number, JD school, undergrad, and any verified experience claims before the bio page can pass the fabrication validator.
- **Phase 2 blocker**: `includes/footer.html` BIO-VERIFY comment slot in credentials column must be filled with verified bar admission year + CA Bar number in Phase 2. Both include file AND every consuming page (index.html + privacy.html + terms.html + disclaimer.html) must update in the same commit.
- **Phase 2 privacy refresh trigger**: If Phase 2+ wires any additional third-party (Segment, Hotjar, Facebook Pixel, retargeting pixel, etc.), privacy.html Third-Party Services + Information We Collect sections must be updated BEFORE the new tool ships.
- **Fresh clone bootstrap**: Every new local clone must run `bash scripts/install_hooks.sh` — `.git/hooks/` isn't tracked by git.

### Blockers/Concerns

- **Hard date: 2026-07-31 Justia sunset**. Phases 1-7 must complete before this. Work back from T-14 = 2026-07-17.
- **Open gaps to address during Phase 1**: Burkett's exact bar credentials (year, number, JD school, undergrad) for `hasCredential` schema; final city list for location matrix; GBP account choice (fresh vs. existing); Google Ads MCC access status; www vs. apex canonical decision before Phase 7 T-14.

## Session Continuity

Last session: 2026-07-06
Stopped at: Completed Plan 02-01 (bio). `/about.html` + `assets/css/bio.css` + sitemap.xml update pushed to main (`6776e4a` + `4477b65` + `1997228`). Sibling Plan 02-02 also complete (`c647449`). Plan 02-03 (homepage + sitewide nav-path cutover from `/attorney-bio/` → `/about.html` and `/contact/` → `/contact.html`) is next — Wave 2, blocked on Waves 1 completion which just landed. Resume file: None (all commits pushed, working tree clean).
Resume file: None (Phase 1 complete)
