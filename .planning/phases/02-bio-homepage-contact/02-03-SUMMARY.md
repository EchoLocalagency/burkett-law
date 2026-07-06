---
phase: 02-bio-homepage-contact
plan: 03
subsystem: ui
tags: [homepage, schema-org, legal-service, local-business, faqpage, website-schema, sitewide-cutover, nav-paths]

# Dependency graph
requires:
  - phase: 01-foundation
    provides: templates/base.html, tokens.css, base.css, header/footer includes, universal chrome, all three validators
  - phase: 02-bio-homepage-contact (Plan 02-01, sibling)
    provides: about.html Person node with @id "https://childcustodyanddivorce.com/about.html#brian-burkett" (referenced by founder + employee on homepage LegalService node)
  - phase: 02-bio-homepage-contact (Plan 02-02, sibling)
    provides: /contact.html LegalService+LocalBusiness node with @id "https://childcustodyanddivorce.com/#legalservice" (matched character-for-character by homepage @graph node — single-entity resolution)
provides:
  - /index.html — primary homepage replacing the Phase 1 placeholder; carries the primary (first) LegalService+LocalBusiness schema instance in an @graph with WebSite + FAQPage nodes
  - assets/css/home.css — hero split, practice grid, meet-Brian band, numbered how-it-works steps, FAQ accordion, service-area block, bottom CTA on navy
  - Sitewide nav-path cutover from Phase 1 placeholders (/attorney-bio/, /contact/) to Phase 2 real URLs (/about.html, /contact.html) across 9 HTML files including both universal include partials + templates/base.html
affects: [phase-03-pillars, phase-04-locations, phase-05-blog, phase-06-analytics, phase-07-cutover]

# Tech tracking
tech-stack:
  added: []
  patterns: [
    "@graph JSON-LD (multiple typed nodes in a single script tag) — WebSite + LegalService+LocalBusiness + FAQPage on the homepage",
    "Cross-page LegalService @id matching (character-for-character) between homepage and contact.html — Google resolves them as ONE entity",
    "Reusable practice-card component (list of anchor cards with h3 + p) — homepage introduces; Phase 3 practice hub will reuse the same class",
    "Numbered how-it-works ordered list with circular gold step-number badges as visual counters"
  ]

key-files:
  created:
    - index.html (450 lines) — hero + CTA trio, 8-card practice grid, Meet Brian teaser, 4-step how-it-works, 6-Q FAQ (visible details + FAQPage schema), San Diego service-area, bottom CTA trio on navy, WebSite + LegalService+LocalBusiness + FAQPage @graph JSON-LD
    - assets/css/home.css (487 lines) — component styles using tokens.css, reduced-motion gated
  modified:
    - includes/header.html — nav paths swept /attorney-bio/ -> /about.html and /contact/ -> /contact.html
    - includes/footer.html — nav paths swept (same two swaps)
    - templates/base.html — nav paths swept in inlined header + footer
    - privacy.html — nav paths swept in inlined header + footer
    - terms.html — nav paths swept
    - disclaimer.html — nav paths swept
    - about.html — nav paths swept in inlined header + footer (Plan 02-01 shipped with Phase 1 stale paths intentionally per the cutover plan)
    - contact.html — nav paths swept in inlined header + footer (Plan 02-02 shipped with Phase 1 stale paths intentionally per the cutover plan)
    - thanks.html — nav paths swept
    - sitemap.xml — root entry lastmod refreshed to 2026-07-06

key-decisions:
  - "Homepage @graph uses THREE typed nodes in a single script tag (WebSite + LegalService+LocalBusiness + FAQPage) instead of three separate script tags. Cleaner cross-node @id resolution and one fewer parse target."
  - "LegalService @id 'https://childcustodyanddivorce.com/#legalservice' is duplicated character-for-character on homepage and contact.html — this is the intended single-entity pattern, not a duplication bug. Google merges both instances into one Local entity because the @id string matches exactly."
  - "founder + employee both reference the bio Person @id 'https://childcustodyanddivorce.com/about.html#brian-burkett' — closes the entity graph loop across all three Wave 1+2 pages of Phase 2. Every downstream authored page (blog posts in Phase 5, practice pillars in Phase 3) will reference the same Person @id via author."
  - "Practice-area grid renders 8 cards linking to /practice-areas/{slug}/ URLs that Phase 3 will fulfill. Netlify serves 404 on those targets today — expected. Adding the internal links now means they light up automatically as Phase 3 ships each pillar."
  - "Homepage was written with the CORRECT nav paths from the start (baked /about.html + /contact.html into its inlined header + footer). The 9-file sweep hit every OTHER HTML file at repo root + includes + templates. This kept the sweep clean of index.html deltas that would only be reverting what Task 1 wrote."
  - "Bottom CTA trio wrapped in a .home__cta-bottom-inner container so the dark navy band spans full width while the CTA cards themselves stay constrained to container-xl."
  - "Meet Brian section uses the same headshot as the hero (a second img tag, lazy-loaded). Kept the fallback design tokens simple rather than optimizing for two crops of the same image on v1."

patterns-established:
  - "Homepage @graph pattern: WebSite is the root/canonical entity; LegalService+LocalBusiness is the operating entity (with sameAs to Cal Bar profile); FAQPage carries the visible FAQs. All three nodes stand alone with @ids that downstream pages can reference."
  - "Sitewide nav-path cutover pattern: sweep every HTML file at repo root + includes/ + templates/ in a SINGLE commit. Piecemeal fixes drift; one sweep guarantees consistency and shows up as one diff at review time."
  - "The Phase 2 wave 2 landing pattern is now confirmed: index.html replaces its Phase 1 placeholder with a full production build in the same commit that lands the nav-path cutover. This is the template for Phase 7 cutover (staging URL -> production DNS) — same 'flip the whole thing at once' discipline."

requirements-completed:
  - HOME-01
  - HOME-02
  - HOME-03
  - HOME-04
  - HOME-05
  - HOME-06
  - HOME-07
  - HOME-08
  - HOME-09

# Metrics
duration: ~30min
completed: 2026-07-06
---

# Phase 02, Plan 03: Homepage + Sitewide Nav-Path Cutover Summary

**Ship the homepage that ties Plans 01 (bio) and 02 (contact) together, plus perform the sitewide nav-path cutover from Phase 1 placeholders (/attorney-bio/, /contact/) to the actual Phase 2 URLs (/about.html, /contact.html) across all 9 existing HTML files including both universal include partials.**

## Performance

- **Duration:** ~30 min
- **Completed:** 2026-07-06
- **Tasks:** 3
- **Files created:** 2 (index.html rewrite from placeholder, assets/css/home.css)
- **Files modified:** 10 (includes/header.html, includes/footer.html, templates/base.html, privacy.html, terms.html, disclaimer.html, about.html, contact.html, thanks.html, sitemap.xml)

## What Shipped

### 1. index.html (450 lines) — the homepage

Sections in order:

1. **Hero** — copy-left / photo-right on desktop (stacks on mobile), warm palette (navy `--ink-900` on cream `--cream-50` with gold `--gold-600` accents), Fraunces display h1, Brian's real headshot from `/assets/img/brian-burkett-headshot.jpg` (aspect 4/5, radius-2xl, shadow-lg, `loading=eager fetchpriority=high`).
2. **CTA trio (hero)** — same three-card pattern from bio/contact: call directly, book a consultation, send a message. Uses the reusable `.cta-card` component from bio.css.
3. **Practice-area grid** — 8 cards on `/practice-areas/{slug}/` URLs (divorce, child-custody, child-support, spousal-support, mediation, domestic-violence, guardianship, family-court). 4-column on desktop, 2-column at tablet, 1-column on mobile. Phase 3 fills the target pages.
4. **Meet Brian teaser** — cream band, circular headshot, three credential chips (CA Bar No. 220343 + Admitted 2002 + Solo Practitioner) reusing `.bio__chip`, link to `/about.html`.
5. **How Working Together Starts** — 4-step numbered list (Reach out -> Free 15-minute intake -> Engagement letter -> Steady representation) with 56px gold circular step-number badges.
6. **FAQ** — 6 `<details>` accordion items on real family-law questions (California waiting period, DIY viability, best-interest custody, hourly rate/retainer, 4-courthouse coverage, legal separation vs divorce). Visible copy is verbatim-mirrored in the FAQPage schema in `<head>`.
7. **Serving San Diego County** — cream-band block naming North County, East County, South County, and coastal/central SD neighborhoods. Also states the 4-courthouse fact.
8. **Bottom CTA trio** — same three-card pattern on a navy (`--ink-800`) full-width band with cream text. Below the CTAs, the Cal Bar 7.1-compliant "contacting does not create an attorney-client relationship" disclaimer.

### 2. index.html @graph JSON-LD (in `<head>`) — three typed nodes

- **WebSite** `@id = https://childcustodyanddivorce.com/#website`, `publisher` -> `#legalservice`, `inLanguage=en-US`.
- **LegalService+LocalBusiness** `@id = https://childcustodyanddivorce.com/#legalservice` (character-for-character match with contact.html), full canonical NAP, `openingHoursSpecification` Mon-Fri 09:00-18:00, `areaServed=San Diego County, California`, `sameAs` -> Cal Bar profile 220343, `founder` + `employee` -> bio Person `@id`.
- **FAQPage** `@id = https://childcustodyanddivorce.com/#faqpage`, 6 Question/Answer pairs with text verbatim-matching the visible details in the FAQ section.

### 3. assets/css/home.css (487 lines)

Tokenized styles for `.home__hero`, `.home__cta-trio`, `.home__practice-grid` + `.practice-card`, `.home__meet` + chips + link, `.home__how` + `.home__steps` + `.home__step-number`, `.home__faq-list` + `.home__faq-item` (details), `.home__service-area`, `.home__cta-bottom` on navy, and `.home__cta-disclaimer`. Includes `@media (prefers-reduced-motion: reduce)` block.

### 4. Sitewide nav-path cutover — 9 files, one sweep

Every occurrence of `href="/attorney-bio/"` was replaced with `href="/about.html"`, and every `href="/contact/"` with `href="/contact.html"`, across:

1. includes/header.html
2. includes/footer.html
3. templates/base.html
4. privacy.html
5. terms.html
6. disclaimer.html
7. about.html (inlined header + footer)
8. contact.html (inlined header + footer)
9. thanks.html (inlined header + footer)

(index.html was written by Task 1 with the correct paths already, so it did not need the sweep — but every other HTML file at repo root + both include partials + the base template did.)

### 5. sitemap.xml

Root URL `/` entry lastmod refreshed to 2026-07-06. `/thanks.html` remains absent (noindex terminal). No structural change to the sitemap otherwise.

## Verification

All plan-verify checks pass:

- `test -f index.html` — yes (450 lines).
- LegalService `@id` on index.html matches contact.html character-for-character (`https://childcustodyanddivorce.com/#legalservice`).
- founder + employee both reference `https://childcustodyanddivorce.com/about.html#brian-burkett` (the Plan 02-01 Person `@id`).
- FAQPage node contains 6 Question/Answer pairs matching the 6 visible `<details>` items verbatim.
- All 8 practice-area URLs present in index.html.
- 6 `.cta-card` instances in the hero + bottom trios combined (24 total `cta-card` string matches when including modifier classes and children).
- `grep -lE '/attorney-bio/|href="/contact/"' *.html includes/*.html templates/*.html` returns empty (sweep clean).
- `grep -q 'href="/about.html"' includes/header.html` succeeds.
- `grep -q 'href="/contact.html"' includes/header.html` succeeds.
- Sitemap root entry present with 2026-07-06 lastmod; `/thanks.html` absent.
- Fabrication validator + Cal Bar 7.1 lint + identity guard all pass on every touched HTML (index, about, contact, thanks, privacy, terms, disclaimer).
- Commit `b7e22bb` pushed to `EchoLocalagency/burkett-law` main; Netlify auto-deploy will pick it up.

## Confirmations Requested in Plan Output

1. **LegalService `@id` character-for-character match:** Confirmed. Both index.html and contact.html declare `"@id": "https://childcustodyanddivorce.com/#legalservice"` — identical string, identical case, no trailing whitespace variance. Google merges into one Local entity.
2. **founder + employee reference bio Person `@id` from Plan 01:** Confirmed. Both fields on the homepage LegalService node contain `{ "@id": "https://childcustodyanddivorce.com/about.html#brian-burkett" }`, which is the exact Person `@id` string that Plan 02-01 SUMMARY locked as the canonical E-E-A-T taproot.
3. **Final list of files touched by the nav-path sweep:** 9 HTML files (includes/header.html, includes/footer.html, templates/base.html, privacy.html, terms.html, disclaimer.html, about.html, contact.html, thanks.html). No extras discovered — the plan's file enumeration was accurate.
4. **FAQ answers rewritten to satisfy Cal Bar lint:** None. All 6 FAQ answers landed verbatim from the plan's pre-vetted copy block. Lint passed on first try.

## Phase 2 Status

Phase 2 wave 2 complete. All 3 plans of Phase 2 (02-01 bio, 02-02 contact/thanks/form, 02-03 homepage + nav cutover) are shipped, committed, and pushed. The E-E-A-T taproot is set (Person `@id` on about.html), the canonical NAP entity is set (LegalService+LocalBusiness `@id` on contact.html + homepage), and every existing page in the repo now points at the real Phase 2 URLs.

Roadmap can flip Phase 2 checkbox to `[x]` once human-verify signs off on the Netlify preview URL. Phase 3 (practice pillar pages) is next and unblocked — the practice-area URLs the homepage grid links to are the URLs Phase 3 will fill.

## User Setup Required

None for this plan. Plan 02-02's Netlify Forms subject-template UI step remains the only outstanding human step for Phase 2.

## Commit

- `b7e22bb` — feat(home): ship homepage + sitewide nav-path cutover to /about.html + /contact.html (12 files, +1020 -74, includes new `assets/css/home.css`)
