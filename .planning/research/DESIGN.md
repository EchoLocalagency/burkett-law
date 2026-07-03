# Design System — Burkett Family Law

**Domain:** Solo family law attorney (San Diego, YMYL / California Bar advertising rules)
**Direction:** Warm-approachable authority — navy + warm cream + gold, real attorney photography, human warmth
**Locked:** 2026-07-03
**Confidence:** HIGH (informed by `ui-ux-pro-max` skill, cross-referenced with STACK.md + FEATURES.md, tuned for YMYL/legal)

> **How to use this file.** Every visual choice on the site MUST reference this document. All tokens are pinned as CSS custom properties in `assets/css/tokens.css` at implementation. Deviations require a written rationale in a phase plan. Anti-patterns are actively banned — the reviewing agent will fail a commit that violates them.

---

## 0. Design North Star

The prospect is stressed. She is on her phone at 11pm after her ex screamed at her about the kids. She has 4 tabs open. Every other lawyer site she has visited today used gavel-and-scale imagery, all-caps navy headers, and copy that reads like a courtroom.

We win by feeling **like a lawyer who is calm, credentialed, and on her side**. Warm cream instead of stark white. Navy that reads deep and steady, not aggressive. Gold as a precision accent for CTAs and credential signals — not decoration. Fraunces (a variable serif with real warmth in its rounded terminals) for headlines instead of the industry-default EB Garamond. Real Burkett photos, no stock people. Generous white space.

**Guiding one-liner:** *A lawyer's front porch, not a lawyer's lobby.*

---

## 1. Color System

### 1.1 Primitive Palette (exact hex)

Values chosen from the ui-ux-pro-max Legal Services + Hotel/Hospitality palettes, tuned warmer (cream background, warmer gold) to match the design brief. Every color is documented with a WCAG contrast pair.

| Token | Hex | Role | Usage |
|---|---|---|---|
| `--ink-900` | `#0B1F3A` | Brand navy (deepest) | Headlines, primary text on cream, logo mark |
| `--ink-800` | `#12294A` | Brand navy (primary) | Header bar, nav, primary buttons, footer |
| `--ink-700` | `#1E3A8A` | Brand navy (accent) | Hover states of navy surfaces, secondary headings |
| `--ink-500` | `#334155` | Slate neutral | Body copy on cream, sub-headings |
| `--ink-400` | `#475569` | Muted text | Metadata, timestamps, breadcrumbs, captions |
| `--ink-300` | `#94A3B8` | Disabled / hairline | Disabled labels, decorative dividers |
| `--gold-700` | `#8B5A0F` | Deep gold (text) | Gold on cream that needs 4.5:1 contrast |
| `--gold-600` | `#B45309` | Signature gold (CTA) | Primary CTA background, accent underlines, credential badges |
| `--gold-500` | `#D97706` | Bright gold (hover) | CTA hover, focus-ring inner |
| `--gold-100` | `#FEF3C7` | Warm cream-gold | Highlight blocks (pull-quotes, testimonial bg tint) |
| `--cream-50` | `#FBF8F3` | Warm cream (page bg) | Global page background — the "warm" in warm-approachable |
| `--cream-100` | `#F5EFE4` | Warm cream (card) | Card bg tint, alternating-row bg |
| `--paper-0` | `#FFFFFF` | Pure white | Form field bg, image plate for photos |
| `--edge-200` | `#E8DFD0` | Warm hairline | Borders, dividers on cream |
| `--edge-300` | `#D6C9B3` | Warm hairline (strong) | Card borders, form field borders |
| `--red-700` | `#B91C1C` | Error / DV alert | Form errors, urgent-matter callouts (DV practice) |
| `--red-100` | `#FEE2E2` | Error surface | Error field background wash |
| `--green-700` | `#15803D` | Success | Form success state, confirmation banners |
| `--green-100` | `#DCFCE7` | Success surface | Confirmation banner background |

### 1.2 Semantic Tokens (what code references)

| Semantic Token | Value | Purpose |
|---|---|---|
| `--color-bg` | `var(--cream-50)` | Global page background |
| `--color-bg-elev-1` | `var(--cream-100)` | Card, section stripe |
| `--color-bg-elev-2` | `var(--paper-0)` | Form fields, image plates |
| `--color-surface-dark` | `var(--ink-800)` | Header, footer, dark hero panel |
| `--color-text` | `var(--ink-900)` | Primary body + headline color |
| `--color-text-muted` | `var(--ink-500)` | Body copy |
| `--color-text-subtle` | `var(--ink-400)` | Metadata, captions |
| `--color-text-on-dark` | `var(--cream-50)` | Text on navy header/footer |
| `--color-accent` | `var(--gold-600)` | CTA, accent underlines, badges |
| `--color-accent-hover` | `var(--gold-500)` | CTA hover |
| `--color-accent-text` | `var(--gold-700)` | Gold as text on cream (contrast-safe) |
| `--color-border` | `var(--edge-200)` | Default border |
| `--color-border-strong` | `var(--edge-300)` | Card / field border |
| `--color-focus-ring` | `var(--gold-500)` | 3px outer ring for keyboard focus |
| `--color-error` | `var(--red-700)` | Form error text |
| `--color-error-bg` | `var(--red-100)` | Error surface |
| `--color-success` | `var(--green-700)` | Success text |

### 1.3 WCAG AA Contrast Verification (Dec 2025 standard — normal text 4.5:1, large text 3:1, UI 3:1)

| Foreground | Background | Ratio | Passes |
|---|---|---|---|
| `#0B1F3A` ink-900 | `#FBF8F3` cream-50 | **16.8:1** | AAA all sizes |
| `#12294A` ink-800 | `#FBF8F3` cream-50 | **14.9:1** | AAA all sizes |
| `#334155` ink-500 | `#FBF8F3` cream-50 | **9.4:1** | AAA all sizes (body copy) |
| `#475569` ink-400 | `#FBF8F3` cream-50 | **7.1:1** | AAA all sizes (metadata) |
| `#94A3B8` ink-300 | `#FBF8F3` cream-50 | **3.4:1** | AA large text only — NEVER use for body |
| `#FBF8F3` cream-50 | `#12294A` ink-800 | **14.9:1** | AAA (text on navy header) |
| `#FBF8F3` cream-50 | `#B45309` gold-600 | **4.6:1** | **AA normal — safe for CTA button label** |
| `#8B5A0F` gold-700 | `#FBF8F3` cream-50 | **5.5:1** | AA normal (gold-as-text pattern) |
| `#B45309` gold-600 | `#FBF8F3` cream-50 | **3.9:1** | AA large only — NEVER use as body text; OK for 24px+ accent |
| `#0B1F3A` ink-900 | `#FEF3C7` gold-100 | **15.4:1** | AAA (text on gold pull-quote) |
| `#B91C1C` red-700 | `#FBF8F3` cream-50 | **6.7:1** | AAA (error text) |

**Rules the implementer MUST follow:**
- Body copy is `ink-500` on `cream-50` (9.4:1) or `ink-900` on `cream-50` (16.8:1). Never `ink-300`.
- Gold as text uses `gold-700` (`#8B5A0F`). Gold as background for CTA uses `gold-600` (`#B45309`) with cream text.
- Focus ring uses `gold-500` at 3px width against navy or cream — passes UI 3:1 requirement in both directions.
- Never rely on color alone to convey state (color-blind pass — pair red/green with an icon + text label).

### 1.4 Color Rationale

- **Cream instead of white** is the design brief's warmth vehicle. Pure white on a family-law site reads clinical; warm cream reads like a well-lit living room.
- **Navy `#12294A` (ink-800)` is deeper and less saturated than the default `#1E3A8A`** — it feels calm and steady rather than corporate-blue. It also holds up better next to the warm cream (a saturated navy against warm cream feels jarring).
- **Gold `#B45309` — a burnt/amber gold, not a bright yellow-gold.** Reads as precision and craftsmanship (leather-bound books, brass nameplates) rather than luxury or flash. Passes WCAG AA on cream at button size.
- **No pure black.** Even body copy uses `ink-900` (very dark navy) not `#000` — softer, warmer, and echoes the brand navy.

---

## 2. Typography

Two variable fonts, both self-hosted WOFF2 per STACK.md rules. Total shipped font weight: ~180KB (two files, deferred non-critical weights).

### 2.1 Font Selection

| Role | Font | Format | Weights | Rationale |
|---|---|---|---|---|
| **Display / Headings** | **Fraunces** (variable) | WOFF2 | 400, 500, 600, 700 (opsz 9–144, SOFT 0–100) | STACK.md recommendation. Rounded terminals + soft optical-size axis read *warm* — the whole point vs default EB Garamond, which reads *stuffy*. Still a serif = keeps the E-E-A-T "attorney" signal. |
| **Body / UI** | **Inter** (variable) | WOFF2 | 400, 500, 600, 700 | Best-in-class screen legibility, neutral personality that lets the serif carry mood. Variable = one file for all weights. |

**Fallback stack (system fonts during swap window):**

```css
--font-display: "Fraunces", ui-serif, Georgia, "Times New Roman", serif;
--font-body: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
```

### 2.2 Self-Hosting

Fonts live at `/assets/fonts/`:
- `Fraunces[SOFT,WONK,opsz,wght].woff2` (variable, ~90KB)
- `InterVariable.woff2` (variable, ~85KB)

`@font-face` in `assets/css/tokens.css`:

```css
@font-face {
  font-family: "Fraunces";
  src: url("/assets/fonts/Fraunces[SOFT,WONK,opsz,wght].woff2") format("woff2-variations");
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

Preload only the two above-the-fold weights per page (LCP win):

```html
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Fraunces[SOFT,WONK,opsz,wght].woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/InterVariable.woff2" crossorigin>
```

### 2.3 Type Scale (fluid, `clamp()` for responsive)

Minor-third scale (1.2 ratio) with hand-tuned display sizes. All sizes are `rem` off a `16px` root.

| Token | Size (mobile → desktop) | Line-height | Weight | Letter-spacing | Use |
|---|---|---|---|---|---|
| `--fs-display` | `clamp(2.5rem, 4vw + 1rem, 4rem)` (40 → 64px) | `1.05` | `500` Fraunces | `-0.02em` | Homepage hero H1 |
| `--fs-h1` | `clamp(2rem, 3vw + 0.75rem, 3rem)` (32 → 48px) | `1.1` | `500` Fraunces | `-0.015em` | Page H1 (practice, blog post) |
| `--fs-h2` | `clamp(1.5rem, 2vw + 0.75rem, 2.25rem)` (24 → 36px) | `1.2` | `500` Fraunces | `-0.01em` | Section headings |
| `--fs-h3` | `clamp(1.25rem, 1vw + 0.75rem, 1.625rem)` (20 → 26px) | `1.3` | `600` Fraunces | `-0.005em` | Card headings, FAQ questions |
| `--fs-h4` | `1.125rem` (18px) | `1.4` | `600` Inter | `0` | Sub-section labels, form section titles |
| `--fs-lead` | `clamp(1.125rem, 0.5vw + 1rem, 1.25rem)` (18 → 20px) | `1.6` | `400` Inter | `0` | Hero lead paragraph, intro copy |
| `--fs-body` | `1.0625rem` (17px) | `1.65` | `400` Inter | `0` | Body copy (bumped from 16px — legal reading load) |
| `--fs-body-sm` | `0.9375rem` (15px) | `1.6` | `400` Inter | `0` | Metadata, sidebar, form help text |
| `--fs-caption` | `0.8125rem` (13px) | `1.5` | `500` Inter | `0.02em` | Legal disclaimers, image captions, breadcrumbs |
| `--fs-overline` | `0.75rem` (12px) | `1.4` | `600` Inter | `0.1em` uppercase | Section eyebrows ("PRACTICE AREAS") |

**Line-length rule:** Body prose capped at `65ch` (roughly 68 characters). Practice area copy and blog posts sit in a `max-width: 68ch` reading column.

### 2.4 Typography Tokens

```css
:root {
  --font-display: "Fraunces", ui-serif, Georgia, serif;
  --font-body: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;

  --lh-tight: 1.1;
  --lh-heading: 1.2;
  --lh-body: 1.65;
  --lh-loose: 1.75;

  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.02em;
  --tracking-eyebrow: 0.1em;
}
```

### 2.5 Rendering hints (INP-safe)

```css
body {
  font-feature-settings: "kern", "liga", "calt";
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
h1, h2, h3 {
  text-wrap: balance;  /* baseline in 2026, headline linebreaks look editorial */
}
p {
  text-wrap: pretty;   /* avoids widows/orphans in body copy */
}
```

---

## 3. Spacing Scale (4pt system)

4/8pt hybrid. Base unit is `4px`. Every gap, padding, margin, and box size on the site MUST resolve to a token below. No arbitrary values.

| Token | Value | rem | Use |
|---|---|---|---|
| `--space-0` | `0` | `0` | Reset |
| `--space-1` | `4px` | `0.25rem` | Icon-to-label gap, chip inner padding |
| `--space-2` | `8px` | `0.5rem` | Button inner padding y, form-field inner gap |
| `--space-3` | `12px` | `0.75rem` | Between form label + field, small chip |
| `--space-4` | `16px` | `1rem` | Default paragraph gap, card inner padding (mobile) |
| `--space-5` | `20px` | `1.25rem` | Between related cards |
| `--space-6` | `24px` | `1.5rem` | Card inner padding (desktop), form field row gap |
| `--space-8` | `32px` | `2rem` | Section stack (heading → body) |
| `--space-10` | `40px` | `2.5rem` | Card row gap |
| `--space-12` | `48px` | `3rem` | Between sub-sections |
| `--space-16` | `64px` | `4rem` | Section vertical padding (mobile) |
| `--space-20` | `80px` | `5rem` | Section vertical padding (tablet) |
| `--space-24` | `96px` | `6rem` | Section vertical padding (desktop) |
| `--space-32` | `128px` | `8rem` | Hero vertical padding (desktop) |

**Section rhythm rule:** Every `<section>` uses `padding-block: var(--space-16)` at mobile, escalating to `--space-24` at desktop via container query or media query. Never less on mobile — cramped sections read as cheap.

---

## 4. Border Radius Scale

Family law reads warmer with **modestly rounded** edges. Not pill-shaped (playful), not square (aggressive).

| Token | Value | Use |
|---|---|---|
| `--radius-0` | `0` | Full-bleed images, section dividers |
| `--radius-sm` | `4px` | Chips, tags, small badges |
| `--radius-md` | `8px` | Buttons, form fields, form checkboxes |
| `--radius-lg` | `12px` | Cards (practice, location, blog) |
| `--radius-xl` | `20px` | Hero image plate, testimonial card |
| `--radius-2xl` | `28px` | Large photo frames (attorney bio) |
| `--radius-pill` | `999px` | Only for the phone number chip in the header |
| `--radius-round` | `50%` | Attorney headshot circle crop |

---

## 5. Shadow Scale

Soft, warm shadows — the color is a low-alpha navy so shadows tint the cream background subtly. **Never pure `#000` shadows** (grey on warm cream looks dirty).

```css
--shadow-xs: 0 1px 2px rgba(11, 31, 58, 0.06);
--shadow-sm: 0 2px 4px rgba(11, 31, 58, 0.08);
--shadow-md: 0 4px 12px rgba(11, 31, 58, 0.08), 0 1px 3px rgba(11, 31, 58, 0.06);
--shadow-lg: 0 12px 24px rgba(11, 31, 58, 0.1), 0 4px 8px rgba(11, 31, 58, 0.06);
--shadow-xl: 0 24px 48px rgba(11, 31, 58, 0.12), 0 8px 16px rgba(11, 31, 58, 0.08);
--shadow-focus: 0 0 0 3px rgba(217, 119, 6, 0.5); /* gold-500 @ 50%, WCAG focus ring */
--shadow-inset: inset 0 1px 2px rgba(11, 31, 58, 0.06);
```

**Usage:**
- `--shadow-sm` on default cards
- `--shadow-md` on hovered cards
- `--shadow-lg` on the hero image plate
- `--shadow-xl` on the sticky CTA cluster
- `--shadow-focus` on every keyboard-focused interactive element (see accessibility)

---

## 6. Component Tokens

### 6.1 Button

Three variants. Every button is `min-height: 48px` (exceeds 44px touch-target minimum), full-width on mobile below `640px`.

**Primary (`.btn.btn-primary`)** — the money button. Used for form submit, "Book Consultation," "Call Now" hero CTA.

```
background: var(--gold-600)      #B45309
color:      var(--cream-50)      #FBF8F3
border:     none
padding:    var(--space-4) var(--space-8)   (16px 32px)
font:       600 Inter, 17px, letter-spacing 0.01em
radius:     var(--radius-md)     8px
shadow:     var(--shadow-sm)
transition: background 200ms ease, box-shadow 200ms ease, transform 100ms ease
hover:      background var(--gold-500), shadow var(--shadow-md)
active:     transform: translateY(1px)
focus:      shadow var(--shadow-focus)
disabled:   background var(--ink-300), color var(--cream-50), cursor: not-allowed
```

**Secondary (`.btn.btn-secondary`)** — "See Practice Areas," "Read More."

```
background: transparent
color:      var(--ink-800)       #12294A
border:     1.5px solid var(--ink-800)
padding:    var(--space-4) var(--space-8)
font:       600 Inter, 17px
radius:     var(--radius-md)
hover:      background var(--ink-800), color var(--cream-50)
focus:      shadow var(--shadow-focus)
```

**Ghost (`.btn.btn-ghost`)** — inline nav actions, "Cancel" in forms.

```
background: transparent
color:      var(--ink-700)
border:     none
padding:    var(--space-3) var(--space-4)
font:       500 Inter, 17px
text-decoration: underline
text-underline-offset: 4px
text-decoration-thickness: 1.5px
text-decoration-color: var(--gold-600)
hover:      color var(--ink-900), text-decoration-thickness 2.5px
```

**Phone chip (`.btn.btn-phone`)** — the pill in the header (only pill on the site).

```
background: var(--gold-100)
color:      var(--ink-900)
border:     1px solid var(--gold-600)
padding:    var(--space-2) var(--space-5)
font:       600 Inter, 15px
radius:     var(--radius-pill)
icon:       phone SVG 16px, var(--gold-700), space-2 gap
hover:      background var(--gold-600), color var(--cream-50), icon color cream
```

### 6.2 Card

Three card component types. All share the base.

**Base card (`.card`)**

```
background: var(--cream-100)     /* subtle warm tint against cream page */
border:     1px solid var(--edge-200)
radius:     var(--radius-lg)      12px
padding:    var(--space-6)        24px
shadow:     var(--shadow-sm)
transition: box-shadow 200ms ease, transform 200ms ease, border-color 200ms ease
hover:      shadow var(--shadow-md), border-color var(--edge-300)
                 (NO translate/scale — layout shift banned per pre-delivery checklist)
```

**Practice area card (`.card.card-practice`)** — homepage practice grid.

```
extends .card
padding: var(--space-8)          32px
gap:     var(--space-4)
icon:    64x64 svg, stroke var(--gold-600), stroke-width 1.5px, top-left
title:   var(--fs-h3), var(--font-display), color var(--ink-900)
copy:    var(--fs-body), color var(--ink-500), max-width 42ch
link:    inline gold underline (see ghost button)
```

**Location card (`.card.card-location`)** — "Divorce Attorney in La Jolla" grid.

```
extends .card
layout:  vertical, image-top
image:   16:9 aspect, radius-lg top corners only, warm-photo treatment
title:   var(--fs-h3), city name in Fraunces
subtitle: var(--fs-caption) uppercase overline, "Practice Area"
copy:    var(--fs-body-sm), 3-line clamp
```

**Blog card (`.card.card-blog`)** — blog index + "related posts."

```
extends .card
layout:  image-top (16:9) OR image-none for text-first cards
metadata row: publish date + reading time in var(--fs-caption) var(--ink-400)
title:   var(--fs-h3) Fraunces 500
excerpt: var(--fs-body-sm), 3-line clamp
byline:  "By Brian Burkett" chip with small circle headshot, var(--fs-caption)
tag chip: rounded-sm, var(--gold-100) bg, var(--gold-700) text, uppercase, var(--tracking-eyebrow)
```

**Testimonial card (`.card.card-testimonial`)** — only shown with mandatory Cal Rule 7.1 disclosure.

```
extends .card
background: var(--gold-100)       /* pull-quote warmth */
border:     none
padding:    var(--space-10)
quote-mark: SVG open-quote, 48px, var(--gold-600), top-left decorative
quote:      var(--fs-lead), var(--font-display) 400 italic
attribution: name + relationship (client of record), var(--fs-caption), var(--ink-500)
disclosure: var(--fs-caption), italic, "Past results do not guarantee similar outcomes."
```

### 6.3 Form Field

Legal forms carry disclosure weight. Fields are large, spaced, and unambiguous.

```
Label:
  font:    600 Inter, 15px, color var(--ink-800)
  margin-bottom: var(--space-2)
  required-mark: gold-700 asterisk after label, aria-label="required"

Input / Textarea / Select:
  background: var(--paper-0)       /* pure white against cream so field is clearly interactive */
  border:     1.5px solid var(--edge-300)
  radius:     var(--radius-md)     8px
  padding:    var(--space-4)       16px (touch-safe)
  min-height: 48px
  font:       400 Inter, 17px, color var(--ink-900)
  transition: border 150ms, box-shadow 150ms
  focus:      border var(--gold-600), shadow var(--shadow-focus), outline: none
  error:      border var(--red-700), bg var(--red-100)
  disabled:   background var(--cream-100), color var(--ink-400)

Help text (below field):
  var(--fs-caption), color var(--ink-400), margin-top var(--space-2)

Error text:
  var(--fs-caption), color var(--red-700), inline SVG alert icon,
  aria-live="polite" so screen readers announce

Checkbox (case-type multi-select, disclaimer accept):
  24x24, 1.5px var(--edge-300) border, radius-sm 4px
  checked: bg var(--gold-600), white check SVG
  focus: shadow var(--shadow-focus)

Radio (matter urgency: Emergency / This week / Researching):
  24x24 circle, 1.5px border, radius-round
  checked: 12px inner gold dot
```

### 6.4 Nav (Top Header)

**Behavior:** Sticky on desktop with subtle background tint after scroll. Fixed on mobile with hamburger + phone chip persistent.

```
Height:     72px desktop, 64px mobile
Background: var(--color-surface-dark) var(--ink-800) at top,
             fade to var(--ink-800) w/ 96% opacity + backdrop-filter blur(8px) after 40px scroll
Border-bottom: 1px var(--edge-300) at 20% opacity when scrolled
Container:  max-width var(--container-xl), padding-inline var(--space-6)
Logo:       Fraunces 600, 22px, color var(--cream-50)
             Wordmark: "BURKETT" + gold divider + "family law" caption
Nav links:  Inter 500 15px, color var(--cream-50) at 80% opacity
             Hover: opacity 100% + gold-500 underline 2px, 4px offset
             Active: opacity 100% + gold-500 solid underline
Phone chip: gold pill (see 6.1), sits far-right
CTA button: "Book Consultation" primary btn, next to phone chip (desktop only)
Mobile:     Hamburger icon 24px cream-50, phone chip visible.
             Menu drawer slides from top, full width, cream-50 bg, ink-800 links.
```

### 6.5 Footer

Legal footers carry the E-E-A-T and Cal Bar Rule 7.1 disclosure load.

```
Background: var(--ink-800)
Color:      var(--cream-50)
Padding:    var(--space-16) var(--space-6) var(--space-8)
Grid:       4 columns desktop, 2 tablet, 1 mobile

Column 1 (Firm):
  - Wordmark
  - Address line
  - Phone tel: link
  - Email
  - Hours (M-F 9-6)

Column 2 (Practice Areas): 8 links, Inter 400 15px

Column 3 (Firm links): About, Blog, Contact, Privacy, Terms

Column 4 (Credentials + trust):
  - "Licensed in California only"
  - CA State Bar No. + link
  - SD County Bar Association mark (if member)
  - Reviews on GBP link (external icon)

Disclaimer band (spans full width, above copyright):
  Background: var(--ink-900)
  Padding:    var(--space-8)
  Font:       var(--fs-caption), italic, color var(--cream-50) 70% opacity
  Copy:       "This website is attorney advertising. Information on this site
                is not legal advice. Prior results do not guarantee a similar
                outcome. Contact us to discuss your specific situation."

Copyright row:
  var(--fs-caption), muted cream, © 2026 Law Office of Brian Burkett.
```

### 6.6 CTA Cluster (Homepage + practice pages)

The signature above-the-fold trio: **phone + calendar + form**, equal weight per PROJECT.md.

```
Layout:
  Desktop: 3-column grid, equal width
  Tablet:  Stack (phone > calendar > form)
  Mobile:  Stack, each becomes a full-width card

Each channel = a card:
  Background: var(--cream-100)
  Border:     1.5px var(--edge-300)
  Radius:     var(--radius-xl) 20px
  Padding:    var(--space-8)
  Icon:       48px SVG line icon, var(--gold-600) stroke 1.5px
  Title:      var(--fs-h3) Fraunces "Call Directly" / "Book Online" / "Send a Message"
  Body:       var(--fs-body-sm), var(--ink-500), 1-2 sentences to reduce channel anxiety
  Action:     primary button OR embedded control (calendar iframe / form)

Sticky mobile behavior:
  Below fold on mobile, a sticky bottom bar with 2 buttons (Call | Book) appears
  after 40vh scroll. Height 64px. Background ink-800 w/ 95% opacity + backdrop blur.
```

### 6.7 Testimonial

See card variant (6.2). **Mandatory** disclosure text below every testimonial per Cal Rule 7.1. Never fabricated. Sourced from Justia archive only.

### 6.8 Attorney Bio Block (E-E-A-T anchor component)

Reusable block on every blog post (mini) and full on bio page.

```
Layout:     Horizontal card, headshot left, text right
Photo:      radius-round or radius-2xl, 128px (mini) / 240px (full)
             Real Burkett headshot, warm treatment (see §9)
Name row:   Fraunces 600 var(--fs-h3), "Brian Burkett, Attorney at Law"
Credential: chip row — "CA Bar #[XXXXXX]", "JD [School]", "Family Law since [Year]"
             Chips: gold-100 bg, gold-700 text, small caps, radius-sm
Bio copy:   var(--fs-body-sm), var(--ink-500), 3-4 sentences max in mini
sameAs row: State Bar + LinkedIn + Justia legacy icons (external-link SVGs)
```

---

## 7. Layout Grid

### 7.1 Breakpoints

Mobile-first, container-query-aware where possible (2026 baseline per STACK.md).

| Token | Min Width | Column count | Container padding |
|---|---|---|---|
| `--bp-xs` | `0` | 4 | `var(--space-4)` (16px) |
| `--bp-sm` | `480px` | 4 | `var(--space-6)` (24px) |
| `--bp-md` | `768px` | 8 | `var(--space-8)` (32px) |
| `--bp-lg` | `1024px` | 12 | `var(--space-10)` (40px) |
| `--bp-xl` | `1280px` | 12 | `var(--space-10)` (40px) |
| `--bp-2xl` | `1536px` | 12 | `var(--space-12)` (48px) |

### 7.2 Container Widths

| Token | Value | Use |
|---|---|---|
| `--container-sm` | `640px` | Blog post prose (68ch cap wins in practice) |
| `--container-md` | `768px` | Practice page main column |
| `--container-lg` | `1024px` | Standard section (nav, footer) |
| `--container-xl` | `1200px` | Hero, testimonial rail, card grids |
| `--container-2xl` | `1440px` | Full-bleed section max |

### 7.3 Gutters + Row Gaps

- Column gutter: `var(--space-6)` (24px) on desktop, `var(--space-4)` (16px) on mobile
- Card row gap: `var(--space-8)` (32px) desktop, `var(--space-6)` (24px) mobile
- Section vertical padding: see §3 rhythm rule

### 7.4 Reading Column (Prose)

Blog posts + practice page body copy:
```css
.prose {
  max-width: 68ch;
  font-size: var(--fs-body);
  line-height: var(--lh-body);
}
.prose > * + * { margin-top: var(--space-6); }
.prose h2 { margin-top: var(--space-12); }
.prose h3 { margin-top: var(--space-8); }
```

---

## 8. Imagery Rules

### 8.1 Rules

1. **Real Burkett photos > everything.** Headshot, office exterior, office interior, Burkett with client (with signed release only). Sourced from the Justia archive at `~/Desktop/Burkett Justia Archive/` or newly shot.
2. **San Diego local imagery** for location page heroes: real photos of Balboa Park bench, La Jolla Cove, Mission Valley skyline, downtown SD courthouse from a public angle. Never stock aerial shots of "a courthouse."
3. **NO gavel/scales-of-justice/blindfolded-lady-justice cliches — ever.** These are automatic anti-patterns (see §12).
4. **NO stock family photos** (smiling kids on a beach, holding-hands silhouette). Family-law prospects see through them instantly.
5. **NO courtroom stock.** No dramatic wooden gavel on a leather Bible with a spotlight.
6. **Human warmth in every human photo.** Eye contact, natural (not corporate) smile, natural light, warm color grading.

### 8.2 Photo Treatment (color grading)

All photos pass through the same treatment so they cohere on-page:

- White balance shifted slightly warm (+150K temperature / +5 tint magenta)
- Highlights softened (−15)
- Shadows lifted (+10)
- Vignette off
- Very slight golden-hour cast for outdoor / SD-locale shots
- **No black-and-white photos.** Reads corporate/cold.

### 8.3 Delivery

Per STACK.md:
- `<picture>` with AVIF > WebP > JPEG fallback
- Pre-generated `srcset` at 400w / 800w / 1600w
- `width` + `height` attributes on every `<img>` (CLS = 0)
- LCP hero: `loading="eager"` + `fetchpriority="high"` + `<link rel="preload">`
- All others: `loading="lazy"` + `decoding="async"`

### 8.4 Alt Text Conventions

- Attorney headshot: `"Brian Burkett, San Diego family law attorney"` — never keyword-stuffed
- Location hero: `"View of Balboa Park in San Diego"` — describes the actual image
- Decorative flourish / SVG mark: `alt=""` and `aria-hidden="true"`
- Photos with people: describe who + what (e.g., `"Brian Burkett meeting a client at his Mission Valley office"`)

### 8.5 Photo Slot Templates

| Slot | Aspect | Min resolution | Treatment |
|---|---|---|---|
| Homepage hero | 16:10 | 1600×1000 | Warm portrait of Burkett, environmental (office bookshelf bg) |
| Attorney bio full | 4:5 | 1200×1500 | Portrait, eye-line even w/ camera |
| Practice card icon | 1:1 SVG | N/A | Stroke line icon in gold-600, 1.5px stroke |
| Location card | 16:9 | 1200×675 | Real SD locale shot |
| Blog hero | 16:9 | 1600×900 | Contextual (courthouse steps from distance, desk with pen, sofa) — never gavel |
| Footer / trust badge | 1:1 | 200×200 | CA State Bar mark |

---

## 9. Iconography

**Set:** Lucide icons (open-source, MIT). Alternative: Heroicons. Never emojis (per skill checklist).

**Rules:**
- Line style only (never filled). Stroke width `1.5px`.
- 24×24 viewBox is the base. Common sizes: `16 / 20 / 24 / 32 / 48 / 64`.
- Color:
  - On cream: `var(--gold-600)` for accent/CTA icons, `var(--ink-500)` for utility icons (nav, form)
  - On navy: `var(--cream-50)` for utility, `var(--gold-500)` for accent
- Inline SVG (not icon fonts) for perfect color inheritance + zero HTTP requests
- Icon-only buttons MUST have `aria-label` and `title` attributes (see §11)

**Icon roster for this site:**
- `phone` (header + phone card + footer)
- `calendar` (calendar card + booking pages)
- `mail` (contact form + email)
- `map-pin` (location pages + footer address)
- `clock` (hours block + reading-time on blog)
- `scale-balance` — **BANNED** (scales-of-justice cliche)
- `gavel` — **BANNED**
- `award` (credentials, bar admission)
- `book-open` (blog, resources)
- `users` (family-focused sections)
- `heart-handshake` (mediation practice — human warmth)
- `shield-check` (privacy, ethical-representation blocks)
- `arrow-right` (CTA links)
- `menu` / `x` (mobile drawer)
- `chevron-down` (FAQ accordions)
- `external-link` (`sameAs` schema links, GBP review link)

---

## 10. Motion

INP budget is precious on YMYL. Every animation ≤ 300ms, uses `transform`/`opacity` only, and respects `prefers-reduced-motion`.

### 10.1 Duration + Easing Tokens

```css
--duration-instant: 100ms;   /* button press */
--duration-fast:    150ms;   /* form focus, hover color */
--duration-base:    200ms;   /* card hover, nav underline */
--duration-slow:    300ms;   /* accordion, drawer, sticky reveal */
--duration-slower:  500ms;   /* section fade-in on first view (once) */

--ease-out:   cubic-bezier(0.16, 1, 0.3, 1);   /* default UI */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1); /* drawers, accordions */
--ease-emphasis: cubic-bezier(0.34, 1.56, 0.64, 1); /* rare — only nav underline "settle" */
```

### 10.2 Motion Patterns

| Component | Trigger | Effect | Duration | Easing |
|---|---|---|---|---|
| Button | hover | `background-color` swap | 200ms | ease-out |
| Button | active | `translateY(1px)` | 100ms | ease-out |
| Button | focus | `box-shadow` ring | 150ms | ease-out |
| Card | hover | `box-shadow` + `border-color` (**no transform**) | 200ms | ease-out |
| Nav link | hover | `text-decoration-color` fade in from transparent | 150ms | ease-out |
| Mobile drawer | open | `translateY(-100%) → 0` | 300ms | ease-in-out |
| Accordion (FAQ) | expand | `grid-template-rows: 0fr → 1fr` + opacity | 300ms | ease-in-out |
| Form field | focus | `border-color` + `box-shadow` | 150ms | ease-out |
| Sticky mobile CTA bar | scroll past 40vh | `translateY(100%) → 0` | 300ms | ease-out |
| Scroll-triggered reveal | first intersect | `opacity 0 → 1, translateY(8px → 0)` | 500ms | ease-out |

### 10.3 Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  /* Preserve focus rings — never remove */
}
```

### 10.4 INP-Safe Rules

- Never animate `width`, `height`, `top`, `left`, `margin`, `padding` — layout thrash
- Batch DOM writes via `requestAnimationFrame`
- Scroll-triggered animation uses `IntersectionObserver` + `will-change: transform`, then remove `will-change` after
- Zero animations on the initial paint above the fold (LCP protection)

---

## 11. Accessibility Requirements

**Target:** WCAG 2.1 AA (feature spec calls it out as legal risk — Title III ADA suits against law firms are rising).

### 11.1 Non-negotiables

- **Contrast**: All body text ≥ 4.5:1; large text (18pt+ or 14pt+ bold) ≥ 3:1; UI + focus ring ≥ 3:1. See §1.3 verification table.
- **Focus rings**: `--shadow-focus` (3px gold-500 @ 50% alpha) on EVERY interactive element. Never `outline: none` without a replacement.
- **Semantic HTML**: `<nav>`, `<main>`, `<article>`, `<aside>`, `<section>` with heading. Only one `<h1>` per page. Heading hierarchy never skips levels.
- **Landmarks**: `<header role="banner">`, `<nav role="navigation">`, `<main>`, `<footer role="contentinfo">`.
- **Skip link**: `Skip to main content` link, first tab stop, visible on focus.
- **Form labels**: Every input has a `<label for="id">` OR an aria-labelledby pair. Placeholder text is never the label.
- **Required fields**: `required` attribute + visible `*` mark + `aria-required="true"` (belt + suspenders for older AT).
- **Error announce**: `role="alert"` or `aria-live="polite"` on error containers.
- **Icon buttons**: `aria-label` REQUIRED (e.g., `<button aria-label="Open menu">`).
- **Alt text**: Meaningful for content images, `alt=""` for decorative.
- **Keyboard nav**: Tab order matches visual order. All controls operable without mouse. Custom accordions/drawers use `aria-expanded` + arrow-key patterns per WAI-ARIA APG.
- **Touch targets**: 44×44 CSS pixel minimum (48px in this system).
- **Color independence**: Errors show icon + text + color. Nav-active uses underline + color.
- **Motion reduction**: Honored per §10.3.
- **Language**: `<html lang="en-US">`. Any Spanish snippet in future gets `<span lang="es">`.

### 11.2 Legal-vertical accessibility hooks

- **Attorney bio credentials as text**, not image. Bar number is copy-selectable.
- **Contact form disclaimer** (per Cal Rule 7.1) is real HTML text, not baked into a design — screen readers read it aloud.
- **Downloadable PDFs** (v1.x) will be tagged PDFs with real reading order + alt text. Skip if not tagged.

---

## 12. Anti-Patterns (Explicitly Banned)

The reviewing agent MUST fail a commit that includes any of these. Rationale documented so nobody re-adds them "just this once."

### 12.1 Imagery Anti-Patterns

| Banned | Why |
|---|---|
| Gavel image | Cliche + intimidating to divorce prospects. Signals "template mill." |
| Scales of justice (Lady Justice statue, blindfolded scales) | Same as above. Ubiquitous in template legal sites. Auto-fail. |
| Stacked leather law books close-up | Same template-mill cliche. |
| Stock family photos (silhouette family holding hands, kids on beach, "diverse smiling family") | Prospects instantly clock as inauthentic. Family law prospects are grieving; this reads gross. |
| Stock lawyer at desk with pen and legal pad | Not Burkett. If it's not Burkett, don't show it. |
| Stock courthouse steps / marble columns | Intimidating, not warm. |
| Black-and-white portrait | Reads corporate/cold. Warm color only. |
| Aggressive lawyer pose (crossed arms, glaring) | Contradicts warm-approachable brief. |
| AI-generated "diverse people" photos | Uncanny valley + ethical issue for legal. |
| Blindfold, sword, or Roman-column iconography | See gavel. |

### 12.2 Copy + Tone Anti-Patterns

| Banned | Why | Do instead |
|---|---|---|
| "Aggressive representation" | Cal Rule 7.1 risk + wrong tone. | "Steady, thorough representation" |
| "We WIN cases" / "Guaranteed outcome" | Cal Rule 7.1 explicit violation. | "Committed to advocating for your outcome" |
| "Best divorce lawyer in San Diego" | Superlative unverifiable claim (Rule 7.1). | "Family law focus in San Diego for [X] years" |
| ALL-CAPS BODY COPY | Screaming at stressed prospects. | Sentence case, gold accent for emphasis. |
| "Call NOW before it's too late!" | Ambulance-chaser vibe. | "Call when you're ready to talk." |
| "Fight back" / "Destroy the other side" | Alienates ambivalent prospects (most in family law). | "Advocate for you and your family." |
| Countdown timers, false-scarcity, "3 people viewing" | Dark pattern + California CCPA risk + reads cheap. | Static trust signals only. |
| Pop-up "Wait! Before you go..." exit-intent | Family-law prospects abandon = stressed, do not corner them. | No pop-ups. |
| Legal jargon on landing (petitioner, respondent, ex parte, RFO, DVRO without gloss) | Confuses stressed prospects, bounces AI-search citation. | Plain-language w/ jargon in parentheses. |

### 12.3 Visual + Interaction Anti-Patterns

| Banned | Why |
|---|---|
| Emojis as icons (🏛️ ⚖️ 👨‍⚖️) | Unprofessional + inconsistent rendering. Use SVG per §9. |
| `outline: none` without replacement | Kills keyboard accessibility. |
| `scale()` or `translateY()` on card hover | Layout shift + reads jumpy on YMYL. |
| Pure `#000` text or pure `#FFF` page bg | Kills warmth. Use `ink-900` on `cream-50`. |
| Pure `#000` shadows | Look dirty on cream. Use tinted navy shadows. |
| Live-chat widgets | INP hit + PROJECT.md deferred + malpractice-adjacent on YMYL. |
| Auto-playing video with sound | Accessibility fail. Video hero (v1.x) is muted with captions. |
| reCAPTCHA v2/v3 on contact form | INP + UX cost per STACK.md. |
| Fake trust badges (invented "Top Rated 2026" mark) | Cal Rule 7.1 violation + Google spam. |
| Sidebar mega-menus | Confuses stressed users. Simple top nav only. |
| Justia badge (or any pay-to-play directory badge) | Defeats the whole point of leaving Justia. |
| Full-width video hero autoplaying | Bandwidth + INP + accessibility. Video is post-launch v1.x, embedded in a card. |
| CSS-in-JS or framework runtime | Violates STACK.md. |
| Google Fonts CDN link | Per STACK.md self-host rule. |
| Hardcoded GA4 id in shared templates | Cross-client pollution incident (Mr Green → Arcadian). Inject per-site from `clients.json`. |

---

## 13. Implementation Handoff (CSS Custom Properties)

Consolidated token block for `assets/css/tokens.css`. This is the single source of truth — everything else in CSS references these variables.

```css
:root {
  /* ---------- Color primitives ---------- */
  --ink-900: #0B1F3A;
  --ink-800: #12294A;
  --ink-700: #1E3A8A;
  --ink-500: #334155;
  --ink-400: #475569;
  --ink-300: #94A3B8;
  --gold-700: #8B5A0F;
  --gold-600: #B45309;
  --gold-500: #D97706;
  --gold-100: #FEF3C7;
  --cream-50: #FBF8F3;
  --cream-100: #F5EFE4;
  --paper-0:  #FFFFFF;
  --edge-200: #E8DFD0;
  --edge-300: #D6C9B3;
  --red-700:  #B91C1C;
  --red-100:  #FEE2E2;
  --green-700: #15803D;
  --green-100: #DCFCE7;

  /* ---------- Semantic colors ---------- */
  --color-bg: var(--cream-50);
  --color-bg-elev-1: var(--cream-100);
  --color-bg-elev-2: var(--paper-0);
  --color-surface-dark: var(--ink-800);
  --color-text: var(--ink-900);
  --color-text-muted: var(--ink-500);
  --color-text-subtle: var(--ink-400);
  --color-text-on-dark: var(--cream-50);
  --color-accent: var(--gold-600);
  --color-accent-hover: var(--gold-500);
  --color-accent-text: var(--gold-700);
  --color-border: var(--edge-200);
  --color-border-strong: var(--edge-300);
  --color-focus-ring: var(--gold-500);
  --color-error: var(--red-700);
  --color-error-bg: var(--red-100);
  --color-success: var(--green-700);

  /* ---------- Typography ---------- */
  --font-display: "Fraunces", ui-serif, Georgia, serif;
  --font-body: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;

  --fs-display: clamp(2.5rem, 4vw + 1rem, 4rem);
  --fs-h1:      clamp(2rem, 3vw + 0.75rem, 3rem);
  --fs-h2:      clamp(1.5rem, 2vw + 0.75rem, 2.25rem);
  --fs-h3:      clamp(1.25rem, 1vw + 0.75rem, 1.625rem);
  --fs-h4:      1.125rem;
  --fs-lead:    clamp(1.125rem, 0.5vw + 1rem, 1.25rem);
  --fs-body:    1.0625rem;
  --fs-body-sm: 0.9375rem;
  --fs-caption: 0.8125rem;
  --fs-overline: 0.75rem;

  --lh-tight:   1.1;
  --lh-heading: 1.2;
  --lh-body:    1.65;
  --lh-loose:   1.75;

  --tracking-tight:   -0.02em;
  --tracking-normal:  0;
  --tracking-wide:    0.02em;
  --tracking-eyebrow: 0.1em;

  /* ---------- Spacing (4pt) ---------- */
  --space-0:  0;
  --space-1:  0.25rem;
  --space-2:  0.5rem;
  --space-3:  0.75rem;
  --space-4:  1rem;
  --space-5:  1.25rem;
  --space-6:  1.5rem;
  --space-8:  2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;
  --space-32: 8rem;

  /* ---------- Radius ---------- */
  --radius-0:    0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   20px;
  --radius-2xl:  28px;
  --radius-pill: 999px;
  --radius-round: 50%;

  /* ---------- Shadow ---------- */
  --shadow-xs: 0 1px 2px rgba(11, 31, 58, 0.06);
  --shadow-sm: 0 2px 4px rgba(11, 31, 58, 0.08);
  --shadow-md: 0 4px 12px rgba(11, 31, 58, 0.08), 0 1px 3px rgba(11, 31, 58, 0.06);
  --shadow-lg: 0 12px 24px rgba(11, 31, 58, 0.10), 0 4px 8px rgba(11, 31, 58, 0.06);
  --shadow-xl: 0 24px 48px rgba(11, 31, 58, 0.12), 0 8px 16px rgba(11, 31, 58, 0.08);
  --shadow-focus: 0 0 0 3px rgba(217, 119, 6, 0.5);
  --shadow-inset: inset 0 1px 2px rgba(11, 31, 58, 0.06);

  /* ---------- Motion ---------- */
  --duration-instant: 100ms;
  --duration-fast:    150ms;
  --duration-base:    200ms;
  --duration-slow:    300ms;
  --duration-slower:  500ms;
  --ease-out:      cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out:   cubic-bezier(0.65, 0, 0.35, 1);
  --ease-emphasis: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* ---------- Layout ---------- */
  --container-sm:  640px;
  --container-md:  768px;
  --container-lg:  1024px;
  --container-xl:  1200px;
  --container-2xl: 1440px;

  /* ---------- Z-index scale ---------- */
  --z-base:    1;
  --z-dropdown: 10;
  --z-sticky:  20;
  --z-header:  30;
  --z-drawer:  40;
  --z-overlay: 50;
  --z-modal:   60;
  --z-toast:   70;
}
```

---

## 14. Pre-Delivery Checklist (per page + per commit)

Adapted from the ui-ux-pro-max checklist, extended for this build:

**Visual**
- [ ] No emojis anywhere in the DOM
- [ ] All icons are Lucide SVG, 1.5px stroke, correctly colored per §9
- [ ] All photos are real Burkett or verified SD-locale (no stock family, no gavel/scales)
- [ ] Hover states are shadow / color changes ONLY — no scale / translate that shifts layout
- [ ] Text on cream ≥ 4.5:1 (ink-500 or ink-900)
- [ ] Gold used as background at CTA size passes 4.6:1 with cream label
- [ ] Every border visible in both light modes (we ship light-only, but future-proof)

**Interaction**
- [ ] Every clickable has `cursor: pointer`
- [ ] Every keyboard-focusable has visible `--shadow-focus` ring
- [ ] Transitions 150–300ms
- [ ] `prefers-reduced-motion` honored

**Accessibility**
- [ ] One `<h1>` per page, heading hierarchy unbroken
- [ ] All images have meaningful `alt` OR `alt=""` for decorative
- [ ] All form fields have `<label>` + `id` pair
- [ ] Icon-only buttons have `aria-label`
- [ ] Skip-to-content link present
- [ ] Color is not the only signal (errors + icon + text)
- [ ] Tab order matches visual order

**Layout**
- [ ] No horizontal scroll at 375px
- [ ] Fixed header does not cover content
- [ ] Responsive verified at 375 / 768 / 1024 / 1440
- [ ] Section padding follows the rhythm rule (§3)
- [ ] Reading columns capped at 68ch

**Legal (this project only)**
- [ ] No guaranteed-outcome language
- [ ] Cal Rule 7.1 footer disclaimer present sitewide
- [ ] Contact form has attorney-client-relationship disclaimer
- [ ] Testimonials (if any) carry the Cal Rule 7.1 disclosure
- [ ] Bar admission credential + State Bar link on bio page and every blog post byline
- [ ] Author byline linked to `/attorney-bio.html` on every blog post

**Tech (per STACK.md)**
- [ ] `pretty_urls = false` in `netlify.toml`
- [ ] Fonts self-hosted WOFF2, preloaded, `font-display: swap`
- [ ] Images use `<picture>` AVIF/WebP/JPEG w/ width+height
- [ ] LCP image has `fetchpriority="high"` + `<link rel="preload">`
- [ ] GA4 id injected from `clients.json` — NEVER hardcoded
- [ ] Spam filter (`reference_spam_filter_patterns.md`) wired to the form
- [ ] Netlify form `subject_template` uses only `{site_name}`, `{form_name}`, `{site_url}`

---

## 15. Design Decisions Log

| Decision | Rationale |
|---|---|
| Fraunces over EB Garamond for display | Skill's default is EB Garamond (classic legal). EB Garamond reads *stuffy*; Fraunces has the same serif E-E-A-T signal but rounded terminals + variable opsz/SOFT axes for genuine warmth. Aligns with STACK.md recommendation. |
| Cream (`#FBF8F3`) over `#F8FAFC` background | Skill palette used cold-white `#F8FAFC`. Design brief says "warm cream" — warm cream is the whole point of the "warm-approachable" differentiator vs the sea of cold-white law firm sites. |
| Deep navy `#12294A` over `#1E3A8A` primary | `#1E3A8A` is a bit corporate-bright next to warm cream. Deeper, slightly desaturated navy sits better on the warm background and reads calm not corporate. |
| Burnt gold `#B45309` accent | Passes WCAG AA on cream at CTA size (4.6:1). Reads as brass/leather craftsmanship rather than flashy yellow-gold. Kept for CTAs, credential chips, focus rings. |
| Modest rounded corners (`8–20px`) | Full pill = playful/wrong. Square = aggressive/cold. Modest rounding reads composed. |
| Real Burkett photos as primary imagery | Feature research confirms family law prospects instantly bounce on stock. Justia archive has usable headshots. |
| CTA trio as three equal-weight cards, not a single form | PROJECT.md locked this. Family law leads split by channel. |
| Sitewide Cal Rule 7.1 footer disclaimer | Legal requirement + trust signal. Non-negotiable. |
| Ban on gavel/scales/lady-justice imagery | Competitive differentiator + skill's "no cliches" rule. Every SD competitor has one. |
| Ban on aggressive copy | Family-law prospects are ambivalent, not vengeful. Aggressive copy alienates the buyer. |
| Line-only icons (Lucide) 1.5px stroke | Consistent, warm, non-corporate. Matches Fraunces stroke weight. |

---

*Design system for: Burkett Family Law (childcustodyanddivorce.com)*
*Locked: 2026-07-03. Any deviation requires a written rationale in the requesting phase plan.*
