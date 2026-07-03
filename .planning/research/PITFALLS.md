# Pitfalls Research

**Domain:** Solo family-law attorney SEO website — YMYL, San Diego, California State Bar Rule 7.1–7.5 jurisdiction, Justia cutover
**Researched:** 2026-07-03
**Confidence:** HIGH for Echo Local incidents (battle-tested), HIGH for CA Bar rules (canonical), HIGH for YMYL/E-E-A-T (Google authoritative), MEDIUM for specific 2026 SERP behavior around FAQ + AI Overviews

> **Scope note.** This file is opinionated and specific. Generic web pitfalls (XSS, SQL injection, "test your code") are out of scope — vanilla static HTML doesn't have those attack surfaces. Every pitfall below is a real failure mode for family-law/YMYL/California/Netlify/Echo Local, either observed cross-client or documented in Cal Bar / Google authoritative sources.

---

## Critical Pitfalls

### Pitfall 1: Content Fabrication (Invented Case Results, Statistics, "Since [Year]" Claims, Fake Expertise)

**What goes wrong:**
The SEO engine or a well-intentioned copywriter generates plausible-sounding claims that aren't traceable to Burkett or the Justia archive. Examples: "Over 500 divorce cases successfully resolved," "20+ years in San Diego Superior Court," "recognized as a top custody attorney by X," "our team," specific outcome percentages, invented multi-lawyer language for a solo, or generic California family-law statistics without a source.

**Why it happens:**
- SEO engine templates were tuned for volume across other Echo Local clients (Mr Green: fabricated steam/enzyme/180°F/"since 2019" claims that shipped and required scrub).
- Generic industry blog templates default to "we/our team/our firm" (Burkett is solo).
- Copy-tone pressure to sound established leads to reaching for round numbers ("20+ years," "1000+ clients").
- Justia mill content that Burkett inherited already contained mill-scale phrasing — carrying it over without a fact-check pass replicates the lie under a new name.

**Consequences:**
- YMYL Google demotion — Dec 2025 update extends E-E-A-T scrutiny to any competitive query. Legal is the highest-scrutiny tier.
- California State Bar Rule 7.1 violation (false or misleading communication about services) — bar complaint risk, not hypothetical.
- Permanent reputation damage in a small SD legal community if a peer or opposing counsel notices.
- Rewrite cost is high: every fabricated claim eventually surfaces and every occurrence must be tracked (Mr Green scrub touched 39 blog posts).

**How to avoid:**
- Build a **content fabrication validator** on top of the existing identity guard. Whitelist-only source of truth: Justia archive + Burkett-verified additions. Reject any generated content containing:
  - Numeric claims not present in source (`\d+\s+(years|cases|clients|families)`)
  - Award/recognition claims (`recognized|top-rated|award|super lawyer|best|leading`) unless in Burkett-verified allowlist
  - Multi-person pronouns (`our team|our attorneys|our firm|we (win|guarantee|handle)`) — force singular voice for a solo practice
  - Guarantee language (`guaranteed|we will win|best outcome|proven results`) — Rule 7.1 violation
  - Any "since [year]" or founding-year claim not verified
- Every practice-area page, blog post, and location page must pass validator before Netlify deploy.
- Human review gate: Burkett approves any factual claim about his experience or credentials before commit.
- Source-of-truth doc at `.planning/content-facts.md` with Burkett-verified: bar admission year, bar number, law school, year of practice history, verified case types.

**Warning signs:**
- Copy uses "we/our team" for a solo attorney.
- Round numbers appear without a citation (`500+ cases`, `20 years`, `95% success`).
- Award badges without a linked source.
- Content-fabrication validator run against draft returns matches.
- Any blog post byline reads "Law Office of Brian Burkett Team."

**Phase to address:**
Phase A (Foundation) — build the validator BEFORE any content generation. Phase B (Content) — every generation run gates on validator. Phase D (Location pages) — validator run again (highest fabrication risk because templates want city-specific claims).

---

### Pitfall 2: E-E-A-T Weak Signals — Missing Author Bio, No On-Page Credentials, No Dates, Generic Jurisdiction

**What goes wrong:**
Blog posts ship without a byline. Practice area pages don't state the attorney's credentials. Content refers vaguely to "family law" instead of California family law + San Diego Superior Court. Missing `datePublished` / `dateModified` on articles. `Person` schema is absent or lacks `hasCredential`. Author schema doesn't `sameAs`-link to the CA State Bar profile.

**Why it happens:**
- Content templates were built for lower-stakes verticals (turf care, landscaping, floors) where E-E-A-T bar is lower.
- "Add a bio" gets pushed to a later phase and never lands.
- The Justia inherited content often lacked bylines because the site was Justia-authored, not attorney-authored.
- Author schema is a text file most editors never touch.

**Consequences:**
- YMYL Google demotion — E-E-A-T is the single highest-weighted YMYL signal per Google Search Quality Rater guidelines.
- Missed AI-search citations — ChatGPT/Perplexity/Google AI Overviews favor authored, dated, credentialed content for legal queries.
- Bounce increase — a stressed prospect who can't find "who is this attorney?" in 5 seconds leaves.

**How to avoke:**
- Ship the attorney bio page FIRST (Phase B start). Every other content asset references it via visible byline + schema `sameAs` / `@id`.
- Visible byline on every blog post: "By Brian Burkett, Attorney at Law — Published [date] · Updated [date]" linking to `/attorney-bio.html`.
- Every practice-area page footer: "Prepared by Brian Burkett, Attorney at Law. Licensed in California. San Diego office."
- Every content page schema block includes `Person` with `hasCredential` (JD, CA Bar admission with year + bar number) and `sameAs` to State Bar profile URL.
- Every article schema has `datePublished` + `dateModified`.
- Jurisdiction lint: any content page must mention "California" and "San Diego" (or a specific SD sub-region). Fail commit if generic-only.
- Bio page states: bar number, admission year, law school, year of first practice, verifiable memberships (SD County Bar Assoc, CA State Bar).

**Warning signs:**
- Blog posts published without a visible byline.
- "Article" schema instead of `LegalArticle`.
- `Person` schema without `hasCredential`.
- Content grep for "California" or "San Diego" returns zero on a practice page.
- `datePublished` on all posts is today (batch-published — Google notices).

**Phase to address:**
Phase B (Content) — bio page ships day 1 of Phase B. Schema block written as reusable snippet before any practice/blog page is written. Phase F (Schema QA) verifies via Rich Results Test.

---

### Pitfall 3: California State Bar Rule 7.1–7.5 Violations (Misleading Claims, Unauthorized Specialization, Missing Disclaimers, Testimonial Misuse)

**What goes wrong:**
Site contains one or more of:
- **Rule 7.1 (Communications about services):** unsupported comparisons ("San Diego's best divorce attorney"), guarantee language, testimonials without disclosure, statistics without substantiation, unqualified past-results claims.
- **Rule 7.2 (Specialization):** Claiming "specialist," "specializes in," or "expert in family law" without CA State Bar Board of Legal Specialization certification. Burkett is a family-law attorney but the word "specialist" is a term of art in California and reserved for certified specialists.
- **Rule 7.3 (Solicitation):** Language that reads as direct solicitation of a specific prospective client (rare on a website, but "we know you need help now — click here for a guaranteed result" could be construed).
- **Rule 7.4 (Communication about services — false/misleading):** overlaps with 7.1.
- **Rule 7.5 (Firm names / letterheads):** implying multiple attorneys ("our team," "our attorneys") when Burkett is solo, or using a firm name that implies partnership.

**Why it happens:**
- Marketing agencies default to superlatives ("best," "top-rated," "leading") because they convert in non-regulated verticals.
- Cal Bar rules were revised (numbering changed from 1-400/1-320 to 7.x series in 2018) — older SEO playbooks reference outdated rules.
- "Specialist" is a common English word; the CA legal-advertising term-of-art usage is easy to miss.
- Testimonials get pulled from Google/Yelp/Avvo and dropped into a site without disclosure.
- Solo attorneys get pitched "our team" copy by default.

**Consequences:**
- Bar complaint. Even a dismissed complaint costs time and creates a record.
- Site required to be scrubbed on short notice — potential downtime or ugly redlines shipped fast.
- Google may also flag the same signals as spam/misleading (double penalty).

**How to avoid:**
- Copy lint rules (block commit if triggered):
  - `\b(best|top-rated|leading|#1|number one)\s+(divorce|family law|custody|attorney|lawyer)` → BLOCK
  - `\bspecialist\b` or `\bspecializes in\b` or `\bexpert(?!ise)\b` → BLOCK (allow "experience," "focuses on," "practice is limited to")
  - `\bguaranteed?\b|\bwe will win\b|\bbest outcome\b|\bproven results\b` → BLOCK
  - `\bour (team|attorneys|firm|lawyers|partners)\b` → BLOCK (solo practice)
  - `\btestimonial\b` without adjacent disclosure text → REVIEW
- Sitewide required disclaimers (footer, present on every page):
  - "This website is attorney advertising."
  - "Information on this site is not legal advice."
  - "Contacting the Law Office of Brian Burkett does not create an attorney-client relationship."
  - "Past results do not guarantee similar outcomes."
  - "Licensed in California only."
- Contact form disclaimer, above the submit button: "Submitting this form does not create an attorney-client relationship. Do not send confidential information until an engagement letter is signed."
- If any real testimonial is published, adjacent disclosure: "Testimonials reflect one client's experience and do not guarantee similar outcomes." No fabricated testimonials, ever.
- Preferred phrasings (whitelist): "focuses on," "practice is devoted to," "handles," "years of experience in," "committed advocacy," "steady representation."

**Warning signs:**
- Any headline uses "best," "top," "specialist," "expert," "guaranteed."
- Testimonial block without disclosure text.
- Footer disclaimers missing on any page (lint every page).
- Solo attorney bio uses "we" or "our team."
- Copy makes a specific outcome promise.

**Phase to address:**
Phase A (Foundation) — copy lint rules live before Phase B. Phase B (Content) — every content asset passes lint. Phase F (QA) — final human read against Cal Bar Rule 7.1–7.5 checklist before cutover.

---

### Pitfall 4: Thin / Programmatic Location Pages (Practice × City Matrix Done Wrong)

**What goes wrong:**
The 15–20 location pages ("Divorce Attorney in La Jolla," "Child Custody Lawyer in Chula Vista," etc.) are template mad-libs — same content, city name swapped. Or they're each 200–400 words with no city-specific substance. Google flags as thin content in a YMYL vertical; some deindex, and some pull the site's overall quality score down.

**Why it happens:**
- Location-page templates in the SEO engine are efficient for landscaping/turf but were never gated for YMYL depth.
- "One template × 15 cities" is genuinely tempting because it's 20 pages of coverage in an afternoon.
- Real city-specific content (local court info, neighborhood dynamics, jurisdiction-specific process) requires research per page.
- Justia archive doesn't have per-neighborhood content — nothing to copy from.

**Consequences:**
- Google deindexes some/all location pages (mirrors Mr Green + SoCal deindex incidents, though those were different root causes).
- Overall site quality score drops — hurts the substantive practice-area pages too.
- YMYL demotion specifically for family law (Google's Search Quality Rater Guidelines call out "thin YMYL content" as low-quality).

**How to avoid:**
- Every location page must have **at least three of five** city-specific elements:
  1. San Diego Superior Court branch info (which branch serves that city — Central, East County, North County, South County).
  2. Travel/logistics context for prospects in that city (commute time to Burkett's Mission Valley office, whether he can meet virtually).
  3. City-specific demographic or jurisdictional note where relevant (e.g., Chula Vista's high Spanish-speaking population + Burkett's approach if any; Rancho Santa Fe's high-asset divorce dynamics; La Jolla / high-earner considerations for support calculations).
  4. Any real neighborhood-specific FAQ ("Can I file for divorce in San Diego if I live in Escondido?").
  5. A city-anchored callout tying back to a practice page.
- Minimum 600 words per location page, and word count is enforced by lint.
- Each page's H1, meta title, meta description, and first paragraph are DIFFERENT — not template substitutions of the same string.
- Schema uses `Service` + `areaServed` at city + county level (not `LocalBusiness` — see Pitfall 6).
- Content-fabrication validator applies here too: don't invent SD Superior Court judge tendencies, don't fabricate city stats.
- Start with 15 pages, not 50. Expand only based on GSC impressions data post-launch.

**Warning signs:**
- Two location pages, when read side by side, are 90%+ identical text.
- Location page word count <500.
- All meta descriptions are the same template with one city substitution.
- GSC "Crawled – currently not indexed" cluster of location URLs post-launch.
- No mention of a San Diego Superior Court branch on a location page.

**Phase to address:**
Phase D (Location pages). Location-page renderer must have a required-elements checklist AND the fabrication validator gate. Also revisit Phase G (post-launch) to prune underperforming pages if GSC shows soft-404 pattern.

---

### Pitfall 5: Duplicate Content Across Service/Location Pages

**What goes wrong:**
"Divorce" practice page and "Divorce Attorney in La Jolla" location page share 70%+ of their content because the location page was built by prepending "In La Jolla, ..." to the practice page. Or two location pages that share a practice ("Divorce in La Jolla" and "Divorce in Del Mar") are 90% identical. Google collapses them in the index and picks one canonical (usually the wrong one), or applies a soft duplicate-content demotion.

**Why it happens:**
- Fast approach to filling out a practice × city matrix.
- Copy fatigue: writing 8 practice pages × several thousand words each is exhausting, then location pages get shortcuts.
- No cross-page similarity check in the build pipeline.

**Consequences:**
- Google picks a canonical you didn't want. Location pages get de-prioritized, practice pages dilute focus.
- Wasted crawl budget on duplicate URLs.
- YMYL secondary hit for low quality signals.

**How to avoid:**
- Cross-page similarity lint at build: compute simhash / normalized-token overlap between every pair of (practice, location) pages and (location, location) pages sharing a practice. Fail commit if any pair >50% similar (excluding shared footer/nav/disclaimer boilerplate).
- Location page content structure forces variance: city-specific FAQ, city-specific court branch, city-specific hook paragraph — cannot be copy-pasted.
- Every practice page and every location page has a unique H1, meta title, meta description, and lead paragraph.
- Self-referential canonical on each page — `<link rel="canonical" href="https://childcustodyanddivorce.com/PATH.html">` absolute URL. Never cross-canonical a location page to a practice page (that defeats their purpose).

**Warning signs:**
- Two pages have identical meta descriptions.
- GSC reports "Duplicate, Google chose a different canonical."
- Cross-page similarity lint returns hits.
- All location pages have identical FAQ blocks.

**Phase to address:**
Phase C (Practice pages) sets the variation template. Phase D (Location pages) enforces cross-page similarity lint. Phase F (QA) runs similarity report before cutover.

---

### Pitfall 6: Missing or Wrong Schema (LocalBusiness on Satellite Pages, Article Instead of LegalArticle, Broken Entity Graph)

**What goes wrong:**
- `LocalBusiness` schema stamped on every location page implying Burkett has a physical office in La Jolla, Chula Vista, etc. (he has one office, Mission Valley).
- Blog posts marked as `Article` instead of `LegalArticle` (weaker YMYL signal).
- `Attorney` schema type used directly on the person (parser support is spotty vs. `Person` with `jobTitle: "Attorney"`).
- `Person` node missing `hasCredential` — no machine-readable bar admission.
- `sameAs` links absent — Google can't reconcile Burkett's entity with State Bar / LinkedIn / Justia.
- FAQ schema with fabricated questions.
- Schema present on page but breaks Rich Results Test with silent validation errors (JSON-LD is silent — missing required properties don't throw a browser error).

**Why it happens:**
- Copy-paste schema from other Echo Local clients (turf care, landscaping) whose location pages legitimately use `LocalBusiness`.
- schema.org has both `Attorney` and `Person`-with-`jobTitle:Attorney` patterns; the former is under-supported by Google's parsers per 2026 guidance.
- Nobody runs the Rich Results Test — it's a manual step.
- FAQ blocks get filled with generic questions that don't reflect Burkett's actual practice.

**Consequences:**
- Fake-NAP `LocalBusiness` for lawyers is specifically penalized by Google (lawyer schema abuse has a dedicated spam classifier since ~2019).
- Missing `LegalArticle` = lower YMYL confidence.
- Broken entity graph = no rich results, weaker AI Overviews citation.
- Silent JSON-LD errors = schema block is present but ignored.

**How to avoid:**
- **One and only one `LocalBusiness` schema on the site** — Mission Valley address, on the home page and contact page. Location pages use `Service` + `areaServed: {@type: City}` + `provider: {@type: LegalService, ...}`.
- Blog posts use `LegalArticle` (subtype of `Article`), never plain `Article`.
- Person schema on bio page + reference on every content page's `author`. Include `hasCredential` (JD + CA Bar admission with year + bar number), `sameAs` (State Bar profile URL, LinkedIn, Justia legacy URL, GBP URL).
- FAQ questions are real Burkett-vetted questions, not generic industry queries. Drop the schema block rather than fabricate.
- Every page's schema block runs through Google Rich Results Test in Phase F QA (or via `curl` with the RRT API). CI check ideally.
- Schema validator (schema.org validator) catches structural errors RRT misses.

**Warning signs:**
- Grep for `"LocalBusiness"` returns >2 occurrences across all HTML files.
- Grep for `"Article"` where it should be `"LegalArticle"`.
- Person schema missing `hasCredential`.
- Rich Results Test returns "no rich results" or errors.
- `sameAs` array is empty.

**Phase to address:**
Phase A (Foundation) — schema template snippets written. Phase B (Content) — schema blocks integrated. Phase C, D (Practice, Location) — apply correctly per page type. Phase F (QA) — validate every page.

---

### Pitfall 7: Cutover Mistakes (DNS TTL, Canonical Mismatches, Sitemap References Old URLs, Broken Redirects from Justia URLs, Indexing Delay)

**What goes wrong:**
- DNS TTL on childcustodyanddivorce.com is set to 86400 (24h) when cutover starts — a mistake takes a full day to reverse.
- New site's canonical URLs reference the Justia domain (whatever it was) because copy was ported literally.
- Sitemap.xml contains Justia URLs or missing new URLs.
- Justia URLs (e.g., `justia-slug/divorce-in-california`) that Google has indexed for years don't get 301-redirected to the new equivalents on childcustodyanddivorce.com — years of SEO history lost.
- Site goes live but GSC isn't verified until 3 days later — indexing delayed.
- Cutover happens mid-day: any prospect on Justia's old URL sees a dark window if Justia takes their site down at 2026-07-31 midnight and Burkett's DNS hasn't propagated.
- `robots.txt` on the new site accidentally has `Disallow: /` from a staging state.

**Why it happens:**
- Network Solutions DNS UI doesn't warn about TTL implications.
- Content porting is copy-paste and doesn't rewrite absolute-URL references.
- Justia URL mapping requires listing every old URL — tedious.
- GSC verification is a separate manual step in a different UI.
- Staging `robots.txt` gets committed to production.
- Justia shuts down THEIR hosting on 2026-07-31 regardless of Burkett's DNS state.

**Consequences:**
- Dark window = lost prospects and lost trust.
- SEO history destroyed if Justia URLs 404 instead of 301.
- Weeks of indexing delay if GSC verify is late.
- Site blocked from Google if `Disallow: /` ships to prod.

**How to avoid:**
- **T-14 days before 2026-07-31 cutover:** Drop DNS TTL on childcustodyanddivorce.com to 300 seconds (5 min) at Network Solutions. Verify with `dig`.
- **T-7 days:** Build a Justia URL → new URL redirect map. Enumerate every Justia URL currently indexed (scrape from Justia archive plus GSC coverage report if available). For each, define the target (canonical practice page, canonical blog post, or homepage if orphaned).
- **T-5 days:** Deploy site to Netlify with a production-mirror preview domain (`burkett-law-preview.netlify.app`). Full smoke test.
- **T-3 days:** Add Netlify `_redirects` file with 301s for every mapped Justia URL. Test each with `curl -I` against preview domain.
- **T-1 day:** Final smoke: RRT on 5 sample pages, `curl` on 5 mapped redirects, GA4 test event, form test submission, phone tap test on mobile.
- **Cutover day (before Justia shuts):** Point childcustodyanddivorce.com DNS to Netlify. Watch propagation with `dig +short A childcustodyanddivorce.com` from multiple resolvers. Force propagation with `dig @1.1.1.1` + `@8.8.8.8`.
- **Cutover +1h:** Verify HTTPS cert issued by Netlify (Let's Encrypt auto-issue can take up to an hour on a new domain). Test root URL, 5 practice URLs, 5 blog URLs, 3 Justia-redirect URLs, contact form submission.
- **Cutover +2h:** Verify GSC (should be verified via DNS TXT set at T-7). Submit sitemap.xml. Submit URL inspection for top 10 pages.
- **Cutover +24h:** Re-check GSC coverage. Verify no `Disallow: /` in robots.txt. Verify canonicals are absolute + correct.
- **Cutover +72h:** Restore DNS TTL to 3600 or 86400 once confirmed stable.
- Pre-cutover checklist doc lives in `.planning/cutover-checklist.md`.

**Warning signs:**
- `dig` shows TTL still 86400 at T-7.
- Sitemap.xml grep for `justia.com` or old domain returns hits.
- Preview site's `robots.txt` says `Disallow: /`.
- Any canonical tag on the new site references a non-childcustodyanddivorce URL.
- GSC coverage shows 100% "Not indexed" after 7 days.

**Phase to address:**
Phase E (Cutover) — dedicated phase. Redirect map is a Phase C/D deliverable (needs practice + location URLs finalized). GSC domain verification is Phase A (do it at day 1, propagation takes hours, and DNS TXT survives redesigns).

---

### Pitfall 8: Google Ads Takeover — Losing Quality Score, Breaking Conversion Tracking, Ad-Group Kill Rules Wiping Data

**What goes wrong:**
- Burkett's current Google Ads account (managed by Justia/Clientomics/Rankaroo) is disconnected before Echo Local's MCC has access — orphaned account, lost history.
- MCC accepts the invite but the Ads account is paused during transition — quality score drops from campaign inactivity.
- Old conversion actions (from Justia/Clientomics tracking) get deleted, breaking conversion history data.
- New "Calls from Ads" conversion action isn't set up before campaign restart, so ads run with zero conversion attribution (repeat of Echo Local's own 2026-06-23 blind-spot).
- Automated bidding strategies (Target CPA, Maximize Conversions) reset when campaigns are rebuilt — Google's learning starts from zero.
- Kill-switch rules from Echo Local's playbook auto-pause the campaign because Burkett's daily budget is too low ($15–25/day is common for solo family law) and catch-up pacing spikes trigger the $38 threshold.
- Family-law negatives aren't added — money burned on DIY-divorce, self-help, court-forms, "how to file for divorce myself" queries.
- Call tracking uses Burkett's actual cell number instead of a Google forwarding number — attribution guessed, not measured.

**Why it happens:**
- MCC transitions have moving parts (Burkett accepts, Justia releases, MCC invites, all sequential).
- Old conversion actions look outdated so instinct is to delete.
- Kill-switch thresholds were tuned for Echo Local's own $16–20/day budgets and never reviewed per-client.
- Legal-vertical negatives are different from home services — separate list needed.
- Call tracking is a separate configuration in Google Ads.

**Consequences:**
- Quality score reset = higher CPCs (family law CPCs are already $15–50/click in San Diego).
- Attribution blind spot = can't optimize what you can't measure.
- Wasted spend on DIY-intent traffic that will never convert.
- Ad-group kill-switch pausing = missed conversion window.

**How to avoid:**
- **Before touching Ads account:** verify MCC 935-051-0225 has requested access. Do NOT accept until Echo Local can see the account (accept invite triggers whatever the sender configured).
- **Step 1 (access secured):** Do NOTHING for 7 days — observe. Capture baseline: current conversion actions, current negatives, current bidding strategy, last-30-day spend/CPC/CTR/CVR.
- **Step 2 (before edits):** Set up "Calls from Ads" conversion action (AD_CALL, min 30s, primary). Same pattern Echo Local used 2026-06-23 to fix its own tracking blind spot. Use a Google forwarding number, not Burkett's cell.
- **Step 3:** Add California family-law negatives:
  - DIY: `-"do it yourself" -"how to file" -"court forms" -"self help" -"pro se" -"without an attorney" -"without a lawyer" -"free divorce"`
  - Wrong vertical: `-immigration -bankruptcy -criminal -dui -personal injury -estate -real estate`
  - Job seekers: `-job -jobs -salary -career -employment -paralegal school`
  - Directories: `-avvo -justia -yelp -findlaw -lawyers.com`
  - Non-SD geo: negatives for LA, OC, Riverside, unless Burkett wants those.
- **Step 4:** Kill-switch review — Burkett's daily budget is likely $10–30/day. Set kill-switch threshold to 2.5× daily budget (not the $38 Echo Local uses).
- **Step 5:** Bidding — keep whatever's currently working. Do NOT switch to Maximize Conversions with zero conversion history. If moving to Maximize Clicks, set CPC ceiling appropriate to family law ($40–60, not Echo Local's $25).
- **Step 6:** GA4 conversion sync — form_submit, phone_click, calendar_view, calendar_booked events flow to Ads as secondary conversions (primary is call).
- **Step 7:** Cancel Clientomics/Rankaroo/Justia AFTER MCC access + baseline captured, not before.

**Warning signs:**
- MCC invite accepted but Echo Local can't see the account.
- Zero conversions in first 7 days = tracking not firing (do the Echo Local diagnostic).
- CPC spikes 3x baseline = quality score drop.
- Kill-switch pausing daily = budget/threshold mismatch.
- DIY-intent queries in search terms report = missing negatives.

**Phase to address:**
Phase G (Google Ads Takeover) — dedicated phase, sequenced after Phase E (Cutover) so ads point at a live site. NEVER before cutover — ads pointing at a dark or half-live site burn quality score.

---

### Pitfall 9: Google Business Profile Mistakes (Name Stuffing Suspension, Wrong Category, Service Area Mis-Set, Hours Drift, Account Correlation)

**What goes wrong:**
- Business name gets "SEO-optimized" ("Brian Burkett - San Diego Family Law Attorney - Divorce & Custody") — this is a GBP guideline violation and triggers suspension (Georgia's suspended prior listings + Burkett was already advised against this per PROJECT.md context).
- Primary category is wrong (Attorney vs. Family Law Attorney vs. Divorce Lawyer — legal has multiple related categories, wrong primary = missed local pack).
- Service area is set to a huge radius including counties Burkett doesn't serve (or set as SAB when he's a storefront — mirrors Georgia's SAB/storefront misconfiguration).
- Hours drift from what's on the site — Google's cross-check flags inconsistency and drops local trust.
- Manager invite from Burkett's email is accepted from an account that's been correlated with a suspended listing (Georgia's `georgiapeach310@gmail.com` correlation incident — burned personal-email account to a listing).
- Photos on GBP don't match site photos (different attorney appearance in stock vs. real).
- Address on GBP has different spacing / abbreviation than site (Georgia's "PsychicExperience" spacing bug).

**Why it happens:**
- Name-stuffing is genuinely a temptation because it does move rankings — until it triggers suspension.
- Google's category list is long; there's overlap (Attorney, Lawyer, Family Law Attorney, Divorce Lawyer, Legal Services).
- SAB vs. storefront is a checkbox that's easy to mis-set.
- Manager invite acceptance is done from whatever browser session is signed in.
- Cross-account correlation is not documented publicly by Google.

**Consequences:**
- Suspension. Days to weeks of GBP downtime. Reinstatement is manual and not guaranteed.
- Missed local pack rankings for correct category.
- NAP inconsistency = trust penalty.
- Manager email account permanently correlated to whatever mistake happens.

**How to avoid:**
- **Business name:** EXACTLY match the legal business name. "Law Office of Brian Burkett" or "Brian Burkett, Attorney at Law" — nothing else. No keywords, no location, no service. If the current listing has SEO-stuffing (from Justia era), REMOVE it before Echo Local takes over — reinstatement risk lower before takeover.
- **Categories:** Primary = "Family Law Attorney." Secondary categories: "Divorce Lawyer," "Child Custody Attorney." Not "Attorney" (too broad — misses vertical-specific pack).
- **Setup type:** Storefront (Burkett has a physical office at 591 Camino De La Reina Suite 821 that clients visit). Not SAB.
- **Service area (optional for storefront):** Add San Diego County; do NOT add adjacent counties unless Burkett actually practices there.
- **Address:** Character-identical to site footer, contact page, `LocalBusiness` schema, and BrightLocal citations. "591 Camino De La Reina, Suite 821, San Diego, CA 92108" — commit to one exact format. NO spacing bugs (`Suite821` or `Suite 821`).
- **Hours:** Match site. Update site + GBP together, always.
- **Manager invite:** Accept from a fresh Google account (not Burkett's personal Gmail if it has any legal-industry history). Preferred: `burkett@echolocalagency.com` or a clean account.
- **Photos:** Same set on GBP and site — Burkett's real photos from Justia archive. Add exterior photo of Suite 821 if Burkett can supply.
- **GBP name change process:** If a change is needed post-live, Google may require re-verification — schedule during a slow-lead window.

**Warning signs:**
- GBP name has more than the legal business name.
- Primary category is "Attorney" (too broad).
- GBP set to SAB with hidden address (Burkett is storefront).
- Hours on site say "M–F 9am–5pm" but GBP says something else.
- NAP grep across site + GBP + BrightLocal shows any character variance.

**Phase to address:**
Phase F (GBP + Local) — dedicated phase. Manager invite accepted at start of Phase F (from a clean account). Name/category/setup/service-area/hours locked in one edit session. Do NOT stack GBP edits over multiple days — each edit is a review event with Google.

---

### Pitfall 10: Netlify-Specific Traps (pretty_urls, Form Spam, subject_template Substitutions, Auto-Deploy Silent Break)

**What goes wrong:**
- `pretty_urls = true` (default) strips `.html` from internal links while canonicals/sitemap keep `.html` → Google starves canonical pages of internal-link support → "Discovered/Crawled — not indexed" cluster (repeat of SoCal/Ecosystem/Mr Green incident June 2026).
- Form spam floods Burkett's inbox with fake design-audit / link-buying / review-buying spam (repeat of Arcadian June 2026 spam wave).
- `subject_template` in Netlify form notification hook uses `{{ name }}` or `{{ email }}` expecting substitution — Netlify only supports `{site_name}`, `{form_name}`, `{site_url}`. Emails ship with literal `{{ name }}` text (repeat of 12 broken hooks fixed 2026-06-09).
- Netlify-GitHub auto-deploy silently breaks — commits push but no deploys happen (Chef Dorothy went 84 days). New posts don't ship, sitemap doesn't update, Burkett thinks the site is stale.

**Why it happens:**
- Netlify `pretty_urls` default is `true` and the setting is buried in a build-processing menu — most sites never notice the mismatch.
- Bots find Netlify forms fast; a new domain is target-ready within days.
- `subject_template` docs mention `{{` variables in some examples that are actually Netlify's own — user assumes any variable works.
- Auto-deploy break is a webhook / OAuth issue, not surfaced in the Netlify UI without a click into deploy settings.

**Consequences:**
- Deindexing / SEO stall.
- Inbox spam noise burying real leads.
- Broken notification emails (Burkett doesn't know a form was submitted, or notification is unreadable).
- Site goes stale, Google notices dropping refresh cadence.

**How to avoid:**
- **`netlify.toml`** at repo root, day 1:
  ```toml
  [build.processing.html]
  pretty_urls = false
  ```
  This is NON-NEGOTIABLE and enforced by a repo lint (grep in CI).
- **Form spam filter:** Reuse `reference_spam_filter_patterns.md` verbatim — 24 regexes + 5 heuristics, silent redirect to `/` on match. Deployed to 6 sites and holding.
- **Netlify honeypot:** `<input name="bot-field" hidden>` + `data-netlify-honeypot="bot-field"` on form.
- **`subject_template`:** ONLY `{site_name}`, `{form_name}`, `{site_url}`. Nothing else. Preferred: `"[{site_name}] New {form_name} submission"`.
- **Auto-deploy verification:** After initial GitHub → Netlify link, check every 30 days that the last commit on `main` matches the last deploy on Netlify. Add to Phase G ops runbook. Also spot-check on every other Echo Local site while this is fresh.
- **Netlify `_headers`** — set security headers (HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy). Trust signal for YMYL.
- **Netlify `_redirects`** — Justia-URL redirect map goes here (Phase E). Also 301 www → apex or apex → www (pick one canonical host, redirect the other).

**Warning signs:**
- `netlify.toml` missing or missing the `pretty_urls = false` block.
- Homepage's internal links point to `/divorce` instead of `/divorce.html`.
- Form spam volume >5/week.
- Email notification with literal `{{ ... }}` text.
- Last deploy timestamp older than last commit timestamp by >7 days.

**Phase to address:**
Phase A (Foundation) — `netlify.toml`, spam filter, honeypot, `subject_template`, security headers, form-notification test all before any content ships. Phase E (Cutover) — `_redirects` file. Phase G (Post-launch ops) — auto-deploy monthly check.

---

## Moderate Pitfalls

### Pitfall 11: Analytics Traps — Cross-Client GA4 Contamination, Missing GSC Verification, Wrong Property

**What goes wrong:**
- Generic SEO-engine template hardcodes a GA4 ID (Mr Green's `G-PGEDP44QR4`) and Burkett's blog/location pages ship polluting the wrong property (repeat of Arcadian + Top Tier + Ecosystem incident).
- GSC verification is deferred to "post-launch" — days of indexing lost.
- GA4 property is verified but the wrong property (Burkett's data flows into Echo Local agency property).
- Conversion events fire but no event definitions in GA4 → nothing shows in reports.
- `phone_click`, `form_submit`, `calendar_view`, `calendar_booked` events aren't wired.

**Prevention:**
- GA4 ID injected per-site from `clients.json` — NEVER hardcoded in shared templates.
- Identity guard (existing Echo Local system) catches any commit with hardcoded GA IDs.
- Burkett gets a new GA4 property + measurement ID before any content ships.
- GSC domain-property verification via DNS TXT at Phase A (day 1) — takes hours to propagate, do it early.
- Test event fires from local dev → visible in GA4 realtime before cutover.
- Post-cutover, GA4 conversions imported into Google Ads as secondary conversions (primary = call).

**Warning signs:**
- Grep for `G-` in shared templates returns any hit.
- GA4 realtime shows zero events after 24h post-launch.
- GSC coverage stuck at "URL is not on Google."
- Ads conversion column always zero.

**Phase to address:** Phase A (Foundation).

---

### Pitfall 12: Accessibility Gaps (WCAG 2.1 AA for Professional Services)

**What goes wrong:**
- Navy + gold palette fails contrast on gold-on-cream buttons (gold at low weight often fails 4.5:1).
- Calendar embed (GHL iframe) isn't keyboard-navigable — screen-reader users can't book.
- Alt text keyword-stuffed ("san diego divorce attorney best custody lawyer") instead of descriptive.
- Form labels missing for="id" association.
- Focus outlines removed for aesthetics — keyboard users lost.
- Video welcome (Phase B v1.x) lacks captions/transcript.
- No skip-to-content link.
- Semantic HTML skipped in favor of `<div>` soup.

**Why it matters for family law:**
Title III ADA lawsuits target law firm websites (there's a cottage industry of plaintiffs' firms suing law firms specifically). Also a soft ranking signal.

**Prevention:**
- Color contrast check every design decision — gold must be dark enough for 4.5:1 on cream backgrounds. Test with WebAIM Contrast Checker.
- Semantic HTML: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`. One `<h1>` per page.
- All images have descriptive alt text (see YMYL — "Brian Burkett, San Diego family law attorney" is fine; keyword-stuffed alt is not).
- Every form input has `<label for="id">`.
- Focus outlines preserved (or replaced with a designed alternative that's just as visible).
- Skip-to-content link as first tab-stop in `<body>`.
- GHL calendar embed tested with keyboard nav; if fails, provide phone/email fallback prominently.
- Video captions + transcript when video ships (Phase B v1.x).
- Run Lighthouse accessibility audit before commit — target 95+.
- axe DevTools scan on every unique page template.

**Phase to address:** Phase A (Design system foundation) — colors + semantic patterns locked. Phase F (QA) — audit before cutover.

---

### Pitfall 13: Privacy Compliance (CCPA/CPRA for California Businesses)

**What goes wrong:**
- No privacy policy, or a boilerplate policy that doesn't reflect actual data collection.
- CCPA "Do Not Sell / Share My Personal Information" link missing (arguably not required for a law firm not "selling" data, but California AG has been aggressive).
- CPRA-required disclosures missing (categories of PI collected, retention, third parties).
- Contact form collects PII (name, email, phone, case type, message) without explicit consent language.
- GA4 basic mode is fine for US-only, but if any EU visitor lands, GDPR technically applies (low practical risk but non-zero).

**Prevention:**
- Privacy policy specific to Burkett's data collection: form submissions, GA4 analytics, GHL CRM, phone call metadata. Link from footer sitewide.
- Terms of use / Terms of service similarly linked.
- Contact form disclosure above submit: "By submitting this form, you consent to the Law Office of Brian Burkett collecting the information you provide for the purpose of responding to your inquiry. See our Privacy Policy for details."
- Attorney-client relationship disclaimer on form (see Pitfall 3).
- CCPA "Your Privacy Choices" or similar link in footer (California AG guidance).
- No GA consent banner needed for US-only + GA4 basic mode.
- If Burkett ever wants EU visitors served (very unlikely for SD family law), add consent mode v2.

**Phase to address:** Phase A (legal pages template) — Privacy Policy + Terms drafted, link in footer.

---

### Pitfall 14: Design / Tone Traps (Ambulance-Chaser Vibes, Fake Stock Testimonials, Fake Courtroom Sets, Corporate Coldness)

**What goes wrong:**
- Copy defaults to aggressive "fight for you" / "get what you deserve" / "we'll destroy the other side" (repels family-law prospects who often still love their ex).
- Homepage hero is a gavel + scales + blurred courthouse stock photo (screams template mill, kills warm-approachable brief).
- Stock photos of diverse attorneys standing in a fake conference room (not Burkett — kills trust).
- Testimonials are stock or generic ("Best lawyer ever!" — no name, no context).
- Cold navy/white classical corporate design competes with 100 other SD family-law sites.
- Actual Burkett photos exist in Justia archive but get demoted for "cleaner" stock.

**Prevention:**
- Design brief locked (PROJECT.md): navy + warm cream + gold, Burkett's real photos front and center, compassionate tone.
- Copy voice guide: "Steady," "compassionate," "in your corner," "clear-eyed guidance," "we're here to help you make hard decisions." NOT "aggressive," "fight," "win," "destroy."
- Zero gavels, zero scales of justice, zero blurred courthouses. If a courthouse image is needed, use a real SD courthouse photo Burkett has rights to.
- Zero stock people photos. Every human image is Burkett or a designed illustration, not a stock attorney model.
- Testimonials only if real (Justia archive), with disclosure (see Pitfall 3), with client's first name or "K.M., San Diego" only for privacy.
- If Burkett has any photos with clients, they're NOT used (attorney-client relationship privacy).

**Warning signs:**
- Hero image is stock.
- Any headline uses "fight" / "aggressive" / "win" / "battle."
- Any human photo isn't Burkett.
- Testimonials without names or with obviously generic praise.

**Phase to address:** Phase A (Design system) — palette + typography + imagery rules locked. Phase B (Content) — copy voice guide referenced on every content asset.

---

## Minor Pitfalls

### Pitfall 15: Missing OG / Twitter Card Metadata

Social shares (someone messaging "check out my attorney" to a friend) render blank cards. Cheap fix: OG title, description, image, url on every page. Twitter card `summary_large_image`.

**Phase:** Phase A template head snippet.

---

### Pitfall 16: 404 Page That Doesn't Convert

Default Netlify 404 kills conversion for anyone hitting a broken URL (during Justia cutover, likely). Custom 404 with phone + calendar + link to practice areas.

**Phase:** Phase A design system.

---

### Pitfall 17: No Structured Error Handling on Form Submit

Form submit fails silently → prospect thinks it worked → nobody follows up → lead lost. Show explicit success state (`/thanks.html` redirect) and explicit failure state with fallback phone number.

**Phase:** Phase A form pattern.

---

### Pitfall 18: Blog Publish Date Drift

Publishing all 15–20 curated posts on the same date screams "batch import." Google notices batch publishes on YMYL. Backdate to reasonable original dates (from Justia archive) and add `dateModified` = today.

**Phase:** Phase B content — set dates from Justia archive lastmod when available.

---

### Pitfall 19: llms.txt Generic or Missing

Legal is a prime GEO vertical (prospects ask ChatGPT/Perplexity "family law attorney san diego"). A curated `llms.txt` with key pages + a Q&A curated for LLM consumption is high-value cheap.

**Phase:** Phase F (Technical SEO polish).

---

### Pitfall 20: Preserving Justia URL Slugs Where Possible

Some Justia URLs have organic traffic history. If a Justia slug is reasonable for the new site, keep it. Don't rename purely for taste.

**Phase:** Phase B/E content + cutover — URL mapping decision.

---

## Technical Debt Patterns

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Copy-paste practice-page template with one paragraph swapped for another practice | Ships 8 pages in a day | YMYL demotion, duplicate-content flag, low-quality footprint | Never — write each practice page with real jurisdictional depth |
| Fill FAQ blocks with generic industry questions | Feeds FAQ schema | If a real prospect asks and gets a Google-scraped answer that doesn't match Burkett's actual practice, trust damage. If schema is present but content is generic, thin-content flag. | Never — real questions only; drop the FAQ block rather than fabricate |
| Skip `LegalArticle` schema, use `Article` | Faster template | Weaker YMYL signal; missed AI citation | Never — cost is a schema string swap |
| Skip Rich Results Test on every schema block | Time saved | Silent schema errors mean schema is present but ignored | Never on v1; can batch on v1.x additions |
| Use Google Fonts CDN instead of self-hosting | 5 minutes saved | Third-party RTT hurts LCP; cookie/GDPR concerns for YMYL trust | Never for this build |
| Skip privacy policy on v1 | Faster to ship | CCPA exposure; trust signal missing | Never — cheap template exists |
| Location pages templated with placeholder swaps | 20 pages in an afternoon | Deindex risk, YMYL thin-content flag | Never for YMYL; acceptable in low-stakes verticals |
| Publish all 15–20 blog posts today with today's date | Simple import | "Batch import" signal to Google, hurts freshness reads | Never — backdate to Justia archive dates + set dateModified = today |
| Wait to verify auto-deploy until "something breaks" | Zero setup effort | Silent 84-day deploy gap (Chef Dorothy pattern) | Never — verify at Phase A + Phase G monthly check |

---

## Integration Gotchas

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| GHL calendar embed | Reusing Echo Local's shared calendar `PW5Ma7sjF3S6AWayZDuK` for Burkett | Create Burkett's own calendar; separate URL. Also `/thanks-booked.html` for conversion firing. |
| GHL webhook to CRM | Firing on every form submit but no field mapping — GHL contact has no info | Map form fields to GHL custom fields explicitly; test with a real submission |
| GA4 → Google Ads conversion import | Assumed automatic — it isn't; conversions must be imported as secondary conversion actions in Ads | Manually import GA4 events as Ads conversions; keep call conversion as primary |
| Netlify Forms honeypot | `<input name="bot-field">` without `data-netlify-honeypot="bot-field"` on `<form>` | Both required. Also `netlify` attribute on form. |
| Netlify Form notification email | Using `subject_template` with `{{ name }}` expecting field substitution | Only `{site_name}`, `{form_name}`, `{site_url}` supported |
| Google Business Profile manager invite | Accepted from Burkett's personal Gmail that has correlation to Justia listings | Accept from clean account (recommend `burkett@echolocalagency.com` or fresh account) |
| GBP business info API | PATCH to name field with SEO stuffing | Match legal business name exactly; API accepts but review flags |
| DNS at Network Solutions | TTL left at 86400 during cutover | Drop to 300 at T-14, restore at cutover +72h |
| Netlify `_redirects` | Wildcard redirect that catches new URLs (`/* /home 301`) | Explicit path-level redirects only for Justia URLs |
| BrightLocal citation upload | Address format drift between site and BrightLocal CSV | Character-identical NAP everywhere; single canonical format |
| Google Rich Results Test | Not run — schema silently invalid | Run on every unique page template before cutover |
| Google Search Console | Verified via HTML file that gets removed during redesign | Verify via DNS TXT — survives redesigns |
| Cloudflare (if in front of Netlify) | Cloudflare cache serves stale HTML after deploy | Purge Cloudflare cache on deploy OR use Netlify direct (no Cloudflare) |
| Stripe (if payments added later) | Wired to marketing site — mixes payment surface with content | Separate subdomain or portal (out of scope v1) |

---

## Performance Traps

Static site is inherently fast, but static ≠ automatic Core Web Vitals pass on mobile.

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| GHL calendar iframe rendered above the fold, eager-loaded | INP > 300ms on homepage mobile | `loading="lazy"` on iframe + intersection-observer mount | Immediately at launch on any 4G / mid-tier Android |
| LCP image not preloaded | LCP > 3s on mobile | `<link rel="preload" as="image" imagesrcset imagesizes>` on hero image per page | Homepage + every practice page |
| Google Fonts CDN with 3+ weights | LCP > 2.5s | Self-host WOFF2, variable font, only preload the 1-2 weights above-the-fold | Any weight beyond 2 |
| Every image is JPEG at 100% quality | Total page weight > 3MB | AVIF with WebP+JPEG fallback via `<picture>`, 3-width `srcset` | Once total imagery > 500KB per page |
| Missing `width`/`height` on images | CLS > 0.1 | Explicit width/height on every `<img>` and reserve iframe space with min-height wrapper | Any image without dimensions |
| Inline all CSS in one file, no critical CSS split | FCP > 2s | Inline critical CSS in `<head>`, defer rest OR ship one small file if under ~15KB | Total CSS > 30KB |
| Analytics + GTM + other scripts in `<head>` blocking | INP > 200ms | GA4 as `<script async>` at end of body; NO GTM | Any GTM install |
| Video welcome autoplaying with sound | INP + LCP hit, autoplay blocked | Autoplay muted + `preload="metadata"` (not `auto`) + lazy-load if below fold | v1.x video ships |

---

## Security Mistakes (Domain-Specific)

Static HTML has minimal attack surface, but YMYL has trust-signal expectations.

| Mistake | Risk | Prevention |
|---------|------|------------|
| No HSTS header | MITM trust concerns on legal-site prospect | `Strict-Transport-Security: max-age=31536000; includeSubDomains` in `_headers` |
| No CSP | XSS if any inline JS gets injected (unlikely on static, but signal-value) | Reasonable CSP: `default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com` (adjust for GA4) |
| `X-Content-Type-Options: nosniff` missing | Signal | Add in `_headers` |
| `Referrer-Policy` missing | Signal + privacy | `strict-origin-when-cross-origin` |
| `Permissions-Policy` missing | Signal | `interest-cohort=()` at minimum |
| Contact form transmits PII over HTTP | If HTTPS misconfigured post-cutover, PII leak | HTTPS enforced via Netlify (default) + HSTS |
| Form data logged to third-party analytics | Confidential inquiry leaked to Google | Do NOT capture form field VALUES in GA4 events — only the fact of submission (`form_submit` event, no parameters with user text) |
| Manager invite accepted from a compromised/reused account | Account correlation to bad listings (Georgia incident) | Fresh clean account for GBP + GA4 + GSC ownership |
| No `security.txt` | Minor trust signal | `/.well-known/security.txt` with contact email |

---

## UX Pitfalls

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Only a form CTA on the homepage | Crisis-callers bounce (they want to call, not type) | Equal-weight trio: phone + calendar + form (PROJECT.md locked) |
| Dense legal jargon (petitioner, respondent, ex parte, RFO, DVRO) on landing pages | Prospects bounce, LLM citation weaker | Plain language with jargon in parentheses |
| Cluttered mega-menu navigation | Stressed prospects can't decide where to click | Simple top nav: Practice Areas / About / Blog / Contact + phone |
| No response-time expectation set | Prospect anxiety spikes; may fill form for another attorney too | "I respond within 1 business day" statement on form |
| Contact form with 12+ fields | Abandonment | 4-5 field short form (name, email, phone, matter type, message) |
| Aggressive tone ("Fight back!", "Get what you deserve!") | Family-law prospect ambivalence + repels | Compassionate: "Steady representation when you need it most" |
| No visible attorney bar admission | Trust signal missing | "Admitted to California State Bar [year], Bar No. [XXXXX]" on bio + footer |
| No parking info at Mission Valley office | Prospect struggles to find office | Parking notes on contact page + Google Map |
| Broken tel: link (formatted with parens/spaces the phone dialer can't parse) | Call button doesn't call | `tel:+16192502683` — E.164 format, no spaces or parens |
| Chat widget on YMYL | Bot answering legal Qs = malpractice-adjacent | No chat. Calendar + phone + form. |
| No exit-facing SEO-history preservation from Justia | Prospects who bookmarked Justia URLs get 404 | 301 redirects for all mapped Justia URLs |

---

## "Looks Done But Isn't" Checklist

Things that appear complete but are missing critical pieces. Verify each at Phase F QA.

- [ ] **Attorney bio:** Often missing bar admission year + bar number — verify visible on-page + in schema `hasCredential`
- [ ] **Practice pages:** Often missing FAQPage schema even though FAQ block is present — verify JSON-LD renders per page via view-source
- [ ] **Blog posts:** Often marked as `Article` instead of `LegalArticle` — grep JSON-LD for `LegalArticle`
- [ ] **Author schema:** Often missing `sameAs` links to State Bar / LinkedIn — verify `sameAs` array is populated
- [ ] **Location pages:** Often thin (<600 words) or duplicate — run word-count + similarity lint
- [ ] **Schema on every page:** Often missing on legal pages (Privacy/Terms) — verify BreadcrumbList + Organization on every page including legal
- [ ] **Sitewide footer disclaimers:** Often present on home but missing on some inner pages — grep every HTML file for disclaimer text
- [ ] **`netlify.toml pretty_urls=false`:** Often forgotten on new sites — grep for the exact string
- [ ] **GA4 events:** Often fire in dev but not prod — verify GA4 realtime shows events after cutover
- [ ] **GSC verification:** Often deferred to post-launch — verify DNS TXT at Phase A
- [ ] **Justia redirects:** Often incomplete map — `curl -I` every mapped Justia URL against preview + prod
- [ ] **Rich Results Test:** Often skipped — run on 1 representative page per template
- [ ] **Contact form end-to-end:** Often "the form loads" tested but not "the notification email arrives" — submit a real test entry, verify email lands
- [ ] **Phone link:** Often formatted as display text instead of `tel:` — test tap on mobile
- [ ] **Calendar embed:** Often present but iframe blocked by ad-blockers or 3rd-party cookie policy — test in incognito + Safari (default ITP)
- [ ] **Robots.txt:** Often has `Disallow: /` from staging — verify prod says allow
- [ ] **Sitemap:** Often lists dev URLs or has trailing-slash inconsistencies — verify every URL 200s
- [ ] **HTTPS + HSTS:** Often HTTPS works but HSTS header not set — `curl -I` for `Strict-Transport-Security`
- [ ] **Auto-deploy:** Often "works today" but breaks silently later — verify last commit === last deploy at Phase G + monthly
- [ ] **GBP NAP:** Often character-drift from site — grep for exact string across site + GBP + BrightLocal CSV
- [ ] **Cal Bar disclaimers:** Often on some pages but not all — required sitewide

---

## Recovery Strategies

When pitfalls occur despite prevention, how to recover.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Content fabrication shipped | MEDIUM (per Mr Green scrub: touched 39 posts, re-render + deploy day of work) | Grep all published content for the fabricated claim; scrub in one commit; force-reindex via GSC URL Inspection; document in `.planning/incidents.md` |
| E-E-A-T signals missing post-launch | LOW | Add byline + schema + credentials sitewide via template update; single commit re-renders all pages |
| Cal Bar Rule 7.1 violation caught by bar | HIGH | Scrub violating content immediately (same day); consult defense counsel; document scrub for bar file. Prevention > recovery here. |
| Thin location pages deindexed | MEDIUM | Expand each page to substantive city-specific content; re-request indexing in GSC; if pages are terminal cases, add redirect to nearest practice page + drop from sitemap |
| Duplicate content collapse | LOW-MEDIUM | Rewrite duplicated sections for variance; update canonicals; re-request indexing |
| Wrong schema shipped | LOW | Fix template; commit; re-render; Google re-crawls in days |
| DNS cutover misconfigured | HIGH if TTL not dropped (24h to fix) / LOW if TTL was 300 | Revert DNS to old target if Justia is still live; if not, sprint to fix Netlify; if Netlify site is broken, deploy a static holding page |
| Justia URL 301s missing | MEDIUM | Enumerate missing redirects from GSC 404 report; add to `_redirects`; deploy; hope some traffic returns (some SEO history is lost permanently) |
| GSC verification delayed | LOW | DNS TXT survives; verify as soon as noticed; indexing catches up in days |
| GA4 pollution / wrong property | LOW-MEDIUM (per Ecosystem incident: single commit fix + GSC re-verify) | Fix template; commit; verify GA4 realtime; re-verify GSC if it was tied to the tag |
| Netlify pretty_urls deindex | MEDIUM (per SoCal incident: single commit fix but weeks of index recovery) | Add `pretty_urls = false` to `netlify.toml`; commit; deploy; GSC URL Inspection on top pages; wait |
| Netlify auto-deploy silent break | LOW | Re-link GitHub → Netlify in dashboard; force a manual deploy; verify next commit deploys automatically |
| GBP suspension from name stuffing | HIGH (Georgia's account correlation: weeks to reinstate + risk of permanent block) | Submit reinstatement request with legal business name; wait; if permanent, create new listing under fresh account (Georgia's playbook) |
| Google Ads quality score reset | HIGH (weeks-to-months of higher CPCs) | Rebuild campaigns with tight kw + negatives + conversion tracking; let Google's learning cycle rebuild over 4-8 weeks |
| Form spam wave | LOW | Deploy Echo Local spam filter; add specific regexes for observed patterns; re-test |
| Cross-client GA4 pollution discovered | LOW | Grep templates for hardcoded GA IDs; fix per-client injection; deploy; Echo Local identity guard prevents recurrence |

---

## Pitfall-to-Phase Mapping

How roadmap phases should address these pitfalls. Phase labels are illustrative — roadmap agent will finalize names/numbers.

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| 1. Content fabrication | Phase A (validator built), Phase B/C/D (validator gates every generation) | Grep for fabricated claim patterns returns zero across all published HTML |
| 2. E-E-A-T weak signals | Phase B (bio ships day 1), Phase B/C/D (byline + schema in every content asset) | Rich Results Test shows `Person` with `hasCredential`; grep for byline on every article HTML |
| 3. Cal Bar Rule 7.1–7.5 | Phase A (copy lint rules), Phase B/C/D (lint gates every commit), Phase F (human read) | Copy lint clean; disclaimers grep across every HTML file |
| 4. Thin location pages | Phase D (required-elements checklist + word-count lint) | Word count >600 per page; similarity lint clean; city-specific FAQ present |
| 5. Duplicate content | Phase C, D (variation template), Phase F (similarity report) | Cross-page similarity <50% (excl. boilerplate) |
| 6. Wrong schema | Phase A (schema snippets locked), Phase F (Rich Results Test per template) | Rich Results Test passes; exactly one `LocalBusiness` grep sitewide |
| 7. Cutover mistakes | Phase E (dedicated cutover) with checklist doc, GSC verify in Phase A | Cutover checklist all checked; no dark window; Justia redirects `curl` clean |
| 8. Google Ads takeover | Phase G (post-launch, dedicated) with observation window + conversion setup first | First 7 days observation → conversion action live → then edits |
| 9. GBP mistakes | Phase F (GBP + Local dedicated), clean account for manager invite | GBP name = legal name; primary category = Family Law Attorney; NAP character-identical |
| 10. Netlify traps | Phase A (`netlify.toml`, spam filter, `subject_template`, headers), Phase E (`_redirects`), Phase G (monthly auto-deploy check) | `pretty_urls = false` grep, form test submission, deploy timestamp check |
| 11. Analytics traps | Phase A (per-client GA4 injection, GSC DNS TXT, identity guard active) | Grep for hardcoded GA IDs clean; GA4 realtime shows events; GSC verified |
| 12. Accessibility gaps | Phase A (design system) + Phase F (Lighthouse + axe audit) | Lighthouse a11y >95; contrast checker on palette; keyboard nav on calendar |
| 13. Privacy compliance | Phase A (Privacy + Terms drafted) | Footer links present; form disclosure present |
| 14. Design/tone traps | Phase A (design system + voice guide), Phase B/C/D (voice referenced) | No gavel/scale imagery; no stock people; copy lint for aggressive tone |
| 15. OG/Twitter card metadata | Phase A template head snippet | View-source shows OG tags on every page |
| 16. 404 conversion | Phase A design system | 404 page has phone + calendar + practice links |
| 17. Form error handling | Phase A form pattern | Test failure case with dev-tools; success state visible |
| 18. Blog date drift | Phase B (dates set from Justia archive) | View-source shows varied `datePublished` values |
| 19. llms.txt curated | Phase F (Technical SEO polish) | `curl /llms.txt` returns curated markdown, not boilerplate |
| 20. Justia URL slug preservation | Phase B/E (URL mapping decision) | URL mapping doc reviewed with Burkett; canonical slugs where possible |

---

## Phase-Specific Warnings

Compressed matrix for the roadmap agent — which phases are high-risk for which pitfall types.

| Phase Topic | Likely Pitfalls | Mitigation |
|-------------|-----------------|------------|
| Foundation / Design system | 3, 10, 11, 12, 13, 14, 15, 16, 17 | Copy lint rules + disclaimers + `netlify.toml` + GA4 injection + accessibility bake + Privacy/Terms drafted + design voice guide all done in Phase A |
| Bio + Practice pages | 1, 2, 3, 6, 18 | Bio first, fabrication validator gates, schema template applied, byline + dates + jurisdiction |
| Blog curation | 1, 2, 3, 6, 18 | Curate 15–20 from 40 Justia, each fabrication-validated, LegalArticle schema, real bylines |
| Location pages | 1, 4, 5, 6 | Required-elements checklist, word-count lint, similarity lint, Service schema (no LocalBusiness on satellites) |
| Cutover | 7, 10, 11 | Dedicated cutover checklist doc, DNS TTL drop at T-14, Justia redirect map, GSC verified beforehand |
| GBP + Local | 9 | Clean account, legal business name, correct category, NAP consistency |
| Google Ads Takeover | 8 | Observation window before edits, conversion tracking first, family-law negatives |
| Post-launch ops | 10, 11 | Monthly auto-deploy check, GA4 sanity, GSC coverage watch |
| Schema QA (can be its own phase or fold into Foundation/Cutover) | 6 | Rich Results Test per template; exactly one LocalBusiness sitewide |

---

## Sources

- **PROJECT.md** — `/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md` — constraints + Echo Local cross-client learnings + locked decisions (HIGH — authoritative for this project)
- **STACK.md** — `.planning/research/STACK.md` — technical baseline this file layers on (HIGH — companion doc)
- **FEATURES.md** — `.planning/research/FEATURES.md` — feature landscape referenced for anti-patterns (HIGH — companion doc)
- **MEMORY.md active context** — Echo Local incident history: Netlify pretty_urls deindex (2026-06-16 SoCal, cross-client to Mr Green + Ecosystem), Ecosystem GA pollution / cross-client GA4 contamination (2026-06-16), Mr Green content fabrication + identity guard (2026-06-23), Netlify subject_template limitation on 12 hooks (2026-06-09), Chef Dorothy 84-day silent auto-deploy break (2026-06-09), Georgia GBP account correlation suspension (2026-06-15), Arcadian spam wave + filter deployment (2026-06-09) (HIGH — battle-tested)
- **California Rules of Professional Conduct 7.1, 7.2, 7.3, 7.4, 7.5** — https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Rules/Rules-of-Professional-Conduct — attorney advertising rules (HIGH — canonical legal source, controlling authority)
- **Google Search Central — E-E-A-T + YMYL guidance** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content (HIGH — official; Dec 2025 update extended E-E-A-T scrutiny to all competitive queries)
- **Google Search Quality Rater Guidelines (2024)** — specifically YMYL / legal sections (HIGH — Google's own rater training doc; publicly available)
- **Google Search Central — Structured Data (LegalService, LegalArticle, FAQPage, Person, LocalBusiness, BreadcrumbList)** — https://developers.google.com/search/docs/appearance/structured-data (HIGH — official)
- **Google Business Profile guidelines — Business name representation** — https://support.google.com/business/answer/3038177 (HIGH — explicit name-stuffing prohibition + suspension policy)
- **Netlify docs — Forms + `pretty_urls` + `_redirects` + `_headers`** — https://docs.netlify.com/ (HIGH — official)
- **web.dev — Core Web Vitals (INP ≤ 200ms Good threshold since March 2024)** — https://web.dev/articles/inp (HIGH — official)
- **California Consumer Privacy Act (CCPA) / CPRA guidance** — https://oag.ca.gov/privacy/ccpa (HIGH — canonical)
- **ADA Title III trends re: law firm websites** — WCAG 2.1 AA as effective compliance benchmark (MEDIUM — case law is trending; safer to comply)
- **Echo Local reference docs** — `reference_spam_filter_patterns.md`, `reference_netlify_pretty_urls_deindex.md`, `reference_identity_guard_system.md`, `reference_netlify_form_subject_template.md`, `reference_gbp_account_correlation_suspension.md`, `reference_ads_call_tracking_fix.md` (HIGH — internal, incident-derived, battle-tested)

---
*Pitfalls research for: Solo family-law attorney SEO website — YMYL, San Diego, California State Bar jurisdiction, Justia cutover*
*Researched: 2026-07-03*
