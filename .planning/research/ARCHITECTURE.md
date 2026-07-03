# Architecture Research

**Domain:** Solo family-law attorney SEO site (San Diego / YMYL / static + Netlify baseline)
**Researched:** 2026-07-03
**Confidence:** HIGH (patterns cross-validated against 2026 ABA, PaperStreet, Rankings.io, YMM Digital, Google Search Central YMYL/E-E-A-T guidance, Echo Local cross-client incidents, and schema.org current specs)

> **Scope.** This document covers **information architecture, URL structure, topical clustering, and internal linking** — the "how the site is organized and how links flow" layer. Stack decisions (framework, hosting, schema tech) live in STACK.md. Feature decisions (what pages exist) live in FEATURES.md. This file connects those two: it defines the **page graph** and **link graph** that turns 50 static HTML files into a topically-authoritative YMYL site.

---

## Standard Architecture

### System Overview (Page Graph)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       HOMEPAGE (LegalService + LocalBusiness)            │
│              Hero + CTA trio + practice teasers + bio teaser             │
└───┬─────────────────┬──────────────────┬──────────────────┬─────────────┘
    │                 │                  │                  │
    ▼                 ▼                  ▼                  ▼
┌────────┐   ┌──────────────────┐   ┌──────────┐   ┌───────────────┐
│  BIO   │   │  PRACTICE HUB    │   │   BLOG   │   │    CONTACT    │
│(Person │   │(/practice-areas/)│   │   HUB    │   │(LocalBusiness │
│ + creds│   │      index       │   │(/blog/)  │   │  + form + map)│
└───┬────┘   └────────┬─────────┘   └────┬─────┘   └───────────────┘
    │                 │                   │
    │                 ▼                   │
    │       ┌─────────────────────────┐   │
    │       │   8 PRACTICE PILLARS    │   │
    │       │  (Service + FAQPage)    │   │
    │       │  divorce, custody,      │   │
    │       │  support, spousal,      │   │
    │       │  mediation, DV,         │   │
    │       │  guardianship, fam-ct   │   │
    │       └────┬────────────────┬───┘   │
    │            │                │       │
    │            ▼                ▼       │
    │   ┌──────────────┐  ┌───────────────┐
    │   │ LOCATION     │  │  BLOG POSTS   │
    │   │ PAGES        │  │ (LegalArticle │
    │   │(practice×city│  │  + author→Bio)│
    │   │ 15-20 total) │  │  15-20 total  │
    │   │ Service +    │  │ Categorized   │
    │   │ areaServed   │  │ by practice   │
    │   └──────────────┘  └───────┬───────┘
    │            ▲                │
    │            │                │
    └────────────┴────────────────┘
         (author byline links back to BIO,
          all pages footer-link back home,
          blog posts link OUT to matching practice pillar,
          location pages link UP to matching practice pillar,
          practice pillars link DOWN to relevant location pages + blog posts)
```

### Component Responsibilities

| Component | Responsibility | Schema Anchor | Link Direction |
|-----------|---------------|---------------|----------------|
| **Homepage** (`/index.html`) | Front door. CTA trio (phone + calendar + form). Practice teasers (all 8). Bio teaser. Trust markers. | `LegalService` + `LocalBusiness` (multi-type) | Links DOWN to all 8 practice pillars + bio + top 3 location pages + top 3 blog posts. Links to contact. |
| **Attorney Bio** (`/attorney-bio.html`) | E-E-A-T taproot. Credentials, bar admission, experience, real photo. Author identity for all content. | `Person` w/ `hasCredential`, `alumniOf`, `memberOf` (CA State Bar), `sameAs` | Links DOWN to practice hub + representative practice pages (top 3-4). Every blog post + every practice page links UP to this bio via byline. |
| **Practice Hub** (`/practice-areas/index.html`) | Navigation waypoint listing all 8 practice pillars w/ 40-60 word teaser + link. Also carries breadcrumb parent for all practice pillar pages. | `CollectionPage` + `BreadcrumbList` | Links DOWN to all 8 pillars. Links UP to home. Cross-links to bio. |
| **Practice Pillar Page** (8 total, e.g., `/practice-areas/divorce/index.html`) | Comprehensive answer to "what does [practice] look like in California / San Diego?" 1000-1500 words. FAQ block. CTA trio. | `Service` (provider = `LegalService`) + `FAQPage` + `BreadcrumbList` | Links UP to practice hub + home. Links DOWN to matching location pages (practice × city variants) + related blog posts (topical cluster spokes). Cross-links to related practice pillars (e.g., Divorce ↔ Child Custody ↔ Spousal Support). Links to bio via author byline. |
| **Location Page** (15-20 total, e.g., `/san-diego/divorce-attorney/index.html`) | Answer "[practice] attorney in [SD-area]?" with genuine local content (courthouse, filing office, local considerations). ~600-900 words minimum. FAQ. CTA trio. | `Service` w/ `areaServed: {@type: City}` + `FAQPage` + `BreadcrumbList` (NOT `LocalBusiness` — only Mission Valley is real) | Links UP to matching practice pillar + home. Cross-links to 2-3 sibling location pages (same practice, different city; or different practice, same city). Links to bio via byline. |
| **Blog Hub** (`/blog/index.html`) | Chronological + category-faceted listing of 15-20 posts. Category filter/nav (Divorce, Custody, Support, Mediation, DV, etc. — mapped to the 8 practice areas). | `Blog` + `BreadcrumbList` | Links UP to home. Links DOWN to all blog posts. Cross-links to practice hub. |
| **Blog Post** (15-20 total, e.g., `/blog/how-long-does-divorce-take-in-california/index.html`) | 800-1500 word deep-dive on one question or topic. Author byline. Publish + updated dates. CTA trio at bottom + inline mid-scroll. | `LegalArticle` w/ `author: Person → bio.@id`, `publisher: LegalService`, `about: Thing`, `datePublished`, `dateModified` | Links UP to blog hub + home. Links to matching practice pillar (topical cluster). Cross-links to 2-3 related posts (same practice cluster). Links to bio via byline. |
| **Contact** (`/contact.html`) | Final-mile conversion. Form + calendar + phone + address + hours + map + parking. Canonical NAP source. | `LegalService` + `LocalBusiness` full NAP + `openingHoursSpecification` + `hasMap` + `geo` + `contactPoint` | Terminal node — inbound from every page's footer + header + CTA trio, does not link deeper. |
| **Legal Pages** (Privacy, Terms, Disclaimer) | Compliance. Linked from footer only. | `WebPage` + `BreadcrumbList` (optional) | Footer-only inbound. Terminal. |
| **Thanks Pages** (`/thanks.html`, `/thanks-booked.html`) | GA4 conversion firing pages. | `WebPage`, `noindex` | Referenced only by form action + GHL calendar redirect. Not in sitemap. |
| **Sitewide Header** | Sticky. Logo (→home), 4-item nav (Practice Areas / About / Blog / Contact), sticky phone button (`tel:6192502683`). Mobile hamburger. | — | Present on every page. |
| **Sitewide Footer** | NAP block (character-identical everywhere), hours, phone, disclaimers, legal-page links, sitemap link, "Licensed in California only." | Contributes to sitewide `Organization`/`LegalService` reinforcement | Present on every page. |
| **Breadcrumbs** | Visible + JSON-LD `BreadcrumbList` on every non-home page. | `BreadcrumbList` | Reinforces IA graph in schema. |

---

## Recommended Project Structure (Static HTML Layout)

```
/                                     # site root, deployed as-is from git
├── index.html                        # homepage (LegalService + LocalBusiness)
├── attorney-bio.html                 # bio (Person + credentials)
├── contact.html                      # contact (LocalBusiness canonical NAP)
├── privacy.html                      # legal
├── terms.html                        # legal
├── disclaimer.html                   # legal (CA Bar advertising)
├── thanks.html                       # form conversion GA event, noindex
├── thanks-booked.html                # calendar booking GA event, noindex
│
├── practice-areas/                   # PRACTICE HUB + 8 pillar pages
│   ├── index.html                    # hub listing all 8 with teasers
│   ├── divorce/index.html            # pillar 1
│   ├── child-custody/index.html      # pillar 2
│   ├── child-support/index.html      # pillar 3
│   ├── spousal-support/index.html    # pillar 4  (alias slug: /alimony/ optional 301)
│   ├── mediation/index.html          # pillar 5
│   ├── domestic-violence/index.html  # pillar 6
│   ├── guardianship/index.html       # pillar 7
│   └── family-court/index.html       # pillar 8
│
├── san-diego/                        # LOCATION PAGES (practice × city matrix)
│   ├── index.html                    # areas-served hub (optional, links to all city×practice combos)
│   ├── divorce-attorney/
│   │   ├── la-jolla/index.html
│   │   ├── chula-vista/index.html
│   │   ├── carlsbad/index.html
│   │   ├── el-cajon/index.html
│   │   └── escondido/index.html
│   ├── child-custody-lawyer/
│   │   ├── la-jolla/index.html
│   │   ├── chula-vista/index.html
│   │   └── ...                       # (top 4-5 cities for top 3-4 practices = 15-20 pages)
│   ├── child-support-attorney/
│   │   └── ...
│   └── mediation/
│       └── ...
│
├── blog/                             # BLOG HUB + 15-20 posts
│   ├── index.html                    # hub (chronological + category nav)
│   ├── category/
│   │   ├── divorce/index.html        # category page — 1 per practice area
│   │   ├── child-custody/index.html
│   │   ├── child-support/index.html
│   │   ├── spousal-support/index.html
│   │   ├── mediation/index.html
│   │   ├── domestic-violence/index.html
│   │   ├── guardianship/index.html
│   │   └── family-court/index.html
│   ├── how-long-does-divorce-take-in-california/index.html
│   ├── what-is-a-legal-separation-in-california/index.html
│   └── ... (15-20 posts total, kebab-case slugs preserved from Justia archive where possible)
│
├── img/                              # AVIF + WebP + JPEG at 3 widths, pre-generated
│   ├── burkett-headshot-800.avif
│   ├── burkett-headshot-800.webp
│   ├── burkett-headshot-800.jpg
│   └── ...
│
├── fonts/                            # self-hosted WOFF2 (Fraunces + Inter variable)
│   ├── fraunces-var.woff2
│   └── inter-var.woff2
│
├── css/                              # single stylesheet; critical CSS inlined in <head>
│   └── site.css
│
├── js/                               # progressive-enhancement only
│   ├── nav.js                        # mobile hamburger
│   ├── form.js                       # spam filter + submit
│   └── calendar-embed.js             # lazy-mount GHL iframe
│
├── downloads/                        # v1.x — gated PDFs (custody checklist, etc)
│   └── (not built in v1)
│
├── sitemap.xml                       # single sitemap, all URLs, <lastmod>
├── robots.txt                        # allow all + explicit GPTBot/ClaudeBot/PerplexityBot allow
├── llms.txt                          # 2026-current standard, high value for legal GEO
├── llms-full.txt                     # optional full-content export
├── .well-known/security.txt          # trust signal
├── _headers                          # HSTS + security headers (Netlify)
├── _redirects                        # any Justia-slug legacy 301s
└── netlify.toml                      # pretty_urls = false (REQUIRED)
```

### Structure Rationale

- **Directory-per-URL, always ending in `/`.** Every non-root page is a folder + `index.html`, not `page.html`. Cleaner canonical URLs (`/practice-areas/divorce/` not `/practice-areas/divorce.html`), consistent trailing-slash behavior, and matches how Netlify serves `pretty_urls=false` correctly. It also lets us add sibling assets (e.g., `/practice-areas/divorce/img/`) later without slug collisions.
- **`/practice-areas/` as the practice hub root.** Groups all 8 pillars under one topical parent. Reinforces the "family law → 8 verticals" hierarchy in the URL itself. Breadcrumbs match: Home > Practice Areas > Divorce.
- **`/san-diego/[practice-slug]/[city-slug]/` for location pages.** Two-level location matrix. Reads naturally in schema `areaServed`. Keeps practice grouping (all divorce-attorney city pages under `/san-diego/divorce-attorney/`), which enables a per-practice-per-city sub-hub if we ever want one. The `-attorney` / `-lawyer` suffix on the practice slug matches the actual search query pattern ("divorce attorney la jolla"), which is a mild slug-level relevance signal. **Do NOT use `/practice-areas/divorce/la-jolla/`** — that conflates the pillar with a city and forces the practice pillar canonical to compete with the location page for the same parent path.
- **`/blog/` flat + `/blog/category/[practice-slug]/`.** Flat slugs for posts (no year/month) keeps URLs stable across future updates + matches Justia legacy slug preservation. Category pages under `/blog/category/` provide the topical-cluster spoke back to the practice pillar without polluting the flat post URL space.
- **Legal pages in root, not `/legal/`.** They are terminal; nesting them buys nothing and burns a directory level.
- **No `/services/` or `/attorneys/` folder.** Solo practice; only one attorney. Bio lives at root as `/attorney-bio.html`. No plural.
- **`img/`, `fonts/`, `css/`, `js/` at root.** Static asset flat directories. Matches Chef Dorothy / Psychic Experience / Mr Green pattern.
- **`sitemap.xml` single file.** Site is ~50 URLs. No need to segment into `sitemap-pages.xml` + `sitemap-blog.xml`. Google recommends splitting only above 50K URLs.

---

## URL Structure Conventions

### The Rules (Non-Negotiable)

1. **Lowercase, kebab-case slugs.** No underscores, no camelCase, no capitals.
2. **Trailing slash on directory URLs.** `/practice-areas/divorce/` not `/practice-areas/divorce`.
3. **No stop words in slugs.** `divorce-attorney` not `the-divorce-attorney-in`.
4. **No year in blog slugs.** `/blog/how-long-does-divorce-take-in-california/` not `/blog/2026/how-long-does-divorce-take/`. Dates live in schema + on-page, not URL. This lets us update posts without URL churn.
5. **Self-referential absolute canonical on every page.** `<link rel="canonical" href="https://childcustodyanddivorce.com/practice-areas/divorce/">` — full URL, no trailing-`index.html`.
6. **No query-string parameters on canonical URLs.** UTM parameters are for outbound tracking only; internal links never carry them.
7. **Slug preservation from Justia archive where practical.** Any Justia blog post whose slug we keep gets a `_redirects` entry from the old URL to the new. Slugs that are keyword-weak get rewritten; log every rewrite for a redirect map.

### URL Templates

| Page Type | URL Template | Example |
|-----------|--------------|---------|
| Homepage | `/` | `/` |
| Attorney bio | `/attorney-bio/` (folder+index) OR `/attorney-bio.html` if legacy | `/attorney-bio/` |
| Contact | `/contact/` | `/contact/` |
| Practice hub | `/practice-areas/` | `/practice-areas/` |
| Practice pillar | `/practice-areas/[practice-slug]/` | `/practice-areas/child-custody/` |
| Location page | `/san-diego/[practice-slug-plus-role]/[city-slug]/` | `/san-diego/divorce-attorney/la-jolla/` |
| Blog hub | `/blog/` | `/blog/` |
| Blog category | `/blog/category/[practice-slug]/` | `/blog/category/child-custody/` |
| Blog post | `/blog/[post-slug]/` | `/blog/how-long-does-divorce-take-in-california/` |
| Legal | `/[name].html` | `/privacy.html`, `/disclaimer.html` |
| GA-only pages | `/[name].html` w/ `noindex` | `/thanks.html`, `/thanks-booked.html` |
| Sitemap | `/sitemap.xml` | `/sitemap.xml` |
| Robots | `/robots.txt` | `/robots.txt` |
| llms.txt | `/llms.txt` and `/llms-full.txt` | `/llms.txt` |

**Practice slug canonical list (locked, use these exact strings sitewide):**
`divorce`, `child-custody`, `child-support`, `spousal-support`, `mediation`, `domestic-violence`, `guardianship`, `family-court`

**Location role suffix (used only on location pages, matches search query pattern):**
- `divorce-attorney`, `child-custody-lawyer`, `child-support-attorney`, `mediation` (mediation typically searched without role suffix)
- Pick ONE role suffix per practice for all its city pages and keep it consistent. Mixing `-attorney` and `-lawyer` for the same practice across cities fragments internal linking.

**City slug list (initial 15-20 pages — top practices × top cities):**
`la-jolla`, `chula-vista`, `carlsbad`, `el-cajon`, `escondido`, `oceanside` (candidate), `poway` (candidate). Confirm final 5-6 cities against Burkett's SD County zip codes doc.

---

## Topical Clustering (Hub-and-Spoke)

Family law has natural topical clusters that mirror how prospects search AND how Google's topical-authority ranking works. Each practice pillar is the **hub**; blog posts + FAQ items + related sub-topics are **spokes**. This is the single most-important IA pattern for YMYL organic growth.

### Cluster Model

```
[PRACTICE PILLAR PAGE]  ← the hub, ~1200 words, comprehensive overview
    │
    ├──> spoke: [BLOG POST answering a specific sub-question]
    ├──> spoke: [BLOG POST answering another sub-question]
    ├──> spoke: [BLOG POST covering process step-by-step]
    ├──> spoke: [LOCATION PAGE: this practice in La Jolla]
    ├──> spoke: [LOCATION PAGE: this practice in Chula Vista]
    └──> spoke: [FAQ block on the pillar itself — inline sub-topics]

Every spoke links UP to the pillar.
Every pillar lists + links DOWN to its spokes ("Related articles" / "Areas we serve").
Sibling spokes cross-link to 2-3 peers (same cluster).
```

### The 8 Clusters (Pillar → Spoke Mapping)

Assumes the 15-20 curated blog posts get distributed across the 8 pillars. Not every pillar will have equal blog coverage in v1 — some pillars (divorce, custody) support 3-4 spokes each; others (guardianship, family-court) may launch with just the pillar + FAQ + location cross-links.

| Pillar | Pillar Page URL | Sub-Topics (potential spokes — pick from Justia archive for v1) | v1 Spoke Target |
|--------|-----------------|-----------------------------------------------------------------|-----------------|
| **Divorce** | `/practice-areas/divorce/` | Uncontested divorce; Contested divorce; High-asset divorce; Military divorce; Summary dissolution; Divorce timeline in CA; Property division (community property); Legal separation vs divorce | 3-4 blog spokes + 3-5 location pages |
| **Child Custody** | `/practice-areas/child-custody/` | Legal vs physical custody; Custody modification; Move-away requests; Custody evaluation; Parenting plans; Grandparent visitation | 3-4 blog spokes + 3-5 location pages |
| **Child Support** | `/practice-areas/child-support/` | CA guideline calculator basics; Modification of support; Enforcement; Interstate (UIFSA); Arrears | 2-3 blog spokes + 2-3 location pages |
| **Spousal Support** | `/practice-areas/spousal-support/` | Temporary vs permanent alimony; Modification; Duration formula; Marital standard of living | 2 blog spokes + 2-3 location pages |
| **Mediation** | `/practice-areas/mediation/` | When mediation works; Mediation vs litigation; Confidentiality; Cost comparison | 1-2 blog spokes + 1-2 location pages |
| **Domestic Violence** | `/practice-areas/domestic-violence/` | Emergency Protective Orders; DVRO process; Effect on custody; Move-out orders | 1-2 blog spokes (sensitive vertical, exit-safety copy required) |
| **Guardianship** | `/practice-areas/guardianship/` | Probate vs juvenile guardianship; Guardian ad litem; Termination | 1 blog spoke, pillar + FAQ carries most weight |
| **Family Court** | `/practice-areas/family-court/` | San Diego Superior Court process; Filing basics; Ex parte hearings; RFO (Request for Order) | 1 blog spoke, pillar + FAQ carries most weight |

**Cluster hygiene rules:**
- Every blog post belongs to **exactly one** primary pillar (its "category"). It may cross-link to sibling clusters but its schema `about` + category tag is single.
- Location pages belong to **exactly one** pillar (the practice slug in the URL).
- Every spoke MUST link back to its pillar in the body copy — not just in a nav.
- Pillars link to their spokes in a "Related articles" / "Areas we serve in [city]" block below the FAQ.
- Cross-cluster links happen (e.g., a Divorce pillar links to Child Custody pillar because they co-occur in real cases) but stay to 2-3 max — over-linking dilutes topical signal.

### Why This Matters (YMYL-Specific)

Google's helpful-content + E-E-A-T signals reward sites where a **single expert covers a topic in depth across a related set of pages**, not sites where scattered posts cover unrelated topics. For a solo attorney, this is a natural fit: Burkett is one person with deep experience in 8 sub-domains of family law. The cluster IA makes that expertise legible to Google's crawler. Cross-client learning: the Echo Local SEO engine's blog + location generators fabricated cross-topic content when identity guards weren't in place (Mr Green incident); the same pattern would kill Burkett's E-E-A-T faster because YMYL is scored harder.

---

## Information Architecture

### Main Navigation (Header, Sticky)

**Rule: 4 items maximum + phone.** Family law prospects are stressed. Simplicity converts. Every top-nav item is a destination they'd want when they're panicking.

| Nav Item | Href | Rationale |
|----------|------|-----------|
| Practice Areas | `/practice-areas/` | Directs to the hub; hub then routes to specific pillar. Do NOT expose all 8 in a mega-menu — clutters mobile and dilutes the hub's purpose. Optional: hover-dropdown on desktop with 8 pillars listed (still one click deeper than hub). |
| About | `/attorney-bio/` | "About" reads as human; "Attorney Bio" reads as legal-industry-jargon. Both work — pick "About" for warmth. |
| Blog | `/blog/` | Signals ongoing publishing + expertise. |
| Contact | `/contact/` | Terminal conversion destination. |
| **Call: (619) 250-2683** | `tel:6192502683` | Sticky button, differentiated visual style. On mobile, converts to a call icon + number. **This is the #1 conversion lever in family-law nav** — do not bury it. |

**No home nav item.** Logo (top-left) links home. Adding "Home" is redundant + burns a slot.
**No dropdown mega-menu.** Mobile-hostile + confuses stressed prospects.
**Sticky on scroll** (both desktop + mobile). Phone button stays reachable at all times.

### Secondary Navigation (In-Page Contextual)

Secondary nav is **not** a persistent sidebar. It's inline, context-appropriate blocks:

| Location | Block Type | Purpose |
|----------|-----------|---------|
| Homepage | "Our Practice Areas" 8-card grid | Routes to each pillar. |
| Homepage | "Recent Insights" 3-card blog teaser | Routes to blog. |
| Practice hub | 8-pillar list w/ 40-60 word teaser + link each | The hub's whole job. |
| Practice pillar page | "Areas We Serve" list of matching location pages (this practice × cities) at the bottom | Links pillar → spokes (location). |
| Practice pillar page | "Related Articles" 2-3 blog post links at the bottom | Links pillar → spokes (blog). |
| Practice pillar page | "Related Practice Areas" 2-3 cross-cluster links (e.g., Divorce → Child Custody, Spousal Support, Property Division) | Cross-cluster reinforcement. |
| Location page | Breadcrumb: Home > San Diego > [Practice] Attorney > [City] | IA reinforcement. |
| Location page | "Learn More About [Practice] in California" link back to pillar | Spoke → hub, prominent. |
| Location page | "Also Serving Nearby Cities" 2-3 sibling location links | Location cluster reinforcement. |
| Blog hub | Category pills/filters (Divorce, Custody, Support, Mediation, DV, Guardianship, Family Court) | Routes to `/blog/category/[slug]/`. |
| Blog post | Byline w/ author link to bio | E-E-A-T anchor. |
| Blog post | "Filed under: [Category]" link to category page | Spoke → cluster reinforcement. |
| Blog post | "Related Articles" 2-3 same-category post links at bottom | Sibling reinforcement. |
| Blog post | "About the Author" bio card at bottom (name + credential summary + link to full bio) | E-E-A-T signal + human trust. |
| Every content page | CTA trio (phone + calendar + form snippet) mid-scroll AND at bottom | Conversion recovery. |

### Footer (Sitewide)

Footer is **legal-industry footer** — dense with trust + compliance signals, not a mega-footer with 50 links.

```
┌─────────────────────────────────────────────────────────────────────┐
│ COLUMN 1: FIRM NAP              COLUMN 2: PRACTICE    COLUMN 3: SITE│
│                                  AREAS                              │
│ Law Office of Brian Burkett      Divorce               About       │
│ 591 Camino De La Reina           Child Custody         Blog        │
│ Suite 821                        Child Support         Contact     │
│ San Diego, CA 92108              Spousal Support       Sitemap     │
│                                  Mediation             Privacy     │
│ (619) 250-2683                   Domestic Violence     Terms       │
│ [email link if published]        Guardianship          Disclaimer  │
│                                  Family Court                       │
│ Hours: Mon-Fri 9am-5pm                                              │
│                                                                     │
│ [social icons if any: LinkedIn]                                     │
├─────────────────────────────────────────────────────────────────────┤
│ DISCLAIMER BLOCK (full-width, small text):                          │
│ "This website is attorney advertising. The information on this      │
│ site is not legal advice. No attorney-client relationship is formed│
│ by using this site or submitting a contact form. Prior results do  │
│ not guarantee a similar outcome. Licensed to practice law in the   │
│ State of California only."                                          │
├─────────────────────────────────────────────────────────────────────┤
│ © 2026 Law Office of Brian Burkett. All rights reserved.            │
└─────────────────────────────────────────────────────────────────────┘
```

**NAP block requirements:**
- Character-identical across footer / contact page / `LocalBusiness` JSON-LD / GBP / BrightLocal citations.
- Address on separate lines (matches GBP formatting exactly, spacing included).
- Phone in tel-friendly format: `(619) 250-2683` displayed; `tel:6192502683` underlying href.
- Hours match GBP.

**Footer link discipline:**
- Only link to **existing** pages. No "Coming Soon" placeholders.
- Practice Areas column lists all 8 pillars for internal-linking uniformity (footer link = one PageRank-equivalent link from every page).
- Do NOT dump all 15-20 location pages in the footer. That over-links satellite pages relative to the primary conversion pages. Use the sitemap.xml + on-page "Areas We Serve" blocks for location discovery.

### Breadcrumbs (Every Non-Home Page)

Visible + JSON-LD `BreadcrumbList` on every page except home + terminal pages (thanks, legal). Breadcrumbs render in Google SERP and reinforce IA machine-readably.

| Page | Breadcrumb Pattern |
|------|--------------------|
| Practice hub | Home > Practice Areas |
| Practice pillar | Home > Practice Areas > Divorce |
| Location page | Home > San Diego > Divorce Attorney > La Jolla |
| Blog hub | Home > Blog |
| Blog category | Home > Blog > Category > Child Custody |
| Blog post | Home > Blog > How Long Does Divorce Take in California? |
| Contact | Home > Contact |
| Bio | Home > About |
| Legal pages | Home > Privacy Policy |

**Breadcrumb rules:**
- Visible above the H1, in a subdued style (not competing with H1).
- Every crumb except the current page is a link.
- Current page is not linked (last item).
- JSON-LD `BreadcrumbList` mirrors visible order exactly.

---

## Practice-Area Page Anatomy (The Pillar Template)

Each of the 8 practice pillars follows the same structure. Consistency helps Google understand the cluster; variety within each page's copy avoids duplicate content.

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Breadcrumb]: Home > Practice Areas > Divorce                       │
│                                                                     │
│ [H1] Divorce Attorney in San Diego                                  │
│ [Subhead/lead paragraph, 40-80 words]                               │
│                                                                     │
│ [CTA TRIO — phone + calendar embed + short form] above fold         │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ [H2] What Is Divorce in California?                                 │
│ [200-300 words plain-language, defines the practice, mentions       │
│  CA statute framework briefly, jurisdictionally anchored]           │
│                                                                     │
│ [H2] The Divorce Process in San Diego Superior Court                │
│ [Step-by-step: petition → response → discovery → resolution         │
│  ~400 words with subheads for each step, real SD court context]     │
│                                                                     │
│ [H2] Types of Divorce We Handle                                     │
│ [Uncontested / Contested / High-asset / Military — 100 words each,  │
│  each with an internal link to the corresponding blog spoke IF one  │
│  exists, or an anchor for future expansion]                         │
│                                                                     │
│ [H2] What to Expect                                                 │
│ [Timeline visual OR bulleted list — v1 = list, v1.x = visual        │
│  timeline per FEATURES.md]                                          │
│                                                                     │
│ [H2] Frequently Asked Questions                                     │
│ [FAQPage schema. 5-8 real Q&A pairs, plain-language answers,        │
│  each 60-150 words, jurisdiction-specific.                          │
│  Curated from Justia archive or Burkett direct.]                    │
│                                                                     │
│ [H2] Related Practice Areas                                         │
│ [2-3 links: Child Custody, Spousal Support, Property Division etc]  │
│                                                                     │
│ [H2] Areas We Serve                                                 │
│ [Link list to all matching location pages, e.g.,                    │
│  "Divorce Attorney in La Jolla / Chula Vista / Carlsbad ..."]       │
│                                                                     │
│ [H2] Recent Articles on Divorce                                     │
│ [2-3 blog post cards, linked to matching cluster posts]             │
│                                                                     │
│ [CTA TRIO — again at bottom]                                        │
│                                                                     │
│ [Author byline + credential mini-card, links to /attorney-bio/]     │
│                                                                     │
│ [Sitewide footer]                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

**Length target:** 1000-1500 words visible content. YMYL practice pages under 800 words get flagged as thin.
**H1 rule:** One H1 per page, contains the primary keyword phrase naturally ("Divorce Attorney in San Diego" not "Divorce" or "Divorce Divorce San Diego Attorney Lawyer Best").
**Schema:** `Service` (with `provider: LegalService`, `areaServed: San Diego County`) + `FAQPage` + `BreadcrumbList`. Nested in a single JSON-LD `<script>` block.
**CTA discipline:** Trio above fold + trio at bottom. Optional mid-scroll snippet (phone + booking button, no full form).
**Author byline:** Not on practice pages by default (they're firm-level services, not authored articles). But `provider` schema references LegalService whose `founder`/`employee` links to Burkett's Person node. On-page author card is fine as a trust signal.

---

## Location Page Anatomy (Practice × City — Thin-Content-Proof)

Location pages are the **highest-risk pages on the site** for YMYL thin-content flags. Google specifically hunts programmatic doorway pages in legal. The IA answer is: only ship location pages that can support **genuine local content**, not template mad-libs.

### Content Differentiation Strategy

Each location page must have at least 4 of the following 6 unique-per-city content blocks. Programmatically-generated pages that only vary the city name in a template = thin content. Manual per-page depth = defensible.

| Content Block | What Makes It Non-Thin | Example (La Jolla Divorce) |
|---------------|------------------------|---------------------------|
| **Local court context** | Reference the specific SD Superior Court branch that serves that city (Central, East County, North County, South County) + filing info | "Divorce filings for La Jolla residents typically go through the Central Division at 1100 Union Street..." |
| **Neighborhood-specific considerations** | Something genuinely different about family-law practice in that city (income levels affecting spousal support ranges; military presence in Coronado/Chula Vista; property values affecting community property complexity in La Jolla) | "High property values in La Jolla often mean complex community property division..." |
| **Local geography / driving context** | Real distance/access info for Burkett's Mission Valley office from that city | "La Jolla is a 15-minute drive from our Mission Valley office via I-5." |
| **Local demographic-anchored FAQ** | 3-5 FAQ items relevant to that city's population (military family FAQ for Chula Vista, high-asset FAQ for La Jolla, etc.) | "How does high-asset divorce work for La Jolla families?" — different Q than default divorce FAQ |
| **Practice-specific city considerations** | Any real practice-specific local pattern (Escondido tends to be North County Superior; Chula Vista is South County; DV protective orders route through different divisions) | — |
| **Actual jurisdictional facts** | Real sourceable facts about the city + practice combo. NEVER fabricate. | — |

### Page Template

```
[Breadcrumb]: Home > San Diego > Divorce Attorney > La Jolla

[H1] Divorce Attorney in La Jolla, California
[Subhead: 30-60 words, mentions La Jolla + divorce + Burkett name]

[CTA TRIO above fold]

[H2] Serving La Jolla Families in Divorce Cases
[150-250 words: the office context, drive from Mission Valley,
 practice-specific local context. UNIQUE per city.]

[H2] San Diego Superior Court and La Jolla Divorce Filings
[200-300 words: which court division serves La Jolla, filing basics.
 UNIQUE per city (courts differ by area).]

[H2] What Sets Divorce in La Jolla Apart
[150-250 words: high-asset considerations, community property complexity,
 whatever is genuinely city-specific.]

[H2] Frequently Asked Questions from La Jolla Families
[3-5 FAQ items curated for THIS city × practice combo. FAQPage schema.]

[H2] Related Areas We Serve
[Links to 2-3 sibling location pages: same practice, nearby city]

[H2] Learn More About Divorce in California
[Prominent link back to /practice-areas/divorce/ pillar]

[CTA TRIO at bottom]

[Author byline mini-card → /attorney-bio/]

[Footer]
```

**Length target:** 600-900 words minimum. Under 600 = thin risk. Over 1000 = may be padding; audit for filler.
**Schema:** `Service` (with `areaServed: {@type: City, name: "La Jolla", containedInPlace: {@type: AdministrativeArea, name: "San Diego County"}}`) + `FAQPage` (city-specific FAQ) + `BreadcrumbList`. **Absolutely no `LocalBusiness` schema on location pages** — only Mission Valley is real; fake NAP for satellite cities is a lawyer-specific Google penalty vector.
**Address on page:** The Mission Valley office address should appear (with "our office serves clients from [city]" framing) so it's clear where the physical practice is. NOT a fake "office in La Jolla" reference.

### What Kills Location Pages (Anti-Patterns to Avoid)

- **Templated boilerplate with only the city name swapped.** Google detects this instantly.
- **`LocalBusiness` schema claiming an address in the city.** Fake NAP for lawyers = manual action risk.
- **Auto-generated at build-time from a CSV without editorial pass.** The Echo Local SEO engine's location_pages generator MUST be gated by a per-city editorial review before commit for Burkett specifically. Reuse the engine, but don't let it batch-ship 15 pages unvetted.
- **Copy-pasted FAQ from the parent pillar page.** Each location page needs its own FAQ subset.
- **Missing the "learn more" link back to the pillar.** Location pages that don't link to the pillar starve the pillar of internal-link support.
- **Empty or thin content backfilled with keyword-stuffed footer.** Google's helpful-content ranks the full-page signal, not the footer.

---

## Internal Linking Pattern

Internal linking is the single most-underrated YMYL SEO lever. Below is the target link graph. Every page's outbound-link discipline is designed to reinforce topical authority + drive prospects toward conversion.

### The Link Graph

```
Bio ←──── every blog post byline
Bio ←──── every practice pillar author-card
Bio ←──── every location page author-card

Home ────> 8 practice pillars (grid on home)
Home ────> Bio (teaser card)
Home ────> Contact (CTA + header)
Home ────> Top 3 blog posts (teasers)

Practice Hub ────> all 8 pillars
Practice Hub <──── every practice pillar (breadcrumb)
Practice Hub <──── every location page (breadcrumb)

Practice Pillar (Divorce) ────> matching location pages (all Divorce × cities)
Practice Pillar (Divorce) ────> cluster blog posts (2-4 spokes)
Practice Pillar (Divorce) ────> 2-3 sibling pillars (Custody, Spousal Support)
Practice Pillar (Divorce) ────> Contact + Bio
Practice Pillar (Divorce) <──── every Divorce location page ("Learn more about Divorce in California")
Practice Pillar (Divorce) <──── every Divorce blog post ("Filed under: Divorce" + inline references)

Location Page (Divorce × La Jolla) ────> Divorce pillar (up)
Location Page ────> 2-3 sibling location pages (Divorce × Chula Vista, etc.)
Location Page ────> Contact + Bio

Blog Hub ────> all 15-20 posts (grid)
Blog Hub ────> 8 category pages
Blog Category (Divorce) ────> all Divorce cluster posts
Blog Post ────> matching practice pillar (cluster reinforcement)
Blog Post ────> 2-3 sibling posts (same category)
Blog Post ────> Bio (author byline + author card)
Blog Post ────> Contact (CTA trio)

Contact ←──── every page (header + footer + CTAs)
Contact does NOT link deeper (terminal)
```

### Linking Rules

1. **Never orphan a page.** Every page must have at least 3 internal inbound links from other pages. Orphaned = ships but Google can't find it via crawl (or finds it and ignores it as low-priority).
2. **No page links to itself** (avoid `href="#"` self-links; if you want jump-to-top, use a scroll button).
3. **Descriptive anchor text.** "Learn more about child custody in California" not "click here" or "read more". Anchor text is a ranking signal.
4. **Practice pillars are the highest-priority link targets.** They should receive the most inbound internal links because they're where organic traffic lands + where high-value keywords rank.
5. **Cross-cluster linking is limited to 2-3 per page.** Beyond that dilutes topical focus.
6. **All navigation links use the canonical URL form** (`/practice-areas/divorce/` with trailing slash, no `index.html`).
7. **Never link with UTM parameters internally.** UTMs are outbound-only.
8. **Bio is linked from author byline on every content page.** This is the E-E-A-T machine-readable signal AND the human trust signal.
9. **Location pages must cross-link within their practice cluster** (Divorce × La Jolla ↔ Divorce × Chula Vista) but NOT across practice clusters (Divorce × La Jolla should NOT link to Custody × Chula Vista in-body; nav can, body should stay in-cluster).
10. **Contact page never links deeper.** It's the terminal conversion node. Adding "explore our practice areas" links from Contact = re-directing conversion energy away.

### Link Depth from Home

Every page must be reachable within **3 clicks from home**. This is the crawl-depth ceiling Google's crawler prioritizes for indexing.

| Page | Depth from Home |
|------|-----------------|
| Bio | 1 |
| Contact | 1 |
| Practice Hub | 1 |
| Blog Hub | 1 |
| Practice Pillar (8 pages) | 2 (via Practice Hub or nav dropdown) — best target is 1-2 |
| Location Page (15-20 pages) | 3 (Home → Pillar → Location) |
| Blog Category (8 pages) | 2 (Home → Blog Hub → Category) |
| Blog Post (15-20 pages) | 3 (Home → Blog Hub → Post OR Home → Pillar → Post) |
| Legal pages | 2 (via footer) |

**Practice pillars should ideally be depth 1.** The best way to hit that: link all 8 pillars from home in a grid AND from the Practice Hub. That gives every pillar two depth-1 paths.

---

## Blog Information Architecture

### Blog Hub Structure

```
/blog/index.html
    - H1: "Family Law Insights" (or "Blog" — pick warm over generic)
    - Category filter bar: All / Divorce / Child Custody / Support / Mediation / DV / Guardianship / Family Court
    - Chronological grid: 15-20 post cards (image + title + author + date + category + 20-word excerpt)
    - Sidebar (optional): About the Author (Burkett mini-card) + CTA trio
    - Pagination NOT needed at 15-20 posts (single page). Add pagination when we exceed 20.
```

### Blog Categories

**8 categories mapping 1:1 to practice pillars.** Not more, not fewer. The blog's job is to serve the practice-pillar clusters; a category unrelated to a pillar is a broken cluster.

Each category page (`/blog/category/[slug]/`) is:
- 200-word intro paragraph explaining what this category covers
- Grid of all posts in this category
- Link back to matching practice pillar ("Get more depth on [Practice] →")
- Schema: `CollectionPage` + `BreadcrumbList`

### Blog Post Anatomy (Article Template)

```
[Breadcrumb]: Home > Blog > How Long Does Divorce Take in California?

[H1] How Long Does Divorce Take in California?
[Byline: "By Brian Burkett, Attorney at Law | Published July 3, 2026 | Updated..."]
[Category tag: "Divorce" → links to /blog/category/divorce/]

[Featured image w/ alt text]

[Intro paragraph — 50-100 words summarizing the answer]

[H2, H3 body content — 800-1500 words, plain-language, jurisdiction-anchored,
 real facts sourced from Justia archive or Burkett direct.
 NO fabricated statistics. NO invented case studies.
 Use bulleted lists + short paragraphs for AI-search citability.
 Break every 200-300 words with a subhead for scanning.]

[H2] Get Help With Your Divorce in San Diego
[CTA trio inline — mid-post + at bottom]

[H2] About the Author
[Bio card — Burkett photo, name, credential summary, link to /attorney-bio/]

[H2] Related Articles
[2-3 cards linking to sibling posts in same category]

[H2] Learn More About Divorce
[Link back to /practice-areas/divorce/ pillar — prominent]

[Footer + disclaimer]
```

**Schema:** `LegalArticle` (subtype of `Article`) with:
- `author: {@type: Person, @id: "/attorney-bio/#person"}` — MUST resolve to the bio's Person node via `@id`
- `publisher: {@type: LegalService, ...}`
- `datePublished`, `dateModified`
- `about: {@type: Thing, name: "Divorce"}` — the topic
- `mainEntityOfPage: {@type: WebPage, @id: <this-post-url>}`

**Author + `@id` linkage is the E-E-A-T entity glue.** Every blog post's author node must use `@id` to reference the bio page's Person node so Google's entity graph resolves them as the same person. Do not stamp separate Person nodes on every post — they must all `@id`-reference back to the bio.

### Author Page (= the Attorney Bio Page)

For a solo practice, the author page IS the attorney bio page. Do not build a separate `/author/burkett/` page — it's a redundant IA node that dilutes the bio's authority.

- Bio page URL: `/attorney-bio/`
- Bio page carries the canonical `Person` schema node with `@id: "https://childcustodyanddivorce.com/attorney-bio/#person"`
- Every blog post's author references this `@id`
- Every practice pillar's `provider.founder` references this `@id`
- Bio page in-page structure:
  - H1: "Brian Burkett — San Diego Family Law Attorney"
  - Photo (real, from Justia archive)
  - Intro paragraph (warmth + credibility)
  - "Credentials" section: bar admission, bar number, year admitted, law school, undergraduate, memberships (CA State Bar, SD County Bar), any real Super Lawyers listing
  - "Practice History" section: years handling family law in San Diego (sourced from Justia)
  - "Areas of Practice" list — links to all 8 practice pillars
  - "Contact" CTA trio
  - "Recent Articles by Brian" list — links to top 3-5 blog posts
  - Schema `sameAs` links: CA State Bar profile URL, LinkedIn, Justia legacy URL (until sunset 2026-07-31, then remove), Avvo if listed

---

## Sitemap Segmentation

**Single sitemap.xml.** At ~50 URLs total, segmentation buys nothing and adds complexity.

### Sitemap Contents

Include:
- Homepage
- Attorney bio
- Contact
- Practice hub
- 8 practice pillars
- 15-20 location pages
- Blog hub
- 8 blog category pages
- 15-20 blog posts

Exclude:
- Thanks pages (`/thanks.html`, `/thanks-booked.html`) — `noindex`
- Privacy / Terms / Disclaimer — technically indexable but low-value; Google will find them via footer links. Optional include with `<priority>` cue removed (Google ignores `<priority>` anyway).

### Sitemap Format Rules

- **`<lastmod>` on every URL** — Google uses this to prioritize crawl. Set to real modification date, not build date.
- **NO `<priority>`, NO `<changefreq>`** — Google explicitly ignores both since ~2017. Adding them is dead code.
- **Absolute URLs, HTTPS, canonical form** (`https://childcustodyanddivorce.com/practice-areas/divorce/` with trailing slash).
- **Auto-updated on new post/page** — reuse the Echo Local SEO engine's `_update_sitemap` function, but adapt for Burkett's URL layout.

### Sitemap Discovery

- `robots.txt` includes `Sitemap: https://childcustodyanddivorce.com/sitemap.xml`
- Submit sitemap in Google Search Console once verified
- Submit sitemap in Bing Webmaster Tools

---

## Data Flow

### User Request Flow

```
User types query → Google SERP → clicks organic result
                                        ↓
                    Static HTML page from Netlify CDN (fast TTFB)
                                        ↓
                    Page renders (LCP < 2.5s target, INP < 200ms)
                                        ↓
                    User reads content, follows internal link OR converts:
                        - Click phone button → tel: → GA4 phone_click event
                        - Click calendar → GHL iframe → book slot → /thanks-booked.html → GA4 calendar_booked
                        - Submit form → Netlify Form → spam filter → email to Burkett + brian@echolocalagency.com → /thanks.html → GA4 form_submit
```

### Content Update Flow (Development)

```
Content change (blog post, practice page edit)
        ↓
Local edit to HTML in Cursor/VSCode
        ↓
git commit + git push origin main
        ↓
Netlify auto-build + auto-deploy
        ↓
Live in ~2 minutes
        ↓
Identity guard checks (in commit hook or pre-push): no cross-client GA id,
    no cross-client brand references, pretty_urls=false in netlify.toml
        ↓
Sitemap auto-updates via SEO engine (or manual for v1 launch)
        ↓
GSC re-crawls on its own schedule (or manual URL Inspection submit for priority pages)
```

### Schema Entity Graph (How Google Resolves Burkett as an Entity)

```
Homepage LegalService node (@id: "https://childcustodyanddivorce.com/#legalservice")
    ├── founder → Person (@id: "https://childcustodyanddivorce.com/attorney-bio/#person")
    ├── areaServed → San Diego County
    ├── address → 591 Camino De La Reina, Suite 821...
    └── sameAs → GBP URL

Bio Person node (@id: "https://childcustodyanddivorce.com/attorney-bio/#person")
    ├── jobTitle → "Attorney"
    ├── worksFor → LegalService (@id above)
    ├── hasCredential → EducationalOccupationalCredential (JD, bar admission)
    ├── memberOf → CA State Bar
    └── sameAs → CA State Bar profile, LinkedIn, Avvo, Justia (until sunset)

Every Blog Post LegalArticle node
    ├── author → @id: "https://childcustodyanddivorce.com/attorney-bio/#person" (references Bio node)
    ├── publisher → LegalService @id (references Homepage node)
    └── about → Thing (topic, e.g., "Divorce")

Every Practice Pillar Service node
    ├── provider → LegalService @id
    ├── areaServed → San Diego County
    └── hasFAQ → FAQPage node

Every Location Page Service node
    ├── provider → LegalService @id
    ├── areaServed → {City: [La Jolla], containedInPlace: {AdministrativeArea: San Diego County}}
    └── hasFAQ → FAQPage node (city-specific)

Every page has BreadcrumbList
```

This entity graph is the machine-readable version of the IA. `@id`-based cross-referencing means Google resolves "Brian Burkett attorney" as a single entity across bio + all blog posts + all practice pages, and the entity graph's completeness is a direct YMYL/E-E-A-T ranking input.

---

## Build Order (Dependency-Driven Phase Sequence)

The IA + link graph + schema graph impose a real dependency order. Ignoring it leads to orphan pages, broken bylines, and rebuild-in-place work.

### Critical Path

```
Phase A — Foundation
    1. Design system (CSS, fonts, colors, base template) — nothing links yet
    2. Netlify + GitHub deploy pipeline + netlify.toml (pretty_urls=false) — infra check
    3. Sitewide header + footer partial (with placeholder nav that will be filled in) — cross-cuts everything
    4. Attorney Bio page
        - REQUIRED FIRST because Person schema @id is referenced by every practice page (as provider.founder) and every blog post (as author)
        - No content page can ship a complete schema graph until bio is live
    5. Contact page (NAP canonical source, LocalBusiness schema)
        - Must exist before homepage LocalBusiness schema references it as address source
        - Also unblocks the CTA trio (which links to /contact/)

Phase B — Practice Structure (depends on Phase A)
    6. Practice Hub page
    7. 8 Practice Pillar pages
        - Can ship in parallel once bio + hub + template are done
        - Each carries Service + FAQPage + Breadcrumb schema
        - Each has "Areas We Serve" placeholder block (will populate when location pages ship)

Phase C — Homepage (depends on Phases A + B)
    8. Homepage
        - CTA trio wiring (calendar embed live, form live, phone tel: correct)
        - Practice teasers link to the 8 real pillar pages
        - Bio teaser links to the real bio
        - Recent Insights placeholder for blog (or omit if blog isn't shipping in parallel)
        - Homepage is intentionally NOT first because it depends on every downstream target

Phase D — Location Pages (depends on Phases A + B)
    9. Practice-hub sub-pages (`/san-diego/[practice]/index.html` optional sub-hub per practice) OR skip and go directly to leaf pages
    10. 15-20 Location Pages
        - Each links UP to its matching Practice Pillar (must exist)
        - Each links to sibling location pages in same practice cluster
        - Each has FAQ + Service + Breadcrumb schema

Phase E — Blog (depends on Phase A + B)
    11. Blog Hub
    12. 8 Blog Category pages
    13. 15-20 Blog Posts
        - Each post's author byline must reference the bio (must exist)
        - Each post's category tag must link to a category page (must exist)
        - Each post links to its matching Practice Pillar (must exist)

Phase F — SEO Technical (final; after all pages exist)
    14. sitemap.xml (auto-generated from URL list)
    15. robots.txt with sitemap ref
    16. llms.txt + llms-full.txt
    17. security.txt
    18. _headers file
    19. Canonical URL check across every page
    20. Schema validation pass (Google Rich Results Test on 1 sample of each page type)
    21. Internal-link crawl (verify no orphans, no dead links, breadcrumbs match IA)

Phase G — Cutover (final)
    22. GA4 property configuration + inject correct id into every page (per clients.json)
    23. GSC verification (DNS TXT on Network Solutions or Cloudflare — verify domain property)
    24. Form test with real submission end-to-end
    25. Calendar test with real booking end-to-end
    26. DNS cutover (Burkett action at Network Solutions — point childcustodyanddivorce.com at Netlify)
    27. Post-cutover: GSC URL Inspection + submit sitemap; Justia slug 301 map lives in _redirects
```

### Parallelization Opportunities

- **Phase B pillar pages** can be shipped in parallel by 8 sub-tasks once the template is done.
- **Phase D location pages** can be shipped in parallel (2-3 per day, per-page editorial pass required).
- **Phase E blog posts** can be shipped in parallel once bio + category pages exist. Curate + rewrite from Justia archive.
- **Phase B (pillars) and Phase E (blog) can run in parallel** if pillar template + blog template are both done. But blog posts should ship after the matching pillar so cluster links resolve immediately.

### Blocking Dependencies (Do NOT Violate)

1. **Bio must exist before any content page ships.** Otherwise blog author byline breaks, practice provider.founder breaks, schema graph incomplete.
2. **Practice pillars must exist before location pages ship.** Otherwise location page "Learn more about [Practice]" links break + cluster hub-and-spoke broken.
3. **Practice pillars must exist before blog posts ship (in same cluster).** Blog post cluster link ("Filed under: Divorce" → pillar) breaks otherwise.
4. **Contact must exist before homepage links to it.** (Trivial but stated: contact.html or /contact/ must be reachable when the homepage CTA renders.)
5. **Homepage should ship last of the primary pages** — it depends on every top-level destination.
6. **Sitemap must be generated after all pages exist** — auto-gen from the file tree.
7. **DNS cutover MUST come after form + calendar + phone are validated end-to-end.** Failed conversion path on live domain = leads lost during the 2026-07-31 window.

---

## Anti-Patterns (What NOT to Do)

### Anti-Pattern 1: Orphan Practice Pages

**What people do:** Ship a practice-area page and rely on top nav + sitemap as the only inbound links.
**Why it's wrong:** Two internal inbound links is not enough for Google to treat a page as important. Practice pillars are the highest-value organic landing pages; they need heavy internal-link support.
**Do this instead:** Every practice pillar has inbound links from: (1) header nav dropdown OR home grid, (2) practice hub page, (3) footer column, (4) every location page in that cluster (via "Learn more about [Practice]"), (5) every blog post in that cluster (via "Filed under" + inline mentions), (6) 2-3 sibling pillar cross-links. Target: 15+ inbound internal links per pillar.

### Anti-Pattern 2: Duplicated Location Boilerplate

**What people do:** Template a location page and vary only the city name across 20 pages.
**Why it's wrong:** Google detects programmatic doorway pages instantly, especially in YMYL/legal. Manual action risk. Also violates the Mr Green fabrication lesson (Echo Local internal: templates hardcoded false content).
**Do this instead:** Every location page has 4+ of the 6 differentiation blocks defined in "Location Page Anatomy" above. Editorial pass gates every page before commit. Location pages that can't be genuinely differentiated should NOT ship — better to have 12 real pages than 20 thin ones.

### Anti-Pattern 3: Deep-Buried CTAs

**What people do:** CTA lives at bottom of page or in a sidebar only.
**Why it's wrong:** Family-law prospects are stressed and skim. CTAs below the fold on mobile lose 50%+ of conversion. On practice pillars specifically, prospects often decide within the first screen whether to call.
**Do this instead:** CTA trio (phone + calendar + form snippet) above the fold on every practice pillar + location page + home. Mid-scroll CTA snippet on long pages (blog posts, pillar pages). Bottom-of-page CTA on every content page. Header sticky phone button on every page.

### Anti-Pattern 4: Unclustered Blog Dumps

**What people do:** Publish blog posts without category tagging or inter-post linking; each post floats independently.
**Why it's wrong:** Wastes the topical-authority signal Google uses to score family-law expertise. Each post ends up as a low-authority island. Also confuses users searching for "more on this topic."
**Do this instead:** Every post has: (1) single primary category = matching practice pillar, (2) inline link to the practice pillar in the body, (3) "Filed under: [Category]" link to category page, (4) 2-3 "Related Articles" links to sibling posts, (5) "Learn More About [Practice]" prominent link back to pillar. Every post reinforces its cluster.

### Anti-Pattern 5: Mega-Menu / Mega-Footer

**What people do:** Expose all 15-20 location pages + all 15-20 blog posts + all 8 pillars in the header dropdown and again in the footer.
**Why it's wrong:** Confuses stressed prospects (esp. mobile). Also flattens PageRank distribution — every page linked from every page = uniform low signal. And YMYL prospects reading a mega-menu perceive a firm that's spread thin, not one focused on family law.
**Do this instead:** Header nav = 4 items + phone. Footer = 8 practice pillars + 4-6 site links. All location + blog discovery happens through the practice hub → pillar → spoke drill-down and the blog hub → category drill-down.

### Anti-Pattern 6: LocalBusiness Schema on Every Location Page

**What people do:** Stamp full `LocalBusiness` JSON-LD with the city's name in the address field on every satellite location page.
**Why it's wrong:** Fake NAP. Google's manual-action team specifically hunts this for lawyers because it's an old-school local-SEO abuse pattern. Result: manual action or algorithmic demotion.
**Do this instead:** ONE `LocalBusiness` schema, on the homepage + contact page + footer schema, all referencing the real Mission Valley address. Location pages use `Service` schema with `areaServed: {@type: City, name: "La Jolla"}` — semantically correct, no fake NAP.

### Anti-Pattern 7: Separate Author Page for Solo Practice

**What people do:** Build `/authors/burkett/` as a separate page from `/attorney-bio/`, thinking it "helps blog SEO."
**Why it's wrong:** Splits authority between two pages. Dilutes the bio's E-E-A-T signal. Confuses the schema graph (two Person nodes referencing the same human).
**Do this instead:** Bio IS the author page. Every blog post's author schema `@id`-references the bio. No duplication.

### Anti-Pattern 8: Blog Posts With Fabricated "Case Studies"

**What people do:** Invent hypothetical client stories to make posts read more concrete.
**Why it's wrong:** YMYL fabrication risk (Mr Green lesson). Also California Bar Rule 7.1 misrepresentation risk if the hypothetical reads as a real result.
**Do this instead:** Real anonymized outcomes only, WITH mandatory disclaimer ("Past results do not guarantee similar outcomes"). Or skip case-study framing entirely — jurisdiction-specific procedural content is stronger for YMYL anyway.

### Anti-Pattern 9: URL Structure That Includes Date

**What people do:** `/blog/2026/07/how-long-does-divorce-take/`
**Why it's wrong:** Every time you update a post (which YMYL freshness requires), the URL either goes stale or you have to 301. Also implies posts get old and users skip them.
**Do this instead:** Flat blog URLs (`/blog/how-long-does-divorce-take-in-california/`). Publish date + updated date live in the byline + schema, not the URL.

### Anti-Pattern 10: Skipping Breadcrumbs on Deep Pages

**What people do:** Ship location pages or blog posts without breadcrumbs because "the nav is enough."
**Why it's wrong:** Breadcrumbs appear in Google SERP (rich result) — losing that display slot is real CTR loss. Also breadcrumbs machine-encode the IA graph for Google's crawler.
**Do this instead:** Visible breadcrumb + `BreadcrumbList` JSON-LD on every non-home, non-terminal page.

### Anti-Pattern 11: Justia Legacy URL Redirects Missing

**What people do:** Ship the new site with new URLs and don't map the old Justia URLs.
**Why it's wrong:** Loses whatever inbound link equity Justia URLs had. Also breaks bookmark traffic from existing clients + referrers.
**Do this instead:** During content curation, log every Justia URL that maps to a new URL. Add all mappings to `_redirects` as 301s. Slugs preserved where possible reduce the redirect count.

### Anti-Pattern 12: Contact Page That Links Deeper

**What people do:** Add "Explore our practice areas" / "Read the blog" links from the contact page.
**Why it's wrong:** Contact is the terminal conversion node. Diluting it with outbound links to non-conversion pages = leaking conversion energy at the moment of highest intent.
**Do this instead:** Contact page has: NAP + form + calendar + phone + map + hours + parking. That's it. Header + footer nav are there for anyone who needs to backtrack; body links stay conversion-only.

---

## Integration Points

### External Services (How the Site Talks to Them)

| Service | Integration Pattern | Notes |
|---------|--------------------|-------|
| GHL Calendar | Embed iframe on home + contact + practice pillars, lazy-mount below fold, `/thanks-booked.html` redirect for GA4 event | Burkett gets his own calendar id (not the shared `PW5Ma7sjF3S6AWayZDuK`). Container reserved w/ min-height to prevent CLS. |
| Netlify Forms | Native form action, spam filter library, Netlify hook → email to Burkett + brian@echolocalagency.com, `/thanks.html` redirect | Subject template only supports `{site_name}/{form_name}/{site_url}` — do not attempt form-field substitution. |
| GBP | NAP echo (address + phone + hours identical on site + GBP). GBP `websiteUri` = `https://childcustodyanddivorce.com/`. | Manual sync via GBP API when GBP is onboarded. |
| GA4 | Injected per-site from `clients.json` — NOT hardcoded in shared templates. Identity guard catches drift. | Standard events: `form_submit`, `phone_click`, `calendar_view`, `calendar_booked`. |
| GSC | Domain property verified via DNS TXT on Network Solutions (Burkett action). Post-verify: sitemap submit + URL inspection on primary pages. | Domain property covers all subdomains + protocols. |
| Bing Webmaster | Add domain + submit sitemap | 3-min add, catches ~5% referral. |
| Google Ads | Not a site integration per se — but conversion tracking IDs need to fire from `form_submit` + `phone_click` + `calendar_booked` events. Add gtag if using Google Ads conversion actions. | Existing Echo Local Google Ads pattern. |
| llms.txt | Static file, no runtime integration | Emerging AI-crawler standard. |

### Internal Boundaries

| Boundary | Communication Pattern | Notes |
|----------|----------------------|-------|
| Static HTML pages | No runtime communication (all pre-rendered) | Zero framework runtime. Every page is fully self-contained HTML shipped to CDN. |
| Sitewide header/footer | Reused via build-time include OR copy-paste (site is small enough for either) | Recommend using the Echo Local SEO engine's per-client template if extending it, otherwise copy-paste w/ pre-push check that all copies match. |
| Schema graph | Cross-page `@id` references (no runtime resolution — just static URIs) | E.g., blog post's `author.@id` = "https://childcustodyanddivorce.com/attorney-bio/#person". |
| Form → Backend | Netlify Forms handles POST natively | No JS handler required; spam filter is client-side JS pre-submit + Netlify honeypot. |

---

## Scaling Considerations

Site is 50-ish pages at launch, projected to grow to 100-150 pages over 6-12 months (more blog posts, more location pages). Scaling concerns are content-scaling and IA-scaling, not traffic (static + CDN scales infinitely).

| Scale | IA Adjustments |
|-------|---------------|
| **50 pages (launch)** | Current IA as-designed. Single sitemap. Flat blog. Practice hub + 8 pillars + 15-20 location + 15-20 blog + support pages. No changes needed. |
| **100 pages (6-12 mo)** | Blog category pages get more posts (5-10 per category). Still no pagination needed until 20+ per category. Consider a per-practice sub-hub for locations (`/san-diego/divorce-attorney/index.html`) if a given practice has >8 city pages. Still single sitemap. |
| **200+ pages (12-24 mo)** | Pagination on blog category pages. Split sitemap by segment (`sitemap-pages.xml` + `sitemap-blog.xml`), if the file grows unwieldy — Google caps at 50K URLs per sitemap, we're far below. Consider adding sub-topic clusters within a pillar (e.g., `/practice-areas/divorce/uncontested/`, `/practice-areas/divorce/military/`) as the pillar's FAQ + spokes accumulate enough content to promote sub-topics to real pages. |

### Scaling Priorities (What Breaks First)

1. **First bottleneck: Blog category thin content.** If a category has only 1-2 posts, the category page reads as filler. Solution: publish at pillar-first pace — new practice content = new pillar + 3 blog spokes together, not solo posts.
2. **Second bottleneck: Location page overproduction.** More cities beyond the initial 15-20 must be earned by GSC data (which cities are actually searched from). Do NOT expand location pages speculatively.
3. **Third bottleneck: Sub-topic emergence.** As a pillar's FAQ + spokes accumulate, some sub-topics deserve their own page. Watch for FAQ questions that could carry 500+ words on their own — promote them to a dedicated page in that pillar's sub-directory.
4. **Fourth bottleneck: Cross-linking overhead.** Beyond 50 pages, manual cross-link maintenance becomes brittle. Consider Eleventy or the Echo Local SEO engine's templating layer to auto-generate related-page blocks at build time.

---

## What Depends on What (Summary Table for Roadmap)

| Component | Depends On | Blocks |
|-----------|-----------|--------|
| Design system + base template | — | Everything else |
| Sitewide header + footer partial | Design system | Every page |
| Netlify + GitHub deploy pipeline + netlify.toml | — | Cutover |
| Attorney Bio | Base template | Every content page's schema graph (author + provider.founder) |
| Contact page | Base template, NAP decision | Homepage LocalBusiness reference; CTA trio destination |
| Practice Hub | Base template | Practice pillars breadcrumb parent |
| 8 Practice Pillars | Bio, Practice Hub, base template | Location pages, blog posts (cluster hub), homepage teasers |
| Homepage | Bio, Contact, Practice Pillars, CTA integrations | — (top of graph) |
| Location pages | Matching practice pillars, editorial pass | — (leaf nodes) |
| Blog Hub | Base template | Blog posts breadcrumb parent |
| Blog Category pages | Blog Hub, matching practice pillar | Blog posts breadcrumb parent |
| Blog Posts | Bio, matching category page, matching practice pillar | — (leaf nodes) |
| sitemap.xml | All pages exist | Google discovery |
| robots.txt | Sitemap URL known | Google + AI crawler discovery |
| llms.txt | Content pages exist (for curated Q&A) | AI-search citability |
| GA4 injection | clients.json entry for Burkett | Conversion tracking |
| GSC verification | DNS access | Sitemap submission |
| Form validation end-to-end | Netlify form, spam filter, notification hook | Cutover safety |
| Calendar validation end-to-end | GHL calendar id for Burkett, embed working | Cutover safety |
| DNS cutover (Burkett) | Every above validated | Live launch |

---

## Sources

- **PROJECT.md** — `/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md` — scope, content source, cross-client learnings (HIGH — authoritative)
- **STACK.md** — `/Users/brianegan/Desktop/burkett-law/.planning/research/STACK.md` — schema decisions, canonical URL rules, technical baseline (HIGH — internal, consistent with this doc)
- **FEATURES.md** — `/Users/brianegan/Desktop/burkett-law/.planning/research/FEATURES.md` — page types, MVP, feature dependencies (HIGH — internal)
- **Google Search Central — E-E-A-T + YMYL guidance** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content (HIGH — official)
- **Google Search Central — Breadcrumb + Structured Data** — https://developers.google.com/search/docs/appearance/structured-data/breadcrumb (HIGH — official)
- **Google Search Central — Sitemaps best practices** — https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview (HIGH — official)
- **schema.org — LegalService, Attorney, LegalArticle, Person, FAQPage, BreadcrumbList, Service** — https://schema.org/ (HIGH — canonical)
- **PaperStreet — Best Family Law Websites 2026** — https://www.paperstreet.com/best-family-lawyer-websites/ (MEDIUM — vertical patterns)
- **Rankings.io — Family Lawyer Website Design 2026** — https://rankings.io/blog/web-design-for-family-lawyers/ (MEDIUM)
- **YMM Digital — SEO for Family Law Attorneys 2026 Roadmap** — https://ymmdigital.com/search-engine-optimization-for-family-law-attorneys-a-2026-roadmap/ (MEDIUM — vertical + local SEO)
- **ABA Law Technology Today — Solo Attorney Website Guidance** — https://www.americanbar.org/groups/law_practice/resources/law-technology-today/ (HIGH — authoritative)
- **Echo Local internal references** — `reference_netlify_pretty_urls_deindex.md` (SoCal deindex incident), `reference_identity_guard_system.md` (cross-client contamination fix), `reference_spam_filter_patterns.md` (HIGH — battle-tested)
- **California State Bar — Rules of Professional Conduct 7.1–7.5** — informs disclaimer + testimonial IA (HIGH — legal)

---

*Architecture research for: Solo family-law attorney SEO site, San Diego / YMYL*
*Researched: 2026-07-03*
