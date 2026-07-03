# Feature Research

**Domain:** Solo family law attorney website (San Diego, YMYL / California State Bar advertising rules)
**Researched:** 2026-07-02
**Confidence:** HIGH (patterns are well-established in the vertical; verified against 2026 ABA, PaperStreet, Rankings.io, YMM Digital, Attorney at Law Magazine sources)

Scope note: This file focuses on WHAT features a family-law site includes, WHAT converts stressed prospects, and WHAT to deliberately avoid. Stack-level decisions (framework, hosting, forms library) are handled in STACK.md and are not repeated here.

---

## Feature Landscape

### Table Stakes (Missing These = Prospect Bounces or Google Downranks)

Family-law prospects are stressed, in crisis, and comparison-shopping 3-5 attorneys in one session. They bounce fast if a site fails a credibility sniff test. Google also downranks YMYL legal sites that miss E-E-A-T signals.

| Feature | Why Expected | Complexity | Family-Law-Specific Notes |
|---------|--------------|------------|---------------------------|
| Attorney bio with verifiable credentials (bar admission number, law school, year admitted, practice history, real headshot) | E-E-A-T is the single strongest ranking + trust signal in YMYL legal. Also California Rule of Professional Conduct 7.1 requires accurate credentialing. | LOW | Must trace to Justia archive or Burkett direct. Include CA State Bar number (searchable). Photo is Burkett's real face, not stock. |
| Practice area pages (one per vertical: divorce, child custody, child support, spousal support, mediation, domestic violence, guardianship, family court) | Every prospect Googles the specific issue, not "family law." Practice pages are the primary landing surface from organic + ads. | MEDIUM | 8 verticals per PROJECT.md. Each page needs: what the service is, CA-specific process, what to expect, FAQ block, CTA. 800-1500 words minimum for YMYL. |
| Phone number in header (sticky on mobile) with `tel:` link | Family-law prospects in crisis call, they don't fill forms. Header phone = #1 conversion lever in the vertical. | LOW | `tel:6192502683` from PROJECT.md. Sticky mobile header. Also in footer, on every practice page, above fold on home. |
| Contact form with clear response-time expectation | Some prospects (custody-fear, DV) won't call — they need a quiet channel. Netlify form pattern already exists in Echo Local infra. | LOW | Reuse `reference_spam_filter_patterns.md`. Notifications to Burkett + brian@echolocalagency.com. Set response-time expectation ("I respond within 1 business day") to reduce bounce anxiety. |
| Consultation booking (calendar embed) | The industry standard is a free or flat-fee initial consult. GHL calendar embed pattern already deployed on other Echo Local sites. | LOW | Burkett gets his own GHL calendar (separate from `PW5Ma7sjF3S6AWayZDuK` echolocal calendar). 15-30 min intake slot. Pair with `/thanks-booked.html` for conversion firing. |
| Real photos of attorney + office | Stock photos on a lawyer site are an instant credibility killer in family law (feels like a mill). Warm-approachable design brief locked. | LOW | Headshots + 3 imagery already in Justia archive per PROJECT.md. May need office exterior photo of 591 Camino De La Reina Suite 821. |
| Attorney/LegalService + Person schema (JSON-LD) | Google's YMYL ranking + rich-result eligibility require it. Non-negotiable per PROJECT.md. | MEDIUM | Home = LegalService + LocalBusiness. Bio = Person/Attorney. Practice pages = Service + FAQPage. Contact = LocalBusiness. Reuse Echo Local schema patterns; extend for Attorney type. |
| Office address + hours + parking notes + Google Map | Prospect verifying you're a real local practice. Also a Google Business Profile echo. | LOW | 591 Camino De La Reina Suite 821, Mission Valley. Include parking (attorney offices often have hidden parking situations that create abandonment). |
| FAQ blocks on practice pages | Family-law queries are anxiety-driven questions ("how long does divorce take in CA," "will I lose custody if..."). FAQ answers = high AI-search citation surface + FAQPage schema eligibility. | MEDIUM | Curate 5-8 real questions per practice page from Justia archive. Every FAQ answer must be jurisdiction-specific (CA / San Diego Superior Court). |
| Location context (San Diego pages) — practice × city matrix | High-intent queries follow "[practice] attorney in [city]" pattern. 15-20 combinations locked in PROJECT.md. | MEDIUM | Top 3-4 practice × top 5-6 SD cities. Each page must NOT be thin (>600 words, city-specific court info, real content — not a template mad-lib). Cross-client learning: thin location pages trigger deindex. |
| Ethical disclaimers | CA Rule 7.1 (no misleading), Rule 7.3 (no direct solicitation implication). Missing disclaimers = bar complaint risk + Google trust hit. | LOW | Standard blocks: "The information on this website is not legal advice," "No attorney-client relationship formed by using this site," "Prior results do not guarantee similar outcomes." Footer + contact page. |
| Blog with real author attribution + dates | E-E-A-T author bylines are now table stakes post-Dec 2025 Google update. Also the primary organic-search moat. | MEDIUM | 15-20 curated posts from 40 Justia originals (PROJECT.md). Every post: Burkett byline linking to bio, publish date, updated date if edited, jurisdiction tag (CA), Article schema. |
| Mobile responsive + <3s load on 4G | 70%+ of family-law traffic is mobile. Slow = bounce, and Core Web Vitals hit YMYL sites hardest. | LOW | Static HTML/CSS/JS per Echo Local pattern is already fast. Image optimization + no bloat framework. |
| Accessibility (WCAG 2.1 AA) | Increasingly a legal target itself (Title III ADA suits against law firms). Also a soft ranking signal. | MEDIUM | Semantic HTML, alt text on all imagery, keyboard-navigable calendar embed, sufficient contrast on navy/cream/gold palette (verify gold hits 4.5:1). |
| Privacy policy + terms | Required for forms collecting PII in CA (CCPA implications for law firms). | LOW | Boilerplate template adapted for a solo CA law firm. Link from footer. |
| Footer with bar admission + jurisdiction + office address + phone + hours | Standard legal-industry footer establishes credibility and legal-compliance minimums. | LOW | Include "Licensed in California only." Prevents unauthorized-practice-of-law implications. |

**Bounce test:** A prospect landing on the site should be able to answer within 5 seconds: (1) Is this a real attorney? (2) Do they handle my specific problem? (3) Are they in San Diego? (4) How do I contact them? If any of those aren't obvious, the site fails.

---

### Differentiators (Family-Law Competitive Edge in San Diego)

San Diego family law is a saturated market (hundreds of solo + boutique firms + Justia mill sites). Every table-stakes item above is table-stakes because most competitors have them. Differentiators are where Burkett out-converts.

| Feature | Value Proposition | Complexity | Family-Law-Specific Notes |
|---------|-------------------|------------|---------------------------|
| Homepage CTA trio — phone + calendar + form, equal weight above fold | Family-law leads split 3 ways by channel preference (crisis-callers, quiet-bookers, form-fillers). Equal surface avoids missing any. Locked in PROJECT.md. | LOW | Rare — most law firm sites bury the calendar and lead with a form. Equal-weight trio is a real edge. |
| Warm-approachable design (navy + cream + gold, real photos, human tone) | Differentiates from the sea of navy-and-white "authoritative classical" law-firm-template sites. Family-law prospects want to feel understood, not intimidated. Locked in PROJECT.md. | LOW | Copy-tone matters as much as visual. "Going through a divorce is hard" > "Aggressive representation." |
| Attorney-authored blog covering CA-specific procedure (San Diego Superior Court forms, filing timelines, local judge tendencies as generalizations only) | High-intent, low-competition organic capture. Also THE moat for AI Overviews / ChatGPT citations — passage-level answers to specific CA procedure questions. | HIGH | Content depth is the work. Requires Burkett input on any post that makes procedural claims. Ties into GEO / AI search strategy. |
| Downloadable resources (custody exchange checklist, divorce filing checklist, financial disclosure prep guide) gated by email opt-in | Family-law prospects are researching for weeks before hiring. A useful checklist = they save the site, come back, convert later. Also generates a nurture list. | MEDIUM | 3-5 PDFs, professionally designed. Delivered via Netlify form → Zapier/GHL. Ties into email-nurture that isn't in v1 scope. Defer to v1.x once forms live. |
| Intake pre-qualifier questions on contact form (matter type dropdown, urgency, opposing counsel yes/no, county of filing) | Qualifies leads before Burkett calls back. Prevents wasted intake calls on out-of-jurisdiction or non-family-law queries. Improves close rate. | LOW | 4-5 conditional fields on the standard contact form. Field values feed into GHL contact + Burkett gets a triaged summary in the notification email. |
| Consult fee transparency ("$X initial consultation" or "Free 15-min case review") | Family-law prospect price-anxiety is enormous. Transparent fee = trust and self-qualification. Opaque = bounce. | LOW | Requires Burkett decision on fee model. Once decided, put it on home + contact + every practice page CTA block. |
| Video welcome from Burkett (60-90 sec, on home) | Video introduction is the closest a website gets to walking into an office. Family-law prospects hire on trust, and 90 seconds of Burkett talking = 10x the trust of static copy. | MEDIUM | Requires filming (phone-quality is fine if authentic). Auto-play muted, captions, transcript for SEO. Also usable on GBP + LinkedIn. |
| Practice-area-level "What to expect" timelines (visual step-by-step of a CA divorce or custody case) | Reduces anxiety and demonstrates expertise. Also a top AI-citation surface because it answers "how does divorce work in California" in a structured way. | MEDIUM | 5-7 step visual per practice area, ~300 words per step. Reuses copy that's already in Justia posts. |
| Attorney in-media / speaking / bar-association badges | Third-party validation signals for E-E-A-T. Cheap trust wins. | LOW | Only include real ones (CA State Bar, San Diego County Bar Assoc, any CLE speaking, Super Lawyers if Burkett is listed). No fake badges. |
| GBP-embedded reviews or curated real testimonials with disclosure | Social proof at the exact conversion moment. Legal ethics allow testimonials in CA with disclosure ("Testimonials do not constitute a guarantee of similar outcomes"). | LOW | Pull from Justia archive reviews. Include disclosure per CA Rule 7.1. NEVER fabricate. Better to show 3 real than 15 fake. |
| llms.txt + AI-crawler-friendly content structure | Family-law queries are increasingly answered by ChatGPT web / Perplexity / Google AI Overviews. Being cited there = downstream lead source. | LOW | Include llms.txt per PROJECT.md. Passage-level FAQ answers, clear H2/H3 structure, JSON-LD schema all help citability. |
| Case-outcome context (carefully worded, with mandatory disclaimer) | Prospects want proof of results. CA Rule 7.1 permits factual accurate result descriptions with disclaimer. | LOW-MEDIUM | Only if Burkett provides real anonymized outcomes. Every one gets "Past results do not guarantee similar outcomes" tag. Skip entirely if Burkett is cautious — safer than a bar complaint. |
| Bilingual-signal minimum (Spanish "Hablamos Español" toggle IF true) | 30%+ San Diego County Spanish-speaking. Signals inclusion even without full translation. | LOW | Only if Burkett or staff actually speaks Spanish. If not, omit — false claim is worse than nothing. |

**Ordering of differentiator payoff for family-law lead conversion:**
1. Homepage CTA trio (highest, all channels captured)
2. Warm-approachable design + real photos (bounce reduction)
3. Consult fee transparency (self-qualification, trust)
4. Video welcome (closes trust gap that static copy can't)
5. Attorney-authored jurisdiction-specific blog (organic + AI-search moat)
6. Intake pre-qualifier (lead quality, not quantity)
7. Everything else (nice-to-have)

---

### Anti-Features (Deliberately NOT Built — And Why)

Family-law + YMYL + California Bar advertising rules make several "common law firm site" features actively harmful. These are documented so they don't get re-added later.

| Anti-Feature | Why Requested / Why Tempting | Why Problematic in Family-Law | Do Instead |
|--------------|------------------------------|-------------------------------|------------|
| Guaranteed-outcome copy ("We win 95% of custody cases," "Guaranteed divorce settlement") | Sounds compelling, converts short-term | CA Rule 7.1 explicit violation. Bar complaint risk + Google's "misleading YMYL" filters demote it. | "Committed to advocating for your outcome" language. Show track record with mandatory disclaimer only. |
| Fake or embellished testimonials | Easy conversion lift on paper | CA Rule 7.1 violation. Google spam signal. If discovered, permanent reputation damage in a small SD legal community. | Real Justia-archive testimonials with disclosure. 3 real > 15 fake. If no real ones survive review, omit. |
| Live chat widget with human-mimicking bot | "It boosts conversions" is the pitch | On a YMYL page, a bot answering legal questions is malpractice-adjacent. Also breaks the trust the design is trying to build. Explicitly deferred in PROJECT.md. | Calendar embed + phone + form. All 3 channels visible. |
| Dense legal jargon (petitioner/respondent, ex parte, RFO, DVRO on landing pages) | Signals "I'm a real lawyer" | Prospects don't know these terms and bounce. Also hurts AI-search citability (LLMs prefer plain-language answers). | Plain-language explanations with jargon in parentheses. "Filing for divorce (called a Petition for Dissolution in California)..." |
| Aggressive "ambulance chaser" copy ("Fight back!," "Get what you deserve!," "We destroy the other side") | Feels action-oriented | Family-law prospects are often ambivalent (they still love the other parent). Aggressive copy alienates. Also reads as unprofessional to referring attorneys. | Compassionate + strong: "Steady representation when you need it most." |
| Dark-pattern intake forms (10+ fields, "urgent" false timers, exit-intent popups pushing consultation) | Marketing agency defaults | Family-law prospects are stressed; dark patterns amplify stress + bounce. Also California Consumer Protection issues. | 4-5 field short form + calendar option. No timers, no popups. |
| Unlicensed-jurisdiction pages ("We serve Arizona family law") | Chasing broader SEO | Unauthorized practice of law risk. Also thin content (Burkett doesn't have CA-Arizona depth). | California-only pages. San Diego County depth. Clear "Licensed in California only" in footer. |
| Thin location pages (auto-generated "Divorce in [tiny suburb]" mad-libs beyond the practice × city matrix) | Programmatic-SEO temptation | Burkett is YMYL — Google specifically hunts thin content in this vertical. Learned from cross-client memory: engine templates fabricated content on Mr Green. | 15-20 real, substantive location pages. Each with local court info + city-specific content. Expand from GSC data, not template generation. |
| Blog posts written to hit keyword frequency (SEO filler) | Volume looks like authority | Post-Dec 2025 Google E-E-A-T update penalizes thin YMYL content. Also risks fabrication (Mr Green lesson). | 15-20 curated posts, each substantive, Burkett-attributed, dated, jurisdiction-specific. |
| Generic stock imagery (gavels, scales of justice, blurred courthouse) | Cheap and available | Family-law prospects see gavel-and-scales stock and think "template mill." Kills the warm-approachable premise. | Burkett's real photos (Justia archive) + local San Diego imagery (real courthouse, not stock). |
| Cluttered sidebar navigation, mega-menus, mega-footers | "Enterprise" law firm sites do it | Confuses stressed prospects. Analytics consistently show top-nav simplicity converts better in family-law. | Simple top nav: Practice Areas / About / Blog / Contact + phone in header. Footer with legal disclaimers, sitemap link, hours, address. |
| Client portal / document upload / online payment | "Modern law firm" feature list | Legal ethics on IOLTA + confidential document handling is non-trivial. Explicitly out of scope in PROJECT.md. Not a $480/mo package feature. | Deferred entirely. If a prospect asks, Burkett handles offline (email, in-person). |
| Multiple languages / hreflang | "Inclusive" signal | Out of scope per PROJECT.md — English-only practice. Wrong hreflang implementation actively hurts SEO. | Optional "Hablamos Español" toggle only IF Burkett or staff actually speak Spanish. Otherwise omit. |
| Countdown timers, "3 people viewing this page" false-scarcity, exit popups | Ecommerce-CRO playbook | These are red flags to family-law prospects. Also CA CCPA / dark-pattern liability. | Trust-based design. Compassionate copy. Let the CTA trio do the work. |
| Full support calculators or custody-schedule visualizers as v1 features | "Interactive tools" is a trendy differentiator | Support calculators must be CA DissoMaster-accurate or they're malpractice-adjacent. Complexity is high; risk is real. | Simple downloadable checklists (v1.x). Reconsider a curated support-estimator with heavy disclaimer in v2 only if lead data justifies. |
| Retainer payment collection or online engagement letter signing | "Modernize the intake" pitch | IOLTA rules on trust accounts + attorney-client formation via website = legal minefield. Explicitly out of scope in PROJECT.md. | Offline. Contact form → Burkett follows up → intake handled in person or via secure email. |
| Directory badges from pay-to-play lawyer directories (Justia badge, Avvo top-rated, expertise.com) | "Third-party validation" | Justia badge would defeat the whole point of moving off Justia. Others read as pay-to-play to sophisticated prospects. | CA State Bar, SD County Bar, real Super Lawyers listing if Burkett has one. That's it. |

---

## Feature Dependencies

```
Attorney Bio (real credentials + photo)
    └──enables──> Person/Attorney schema
    └──enables──> Blog post bylines (E-E-A-T)
    └──enables──> Video welcome (same face, coherent brand)

Practice Area Pages
    └──requires──> Attorney Bio (E-E-A-T author signal on service pages)
    └──enables──> FAQ blocks + FAQPage schema
    └──enables──> Location pages (practice × city matrix)
    └──enables──> Blog posts (blog links to relevant practice page)

Location Pages (practice × city matrix)
    └──requires──> Practice Area Pages
    └──requires──> LocalBusiness schema on contact/home
    └──requires──> GBP being live (citation echoes reinforce)
    └──conflicts──> Thin-content risk if pages are template mad-libs

Homepage CTA Trio (phone + calendar + form)
    └──requires──> GHL calendar (Burkett's own, not echolocal shared)
    └──requires──> Netlify form + spam filter deployed
    └──requires──> Working tel: link + phone number decision
    └──enables──> Conversion tracking (call tracking + form submit + calendar booking events)

Blog (15-20 curated posts)
    └──requires──> Attorney Bio (byline target)
    └──requires──> Justia archive content curation + rewrite pass
    └──enables──> AI-search citation surface
    └──enables──> Downloadable resources (blog CTA to gated PDF)

Downloadable Resources
    └──requires──> Netlify form working end-to-end
    └──enables──> Email nurture (defer to v1.x)
    └──requires──> 3-5 PDFs designed + written (Burkett input)

Video Welcome
    └──requires──> Burkett to record (60-90 sec, iPhone quality OK)
    └──enhances──> Homepage CTA trio (video sits above/alongside the trio)

Attorney/LegalService Schema
    └──requires──> Verified bar credentials to reference
    └──requires──> Real office address (LocalBusiness)
    └──enables──> Rich results eligibility + AI citation clarity

llms.txt + AI-friendly structure
    └──requires──> Clean H2/H3 hierarchy on all content pages
    └──enables──> AI Overview / ChatGPT / Perplexity citations
    └──enhances──> Blog + FAQ (already structured for passage-level answers)

Intake Pre-Qualifier
    └──requires──> Netlify form + GHL webhook
    └──enhances──> Contact form (small addition, big lead-quality win)
```

### Dependency Notes

- **Attorney Bio is the taproot.** Nearly every E-E-A-T-relevant feature (blog bylines, schema, video) descends from a substantive, credentialed bio page. Ship this first with sourced facts from the Justia archive.
- **Location pages depend on Practice Area pages.** Practice × city matrix cross-links back to the parent practice page for topical authority. Do not ship location pages before the 8 practice pages are done.
- **Homepage CTA trio has three prerequisites** (GHL calendar, Netlify form, phone `tel:` link). All three need to work end-to-end before homepage feels launched. Test each channel independently with a real submission before cutover.
- **GBP is a parallel workstream that reinforces location pages.** They don't block each other, but GBP live + optimized amplifies location page ranking. Sequence them together in the same phase.
- **Downloadable resources depend on the form being real.** Don't scope PDFs into v1 unless the delivery pipeline (form → email delivery) is verified. Otherwise they're a broken promise on the site.
- **Video welcome depends on Burkett filming.** Client-input dependency = risk. Scope it into v1.x, not blocking v1 launch.

---

## MVP Definition

### Launch With (v1) — Must Be Live by 2026-07-31 Cutover

Everything below is a P1 — the site cannot go live without it, either for legal-ethics, E-E-A-T, or basic conversion reasons.

- [ ] Attorney bio page with verified credentials + real photo — E-E-A-T anchor, everything else references it
- [ ] 8 practice area pages (divorce, child custody, child support, spousal support, mediation, DV, guardianship, family court) — the actual landing surfaces for organic + ads traffic
- [ ] Homepage with equal-weight CTA trio (phone + GHL calendar + Netlify form) above fold — locked in PROJECT.md, primary conversion vehicle
- [ ] Contact page with form + calendar + phone + office address + hours + map — final-mile conversion page
- [ ] 15-20 location pages (practice × city matrix) — high-intent local SEO capture
- [ ] 15-20 curated blog posts with real bylines + dates + jurisdiction tags — organic + AI-search moat
- [ ] FAQ blocks on every practice page (5-8 real questions each) — anxiety-reducer + FAQPage schema
- [ ] Attorney/LegalService + Person + LocalBusiness + FAQPage schema across relevant pages — YMYL non-negotiable
- [ ] Sticky phone in header, footer with disclaimers + jurisdiction + address, mobile-responsive — table stakes
- [ ] Ethical disclaimers (no legal advice, no attorney-client relationship, past results do not guarantee) — CA Bar requirement
- [ ] Privacy policy + terms — CCPA + form data collection minimum
- [ ] Netlify form + spam filter + email notifications working — validated with real test submission
- [ ] Warm-approachable design system (navy + cream + gold + real photos) — differentiator locked
- [ ] Technical SEO baseline (sitemap.xml, robots.txt, canonicals, OG, llms.txt, `pretty_urls=false`, GA4 injection per clients.json) — cross-client learnings applied
- [ ] Intake pre-qualifier fields on contact form (matter type, urgency, county, opposing counsel) — lead-quality win, near-zero build cost

### Add After Validation (v1.x) — First 60 Days Post-Launch

Trigger for adding = site is live, form submissions are landing, GSC data is coming in.

- [ ] Video welcome from Burkett on home — Burkett records when ready; trust-close differentiator
- [ ] 3-5 downloadable resource PDFs (custody exchange checklist, divorce filing checklist, financial disclosure prep) with email opt-in gate — nurture list builder
- [ ] Consult fee transparency block — pending Burkett decision on fee model
- [ ] Practice-area "What to expect" visual timelines — content depth + AI citation surface
- [ ] Case-outcome context blocks (carefully worded) IF Burkett provides real anonymized outcomes — otherwise skip permanently
- [ ] Curated real testimonials with CA Rule 7.1 disclosure from Justia archive — final review with Burkett
- [ ] Attorney-in-media / bar association badges (real only) — trust signal expansion
- [ ] Additional blog posts (16→25+) based on GSC opportunity keywords — organic expansion
- [ ] Expanded location pages beyond initial 15-20, based on GSC data — earned expansion, not speculative

### Future Consideration (v2+) — Only If Lead Data Justifies

- [ ] Interactive support-estimator calculator (CA-specific, heavy disclaimer) — high complexity + malpractice risk; only worth building if lead data shows research-stage prospects are the bottleneck
- [ ] Custody-schedule visualizer — same reasoning as support calculator
- [ ] Client portal / document upload — out of scope per PROJECT.md; legal + technical complexity, not in $480/mo package
- [ ] Online retainer payment / engagement letter signing — IOLTA/CA Bar complexity, out of scope per PROJECT.md
- [ ] Full Spanish language site with hreflang — only if Burkett hires Spanish-speaking staff or partners
- [ ] AI receptionist (Roman-style) integration — deferred to post-launch phase per PROJECT.md, wires to Burkett's phone after v1 ships

---

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| Attorney bio (real credentials + photo) | HIGH | LOW | P1 |
| 8 practice area pages | HIGH | MEDIUM | P1 |
| Homepage CTA trio (phone + calendar + form) | HIGH | LOW | P1 |
| Sticky phone in header + `tel:` links everywhere | HIGH | LOW | P1 |
| Contact page with form + calendar + address/map | HIGH | LOW | P1 |
| 15-20 location pages (practice × city matrix) | HIGH | MEDIUM | P1 |
| 15-20 curated blog posts (E-E-A-T rewrite) | HIGH | HIGH | P1 |
| FAQ blocks on practice pages | HIGH | MEDIUM | P1 |
| Attorney/LegalService + Person + LocalBusiness schema | HIGH | MEDIUM | P1 |
| Ethical disclaimers + privacy policy + terms | HIGH | LOW | P1 |
| Warm-approachable design system | HIGH | MEDIUM | P1 |
| Netlify form + spam filter + notifications | HIGH | LOW | P1 |
| Intake pre-qualifier fields | HIGH | LOW | P1 |
| Technical SEO baseline (sitemap, robots, canonicals, llms.txt, `pretty_urls=false`) | HIGH | LOW | P1 |
| Mobile responsive + <3s load | HIGH | LOW | P1 (inherent to static stack) |
| Accessibility (WCAG 2.1 AA) | MEDIUM | MEDIUM | P1 (legal risk) |
| Video welcome from Burkett | HIGH | MEDIUM | P2 |
| Downloadable resources (checklists, guides) | HIGH | MEDIUM | P2 |
| Consult fee transparency | HIGH | LOW | P2 (pending Burkett decision) |
| "What to expect" visual timelines per practice | MEDIUM | MEDIUM | P2 |
| Real curated testimonials with disclosure | HIGH | LOW | P2 (Burkett review gated) |
| Case-outcome context (with disclaimer) | MEDIUM | LOW | P2 (Burkett gated) |
| Attorney-in-media / bar badges | MEDIUM | LOW | P2 |
| Bilingual "Hablamos Español" toggle | MEDIUM | LOW | P3 (only if true) |
| Interactive support calculator | MEDIUM | HIGH | P3 (v2+, malpractice risk) |
| Client portal / document upload | LOW | HIGH | P3 (out of scope) |
| Online retainer / payment | LOW | HIGH | P3 (out of scope) |
| Live chat widget | NEGATIVE | MEDIUM | ANTI (deferred per PROJECT.md) |
| Multi-language hreflang | LOW | HIGH | P3 (out of scope) |

**Priority key:**
- P1: Must have for launch (2026-07-31 hard date)
- P2: Should have, add in v1.x after launch validates
- P3: Nice to have, future consideration only if data justifies
- ANTI: Explicitly do not build (see Anti-Features table for rationale)

---

## Competitor Feature Analysis

Sampled from 2026 SD family-law competitors (public sites) + PaperStreet / Rankings.io / Attorney at Law Magazine "best of" lists.

| Feature | Typical SD Solo Family Law Competitor | High-Performing Family Law Firms (national) | Burkett Site Approach |
|---------|---------------------------------------|---------------------------------------------|-----------------------|
| Homepage CTA | Form-first, phone in header, no calendar | Phone + calendar + form (varies) | Equal-weight trio, all above fold (differentiator) |
| Design tone | Navy/white classical, gavel imagery, stock | Warm palette + real photos + human copy | Warm-approachable (navy + cream + gold + Burkett photos) |
| Practice area pages | 3-5 short pages, generic copy | 8-12 pages, jurisdiction-specific, FAQ blocks | 8 pages, CA/SD-specific, FAQ per page, ~1000 words each |
| Blog | Empty or 5-10 old posts, no bylines | 20-50 posts, author bylines, dates | 15-20 curated + Burkett-bylined, E-E-A-T rewritten |
| Location targeting | None or thin "we serve all of SD" | Practice × city pages (varies quality) | 15-20 substantive practice × city pages |
| Attorney bio | Short paragraph + headshot | Full credentials + photo + video + reviews | Full credentials + photo + (video in v1.x) |
| Schema | None or basic Organization | LegalService + Attorney + FAQPage + Article | Full stack: LegalService + Attorney + LocalBusiness + FAQPage + Article + Person |
| Video | Rare | Increasingly common on premium firms | v1.x add (Burkett records) |
| Downloadable resources | Rare | Common on top-tier | v1.x add (3-5 checklists) |
| Live chat | Common (often bad) | Increasingly rare (replaced by calendar) | Not building (differentiator by omission) |
| Consult fee transparency | Rarely shown | Increasingly common | v1.x once Burkett decides |
| llms.txt / AI-search optimization | Almost none | Rare, but growing | Included in v1 (differentiator) |
| Accessibility (WCAG AA) | Often failing | Increasingly compliant | v1 requirement |

**Key insight:** Most SD solo family law sites fail at 4+ table-stakes items (thin bio, no FAQ, no schema, no location depth). Burkett's edge in v1 is *executing table stakes correctly at the YMYL bar*, layered with a small set of high-impact differentiators (CTA trio, warm design, AI-search readiness). Interactive tools + video + downloads are v1.x — good to have, not what wins v1.

---

## Sources

- PROJECT.md (Burkett's constraints, scope, design brief, content source)
- MEMORY.md (Echo Local cross-client learnings: Netlify pretty_urls, GA4 pollution, fabrication risk, form subject templates, spam filter patterns)
- [What a Solo Law Firm Website Actually Needs in 2026 — LuckyFish Media](https://www.luckyfishmedia.com/2026/what-a-solo-law-firm-website-actually-needs-in-2026-and-whats-a-waste-of-money/) — MEDIUM confidence (industry commentary, current)
- [How to Build a High-Performing Solo Attorney Website — ABA Law Technology Today](https://www.americanbar.org/groups/law_practice/resources/law-technology-today/2025/how-to-build-a-high-performing-solo-attorney-website/) — HIGH confidence (ABA authoritative)
- [Best Family Law Websites in 2026 — PaperStreet](https://www.paperstreet.com/best-family-lawyer-websites/) — MEDIUM (industry curated examples)
- [Family Lawyer Website Design 2026 — Rankings.io](https://rankings.io/blog/web-design-for-family-lawyers/) — MEDIUM (vertical-specific analysis)
- [SEO for Family Law Attorneys 2026 Roadmap — YMM Digital](https://ymmdigital.com/search-engine-optimization-for-family-law-attorneys-a-2026-roadmap/) — MEDIUM (vertical + SEO analysis)
- [Best Law Firm Websites in 2026 — Attorney at Law Magazine](https://attorneyatlawmagazine.com/legal-marketing/website-design/best-law-firm-websites) — MEDIUM (curated examples)
- California Rules of Professional Conduct 7.1, 7.3 (attorney advertising rules) — HIGH confidence (canonical legal source, applied to anti-features rationale)

---

*Feature research for: Solo family law attorney website, San Diego / YMYL / California*
*Researched: 2026-07-02*
