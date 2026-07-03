# Requirements: Burkett Family Law Website

**Defined:** 2026-07-03
**Core Value:** Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Foundation & Design System

- [ ] **FND-01**: Static-site scaffold in `~/Desktop/burkett-law/` committed to GitHub (EchoLocalagency org, new repo `burkett-law`) with Netlify auto-deploy verified
- [ ] **FND-02**: `netlify.toml` includes `[build.processing.html] pretty_urls = false` (prevent SoCal deindex bug)
- [ ] **FND-03**: `_headers` file with security headers (CSP, X-Frame-Options, Referrer-Policy) + `_redirects` file initialized
- [ ] **FND-04**: Design tokens implemented as CSS custom properties per DESIGN.md (palette, type, spacing, radius, shadow, motion) in `assets/css/tokens.css`
- [ ] **FND-05**: Self-hosted Fraunces + Inter WOFF2 files in `assets/fonts/` with `font-display: swap` and preload
- [ ] **FND-06**: Base HTML template with semantic landmarks, skip-link, meta viewport, favicon set, and OG image slot
- [ ] **FND-07**: Universal footer with correct NAP (591 Camino De La Reina Suite 821, San Diego CA 92108 / (619) 250-2683), hours, sitewide legal disclaimer, and California Bar disclaimer
- [ ] **FND-08**: Universal header with logo, primary nav (Home, Practice Areas, About, Blog, Contact), call button (tel:6192502683)
- [ ] **FND-09**: `robots.txt`, `sitemap.xml`, and `llms.txt` scaffolding created at project root
- [ ] **FND-10**: Legal pages shipped (Privacy Policy w/ CCPA/CPRA notice + California Consumer Rights, Terms of Use, Attorney Advertising Disclaimer)
- [ ] **FND-11**: Content-fabrication validator + California Bar Rule 7.1 copy lint scripts in `scripts/` (runs pre-commit)
- [ ] **FND-12**: Per-client identity guard verifies correct GA4 id + no cross-client contamination before commit

### Attorney Bio (E-E-A-T Taproot)

- [ ] **BIO-01**: `/about/` page with Burkett's real bio sourced from Justia archive (no fabrication)
- [ ] **BIO-02**: Verifiable credentials on-page: bar admission year, California Bar Number, education (JD school, undergrad), practice history, professional memberships
- [ ] **BIO-03**: Person schema with `hasCredential` (bar admission), `alumniOf`, `memberOf`, `image`, `jobTitle`, `worksFor` (linked to LegalService)
- [ ] **BIO-04**: `@id` anchor on Person entity so every content page's schema `author` links back to bio
- [ ] **BIO-05**: Real Burkett photograph (from Justia archive) as hero
- [ ] **BIO-06**: Approach/philosophy section (warm, plain-language, no fear-based copy)
- [ ] **BIO-07**: CTA trio (call + calendar + form) at end of bio

### Homepage

- [ ] **HOME-01**: Hero with warm-approachable design (navy + cream + gold), real Burkett photo, headline + subhead + CTA trio above fold
- [ ] **HOME-02**: CTA trio equal-weight (call button, GHL calendar embed, contact form) surfaced above fold
- [ ] **HOME-03**: Practice-area grid (8 cards) linking to `/practice-areas/[slug]/`
- [ ] **HOME-04**: "Meet Brian Burkett" section with real photo + credentials snippet linking to `/about/`
- [ ] **HOME-05**: How-it-works / what-to-expect section (3-4 steps for engaging an attorney)
- [ ] **HOME-06**: FAQ block (top 5-6 family-law FAQs, marked up with FAQPage schema)
- [ ] **HOME-07**: Location-served block with San Diego County context (link to top location pages)
- [ ] **HOME-08**: LegalService + LocalBusiness schema on homepage (single canonical NAP)
- [ ] **HOME-09**: Repeat CTA trio at bottom of page

### Contact

- [ ] **CON-01**: `/contact/` page with map embed, NAP, hours, and CTA trio
- [ ] **CON-02**: Netlify contact form with fields (name, email, phone, matter type, message) + hidden spam honeypot + spam filter per reference_spam_filter_patterns.md
- [ ] **CON-03**: Intake pre-qualifier fields (matter type dropdown, urgency, county, opposing counsel awareness) — conditional/optional
- [ ] **CON-04**: Form action redirects to `/thanks/` with GA4 event + AW conversion fire
- [ ] **CON-05**: Netlify form notifications configured to Burkett + brian@echolocalagency.com (subject template validated)
- [ ] **CON-06**: Legal disclaimer directly under form ("Submitting this form does not create an attorney-client relationship")
- [ ] **CON-07**: LocalBusiness schema on contact page (single canonical NAP with homepage)

### Practice Area Pages (8 Pillars)

- [ ] **PA-01**: `/practice-areas/` hub page listing all 8 practice areas with intro copy
- [ ] **PA-02**: `/practice-areas/divorce/` — pillar page with H1, intro, subsections (uncontested/contested/high-asset), FAQ, related links, CTA
- [ ] **PA-03**: `/practice-areas/child-custody/` — same structure
- [ ] **PA-04**: `/practice-areas/child-support/` — same structure
- [ ] **PA-05**: `/practice-areas/spousal-support/` — same structure (alimony)
- [ ] **PA-06**: `/practice-areas/mediation/` — same structure
- [ ] **PA-07**: `/practice-areas/domestic-violence/` — same structure (restraining orders)
- [ ] **PA-08**: `/practice-areas/guardianship/` — same structure
- [ ] **PA-09**: `/practice-areas/family-court/` — same structure (procedural help / family court navigation)
- [ ] **PA-10**: Each practice page ships with Service + FAQPage + BreadcrumbList schema (author @id → Bio)
- [ ] **PA-11**: Each practice page carries jurisdiction-specific content (California family law, San Diego Superior Court references)

### Location Pages (Practice × City Matrix)

- [ ] **LOC-01**: 15-20 location pages at `/san-diego/[practice-attorney]/[city]/` covering top 3-4 practice areas × top 5-6 SD cities (La Jolla, Chula Vista, Del Mar, Carlsbad, Escondido, Coronado, El Cajon, Oceanside — final list TBD from Burkett's zip doc)
- [ ] **LOC-02**: Each location page carries 4+ of 6 differentiation blocks (local court context, neighborhood considerations, distance from Mission Valley office, city-specific FAQ, practice-specific city considerations, sourceable facts) — 600-900 word floor
- [ ] **LOC-03**: Each location page uses `Service` schema with `areaServed: City` (NOT LocalBusiness — avoids fake-NAP lawyer penalty)
- [ ] **LOC-04**: Every location page links body-copy back to its practice pillar (hub-and-spoke)
- [ ] **LOC-05**: Cross-page similarity lint gate — no location page >70% duplicate content
- [ ] **LOC-06**: Location pages skipped in main nav; surfaced via practice pages + service-area section on homepage

### Blog (E-E-A-T Curated)

- [ ] **BLOG-01**: `/blog/` hub with category filter (Divorce / Child Custody / Family Court Guidance) and post cards
- [ ] **BLOG-02**: 15-20 curated posts from the 40 Justia originals, rewritten to E-E-A-T bar (real author, publish date, San Diego / California specificity)
- [ ] **BLOG-03**: Each post uses LegalArticle schema (NOT generic Article) with `author` @id → Bio, `datePublished`, `dateModified`, `articleSection` (category), `mainEntityOfPage`, `image`
- [ ] **BLOG-04**: Justia legacy blog URLs mapped 301 → new slugs in `_redirects` (preserve SEO history)
- [ ] **BLOG-05**: Blog posts backdated from Justia lastmod (not batched to 2026-07 — avoids batch-import signal)
- [ ] **BLOG-06**: Each post links body-copy to at least one practice pillar + one related post (cluster linking)
- [ ] **BLOG-07**: Every post carries author byline block at top ("By Brian Burkett" + verifiable credentials snippet + link to `/about/`)
- [ ] **BLOG-08**: Content fabrication validator scans every post before commit (block invented statistics, guaranteed outcomes, misleading claims)

### Technical SEO & Schema

- [ ] **SEO-01**: Every page has canonical URL, meta description ≤160 chars, unique H1, meta title ≤60 chars
- [ ] **SEO-02**: Every page has Open Graph tags (og:title, og:description, og:image, og:type, og:url)
- [ ] **SEO-03**: `sitemap.xml` auto-includes every static page + blog post (excludes /thanks/, /404/)
- [ ] **SEO-04**: `robots.txt` allows all crawlers including AI (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) — YMYL sites benefit from citation eligibility
- [ ] **SEO-05**: `llms.txt` curated with top pages + descriptions for LLM crawling
- [ ] **SEO-06**: BreadcrumbList schema on all non-home pages
- [ ] **SEO-07**: Every schema block validates via Google Rich Results Test before commit
- [ ] **SEO-08**: Core Web Vitals target: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 (measured via PSI)
- [ ] **SEO-09**: All images use `<picture>` with AVIF + WebP + JPEG fallback, lazy-load below fold, explicit width/height
- [ ] **SEO-10**: WCAG 2.1 AA compliance — contrast ratios pass, keyboard nav works, focus rings visible, semantic landmarks present, alt text on all images

### Analytics & Search Console

- [ ] **ANL-01**: GA4 property created for childcustodyanddivorce.com with correct measurement ID injected into every page (identity guard verifies)
- [ ] **ANL-02**: GA4 conversion events: `form_submit`, `phone_click`, `calendar_book`, `contact_page_view`
- [ ] **ANL-03**: Google Search Console verified via DNS TXT record at cutover phase
- [ ] **ANL-04**: GSC sitemap submitted post-cutover
- [ ] **ANL-05**: Google Ads AW conversion action `form_submit` wired + `phone_click` for call tracking

### Google Business Profile

- [ ] **GBP-01**: Manager invite from Burkett accepted via brian@echolocalagency.com
- [ ] **GBP-02**: Legal name only in GBP name field (no keyword-stuffing — suspension risk)
- [ ] **GBP-03**: Primary category set to "Family Law Attorney"; secondary categories for Divorce Lawyer, Child Custody Attorney where allowed
- [ ] **GBP-04**: Services list matches practice areas 1:1 with 200-char descriptions
- [ ] **GBP-05**: Hours + address + phone match sitewide NAP character-for-character
- [ ] **GBP-06**: `websiteUri` set to https://childcustodyanddivorce.com post-cutover
- [ ] **GBP-07**: 12+ photos uploaded (exterior, interior, headshot, team) sourced from Justia archive + new if needed

### Google Ads Takeover

- [ ] **ADS-01**: Access to Burkett's Google Ads account confirmed (either user-add to brian@echolocalagency.com Admin, or MCC link to customer id 935-051-0225)
- [ ] **ADS-02**: 7-day observation window before making changes — capture baseline (CPC, CTR, conversion rate, search terms)
- [ ] **ADS-03**: AD_CALL conversion action created for call tracking (min 30s, primary) before ANY campaign edits
- [ ] **ADS-04**: Family-law-specific negative keyword list applied (free consultation, DIY, pro se, self-help, law student, jobs)
- [ ] **ADS-05**: Existing campaigns audited for quality score preservation (no wholesale rebuild that resets QS)
- [ ] **ADS-06**: Landing pages for ads point to relevant practice/location pages (not homepage) with correct conversion tracking

### Cutover & Launch

- [ ] **CUT-01**: T-14 days before cutover: DNS TTL lowered to 300s on Network Solutions
- [ ] **CUT-02**: T-7 days: Full site QA (all pages render, all forms submit, all CTAs fire, all schemas validate)
- [ ] **CUT-03**: Justia URL enumeration + 301 redirect map built in `_redirects` (every existing Justia URL points somewhere on new site)
- [ ] **CUT-04**: Cutover day: Point childcustodyanddivorce.com A/AAAA/CNAME at Netlify, verify HTTPS cert provisioning, verify sitewide serving
- [ ] **CUT-05**: T+24h post-cutover: GSC re-verify, sitemap resubmit, spot-check indexing of 5-10 canonical URLs
- [ ] **CUT-06**: T+72h post-cutover: Confirm GA4 receiving events, Netlify form submissions delivered, calendar booking flow works
- [ ] **CUT-07**: Zero dark window — old Justia site remains live until DNS TTL confirms cutover, then Justia can be cancelled

### Citations & Local SEO

- [ ] **CIT-01**: BrightLocal citation CSV built for Attorney/Family Law category with correct NAP + hours + description; Brian uploads

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### AI Voice & Receptionist

- **AI-01**: Roman-style AI receptionist wired to Burkett's phone number via Twilio → Retell (post-launch phase)
- **AI-02**: Retell prompt tuned for family-law intake with sensitivity handling (crisis flags: domestic violence, child abduction)

### Video & Trust

- **VID-01**: Welcome video from Burkett on homepage (2-minute personal intro)
- **VID-02**: Practice-area explainer videos (2-3 min each, 3-4 top practices)

### Testimonials

- **TEST-01**: Curated real client testimonials (Cal Rule 7.1 compliant, with disclosure) from Justia archive + Google Reviews

### Downloadable Resources

- **DOWN-01**: San Diego Divorce Checklist (PDF, gated with email capture)
- **DOWN-02**: Custody Preparation Guide (PDF, gated)

### Backlinks

- **LINK-01**: Featured.com API-automated response drafting (per backlink product decision, month 3)

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Client portal / document upload | Legal-sensitive, not in $480/mo package |
| Online retainer payment | IOLTA/legal trust requirements, defer |
| Live chat widget | INP risk, added friction on YMYL pages, deferred |
| Spanish translation / hreflang | US-only English practice, not requested |
| Support calculator / custody visualizer | Cal Rule 7.1 risk if outcomes look guaranteed; skip v1 |
| Case results / outcome database | Cal Rule 7.1 violation risk without heavy disclaimers |
| Fake reviews / undisclosed testimonials | Ethics violation + Google penalty |
| Practice areas outside California | Unlicensed jurisdiction |
| More than 20 blog posts | Thin-content risk on YMYL |
| Location pages beyond top 15-20 | Thin-content risk; expand based on GSC signal |
| Gavel / scales / courtroom stock imagery | Design brief warm-approachable; DESIGN.md ban list |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| FND-01 through FND-12 | Phase 1 | Pending |
| BIO-01 through BIO-07 | Phase 2 | Pending |
| HOME-01 through HOME-09 | Phase 2 | Pending |
| CON-01 through CON-07 | Phase 2 | Pending |
| PA-01 through PA-11 | Phase 3 | Pending |
| LOC-01 through LOC-06 | Phase 4 | Pending |
| BLOG-01 through BLOG-08 | Phase 5 | Pending |
| SEO-01 through SEO-10 | Phase 6 | Pending |
| ANL-01 through ANL-05 | Phase 6 | Pending |
| CUT-01 through CUT-07 | Phase 7 | Pending |
| GBP-01 through GBP-07 | Phase 8 | Pending |
| ADS-01 through ADS-06 | Phase 8 | Pending |
| CIT-01 | Phase 8 | Pending |

**Coverage:**
- v1 requirements: 87 total
- Mapped to phases: 87
- Unmapped: 0 ✓

---
*Requirements defined: 2026-07-03*
*Last updated: 2026-07-03 after initialization*
