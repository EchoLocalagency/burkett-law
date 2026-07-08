# WCAG 2.1 AA Spot Audit — Phase 6

## Method
Programmatic pass across all 52 HTML pages, plus manual review of the
design tokens + focus styles. No axe-core / Lighthouse run against the
Netlify preview yet (Phase 7 T-7 QA covers that against the live URL);
this pass is the "no obvious A/AA violations in source" gate.

## Pass results

### 1.1.1 — Non-text Content (Level A)
- **`<img>` alt attributes**: 0 images sitewide missing `alt`.
- Every headshot / hero image on `about.html` + service-area callouts has
  descriptive alt.
- Icons in header/footer / SVG glyphs use `aria-hidden="true"` (verified
  in `includes/header.html` phone icon block).

### 1.3.1 — Info and Relationships (Level A)
- Every page has exactly one `<h1>` (0 pages have >1, 0 pages have 0).
- Heading hierarchy correct across templates (H1 → H2 → H3).
- Semantic landmarks present: `<header role="banner">`, `<main id="main">`,
  `<footer role="contentinfo">`, `<nav aria-label="Primary">`.

### 1.4.3 — Contrast Minimum (Level AA)
- Design tokens (assets/css/tokens.css) define the warm-approachable palette:
  - `--color-text` = `--ink-900` on `--color-bg` = `--cream-50` — approx 15:1
    contrast, passes AAA.
  - `--color-text-muted` = `--ink-500` on cream — approx 6.5:1, passes AA.
  - `--color-accent` = `--gold-600` on cream — approx 4.6:1, passes AA for
    large text (18pt+ or 14pt bold). CTAs use `--gold-600` on `--ink-900`
    (dark button) — passes AAA.
  - `--color-focus-ring` = `--gold-500` — distinct on cream background.
- No hard-coded hex values found outside `tokens.css` (grep clean).

### 2.1.1 — Keyboard (Level A)
- **Skip link**: every page ships `<a href="#main" class="skip-link">Skip to
  main content</a>` as the first element in `<body>` (0 pages missing).
- **Mobile nav**: `assets/js/nav.js` toggles `aria-expanded` on the
  hamburger button. Focus goes to nav on open.
- **:focus-visible** styles present in `assets/css/base.css` — all
  focusable elements get the gold focus ring.

### 2.4.4 — Link Purpose (Level A)
- All footer links have descriptive text (no "click here").
- Phone links have `aria-label` (e.g. `Call the Law Office of Brian
  Burkett at (619) 250-2683`).

### 3.1.1 — Language of Page (Level A)
- Every page declares `<html lang="en-US">`.

### 4.1.2 — Name, Role, Value (Level A)
- Form inputs on `/contact.html` have associated `<label>` elements.
- Hamburger button has `aria-label` + `aria-controls` + `aria-expanded`.
- Skip link + banner-role header + main landmark all in place.

## Deferred to Phase 7 T-7 QA
- **Lighthouse mobile accessibility score** (needs live preview URL)
- **Axe DevTools** manual sweep on 5 sample pages
- **Screen reader smoke test** (VoiceOver on Safari mobile)
- **Real color-contrast measurement via WebAIM contrast checker** (rather
  than approximated math)

## No violations blocking Phase 6 closeout.
