# DNS Records for Cutover

**Domain**: `childcustodyanddivorce.com`
**Registrar**: Network Solutions
**Target**: Netlify site `burkett-law` (site_id `69d38c3a-fcb7-4424-877e-df9fcd884e71`)
**Custom domain status**: ADDED on Netlify side 2026-07-08 (waiting for DNS to point).

The Netlify custom-domain slot is already configured with:
- `custom_domain: childcustodyanddivorce.com`
- `domain_aliases: [www.childcustodyanddivorce.com]`

Once these DNS records land, Netlify auto-provisions a Let's Encrypt certificate (usually within 5-60 minutes; wildcard covers both apex and www). No manual cert action needed on Netlify.

---

## Records Burkett Must Add at Network Solutions

Log in at https://www.networksolutions.com/manage-it/index.jsp then Domains → `childcustodyanddivorce.com` → **DNS / Advanced DNS**.

### 1. Apex (`childcustodyanddivorce.com`)

**Preferred (if Network Solutions supports ALIAS/ANAME on apex — most modern registrars do; Network Solutions historically does NOT expose an ALIAS type in their UI. So plan on option B by default.)**

- **Option A — ALIAS / ANAME (only if the UI has this row type):**
  - Type: `ALIAS` or `ANAME`
  - Host: `@` (or leave blank / "root")
  - Target: `apex-loadbalancer.netlify.com`
  - TTL: `300` (5 min) for cutover; restore to `3600` at T+72h

- **Option B — A records (Network Solutions default; use this):**
  - Type: `A`
  - Host: `@` (or leave blank / "root")
  - Target: `75.2.60.5`
  - TTL: `300`

  Netlify's shared apex load balancer resolves to `75.2.60.5` (documented Netlify public IP). If Network Solutions requires more than one A record, add a second: `99.83.190.102` (Netlify AWS backup pool). One A record is sufficient for correctness; two adds redundancy.

### 2. WWW subdomain (`www.childcustodyanddivorce.com`)

- Type: `CNAME`
- Host: `www`
- Target: `burkett-law.netlify.app` (final `.` if the UI requires FQDN)
- TTL: `300`

### 3. Google Search Console DNS TXT verification

At T-14 Brian pulls the verification TXT token from Google Search Console UI (Add Property → Domain → copy the `google-site-verification=...` string).

- Type: `TXT`
- Host: `@` (root)
- Value: `google-site-verification=<TOKEN_FROM_GSC>` (paste the whole string exactly, no quotes needed — Network Solutions wraps it automatically)
- TTL: `3600` (this record is permanent; keep it forever so GSC stays verified through any future DNS moves)

### 4. Email MX records — DO NOT TOUCH

If `childcustodyanddivorce.com` currently receives email (check Network Solutions for existing MX records), **leave every MX record and any related SPF/DKIM/DMARC TXT records exactly as they are**. This cutover only affects web traffic. Confirm with Burkett before touching anything besides A / AAAA / CNAME / GSC-TXT.

---

## Records to REMOVE at cutover

Whatever A / AAAA / CNAME records currently point the apex or www at Justia. Typical Justia DNS pattern:
- Apex A: `<Justia IP>` — **DELETE**
- www CNAME: `<something>.justia.com` — **DELETE**

Only delete the Justia web-serving records. Do not touch MX or TXT.

---

## Verification Commands (post-DNS-change)

Run these from a shell after DNS is updated. Use two different resolvers to confirm propagation is not stale-cache.

```bash
# Apex resolves to Netlify
dig +short A childcustodyanddivorce.com @1.1.1.1
dig +short A childcustodyanddivorce.com @8.8.8.8
# Expected: 75.2.60.5 (or Netlify range 75.2.60.0/24, 99.83.190.0/24)

# www resolves to Netlify hostname
dig +short CNAME www.childcustodyanddivorce.com @1.1.1.1
dig +short CNAME www.childcustodyanddivorce.com @8.8.8.8
# Expected: burkett-law.netlify.app.

# GSC verification TXT present
dig +short TXT childcustodyanddivorce.com @1.1.1.1 | grep google-site-verification
# Expected: the verification string

# HTTPS cert live
curl -I https://childcustodyanddivorce.com
# Expected: HTTP/2 200, valid Let's Encrypt cert
```

---

## Rollback Plan

If cutover reveals a critical issue in the first hour, restore the previous A/CNAME records at Network Solutions. Because TTL was lowered to 300s at T-14, the world sees the rollback within ~5 minutes. Justia stays live through 2026-07-31, so the fallback surface is intact until then. After 2026-07-31 Justia is gone — do not attempt a cutover-then-rollback after that date; commit to Netlify.
