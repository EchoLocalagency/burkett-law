# Google Ads Takeover — Law Office of Brian Burkett

**Requirement coverage**: ADS-01, ADS-02, ADS-03, ADS-04, ADS-05, ADS-06
**Type**: Preparation playbook + execution runbook. Brian executes once Burkett's Google Ads access is confirmed AND site is live at childcustodyanddivorce.com (Phase 7 cutover complete).
**Sequence lock**:
1. Site live at target domain → 2. Access confirmed → 3. AD_CALL conversion action created → 4. 7-day observation → 5. Edits begin.

**Do NOT skip the 7-day observation.** This is the 2026-06-23 Echo Local blind-spot rule. Editing without baseline metrics loses the counterfactual you need to prove your changes helped.

**Do NOT cancel Clientomics/Rankaroo/Justia access until baseline is in hand.** Burkett committed to canceling them per his 2026-07-01 email, but the actual cancellation waits until we have their historical CPC + CTR + conversion + negative-keyword data captured.

---

## Prerequisites

| Item | Status | Notes |
|------|--------|-------|
| Site live at childcustodyanddivorce.com | Phase 7 gate | AW conversion actions attribute to a specific site — needs the real site live. |
| Burkett's Google Ads Customer ID | Ask Burkett | Format: `XXX-XXX-XXXX`. Burkett's 2026-07-01 email said he figured out access — ask for CID before proceeding. |
| Access path decided | See Step 1 | Two options: user-add to brian@echolocalagency.com Admin, OR MCC link (Brian's MCC = `935-051-0225`). |
| Rankaroo/Clientomics historical data captured | Blocked | Run baseline capture BEFORE cancellation. See Step 3. |
| AW placeholder audit clean | Passed | `grep -r "AW-BURKETTAWXXX0" .` returns 3 placeholders wired in `assets/js/analytics.js` — swap after real IDs land (see GoogleAds-conversions.md Phase 6 doc). |

---

## Step 1 — Access (ADS-01)

Two paths. Prefer MCC link (cleaner, revocable, no user-account exposure):

### Path A (preferred): MCC link

1. Brian sends a link request from `935-051-0225` to Burkett's Customer ID:
   - Google Ads → sign in as MCC `935-051-0225` → Tools & Settings → Access and security → Managers → **Send invitation**
   - Enter Burkett's Customer ID → Access level: **Admin** → Send.
2. Burkett receives the link request in HIS Google Ads UI → Tools → Access and security → **Managers** → Accepts.
3. Brian confirms — `935-051-0225` now shows Burkett's account in "Accounts" list.

Advantages: Brian can pull access without touching Burkett's Google account. All actions are attributed to the MCC login. Reporting stays in one place with Echo Local's other clients.

### Path B: User-add

1. Burkett: Google Ads → Tools → Access and security → **Add user** → `brian@echolocalagency.com` → Admin.
2. Brian accepts.

Advantages: works even if Burkett is on a legacy account structure MCC won't link to.

Disadvantages: harder to revoke cleanly. If Brian ever leaves, Burkett has to remember to remove access.

### Verification

After access is confirmed, Brian must be able to see (without editing anything):
- Account overview → last 30 days impressions + clicks + spend
- Campaigns list
- Search terms report
- Existing conversion actions
- Existing negative keyword lists

---

## Step 2 — Create AD_CALL conversion action FIRST (ADS-03)

**Rule from 2026-06-23 Echo Local audit**: create AD_CALL conversion BEFORE any campaign edits. Otherwise you edit blind — the calls that DID come in from ads get zero attribution, and every "campaign is wasted" call looks like fact when it's actually a tracking gap.

### The action

**Type**: Calls from ads
**Goal category**: Contact (or "Book appointment" if leads pass to calendar)
**Name**: `AD_CALL Burkett`
**Value**: $200 (proxy value per qualified call; family law leads > Echo Local's $150 because higher lifetime value per case)
**Count**: One (dedupe per session)
**Minimum call length**: **30 seconds** (locked — Echo Local's rule; prevents wrong-number 5-sec bounces from counting)
**Attribution model**: Data-driven
**Include in "Conversions"**: **YES** (primary — this is the metric bidding optimizes)

### Create the action

1. Google Ads → Tools & Settings → Measurement → **Conversions** → **New conversion action**.
2. Choose **Phone calls** → **Calls from ads**.
3. Configure per above.
4. Google will require enabling **account-level call reporting**. Enable it (per 2026-06-23 Echo Local rule — Burkett's account may already have it on if Rankaroo enabled it).
5. Enter Burkett's cell/office phone in the call reporting settings so Google's forwarding number → forwards to the correct destination. The forwarding number is what shows in the ads, NOT the primary phone.

### Verify the action fires

Wait 24-72h after ads run with the new action. Google Ads → Tools → Conversions → `AD_CALL Burkett` should show "Recording" and non-zero calls.

---

## Step 3 — 7-day observation window (ADS-02)

**Rule**: no campaign edits during this window. Purpose is to establish baseline before edits so we can prove the takeover helped, not hurt.

### Baseline capture (day 0)

Run on day 0 of access, before AD_CALL has data:

```bash
# Placeholder — actual capture uses Google Ads Editor CSV export
# or the Google Ads API via a script similar to ~/EchoLocalClientTracker/scripts/echo_local_ads_lockdown_2026_06_07.py

# Metrics to capture per campaign, last 30 days:
# - Impressions
# - Clicks
# - CTR
# - Avg CPC
# - Total spend
# - Conversions (whatever action was configured pre-takeover, if any)
# - Cost / conv
# - Search terms report (top 100 terms with impressions + clicks + conversions)
# - Negative keyword lists (all lists + all keywords per list)
# - Bidding strategy per campaign
# - Ad groups + ad copy per campaign
# - Landing page URL per ad
```

**Save the baseline** to `.planning/phases/08-gbp-ads-citations/ads-baseline-day0.json` (create as needed on execution day).

### Daily monitoring (days 1-7)

Per campaign per day, capture:
- Impressions, clicks, spend, conversions, cost/conv
- Any search-terms report entries with clicks > 3 and 0 conversions (candidate negatives)

**Do NOT edit anything.** Log observations only.

**One exception**: If a campaign is bleeding budget on an obvious junk term (competitor lawyer name Burkett doesn't want to bid on, "law student jobs" showing 20 clicks and 0 conv), the kill-switch rule applies — add an emergency negative. Log it. Otherwise, hands off.

### Baseline report at day 7

Write `.planning/phases/08-gbp-ads-citations/ads-baseline-day7.md` with:
- Overall 30-day performance summary
- Top 10 converting search terms (if any conversions)
- Top 10 zero-converting high-click search terms (candidates for negatives)
- Existing negative keyword coverage — what's missing for family law
- Existing ad copy — Cal Bar 7.1 issues (any "specialist", "guaranteed", "best")
- Landing page audit — are ads pointing at Justia, homepage, or a practice page? If Justia, all clicks are 404-ing post-cutover — highest priority fix.

Only AFTER this report is written do we start Step 4.

---

## Step 4 — Family-law negative keyword list (ADS-04)

Locked master list. Applied to every family-law-intent campaign.

### Category 1 — Free / DIY / self-service intent (buyer is NOT hiring an attorney)
- `free`
- `free consultation` (unless Burkett changes his no-free-consult policy)
- `free legal advice`
- `DIY`
- `do it yourself`
- `pro se`
- `pro-se`
- `represent myself`
- `represent yourself`
- `self help`
- `self-help`
- `self represent`
- `court forms`
- `download form`
- `form template`
- `legalzoom`
- `rocket lawyer`
- `nolo`

### Category 2 — Wrong practice area (family law only)
- `criminal`
- `criminal defense`
- `DUI`
- `personal injury`
- `car accident`
- `motorcycle accident`
- `slip and fall`
- `wrongful death`
- `immigration`
- `visa`
- `green card`
- `deportation`
- `bankruptcy`
- `chapter 7`
- `chapter 13`
- `estate planning`
- `will`
- `trust`
- `probate` (except guardianship — Burkett handles Probate Code guardianship)
- `real estate`
- `landlord tenant`
- `employment`
- `workers comp`
- `workers compensation`

### Category 3 — Educational / research intent (not converting)
- `law student`
- `paralegal`
- `legal secretary`
- `law school`
- `law degree`
- `bar exam`
- `wikipedia`
- `legal aid`  (Burkett is private-pay, legal aid users don't convert)
- `pro bono`  (same reason)
- `sliding scale`
- `low income`

### Category 4 — Jobs / career
- `jobs`
- `hiring`
- `career`
- `salary`
- `job description`
- `attorney jobs`
- `paralegal jobs`
- `internship`

### Category 5 — Wrong geography (Burkett is San Diego County only)
- `los angeles`
- `LA county`
- `orange county`
- `riverside`
- `san bernardino`
- `arizona`
- `nevada`
- `mexico`
- `tijuana`

Do NOT negative-out "north county" or "south bay" or SD sub-region names — those are Burkett's serve area.

### Category 6 — Publisher / directory / rating sites
- `avvo`
- `justia`  (post-cutover — his OWN Justia URL is going away, don't pay to click to it)
- `findlaw`
- `lawyers.com`
- `superlawyers`
- `martindale`
- `yelp`
- `reddit`
- `quora`

### Match type strategy

Per the 2026-06-12 Echo Local negative-match-type fix: **broad negatives leak**. Use **phrase match** for all of these. If a term shows up in a search-terms report as EXACT (e.g., "wix" cost $15.88 because exact-match negative didn't block "wix com"), convert to phrase.

Recommended: apply ALL of the above as **phrase negatives** at the shared negative-keyword list level, then attach the list to all campaigns.

### Applying the list

1. Google Ads → Tools & Settings → Shared library → Negative keyword lists → **Create list** → name: `Burkett Family Law Master Negatives` → paste all keywords with **phrase** as the match type indicator.
2. Attach to every campaign: Campaigns → select each → Settings → Negative keywords → Attach list.

---

## Step 5 — Landing page routing (ADS-06)

**Rule**: Ads never land on the homepage. Every ad lands on the specific practice pillar or location page that matches the intent.

### Ad group → landing page map

| Ad group / Intent | Landing page |
|-------------------|-------------|
| Divorce San Diego | `/practice-areas/divorce/` |
| Divorce lawyer Mission Valley | `/san-diego/divorce-attorney/mission-valley/` (if exists) OR pillar |
| Divorce lawyer North County | `/san-diego/divorce-attorney/vista/` OR closest city |
| Child custody San Diego | `/practice-areas/child-custody/` |
| Child support San Diego | `/practice-areas/child-support/` |
| Spousal support / alimony | `/practice-areas/spousal-support/` |
| Domestic violence restraining order | `/practice-areas/domestic-violence/` |
| Family law mediation San Diego | `/practice-areas/mediation/` |
| Guardianship attorney San Diego | `/practice-areas/guardianship/` |
| Emergency family law (urgent DVRO, ex parte) | `/practice-areas/domestic-violence/` (has urgency framing) |
| Brand: "brian burkett attorney" | `/about.html` (E-E-A-T anchor, direct-brand landing) |

### Conversion tracking on landing pages

Every landing page above already has (from Phase 6):
- `phone_click` event on tel: links
- `form_submit` event on `/thanks/` load
- `calendar_book` event on GHL widget postMessage

Post-Phase-8 conversion action creation → the placeholder `AW-BURKETTAWXXX0/*` IDs in `assets/js/analytics.js` get sed-swapped for real IDs. See `.planning/phases/06-technical-seo/GoogleAds-conversions.md` Phase 8 swap section.

---

## Step 6 — Existing campaign audit (ADS-05)

**Rule**: do NOT wholesale-rebuild. Wholesale rebuild resets Quality Score history, which raises CPC 20-40% for weeks. Preserve existing campaigns; add negatives, adjust match types, swap landing pages, edit ad copy — but do NOT delete and recreate.

### Audit each existing campaign

For each campaign that Rankaroo/Clientomics created (visible after Step 1 access):

| Check | If found | Action |
|-------|----------|--------|
| Landing page is Justia URL | Yes | HIGH PRIORITY — swap to new site page per Step 5 map. Post-cutover, Justia URLs 404. |
| Landing page is site homepage | Yes | Swap to specific practice pillar per Step 5 (intent match improves QS + CVR). |
| Ad copy contains "specialist," "expert," "best," "guaranteed" | Yes | Cal Bar 7.1 violation. Rewrite. |
| Ad copy contains testimonials without disclaimer | Yes | Cal Bar 7.1 violation. Remove testimonials in ad copy (only site has disclaimer bandwidth). |
| Broad-match keywords with 0 conversions and >20 clicks | Yes | Convert to phrase match OR pause. |
| No negative keyword list attached | Yes | Attach the master list from Step 4. |
| Bidding strategy = Maximize Conversions with no cap | Yes | Add a max CPC cap (family law CPC can run $30-50 in SD; cap at $40 to prevent runaway spend). |
| Daily budget vs 30-day spend | Yes | If budget is set to $30 but spend spikes to $80 on catch-up pacing → per 2026-06-23 Echo Local rule, this triggers false kill-switches. Confirm budget is set intentionally. |

### Kill-switch rule

Per Burkett-specific tuning: kill-switch fires at **2.5× daily budget in a rolling 24h window**. NOT the $38 flat threshold Echo Local uses (Echo Local's threshold was too low for the $16-20 daily budgets and kept auto-pausing).

For Burkett, if daily budget = $50, kill-switch = $125/day. If daily budget = $100, kill-switch = $250/day.

Implementation: Google Ads Automated Rules → Campaign level → "Pause campaign when daily cost > $X." Set the X per campaign.

---

## Step 7 — Post-swap conversion swap (from Phase 6 doc)

Once the real Google Ads AW conversion actions are created (Step 2 + Step 5's follow-up actions for form_submit + phone_click + calendar_book), swap the placeholders in the site's analytics:

```bash
cd /Users/brianegan/Desktop/burkett-law

# Placeholder → real value (fill after creating the actions)
FORM_SEND="AW-<CUSTOMER_ID>/<FORM_LABEL>"
PHONE_SEND="AW-<CUSTOMER_ID>/<PHONE_LABEL>"
CAL_SEND="AW-<CUSTOMER_ID>/<CAL_LABEL>"

grep -rl "AW-BURKETTAWXXX0/FORMSUBMITXX" . --include='*.html' --include='*.js' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/FORMSUBMITXX|${FORM_SEND}|g"

grep -rl "AW-BURKETTAWXXX0/PHONECLICKXX" . --include='*.html' --include='*.js' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/PHONECLICKXX|${PHONE_SEND}|g"

grep -rl "AW-BURKETTAWXXX0/CALBOOKXX" . --include='*.html' --include='*.js' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/CALBOOKXX|${CAL_SEND}|g"

# Sanity: no placeholders left
grep -r "AW-BURKETTAWXXX0" . --include='*.html' --include='*.js'  # should return 0 hits

# Run validators (identity guard etc.) before commit
bash scripts/run_all_validators.sh

git add -A
git -c user.email=bwegan77@gmail.com -c user.name="Brian Egan" \
    commit -m "phase 8: swap AW conversion placeholders for real Google Ads IDs"
git push
```

Also update Google Ads → Tools → Conversions → each action → Tag setup verified.

---

## Step 8 — Cancel prior vendors (Rankaroo / Clientomics / Justia)

**Only after** baseline captured (Step 3) AND access confirmed (Step 1) AND AD_CALL is recording (Step 2).

Sequence:
1. Confirm baseline captured (`ads-baseline-day0.json` and `ads-baseline-day7.md` both exist).
2. Confirm AD_CALL has ≥1 recorded call in a 24h window.
3. Confirm at least one Burkett-managed campaign edit has completed successfully (negatives applied + landing pages fixed).
4. Then Burkett cancels Rankaroo/Clientomics/Justia billing.

**Do NOT let Burkett cancel before step 3.** Losing Justia access before we have Justia's referrer/GA data captured loses irreplaceable history.

---

## Rollback plan

If ANY Burkett-side campaign edit degrades performance measurably (day-over-day CTR drop >30%, cost/conv rise >2×), rollback:
1. Google Ads → History → find the edit → Revert.
2. If revert not possible, restore from Editor CSV backup of pre-edit state (Google Ads Editor → Backup).
3. Log the rollback + reason in `.planning/phases/08-gbp-ads-citations/ads-changelog.md`.

**Do NOT panic on day-1 or day-2 dips.** Quality Score reindexes after edits; wait 5-7 days before treating a dip as real.

---

## Verification checklist

- [ ] Google Ads access confirmed (MCC link or user-add) with Admin permissions
- [ ] AD_CALL conversion action created (min 30s, primary, Recording)
- [ ] `ads-baseline-day0.json` captured before any edits
- [ ] 7 days of observation logged
- [ ] `ads-baseline-day7.md` written
- [ ] Master negative keyword list created (Categories 1-6 all included)
- [ ] Master negative list attached to every family-law-intent campaign
- [ ] Every ad group's landing page routed per Step 5 map (no Justia URLs, no bare homepage)
- [ ] Existing ad copy audited for Cal Bar 7.1 violations, offending ads paused or rewritten
- [ ] Kill-switch rules set at 2.5× daily budget per campaign
- [ ] AW conversion placeholders sed-swapped for real IDs
- [ ] `grep AW-BURKETTAWXXX0` returns 0 hits
- [ ] Rankaroo/Clientomics/Justia cancellation triggered ONLY after baseline + AD_CALL + first successful edit
- [ ] Rollback plan documented in this file

---

## Reference: Echo Local ads-lockdown script pattern

The pattern to follow when the takeover moves from planning to execution is `~/EchoLocalClientTracker/scripts/echo_local_ads_lockdown_2026_06_07.py`. It uses:
- `google-ads` Python library
- MCC login as manager
- Idempotent operations: check-then-create
- Structured logging (change, from, to, timestamp)
- Dry-run mode via `--dry-run` flag

Adapt for Burkett:
- `scripts/burkett_ads_lockdown.py` (create when executing)
- Customer ID = Burkett's (env var `BURKETT_ADS_CID`)
- Login CID = MCC `935-051-0225`
- Negatives from Step 4 as a Python constant
- Landing-page swap map from Step 5 as a Python constant
- Kill-switch rule from Step 6 injected via automated_rules API (or manual via UI — API path is fiddly)

Ship this script when Burkett's access lands; do not build now (nothing to test against).
