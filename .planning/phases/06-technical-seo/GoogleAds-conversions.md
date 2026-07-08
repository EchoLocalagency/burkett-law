# Google Ads AW Conversion Actions — Wire-Up

## Status
Every page fires three GA4 events that are also stubbed to fire a
Google Ads `conversion` event with placeholder `send_to` values:

| Event | Fires on | AW placeholder send_to |
|-------|----------|----------------------|
| `form_submit` | `thanks.html` load | `AW-BURKETTAWXXX0/FORMSUBMITXX` |
| `phone_click` | Any `<a href="tel:…">` click | `AW-BURKETTAWXXX0/PHONECLICKXX` |
| `calendar_book` | GHL calendar embed postMessage | `AW-BURKETTAWXXX0/CALBOOKXX` |

The `AW-BURKETTAWXXX0` prefix is a placeholder. Google Ads silently drops
conversion events with an unknown ID, so the wire is safe to ship as-is
— nothing spurious lands in a real account, and the swap at Phase 8
requires only `sed`.

## Why deferred to Phase 8
- Burkett's Google Ads account access is still being handed off from
  Rankaroo. Cancelling Rankaroo access before the 7-day baseline
  observation window (per the 2026-06-23 rule) would lose the CPC / CTR
  / negative-keyword history.
- Even with access, creating AW conversion actions before the site is
  live at `childcustodyanddivorce.com` would fire against Justia and
  attribute Justia's traffic to Burkett — the wrong signal.
- Phase 8 handles: (1) MCC link OR user-add to Burkett's account,
  (2) 7-day observation, (3) AW conversion action creation, (4) sed
  swap of the placeholder into the real IDs.

## Phase 8 — Creating the AW conversion actions

Once Google Ads account access is confirmed:

1. Google Ads → Tools & Settings → Measurement → Conversions → **New conversion action** → Website.
2. Do NOT let it auto-detect. Choose **Add a conversion action manually**.
3. Create three actions:

### Action 1: Form Submit
- Goal category: Submit lead form
- Conversion name: `Form Submit`
- Value: $200 (proxy — one qualified lead)
- Count: One
- Click-through window: 30 days
- View-through window: 1 day
- Attribution model: Data-driven
- Enhanced conversions: ON (email + phone from form)

### Action 2: Phone Click (from ads)
- Goal category: Contact
- Conversion name: `Phone Click`
- Value: $150
- Count: One (dedupe per session)

Note: This is a *page click* on a tel: link, not an *ad phone-forwarding*
conversion. Different action from `Calls from Ads` (Echo Local's account
uses that for the account-level phone number). Keep them separate — do
not merge.

### Action 3: Calendar Book
- Goal category: Book appointment
- Conversion name: `Calendar Book`
- Value: $250 (higher intent than a form)
- Count: One

## Phase 8 — Swap the placeholders

After each action is created, Google Ads shows a `Google tag` panel with
the `send_to` value in the form `AW-<CustomerID>/<ConversionLabel>`.
Copy the three values, then:

```bash
cd /Users/brianegan/Desktop/burkett-law

# Replace each placeholder with the real send_to value.
FORM_SEND="AW-XXXXXXXXXX/YYYYYYYYYY"
PHONE_SEND="AW-XXXXXXXXXX/ZZZZZZZZZZ"
CAL_SEND="AW-XXXXXXXXXX/WWWWWWWWWW"

grep -r -l "AW-BURKETTAWXXX0/FORMSUBMITXX" . --include='*.html' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/FORMSUBMITXX|${FORM_SEND}|g"

grep -r -l "AW-BURKETTAWXXX0/PHONECLICKXX" . --include='*.html' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/PHONECLICKXX|${PHONE_SEND}|g"

grep -r -l "AW-BURKETTAWXXX0/CALBOOKXX" . --include='*.html' \
  | xargs sed -i '' "s|AW-BURKETTAWXXX0/CALBOOKXX|${CAL_SEND}|g"

# Sanity: nothing left with the placeholder.
grep -r "AW-BURKETTAWXXX0" . --include='*.html'  # should return 0 hits

# Commit + push.
git add -A
git -c user.email=bwegan77@gmail.com -c user.name="Brian Egan" commit -m "phase 8: swap AW conversion placeholders for real Google Ads IDs"
git push
```

## Verify

Google Ads → Tools → Conversions → each action shows **Recording**
within an hour of a real conversion event firing. If it stays on **No
recent conversions**, DevTools → Network → filter `googleadservices`
and check the request payload for the correct `send_to`.

## Cross-attribution: Google Ads ↔ GA4
Once GA4 is created and Google Ads is linked, GA4 will show the same
events under Reports → Realtime → Conversions. Do NOT enable
"Import GA4 conversions" into Google Ads while native AW events are
also firing — that double-counts. Native AW events beat imported GA4
conversions on data quality.
