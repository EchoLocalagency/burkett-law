---
phase: 01-foundation-design-system-validators
plan: 04
subsystem: ui
tags: [html, css, javascript, accessibility, cal-bar, nap]

# Dependency graph
requires:
  - phase: 01-foundation-design-system-validators/02
    provides: tokens.css + base.css + templates/base.html scaffold + self-hosted Fraunces/Inter fonts
  - phase: 01-foundation-design-system-validators/03
    provides: Cal Bar lint + fabrication validator + identity guard + pre-commit hook
provides:
  - includes/header.html (universal sticky-navy header fragment)
  - includes/footer.html (universal 4-column navy footer fragment with character-identical NAP + Cal Bar Rule 7.1 disclaimer band)
  - assets/css/header.css (header component styles, token-only, 138 lines)
  - assets/css/footer.css (footer component styles, token-only, 134 lines)
  - assets/js/nav.js (accessible mobile drawer toggle — Escape close + focus trap + link-click close)
  - templates/base.html updated to inline both includes + link both stylesheets
  - Refined Cal Bar lint RULE_7_1_GUARANTEE to allow legally-required negations ("do not guarantee") while still catching marketing claims
affects: [phase-01-plan-05-legal-pages, phase-02-bio-homepage-contact, phase-03-practice-pillars, phase-04-location-pages, phase-05-blog]

# Tech tracking
tech-stack:
  added: []  # No new libs — vanilla HTML/CSS/JS on top of Plan 02's design tokens
  patterns:
    - "Hand-inline include pattern (no build system): every future page copies templates/base.html verbatim; header/footer text lives in includes/*.html as the canonical source of truth. Cross-page consistency enforced by identity guard + Cal Bar lint via pre-commit hook."
    - "Component-scoped CSS: header.css + footer.css use only var(--*) from tokens.css. Zero hex literals. Every component adds one <link> in <head>."
    - "Character-identical NAP: address string '591 Camino De La Reina, Suite 821, San Diego, CA 92108' + phone display '(619) 250-2683' + tel: E.164 '+16192502683' — the canonical strings every downstream schema author + Phase 8 GBP + BrightLocal citation write must match verbatim (PITFALLS.md Pitfall 9)."

key-files:
  created:
    - includes/header.html
    - includes/footer.html
    - assets/css/header.css
    - assets/css/footer.css
    - assets/js/nav.js
  modified:
    - templates/base.html
    - scripts/lint_cal_bar.py (RULE_7_1_GUARANTEE regex refined)

key-decisions:
  - "Cal Bar lint RULE_7_1_GUARANTEE refined (not weakened) with negative lookbehinds for 'do not | does not | cannot | no ' + guarantee, so the legally-required disclaimer sentence 'Past results do not guarantee a similar outcome' passes while marketing claims like 'we guarantee' or 'guaranteed outcome' still fail. Full test_validators.sh suite still passes."
  - "tel: uses E.164 '+16192502683' per PITFALLS.md UX pitfall (parens/spaces can break international dialers) — supersedes literal FND-08 wording 'tel:6192502683' and the ROADMAP success-criterion string. Display form '(619) 250-2683' unchanged."
  - "Bar admission year + bar number left as BIO-VERIFY placeholder comment in footer credentials column. Phase 2 (bio) must fill these AND add to scripts/content_facts.md allowlist so the fabrication validator continues to pass when real numeric claims land."
  - "Hand-inline include pattern (no build system): base.html physically contains a copy of includes/header.html + includes/footer.html. Every future page will copy base.html to get both for free. If the header or footer needs a change, both the include file AND every consuming page must be updated in the same commit."

patterns-established:
  - "Header include pattern: <div class=\"site-header container-xl\"> + logo + hamburger + nav + phone chip inside <header role=\"banner\">"
  - "Footer include pattern: <div class=\"site-footer container-xl\"> + 4-col grid + full-bleed disclaimer band + copyright inside <footer role=\"contentinfo\">"
  - "Mobile drawer pattern: aria-controls + aria-expanded on hamburger toggle, data-open on nav, focus trap via keydown handler on document"

requirements-completed: [FND-07, FND-08]

# Metrics
duration: ~15min
completed: 2026-07-03
---

# Phase 01 Plan 04: Universal Header + Footer Summary

**Sticky navy header (BURKETT logo + 4-item nav + gold phone chip + accessible mobile drawer) and 4-column navy footer with character-identical NAP + Cal Bar Rule 7.1 sitewide disclaimer, both inlined into templates/base.html and passing all three validators.**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-07-03
- **Completed:** 2026-07-03
- **Tasks:** 3 (Header, Footer, Wire-into-base) + 1 lint refinement
- **Files created:** 5
- **Files modified:** 2

## Accomplishments
- Universal sticky header: BURKETT | family law logo, 4-item primary nav (Practice Areas, About, Blog, Contact), gold pill phone chip linking to `tel:+16192502683` (E.164), sticky navy bar with backdrop-blur.
- Universal 4-column footer: character-identical NAP (`591 Camino De La Reina, Suite 821, San Diego, CA 92108`), tel: + hours, all 8 practice-area links, all 6 firm/legal links (About, Blog, Contact, Privacy, Terms, Disclaimer), Cal Bar Rule 7.1 disclaimer band with all 5 required sentences verbatim, copyright.
- Mobile hamburger drawer with `aria-controls`/`aria-expanded`, Escape-to-close, focus trap (Tab wraps within drawer), and body-scroll lock while open. Skip-link remains first tab stop.
- All CSS references design tokens from Plan 02's `tokens.css` — zero hex literals in header.css or footer.css.
- All three validators (Cal Bar lint + fabrication + identity guard) pass on `templates/base.html` + both includes with zero violations.

## Task Commits

Each task was committed atomically:

1. **Task 1: Header component (include + CSS + nav.js)** — `1926b58` (feat)
2. **Task 2: Footer component (include + CSS) + Cal Bar lint refinement** — `668c5fe` (feat)
3. **Task 3: Wire header + footer into base.html template** — `6f01114` (feat)

All three pushed to `origin/main` (`0bb52d6..6f01114`). Netlify auto-deploys from GitHub webhook.

## Files Created/Modified
- `includes/header.html` — Universal header HTML fragment (39 lines): logo + hamburger + 4-item nav + phone chip + deferred nav.js include.
- `includes/footer.html` — Universal footer HTML fragment (68 lines): 4-column grid + disclaimer band + copyright, with character-identical NAP.
- `assets/css/header.css` — Header component styles (138 lines), token-only.
- `assets/css/footer.css` — Footer component styles (134 lines), token-only.
- `assets/js/nav.js` — Vanilla-JS mobile drawer toggle with Escape + focus trap (60 lines).
- `templates/base.html` — Added header.css + footer.css links; inlined full contents of both includes into `<header role="banner">` + `<footer role="contentinfo">` landmarks. Added pattern-comments explaining the hand-inline copy convention.
- `scripts/lint_cal_bar.py` — Refined RULE_7_1_GUARANTEE regex to skip mandated negations (see Deviations below).

## Decisions Made
- **E.164 tel: format** — Used `tel:+16192502683` per PITFALLS.md UX guidance (parens/spaces break international dialers). Supersedes the literal `tel:6192502683` in FND-08 + ROADMAP §Phase 1 Success Criterion 3. Display form `(619) 250-2683` unchanged. Was called out in Plan 04's must_haves.truths.
- **BIO-VERIFY placeholder for bar credentials** — Bar admission year + CA Bar number left as HTML comment in footer credentials column. Phase 2 (bio) must fill in the verified values AND add them to `scripts/content_facts.md` allowlist so the fabrication validator continues to pass.
- **Hand-inline include pattern** — No template engine. Base template physically contains a copy of includes/header.html + includes/footer.html. Every future page will `cp templates/base.html` to get both for free. When either include changes, both the include file AND every consuming page must be updated in the same commit. Alternative (build-time SSI/liquid) rejected in Plan 02 as unnecessary complexity for ≤ 60 pages.

## Deviations from Plan

### Auto-fixed Issues

**1. [Cal Bar lint RULE_7_1_GUARANTEE false positive on required disclaimer sentence]**
- **Found during:** Task 2 (running validators after writing includes/footer.html)
- **Issue:** `RULE_7_1_GUARANTEE` regex `\bguarantee[sd]?\b` matched the mandated Cal Bar Rule 7.1 disclaimer sentence "Past results do not guarantee a similar outcome" — a legally-required negation, not a marketing claim. Plan 04's `must_haves.truths` explicitly requires this sentence verbatim.
- **Fix:** Refined regex with negative lookbehinds: `(?<!do not )(?<!does not )(?<!cannot )(?<!no )\bguarantee[sd]?\b`. This is a precision refinement, not a weakening — marketing claims ("we guarantee", "guaranteed outcome") still fire. Confirmed the existing violate_cal_bar_sample.html fixture still fails (contains "We guarantee the best outcome" — no negation prefix).
- **Files modified:** `scripts/lint_cal_bar.py`
- **Verification:** `bash scripts/tests/test_validators.sh` — all 6 assertions pass. `bash scripts/run_all_validators.sh templates/base.html includes/header.html includes/footer.html index.html` — zero violations.
- **Committed in:** `668c5fe` (Task 2 commit)

---

**Total deviations:** 1 auto-fixed (Cal Bar lint precision refinement for legally-mandated disclaimer negation)
**Impact on plan:** Required to satisfy Plan 04's own `must_haves.truths` — the plan mandates both zero violations AND the exact required disclaimer sentence, which the original regex forbade. No scope creep.

## Issues Encountered
None beyond the deviation above.

## User Setup Required
None — no external service configuration for this plan.

**Human-verify checkpoint (from plan):** Plan 04 is `autonomous: false` with a `human-verify` gate at the end. All authoring tasks are committed + pushed to `main` (Netlify auto-deploys). The plan describes copying `templates/base.html` to a temp preview file at repo root for visual QA. Brian to run the 9-point manual QA (sticky header, footer NAP + disclaimer band visible, mobile hamburger + Escape + focus, phone tap opens dialer, keyboard skip-link → logo → nav order, view-source ARIA landmarks, DevTools computed background colors). Real end-to-end render will be visible on any page cloned from base.html — but the current placeholder index.html at repo root does NOT yet consume base.html, so it will look bare until Phase 2 rebuilds the homepage from the template. That is expected and documented in the success criteria.

## Next Phase Readiness
- **Plan 05 (Legal pages)**: Unblocked. Can consume includes/header.html + includes/footer.html + templates/base.html to build privacy.html + terms.html + disclaimer.html. Zero file overlap with Plan 04.
- **Phase 2 (Bio + Homepage + Contact)**: Unblocked once Plan 05 lands. Bio page fills the `BIO-VERIFY` bar-credentials placeholder in the footer credentials column AND adds the verified values (admission year, bar number, JD school, undergrad) to `scripts/content_facts.md` so the fabrication validator continues to pass.
- **Canonical NAP for Phase 8 GBP / BrightLocal**: `591 Camino De La Reina, Suite 821, San Diego, CA 92108` + phone display `(619) 250-2683` + tel E.164 `+16192502683`. Any Phase 8 write to GBP or BrightLocal citation must match these strings character-for-character (identity guard enforces on-site; PITFALLS.md Pitfall 9 is the reason).

---
*Phase: 01-foundation-design-system-validators*
*Completed: 2026-07-03*
