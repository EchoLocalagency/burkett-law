# Google Search Console — Domain Verification

## Status
**Not verified yet.** Verification requires a DNS TXT record on
`childcustodyanddivorce.com`, and the domain still points at Justia
Hosting (Network Solutions is the registrar; Justia controls the DNS
zone). This gets done at Phase 7 T-14 as part of the DNS-and-nameserver
cutover, not before, because Justia's DNS provider won't let Brian add
TXT records without pulling the nameservers first.

## Why DNS TXT (not HTML tag or GA)
- **Domain-property verification** in GSC survives subdomain changes,
  HTTPS/HTTP switches, and Netlify redeploys. HTML-tag and GA4 methods
  are URL-prefix-only and each variant (`http://`, `https://`,
  `www.`, apex) is a separate property. Domain-property = one place to
  watch, and the TXT verification persists forever.
- **Justia deindex risk**: at cutover, Google's crawler sees an entirely
  new IP + new content. If the domain-property verification is already
  in place before DNS switches, GSC keeps its historical Coverage +
  Performance data attached to the same property rather than treating
  the cutover as a brand-new site.

## Step 1 — Get the TXT record value (Brian, 1 min)

1. Go to https://search.google.com/search-console (log in as brian@echolocalagency.com).
2. Click **Add property** (top-left dropdown).
3. Choose **Domain** (not URL prefix).
4. Enter: `childcustodyanddivorce.com`
5. Click **Continue**.
6. Google shows a TXT record value like:
   ```
   google-site-verification=<64-char-string>
   ```
7. Copy that value.

## Step 2 — Add TXT to Network Solutions DNS (Phase 7 T-14, coordinated with DNS cutover)

At T-14, the Network Solutions DNS zone gets rewritten to point A/AAAA
at Netlify. **Add the TXT record in the same session**:

- **Type**: TXT
- **Host / Name**: `@` (root — some registrars use `_google-site-verification` but Google's domain-property uses the root)
- **Value**: `google-site-verification=<the-string-from-step-1>`
- **TTL**: 300s (matches the general TTL drop at T-14)

## Step 3 — Verify (T-14 + 15 min)

DNS propagates fast on a fresh zone. Confirm with:

```bash
dig +short TXT childcustodyanddivorce.com @1.1.1.1
dig +short TXT childcustodyanddivorce.com @8.8.8.8
```

Both should return the `google-site-verification=…` string. Once it
resolves, go back to GSC → click **Verify**. GSC will confirm.

## Step 4 — Post-verification actions

Once verified:
1. Submit the sitemap: GSC → Sitemaps → add `sitemap.xml` (relative
   path — GSC auto-resolves to `https://childcustodyanddivorce.com/sitemap.xml`).
2. Submit the top 5 canonical URLs for indexing:
   - `https://childcustodyanddivorce.com/`
   - `https://childcustodyanddivorce.com/about.html`
   - `https://childcustodyanddivorce.com/practice-areas/`
   - `https://childcustodyanddivorce.com/practice-areas/divorce/`
   - `https://childcustodyanddivorce.com/blog/`
3. Enable **email alerts** on Coverage errors + Manual actions.
4. Cross-link the property to the Google Ads account (Google Ads →
   Tools → Linked accounts → GSC).

## Keep the record forever
Never delete the TXT record. Losing verification silently drops
Coverage + Performance history if Google re-verifies later, and every
subsequent access requires re-adding the TXT.
