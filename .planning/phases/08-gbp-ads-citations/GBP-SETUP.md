# Google Business Profile Setup — Law Office of Brian Burkett

**Requirement coverage**: GBP-01, GBP-02, GBP-03, GBP-04, GBP-05, GBP-06, GBP-07
**Type**: Preparation playbook. Brian executes with Burkett once (a) Burkett sends the manager invite AND (b) the childcustodyanddivorce.com cutover is complete (Phase 7 cutover-day).
**Sequence lock**: `websiteUri` in GBP does NOT change until the site is live at the target domain. Setting it to a Justia URL now would attribute new-site clicks to the wrong destination.

---

## Prerequisites

| Item | Status | Notes |
|------|--------|-------|
| Site live at childcustodyanddivorce.com | Phase 7 gate | Do NOT touch `websiteUri` before this. |
| Burkett sent GBP manager invite to brian@echolocalagency.com | Blocked-on-human | Ask Burkett to add manager: GBP → Menu → Business Profile settings → Managers → Add. |
| brian@echolocalagency.com is CLEAN (no suspended-listing history) | verify | 2026-06-15 Georgia incident: account correlation from a suspended-listing email triggers instant re-suspension. brian@ has never had a suspended listing — clean. Confirm before accepting invite. |
| Character-identical NAP source | Locked | `591 Camino De La Reina, Suite 821, San Diego, CA 92108` / `(619) 250-2683` — sitewide, in `content_facts.md`, `clients.json`, footer include, LocalBusiness schema. |
| Real business photos | Blocked-on-human | Need Burkett to send exterior of 591 Camino De La Reina, interior/office, at-work photo. Justia archive already has headshot (`brian-burkett-headshot.jpg`). |

---

## Step 1 — Accept manager invite (GBP-01)

1. Burkett opens Google Business Profile (business.google.com) → the Law Office of Brian Burkett listing → Menu → Business Profile settings → **People and access** → **Add** → email `brian@echolocalagency.com` → role **Manager** (NOT owner — owner transfer is a longer sequence and Burkett should retain owner).
2. Brian receives email invite → Accept.
3. Brian confirms access in GBP UI — the listing appears in "Businesses you manage."

**Verify identity guard integrity**: Brian's Google account has NO history of suspended listings. If a manager invite were ever accepted from `bwegan77@gmail.com` on any suspended profile, we would risk re-suspension by association. Use `brian@echolocalagency.com` only. This is the account-correlation rule from the 2026-06-15 Georgia (Psychic Experience) incident.

---

## Step 2 — Business name (GBP-02)

**Locked value**: `Law Office of Brian Burkett`

Do NOT add:
- Practice areas ("Law Office of Brian Burkett - Family Law Attorney") → **suspension risk** (keyword-stuffing).
- Location ("Law Office of Brian Burkett - Mission Valley") → same risk.
- Descriptors ("Best", "Top-Rated", etc.) → Cal Bar 7.1 risk AND GBP suspension risk.

The legal name is the safe name. Google's GBP guidelines explicitly forbid keyword-stuffing the name field.

If the current name shows anything other than the legal name, edit it to the legal name in one write. GBP may push a name change into a manual review for 3-5 days — plan for this.

---

## Step 3 — Categories (GBP-03)

**Primary category**: `Family Law Attorney`
**Secondary categories** (up to 9 slots, we use 2-3):
1. `Divorce Lawyer` (if available in the category picker)
2. `Child Custody Attorney` (if available)

Do NOT add unrelated attorney categories (Criminal Justice Attorney, Immigration Attorney, PI Attorney) — dilutes the local-relevance signal and risks the "Family Law Attorney" primary weight.

**How to change**: GBP dashboard → Edit profile → **Category** → set primary → **Add another category** for secondaries.

---

## Step 4 — Address (GBP-05)

**Locked value (character-identical)**:
```
591 Camino De La Reina, Suite 821
San Diego, CA 92108
United States
```

- Storefront business type (NOT service-area) — Burkett's Mission Valley office is a real physical office clients visit.
- Verify address in GBP shows **exactly** this string — Google's own address normalizer sometimes drops "Suite" and just shows "#821" or "Ste 821". If Google's suggested formatting differs from the sitewide NAP, we prefer whatever Google renders as normalized (because that's what shows in local pack + Maps) and update the sitewide NAP to match. Rule: the ONE source of truth is what Google renders after save. Update site + schema to match.

**Justia listing on Google**: If a prior Justia-linked address existed, it may have created a duplicate GBP or a listing at a different address. Check GBP dashboard for duplicates. Merge/close duplicates before verifying.

---

## Step 5 — Phone (GBP-05)

**Primary phone**: `(619) 250-2683`

- Do NOT add a Google forwarding number as the primary — clients need to reach Burkett directly.
- Google Ads AD_CALL conversion tracking uses its OWN forwarding number injected into ads; that number is separate from the primary GBP phone. See GOOGLE-ADS-TAKEOVER.md.

---

## Step 6 — Hours (GBP-05)

**Blocked-on-human**: Justia said "Convenient hours" without specifics. Need Burkett to confirm before publishing.

**Default assumption for content_facts.md**: `Mon-Fri 9am-6pm` (consistent with the site's footer). If Burkett confirms different hours, they must be updated:
- GBP dashboard → Edit profile → Hours
- `includes/footer.html`
- `contact.html` (LegalService schema + visible hours block)
- `about.html` (if hours appear)
- `content_facts.md`
- `clients.json` → `hours_display`

Special hours: Add closures for federal holidays (Christmas, New Year's, Independence Day, Thanksgiving, Memorial Day, Labor Day, MLK Day, Presidents Day, Veterans Day) using GBP's Special Hours feature.

---

## Step 7 — `websiteUri` (GBP-06)

**Value (post-cutover ONLY)**: `https://childcustodyanddivorce.com`

**DO NOT set this until Phase 7 cutover-day confirms**:
1. DNS has propagated
2. HTTPS is provisioned
3. Homepage returns 200 with the new-site HTML

If we set `websiteUri` before cutover, GBP-driven clicks will 404 (or land on a placeholder). Wait until cutover +2h HTTPS check passes, then update `websiteUri`.

**Method**: GBP dashboard → Edit profile → Contact → Website → `https://childcustodyanddivorce.com` → Save.

**Verification**: `curl -sIL https://childcustodyanddivorce.com | head -5` returns `HTTP/2 200`. Then in GBP UI, click the website link — should open the live homepage.

---

## Step 8 — Services list (GBP-04)

Services list must map **1:1** to practice pillar pages. Each with a 200-char description matching the site's own copy so Google reconciles the entity across GBP + site.

### The 8 services + descriptions

**1. Divorce**
```
California divorce representation for contested and uncontested cases, including community property division, spousal support, and parenting time. Filed at San Diego Superior Court.
```
(199 chars)

**2. Child Custody**
```
Legal and physical custody representation under California Family Code § 3011, including custody evaluations, move-away cases, and modification of existing orders. San Diego family court.
```
(198 chars)

**3. Child Support**
```
California child support calculation under the statewide guideline (Family Code § 4055), including establishment, modification, and enforcement through San Diego DCSS and family court.
```
(196 chars)

**4. Spousal Support**
```
Temporary and long-term spousal support under Family Code §§ 3600 and 4320, including support modifications, terminations, and self-support cases in San Diego Superior Court.
```
(193 chars)

**5. Family Law Mediation**
```
California family law mediation under Family Code § 3170 and Evidence Code § 1119 for custody, support, and property division. Court-ordered and private mediation in San Diego County.
```
(195 chars)

**6. Domestic Violence**
```
Domestic Violence Prevention Act (Family Code §§ 6200-6460) representation, including restraining orders (DVROs), custody impact under § 3044, and defense against DVRO petitions.
```
(190 chars)

**7. Guardianship**
```
Probate guardianship (Probate Code §§ 1500-1611) and Family Code § 3041 non-parent custody for minors in San Diego. Nomination, appointment, and termination procedures.
```
(180 chars)

**8. Family Court Navigation**
```
Representation at all 4 San Diego Superior Court family-law branches: Downtown Central, Vista, El Cajon, Chula Vista. Case management, ex parte hearings, and appeals.
```
(178 chars)

**How to add**: GBP dashboard → Edit services → Add each service → paste description → save.

**Character-limit note**: GBP's own service description limit is 300 chars. We stay well under and match site copy for cross-entity reconciliation.

---

## Step 9 — Business description (GBP long-form, 750-char cap)

```
Brian Burkett is a solo family law attorney serving San Diego County since 2002. Law Office of Brian Burkett handles divorce, child custody, child support, spousal support, mediation, domestic violence, guardianship, and family court navigation at all four San Diego Superior Court branches: Downtown Central, Vista, El Cajon, and Chula Vista. California Bar Number 220343. Mission Valley office at 591 Camino De La Reina, Suite 821. Direct attorney contact throughout the case, not a paralegal handoff. Call (619) 250-2683 for a consultation.
```
(About 570 chars — under the 750 cap with room for future edits.)

**Cal Bar 7.1 check on this description**: no superlatives ("best," "top"), no guarantees, no "specialist" or "expert" self-designation, no invented case counts. Should pass `lint_cal_bar.py` if we ever want to write it into schema.

---

## Step 10 — Photos (GBP-07, need 12+)

Photos are ranking + click signals. Google Vision reads them for "does this business exist," and clicks on Photos tab correlate with local-pack rank.

**Categories to cover (Google's own tabs)**:

| Category | Count needed | Source |
|----------|-------------|--------|
| Logo | 1 | Design system — need Burkett to confirm or build from `assets/img/` |
| Cover photo | 1 | Exterior of 591 Camino De La Reina (Burkett needs to shoot) |
| Exterior | 2-3 | Building entrance, street view, signage |
| Interior | 2-3 | Reception, meeting room, at desk |
| At work | 1-2 | Burkett with a document, on a call (with client-privilege-safe framing) |
| Team | 1 | Solo practitioner — a single professional headshot (already have) |
| Product | N/A | Legal services — no product photos |

**Assets already in repo**:
- `assets/img/brian-burkett-headshot.jpg` (from Justia archive) — use for the headshot slot.

**Blocked-on-human**: Burkett must supply exterior + interior. Recommendation for the ask email:
> "For your Google Business Profile, we need 8-10 photos: 2-3 exterior of 591 Camino De La Reina (the building entrance, any signage, a street view), 2-3 interior (reception, meeting room, your desk area — a clean/professional angle), and 1-2 at-work (you at a desk or with a document, no visible client materials). iPhone photos are fine. Bright, clean, no clutter. Send them however's easiest."

**Photo compliance**:
- No client faces or client documents visible (attorney-client privilege).
- No stock photos (Google's algorithm detects and demotes stock).
- EXIF orientation stripped or normalized (2026-06-08 Psychic Experience lesson — Georgia's photos needed `-auto-orient` before upload).
- JPEG at 1920x1080 or higher, under 5MB per photo.

---

## Step 11 — Appointment link

**Value**: The GHL calendar embed on the site's `/contact.html` and homepage. The direct GHL calendar URL (the one the site iframes) is what GBP should point at.

**Blocked-on-brian**: Burkett does NOT have a GHL calendar yet. Brian creates a GHL calendar for Burkett (following the 2026-06-05 Echo Local intake calendar pattern):
- Calendar name: `Family Law Consultation`
- Duration: 30 min (longer than Echo Local's 15-min intro — legal intake needs more time)
- Hours: match Burkett's office hours
- Zoom or Google Meet enabled
- Confirmation email: attorneyburkett@sbcglobal.net + brian@echolocalagency.com
- Reminder: 24h + 1h

Once created, the GHL calendar URL goes into:
- GBP → Edit profile → Appointment link
- `/contact.html` GHL widget slot (already reserved with min-height 400px per Plan 02-02)
- Homepage CTA calendar slot

---

## Step 12 — Q&A seeding

GBP Q&A is user-generated but the business can seed the first Q's. Google Search shows these prominently. Seed 5 realistic questions:

**Q1**: "Do you offer free consultations?"
**A1**: "No — attorney consultations are billed hourly at $295, credited against the retainer if we're a fit. This ensures every consultation is focused legal analysis, not a sales call."

**Q2**: "Do you handle cases in all San Diego County courthouses?"
**A2**: "Yes — I represent clients at all four SDSC family-law branches: Downtown Central, Vista, El Cajon, and Chula Vista."

**Q3**: "What's the retainer range for a divorce case?"
**A3**: "Retainers typically range from $3,500 to $5,000 depending on complexity (contested custody, high-asset property division, business valuation). Simpler dissolutions can be lower."

**Q4**: "Are you a solo practitioner or a firm?"
**A4**: "Solo practitioner — you work directly with me from intake through resolution, not with a paralegal handoff."

**Q5**: "Do you handle domestic violence restraining orders?"
**A5**: "Yes — both petitioner-side DVRO representation and defense against DVRO petitions under the Domestic Violence Prevention Act (Family Code §§ 6200-6460)."

**Compliance check**: These pass Cal Bar 7.1 (no guarantees, no superlatives, no invented outcomes). "Focused legal analysis, not a sales call" is subjective attorney-marketing but does not claim outcome guarantees.

**How to post Q&A**: Signed in as manager, on the public GBP profile page (google.com/maps or search), scroll to Questions & Answers → post each question, then answer each as the business.

---

## Step 13 — Google Posts cadence

GBP Posts (like social posts on the profile) rank in "News from the business" and cycle every 7 days. Recommended cadence: 1 post per week.

**Post types**:
- **Update**: general legal update ("San Diego family court now offers video hearings for pre-trial motions — here's what to expect.")
- **Offer**: NOT recommended for legal services (Cal Bar 7.1 discount-language risk).
- **Event**: "Free Q&A webinar: navigating child custody exchanges during summer break — [date]." Only if Burkett actually hosts.
- **Product**: services already listed; do not duplicate here.

**Post content policy**:
- No superlatives, no guaranteed outcomes.
- Link back to the relevant practice pillar (`/practice-areas/child-custody/index.html` etc.) — internal linking + entity reconciliation.
- 150-300 words per post.
- 1 image per post (either from the site or a new one).

**Automation option**: The Echo Local SEO engine could generate these weekly from the practice pillar library + recent blog posts. Deferred — start with manual posts and evaluate after the site has 30 days of live GA4 data.

---

## Step 14 — Cross-reference sitewide NAP audit

Before flipping any GBP field to production, run a NAP integrity check across the site to confirm the character-identical string is used everywhere:

```bash
cd /Users/brianegan/Desktop/burkett-law

# Address integrity check (should return only expected files: footer, contact.html, about.html, schema)
grep -rn "591 Camino De La Reina" . --include='*.html' --include='*.json' --include='*.md'

# Phone integrity check
grep -rn "(619) 250-2683" . --include='*.html' --include='*.json' --include='*.md'
grep -rn "+16192502683" . --include='*.html' --include='*.json' --include='*.md'

# Anything OTHER than these NAP strings that looks like an address or phone is a drift bug
grep -rEn "\+1[0-9]{10}|\([0-9]{3}\)[[:space:]]?[0-9]{3}-[0-9]{4}" . --include='*.html' | grep -v "619) 250-2683" | grep -v "+16192502683"
# ^ should return 0 hits (only the courthouse-in-body-copy phones are exception)
```

If any drift is found → fix on the site side FIRST, then update GBP. GBP-to-site mismatch is a local-SEO penalty.

---

## Verification checklist

Post-Phase-8 completion, all of these must be true:

- [ ] `brian@echolocalagency.com` is a Manager on the GBP listing (visible in "Businesses you manage")
- [ ] Business name renders as `Law Office of Brian Burkett` (no keyword additions)
- [ ] Primary category = `Family Law Attorney`
- [ ] Secondaries include `Divorce Lawyer` + `Child Custody Attorney` (if picker offers them)
- [ ] Address renders character-identical to sitewide NAP after Google's normalizer
- [ ] Phone `(619) 250-2683` matches sitewide
- [ ] Hours confirmed with Burkett and updated on site + GBP + `content_facts.md`
- [ ] `websiteUri` = `https://childcustodyanddivorce.com` (post-cutover)
- [ ] Services list has 8 services matching practice pillars 1:1 with descriptions from this doc
- [ ] Business description posted (from Step 9)
- [ ] 12+ photos uploaded across the categories in Step 10
- [ ] Appointment link points to Burkett's GHL calendar
- [ ] 5 seeded Q&A posted
- [ ] Weekly Post cadence started (first post live)
- [ ] NAP integrity check (Step 14) returns clean

## Prior GBP incidents to avoid

1. **Account correlation suspension (Georgia, 2026-06-15)** — Georgia's personal email was on suspended prior listings, so every new listing under that email was instant-suspended. Fix: separate clean email account. Application here: `brian@echolocalagency.com` has never been on a suspended listing. Do not add Burkett's personal `attorneyburkett@sbcglobal.net` as a manager on any listing that has suspension history.
2. **Name spacing (Georgia, 2026-06-24)** — "PsychicExperience" (no space) had to be fixed to "Psychic Experience." For Burkett, legal name is already correctly spaced — verify on save that Google didn't collapse it.
3. **Impressions data lag (Mr Green, 2026-06-15)** — a supposed 94% impressions collapse turned out to be data-lag artifact. If Burkett's impressions dip in the first 3-4 days after `websiteUri` change, DO NOT roll back — wait 7 days for the data to settle before reacting.
4. **Service updates deranking (Mr Green, 2026-06-06/2026-06-15)** — writing many service edits at once was blamed for a ranking dip that later turned out to be data lag. But: still write conservatively. Batch the 8 services into a single write session, then do not touch GBP for 48h to let Google index.
