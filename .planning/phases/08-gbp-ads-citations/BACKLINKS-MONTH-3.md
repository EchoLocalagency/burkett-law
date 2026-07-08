# Backlink Product (Deferred to Month 3)

**Status**: **Deferred**. Do not execute until month 3 of Burkett's engagement.
**Reason**: Per Burkett's 2026-07-01 close email, the $480/mo package covers site + hosting + SEO + AI/voice + GBP + Google Ads management. Backlinks are an add-on product Brian raises to Burkett at month 2-3 once the site has established a baseline and Burkett has trust in the delivery cadence.
**Decision (from 2026-07-01 agency memory)**: **Featured is the default** for Burkett — YMYL requires E-E-A-T-safe white-hat backlinks. Semantic Links (gray-hat but low-risk-for-local) is a fallback if Burkett declines the Featured cadence.

---

## Product decision recap

### Featured (featured.com) — DEFAULT for Burkett
- **Cost**: $100/month seat (Business tier) or pay-as-you-go credits
- **Charge**: $250/month (retail)
- **Margin**: $150
- **Type**: White-hat — attorney responds to journalist source requests, response gets published as a byline in the outlet, natural backlink from a real editorial context
- **Why for Burkett**: Family law is YMYL. Google's Dec 2025 E-E-A-T update explicitly extends to all competitive queries. A byline in a real publication + attorney bio linking back = the gold-standard trust signal.
- **Cadence**: 1-3 published bylines per month at typical response volume + acceptance rate (empirical 18-20% pickup after ~3-month ramp per 2026-07-02 Connectively-support conversation)
- **Legal-specific gate**: Attorney byline responses need Burkett approval before submission — Cal Bar 7.1 attaches to any published statement. Brian drafts, Burkett approves, then submit.
- **Featured seat lock caveat (from 2026-07-02 Connectively-support conversation)**: A Featured paid seat locks to ONE expert profile for the full 30-day billing period — cannot rotate mid-cycle across Brian's client roster. This means Burkett gets his seat for the full billing month; the seat is not shared with Mr Green or another client during that month.

### Semantic Links (semanticlinks.io) — FALLBACK
- **Cost**: $299/month flat
- **Charge**: $400/month
- **Margin**: $100
- **Type**: Gray-hat — private blog network + guest posts. Real, indexed, DR 20-40 domains. Lower editorial vetting than Featured.
- **Why NOT default for Burkett**: YMYL family law. Any hint of PBN-style backlink pattern raises Google Trust Team scrutiny. Fine for non-YMYL locals (Mr Green, Arcadian). Not the safe first move for a family law attorney.
- **When to consider**: If Featured yields <1 byline/month for Burkett over the first 2 months of Featured subscription, Semantic Links becomes the volume backstop. Reserved decision.

---

## Month 3 execution sequence

**Prerequisites** (do not execute before all of these):
- [ ] Site has ≥60 days of live GA4 data at childcustodyanddivorce.com
- [ ] GSC shows organic impressions trending up (any positive slope)
- [ ] Burkett has paid month 2 successfully (retention proof)
- [ ] Cal Bar 7.1 attorney-approval workflow is documented (see below)

### Step 1 — Discuss with Burkett
Email or call: "We've had 2 months of the site live, GA4 shows [X] sessions and [Y] leads. To accelerate ranking for competitive terms (San Diego divorce attorney, child custody San Diego), the next lever is authoritative backlinks — real publications citing you as a family law source. There's a service called Featured that connects attorneys to journalists at outlets like Forbes, Newsweek, Inc.com looking for expert quotes. It's $250/month, adds 1-3 published bylines per month with real backlinks. Every response is drafted for your approval before it goes out — nothing publishes under your name without your sign-off. Interested?"

### Step 2 — Attorney approval workflow (Cal Bar 7.1)
Every Featured response Brian drafts for Burkett follows this cycle:
1. Brian receives Featured source request (e.g., "Family law attorney needed for a Forbes piece on high-asset divorce")
2. Brian drafts response using Burkett's practice facts + Cal Bar 7.1 clean language (no superlatives, no guarantees, no invented outcomes)
3. Brian sends draft to Burkett via email with 48h approval deadline
4. Burkett replies with edits or approval
5. Brian submits final approved text to Featured
6. When published, Brian archives the URL + PDF of the published byline to `.planning/phases/08-gbp-ads-citations/backlinks/featured/` (create when this ships)

### Step 3 — Subscribe and configure
1. Brian creates a Featured seat under his agency account with Burkett as the expert profile.
2. Configure the profile: bio (matches site `/about.html`), expertise areas (family law, divorce, child custody, California), practice location (San Diego), byline link (https://childcustodyanddivorce.com/about.html).
3. Set daily source-request digest → brian@echolocalagency.com.

### Step 4 — Track outcomes
Log each submitted response + outcome in `.planning/phases/08-gbp-ads-citations/backlinks/featured/response-log.md`:

| Date | Source Request | Outlet | Response Drafted | Burkett Approved | Submitted | Published URL | DR |

Target after 3 months of Featured: ≥3 published bylines, ≥2 backlinks from DR 40+ domains.

If below target after 3 months → escalate: increase response volume, or switch to Semantic Links fallback.

---

## Automation potential (future)

**Idea**: A daily-scan brain script (`scripts/burkett_featured_scan.py`) that:
1. Polls Featured API for new source requests matching Burkett's expertise tags
2. Filters for family-law-related requests
3. Uses `claude -p` (CLI subprocess, per Brain Pattern in ~/CLAUDE.md) to draft a response following:
   - Burkett's practice facts from `content_facts.md`
   - Cal Bar 7.1 lint clean
   - Attorney-voice tone match
4. Emails the draft to Burkett with the source request URL + 48h deadline
5. On Burkett's approval-reply (email watcher via Gmail API), submits to Featured
6. Logs to response-log.md

**Do not build now** — nothing to test against. Build after 1 month of manual Featured operation to confirm the response pattern and Burkett's approval preferences are well understood.

---

## Placeholder file structure

When backlinks ship in month 3, this directory structure will be created:

```
.planning/phases/08-gbp-ads-citations/backlinks/
├── featured/
│   ├── response-log.md
│   ├── published/
│   │   └── YYYY-MM-DD_outlet-slug.md (archive of published bylines)
│   └── drafts/
│       └── YYYY-MM-DD_source-request-slug.md
├── semantic-links/  (only if fallback triggered)
│   └── ...
└── BACKLINKS-STATUS.md  (rolling status doc)
```

---

## Blockers / decisions to revisit

- **Featured PAYG pricing**: Not yet quoted by Connectively (per 2026-07-02 memory). Confirm PAYG rate before committing — if PAYG is high per-credit, seat-lock disadvantage is amplified.
- **Semantic Links exclusivity**: Before ever escalating to Semantic Links for Burkett, confirm per-client domain exclusivity (Burkett doesn't share a link-source domain with Mr Green or another client — Google's link graph flags this).
- **Cal Bar 7.1 on published content**: Every byline that goes live under Burkett's name is subject to Cal Bar. Confirm Burkett's malpractice carrier has no marketing-content exclusion.
