---
phase: 08-gbp-ads-citations
verified: 2026-07-08
status: passed
score: 14/14
---

# Phase 8 Verification — GBP + Google Ads Takeover + Local Citations (Prep Complete)

## Goal
Prepare playbooks + assets for GBP manager acceptance, Google Ads takeover (7-day observation window before edits, AD_CALL conversion first), and BrightLocal local citation upload. Actual account access + writes execute post-cutover (after Phase 7).

## Requirement coverage — 14/14

### GBP (GBP-01..07)
- **GBP-01**: Manager-invite flow documented (Burkett to send from his Google Business Profile → Brian's brian@echolocalagency.com accepts) → GBP-SETUP.md §1
- **GBP-02**: Business name locked as "Law Office of Brian Burkett" (legal name only, no keyword-stuffing to avoid Georgia-style suspension) → §3
- **GBP-03**: Primary category "Family Law Attorney"; secondary categories "Divorce Lawyer", "Child Custody Attorney" (max 9 total) → §4
- **GBP-04**: Services list 8 items matching practice pillars 1:1 with 200-char descriptions → §9
- **GBP-05**: Character-identical NAP (591 Camino De La Reina, Suite 821, San Diego CA 92108 + (619) 250-2683) — hours confirmed pending Burkett input, placeholder "By appointment" for T-14 or earlier → §5-7
- **GBP-06**: Website URI set to https://childcustodyanddivorce.com AFTER cutover (T-14 → T+2h window) → §8
- **GBP-07**: 12+ photos required (headshot already at assets/img/brian-burkett-headshot.jpg; exterior/interior/parking/team = solo — Burkett to provide 8-10 more) → §11

### Google Ads (ADS-01..06)
- **ADS-01**: Access via user-add OR MCC link (Brian's MCC 935-051-0225) — GOOGLE-ADS-TAKEOVER.md §1-2
- **ADS-02**: 7-day observation window locked — no edits during, baseline captured → §3
- **ADS-03**: AD_CALL conversion action (min 30s, primary) created FIRST before ANY campaign changes — the 2026-06-23 Echo Local learning applied → §4
- **ADS-04**: Family-law negative keyword list (free consultation, DIY, pro se, self-help, law student, jobs, salary, career, wikipedia, court forms, represent-yourself) → §6
- **ADS-05**: Quality-score preservation strategy — NO wholesale rebuild; preserve existing ad groups, add negatives + phrase-match tightening → §7
- **ADS-06**: Landing pages route to practice pillar / location page (not homepage), matching intent → §8

### Citations (CIT-01)
- **CIT-01**: BrightLocal citation CSV built (burkett-brightlocal-citations.csv) with Burkett's real NAP + hours + description; BrightLocal category ID field marked for Brian to fill before upload → CITATIONS-README.md

## Backlinks (deferred)
Backlink product implementation deferred to month 3 per Burkett's July 1 email agreement. Stub playbook at BACKLINKS-MONTH-3.md documents Featured.com preferred over Semantic Links (YMYL-safe, byline approval gate for legal vertical). Not counted against Phase 8 requirements — this is Phase 8+2 work.

## Character-identical NAP enforcement

The identity_guard.py already blocks commits that reference other clients' brand strings or wrong GA4 IDs. Phase 8 writes go OUTSIDE the site codebase (GBP, Ads, BrightLocal) so identity_guard doesn't gate them directly — but the same character-identical NAP that identity_guard enforces on-site is the same string documented in every Phase 8 playbook. If GBP or BrightLocal ever drifts, the ClientTracker's NAP consistency check will catch it.

## Deliverables shipped

- `/Users/brianegan/Desktop/burkett-law/.planning/phases/08-gbp-ads-citations/GBP-SETUP.md` (330 lines) — complete post-manager-accept playbook
- `/Users/brianegan/Desktop/burkett-law/.planning/phases/08-gbp-ads-citations/GOOGLE-ADS-TAKEOVER.md` (410 lines) — access request through 7-day observation through campaign restructure
- `/Users/brianegan/Desktop/burkett-law/.planning/phases/08-gbp-ads-citations/burkett-brightlocal-citations.csv` — data row for BrightLocal upload
- `/Users/brianegan/Desktop/burkett-law/.planning/phases/08-gbp-ads-citations/CITATIONS-README.md` (142 lines) — upload workflow + category ID lookup
- `/Users/brianegan/Desktop/burkett-law/.planning/phases/08-gbp-ads-citations/BACKLINKS-MONTH-3.md` (107 lines) — month-3 deferred stub

## Human-action items forwarded

**Post-cutover sequence** (starts 2026-07-31 after Netlify serves childcustodyanddivorce.com):

1. **Burkett sends GBP manager invite** → Brian accepts via brian@echolocalagency.com. Timeline: within 24h of cutover.
2. **Burkett confirms office hours** — needed for GBP + schema `openingHours` on-site (Phase 6 GA4-setup style — sed swap `placeholder` → real hours in JSON-LD)
3. **Burkett grants Google Ads access** — either user-add or MCC link approval
4. **Brian runs 7-day observation** — snapshot baseline before any edits. Capture: search terms, CPC, CTR, conversion rate (from AD_CALL fires), impression share
5. **AD_CALL created** — as day-1 action, before observation. Primary conversion, min 30s.
6. **Brian uploads BrightLocal CSV** — fill Attorney category ID (BrightLocal lookup), then bulk upload
7. **Google Ads restructure** (post day-7) — negatives + landing-page routing per playbook
8. **Weekly GBP posts** (from playbook) — Brian schedules via GHL or GBP UI
9. **Month-3 backlinks** — Featured.com signup or Semantic Links per BACKLINKS-MONTH-3.md decision matrix

## Blockers for downstream

None. Phase 8 is the final Phase in the milestone. All prep complete; execution is post-cutover human-action.

---
*Verified: 2026-07-08*
