# Roadmap: Burkett Family Law Website

## Overview

Build a YMYL-grade static family-law website for Brian Burkett (San Diego) on childcustodyanddivorce.com — live and cut over from Justia before the 2026-07-31 sunset date, with zero dark window and full SEO history preservation. The build follows a dependency-strict path: foundation + design system + fabrication/Cal-Bar-lint validators gate every content-generation phase (Phase 1); the attorney bio ships before any authored content because every downstream schema author references it via `@id` (Phase 2); practice pillars ship before location pages because pillars are the cluster hubs (Phases 3 → 4); blog posts land after pillars exist so each post attaches to a cluster (Phase 5); technical SEO + Justia redirect map close out content-complete state before the fulcrum (Phase 6); a dedicated cutover phase with T-14 / T-7 / T-3 / T-1 / cutover-day / +2h / +24h / +72h checklist lands the DNS switch (Phase 7); and GBP + Google Ads takeover + BrightLocal citations run after the site is live, with the mandatory 7-day Ads observation window before any edits (Phase 8). All 87 v1 requirements map to exactly one phase.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Foundation + Design System + Validators** - Repo, Netlify infra, tokens, self-hosted fonts, legal pages, and the content-fabrication + Cal Bar Rule 7.1 lints that gate every subsequent content-generation phase
- [ ] **Phase 2: Bio + Homepage + Contact (E-E-A-T Taproot & CTA Trio)** - Ship the bio (Person schema `@id` referenced by every downstream author), homepage w/ LegalService+LocalBusiness schema + CTA trio, and contact page as canonical NAP
- [ ] **Phase 3: Practice Pillar Pages (8 Cluster Hubs)** - Ship the practice hub and 8 practice pillar pages (divorce, child custody, child support, spousal support, mediation, domestic violence, guardianship, family court) with Service + FAQPage schema
- [ ] **Phase 4: Location Pages (Practice × City Matrix)** - Ship 15-20 location pages using Service + areaServed:City (never LocalBusiness), each ≥600 words with ≥4 of 6 differentiation blocks, gated by cross-page similarity lint
- [ ] **Phase 5: Blog (E-E-A-T Curated 15-20 Posts)** - Curate + rewrite 15-20 posts from the 40 Justia originals with LegalArticle schema, author `@id` → Bio, backdated publish dates, and cluster linking back to pillars
- [ ] **Phase 6: Technical SEO + Analytics + Justia Redirect Map** - Sitemap/robots/llms.txt, per-page canonical + OG + BreadcrumbList, Rich Results Test pass on every template, Core Web Vitals in budget, GA4 + GSC wired, and the complete Justia URL → new URL 301 map
- [ ] **Phase 7: Cutover to childcustodyanddivorce.com** - Execute the T-14 / T-7 / T-3 / T-1 / cutover-day / +2h / +24h / +72h checklist to land DNS on Netlify before Justia's 2026-07-31 sunset with zero dark window
- [ ] **Phase 8: GBP + Google Ads Takeover + Local Citations** - Accept GBP manager invite (clean account, exact legal name, storefront), take over Google Ads with 7-day observation before edits + AD_CALL conversion pre-wired, and ship BrightLocal citation CSV

## Phase Details

### Phase 1: Foundation + Design System + Validators
**Goal**: A committed, auto-deploying Netlify repo with the warm-approachable design system, self-hosted fonts, universal header/footer, legal pages, and — critically — the content-fabrication validator + California Bar Rule 7.1 copy lint + per-client identity guard that will gate every content-generation phase downstream. Also lands GSC DNS TXT verification early so propagation completes before cutover.
**Depends on**: Nothing (first phase)
**Requirements**: FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10, FND-11, FND-12
**Success Criteria** (what must be TRUE):
  1. `git push` to `EchoLocalagency/burkett-law` triggers a successful Netlify auto-deploy serving a placeholder homepage with the warm palette (navy `#12294A` + cream `#FBF8F3` + gold `#B45309`) at a Netlify preview URL
  2. `netlify.toml` contains `pretty_urls = false` (verified with `curl -I` — internal `.html` links are preserved), `_headers` ships HSTS + CSP + X-Frame-Options + Referrer-Policy, and `_redirects` scaffold exists
  3. Every page renders universal header (logo + 4-item nav + sticky `tel:6192502683` button) and footer (character-identical NAP `591 Camino De La Reina, Suite 821, San Diego, CA 92108` / `(619) 250-2683`, hours, and Cal Bar Rule 7.1 sitewide disclaimer band)
  4. Running `scripts/validate_fabrication.py` + `scripts/lint_cal_bar.py` on a copy that violates rules (contains `specialist`, `guaranteed`, `our team`, invented `500+ cases`) exits non-zero and blocks commit via pre-commit hook; running on clean copy exits zero
  5. Legal pages ship — `/privacy.html` (CCPA/CPRA notice), `/terms.html`, `/disclaimer.html` (Cal Bar attorney advertising) — all linked from footer and human-reviewed for California jurisdiction accuracy
**Plans**: 5 plans
- [x] 01-PLAN.md — Repo scaffold + Netlify infra (netlify.toml pretty_urls=false, _headers, _redirects, robots.txt/sitemap.xml/llms.txt/security.txt) + placeholder homepage + GitHub push + auto-deploy verify (FND-01, FND-02, FND-03, FND-09)
- [x] 02-PLAN.md — Design tokens CSS (DESIGN.md §13 verbatim) + self-hosted Fraunces + Inter WOFF2 + base HTML template (FND-04, FND-05, FND-06)
- [x] 03-PLAN.md — Content-fabrication validator + Cal Bar Rule 7.1-7.5 lint + identity guard + pre-commit hook + test fixtures (FND-11, FND-12)
- [x] 04-PLAN.md — Universal header + footer with character-identical NAP + Cal Bar disclaimer band + nav.js mobile drawer (FND-07, FND-08)
- [x] 05-PLAN.md — Legal pages (privacy.html CCPA/CPRA + terms.html + disclaimer.html Cal Bar Rule 7.1-7.5) (FND-10)

### Phase 2: Bio + Homepage + Contact (E-E-A-T Taproot & CTA Trio)
**Goal**: Ship the E-E-A-T taproot (bio page with verifiable credentials + Person schema carrying a canonical `@id` that every downstream authored page references), plus the two pages that carry the site's only `LocalBusiness` schema instances (homepage + contact). Homepage CTA trio (phone + GHL calendar embed + Netlify contact form) works end-to-end with form submission landing in Burkett + brian@echolocalagency.com inboxes.
**Depends on**: Phase 1
**Requirements**: BIO-01, BIO-02, BIO-03, BIO-04, BIO-05, BIO-06, BIO-07, HOME-01, HOME-02, HOME-03, HOME-04, HOME-05, HOME-06, HOME-07, HOME-08, HOME-09, CON-01, CON-02, CON-03, CON-04, CON-05, CON-06, CON-07
**Success Criteria** (what must be TRUE):
  1. `/about/` renders Burkett's real bio + photo from Justia archive with verifiable credentials (bar admission year, CA Bar Number, JD school, undergrad, memberships) and a Person schema block whose `@id` (`https://childcustodyanddivorce.com/about/#brian-burkett`) is a stable anchor every future authored page references — validated in Google Rich Results Test
  2. Homepage renders hero + warm-approachable design + CTA trio (call button, GHL calendar embed for Burkett's own calendar, Netlify contact form) all equal-weight above the fold on mobile + desktop; LegalService + LocalBusiness multi-type schema validates in RRT
  3. Submitting the contact form triggers a `/thanks/` redirect, fires the GA4 `form_submit` event + AW conversion, and delivers an email with correct `subject_template` (using only `{site_name}`/`{form_name}`/`{site_url}` — no field placeholders) to both Burkett and brian@echolocalagency.com
  4. Contact page ships the canonical `LocalBusiness` schema (single sitewide NAP source), map embed, hours, CTA trio, and the "Submitting this form does not create an attorney-client relationship" disclaimer directly under the form
  5. Every page passes fabrication validator + Cal Bar lint + identity guard (correct GA4 id from `clients.json`, no Mr Green / Arcadian / Ecosystem contamination) before commit
**Plans**: 3 plans
- [x] 02-01-PLAN.md — Attorney bio at `/about.html` with Person schema `@id` anchor, hasCredential for JD + bar admission, alumniOf, memberOf, real headshot, approach section, CTA trio (BIO-01..07)
- [x] 02-02-PLAN.md — Contact page at `/contact.html` with LocalBusiness+LegalService JSON-LD (canonical NAP source), map embed, Netlify form + intake pre-qualifier (matter type / urgency / county / opposing-counsel) + honeypot + 8 spam regexes + Cal Bar 7.1 disclaimer, plus `/thanks.html` with GA4 form_submit slot (CON-01..07)
- [ ] 02-03-PLAN.md — Homepage `/index.html` with hero + CTA trio, 8-card practice grid, Meet Brian teaser, 4-step how-it-works, 6-Q FAQ (visible + FAQPage schema), San Diego County service-area block, bottom CTA trio, LegalService+LocalBusiness+FAQPage+WebSite `@graph`, plus sitewide nav-path cutover from Phase 1 placeholders (`/attorney-bio/`, `/contact/`) to Phase 2 URLs (`/about.html`, `/contact.html`) (HOME-01..09)

### Phase 3: Practice Pillar Pages (8 Cluster Hubs)
**Goal**: Ship the practice hub and all 8 practice pillar pages so the topical cluster hubs exist before any spoke content (location pages or blog posts) attaches to them. Each pillar is 1000-1500 words, jurisdiction-anchored to California family law + San Diego Superior Court, ships Service + FAQPage + BreadcrumbList schema with `author.@id` → bio, and carries the CTA trio inline + at bottom.
**Depends on**: Phase 2
**Requirements**: PA-01, PA-02, PA-03, PA-04, PA-05, PA-06, PA-07, PA-08, PA-09, PA-10, PA-11
**Success Criteria** (what must be TRUE):
  1. `/practice-areas/` hub page lists all 8 practice areas with 40-60 word teasers linking to each pillar page
  2. All 8 pillars (`divorce`, `child-custody`, `child-support`, `spousal-support`, `mediation`, `domestic-violence`, `guardianship`, `family-court`) render at their canonical URLs with unique H1, unique meta title (≤60 chars), unique meta description (≤160 chars), and unique lead paragraph
  3. Every pillar page ships Service + FAQPage + BreadcrumbList schema; `author.@id` resolves to the bio Person node (verified in Rich Results Test on 3 sample pillars)
  4. Every pillar page mentions "California" AND "San Diego" (or a specific SD sub-region / Superior Court branch) in body copy, verified by a jurisdiction lint pass
  5. Every pillar page passes fabrication validator + Cal Bar Rule 7.1 lint (no `specialist`, `expert`, `guaranteed`, `best`, `our team`) before commit
**Plans**: TBD

### Phase 4: Location Pages (Practice × City Matrix)
**Goal**: Ship 15-20 practice × city location pages at `/san-diego/[practice-role]/[city]/` — the highest thin-content + fabrication risk phase. Each page is ≥600 words, uses `Service` + `areaServed: City` (NEVER `LocalBusiness` — only Mission Valley home + contact carry that), carries 4+ of 6 differentiation blocks (SD Superior Court branch, driving from Mission Valley, city-specific demographic/jurisdiction note, city-anchored FAQ, city-specific practice callout, sourceable fact), and passes a cross-page similarity lint (no pair >70% similar excluding chrome).
**Depends on**: Phase 3
**Requirements**: LOC-01, LOC-02, LOC-03, LOC-04, LOC-05, LOC-06
**Success Criteria** (what must be TRUE):
  1. 15-20 location pages render at `/san-diego/[practice-attorney]/[city]/` covering top 3-4 practices × top 5-6 SD cities (final list confirmed from Burkett's zip codes / neighborhoods doc)
  2. Every location page ships `Service` + `areaServed: City` schema (no `LocalBusiness` — a grep for `"@type":"LocalBusiness"` across `/san-diego/**/*.html` returns zero hits)
  3. Every location page carries ≥4 of 6 differentiation blocks and ≥600 words (enforced by lint) and body-copy links back to its matching practice pillar (hub-and-spoke reinforced)
  4. Cross-page similarity lint reports no page pair >70% duplicate (excluding shared footer/nav/disclaimer boilerplate)
  5. Location pages are surfaced via a homepage service-area block and per-pillar "Areas We Serve" blocks — NOT in the main nav (prevents top-nav bloat)
**Plans**: TBD

### Phase 5: Blog (E-E-A-T Curated 15-20 Posts)
**Goal**: Curate 15-20 posts from the 40 Justia originals, rewrite each to the E-E-A-T bar (real author byline, backdated publish date from Justia lastmod, jurisdiction specificity), attach each post to exactly one practice pillar cluster, and ship LegalArticle schema (not plain Article) with `author.@id` → bio + `datePublished` + `dateModified` + `articleSection`. Every rewrite passes fabrication validator (no invented statistics, guaranteed outcomes, or misleading claims).
**Depends on**: Phase 3 (pillars exist as cluster targets), Phase 2 (bio `@id` for author schema)
**Requirements**: BLOG-01, BLOG-02, BLOG-03, BLOG-04, BLOG-05, BLOG-06, BLOG-07, BLOG-08
**Success Criteria** (what must be TRUE):
  1. `/blog/` hub renders with category filter (Divorce / Child Custody / Family Court Guidance / etc.) and post cards for all 15-20 posts
  2. Every blog post ships LegalArticle schema (verified by grep — no plain `"@type":"Article"` on blog posts) with `author.@id` resolving to bio Person node, `datePublished` backdated from Justia lastmod (not batched to 2026-07), `dateModified` = today, and `articleSection` = practice category
  3. Every blog post has a visible byline block at top ("By Brian Burkett, Attorney at Law · Published [date] · Updated [date]") linking to `/about/`, and body-copy links to at least one practice pillar + one related post
  4. Justia legacy blog URLs are mapped 301 → new post slugs in `_redirects` (every Justia post URL that gets curated points to its new home; posts that get cut point to the practice pillar or `/blog/`)
  5. Every post passes fabrication validator + Cal Bar lint before commit (no invented case counts, no guarantee language, no `our team`)
**Plans**: TBD

### Phase 6: Technical SEO + Analytics + Justia Redirect Map
**Goal**: Site is content-complete after Phase 5; this phase validates the full technical SEO surface (sitemap, robots, llms.txt, canonical, OG, BreadcrumbList, Core Web Vitals, images, WCAG 2.1 AA), wires GA4 + GSC + Google Ads conversion actions, and finalizes the complete Justia URL → new URL 301 redirect map so cutover on Phase 7 is checklist-driven, not discovery-driven.
**Depends on**: Phase 5 (all content URLs finalized so redirects can point to real targets)
**Requirements**: SEO-01, SEO-02, SEO-03, SEO-04, SEO-05, SEO-06, SEO-07, SEO-08, SEO-09, SEO-10, ANL-01, ANL-02, ANL-03, ANL-04, ANL-05
**Success Criteria** (what must be TRUE):
  1. `sitemap.xml` auto-includes every static page + blog post (excludes `/thanks/` + `/404/`), `robots.txt` explicitly allows GPTBot / ClaudeBot / PerplexityBot / Google-Extended, `llms.txt` curates top pages, and BreadcrumbList schema renders on every non-home page
  2. Every unique page template (home, bio, contact, practice hub, practice pillar, location page, blog hub, blog category, blog post) passes Google Rich Results Test with zero errors and warnings that impact rich result eligibility
  3. Core Web Vitals target met on top 5 pages (measured via PageSpeed Insights mobile): LCP ≤2.5s, INP ≤200ms, CLS ≤0.1; images use `<picture>` with AVIF + WebP + JPEG fallback, explicit width/height, and lazy-load below fold; WCAG 2.1 AA passes on keyboard nav + contrast + alt text
  4. GA4 property is created for childcustodyanddivorce.com, correct measurement ID is injected into every page (identity guard verifies), GSC is domain-verified via DNS TXT (verification propagated), and Google Ads AW conversion actions (`form_submit` + `phone_click`) are wired
  5. Justia URL enumeration is complete (from `~/Desktop/Burkett Justia Archive/` + GSC coverage report if available), and every Justia URL has a 301 target in `_redirects` — every mapped redirect passes `curl -I` against the Netlify preview domain returning 301 to the correct new URL
**Plans**: TBD

### Phase 7: Cutover to childcustodyanddivorce.com
**Goal**: Execute the pre-planned checklist to point childcustodyanddivorce.com from Network Solutions DNS to Netlify BEFORE Justia's 2026-07-31 sunset, with zero dark window and full HTTPS + GSC + GA4 + form + calendar verification in the T+72h window. This is the hard fulcrum phase — every prep step from Phases 1-6 culminates here.
**Depends on**: Phase 6 (redirect map + GSC verification + all schema validated)
**Requirements**: CUT-01, CUT-02, CUT-03, CUT-04, CUT-05, CUT-06, CUT-07
**Success Criteria** (what must be TRUE):
  1. T-14: Network Solutions DNS TTL for `childcustodyanddivorce.com` is dropped to 300s (verified with `dig`); T-7: full site QA pass (every page renders, every form submits, every CTA fires, every schema validates in RRT)
  2. T-3: `_redirects` is deployed to Netlify preview; every mapped Justia URL passes `curl -I` returning 301 to the correct new URL; T-1: final smoke (RRT on 5 sample pages, GA4 realtime test event visible, form test submission delivered, phone `tel:` link works on mobile, `robots.txt` does NOT contain `Disallow: /`)
  3. Cutover day (before Justia shuts): DNS A/AAAA/CNAME for childcustodyanddivorce.com points at Netlify, propagation is confirmed via `dig @1.1.1.1` + `@8.8.8.8`, Netlify auto-provisions HTTPS cert (Let's Encrypt) within 1 hour
  4. T+24h post-cutover: GSC is re-verified (DNS TXT survived, or new verification done), sitemap.xml is resubmitted, top 5-10 canonical URLs are URL-inspected for indexing
  5. T+72h post-cutover: GA4 is receiving events (form_submit, phone_click, calendar_book), Netlify form submissions are landing in Burkett + brian@ inboxes, calendar booking end-to-end works, DNS TTL is restored to 3600; Justia site remains live until this point — zero dark window achieved
**Plans**: TBD

### Phase 8: GBP + Google Ads Takeover + Local Citations
**Goal**: With the site live and stable, complete the local-search + paid-search half of the package. Accept GBP manager invite from a clean account (avoid Georgia's account-correlation incident), configure GBP with exact legal name + primary category "Family Law Attorney" + storefront + character-identical NAP + real Burkett photos. Take over Google Ads via MCC access or user-add, observe 7 days before making any edits (per the 2026-06-23 blind-spot rule), set up AD_CALL conversion tracking BEFORE any campaign edits, apply family-law negatives, and preserve quality score. Deliver BrightLocal citation CSV for Brian to upload.
**Depends on**: Phase 7 (GBP + Ads point at a live site — never before cutover)
**Requirements**: GBP-01, GBP-02, GBP-03, GBP-04, GBP-05, GBP-06, GBP-07, ADS-01, ADS-02, ADS-03, ADS-04, ADS-05, ADS-06, CIT-01
**Success Criteria** (what must be TRUE):
  1. GBP manager invite is accepted from a clean account (brian@echolocalagency.com, not any account with suspended-listing history); business name is exactly "Law Office of Brian Burkett" (no keyword-stuffing); primary category = "Family Law Attorney" + secondaries Divorce Lawyer / Child Custody Attorney; NAP is character-identical to site + schema
  2. GBP `websiteUri` is set to `https://childcustodyanddivorce.com` post-cutover, hours match sitewide NAP, ≥12 photos uploaded (exterior, interior, headshot) sourced from Justia archive + supplement, and services list maps 1:1 to practice areas with 200-char descriptions
  3. Google Ads access is confirmed (either MCC 935-051-0225 link or user-add to brian@echolocalagency.com Admin), a 7-day observation window has elapsed with baseline captured (CPC, CTR, CVR, search terms, negatives, bidding) before ANY campaign edits, and Clientomics/Rankaroo/Justia access is NOT cancelled until baseline is in hand
  4. AD_CALL conversion action is created (min 30s, primary, using a Google forwarding number NOT Burkett's cell) BEFORE any campaign edits — every campaign edit thereafter has attribution; family-law negatives (DIY, self-help, court-forms, immigration, bankruptcy, criminal, PI, estate, jobs, directories, non-SD geo) are applied; kill-switch threshold is set to 2.5× daily budget (not the $38 Echo Local uses); existing quality score is preserved (no wholesale rebuild)
  5. BrightLocal citation CSV for the Attorney / Family Law category is built with character-identical NAP + hours + description and delivered to Brian for category-ID fill-in + upload
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation + Design System + Validators | 5/5 | Complete (awaiting human-verify sign-off on Plan 05) | 2026-07-06 |
| 2. Bio + Homepage + Contact | 2/3 | In Progress | - |
| 3. Practice Pillar Pages | 0/TBD | Not started | - |
| 4. Location Pages | 0/TBD | Not started | - |
| 5. Blog | 0/TBD | Not started | - |
| 6. Technical SEO + Analytics + Justia Redirect Map | 0/TBD | Not started | - |
| 7. Cutover to childcustodyanddivorce.com | 0/TBD | Not started | - |
| 8. GBP + Google Ads Takeover + Local Citations | 0/TBD | Not started | - |

## Critical Path Notes

- **2026-07-31 hard date**: Phases 1-7 must complete before this. Phase 7 (cutover) is the fulcrum. Work back from T-14 = 2026-07-17 to schedule Phases 1-6.
- **Bio ships before blog**: Bio's Person `@id` is the anchor for every blog post's `author` schema. Phase 2 → Phase 5 dependency is non-negotiable.
- **Practice pillars ship before location pages**: Location pages link UP to pillars (cluster spokes). Phase 3 → Phase 4 dependency is non-negotiable.
- **Validators ship in Phase 1**: Content-fabrication validator + Cal Bar Rule 7.1 lint + identity guard MUST exist before Phase 2 begins any content generation. This is what prevents the Mr Green fabrication echo on YMYL.
- **Google Ads observation window**: Phase 8 requires 7 days of baseline observation BEFORE any campaign edits. Do NOT cancel Clientomics/Rankaroo/Justia access until baseline is captured.
- **Netlify pretty_urls**: `netlify.toml` must ship `pretty_urls = false` on the very first commit in Phase 1 — SoCal/Ecosystem/Mr Green all hit the deindex bug when this was missed.
