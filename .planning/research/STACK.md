# Stack Research

**Domain:** Solo family-law attorney SEO site (YMYL / legal / local intent, San Diego)
**Researched:** 2026-07-02
**Confidence:** HIGH (baseline stack is locked and proven across 6+ Echo Local client sites; additions are 2026-current best-practice layers)

> **Scope note.** The baseline (static HTML/CSS/JS + GitHub → Netlify auto-deploy + GA4 + GHL calendar embed + Netlify Forms + spam filter) is a CONFIRMED constraint, not a research question. This document only covers the SEO/YMYL layers that stack on top of that baseline.

---

## Recommended Stack

### Core Technologies (Baseline — Confirmed, not up for debate)

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Static HTML5 | living std | All pages (home, 8 practice areas, 15–20 location pages, 15–20 blog posts, bio, contact) | Fastest possible LCP/INP, zero framework JS to hurt Core Web Vitals, matches every other Echo Local client site, YMYL rewards fast + simple |
| Vanilla CSS (no preprocessor required) | CSS3 (2026 baseline: `container queries`, `:has()`, `oklch()`, `text-wrap: balance`) | Styling | Reduce toolchain surface, no CSS-in-JS runtime cost; modern CSS features cover everything the design brief needs |
| Vanilla JS (progressive enhancement only) | ES2023 | Nav toggle, form spam filter, calendar embed lazy-inject | Site must be fully usable with JS disabled (YMYL trust signal, accessibility) |
| GitHub + Netlify auto-deploy | current | Hosting + CI | Matches CLAUDE.md deploy rule — NEVER `netlify deploy` direct; commits push to main → Netlify auto-builds |
| Netlify Forms | native | Contact submissions | Free tier covers volume, native email notifications, spam honeypot built-in, integrates with existing spam filter library |
| Netlify `netlify.toml` | required | `[build.processing.html] pretty_urls = false` | **NON-NEGOTIABLE** — Netlify pretty_urls stripping `.html` from internal links caused SoCal deindexing (see PROJECT.md). Every Echo Local site needs this one line. |

### Schema.org Structured Data (JSON-LD, per page type)

Family law / solo-attorney recommended schema combination. **Use JSON-LD only** (never Microdata or RDFa for a new build in 2026 — Google explicitly prefers JSON-LD and it decouples markup from rendering).

| Page Type | Schema Types (nested) | Rationale |
|-----------|----------------------|-----------|
| Home | `LegalService` (as primary) + `LocalBusiness` (via `@type: ["LegalService", "LocalBusiness"]` multi-type) + `Attorney` reference via `provider` + `WebSite` with `SearchAction` (optional) | `LegalService` is the schema.org-preferred type for law firms; `LocalBusiness` unlocks the San Diego local pack signals. Multi-typing is valid schema.org and is how Google's own examples do it. |
| Attorney bio | `Attorney` (subtype of `LocalBusiness`, but for the person use `Person` with `jobTitle: "Attorney"`, `worksFor: {@type: LegalService, ...}`, `alumniOf`, `memberOf` for State Bar, `hasCredential` for JD/bar admissions) | `Attorney` type exists in schema.org but is under-supported by parsers. Safer pattern is `Person` with rich credentialing properties; this is the pattern Google's rich-results test validates cleanly. `hasCredential` with `EducationalOccupationalCredential` is the 2026-current way to encode "admitted to California State Bar 20XX." |
| Practice area page (divorce, custody, etc.) | `Service` with `serviceType: "Family Law – Divorce"`, `provider: {@type: LegalService, ...}`, `areaServed: {@type: AdministrativeArea, name: "San Diego County"}` + `FAQPage` (below) + `BreadcrumbList` | `Service` is the schema.org-correct type for a single practice area; nesting `provider` back to the LegalService links entities. FAQ + Breadcrumbs are the two schema types Google still renders visibly in SERP for legal content. |
| Practice area FAQ | `FAQPage` with 4–8 `Question`/`Answer` pairs per practice area | FAQ rich results reduced in 2024 but Google still indexes them for legal queries; the entity graph benefit remains even if the SERP feature is gone. Use questions Burkett actually gets, not fabricated ones. |
| Location page (e.g., "Divorce Attorney in La Jolla") | `Service` with `areaServed: {@type: City, name: "La Jolla", containedInPlace: {@type: AdministrativeArea, name: "San Diego County"}}` + `LegalService` provider + `BreadcrumbList` + `FAQPage` (city-specific) | `areaServed` at city + county granularity is the modern local-signal encoding. Do NOT stamp `LocalBusiness` on satellite location pages — only one physical address (Mission Valley) is real; fake NAP for other cities is a Google penalty vector for lawyers. |
| Blog post | `LegalArticle` (subtype of `Article`) + `author: {@type: Person, ...}` (must resolve to Burkett's bio page via `sameAs` / `@id`) + `publisher: {@type: LegalService}` + `datePublished` + `dateModified` + `about: {@type: Thing, name: "Child Custody"}` | `LegalArticle` is a real schema.org type and is the 2026-current E-E-A-T signal for legal content — it tells Google "this is legal information written by an attorney." Author link back to bio page is the entity-graph glue that makes E-E-A-T computable. |
| Contact page | `LegalService` + `LocalBusiness` with full NAP + `openingHoursSpecification` + `hasMap` (Google Maps URL) + `geo` (lat/lng from GBP) + `contactPoint` | Contact page is the canonical NAP source that Google cross-references with GBP + citations. NAP must be **character-identical** across site, GBP, and BrightLocal citations. |
| Sitewide (in `<head>` on every page) | `BreadcrumbList` + `Organization` reference (via `publisher` on all Article/Service schemas) | Breadcrumbs still render in SERP; Organization glue links every page back to the entity graph. |

**Schema-level YMYL requirements (call out):**
- Every blog post's `author` MUST resolve to a real `Person` node with `hasCredential` (JD, bar admission). This is the single strongest E-E-A-T machine-readable signal.
- `LegalService` node should include `priceRange`, `paymentAccepted`, `currenciesAccepted`, and `openingHours` — completeness feeds Google's confidence in the entity.
- Add `sameAs` links from the `Person` node to: State Bar profile URL, Justia profile (until 2026-07-31 sunset), LinkedIn, Avvo, Google Business Profile URL. These are the entity-reconciliation links Google actually uses.

### Image Format & Delivery

| Layer | Recommendation | Why |
|-------|----------------|-----|
| Primary format | **AVIF with WebP fallback with JPEG fallback** via `<picture>` element | AVIF is 2026-baseline (>96% browser support per caniuse); ~50% smaller than JPEG at same quality; ~20% smaller than WebP. WebP fallback covers old iOS + edge cases. JPEG is the universal safety net. |
| Delivery | Netlify Image CDN (built-in, via `/.netlify/images?url=...&w=...&fm=avif`) OR pre-generated multi-format assets committed to repo | Netlify Image CDN is free tier–friendly and does on-the-fly AVIF/WebP conversion. For a 30-page site, pre-generated assets in `/img/` are simpler and remove the CDN dependency (matches Chef Dorothy / Psychic Experience pattern). **Recommend pre-generated** — determinism > convenience for YMYL. |
| Sizes | `srcset` with 3 widths: 400w, 800w, 1600w (mobile / tablet / desktop-retina) | Covers 99% of device pixel scenarios without exploding asset count |
| Attribute discipline | `width` + `height` attributes REQUIRED on every `<img>` | Prevents CLS (Core Web Vitals). Non-negotiable. |
| Alt text | Real, descriptive, not keyword-stuffed | YMYL + accessibility. "Brian Burkett, San Diego family law attorney" not "san diego divorce lawyer child custody attorney best" |
| Hero images | Preload the LCP image: `<link rel="preload" as="image" imagesrcset="..." imagesizes="...">` | Directly improves LCP. Do this on the homepage + every practice/location page (top image is always LCP). |

### Lazy-Loading Pattern

| Element | Loading Attribute | Notes |
|---------|-------------------|-------|
| Above-the-fold hero image | `loading="eager"` + `fetchpriority="high"` | Never lazy-load LCP — it destroys LCP metric |
| All below-the-fold images | `loading="lazy"` | Native browser lazy-load, no JS library needed. Fully supported since 2020, no polyfill required in 2026. |
| Below-the-fold iframes (GHL calendar embed) | `loading="lazy"` on the iframe + defer script | GHL calendar iframe is heavy; lazy-load reclaims ~500ms of INP budget |
| Decorative images | `loading="lazy"` + `decoding="async"` | `decoding="async"` yields main thread during image decode |
| Fonts | See font strategy below | Not a lazy-load target; treated separately |

### Font Strategy

| Layer | Recommendation | Why |
|-------|----------------|-----|
| Hosting | **Self-host via `/fonts/` directory in the repo** (NOT Google Fonts CDN) | Third-party font hosts add TLS+DNS RTT, hurt LCP, and increase third-party risk. Self-hosting removes 3rd-party cookie flags and satisfies GDPR-adjacent trust signals (relevant for legal). |
| Format | **WOFF2 only** (skip WOFF, TTF, EOT) | Universal browser support since 2020; ~30% smaller than WOFF; single file per weight |
| Loading | Variable fonts where possible | One file for weights 300–800 vs 3–5 separate weight files. Cuts bytes + connections. |
| Font-display | `font-display: swap` in every `@font-face` | Prevents invisible-text render blocking; text renders in fallback then swaps. INP-friendly. |
| Preload | `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the 1–2 font files used above-the-fold | Direct LCP win. Do NOT preload every weight — only the ones needed for hero copy. |
| Fallback stack | System stack fallback in `font-family` (e.g., `"Inter Var", -apple-system, BlinkMacSystemFont, sans-serif`) | Zero-FOIT experience during swap window |
| Recommended pairing | Serif display + sans body OR two contrasting sans. Design brief says navy + warm cream + gold, warm/approachable — suggest: **Fraunces (variable serif) for headlines + Inter (variable sans) for body**, both self-hosted WOFF2 | Fraunces reads warm/human (matches "compassionate family law"), Inter is neutral/legible for long-form legal content. Both variable = 2 files total. |

### Form Handling + Spam

| Layer | Recommendation | Why |
|-------|----------------|-----|
| Backend | Netlify Forms (native, no separate service) | Free tier covers volume, email notifications work, matches every other client |
| Spam filter | **The existing 24-regex + 5-heuristic library** from `reference_spam_filter_patterns.md` (rolled out to 6 client sites 2026-06-09) | Battle-tested against real spam (Douglas Mkt "design audit," Alex Bangladeshi review-buying). Silently redirects spam to `/` so bots think they succeeded. |
| Honeypot | Native Netlify honeypot field: `<input name="bot-field" hidden>` + `data-netlify-honeypot="bot-field"` on form | Catches bulk bots for free |
| reCAPTCHA v3 | **DO NOT ADD** on v1 | Adds ~200ms INP hit, third-party cookie, and legal-vertical prospects abandon forms with captchas. Regex+honeypot has been sufficient at Echo Local's volume. Revisit if spam exceeds 5/week. |
| Email notification | Netlify hook to Burkett's email + brian@echolocalagency.com | Use `{site_name}`, `{form_name}`, `{site_url}` in `subject_template` ONLY — no form-field substitution supported (learned from 12 broken hooks per PROJECT.md) |
| Field-level | Standard fields: name, email, phone, case type (dropdown: Divorce / Custody / Support / Other), message | Case-type dropdown enables downstream lead-routing without adding friction |
| Legal compliance on form | Small print: "This is not legal advice. Submitting this form does not create an attorney-client relationship. Do not send confidential information until an engagement letter is signed." | **REQUIRED** by California State Bar advertising rules. Non-optional. |

### Analytics + Search Console

| Layer | Recommendation | Why |
|-------|----------------|-----|
| Analytics | **GA4** (property injected per-site from `clients.json` — DO NOT hardcode) | Standard. Per-client injection prevents the cross-client pollution incident (Mr Green's GA id was leaking into Arcadian + Top Tier per PROJECT.md). |
| GA4 injection method | Inject via a per-site `<script>` block in `<head>` that reads `SITE_CONFIG.ga4_id` (template variable) — NOT hardcoded in shared templates | Identity guard must catch any commit with a hardcoded GA id |
| Search Console | GSC domain-property verification via DNS TXT (Cloudflare / Network Solutions) | Domain property covers all subdomains + protocols in one shot. TXT verification survives redesigns better than HTML file / meta tag. |
| Conversion tracking | GA4 events: `form_submit`, `phone_click` (tel: link), `calendar_view` (GHL calendar iframe intersection), `calendar_booked` (thanks-booked.html pageview) | Matches the Echo Local pattern (`/thanks-booked.html` redirect from GHL calendar) |
| Consent | No consent banner required for US-only site with GA4 basic mode | Save the banner UX cost. If Burkett ever serves EU clients (unlikely for SD family law), add consent v2 mode. |
| Extra | Bing Webmaster Tools (add domain, submit sitemap) | 3-minute add, catches ~5% of search referrals Google won't show |
| AVOID | Google Tag Manager | Adds a 3rd-party dependency, hurts INP by ~50–100ms, and is unnecessary for 4 events. Hard-code GA4 + fire events with 4 lines of vanilla JS. |

### Core Web Vitals Patterns (INP-focused for 2026)

INP replaced FID as a Core Web Vital in March 2024. **INP ≤ 200ms is the "Good" threshold** (Google), and family-law prospects on mobile are the exact audience Google scores harshly.

| Metric | 2026 Target | How to Hit It on Static Site |
|--------|-------------|------------------------------|
| LCP | ≤ 2.5s | Preload LCP image with `fetchpriority="high"`; self-host fonts w/ `swap`; AVIF hero; no framework JS to parse |
| INP | ≤ 200ms | **Zero unnecessary JS**. No jQuery, no page-builder scripts, no analytics tag manager. Break any handler >50ms into `requestIdleCallback` / `queueMicrotask`. Defer GHL calendar iframe below-the-fold with `loading="lazy"`. |
| CLS | ≤ 0.1 | Explicit `width`/`height` on every image + iframe; reserve space for GHL calendar with min-height wrapper; no injected banners |
| FCP | ≤ 1.8s | Inline critical CSS (or ship a single small CSS file); no render-blocking JS |
| TTFB | ≤ 800ms | Netlify's global CDN handles this by default; ensure `.html` files aren't dynamically generated |

**INP-specific static-site tactics:**
- Split any inline `<script>` >5KB into deferred external file
- Use `<script defer>` for all scripts (never blocking)
- Avoid CSS-in-JS-generated stylesheets (irrelevant here since we're vanilla, but flag for anyone tempted)
- Event handlers that write to DOM should batch via `requestAnimationFrame`
- GHL calendar embed = biggest INP risk on the site. Lazy-load its iframe + defer its script; consider intersection-observer trigger so it only mounts when scrolled into view.

### Sitemap, Robots, llms.txt

| File | Format | Notes |
|------|--------|-------|
| `sitemap.xml` | Standard XML sitemap, single file (site is ~50 URLs total, no need to split) | Include `<lastmod>` on every URL (Google uses it), no `<priority>` or `<changefreq>` (Google explicitly ignores both). Auto-updated by SEO engine's `_update_sitemap` (matches other clients). |
| `robots.txt` | Allow all crawlers; explicitly Allow: GPTBot, ClaudeBot, PerplexityBot, Google-Extended | Legal firm wants to be citable by AI search — those clients ARE their prospects. Explicit allow (redundant but a signal). |
| `robots.txt` | Reference sitemap: `Sitemap: https://childcustodyanddivorce.com/sitemap.xml` | Discovery hint for crawlers |
| `llms.txt` | 2026-current standard: markdown file at `/llms.txt` describing site structure, key pages, and a curated Q&A for LLM consumption | Emerging standard (2024–2026), adopted by AI search engines for citation surfacing. Legal is a prime GEO vertical — prospects ask ChatGPT/Perplexity "family law attorney san diego." **HIGH VALUE for legal.** |
| `llms-full.txt` | Optional companion — full markdown export of all practice pages + bio + top FAQ | Some LLM crawlers prefer the full-content variant. Since site is <50 pages, this is cheap to generate. |
| `humans.txt` | Skip | Zero SEO value, no legal signal |
| `security.txt` | `/.well-known/security.txt` with contact email | Trust signal; some GEO / crawler heuristics reward it. Cheap to add. |
| Canonical URLs | Every page: `<link rel="canonical" href="https://childcustodyanddivorce.com/PATH.html">` — self-referential | Prevents any pretty-URL / trailing-slash duplicate. **Absolute URLs, always.** |
| `pretty_urls = false` in `netlify.toml` | REQUIRED | See baseline table. Non-negotiable. |

### GBP (Google Business Profile) Integration Signals

GBP itself lives outside the site, but the site must feed it correctly:

| Signal | Site-side Implementation | Why |
|--------|-------------------------|-----|
| NAP consistency | Character-identical Name / Address / Phone on: footer of every page, contact page, `LocalBusiness` JSON-LD, GBP, BrightLocal citations | Any drift = Google trust penalty for local. Watch spacing (Georgia's "PsychicExperience" bug). |
| Address | Full physical address in footer + contact page + schema (Mission Valley: 591 Camino De La Reina, Suite 821, San Diego, CA 92108) | Physical address on-site is the pairing signal GBP checks against |
| Phone | tel: link matching GBP primary number (6192502683) | Click-to-call = tracked GA4 conversion + matches GBP for local trust |
| Hours | `openingHoursSpecification` in schema, human-readable hours on contact page, matching GBP | Cross-check |
| Reviews (embedded on site) | **Skip embedded review widgets on v1** (per project scope: no auto-review widgets). Link out to GBP reviews from contact page. | Ca State Bar has restrictions on displaying client testimonials; safer to link out than to embed. |
| Photos | Same photo set on site + GBP (Burkett's real photos from Justia archive) | Reverse-image consistency reinforces entity identity |
| GBP website URL | Set to `https://childcustodyanddivorce.com/` (root, no path) | Canonical entry point |

### YMYL / E-E-A-T Technical Signals (Legal-Specific)

Family law is a Google YMYL category. These technical signals feed E-E-A-T machine-readably:

| Signal | Implementation | Confidence |
|--------|---------------|------------|
| Author schema on every content page | `Person` JSON-LD with `jobTitle: "Attorney"`, `hasCredential`, `alumniOf`, `memberOf` (State Bar), `sameAs` (State Bar profile URL, LinkedIn, Justia legacy URL, Avvo) | HIGH — this is the single most-cited E-E-A-T signal in Google's own documentation |
| Author byline on every blog post | Visible on-page: "By Brian Burkett, Attorney at Law" linking to `/attorney-bio.html` | HIGH — both a UX signal and a schema entity-link |
| Published + Last Modified dates | Visible on-page + `datePublished` / `dateModified` in schema | HIGH — YMYL freshness is scored |
| Bar admission on-page | Bio page states "Admitted to California State Bar [year], Bar No. [number]" with link to State Bar profile | HIGH — verifiable credential, both human and machine readable |
| Practice area experience | Bio + per-practice-area page: "X years handling [practice area] in San Diego Superior Court" — sourced from Justia archive, not fabricated | HIGH — E-E-A-T's "Experience" pillar |
| Jurisdiction specificity | Every practice/blog page anchored to California family law + San Diego Superior Court, not generic "family law" | HIGH — jurisdictional accuracy is a YMYL trust signal for legal |
| Disclaimers | Footer sitewide: "This website is attorney advertising. Information on this site is not legal advice. Prior results do not guarantee a similar outcome. Contact us to discuss your specific situation." | REQUIRED by California State Bar advertising rules (Rule 7.1–7.5). Non-optional. |
| No testimonials without disclosure | If client reviews shown anywhere, include disclosure per Cal Rule 7.1 | Legal compliance |
| No guaranteed-outcome language | Content review before publish: strip "we will win," "guaranteed," "best outcome" language | Rule 7.1 compliance + Google spam signal |
| HTTPS + HSTS | Netlify default HTTPS + add `Strict-Transport-Security` header via `_headers` file | Trust signal, especially YMYL |
| Security headers | `_headers`: `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: interest-cohort=()` | Trust signal + GEO / AI-crawler heuristics reward secure sites |
| Privacy policy | Real, US-jurisdiction, references GA4 collection | Trust + linked from footer sitewide |
| Contact page with multiple channels | Address + phone + form + calendar + email = 5 contact vectors | E-E-A-T "trustworthy contact info" pattern |

---

## Supporting Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Existing spam-filter library (`reference_spam_filter_patterns.md`) | current | Form spam filter | On the contact form. Reuse verbatim from the 6 sites already using it. |
| Existing SEO engine (`~/EchoLocalClientTracker/`) | current | Blog + location page generation, sitemap update, identity guard | For blog + location page generation. Must use the leak-proof renderers (`identity.py`, `blog_renderer.py`, `location_renderer.py`) built 2026-06-23. **YMYL layer needed on top**: content fabrication validator that flags any generated legal claim not traceable to Burkett or the Justia archive (see PITFALLS.md). |
| BrightLocal citation CSV builder | current | Local citations (post-launch) | After site live, generate legal-category CSV, Brian fills category IDs + uploads |
| GHL calendar embed | pattern doc | Booking widget | Above-the-fold on home + practice pages. Burkett gets his own calendar (not the shared `PW5Ma7sjF3S6AWayZDuK`). |
| GHL contact/form webhook | pattern doc | Form submissions land in GHL for CRM tracking | Optional v1, add if lead volume warrants CRM |
| Netlify Image CDN | native | On-demand image transforms (fallback if pre-generation isn't feasible) | Only if pre-generated pipeline is too slow — default = pre-generated |

## Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| ImageMagick / `sharp` (CLI) | Pre-generate AVIF/WebP/JPEG at 3 widths from source images | Run once at build; commit output to `/img/` |
| Netlify CLI (`netlify` command, `deploy` prohibited) | Local dev preview only via `netlify dev` | NEVER `netlify deploy` — CLAUDE.md rule |
| Google Rich Results Test | Schema validation before push | Run every schema block through it before commit; JSON-LD errors are silent otherwise |
| Schema.org validator (schema.org/validator) | Broader schema validation | Catches structural errors Google Rich Results doesn't flag |
| PageSpeed Insights + CrUX | Core Web Vitals + INP measurement | Baseline before cutover + weekly during first month |
| Lighthouse (CI or local) | Pre-push perf + accessibility check | Add as a manual pre-push gate |
| GSC URL Inspection | Post-launch: submit each page for indexing | Manual, Brian does in UI (API lacks scope per PROJECT.md) |
| `hreflang` — SKIP | US-only site | Out of scope per PROJECT.md |

## Installation

```bash
# Nothing to install for the runtime (it's static HTML/CSS/JS).
# Dev-time tools (Node/Python already on system):

# Image pipeline (Node + sharp)
npm install -g sharp-cli
# OR use ImageMagick already on macOS: brew install imagemagick

# Existing tooling (already present):
# - Echo Local SEO engine at ~/EchoLocalClientTracker/
# - Existing spam filter library
# - BrightLocal CSV builder
```

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Static HTML/CSS/JS | Astro / Eleventy (SSG) | If content volume exceeded ~200 pages OR component reuse became painful. Not the case for 50-page site. |
| Static HTML/CSS/JS | Next.js / Gatsby | NEVER for this domain — framework JS hurts INP, adds YMYL risk, and violates the Echo Local pattern |
| Static HTML/CSS/JS | Squarespace / Wix / WordPress | NEVER — page-builder JS bloat + YMYL content-quality signals cannot be controlled + Google Ads negative-keyword list already blocks these terms for a reason |
| Netlify Forms | Formspree / Basin / Web3Forms | If Netlify Forms hits volume caps (~100/mo free tier) OR need advanced field-level validation. Not the case v1. |
| JSON-LD schema | Microdata / RDFa | Google prefers JSON-LD; decouples markup from rendering; MUCH easier to maintain. Never use the alternatives on a new build. |
| GA4 | Plausible / Fathom | If Burkett wants zero third-party analytics for privacy reasons. Currently he doesn't, and GA4's Ads integration is required for the Google Ads conversion tracking that's part of the package. |
| Google Search Console | Bing Webmaster only | Add BOTH — GSC primary, Bing secondary. |
| Self-hosted fonts | Google Fonts CDN | Only if font selection isn't available for self-hosting. All Google Fonts allow self-hosting; no reason to use the CDN. |
| AVIF (with WebP+JPEG fallback) | WebP-only | If build pipeline can't produce AVIF. Modern `sharp` and Netlify Image CDN both do AVIF natively as of 2024. No reason to skip AVIF in 2026. |
| Netlify pretty_urls=false | pretty_urls=true | NEVER — see SoCal deindexing incident. This is a hard-learned lesson. |
| Netlify hosting | Cloudflare Pages | Comparable performance. Would only switch if Netlify Forms became inadequate. Netlify is the Echo Local standard. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| JS framework (React / Vue / Next / Astro w/ hydration) | Hurts INP, adds YMYL risk (broken pages hurt trust), violates Echo Local pattern | Vanilla static HTML |
| Page builder (Squarespace / Wix / WordPress) | Cannot control YMYL content signals, bloated CSS/JS, hurts Core Web Vitals, hurts Google Ads relevance score | Vanilla static HTML |
| Google Tag Manager | Adds 3rd-party dependency + INP hit for 4 tracked events | Hardcoded GA4 + 4 lines of `dataLayer` push |
| reCAPTCHA v2/v3 on contact form | INP + UX cost, drives away legal-vertical prospects, existing regex+honeypot suffices | Existing spam filter library + Netlify honeypot |
| Google Fonts CDN | 3rd-party RTT hurts LCP, cookie/GDPR concerns | Self-hosted WOFF2 |
| Auto-review widgets (embedded Google/Yelp/Avvo review carousels) | California Bar Rule 7.1 disclosure risk + widget JS hurts INP | Link out to GBP reviews from contact page |
| Live chat widget (Intercom, Drift, Tawk.to, etc.) | Adds ~200ms INP + friction on YMYL + package doesn't include chat handling | tel: + calendar + form (3 CTAs already) |
| Microdata / RDFa schema | Deprecated in practice; Google prefers JSON-LD | JSON-LD |
| Priority + changefreq in sitemap.xml | Google explicitly ignores both since 2017 | lastmod only |
| Guaranteed-outcome language ("we win," "guaranteed," "best divorce lawyer in San Diego") | Violates California Bar Rule 7.1 + Google spam signal | Compassionate, factual language: "We help San Diego families through divorce" |
| Fabricated attorney credentials or "since [year]" claims | Bit Mr Green (steam/enzyme/180°F). YMYL fatal. | Only credentials sourceable from Justia archive or Burkett directly. Author schema uses verified data only. |
| Client testimonials without disclosure | California Bar Rule 7.1 violation | Link out to GBP or skip entirely on v1 |
| Hardcoded GA4 id in shared templates | Cross-client pollution bug (Mr Green id leaked into Arcadian) | Per-client injection from `clients.json` + identity guard |
| Fake location pages (`LocalBusiness` schema for cities where no office exists) | Google penalizes fake NAP for lawyers particularly harshly | `Service` + `areaServed` schema on location pages; only ONE `LocalBusiness` (Mission Valley office) sitewide |
| Blog posts >20 in v1 | Thin content flag for YMYL | Curate to 15–20 best from Justia archive; expand later based on GSC performance |
| `netlify deploy` command | CLAUDE.md hard rule | `git push origin main` → Netlify auto-deploys |

## Stack Patterns by Variant

**If Burkett later wants to add a Spanish version (hreflang):**
- Use `hreflang` `alternate` tags in `<link>` and sitemap
- Duplicate the URL structure under `/es/` (not `/es-US/`)
- Requires a certified translator for legal content — machine translation of legal terms is malpractice-adjacent
- Currently OUT OF SCOPE per PROJECT.md

**If content volume exceeds 200 pages (year 2+ growth):**
- Consider Eleventy (11ty) as a static-site generator layer on top of the same HTML output
- Preserves the vanilla runtime, adds templating for content scale
- Still commits generated HTML to git so Netlify continues serving static

**If a client portal / document upload is added post-v1:**
- Do NOT bolt onto the marketing site
- Separate subdomain (`portal.childcustodyanddivorce.com`) with a compliant hosted solution (Clio Connect, MyCase, etc.)
- Marketing site stays static; portal is a discrete auth'd app

**If Roman AI receptionist wires in (per PROJECT.md deferred scope):**
- Twilio → Retell agent bound to a new number, forwarded from Burkett's phone
- Site-side: replace `tel:6192502683` links only if the Retell number becomes primary
- GA4 event: `phone_click` still tracks the tap; call analytics come from Retell

## Version Compatibility

| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| AVIF (`<picture>` with WebP+JPEG fallback) | All browsers | AVIF native support: Chrome 85+, Safari 16.4+, Firefox 93+, Edge 121+. `<picture>` fallback covers everything else. |
| Native `loading="lazy"` | All browsers ≥ 2020 | No polyfill needed in 2026 |
| CSS `container queries` | All browsers ≥ 2023 | Baseline in 2026 |
| CSS `:has()` | All browsers ≥ 2023 | Baseline in 2026 |
| Variable fonts | All browsers ≥ 2019 | Baseline |
| JSON-LD schema | All Google + Bing + AI crawlers | Zero compatibility concern |
| `pretty_urls = false` in netlify.toml | Netlify current | Verified stable since 2023 |

## YMYL / Legal-Specific Choices (Flagged Separately)

These are the choices driven specifically by family law being a YMYL vertical + California Bar rules. Flagging so they're not dropped:

1. **`LegalArticle` schema (not just `Article`) on blog posts** — YMYL-specific machine-readable signal
2. **`Person` + `hasCredential` schema on author** — E-E-A-T's single strongest structured signal
3. **Sitewide advertising disclaimer in footer** — California Bar Rule 7.1–7.5 requirement
4. **Contact form disclaimer** — attorney-client-relationship disclaimer required by state bar
5. **No guaranteed-outcome language content review** — Rule 7.1 + Google spam
6. **Only ONE `LocalBusiness` schema (Mission Valley address)** — fake NAP for satellite location pages is a lawyer-specific Google penalty
7. **Content-fabrication validator on SEO engine** — needed on top of existing identity guard, because YMYL punishes invented facts harder than any other vertical (see PITFALLS.md)
8. **Self-hosted fonts + no GTM + no reCAPTCHA v3** — trust + privacy signals disproportionately valuable for legal
9. **Bar admission + Bar No. + State Bar profile `sameAs` link** — machine-readable credential
10. **Jurisdictional specificity in every content asset** — California / San Diego Superior Court, not generic "family law"
11. **Explicit AI crawler allowlist in robots.txt + `llms.txt`** — legal prospects use ChatGPT / Perplexity to research attorneys; being cited is high-value; legal is a prime GEO vertical
12. **Author byline visible on every blog post** — human-side E-E-A-T signal

## Sources

- **PROJECT.md** — `/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md` — constraints, cross-client learnings, locked decisions (HIGH — authoritative for this project)
- **MEMORY.md active context** — `~/.claude/projects/-Users-brianegan/memory/MEMORY.md` — Echo Local incidents: SoCal pretty_urls deindexing (2026-06-16), Ecosystem GA pollution (2026-06-16), Mr Green identity guard (2026-06-23), spam filter rollout (2026-06-09), Georgia GBP account correlation (2026-06-15) (HIGH — battle-tested)
- **Google Search Central — E-E-A-T + YMYL guidance** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content (HIGH — official)
- **Google Search Central — Structured Data (LegalService, Attorney, LocalBusiness, LegalArticle, FAQPage, BreadcrumbList, Person)** — https://developers.google.com/search/docs/appearance/structured-data (HIGH — official)
- **schema.org** — https://schema.org/LegalService, https://schema.org/Attorney, https://schema.org/LegalArticle, https://schema.org/Person, https://schema.org/FAQPage, https://schema.org/BreadcrumbList (HIGH — canonical)
- **web.dev — Core Web Vitals (INP threshold ≤ 200ms Good)** — https://web.dev/articles/inp (HIGH — official, March 2024 promotion)
- **web.dev — LCP + fetchpriority + `<link rel="preload">` for images** — https://web.dev/articles/optimize-lcp (HIGH — official)
- **caniuse.com AVIF support ≥96%** — https://caniuse.com/avif (HIGH)
- **Netlify docs — Forms + Image CDN + `pretty_urls` + `_headers`** — https://docs.netlify.com/ (HIGH — official)
- **California State Bar — Rules of Professional Conduct 7.1–7.5 (attorney advertising)** — https://www.calbar.ca.gov/ (HIGH — legal requirement)
- **llms.txt emerging standard** — https://llmstxt.org/ (MEDIUM — 2024–2026 emerging, adopted by AI search but not yet formalized)
- **Echo Local reference docs** — `reference_spam_filter_patterns.md`, `reference_netlify_pretty_urls_deindex.md`, `reference_identity_guard_system.md`, `reference_netlify_form_subject_template.md` (HIGH — internal, incident-derived)

---
*Stack research for: Solo family-law attorney SEO site (YMYL, San Diego, static + Netlify baseline)*
*Researched: 2026-07-02*
