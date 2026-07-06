---
phase: 02-bio-homepage-contact
plan: 01
subsystem: ui
tags: [html, css, schema-jsonld, person-schema, e-e-a-t, cal-bar-rule-7-1]

requires:
  - phase: 01-foundation-design-validators
    provides: templates/base.html, includes/header.html, includes/footer.html, assets/css/tokens.css, assets/css/base.css, scripts/content_facts.md, three-validator pre-commit hook, brian-burkett-headshot.jpg

provides:
  - /about.html — attorney bio page with canonical Person JSON-LD (@id anchor)
  - assets/css/bio.css — bio component styles + reusable .cta-card class
  - sitemap.xml entry for /about.html
  - Canonical E-E-A-T Person @id string every downstream authored page references

affects: [02-02-contact, 02-03-homepage, 03-practice-pillars, 05-blog-engine]

tech-stack:
  added: [Person JSON-LD structured data]
  patterns: [Reusable .cta-card component class, dl-based credentials block, singular-voice bio copy for solo practitioner]

key-files:
  created:
    - about.html
    - assets/css/bio.css
  modified:
    - sitemap.xml

key-decisions:
  - "Person @id string is locked to https://childcustodyanddivorce.com/about.html#brian-burkett — every downstream authored page (blog posts in Phase 5, practice pillars in Phase 3) must reference this exact @id in its author/about link. Do not change."
  - "CTA trio card component (.cta-card + .cta-card__label/value/note) is defined in bio.css and will be reused verbatim by the homepage (Plan 02-03) and practice pages (Phase 3). Any style change ripples across the site."
  - "About hero title uses 'San Diego Family Law Attorney · 24 Years of Family-Law Practice' verbatim to match the content_facts.md allowlist entry — the fabrication validator rejects '24 years of practice' unless it appears in content_facts.md."
  - "Header nav still links to /attorney-bio/ (not /about.html). Plan 02-03 will do the sitewide swap in one commit. Do not fix piecemeal."

patterns-established:
  - "Person schema pattern: @type Person + @id URL#anchor + hasCredential array (JD + bar admission) + alumniOf array + memberOf + worksFor LegalService + sameAs to calbar.ca.gov Licensee profile. This template will be re-used verbatim on any future attorney bio page."
  - "Bio prose voice: first-person singular ('I', 'my practice'), 'practices exclusively', 'solo practitioner', 'family-law practice' — every phrase is Cal Bar Rule 7.1 lint-clean."

requirements-completed: [BIO-01, BIO-02, BIO-03, BIO-04, BIO-05, BIO-06, BIO-07]

duration: 15 min
completed: 2026-07-06
---

# Phase 02 Plan 01: Bio Page Summary

**Attorney bio at /about.html with canonical Person JSON-LD (@id `#brian-burkett`), verified credentials block (CA Bar 220343, admitted 2002, JD Thomas Jefferson, undergrad Pepperdine), plain-language approach section in singular voice, and a reusable CTA trio anchoring E-E-A-T across the site.**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-07-06 (Plan 02-01 kickoff)
- **Completed:** 2026-07-06
- **Tasks:** 3
- **Files created:** 2 (about.html, assets/css/bio.css)
- **Files modified:** 1 (sitemap.xml)

## Accomplishments

- Shipped `/about.html` with a Person JSON-LD block whose `@id` is the canonical E-E-A-T anchor (`https://childcustodyanddivorce.com/about.html#brian-burkett`). Every future blog post, practice pillar, and location page will point `author` / `about` at this @id.
- All on-page credentials are verifiable and traceable: CA Bar Membership No. 220343 (link to calbar.ca.gov Licensee profile), admitted 2002, JD from Thomas Jefferson School of Law, undergrad from Pepperdine University, 24 years of family-law practice, all four San Diego County family-law courthouses named.
- Approach section rewritten in warm plain-language singular voice — no "specialist", no "expert" as noun, no "guaranteed", no "our team". Cal Bar Rule 7.1-7.5 lint returns clean.
- Reusable `.cta-card` component class shipped in bio.css. Plans 02-02 (contact) and 02-03 (homepage) will import bio.css or refactor cta-card into a shared component sheet.
- Sitemap updated with `/about.html` at `<lastmod>2026-07-06</lastmod>`.

## Task Commits

Each task was committed atomically:

1. **Task 1: Write /about.html with hero, credentials, approach, practice list, CTA trio, Person JSON-LD** — `6776e4a` (feat)
2. **Task 2: Write assets/css/bio.css using design tokens** — `4477b65` (feat)
3. **Task 3: Add /about.html to sitemap.xml, run validators, commit** — `1997228` (feat)

## Files Created/Modified

- `about.html` — 395-line bio page with inline Person schema, hero (real 800x800 Burkett headshot as LCP-priority image), credential chips, My Approach + Credentials + What I Handle sections, CTA trio, disclaimer sentence.
- `assets/css/bio.css` — 346 lines of bio-specific styles + reusable `.cta-card` component; every value references `var(--...)` custom properties from tokens.css; includes `prefers-reduced-motion` block.
- `sitemap.xml` — one new `<url>` entry for /about.html with `<lastmod>2026-07-06</lastmod>`, positioned after homepage.

## Decisions Made

- **Person @id string locked** to `https://childcustodyanddivorce.com/about.html#brian-burkett`. This is the taproot for E-E-A-T. Every downstream authored asset in Phases 3, 4, 5 must reference this exact string. Changing it means re-writing every blog post byline schema.
- **Reusable `.cta-card` in bio.css.** Plan 02-02 and Plan 02-03 will re-use this class for their own CTA trios. Any hover/focus/color adjustment must be reviewed for cross-page consistency.
- **`24 Years of Family-Law Practice` verbatim** in the hero subtitle (not `24 years of practice`) so the fabrication validator's substring match against content_facts.md whitelisted line succeeds.
- **Header nav intentionally still points to `/attorney-bio/`.** Plan 02-03 (homepage) will do the sitewide swap to `/about.html` + `/contact.html` in one commit — do not touch header/footer include files here.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Fabrication validator rejected "24 years of practice"**
- **Found during:** Task 1 (about.html initial write)
- **Issue:** Meta description, OG description, and hero subtitle all said "24 years of practice". The fabrication validator (`FAB_YEARS_OR_COUNT` pattern) requires the exact substring to appear in a line of `scripts/content_facts.md`. The whitelisted line is `24 years of family-law practice` — so "24 years of practice" is not a substring match and fails.
- **Fix:** Rewrote three occurrences to "24 years of family-law practice" (in meta description, OG description, hero `.bio__title`).
- **Files modified:** about.html
- **Verification:** Re-ran `validate_fabrication.py about.html` → exit 0. All three validators pass via `bash scripts/run_all_validators.sh $(pwd)/about.html`.
- **Committed in:** `6776e4a` (Task 1 commit, before the initial commit reached git — no separate fix commit needed).

---

**Total deviations:** 1 auto-fixed (1 blocking).
**Impact on plan:** Zero scope creep. Rewording tightens the copy to match the verified fact language.

## Issues Encountered

None — plan executed cleanly after the phrasing correction above.

## User Setup Required

None — no external service configuration required for this plan.

## Next Phase Readiness

- **Downstream references:** The Person `@id` string `https://childcustodyanddivorce.com/about.html#brian-burkett` is now stable and can be referenced by:
  - Plan 02-03 (homepage) — homepage LocalBusiness / LegalService schema will point `founder` or `employee` at this @id
  - Phase 3 (practice pillars) — each Service schema's `provider` will reference this @id
  - Phase 5 (blog engine) — every post's Article/BlogPosting schema's `author` will be `{"@id":"https://childcustodyanddivorce.com/about.html#brian-burkett"}`
- **Nav mismatch (intentional):** Header currently links "About" → `/attorney-bio/`. Plan 02-03 will fix this + the footer link in the same commit that updates every existing HTML page. Do not attempt piecemeal fixes.
- **CTA card component:** `.cta-card` class is defined in `assets/css/bio.css`. If Plan 02-02 or Plan 02-03 needs it, either link `bio.css` from those pages OR refactor into a shared `components.css` (deferred — not a blocker for Plan 02-02 which is running in a sibling agent and creates its own `contact.css`).
- **Parallel plan status:** Sibling agent Plan 02-02 has already shipped `/contact.html` + `/thanks.html` + spam-filter form JS + contact.css (commit `c647449`). Sitemap coordination worked without conflict — this plan added `/about.html` before privacy.html; the sibling likely added `/contact.html` + `/thanks.html` at the appropriate positions.
- **Ready for Plan 02-03 (homepage):** Both bio (this plan) and contact (sibling) are on main. Plan 02-03 can now write index.html with cross-links to `/about.html` and `/contact.html` and do the sitewide `/attorney-bio/` → `/about.html` swap.

---
*Phase: 02-bio-homepage-contact*
*Completed: 2026-07-06*
