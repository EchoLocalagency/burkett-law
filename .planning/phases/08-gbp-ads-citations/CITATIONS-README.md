# BrightLocal Citation Upload — Law Office of Brian Burkett

**Requirement coverage**: CIT-01
**Type**: Human-execution manual + CSV.
**File to upload**: `burkett-brightlocal-citations.csv` (same directory)

---

## What this is

BrightLocal is the citation-building service Echo Local uses to submit the same NAP (Name, Address, Phone) to 60+ business directories — Yelp, Yellow Pages, BBB, Justia (the directory, not the site host), Avvo, Findlaw, Cortera, etc. Consistent citations across those directories reinforce Google's confidence in the business's identity and geography, which lifts local-pack ranking.

For Burkett, we ship one CSV row with character-identical NAP to the sitewide source of truth, plus the 750-char description + practice-area services + hours + payment types. Brian uploads this to BrightLocal → BrightLocal submits to its directory network → we watch for citation live-checks over the following 2-4 weeks.

---

## Pre-upload checklist for Brian

### 1. Fill the Business Category ID
The CSV ships with `FILL_BRIGHTLOCAL_ATTORNEY_CATEGORY_ID` as the placeholder in the `Business Category ID` column. BrightLocal's category picker uses numeric IDs (Georgia's psychic was `1267`).

Fetch the correct ID:
- Log into BrightLocal → New citation campaign → search category "Family Law Attorney" or "Attorney" → copy the ID displayed next to it.
- If BrightLocal offers both "Attorney" (generic) AND "Family Law Attorney" (specific), pick the specific — matches Burkett's GBP primary.
- Replace `FILL_BRIGHTLOCAL_ATTORNEY_CATEGORY_ID` in the CSV.

### 2. Confirm NAP integrity
The CSV NAP MUST match:
- GBP listing exactly (post-Step-2-4 of GBP-SETUP.md)
- Site footer + contact.html + LocalBusiness schema exactly
- `scripts/content_facts.md` exactly
- `scripts/clients.json` → `phone_display` + `address_full` exactly

If any of these drift AFTER the CSV is uploaded, BrightLocal will submit stale data — worst case, we get inconsistent citations back. Rule: only upload after Phase 7 cutover confirmed live AND GBP-SETUP.md Step 4 (address) + Step 5 (phone) + Step 6 (hours) are locked.

### 3. Confirm hours (blocked-on-Burkett)
CSV currently ships with `Mon-Fri 9:00 am - 6:00 pm` (matching `content_facts.md` default assumption). If Burkett confirms different hours, update:
- The CSV (Monday Start Time through Sunday End Time columns)
- The site footer + contact.html
- `content_facts.md` + `clients.json`

Don't upload before hours are confirmed — updating citations after the fact requires paid "update" credits.

### 4. Confirm photos
CSV ships with:
- Logo: `https://childcustodyanddivorce.com/assets/img/logo.svg`
- Photo 1: `https://childcustodyanddivorce.com/assets/img/brian-burkett-headshot.jpg`

Both URLs must return 200 AT the time BrightLocal fetches them for submission. Verify with:
```bash
curl -sIL https://childcustodyanddivorce.com/assets/img/logo.svg | head -5
curl -sIL https://childcustodyanddivorce.com/assets/img/brian-burkett-headshot.jpg | head -5
```

Only upload after cutover confirms the site is live and the images are served.

### 5. Verify description is Cal Bar 7.1 clean
Short and long descriptions in the CSV are content — subject to Cal Bar Rule 7.1. Run the lint against the CSV descriptions if paranoid:
```bash
# Copy the description text to a scratch file and lint it
echo "The Law Office of Brian Burkett is a solo family-law practice..." > /tmp/burkett-description.txt
cd /Users/brianegan/Desktop/burkett-law
python scripts/lint_cal_bar.py /tmp/burkett-description.txt
```

Current descriptions have been checked: no "specialist," "expert," "guaranteed," "best," "our team," no invented case counts. Should pass.

---

## Upload sequence

1. Log into BrightLocal (Brian's Echo Local account).
2. Add new client campaign → `Law Office of Brian Burkett` → San Diego.
3. Choose "Citation Builder" (60+ directories) as the service.
4. Import CSV → select `burkett-brightlocal-citations.csv`.
5. Preview parsed data → confirm all fields render correctly (spot-check NAP + description + services + hours).
6. Confirm submission budget + credits.
7. Submit.

BrightLocal will begin submitting to its directory network within 24-48h. Full submission typically completes in 2-4 weeks. Track progress in BrightLocal → Reports → Citation Builder → Burkett.

---

## Post-upload verification

At weeks 2, 4, 6 after upload, spot-check 10 major directories manually:

Priority directories to verify (Google reads these):
- Yelp
- Yellow Pages
- BBB (Better Business Bureau)
- Findlaw (attorney-specific)
- Justia directory (the directory listing, not Burkett's old Justia website)
- Avvo
- Superlawyers
- Cortera
- Manta
- Foursquare

For each: search "Law Office of Brian Burkett San Diego" → find the listing → verify NAP matches character-identical. Flag any drift.

---

## Reference — CSV field mapping decisions

| Column | Value | Reason |
|--------|-------|--------|
| Client Reference | BURKETT001 | Echo Local's internal client ID pattern |
| Location Name | Law Office of Brian Burkett | Legal name — matches GBP + LocalBusiness schema |
| Location ID | (blank) | Assigned by BrightLocal on import |
| Unique Location Reference | law-office-brian-burkett-sd | Slug-style unique key for reference |
| Website URL | https://childcustodyanddivorce.com/ | Target domain (post-cutover) |
| Business Category ID | FILL — Brian fills before upload | BrightLocal numeric ID for Attorney or Family Law Attorney |
| Country | USA | Standard |
| Address 1 | 591 Camino De La Reina, Suite 821 | Character-identical NAP |
| State/County/Region | CA | Standard |
| Town/City | San Diego | Standard |
| Postcode/Zip | 92108 | Mission Valley zip |
| Telephone | 619-250-2683 | Character-identical (BrightLocal uses XXX-XXX-XXXX format; the site uses (619) 250-2683 which is the same digits) |
| Contact First/Last | Brian / Burkett | Real attorney name |
| Contact Email | attorneyburkett@sbcglobal.net | Real email — used for citation notifications |
| Number of Employees | 1 | Solo practitioner |
| Date of Company Formation | 01-2002 | Bar admission year (proxy for practice founding — Burkett has been in solo practice since admission per Justia archive) |
| Extra Business Categories | (blank) | GBP has secondary categories; BrightLocal single-category is fine per BrightLocal's own guidance |
| Hours Mon-Fri | 9:00 am - 6:00 pm | From content_facts.md default assumption (confirm with Burkett before upload) |
| Hours Sat/Sun | (blank) | Closed weekends unless Burkett confirms otherwise |
| Payment Types | Visa, MC, AmEx, Personal Check, Invoice, ATM/Debit, Discover | Standard for attorney — no PayPal (client trust accounts), no Cash (Cal Bar risk on cash retainers) |
| Short Description | 261 chars | Under BrightLocal's short-desc typical 300-char limit |
| Full Description | ~890 chars | Under BrightLocal's full-desc typical 1500-char limit |
| Service 1-5 | Divorce / Child Custody / Child Support / Spousal Support / Family Law Mediation | Top 5 practice pillars (BrightLocal only takes 5) — DVRO/guardianship/family-court in the long description |
| Is Service Area Business | No | Storefront — clients visit 591 Camino De La Reina |
| Language | English | Standard |
| Logo URL / Photo URL 1 | Live site URLs | Must be reachable at upload time |

---

## Failure modes to watch for

1. **Broken image URL on upload** — BrightLocal fetches the image; if the site isn't live yet, the fetch fails and BrightLocal submits without image. Don't upload before Phase 7 cutover confirms live.
2. **Category ID mismatch** — If Brian pastes the wrong numeric ID (e.g., grabs "Divorce Lawyer" instead of "Family Law Attorney"), directories may miscategorize. Verify the ID renders "Family Law Attorney" in BrightLocal's preview before submitting.
3. **Duplicate listing suppression** — Some directories already have a Justia-created listing for Burkett. BrightLocal may either flag as duplicate (good — merge) or create a second entry (bad — duplicate suppression by Google). Monitor BrightLocal's dedupe report; manually merge dupes on Yelp, BBB, Yellow Pages.
4. **NAP drift after upload** — If GBP is edited AFTER BrightLocal submits, the citations across the directory network stay stale. Wait until GBP is locked in Phase 8 before running BrightLocal. If drift happens later, "update citations" is a separate paid product on BrightLocal.
