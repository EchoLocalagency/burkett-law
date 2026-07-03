# Project Research Summary

**Project:** Burkett Family Law Website (childcustodyanddivorce.com)
**Domain:** Solo family-law attorney SEO site — YMYL, San Diego, California State Bar advertising rules, Justia cutover before 2026-07-31
**Researched:** 2026-07-03
**Confidence:** HIGH

## Executive Summary

Burkett is a solo family-law attorney in San Diego whose current Justia-owned site shuts off on 2026-07-31. He signed $480/mo all-in and needs a warm-approachable, YMYL-grade static site live on childcustodyanddivorce.com by that date with zero dark window. This is Echo Local's first attorney client and first YMYL/legal build — the ranking bar (E-E-A-T) and legal bar (California Rules of Professional Conduct 7.1–7.5) are both non-optional.

The recommended build is the Echo Local static baseline (HTML/CSS/JS + GitHub → Netlify auto-deploy + Netlify Forms + GHL calendar embed) hardened with two YMYL layers: (1) a schema entity graph (`LegalService`+`LocalBusiness` on home/contact only, `Person` with `hasCredential` on bio, `Service`+`FAQPage` on practice pillars, `Service`+`areaServed:City` on location pages — NEVER `LocalBusiness` on satellites — and `LegalArticle` with `@id`-linked `author` on every blog post), and (2) a content-fabrication validator on top of the existing identity guard that blocks invented case counts, "our team" plural pronouns for a solo, "specialist"/"guaranteed"/"best" superlatives (Cal Bar Rule 7.1), and any claim not traceable to the Justia archive at `~/Desktop/Burkett Justia Archive/` or verified with Burkett. Warm-approachable design system locked: navy `#12294A` + warm cream `#FBF8F3` + burnt gold `#B45309`, Fraunces variable serif + Inter variable sans (both self-hosted WOFF2), Burkett's real photos only.

Key risks concentrate around (a) content fabrication (Mr Green scrub echo — YMYL punishes it hardest), (b) thin/duplicate location pages (SoCal deindex echo — programmatic doorway penalty is a lawyer-specific spam classifier), (c) the Netlify `pretty_urls=false` requirement (three-client deindex incident), (d) the Justia URL 301-map cutover on 2026-07-31 (miss = years of SEO history lost + dark window), and (e) the Google Ads account transition from Clientomics/Rankaroo/Justia to Echo Local's MCC 935-051-0225 without losing quality score, conversion history, or breaking call tracking.

## Key Findings

### Recommended Stack

Static HTML/CSS/JS on Netlify (auto-deploy from GitHub, `netlify deploy` command banned per CLAUDE.md) with two YMYL/legal layers stacked on top: a full Schema.org entity graph in JSON-LD, and a content-fabrication validator gate before any Netlify deploy. Everything else — Fraunces/Inter self-hosted WOFF2, AVIF/WebP/JPEG `<picture>` at 3 widths, native `loading="lazy"`, GA4 injected per-site from `clients.json`, existing 24-regex spam filter + Netlify honeypot, GHL calendar embed lazy-mounted below the fold — is the Echo Local pattern used on six live client sites.

**Core technologies:**
- **Static HTML5 + vanilla CSS/JS** — matches every Echo Local client; zero framework JS to blow INP; YMYL rewards fast+simple
- **Netlify + `pretty_urls=false` in `netlify.toml`** — mandatory (SoCal/Ecosystem/Mr Green deindex bug caught 2026-06-16); auto-deploy from GitHub push
- **Netlify Forms + existing spam filter library + honeypot** — reuses `reference_spam_filter_patterns.md`; no reCAPTCHA (INP + UX cost)
- **JSON-LD schema stack** — `LegalService`+`LocalBusiness` (home/contact only), `Person` with `hasCredential`+`sameAs` (bio, `@id`-referenced by every author), `Service`+`FAQPage` (practice pillars), `Service`+`areaServed:City` (location pages — NEVER `LocalBusiness`), `LegalArticle` (blog posts, not plain `Article`)
- **GA4 injected per-site from `clients.json`** — never hardcoded (Mr Green ID leaked into Arcadian/Top Tier/Ecosystem, 2026-06-16)
- **Fraunces + Inter, self-hosted WOFF2, variable, preloaded** — warm serif for headlines (rounded terminals beat EB Garamond stuffiness), Inter body; total ~180KB
- **AVIF `<picture>` with WebP+JPEG fallback + `srcset` at 400/800/1600** — pre-generated, committed to `/img/`
- **Existing Echo Local SEO engine** at `~/EchoLocalClientTracker/` (blog_engine, location_pages, identity guard) — reused, WITH new fabrication validator gate
- **GHL calendar embed (Burkett's own, not shared `PW5Ma7sjF3S6AWayZDuK`)** — lazy-loaded iframe with `/thanks-booked.html` conversion firing
- **llms.txt + explicit `Allow: GPTBot, ClaudeBot, PerplexityBot`** in robots.txt — legal is a prime GEO vertical

Deferred/rejected: JS frameworks (INP hit), page builders (YMYL signals uncontrollable), Google Tag Manager (INP + unnecessary for 4 events), Google Fonts CDN (RTT + privacy), reCAPTCHA (INP + UX), Microdata/RDFa (JSON-LD is Google-preferred), live chat (malpractice-adjacent on YMYL).

### Expected Features

**Must have (table stakes — no launch without these):**
- Attorney bio page with verified credentials (bar admission year + number, JD, law school, practice history — all sourceable from Justia archive)
- 8 practice pillar pages (divorce, child custody, child support, spousal support, mediation, domestic violence, guardianship, family court), 1000–1500 words each, jurisdiction-anchored, FAQ block, CTA trio
- Homepage CTA trio (phone `tel:6192502683` + GHL calendar + Netlify form) equal-weight above the fold — PROJECT.md-locked signature
- Contact page: form + calendar + phone + full NAP + hours + Google map + parking notes
- 15–20 location pages (practice × city matrix — top 3–4 practices × top 5–6 SD cities), 600–900 words min, city-specific court/geography/FAQ
- 15–20 curated blog posts (from 40 Justia originals), rewritten to E-E-A-T bar (Burkett byline, publish + updated dates, jurisdiction tag, `LegalArticle` schema)
- Sitewide sticky phone in header, footer with Cal Rule 7.1 advertising disclaimers
- Netlify form with intake pre-qualifier fields (matter type, urgency, county, opposing counsel Y/N)
- Full schema entity graph (see stack)
- Technical SEO baseline (sitemap.xml with `<lastmod>`, robots.txt with AI crawler allowlist, absolute canonicals, OG tags, llms.txt, `pretty_urls=false`, per-site GA4)
- Legal pages: Privacy Policy, Terms, Disclaimer — real, CA-jurisdiction, linked from footer
- WCAG 2.1 AA baseline (Title III ADA suits target law firms)
- Warm-approachable design system (navy/cream/gold + Burkett's real photos)

**Should have (differentiators — v1 if time permits, else v1.x):**
- Video welcome from Burkett on home (60–90 sec, muted+captioned) — trust close
- 3–5 downloadable resources (custody exchange checklist, divorce filing checklist, financial disclosure prep) with email opt-in gate
- Consult fee transparency block (pending Burkett decision on fee model)
- Practice-area "what to expect" visual timelines
- Real curated testimonials with Cal Rule 7.1 disclosure (from Justia archive only)
- Bar association / Super Lawyers badges — real only

**Defer (v2+ or post-launch phase):**
- Interactive support-estimator / custody-schedule calculators (CA DissoMaster accuracy = malpractice risk)
- Client portal / document upload (IOLTA/confidentiality complexity, out of scope)
- Online retainer payment / engagement letter signing (CA Bar/IOLTA, out of scope)
- Roman-style AI receptionist (deferred to post-launch phase per PROJECT.md; site + SEO + GBP + Ads first)
- Backlink service (Burkett-approved defer to month 3 — foundation must exist to point links at)
- Spanish/hreflang (US-only English practice per scope)

### Table Stakes Anti-Features (Must NOT Build)

- Guarantee/outcome language ("we win," "guaranteed," "best divorce lawyer in San Diego") — Cal Rule 7.1 violation + Google spam
- "Specialist"/"specializes in"/"expert" without CA State Bar Board of Legal Specialization certification — Rule 7.2 term-of-art violation
- "Our team"/"our attorneys"/"our firm" plural pronouns — Rule 7.5 (solo attorney)
- Fake or embellished testimonials; testimonials without Rule 7.1 disclosure
- Live chat widget (malpractice-adjacent on YMYL; PROJECT.md deferred)
- Gavel / scales-of-justice / blindfolded Lady Justice / leather-books stock imagery — cliche + reads template mill
- Stock family photos, stock lawyer-at-desk, stock courthouse steps — kills warm-approachable
- Dense legal jargon on landing pages (petitioner, ex parte, RFO, DVRO without gloss)
- Aggressive "fight back / destroy the other side" copy (family-law prospects are ambivalent)
- Dark patterns: countdown timers, "3 people viewing," exit-intent popups, false scarcity (also CCPA/CPRA risk)
- Thin programmatic location pages (mad-libs with only city name swapped) — YMYL doorway penalty
- `LocalBusiness` schema on any page except home/contact (fake NAP = lawyer-specific Google penalty)
- Hardcoded GA4 ID in shared templates (cross-client pollution incident)
- Google Tag Manager, Google Fonts CDN, reCAPTCHA, Microdata/RDFa
- Blog posts >20 in v1 (thin-content flag for YMYL)
- Justia badge or any pay-to-play directory badge (defeats the point of leaving Justia)
- Client portal, online payments, hreflang, `netlify deploy` command

### Architecture Approach

Directory-per-URL static site (~50 pages) organized as an 8-cluster hub-and-spoke topical model. Practice hub at `/practice-areas/` routes to 8 pillars; each pillar links DOWN to its matching location pages (`/san-diego/[practice-role]/[city]/`) and blog spokes (`/blog/[slug]/`), UP to hub+home, and CROSS to 2–3 sibling pillars. Every content page's `author` schema `@id`-references a single canonical `Person` node on `/attorney-bio/`. Location pages use `Service`+`areaServed:{City containedInPlace: San Diego County}` only — Mission Valley is the site's one and only `LocalBusiness`. Every page ≤3 clicks from home. Contact page is the terminal conversion node (never links deeper).

**Major components:**
1. **Homepage** (`/`) — LegalService+LocalBusiness multi-type schema; CTA trio + 8-practice grid + bio teaser + top-3 blog teaser
2. **Attorney Bio** (`/attorney-bio/`) — E-E-A-T taproot; `Person` node with `hasCredential`+`sameAs`, referenced by every content page's author via `@id`
3. **Practice Hub + 8 Pillars** (`/practice-areas/[slug]/`) — Service+FAQPage+BreadcrumbList; 1000–1500 words each; jurisdiction-anchored
4. **Location Pages** (`/san-diego/[practice-role]/[city]/`, 15–20) — Service+areaServed:City only, no LocalBusiness; 600–900 words with SD court branch + city-specific context + city-specific FAQ
5. **Blog Hub + 8 Category Pages + 15–20 Posts** (`/blog/[slug]/`) — LegalArticle with `@id`-linked author; every post belongs to exactly one category cluster
6. **Contact** (`/contact/`) — canonical NAP source; LocalBusiness with full openingHoursSpecification+geo+hasMap
7. **Legal pages** (`/privacy.html`, `/terms.html`, `/disclaimer.html`) — footer-linked terminals
8. **Sitewide header + footer + breadcrumbs** — sticky phone in header, Cal Rule 7.1 disclaimer band in footer, JSON-LD BreadcrumbList on every non-home page
9. **Netlify infra** — `netlify.toml` (pretty_urls=false), `_headers` (HSTS + security), `_redirects` (Justia URL map), `sitemap.xml` (single file, ~50 URLs, `<lastmod>` only), `robots.txt` (AI crawler allowlist), `llms.txt` + `llms-full.txt`

### Critical Pitfalls (Top 7)

1. **Content fabrication (Mr Green scrub echo)** — SEO engine + Justia mill inheritance both risk shipping invented case counts, "since [year]" claims, "our team" pronouns, or unqualified testimonials. YMYL punishes it hardest; Cal Rule 7.1 makes it a bar complaint risk. **Prevent:** build a fabrication validator that whitelists only Justia archive + Burkett-verified facts, blocks numeric claims + superlatives + guarantee language + plural pronouns + unverified awards; every generation run gates on validator; source-of-truth doc at `.planning/content-facts.md`.

2. **California State Bar Rule 7.1–7.5 violations (superlatives, "specialist," "our team," missing disclaimers, undisclosed testimonials)** — Rule 7.2 makes "specialist" a term-of-art requiring Board of Legal Specialization certification. **Prevent:** copy lint regexes block `best|top-rated|leading|specialist|expert(?!ise)|guaranteed|our (team|attorneys|firm)`; sitewide footer disclaimers ("This website is attorney advertising," "not legal advice," "does not create attorney-client relationship," "past results do not guarantee," "Licensed in California only"); contact form disclaimer above submit.

3. **Thin/duplicate location pages (SoCal deindex + programmatic doorway penalty)** — 15–20 location pages built as mad-libs = YMYL deindex + lawyer-specific spam classifier hit. **Prevent:** each location page needs ≥3 of 5 real elements (SD Superior Court branch, driving/logistics from Mission Valley, city-specific demographic/jurisdiction note, city-anchored FAQ, city-specific practice callout); ≥600 words enforced by lint; cross-page similarity lint fails >50% overlap; unique H1 + meta title + meta description + lead paragraph per page.

4. **Netlify `pretty_urls` deindex (three-client incident)** — Default `pretty_urls=true` strips `.html` from served internal links while canonical/sitemap keep it → Google starves canonical of link support. **Prevent:** `netlify.toml` day 1 with `[build.processing.html]\npretty_urls=false`; grep-lint in CI; verify with `curl` after first deploy.

5. **Justia cutover on 2026-07-31 (dark window + SEO history loss)** — DNS TTL, canonical mismatches, missing 301-redirect map from Justia URLs, sitemap referencing old domain, GSC not verified pre-launch, `Disallow: /` shipped from staging. **Prevent:** T-14 drop DNS TTL to 300s at Network Solutions; T-7 build Justia→new URL redirect map + GSC domain-property verify via DNS TXT; T-5 preview-domain smoke test; T-3 `_redirects` deployed + `curl -I` tested; T-1 final smoke (RRT + form + phone + GA4 realtime); cutover day BEFORE Justia shuts, verify propagation + HTTPS cert issue; cutover +2h verify GSC + submit sitemap + URL inspect top 10; cutover +72h restore TTL. Checklist at `.planning/cutover-checklist.md`.

6. **Schema errors (LocalBusiness on satellites, Article instead of LegalArticle, missing hasCredential, broken entity graph)** — Silent JSON-LD errors mean schema is present but ignored; fake NAP on lawyer sites has a dedicated Google spam classifier. **Prevent:** exactly ONE `LocalBusiness` node sitewide (Mission Valley, on home + contact); location pages use `Service`+`areaServed:City` only; blog posts use `LegalArticle` never plain `Article`; author uses `Person`+`jobTitle:"Attorney"` (not the under-parsed `Attorney` type) with `hasCredential`+`sameAs`; every post's `author.@id` resolves to bio's Person `@id`; Google Rich Results Test on every unique page template pre-cutover.

7. **Google Ads takeover breaks (quality score reset, conversion tracking blind spot, wrong negatives)** — Repeat of Echo Local's own 2026-06-23 blind spot; family-law CPCs are $15–50/click in SD, blind spots are expensive. **Prevent:** verify MCC 935-051-0225 has access before touching; observe 7 days before edits (baseline conversion actions, negatives, bidding, spend); set up "Calls from Ads" AD_CALL primary conversion (min 30s) BEFORE campaign edits, using a Google forwarding number not Burkett's cell; add family-law negatives (DIY, self-help, court-forms, immigration/bankruptcy/criminal/PI/estate, jobs, directories, non-SD geo); kill-switch threshold = 2.5× daily budget (not Echo Local's $38); keep working bidding; import GA4 events as secondary conversions; cancel Clientomics/Rankaroo/Justia AFTER MCC access + baseline captured.

Also close behind: Pitfall 9 (GBP name-stuffing suspension + account correlation — accept manager invite from clean account, exact legal name only, primary category "Family Law Attorney," storefront setup, character-identical NAP); Pitfall 10 (Netlify form `subject_template` only supports `{site_name}`/`{form_name}`/`{site_url}`, Netlify-GitHub auto-deploy silent-break monthly check); Pitfall 11 (GA4 cross-client pollution — per-site injection from `clients.json`, identity guard catches hardcoded IDs).

### Design System Top-Line

**Palette:** navy `--ink-800: #12294A` (deeper/less saturated than default corporate blue) + warm cream `--cream-50: #FBF8F3` (page bg; cream not white is the warmth vehicle) + burnt gold `--gold-600: #B45309` (CTA bg, passes 4.6:1 with cream label; use `--gold-700: #8B5A0F` for gold-as-text). Body copy is `--ink-500` on cream (9.4:1 AAA). No pure black anywhere.

**Fonts:** Fraunces variable (display, rounded terminals + SOFT/opsz axes read warm — beats stuffy EB Garamond default) + Inter variable (body). Both self-hosted WOFF2 (~180KB total), preloaded, `font-display: swap`. `text-wrap: balance` on headings, `text-wrap: pretty` on body. 68ch reading column cap.

**Treatment:** modest rounded corners (`--radius-md: 8px` buttons, `--radius-lg: 12px` cards, `--radius-xl: 20px` hero) — not pill (playful), not square (aggressive). Soft navy-tinted shadows (never `#000` — looks dirty on cream). Lucide line icons at 1.5px stroke — BANNED: gavel, scales-balance, emojis. Motion ≤300ms, transform/opacity only, `prefers-reduced-motion` honored, NO scale/translate on card hover (layout shift banned). Real Burkett photos only — no stock people, no gavel/scales/leather-books/courtroom cliches, no black-and-white. WCAG 2.1 AA verified in the palette contrast table.

Guiding one-liner from DESIGN.md: *A lawyer's front porch, not a lawyer's lobby.*

## Implications for Roadmap

### Suggested Phase Order

The build order below is derived from dependency analysis (bio → schema entity graph → every content page; practice pillars → location pages → cluster blog posts; site live + form working → GBP + Ads takeover). Cutover on 2026-07-31 is the hard fulcrum — Phases A–F must be done before it; Phase G (Ads takeover + GBP) runs concurrently with cutover; Phase H is post-launch operations.

### Phase A: Foundation & Design System
**Rationale:** Everything downstream depends on tokens, templates, and lints being in place. Also: content-fabrication validator and Cal Bar copy lint MUST exist before any content generation (Pitfall 1, Pitfall 3). GSC DNS TXT verify goes here because propagation takes hours.
**Delivers:** Repo scaffold (EchoLocalagency/burkett-law GitHub repo → Netlify), `netlify.toml` with `pretty_urls=false`, `_headers` with HSTS + security, design tokens CSS (from DESIGN.md §13), self-hosted Fraunces+Inter WOFF2 preload, Lucide icon set, base HTML layout (header/footer/breadcrumbs), reusable schema JSON-LD snippets (LegalService, LocalBusiness, Person, LegalArticle, Service, FAQPage, BreadcrumbList), Netlify form + spam filter + honeypot + `subject_template`, GA4 injected per-site from `clients.json`, GSC domain-property verification via DNS TXT, content-fabrication validator + Cal Bar copy lint (BLOCK regexes), Privacy/Terms/Disclaimer legal pages, custom 404 page, source-of-truth doc `.planning/content-facts.md` with Burkett-verified credentials.
**Addresses:** All P1 baseline features from FEATURES.md; palette + typography + component tokens from DESIGN.md.
**Avoids:** Pitfalls 1, 3, 4, 6 (foundation-level), 10, 11, 12, 13, 15, 16, 17.

### Phase B: Bio + Homepage + Contact
**Rationale:** Bio is the E-E-A-T taproot — every downstream schema `author.@id` references it, so it ships first. Homepage + Contact carry the primary `LocalBusiness` (only two pages that get it). Homepage CTA trio (phone + GHL calendar + form) is the primary conversion vehicle — needs to work end-to-end before content pages layer on. Contact page is canonical NAP.
**Delivers:** `/attorney-bio/` with credentials + real photo + Person schema (hasCredential + sameAs to CA State Bar); `/` homepage with LegalService+LocalBusiness multi-type schema, CTA trio, 8-practice grid teaser, bio teaser, top-3 blog placeholder; `/contact/` with LocalBusiness canonical NAP + openingHoursSpecification + hasMap + geo, form with intake pre-qualifier fields, calendar (Burkett's own GHL calendar), tel:+16192502683 link, parking notes; `/thanks.html` + `/thanks-booked.html` conversion pages.
**Uses:** Fraunces/Inter, tokens.css, LegalService+LocalBusiness+Person schema snippets from Phase A.
**Implements:** Homepage + Bio + Contact components from ARCHITECTURE.md.
**Avoids:** Pitfalls 2 (E-E-A-T weak signals), 6 (LocalBusiness discipline — only these two pages), 14 (design/tone), 17 (form success/fail states).

### Phase C: 8 Practice Pillar Pages
**Rationale:** Practice pillars are the cluster hubs — location pages and blog posts BOTH depend on them existing (spokes link up). They're also the primary organic + ads landing surfaces. Each 1000–1500 words, jurisdiction-anchored to CA + San Diego Superior Court.
**Delivers:** `/practice-areas/` hub + 8 pillars (`divorce`, `child-custody`, `child-support`, `spousal-support`, `mediation`, `domestic-violence`, `guardianship`, `family-court`); each with Service+FAQPage+BreadcrumbList schema, 5–8 real FAQ items curated from Justia archive, plain-language copy w/ jurisdiction specificity, related-pillar cross-links (2–3 max), inline + bottom CTA trio, author byline linking to bio.
**Uses:** Practice pillar template from ARCHITECTURE.md; fabrication validator from Phase A on every generation.
**Avoids:** Pitfalls 1, 2, 3, 5 (variation template established here), 6.

### Phase D: 15–20 Location Pages (Practice × City Matrix)
**Rationale:** HIGHEST fabrication + thin-content risk on the site. Runs AFTER pillars (spokes need hubs). Must be gated by the fabrication validator + per-city editorial review + cross-page similarity lint. Starts narrow (15–20), expands post-launch based on GSC data.
**Delivers:** `/san-diego/[practice-role]/[city]/` pages for top 3–4 practices × top 5–6 cities. Each page: ≥600 words, ≥3 of 5 required real elements (SD Superior Court branch, driving from Mission Valley, city-specific demographic/jurisdiction note, city-anchored FAQ, city-specific practice callout); Service+areaServed:City+FAQPage+BreadcrumbList schema (NO LocalBusiness); unique H1+meta title+meta description+lead paragraph; cross-links to 2–3 sibling location pages within cluster; "Learn More About [Practice] in California" link back to pillar; CTA trio.
**Uses:** Location page template from ARCHITECTURE.md; SEO engine's location_pages generator (Echo Local, with leak-proof renderer from 2026-06-23) WITH added fabrication gate and per-city editorial review before commit.
**Avoids:** Pitfalls 1, 4 (thin content — the biggest risk in this phase), 5 (duplicate content), 6 (no LocalBusiness on satellites).

### Phase E: Blog — 15–20 Curated Posts
**Rationale:** Blog spokes reinforce practice pillar clusters + primary AI-search citation surface. Each post belongs to exactly one category (= one pillar). Curated from 40 Justia originals, rewritten to E-E-A-T bar with real bylines, dates, jurisdiction tags. Backdate publish dates from Justia archive to avoid "batch import" signal.
**Delivers:** `/blog/` hub + 8 category pages (`/blog/category/[practice-slug]/`) + 15–20 posts (`/blog/[post-slug]/`); each post has LegalArticle schema with `author.@id` resolving to bio's Person `@id`, publisher LegalService, datePublished (backdated from Justia lastmod), dateModified (today), about:Thing:[practice topic]; visible byline linking to `/attorney-bio/`; category tag linking to category page; author card at bottom; "Related Articles" (2–3 sibling posts); prominent "Learn More About [Practice]" link back to pillar; CTA trio inline + at bottom. Preserve Justia slugs where reasonable; log rewrites for Phase F redirect map.
**Uses:** Blog + LegalArticle template from ARCHITECTURE.md; SEO engine's blog_engine.
**Avoids:** Pitfalls 1, 2, 5, 6 (LegalArticle not Article), 18 (batch publish date drift).

### Phase F: Technical SEO + Schema QA + Justia Redirect Map
**Rationale:** Site is content-complete after Phase E; before cutover, everything gets validated and the Justia URL redirect map is finalized. Also llms.txt/llms-full.txt (legal is a prime GEO vertical).
**Delivers:** `sitemap.xml` with all ~50 URLs and `<lastmod>` only (no priority/changefreq); `robots.txt` with AI crawler explicit allowlist + sitemap reference; `llms.txt` + `llms-full.txt` curated for LLM consumption; every schema block validated via Google Rich Results Test + schema.org validator; Lighthouse ≥95 accessibility + INP ≤200ms on every unique page template; cross-page similarity lint sweep; content-fabrication validator sweep; Cal Bar Rule 7.1 human-read against checklist; Justia URL → new URL redirect map (`_redirects` file) built from Justia archive enumeration + GSC coverage; Justia slug preservation decisions logged; OG/Twitter cards on every page; security.txt at `/.well-known/security.txt`.
**Uses:** All schema + content from Phases B–E.
**Avoids:** Pitfalls 6, 7 (redirect map — needs to exist before cutover), 15 (OG), 19 (llms.txt).
**Research flag:** Google Rich Results Test workflow (manual per page vs. RRT API automation) may need a phase-planning research bump.

### Phase G: Cutover to childcustodyanddivorce.com (2026-07-31 hard date)
**Rationale:** Fulcrum phase. Dedicated because too many DNS/TLS/DNS/GSC/robots things can silently break. All prep in Phases A–F culminates in this phase.
**Delivers:** T-14 drop DNS TTL at Network Solutions to 300s (verified with `dig`); T-7 GSC domain-property already verified (Phase A) + Justia redirect map in place (Phase F); T-5 preview-domain (`burkett-law-preview.netlify.app`) full smoke test; T-3 `_redirects` deployed + every mapped Justia URL `curl -I` tested; T-1 final smoke (RRT on 5 sample pages, GA4 test event visible in realtime, form test submission, phone tap on mobile, `robots.txt` NOT `Disallow: /`); cutover day (BEFORE Justia shuts) point childcustodyanddivorce.com DNS to Netlify, monitor propagation via `dig @1.1.1.1` + `@8.8.8.8`; +1h verify HTTPS cert issued (Let's Encrypt auto); +2h verify GSC + submit sitemap + URL inspection on top 10; +24h re-check GSC coverage + no `Disallow: /` + canonical audit; +72h restore DNS TTL to 3600; cutover checklist at `.planning/cutover-checklist.md`.
**Avoids:** Pitfall 7 (the whole point of this phase).

### Phase H: GBP Onboarding + Local Citations + Google Ads Takeover
**Rationale:** Runs during and immediately after cutover. GBP + Ads point at a live site — never before. Manager invite acceptance from CLEAN account (Georgia's correlation incident). Ads observation period BEFORE any edits.
**Delivers:**
- **GBP:** manager invite accepted from clean account (not Burkett's personal Gmail if legal-history correlated); business name = exact legal name only ("Law Office of Brian Burkett") — NO SEO stuffing; primary category "Family Law Attorney" + secondaries "Divorce Lawyer"/"Child Custody Attorney" (NOT "Attorney" — too broad); storefront setup (not SAB); service area SD County only; NAP character-identical to site+schema+BrightLocal; hours match site; Burkett's real photos matching site; all edits in ONE session (not stacked over days).
- **BrightLocal:** legal-category citation CSV generated + delivered to Brian for category IDs + upload.
- **Google Ads:** verify MCC 935-051-0225 has access (do NOT accept invite blind); observe 7 days for baseline (conversion actions, negatives, bidding, spend); set up "Calls from Ads" AD_CALL primary conversion (min 30s) using Google forwarding number NOT Burkett's cell; add family-law negatives (DIY, self-help, court-forms, immigration/bankruptcy/criminal/PI/estate, jobs, directories, non-SD geo); kill-switch threshold = 2.5× daily budget; keep working bidding (don't reset to Max Conversions with zero history); import GA4 events (`form_submit`, `phone_click`, `calendar_view`, `calendar_booked`) as secondary conversions; cancel Clientomics/Rankaroo/Justia AFTER MCC access + baseline captured.
**Avoids:** Pitfalls 8, 9.
**Research flag:** May want `/gsd:research-phase` here — MCC access sequencing + baseline observation window + when to cancel Clientomics is genuinely delicate.

### Phase I: Post-Launch Operations (30/60/90-day)
**Rationale:** Silent-break monitoring (Chef Dorothy went 84 days without deploys). GSC data starts arriving; location page expansion decisions rely on real impression data, not speculation.
**Delivers:** Monthly Netlify-GitHub auto-deploy verification (last commit vs. last deploy timestamp); v1.x differentiator layer as Burkett has capacity (video welcome, 3–5 downloadable resource PDFs with email opt-in, consult fee transparency, "what to expect" visual timelines per practice); real testimonials with Rule 7.1 disclosure IF Burkett approves; expanded location pages based on GSC "Discovered — currently not indexed" + impression data; expanded blog posts based on GSC opportunity keywords; Roman AI receptionist wire-up (deferred to this phase per PROJECT.md); backlink service evaluation at month 3 (Featured default per MEMORY.md, Semantic Links reserve).
**Avoids:** Pitfall 10 (auto-deploy silent-break), general phase-8 anti-features.

### Phase Ordering Rationale
- **Bio-first is E-E-A-T-first:** every downstream `author.@id` references the bio's Person node — bio must exist before any authored content.
- **Pillars before spokes:** location pages and blog posts both link UP to pillars; shipping spokes without hubs orphans them (Pitfall: never orphan a page).
- **Validators before content:** the content-fabrication validator + Cal Bar copy lint are Phase A deliverables so they gate every subsequent content-generation phase. Building them post-hoc would replay the Mr Green fabrication scrub.
- **Location pages after pillars but before blog:** location pages are the highest thin-content risk; getting them right needs the pillar variation template established in Phase C, and the writing discipline transfers to blog rewrites in Phase E.
- **Technical SEO + redirect map before cutover:** GSC DNS TXT verification in Phase A gives it hours to propagate; final RRT + `_redirects` in Phase F ensures cutover day is checklist-driven, not discovery-driven.
- **Cutover as a dedicated phase:** too many silent-break vectors (DNS TTL, HTTPS cert, robots.txt, canonicals, GSC verify) to bundle into a content phase.
- **Ads takeover AFTER cutover, not before:** ads pointing at a dark or half-live site burn quality score. The 7-day observation window is a hard rule from the 2026-06-23 blind-spot incident.
- **Post-launch ops is a phase not a shrug:** the Chef Dorothy 84-day deploy break happened because nobody scheduled a check.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase F (Technical SEO QA):** Google Rich Results Test API vs. manual per-page workflow at 50-page scale — worth 20 minutes of `/gsd:research-phase` before planning.
- **Phase G (Cutover):** Network Solutions DNS UI + TTL controls + apex vs. www canonical decision — verify with a dry-run in Network Solutions before T-14.
- **Phase H (GBP + Ads):** MCC 935-051-0225 access request sequencing + when to cancel Clientomics/Rankaroo/Justia + which Google forwarding number to provision — worth a `/gsd:research-phase` because the sequence is easy to break.

Phases with standard patterns (skip `/gsd:research-phase`):
- **Phase A (Foundation):** Echo Local pattern (Chef Dorothy, Primal Plates, Psychic Experience) is well-established.
- **Phase B (Bio + Home + Contact):** design + component tokens from DESIGN.md are already locked; schema patterns from STACK.md are official Google-documented.
- **Phase C (Practice Pillars):** template from ARCHITECTURE.md is prescriptive; content generation gated by validators from Phase A.
- **Phase E (Blog):** Echo Local blog_engine reused; only the fabrication validator + `@id` linkage is new.
- **Phase I (Post-launch):** operational, not research-driven.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Baseline is confirmed across 6+ Echo Local sites; schema/YMYL layers cross-validated against Google Search Central + schema.org canonical docs + Cal Bar Rules 7.1–7.5. |
| Features | HIGH | Table stakes + anti-features vetted against 2026 ABA, PaperStreet, Rankings.io, YMM Digital, Attorney at Law Magazine. Anti-features are Cal Bar-driven (canonical legal source). |
| Architecture | HIGH | Directory-per-URL + hub-and-spoke cluster + 3-clicks-from-home is standard IA for YMYL local SEO. Location page anti-thin discipline is opinionated but justified by cross-client incidents. |
| Pitfalls | HIGH | 10 critical pitfalls are Echo-Local-observed (Mr Green fabrication, SoCal deindex, Ecosystem GA pollution, Georgia GBP account correlation, Chef Dorothy auto-deploy break) OR Cal Bar canonical OR Google-documented YMYL guidance. |
| Design | HIGH | Tokens locked in DESIGN.md with WCAG AA contrast verification; palette + fonts justified against PROJECT.md warm-approachable brief. |

**Overall confidence:** HIGH

### Gaps to Address

- **Burkett's exact bar credentials for `hasCredential` schema.** Need bar admission year, bar number, law school, undergraduate. Ask during Phase A `.planning/content-facts.md` build.
- **Justia URL enumeration for redirect map.** The `~/Desktop/Burkett Justia Archive/` scrape provides 63 pages; if Justia had URLs that weren't in the archive, GSC coverage report is the fallback. Also need to check if Burkett has access to any old Google Search Console for the Justia-hosted site.
- **Burkett's fee model decision** (free consult vs. flat-fee consult vs. paid consult) — blocks the "consult fee transparency" v1.x differentiator.
- **Real Justia testimonials curation** — need Burkett to review + approve any published testimonials (Rule 7.1 disclosure required).
- **Final city list for location matrix.** PROJECT.md notes "Burkett attached a full SD County zip codes/neighborhoods doc" — reference this during Phase D city selection.
- **GBP account choice** — accept manager invite from `burkett@echolocalagency.com` (recommend fresh) vs. Burkett's account. Avoid Georgia's correlation incident.
- **Google Ads MCC access status** — confirm 935-051-0225 request has been sent + accepted before Phase H starts.
- **Video welcome feasibility for v1.x** — depends on Burkett recording (iPhone quality OK per FEATURES.md).
- **Domain www vs. apex canonical** — pick one, 301 the other, decide before Phase G T-14.

## Sources

### Primary (HIGH confidence)
- Google Search Central — E-E-A-T + YMYL guidance (Dec 2025 update): https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central — Structured Data (LegalService, Attorney, LocalBusiness, LegalArticle, FAQPage, BreadcrumbList, Person): https://developers.google.com/search/docs/appearance/structured-data
- schema.org canonical docs — LegalService, Attorney, LegalArticle, Person, FAQPage, BreadcrumbList, Service
- California State Bar — Rules of Professional Conduct 7.1–7.5 (attorney advertising) — https://www.calbar.ca.gov/
- web.dev — Core Web Vitals + INP ≤200ms threshold (March 2024 promotion), LCP + fetchpriority + preload patterns
- Netlify docs — Forms, Image CDN, `pretty_urls`, `_headers`, `_redirects`
- ABA Law Technology Today — solo attorney website 2025+ guidance
- caniuse.com — AVIF ≥96%, container queries + :has() 2023 baseline

### Secondary (MEDIUM confidence)
- llmstxt.org — 2024–2026 emerging AI-crawler standard (adopted, not yet formalized)
- PaperStreet + Rankings.io + YMM Digital + Attorney at Law Magazine — vertical-specific 2026 family-law site pattern analysis
- LuckyFish Media — solo law firm website 2026 commentary
- ui-ux-pro-max skill's Legal Services + Hotel/Hospitality palettes (as design starting points, tuned per DESIGN.md)

### Tertiary (LOW confidence — validate during implementation)
- Google's specific 2026 SERP behavior around FAQ rich results (Google has scaled back FAQ SERP rendering since 2024; entity-graph benefit still applies)
- Specific California AG posture on CCPA/CPRA enforcement against solo law firms (privacy policy is cheap insurance)

### Echo Local Reference Docs (internal, HIGH confidence — incident-derived)
- `reference_spam_filter_patterns.md` (2026-06-09) — 24 regex + 5 heuristic filter deployed to 6 sites
- `reference_netlify_pretty_urls_deindex.md` (2026-06-16) — SoCal + Ecosystem + Mr Green incident
- `reference_identity_guard_system.md` (2026-06-23) — cross-client GA4 + brand pollution guard
- `reference_netlify_form_subject_template.md` (2026-06-09) — 12 broken hooks incident
- `reference_ads_call_tracking_fix.md` (2026-06-23) — Echo Local's own AD_CALL tracking blind spot fix
- `reference_gbp_account_correlation_suspension.md` (2026-06-15) — Georgia's suspended prior listings

---
*Research completed: 2026-07-03*
*Ready for roadmap: yes*
