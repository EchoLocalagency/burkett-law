# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-07-02)

**Core value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).
**Current focus:** Phase 1: Foundation + Design System + Validators

## Current Position

Phase: 1 of 8 (Foundation + Design System + Validators)
Plan: 3 of 5 complete (01 + 02 + 03 done; 04 + 05 pending)
Status: Design system + validators both live. Ready for parallel Plans 04 + 05.
Last activity: 2026-07-03 — Plan 02 complete: tokens.css (150 lines, DESIGN.md §13 verbatim) + base.css (83 lines, zero hex literals) + variable Fraunces WOFF2 (all 4 axes SOFT/WONK/opsz/wght, 205 KB, converted from upstream TTF via fontTools) + variable Inter WOFF2 (352 KB) + OFL LICENSE files + templates/base.html semantic scaffold. Commits 08845a3 / 1c58475 / 6e7b71a on main (pushed 4a9859b..6e7b71a). Prior in the day: Plan 03 (validators + pre-commit hook) complete via parallel agent — commits 1ff496e / 5915d24 / 299fa9e.

Progress: [████░░░░░░] 35%

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

### Pending Todos

- **Plan 04**: Universal header + footer with character-identical NAP + Cal Bar disclaimer band + nav.js mobile drawer (FND-07, FND-08). Consumes tokens.css + base.css + templates/base.html from Plan 02.
- **Plan 05**: Legal pages (privacy.html CCPA/CPRA + terms.html + disclaimer.html Cal Bar Rule 7.1-7.5) (FND-10). Consumes templates/base.html from Plan 02.
- **Phase 2 blocker**: `scripts/content_facts.md` is deliberately empty. Phase 2 (bio) MUST fill it with Burkett's bar admission year, bar number, JD school, undergrad, and any verified experience claims before the bio page can pass the fabrication validator.
- **Fresh clone bootstrap**: Every new local clone must run `bash scripts/install_hooks.sh` — `.git/hooks/` isn't tracked by git.

### Blockers/Concerns

- **Hard date: 2026-07-31 Justia sunset**. Phases 1-7 must complete before this. Work back from T-14 = 2026-07-17.
- **Open gaps to address during Phase 1**: Burkett's exact bar credentials (year, number, JD school, undergrad) for `hasCredential` schema; final city list for location matrix; GBP account choice (fresh vs. existing); Google Ads MCC access status; www vs. apex canonical decision before Phase 7 T-14.

## Session Continuity

Last session: 2026-07-03
Stopped at: Plans 02 + 03 both complete. Design tokens + fonts + base template live (Plan 02, commits 08845a3 / 1c58475 / 6e7b71a); content validators + pre-commit hook live (Plan 03, commits 1ff496e / 5915d24 / 299fa9e). Next: Plans 04 (universal header + footer) and 05 (legal pages) can execute in parallel — both depend only on Plan 02 artifacts and both must pass Plan 03 validators.
Resume file: .planning/phases/01-foundation-design-system-validators/04-PLAN.md (parallel with 05-PLAN.md)
