---
phase: 01-foundation-design-system-validators
plan: 02
subsystem: ui
tags: [css, design-tokens, fonts, woff2, fraunces, inter, self-hosted-fonts, html-template]

requires:
  - phase: 01-plan-01
    provides: Netlify repo + deploy pipeline (fonts/css served on push)
provides:
  - assets/css/tokens.css (all ~90 design tokens from DESIGN.md §13 + two @font-face)
  - assets/css/base.css (reset, headings, links, skip-link, focus ring, .prose, containers, reduced-motion, section rhythm)
  - assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2 (variable, all axes)
  - assets/fonts/InterVariable.woff2 (variable)
  - assets/fonts/LICENSE-Fraunces.txt + LICENSE-Inter.txt (OFL attribution)
  - templates/base.html (semantic scaffold: skip link, landmarks, font preloads, meta/OG/canonical slots, GA4 + JSON-LD sentinels)
affects: [02-bio-homepage-contact, 03-practice-pillars, 04-location-pages, 05-blog, all future pages consume tokens.css + base.css + copy templates/base.html]

tech-stack:
  added:
    - Self-hosted variable Fraunces (SIL OFL) with SOFT/WONK/opsz/wght axes
    - Self-hosted variable Inter (SIL OFL)
    - Vanilla CSS custom properties as the sole design-token layer (no framework, no CSS-in-JS)
  patterns:
    - "Design tokens live at one URL (assets/css/tokens.css); every page links it — no token duplication in component CSS"
    - "base.css uses zero hex literals — all color goes through var(--*) semantic tokens"
    - "templates/base.html is a manual-copy source-of-truth (literal {{ ... }} placeholders — no template engine, no build step)"
    - "GA4 injected via sentinel-delimited comment block so Plan 03 identity guard can rewrite per-site (cross-client pollution prevention)"

key-files:
  created:
    - assets/css/tokens.css
    - assets/css/base.css
    - assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2
    - assets/fonts/InterVariable.woff2
    - assets/fonts/LICENSE-Fraunces.txt
    - assets/fonts/LICENSE-Inter.txt
    - templates/base.html
  modified: []

key-decisions:
  - "Fraunces sourced from undercasetype/Fraunces master TTF (all 4 axes) and locally converted to WOFF2 via fontTools — Google's gstatic WOFF2 for Fraunces only exposes wght+opsz (no SOFT/WONK); the design system uses those two axes so the full-axis file is required."
  - "Inter sourced directly from rsms/inter master WOFF2 — already a variable WOFF2 release asset."
  - "No hex literals in base.css — every color reference goes through a semantic token so a future palette swap flips one file."
  - "GA4 and JSON-LD blocks are commented in the template with BEGIN/END sentinels so the identity guard (Plan 03) can inject per-site instead of hardcoding — prevents the Mr Green cross-client GA pollution incident from recurring."

patterns-established:
  - "Font preloads: <link rel=preload as=font type=font/woff2 crossorigin> pair in <head> for both above-the-fold typefaces (LCP win per DESIGN.md §2.2)"
  - "Skip link is the first tab stop, hidden off-screen until :focus (DESIGN.md §11.1)"
  - "Semantic landmarks in template: role=banner header, <main id=main>, role=contentinfo footer — anchors WCAG landmark navigation"
  - "Reading column: .prose class caps at 68ch and stacks children with --space-6 rhythm (DESIGN.md §7.4)"
  - "Reduced motion: universal *,*::before,*::after selector caps animation-duration + transition-duration + scroll-behavior for prefers-reduced-motion users (DESIGN.md §10.3 verbatim)"

requirements-completed:
  - FND-04
  - FND-05
  - FND-06

duration: 12min
completed: 2026-07-03
---

# Phase 01 Plan 02 Summary — Design System Foundation

**Full DESIGN.md §13 token block + self-hosted variable Fraunces (all 4 axes) + variable Inter, wired into a semantic base.html scaffold every future page copies.**

## Performance

- **Duration:** ~12 min
- **Started:** 2026-07-03T11:54Z
- **Completed:** 2026-07-03T12:00Z
- **Tasks:** 3
- **Files created:** 7

## Accomplishments
- All ~90 CSS custom properties from DESIGN.md §13 (color primitives + semantic + typography + spacing + radius + shadow + motion + layout + z-index) landed verbatim in `assets/css/tokens.css` alongside both `@font-face` declarations with `font-display: swap`
- Both variable fonts self-hosted at `assets/fonts/` under OFL — Fraunces WOFF2 built from the upstream full-axis TTF (SOFT + WONK + opsz + wght all present, 205 KB) via `fontTools`, Inter WOFF2 fetched directly from rsms/inter master (352 KB)
- `assets/css/base.css` provides the site-wide reset + heading defaults + link ghost pattern + `.skip-link` + global `:focus-visible` ring + `.prose` reading column + `.container-*` widths + `prefers-reduced-motion` block + section rhythm — 31 `var(--*)` references, zero hex literals
- `templates/base.html` is a working scaffold with skip link, banner/main/contentinfo landmarks, favicon slots, OG image slot, canonical link, font preloads, tokens.css + base.css links, and GA4 + JSON-LD sentinel-delimited comments — no hardcoded GA4 measurement ID

## Task Commits

Each task committed atomically to `main` (pushed `4a9859b..6e7b71a`):

1. **Task 1: Fonts + LICENSEs** — `08845a3` (feat: add self-hosted Fraunces + Inter variable WOFF2 fonts)
2. **Task 2: tokens.css + base.css** — `1c58475` (feat: add tokens.css + base.css design system foundation)
3. **Task 3: base.html template** — `6e7b71a` (feat: add reusable base HTML template scaffold)

## Files Created/Modified

- `assets/css/tokens.css` (150 lines) — DESIGN.md §13 token block verbatim + 2 @font-face
- `assets/css/base.css` (83 lines) — reset + prose + focus ring + reduced-motion + containers
- `assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2` (205 KB) — variable, all 4 axes
- `assets/fonts/InterVariable.woff2` (352 KB) — variable
- `assets/fonts/LICENSE-Fraunces.txt` + `assets/fonts/LICENSE-Inter.txt` — OFL attribution
- `templates/base.html` (81 lines) — semantic scaffold with slot placeholders

## Font source URLs (for Phase 6 performance baseline + future re-fetch)

- **Fraunces**: `https://github.com/undercasetype/Fraunces/raw/master/fonts/variable/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf` → converted locally to WOFF2 via `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('...ttf'); f.flavor='woff2'; f.save('...woff2')"` (after `pip3 install brotli`). Final file: 205,376 bytes.
- **Inter**: `https://github.com/rsms/inter/raw/master/docs/font-files/InterVariable.woff2` (already WOFF2, no conversion). Final file: 352,240 bytes.

## Decisions Made

- **Fraunces source = GitHub master TTF + local WOFF2 conversion** (not Google's gstatic WOFF2). Google's variable Fraunces WOFF2 only exposes `wght` + `opsz` axes — the design system relies on `SOFT` (which needs the full-axis file). Kept OFL attribution file inline to remain redistribution-compliant.
- **No hex literals allowed in base.css.** Every color goes through a semantic token (`var(--color-*)` or `var(--<primitive>)`). Enforced by a verify grep. Rationale: single-file palette swap safety.
- **GA4 injected via BEGIN/END sentinels in a comment.** Prevents the Mr Green → Arcadian/Top Tier cross-client GA pollution incident (PITFALLS.md Pitfall 11) — the identity guard shipped in Plan 03 rewrites the block per-site instead of the template carrying a hardcoded ID.

## Deviations from Plan

None — plan executed exactly as written. The plan flagged the Google gstatic WOFF2 fallback path and the fontTools-conversion path as equally acceptable for Fraunces; the fontTools path was chosen because it preserves all 4 axes (SOFT + WONK + opsz + wght) that the design system uses.

## Issues Encountered

- The plan text pointed at `github.com/undercase/Fraunces` (missing "type" suffix) which returns an HTML 404 disguised as a text file. Resolved by using the correct repo `github.com/undercasetype/Fraunces` for both the source TTF and the OFL license. Recorded here so future plans reference the correct upstream.
- `fontTools` was already installed system-wide but its WOFF2 flavor needs `brotli`. Fixed with `pip3 install brotli` (single package).

## Consumer pattern (how future plans use this)

Every future page in Phase 2+ starts with:
1. Copy `templates/base.html` to the new page path
2. Fill the `{{ page_title }}` / `{{ page_description }}` / `{{ page_path }}` / `{{ og_image_path }}` / `{{ page_h1 }}` / `{{ page_lead }}` placeholders inline (no build step)
3. Replace the `<main>` content between the landmarks
4. Inject the per-page JSON-LD inside the `SCHEMA-BEGIN` sentinel block
5. Never touch `@font-face` or CSS custom properties in the page — always through `tokens.css` + `base.css`

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Design system layer is live at `https://burkett-law.netlify.app/assets/css/tokens.css` after Netlify auto-deploy of commit `6e7b71a` (push `4a9859b..6e7b71a`).
- Plans 03 (validators + identity guard) and 04 (universal header/footer) can proceed in parallel — both consume tokens.css + base.css but do not modify them.
- Plan 04 will fill the header/footer placeholders in `templates/base.html`. Plan 03's identity guard will target the GA4 BEGIN/END sentinels for per-site injection.

---
*Phase: 01-foundation-design-system-validators*
*Plan: 02*
*Completed: 2026-07-03*
