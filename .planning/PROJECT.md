# Burkett Family Law Website

## What This Is

An SEO-optimized static website for the Law Office of Brian Burkett (San Diego family law attorney) that replaces his current Justia-owned site before Justia's 2026-07-31 shutoff. Built to rank locally for high-intent family law queries across San Diego County, convert stressed prospects into consultations via phone/calendar/form, and give Burkett full ownership of his content and lead flow. This is Echo Local's first attorney client and first YMYL legal build.

## Core Value

Burkett owns the site, owns the leads, and ranks locally in San Diego for divorce, child custody, and related family law intent — with content Google trusts as genuine legal expertise (E-E-A-T signals real enough for the YMYL bar).

## Requirements

### Validated

<!-- Shipped and confirmed valuable. -->

(None yet — ship to validate)

### Active

<!-- Current scope. Building toward these. -->

- [ ] Static site scaffolded and deployed to Netlify from GitHub (EchoLocalagency org) with warm-approachable design system (navy + warm cream + gold, Burkett's real photos, human warmth appropriate for family-law prospects)
- [ ] Attorney bio page with verifiable credentials (bar admission, education, practice history) sourced from Justia archive — real, no fabrication
- [ ] Practice area pages for the 8 verticals from Justia (divorce, child custody, child support, spousal support/alimony, mediation, domestic violence, guardianship, family court) with FAQ schema
- [ ] San Diego County location pages: practice × city matrix, 15-20 combinations for high-intent local SEO
- [ ] Blog: 15-20 curated posts from the 40 Justia originals, rewritten to E-E-A-T bar (real author, dates, jurisdiction specificity)
- [ ] Homepage above-the-fold conversion: call button (tel:6192502683), calendar embed (GHL), and contact form — all three equally prominent
- [ ] Netlify contact form with spam filter (per reference_spam_filter_patterns.md) and email notifications to Burkett + brian@echolocalagency.com
- [ ] Attorney/LegalService + Person schema on every relevant page (LegalService, Attorney/Person for bio, FAQ on practice pages, LocalBusiness on home/contact)
- [ ] Technical SEO baseline: sitemap.xml, robots.txt, canonical URLs, OG tags, llms.txt, `pretty_urls=false` in netlify.toml (prevent the deindex bug hit on Mr Green/Ecosystem), correct GA4 injection per site
- [ ] Google Business Profile onboarded and optimized (accept manager invite, categories, services, hours, description, photos)
- [ ] Google Ads takeover: gain access to his account, restructure campaigns for family law San Diego intent, set call tracking, add negatives
- [ ] Domain cutover: point childcustodyanddivorce.com (Network Solutions) at Netlify before 2026-07-31 without a dark window
- [ ] GA4 property + Google Search Console verified, spam filter live, form submissions land in inbox
- [ ] Local citations plan (BrightLocal CSV built for legal category, Brian uploads)

### Out of Scope

<!-- Explicit boundaries. Includes reasoning to prevent re-adding. -->

- Backlink service — Burkett agreed to defer link building to month 3 so foundation exists to point links at
- Live chat widget — added friction on YMYL pages, deferred; Burkett prefers call/booking anyway
- Client portal / document upload — legal-sensitive, not part of $480/mo package, defer to future
- Payment/retainer intake online — legal trust/IOLTA requirements; keep off v1
- Multiple languages (hreflang) — US-only English practice, no Spanish requested at this scope
- AI receptionist (Roman-style) integration — package includes AI/voice but scope to post-launch phase; site + SEO + GBP + Ads first, then wire receptionist to his number
- Ecommerce / online scheduling of paid services — not applicable
- Blog posts >20 or thin location pages beyond the practice×city matrix — protects against Google's YMYL/thin-content flags

## Context

**Client profile.** Brian Burkett, solo family law attorney in San Diego (Mission Valley office at 591 Camino De La Reina Suite 821). Domain childcustodyanddivorce.com is his; he controls the Network Solutions registrar login. His current site is Justia-owned — Justia will keep it live until 2026-07-31. He signed $480/mo all-in (site + hosting + SEO + AI/voice + GBP + Google Ads mgmt) plus separate ad spend paid direct to Google. Payment came in 2026-07-02. He explicitly told Brian he expects a learning curve since he's Brian's first attorney client and prefers thorough over fast.

**Content source.** ~/Desktop/Burkett Justia Archive/ contains a full scrape: 63 HTML pages, 12 images (headshots + practice imagery), 63 text extracts. Includes his attorney bio, all 8 practice area pages, ~40 blog posts, and reviews. This is the raw material for site content — nothing needs to be invented.

**Vertical constraints (YMYL/legal).** Family law is a Google YMYL category. Sites get scrutinized harder on E-E-A-T than almost any other vertical. Content must have real author attribution (Burkett as author), verifiable credentials on-page, jurisdiction-specific accuracy (California family law, San Diego Superior Court), and Attorney/LegalService schema. Thin or generic content actively hurts. Legal ethics rules also apply — no client testimonials that could be misleading, no guaranteed-outcome language, appropriate disclaimers.

**Agency infrastructure available.** SEO engine at ~/EchoLocalClientTracker/ (blog_engine, location_pages, identity guard system), spam filter library, Netlify form pattern, BrightLocal citation CSV builder, GHL calendar embed pattern (calendar id already identified: PW5Ma7sjF3S6AWayZDuK / echolocal-free-audit — Burkett will need his own), Roman receptionist framework, GBP Business Information API, Google Ads MCC (customer id 935-051-0225), Supabase client tracker. Everything already used for other clients.

**Cross-client learnings to bake in.**
- Netlify pretty_urls bug caused SoCal deindexing — always set `pretty_urls=false` in netlify.toml.
- Cross-client GA4 pollution happened when generic engine templates hardcoded one client's GA id — must inject Burkett's GA4 from clients.json per page.
- Fabricated content bit Mr Green (steam/enzyme/180°F claims). Content-fabrication risk is real; every claim on the site must be sourceable from the Justia archive or verified with Burkett.
- Netlify subject_template only supports {site_name}/{form_name}/{site_url} — no form field substitution (learned from 12 broken hooks).
- Netlify-GitHub auto-deploy can break silently (Chef Dorothy went 84 days without deploys). Verify auto-deploy after initial link.
- Address spacing in GBP names matters (Georgia's "PsychicExperience" issue).

**Design brief locked.** Warm-approachable direction: navy + warm cream + gold, Burkett's real photos (from Justia archive) front and center, compassionate tone appropriate for stressed family-law prospects. Not glossy corporate, not stuffy classical.

**CTA strategy locked.** Homepage and every practice page surface all three: phone (tel:6192502683), GHL calendar embed (for booking a 15-min intake), and contact form. Equal weight so leads self-select their channel.

**Content strategy locked.** Curate the 40 Justia blog posts down to the strongest 15-20, rewrite each for E-E-A-T (real author bio, publish date, San Diego / California specificity), preserve URL slugs where possible for SEO history. Port the 8 practice areas 1:1 with structural rewrite for better on-page SEO.

**Location strategy locked.** Practice × City matrix — 15-20 pages like "Divorce Attorney in La Jolla" and "Child Custody Lawyer in Chula Vista" using the top 3-4 practice areas × top 5-6 San Diego cities. Burkett attached a full SD County zip codes/neighborhoods doc to reference. Start narrow, expand post-launch based on GSC performance.

## Constraints

- **Timeline**: Justia site sunset 2026-07-31. Build must be live on childcustodyanddivorce.com by that date with zero dark window during cutover. Burkett agreed to no-rush, quality-first pacing — but the hard date is fixed.
- **Vertical**: YMYL/legal. E-E-A-T is not optional. All content must be sourceable, credentialed, and appropriately disclaimered. No fabricated claims or guarantees.
- **Tech stack**: Static HTML/CSS/JS per CLAUDE.md client-site pattern (Chef Dorothy, Primal Plates, Psychic Experience). No framework. Deploy via GitHub push → Netlify auto-deploy. No `netlify deploy` direct commands.
- **Domain control**: Burkett owns childcustodyanddivorce.com at Network Solutions. DNS change is a manual step he executes when the new site is ready.
- **Package scope**: $480/mo total. Backlinks deferred to month 3. AI receptionist deferred to post-launch phase. No client portal, no online payments.
- **Content source**: All facts, credentials, service descriptions must trace back to the Justia archive at ~/Desktop/Burkett Justia Archive/ or to Burkett directly. No fabrication.
- **Deployment discipline**: Every commit must pass identity guard checks (no cross-client contamination), correct GA4 id from clients.json, and Netlify `pretty_urls=false` to prevent deindex bug.
- **Legal compliance**: California State Bar advertising rules apply — no misleading claims, appropriate disclaimers, no testimonials without disclosure.

## Key Decisions

<!-- Decisions that constrain future work. Add throughout project lifecycle. -->

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Warm-approachable design direction (navy + warm cream + gold, real photos) | Family law prospects are stressed; warm palette + human imagery reads compassionate and trustworthy. Differentiates from cookie-cutter classical-authoritative law firm aesthetic. | — Pending |
| Homepage CTA: all three (call + calendar + form) equal weight above fold | Family law leads split by channel preference (some call in crisis, some book quietly, some fill forms). Equal surface avoids missing any. | — Pending |
| Blog: curate top 15-20, rewrite for E-E-A-T | YMYL legal has the highest content-quality bar. Better to ship 15 strong posts than 40 mediocre ones that Google flags. | — Pending |
| Location strategy: practice × city matrix (15-20 to start) | High-intent local queries follow this pattern. Narrow start prevents thin-content flags; expandable post-launch based on GSC. | — Pending |
| Static HTML/CSS/JS + Netlify + GitHub deploy pattern | Matches every other Echo Local client site. Zero framework overhead, fastest to ship, easiest to maintain. | — Pending |
| Defer AI receptionist to post-launch phase | Package includes it but site + SEO + GBP + Ads takeover is the critical path for the 2026-07-31 cutover. Receptionist wires in after site is live. | — Pending |
| Defer backlinks to month 3 (per Burkett-approved plan) | Foundation must exist before pointing authority at it — new site + content + profile + citations first. Confirmed with client. | — Pending |
| Content must trace to Justia archive or Burkett direct | Learned from Mr Green fabrication issue. YMYL legal cannot have invented claims. | — Pending |

---
*Last updated: 2026-07-02 after initialization*
