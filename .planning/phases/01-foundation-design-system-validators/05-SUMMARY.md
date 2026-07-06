---
phase: 01-foundation-design-system-validators
plan: 05
subsystem: legal-pages
tags: [html, ccpa, cpra, cal-bar, attorney-advertising, ymyl, legal]

# Dependency graph
requires:
  - phase: 01-foundation-design-system-validators/02
    provides: templates/base.html scaffold + tokens.css + base.css + self-hosted Fraunces/Inter fonts
  - phase: 01-foundation-design-system-validators/03
    provides: Cal Bar lint + fabrication validator + identity guard + pre-commit hook
  - phase: 01-foundation-design-system-validators/04
    provides: includes/header.html + includes/footer.html inlined into templates/base.html (universal chrome + Cal Bar Rule 7.1 sitewide disclaimer band + footer legal-links column)
provides:
  - privacy.html (CCPA + CPRA California-jurisdiction Privacy Policy reflecting the actual data-collection surface — Netlify Forms + GA4 + GHL calendar + Netlify server logs + tel: metadata)
  - terms.html (Terms of Use with no-attorney-client-relationship + do-not-send-confidential + California jurisdiction/venue)
  - disclaimer.html (Cal Bar Rule 7.1-7.5 Attorney Advertising Disclaimer with prior-results + testimonial policy + calbar.ca.gov verify-standing link + California-only-jurisdiction statement)
  - Updated sitemap.xml (adds /privacy.html, /terms.html, /disclaimer.html alongside homepage entry)
affects: [phase-02-bio-homepage-contact, phase-03-practice-pillars, phase-05-blog, phase-06-tech-seo, phase-07-cutover]

# Tech tracking
tech-stack:
  added: []  # No new libs — three additional static HTML pages using Plan 02 + Plan 04 chrome
  patterns:
    - "Copy-base pattern: each legal page is a hand-copy of templates/base.html with unique <title>/description/canonical/OG/schema plus a container-md .prose <main> body. Confirms base.html is a real template that other pages consume."
    - "WebPage JSON-LD per page: every legal page ships a minimal WebPage JSON-LD block with name + url + isPartOf pointing at the WebSite entity. Establishes the per-page schema slot pattern Phases 2-5 will extend (LocalBusiness / Person / Service / LegalArticle)."
    - "California-only legal surface: all three pages are California-jurisdiction-specific (CCPA/CPRA, Cal Bar Rules 7.1-7.5, California venue). Not portable to any second state without substantive rewrites."

key-files:
  created:
    - privacy.html
    - terms.html
    - disclaimer.html
  modified:
    - sitemap.xml

key-decisions:
  - "Testimonial-disclaimer sentence reworded to satisfy the Plan 03 Cal Bar RULE_7_1_GUARANTEE regex without weakening the validator. Original phrasing 'is not a promise, guarantee, or prediction' triggered the regex because 'guarantee' was not preceded by one of the four allowed negations (do not / does not / cannot / no). Rewrote to 'is not a promise or prediction about the outcome of any other case, and does not guarantee a similar result' — preserves the legal meaning, adds a stronger explicit disavowal, uses the allowed 'does not guarantee' negation. Validator unchanged."
  - "Character-identical NAP repeated in all three legal-page 'Contact' sections: '591 Camino De La Reina, Suite 821, San Diego, CA 92108' + phone display '(619) 250-2683' + tel:+16192502683. Matches header + footer + clients.json exactly for the character-identical NAP invariant (PITFALLS.md Pitfall 9 — Phase 8 GBP + BrightLocal citations will need identical strings)."
  - "Publish + last-updated date = 2026-07-03 (site initialization date used in all Phase 1 plans). Any future material revision must update the 'Last updated' line AND the schema dateModified when we add one (schema currently ships name + url + isPartOf only; dateModified deferred until content changes)."
  - "Legal pages describe the ACTUAL data-collection surface (Netlify Forms fields, GA4 events, GHL calendar embed, Netlify server logs, tel: metadata) — not boilerplate. If Phase 2 or later phases wire additional third parties (Segment, Hotjar, Facebook Pixel, etc.), privacy.html must be updated to list them BEFORE those tools go live. Never ship a tool that isn't disclosed."

patterns-established:
  - "Legal page pattern: <main> → container-md → article.prose → h1 + section h2 blocks + Contact NAP block. No new component CSS — everything renders from tokens + base.css + .prose."
  - "WebPage JSON-LD slot pattern per non-index page: name + url + isPartOf → WebSite entity."
  - "Footer legal-links column (Privacy / Terms / Disclaimer) resolves to real pages — no 404 from footer chrome."

requirements-completed: [FND-10]

# Metrics
duration: ~10min
completed: 2026-07-06
---

# Phase 01 Plan 05: Legal Pages Summary

**Three California-jurisdiction legal pages ship — CCPA/CPRA-compliant Privacy Policy describing the actual data-collection surface, Terms of Use with no-attorney-client-relationship + do-not-send-confidential + California venue, and Cal Bar Rule 7.1-7.5 Attorney Advertising Disclaimer with prior-results + testimonial policy + calbar.ca.gov verify-standing link — all copies of templates/base.html, all passing the three validators, all linked from the footer legal column with no 404s.**

## Performance

- **Duration:** ~10 min
- **Started:** 2026-07-06
- **Completed:** 2026-07-06
- **Tasks:** 2 (privacy + terms in Task 1; disclaimer + sitemap in Task 2) + 1 minor deviation-fix
- **Files created:** 3
- **Files modified:** 1

## Accomplishments

- `privacy.html` ships CCPA + CPRA California disclosures: Information We Collect (Netlify Forms + GHL calendar + GA4 + Netlify server logs + tel: metadata — actual site surface, not boilerplate), How We Use Information, What We Do Not Do (do-not-sell, do-not-share-with-data-brokers, no cross-site tracking, no behavioral ads), Your California Privacy Rights (know / delete / correct / opt-out-of-sale-or-sharing / limit-sensitive-info / non-discrimination), Cookies, Third-Party Services (Netlify + Google + GoHighLevel with linked privacy policies), Data Retention, Children's Privacy, Security, Changes, Contact Us with character-identical NAP.
- `terms.html` ships Terms of Use: Purpose, No Attorney-Client Relationship, Do Not Send Confidential Information Until Engaged, Attorney Advertising (linking to disclaimer.html), Accuracy and Currency, Links to Third-Party Sites, Intellectual Property, Jurisdiction and Governing Law (California + San Diego County venue), Modifications, Contact with character-identical NAP.
- `disclaimer.html` ships Cal Bar Rule 7.1-7.5 attorney advertising disclaimer: attorney advertising statement, Not Legal Advice, No Attorney-Client Relationship, Past Results (prior results do not guarantee a similar outcome — verbatim required sentence), Jurisdiction (California-only + San Diego County focus), Testimonials and Endorsements (permission-only, not paid, no guarantee of outcome), Confidential Information, Verification of Bar Standing (calbar.ca.gov link), Contact with character-identical NAP.
- All three pages inherit the universal navy header + footer + tokens + fonts by hand-copying templates/base.html (the copy-base pattern confirmed working).
- All three pages ship a per-page WebPage JSON-LD block (`@type: WebPage` + name + url + isPartOf → WebSite entity) in the schema slot — establishes the per-page schema pattern for Phases 2-5.
- `sitemap.xml` updated to include `/privacy.html`, `/terms.html`, `/disclaimer.html` with `lastmod` 2026-07-03 alongside the homepage entry.
- All three pages pass all three validators (Cal Bar lint + fabrication + identity guard) with zero violations.
- Both commits pushed to `origin/main`. Netlify auto-deploys via GitHub webhook.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create privacy.html + terms.html** — `e41d61d` (feat)
2. **Task 2: Create disclaimer.html + update sitemap.xml** — `dfc4bb4` (feat)

Both pushed to `origin/main` (`26991db..dfc4bb4`). Netlify auto-deploys from GitHub webhook.

## Files Created/Modified

- `privacy.html` — 209 lines. CCPA + CPRA California Privacy Policy reflecting Netlify Forms / GA4 / GHL / Netlify server logs / tel: metadata. Character-identical NAP + WebPage schema.
- `terms.html` — 173 lines. Terms of Use with no-attorney-client-relationship + do-not-send-confidential + California jurisdiction/venue. Character-identical NAP + WebPage schema.
- `disclaimer.html` — 175 lines. Cal Bar Rule 7.1-7.5 Attorney Advertising Disclaimer including required "Prior results do not guarantee a similar outcome" sentence, testimonial policy, calbar.ca.gov verify-standing link, California-only-jurisdiction statement. Character-identical NAP + WebPage schema.
- `sitemap.xml` — Added three `<url>` entries (privacy.html, terms.html, disclaimer.html) with `<lastmod>2026-07-03</lastmod>` alongside the existing homepage entry.

## Decisions Made

- **Publish + last-updated date = 2026-07-03**: All three pages carry "Last updated: July 3, 2026" — same site initialization date used in prior Phase 1 plans. Any future material revision must update this line AND (once added) the schema `dateModified` field.
- **California-only legal surface**: All three pages are California-jurisdiction-specific (CCPA/CPRA, Cal Bar Rules 7.1-7.5, California venue). If Burkett ever adds a second state, these need substantive rewrites, not just addition of another state's boilerplate.
- **Actual data-collection surface**: privacy.html lists Netlify Forms + GA4 + GHL calendar + Netlify server logs + tel: metadata — the real vectors per PROJECT.md + STACK.md. If Phase 2 or later wires additional third parties (Segment, Hotjar, Facebook Pixel), privacy.html must be updated to list them BEFORE those tools go live.
- **Testimonial-disclaimer rewording (deviation, see below)**: preserved legal meaning while satisfying the Plan 03 Cal Bar RULE_7_1_GUARANTEE regex without weakening the validator.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Cal Bar lint blocked the testimonial disclaimer sentence in disclaimer.html**

- **Found during:** Task 2 (running `bash scripts/run_all_validators.sh privacy.html terms.html disclaimer.html`)
- **Issue:** The Testimonials section originally read "is not a promise, guarantee, or prediction about the outcome of any other case." The Plan 03 → Plan 04 refined `RULE_7_1_GUARANTEE` regex `(?<!do not )(?<!does not )(?<!cannot )(?<!no )\bguarantee[sd]?\b` matched the standalone "guarantee" (preceded by a comma, not by an allowed negation phrase). Blocked commit.
- **Fix:** Rewrote to "is not a promise or prediction about the outcome of any other case, and does not guarantee a similar result." Preserves the legal meaning (arguably strengthens the disavowal), uses the allowed "does not guarantee" negation. Validator unchanged.
- **Files modified:** `disclaimer.html`
- **Verification:** `bash scripts/run_all_validators.sh privacy.html terms.html disclaimer.html` — zero violations.
- **Committed in:** `dfc4bb4` (Task 2 commit).

---

**Total deviations:** 1 auto-fixed (Cal Bar lint validator caught a legitimately ambiguous phrasing; rewrite satisfies both the legal intent and the validator).
**Impact on plan:** Zero scope creep. The plan explicitly stated "If a violation fires, fix the specific text — do NOT weaken the validator." Followed exactly.

## Issues Encountered

None beyond the deviation above.

## User Setup Required

None — no external service configuration for this plan.

**Human-verify checkpoint (from plan):** Plan 05 is `autonomous: false` with a `human-verify` gate at the end. Both authoring tasks are committed + pushed to `main`. Netlify auto-deploy triggered on push. Brian to verify at the Netlify preview URL:

1. `<preview>/privacy.html` — universal navy header + phone chip at top; H1 "Privacy Policy" + "Last updated: July 3, 2026" caption; all sections present (Information We Collect / How We Use Information / What We Do Not Do / Your California Privacy Rights (CCPA / CPRA) / Cookies / Third-Party Services / Data Retention / Children's Privacy / Security / Changes / Contact Us); character-identical NAP in Contact Us; universal navy footer at bottom.
2. `<preview>/terms.html` — H1 "Terms of Use"; No Attorney-Client Relationship + Do Not Send Confidential Information Until Engaged sections both visible; California venue in Jurisdiction section.
3. `<preview>/disclaimer.html` — H1 "Attorney Advertising Disclaimer"; "Prior results do not guarantee a similar outcome" verbatim; calbar.ca.gov link works.
4. Click through EACH footer link (Privacy Policy / Terms of Use / Attorney Advertising Disclaimer) on any page — all land correctly, no 404.
5. Skim for California-specific language: no "US law" instead of "California law"; no "our firm" language (identity + Cal Bar validators already enforced).
6. Optional legal read: Burkett reads all three pages for jurisdictional accuracy before Phase 7 cutover.

Type "approved" if all 6 checks pass, or describe specific text that needs revision.

## Next Phase Readiness

- **Phase 1 (Foundation + Design System + Validators)**: All 5 plans complete (01, 02, 03, 04, 05). Foundation shipped. All 12 FND-* requirements met. Phase 1 closes on human-verify approval.
- **Phase 2 (Bio + Homepage + Contact)**: Unblocked. Bio page consumes:
  - `templates/base.html` as its structural scaffold
  - `includes/footer.html` BIO-VERIFY comment slot (fills bar admission year + CA Bar number)
  - `scripts/content_facts.md` — MUST populate with Burkett's verified bar admission year, CA Bar number, JD school, undergrad, and any experience claims BEFORE bio can pass the fabrication validator (currently returns validator-empty allowlist)
- **Canonical NAP for downstream**: `591 Camino De La Reina, Suite 821, San Diego, CA 92108` + phone display `(619) 250-2683` + tel E.164 `+16192502683`. Every future page (bio, homepage, contact, pillars, location pages, blog) must use these character-identical strings. Every Phase 8 GBP + BrightLocal citation write must match verbatim.
- **Legal-page refresh cadence**: Any change to data-collection tools (add Segment, Hotjar, Facebook Pixel, etc. in Phase 2+) requires updating `privacy.html` Third-Party Services + Information We Collect BEFORE the new tool ships. Any material policy revision bumps the "Last updated" line to the revision date. Add `dateModified` to the WebPage schema at that point.

---
*Phase: 01-foundation-design-system-validators*
*Completed: 2026-07-06*
