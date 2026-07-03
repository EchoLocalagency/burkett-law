---
phase: 01-foundation-design-system-validators
plan: 02
type: execute
wave: 2
depends_on: [01]
files_modified:
  - assets/css/tokens.css
  - assets/css/base.css
  - assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2
  - assets/fonts/InterVariable.woff2
  - assets/fonts/LICENSE-Fraunces.txt
  - assets/fonts/LICENSE-Inter.txt
  - templates/base.html
autonomous: true
requirements: [FND-04, FND-05, FND-06]

must_haves:
  truths:
    - "tokens.css is loadable and defines every design token from DESIGN.md §13 as a CSS custom property"
    - "Fraunces + Inter WOFF2 files exist at /assets/fonts/ with matching @font-face declarations using font-display: swap"
    - "Preload directives for both font files are present in the base template <head>"
    - "The base HTML template is a working starting point that includes semantic landmarks, skip link, viewport, favicon slot, and OG image slot"
    - "Copying the base template to a new .html file and opening it locally shows Fraunces headings + Inter body text with the cream/navy palette"
  artifacts:
    - path: "assets/css/tokens.css"
      provides: "The complete token block from DESIGN.md §13 (color primitives + semantic tokens + typography + spacing + radius + shadow + motion + layout + z-index) plus the two @font-face declarations"
      min_lines: 140
      contains: "--ink-800: #12294A"
    - path: "assets/css/base.css"
      provides: "Reset + typographic defaults + link/button base + focus ring + prefers-reduced-motion + .prose reading column + .container widths"
      min_lines: 80
    - path: "assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2"
      provides: "Self-hosted Fraunces variable font"
    - path: "assets/fonts/InterVariable.woff2"
      provides: "Self-hosted Inter variable font"
    - path: "templates/base.html"
      provides: "Reusable base HTML template with landmarks + skip link + head boilerplate + placeholder GA4/schema slots — commented so Phase 2+ pages can copy and fill"
      contains: "Skip to main content"
  key_links:
    - from: "templates/base.html"
      to: "assets/css/tokens.css + base.css"
      via: "<link rel=stylesheet> in <head>"
      pattern: "assets/css/tokens.css"
    - from: "templates/base.html"
      to: "assets/fonts/*.woff2"
      via: "<link rel=preload as=font crossorigin> pair in <head>"
      pattern: "rel=\"preload\".*font"
    - from: "assets/css/tokens.css"
      to: "assets/fonts/*.woff2"
      via: "@font-face src url()"
      pattern: "@font-face"
---

<objective>
Land the visual foundation the entire site consumes: the DESIGN.md token layer as a real tokens.css file, a base.css providing the reset + prose column + focus ring + reduced-motion + container widths, self-hosted Fraunces + Inter variable WOFF2 fonts wired via @font-face and preload, and a reusable base HTML template that later plans copy for every new page.

Purpose: Phase 2 (bio + homepage + contact) starts building real pages. Those pages must NOT hand-roll color values or repeat @font-face declarations — they consume tokens.css and copy templates/base.html. Locking the design system here means visual consistency across the site is enforced by construction, not by discipline. Self-hosting the fonts avoids Google Fonts CDN (STACK.md rule + trust signal for YMYL/legal).

Output: A tokens.css that is copy-pasteable from DESIGN.md §13 verbatim, a base.css shim for the site-wide reset + reading column, two WOFF2 font files at /assets/fonts/, and a base.html template that is a working starting point every future page uses.
</objective>

<execution_context>
@/Users/brianegan/.claude/get-shit-done/workflows/execute-plan.md
@/Users/brianegan/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md
@/Users/brianegan/Desktop/burkett-law/.planning/ROADMAP.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/DESIGN.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/STACK.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/ARCHITECTURE.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/PITFALLS.md

<interfaces>
<!-- Token block, @font-face pattern, and base template head structure the implementer will USE VERBATIM. -->

Complete :root { ... } token block: Copy from research/DESIGN.md §13 lines 826-953 EXACTLY as written. Do not modify values. Do not skip tokens. All ~90 custom properties.

@font-face declarations (from DESIGN.md §2.2, adapted for exact filenames used in this plan):
```css
@font-face {
  font-family: "Fraunces";
  src: url("/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2") format("woff2-variations");
  font-weight: 400 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("/assets/fonts/InterVariable.woff2") format("woff2-variations");
  font-weight: 400 700;
  font-style: normal;
  font-display: swap;
}
```

Preload pattern for base.html <head> (LCP win per DESIGN.md §2.2):
```html
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/InterVariable.woff2" crossorigin>
```

Skip link + landmarks (from DESIGN.md §11.1):
```html
<a href="#main" class="skip-link">Skip to main content</a>
<header role="banner"><!-- Phase 4 fills nav --></header>
<main id="main">...</main>
<footer role="contentinfo"><!-- Phase 4 fills footer --></footer>
```

Font source URLs (variable WOFF2 releases as of 2026-07):
- Fraunces: https://github.com/undercase/Fraunces/raw/main/fonts/variable/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf — NEED WOFF2 conversion. Alternative: https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700 — the served WOFF2 URL inside the CSS response is directly downloadable.
- Inter: https://github.com/rsms/inter/releases (InterVariable.woff2 is a published asset since v4.0).
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Download + install Fraunces + Inter WOFF2 fonts at /assets/fonts/</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2,
    /Users/brianegan/Desktop/burkett-law/assets/fonts/InterVariable.woff2,
    /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Fraunces.txt,
    /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Inter.txt
  </files>
  <action>
Create /Users/brianegan/Desktop/burkett-law/assets/fonts/ and download the variable WOFF2 files.

Inter (easiest — published WOFF2):
1. `curl -sL -o /Users/brianegan/Desktop/burkett-law/assets/fonts/InterVariable.woff2 https://github.com/rsms/inter/raw/master/docs/font-files/InterVariable.woff2`
2. Verify with `file /Users/brianegan/Desktop/burkett-law/assets/fonts/InterVariable.woff2` — output should say `Web Open Font Format (Version 2)`. If file size < 300KB or file says "HTML document", the URL is wrong — try `https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip` and extract InterVariable.woff2 from the "Inter Web" folder.

Fraunces (Google-served WOFF2 works cleanly):
1. Fetch the Google CSS that references the variable font:
   `curl -sL -A "Mozilla/5.0" -o /tmp/fraunces.css 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&display=swap'`
2. Extract the WOFF2 URL: `grep -oE "https://fonts.gstatic.com/[^)]+\.woff2" /tmp/fraunces.css | head -1`
3. Download the WOFF2 to the target path:
   `curl -sL -o "/Users/brianegan/Desktop/burkett-law/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" "<extracted-url>"`
4. Verify with `file` command as above.

FALLBACK if Google-served WOFF2 doesn't include all axes:
Download the TTF variable font from https://github.com/undercase/Fraunces/raw/main/fonts/variable/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf to /tmp/, then convert with either woff2_compress (Homebrew: `brew install woff2` then `woff2_compress /tmp/Fraunces\[...\].ttf`) OR the Python `fonttools` (`pip install fonttools brotli` then `python -c "from fontTools.ttLib import TTFont; f=TTFont('/tmp/...ttf'); f.flavor='woff2'; f.save('/Users/brianegan/Desktop/burkett-law/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2')"`).

Save the OFL LICENSE files:
- Fraunces: `curl -sL -o /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Fraunces.txt https://github.com/undercase/Fraunces/raw/main/OFL.txt`
- Inter: `curl -sL -o /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Inter.txt https://github.com/rsms/inter/raw/master/LICENSE.txt`

CRITICAL:
- Both fonts are SIL Open Font License (OFL) — free to self-host + redistribute. Do NOT skip the LICENSE files (attribution required).
- Do NOT commit any font-decompressed / TTF working copies — only the two .woff2 files + LICENSE files.
- File sizes: Fraunces WOFF2 should be ~90-150KB; InterVariable WOFF2 should be ~85-130KB. Fail loudly if either is >500KB (wrong download) or <50KB (partial download).
  </action>
  <verify>
    <automated>ls -la /Users/brianegan/Desktop/burkett-law/assets/fonts/ && file "/Users/brianegan/Desktop/burkett-law/assets/fonts/InterVariable.woff2" | grep -q "Web Open Font Format" && file "/Users/brianegan/Desktop/burkett-law/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" | grep -q "Web Open Font Format" && test -f /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Fraunces.txt && test -f /Users/brianegan/Desktop/burkett-law/assets/fonts/LICENSE-Inter.txt && echo "PASS"</automated>
  </verify>
  <done>Both WOFF2 files exist, `file` command identifies each as "Web Open Font Format (Version 2)", both OFL LICENSE files present, no stray TTF/OTF files committed.</done>
</task>

<task type="auto">
  <name>Task 2: Create tokens.css + base.css</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css,
    /Users/brianegan/Desktop/burkett-law/assets/css/base.css
  </files>
  <action>
Create /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css:
1. Header comment: "Design tokens for Burkett Family Law — sourced verbatim from .planning/research/DESIGN.md §13. Any deviation requires a written rationale in a phase plan (per DESIGN.md §0)."
2. Two @font-face declarations EXACTLY as written in the interfaces block above.
3. The full :root { ... } block copied VERBATIM from research/DESIGN.md §13 (the "Consolidated token block" from lines 826-953). Every single custom property. Do not summarize, do not merge sections, do not drop the z-index scale.

Create /Users/brianegan/Desktop/burkett-law/assets/css/base.css:
1. Header comment: "Site-wide reset + typographic defaults + reading column + focus ring. Consumed by every page via <link>. Component styles live in component-scoped CSS files (Plan 04 adds header/footer)."
2. Modern reset (no need for Normalize.css — Vanilla CSS is baseline per STACK.md):
```css
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
body {
  min-height: 100vh;
  background: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: var(--lh-body);
  font-feature-settings: "kern", "liga", "calt";
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
img, picture, svg, video, canvas { display: block; max-width: 100%; height: auto; }
input, button, textarea, select { font: inherit; color: inherit; }
```
3. Headings (per DESIGN.md §2):
```css
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  color: var(--color-text);
  line-height: var(--lh-heading);
  text-wrap: balance;
}
h1 { font-size: var(--fs-h1); font-weight: 500; letter-spacing: var(--tracking-tight); }
h2 { font-size: var(--fs-h2); font-weight: 500; letter-spacing: -0.01em; }
h3 { font-size: var(--fs-h3); font-weight: 600; }
p  { text-wrap: pretty; }
```
4. Links (per DESIGN.md §6.1 ghost pattern):
```css
a { color: var(--color-accent-text); text-decoration-thickness: 1.5px; text-underline-offset: 4px; text-decoration-color: var(--gold-600); }
a:hover { color: var(--ink-900); text-decoration-thickness: 2.5px; }
```
5. Skip link (per DESIGN.md §11.1):
```css
.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
  background: var(--ink-800);
  color: var(--cream-50);
  padding: var(--space-3) var(--space-4);
  z-index: var(--z-toast);
  border-radius: 0 0 var(--radius-md) 0;
}
.skip-link:focus { left: 0; outline: none; box-shadow: var(--shadow-focus); }
```
6. Global focus ring:
```css
:focus-visible { outline: none; box-shadow: var(--shadow-focus); border-radius: var(--radius-sm); }
```
7. Reading column (per DESIGN.md §7.4):
```css
.prose { max-width: 68ch; margin-inline: auto; font-size: var(--fs-body); line-height: var(--lh-body); color: var(--color-text-muted); }
.prose > * + * { margin-top: var(--space-6); }
.prose h2 { margin-top: var(--space-12); color: var(--color-text); }
.prose h3 { margin-top: var(--space-8); color: var(--color-text); }
```
8. Container widths (per DESIGN.md §7.2):
```css
.container-sm { max-width: var(--container-sm); margin-inline: auto; padding-inline: var(--space-6); }
.container-md { max-width: var(--container-md); margin-inline: auto; padding-inline: var(--space-6); }
.container-lg { max-width: var(--container-lg); margin-inline: auto; padding-inline: var(--space-6); }
.container-xl { max-width: var(--container-xl); margin-inline: auto; padding-inline: var(--space-6); }
```
9. Reduced motion (per DESIGN.md §10.3 — copy VERBATIM):
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
10. Section rhythm helper (per DESIGN.md §3 rhythm rule):
```css
section { padding-block: var(--space-16); }
@media (min-width: 768px) { section { padding-block: var(--space-20); } }
@media (min-width: 1024px) { section { padding-block: var(--space-24); } }
```

CRITICAL:
- No color literal hex codes in base.css — every color reference goes through a var(--*) token.
- No frameworks, no CSS-in-JS.
- No imports of other CSS files — tokens.css and base.css are separately linked in the base template.
- Do NOT add nav / footer / button component styles here — those live in the Plan 04 component CSS files.
  </action>
  <verify>
    <automated>test -f /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && test -f /Users/brianegan/Desktop/burkett-law/assets/css/base.css && grep -q '#12294A' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && grep -q '#FBF8F3' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && grep -q '#B45309' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && grep -q '@font-face' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && grep -c '@font-face' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css | grep -q '^2$' && grep -q 'font-display: swap' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css && grep -q 'prefers-reduced-motion' /Users/brianegan/Desktop/burkett-law/assets/css/base.css && grep -q '.skip-link' /Users/brianegan/Desktop/burkett-law/assets/css/base.css && ! grep -E '#[0-9A-Fa-f]{6}' /Users/brianegan/Desktop/burkett-law/assets/css/base.css && echo "PASS"</automated>
  </verify>
  <done>tokens.css contains all three brand hexes AND two @font-face blocks with font-display: swap; base.css contains reset, headings, links, .skip-link, focus-visible, .prose, .container-*, prefers-reduced-motion — with ZERO hex literals in base.css (all color via tokens).</done>
</task>

<task type="auto">
  <name>Task 3: Create reusable base HTML template</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/templates/base.html
  </files>
  <action>
Create /Users/brianegan/Desktop/burkett-law/templates/ directory. This directory is a source-of-truth for HTML pattern reuse — pages in Phase 2+ COPY base.html and fill in content. Do NOT wire a build system; templates/ is a manual copy-source.

Create /Users/brianegan/Desktop/burkett-law/templates/base.html:

```html
<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- TITLE + META (unique per page) -->
  <title>{{ page_title }} — Law Office of Brian Burkett</title>
  <meta name="description" content="{{ page_description }}">
  <link rel="canonical" href="https://childcustodyanddivorce.com{{ page_path }}">

  <!-- Open Graph (unique per page, image slot per page) -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{{ page_title }}">
  <meta property="og:description" content="{{ page_description }}">
  <meta property="og:url" content="https://childcustodyanddivorce.com{{ page_path }}">
  <meta property="og:image" content="https://childcustodyanddivorce.com{{ og_image_path }}">
  <meta property="og:site_name" content="Law Office of Brian Burkett">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Favicons -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <!-- Preload above-the-fold fonts (LCP win per DESIGN.md §2.2) -->
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/InterVariable.woff2" crossorigin>

  <!-- Design tokens + base styles -->
  <link rel="stylesheet" href="/assets/css/tokens.css">
  <link rel="stylesheet" href="/assets/css/base.css">

  <!-- GA4 slot — MUST inject the site-specific measurement ID from clients.json.
       NEVER hardcode a GA4 id in this template (cross-client pollution incident,
       PITFALLS.md Pitfall 11). Phase 6 wires the real id. Placeholder below. -->
  <!-- GA4-BEGIN
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-BURKETT_ID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-BURKETT_ID');
  </script>
  GA4-END -->

  <!-- Schema slot — per-page JSON-LD block goes here. Phase 2 wires bio + LocalBusiness; Phase 3 wires Service+FAQPage per pillar. -->
  <!-- SCHEMA-BEGIN
  <script type="application/ld+json">{ ... }</script>
  SCHEMA-END -->
</head>

<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header role="banner">
    <!-- Universal header (logo + 4-item nav + tel: chip) lands in Plan 04. Placeholder. -->
    <div class="container-xl">
      <p><em>Header component lands in phase 01 Plan 04.</em></p>
    </div>
  </header>

  <main id="main">
    <!-- Page content goes here -->
    <div class="container-lg">
      <h1>{{ page_h1 }}</h1>
      <p class="prose">{{ page_lead }}</p>
    </div>
  </main>

  <footer role="contentinfo">
    <!-- Universal footer (NAP + hours + disclaimer + legal links) lands in Plan 04. Placeholder. -->
    <div class="container-xl">
      <p><em>Footer component lands in phase 01 Plan 04.</em></p>
    </div>
  </footer>

  <!-- Progressive-enhancement JS (nav toggle, form spam filter, calendar lazy-mount).
       Add as needed per page. Never blocking. -->
</body>
</html>
```

CRITICAL:
- The `{{ ... }}` placeholders are literal text — this template is copied and hand-filled by later plans, NOT run through a template engine.
- Do NOT hardcode a GA4 id (Mr Green → Arcadian pollution incident). The GA4 script block is COMMENTED and marked with GA4-BEGIN / GA4-END sentinels so the identity guard (Plan 03) can inject/replace it per site.
- Do NOT add nav links or footer NAP here — Plan 04 owns those. This is scaffolding only.
- One <h1>, semantic landmarks (`role="banner"`, `<main>`, `role="contentinfo"`), skip link as first tab stop.
- All external URLs use https and match childcustodyanddivorce.com.
  </action>
  <verify>
    <automated>test -f /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'lang="en-US"' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'class="skip-link"' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'role="banner"' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'role="contentinfo"' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q '<main id="main">' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'rel="preload"' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'tokens.css' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'og:image' /Users/brianegan/Desktop/burkett-law/templates/base.html && grep -q 'GA4-BEGIN' /Users/brianegan/Desktop/burkett-law/templates/base.html && ! grep -E 'G-[A-Z0-9]{10}' /Users/brianegan/Desktop/burkett-law/templates/base.html && echo "PASS"</automated>
  </verify>
  <done>templates/base.html exists with lang="en-US", skip link, semantic landmarks (banner/main/contentinfo), font preloads, tokens.css + base.css links, OG image slot, GA4 slot commented (no real id), schema slot commented. Zero hardcoded GA4 measurement ids.</done>
</task>

</tasks>

<verification>
Phase 1 Plan 02 verification:
- `find /Users/brianegan/Desktop/burkett-law/assets -type f` returns tokens.css, base.css, both WOFF2 files, both LICENSE files.
- `grep -c '@font-face' /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css` returns 2.
- `grep -c 'var(--' /Users/brianegan/Desktop/burkett-law/assets/css/base.css` returns ≥ 15 (base.css uses tokens throughout).
- `wc -l /Users/brianegan/Desktop/burkett-law/assets/css/tokens.css` returns ≥ 140 (full token block).
- No file at `/Users/brianegan/Desktop/burkett-law/` contains a real GA4 measurement ID matching `G-[A-Z0-9]{10}` outside of a commented block.
- Open templates/base.html in a browser via a local file server — the placeholder H1 renders in Fraunces, body in Inter, page bg is cream. (Manual dev-time check; not part of automated verify.)
</verification>

<success_criteria>
- Design tokens (all ~90 custom properties from DESIGN.md §13) live at assets/css/tokens.css
- Self-hosted Fraunces + Inter variable WOFF2 files at assets/fonts/ with OFL LICENSE files
- @font-face declarations use font-display: swap
- base.css provides reset + headings + skip-link + focus-visible + .prose + container-* + prefers-reduced-motion
- templates/base.html has semantic landmarks (banner/main/contentinfo), skip link as first tab stop, font preloads, tokens+base CSS links, canonical/OG/favicon slots, and commented GA4 + schema slots
- No hardcoded GA4 id anywhere (Mr Green pollution prevention)
- No hex color literals in base.css (all color via tokens)
</success_criteria>

<output>
After completion, create `.planning/phases/01-foundation-design-system-validators/01-02-SUMMARY.md` recording:
- Final font file sizes (Fraunces WOFF2 KB, Inter WOFF2 KB) — for Phase 6 performance baseline
- Any deviations from DESIGN.md §13 tokens (should be zero)
- Which URL was used to source each WOFF2 (Google gstatic vs rsms GitHub) — for future re-fetch
- The template consumer pattern: "future pages copy templates/base.html and fill {{ ... }} placeholders manually"
</output>
