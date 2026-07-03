---
phase: 01-foundation-design-system-validators
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - netlify.toml
  - _headers
  - _redirects
  - robots.txt
  - sitemap.xml
  - llms.txt
  - index.html
  - .well-known/security.txt
  - .gitignore
  - README.md
files_created:
  - netlify.toml
  - _headers
  - _redirects
  - robots.txt
  - sitemap.xml
  - llms.txt
  - index.html
  - .well-known/security.txt
  - .gitignore
  - README.md
autonomous: false
requirements: [FND-01, FND-02, FND-03, FND-09]
user_setup:
  - service: GitHub
    why: "Create empty repo EchoLocalagency/burkett-law and grant Netlify OAuth access"
    dashboard_config:
      - task: "Create empty public repo EchoLocalagency/burkett-law (no README, no license — repo is bootstrapped from local)"
        location: "https://github.com/organizations/EchoLocalagency/repositories/new"
  - service: Netlify
    why: "Create Netlify site connected to burkett-law repo for auto-deploy"
    dashboard_config:
      - task: "Import EchoLocalagency/burkett-law to Netlify; set publish directory to '/' (site root); production branch = main"
        location: "https://app.netlify.com/start"
      - task: "Verify auto-deploy webhook is active (Deploys tab shows most recent commit within 5 minutes of push)"
        location: "https://app.netlify.com/sites/burkett-law/deploys"

must_haves:
  truths:
    - "git push to EchoLocalagency/burkett-law triggers a Netlify auto-deploy that succeeds"
    - "Netlify preview URL serves index.html with warm palette (navy #12294A, cream #FBF8F3, gold #B45309) visible"
    - "curl -I on internal .html link on the deployed site preserves the .html (pretty_urls disabled)"
    - "curl -I on deployed page returns Strict-Transport-Security, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, Content-Security-Policy headers"
    - "robots.txt explicitly Allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended and references sitemap URL"
  artifacts:
    - path: "netlify.toml"
      provides: "pretty_urls=false + build config"
      contains: "pretty_urls = false"
    - path: "_headers"
      provides: "HSTS + CSP + X-Frame-Options + Referrer-Policy + Permissions-Policy"
      contains: "Strict-Transport-Security"
    - path: "_redirects"
      provides: "Redirect scaffold (empty of real rules, comment header explaining Justia map lands in Phase 6)"
    - path: "robots.txt"
      provides: "Allow-all + explicit AI crawler allows + sitemap reference"
      contains: "Sitemap: https://childcustodyanddivorce.com/sitemap.xml"
    - path: "sitemap.xml"
      provides: "Sitemap scaffold with homepage only for now"
      contains: "<urlset"
    - path: "llms.txt"
      provides: "LLM discovery scaffold with site title + description + top-page placeholder list"
    - path: "index.html"
      provides: "Placeholder homepage proving palette + auto-deploy pipeline"
      contains: "#12294A"
    - path: ".well-known/security.txt"
      provides: "Contact email + expires date for security disclosures"
  key_links:
    - from: "netlify.toml"
      to: "Netlify build system"
      via: "pretty_urls=false directive under [build.processing.html]"
      pattern: "pretty_urls\\s*=\\s*false"
    - from: "GitHub main branch"
      to: "Netlify auto-deploy"
      via: "OAuth webhook wired at Netlify site import"
    - from: "robots.txt"
      to: "sitemap.xml"
      via: "Sitemap: https://childcustodyanddivorce.com/sitemap.xml line"
---

<objective>
Bootstrap the Burkett family law repo. Create the Netlify + deploy infrastructure (netlify.toml with pretty_urls=false, _headers with the full security header set, _redirects scaffold), the crawler/discovery files (robots.txt, sitemap.xml, llms.txt, security.txt), and a placeholder homepage proving the design palette and the git push → Netlify auto-deploy loop is working end-to-end.

Purpose: Every downstream plan assumes a working deploy pipeline and the pretty_urls=false setting. SoCal/Ecosystem/Mr Green all hit the deindex bug when this was missed — this plan lands it on the first commit so it can never regress. Security headers ship day 1 so YMYL trust signals are present from launch.

Output: Repo skeleton pushed to EchoLocalagency/burkett-law, Netlify site auto-deploying, verifiable preview URL with palette + security headers.
</objective>

<execution_context>
@/Users/brianegan/.claude/get-shit-done/workflows/execute-plan.md
@/Users/brianegan/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md
@/Users/brianegan/Desktop/burkett-law/.planning/ROADMAP.md
@/Users/brianegan/Desktop/burkett-law/.planning/STATE.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/STACK.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/PITFALLS.md
@/Users/brianegan/CLAUDE.md

<interfaces>
<!-- Key configuration contracts consumed by later plans. Extracted from research files. -->

Palette (from research/DESIGN.md §1):
- Navy: #12294A (ink-800) — header, footer, primary text
- Cream: #FBF8F3 (cream-50) — page background
- Gold: #B45309 (gold-600) — CTA, accents

netlify.toml required stanza (from STACK.md + PITFALLS.md Pitfall 10):
```toml
[build]
  publish = "."

[build.processing.html]
  pretty_urls = false
```

_headers required entries (from STACK.md YMYL Technical Signals + PITFALLS.md Security Mistakes):
```
/*
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: interest-cohort=(), geolocation=(), microphone=(), camera=()
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self' https://www.google-analytics.com; frame-src 'self' https://api.leadconnectorhq.com https://msgsndr.com
```

robots.txt required stanza (from STACK.md Sitemap section):
```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://childcustodyanddivorce.com/sitemap.xml
```
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Create Netlify infra + crawler scaffolds at repo root</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/netlify.toml,
    /Users/brianegan/Desktop/burkett-law/_headers,
    /Users/brianegan/Desktop/burkett-law/_redirects,
    /Users/brianegan/Desktop/burkett-law/robots.txt,
    /Users/brianegan/Desktop/burkett-law/sitemap.xml,
    /Users/brianegan/Desktop/burkett-law/llms.txt,
    /Users/brianegan/Desktop/burkett-law/.well-known/security.txt,
    /Users/brianegan/Desktop/burkett-law/.gitignore,
    /Users/brianegan/Desktop/burkett-law/README.md
  </files>
  <action>
Create all root-level configuration files. Use the interfaces block above verbatim for netlify.toml, _headers, and robots.txt sections.

netlify.toml: [build] publish = "." + [build.processing.html] pretty_urls = false. Also add [build.environment] NODE_VERSION = "20" as a defensive baseline. NOTHING else — no plugins, no build command (site is static).

_headers: Use the /* stanza from the interfaces block. Do NOT weaken CSP. frame-src allowlist includes GHL calendar iframe domains (api.leadconnectorhq.com, msgsndr.com) — these will be used in Phase 2. If a domain is later missing, Phase 2 loosens it there — do not preemptively add other domains here.

_redirects: Create with a comment-only header block explaining "Justia URL 301 map lands in Phase 6 (Technical SEO). Add www→apex canonical decision here at Phase 7 T-14. Do not add wildcard rules that catch new URLs (PITFALLS.md Pitfall 10)." No actual rules yet.

robots.txt: Use the interfaces block stanza exactly.

sitemap.xml: XML declaration + urlset with a SINGLE url entry for the homepage (https://childcustodyanddivorce.com/) with <lastmod>2026-07-03</lastmod>. Do NOT include priority or changefreq (Google ignores per STACK.md). Sitemap is scaffold — Phase 6 automates additions.

llms.txt: Follow llmstxt.org 2026 standard:
```
# Law Office of Brian Burkett — San Diego Family Law

> Solo family law attorney in San Diego (Mission Valley) — divorce, child custody, child support, spousal support, mediation, domestic violence, guardianship, family court. Serving San Diego County.

## Overview
- Attorney: Brian Burkett
- Office: 591 Camino De La Reina, Suite 821, San Diego, CA 92108
- Phone: (619) 250-2683
- Practice: California family law, San Diego Superior Court

## Key Pages
- [Homepage](https://childcustodyanddivorce.com/): Firm overview and how to reach the office
- [About Brian Burkett](https://childcustodyanddivorce.com/attorney-bio/): Bar admission, credentials, experience (Phase 2)
- [Practice Areas](https://childcustodyanddivorce.com/practice-areas/): The eight practice pillars (Phase 3)
- [Contact](https://childcustodyanddivorce.com/contact/): Address, hours, contact form (Phase 2)
```
(Phase 5 fills in real blog post index; keep the scaffold small.)

.well-known/security.txt (create the .well-known dir if not present):
```
Contact: mailto:brian@echolocalagency.com
Expires: 2027-07-03T00:00:00.000Z
Preferred-Languages: en
Canonical: https://childcustodyanddivorce.com/.well-known/security.txt
```

.gitignore: Ignore .DS_Store, node_modules/, .netlify/, .env, .env.local, *.log, .idea/, .vscode/.

README.md: One-paragraph description + link to .planning/PROJECT.md. Do NOT add any marketing copy — this repo is public and README.md is not the marketing surface. Just: "Static site for the Law Office of Brian Burkett (childcustodyanddivorce.com). See .planning/PROJECT.md for full context. Deploy via git push (Netlify auto-deploys). Never run `netlify deploy` per CLAUDE.md."

CRITICAL rules:
- Do NOT delete or modify the existing .planning/ directory or .git/ directory.
- Do NOT create index.html here — it lands in Task 2 so it stays a single file change on this task.
- Do NOT touch any files outside the burkett-law repo root.
  </action>
  <verify>
    <automated>cd /Users/brianegan/Desktop/burkett-law && grep -q 'pretty_urls = false' netlify.toml && grep -q 'Strict-Transport-Security' _headers && grep -q 'GPTBot' robots.txt && grep -q 'ClaudeBot' robots.txt && grep -q 'childcustodyanddivorce.com/sitemap.xml' robots.txt && test -f _redirects && test -f sitemap.xml && test -f llms.txt && test -f .well-known/security.txt && test -f .gitignore && test -f README.md && echo "PASS"</automated>
  </verify>
  <done>All 9 files exist at correct paths, netlify.toml contains pretty_urls=false, _headers contains all six required security header directives, robots.txt allows AI crawlers + references sitemap, sitemap.xml is valid XML, llms.txt has the site overview scaffold, security.txt has contact + expires. Zero files outside /Users/brianegan/Desktop/burkett-law/ modified.</done>
</task>

<task type="auto">
  <name>Task 2: Placeholder homepage + initial commit + GitHub push</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/index.html
  </files>
  <action>
Create a MINIMAL placeholder index.html that proves (a) the deploy pipeline is live and (b) the palette is correctly wired. NOT the real homepage — Phase 2 replaces this entirely.

Structure:
- `<!doctype html>` + `<html lang="en-US">`
- `<head>` with: `<meta charset="utf-8">`, viewport, `<title>Law Office of Brian Burkett — San Diego Family Law</title>`, meta description ("Placeholder — full site launches before 2026-07-31."), inline `<style>` block using the exact palette from DESIGN.md.
- `<body>` with a single `<main>` containing an `<h1>Law Office of Brian Burkett</h1>`, a subhead paragraph "San Diego family law — site coming soon. Please call (619) 250-2683.", and a `tel:` link.

Inline styles use these exact hex values so the palette is visually verifiable on the Netlify preview:
- body: background #FBF8F3 (cream-50), color #0B1F3A (ink-900), font-family: system-ui, sans-serif (real font ships in Plan 02)
- main: max-width 640px, margin: 4rem auto, padding: 2rem
- h1: color #12294A (ink-800), font-size: 2.5rem
- a[href^="tel:"]: display inline-block, background #B45309 (gold-600), color #FBF8F3, padding: 0.75rem 1.5rem, border-radius: 8px, text-decoration: none, margin-top: 1rem

Do NOT add nav, footer, GA4, or schema in this placeholder. Phase 2 builds the full homepage. This is deploy-pipeline proof only.

After files exist:
1. Run `cd /Users/brianegan/Desktop/burkett-law && git add netlify.toml _headers _redirects robots.txt sitemap.xml llms.txt index.html .well-known/security.txt .gitignore README.md`
2. Run `git status` — verify staged files, no unwanted extras.
3. Run `git commit -m "feat(01-01): bootstrap Netlify infra + placeholder homepage" -m "" -m "Ships netlify.toml (pretty_urls=false — SoCal/Ecosystem deindex bug prevention), _headers (HSTS+CSP+X-Frame-Options+Referrer-Policy+Permissions-Policy for YMYL trust), _redirects scaffold, robots.txt (explicit AI crawler allows), sitemap.xml, llms.txt, security.txt, and a placeholder index.html proving the palette is live. Phase 2 replaces index.html with the real homepage."`
4. Verify remote via `git remote -v`. If no remote named `origin` exists, print INSTRUCTIONS for Brian: create empty repo at https://github.com/organizations/EchoLocalagency/repositories/new named `burkett-law`, then `git remote add origin git@github.com:EchoLocalagency/burkett-law.git && git push -u origin main`. Then PAUSE at the checkpoint task (Task 3) — do NOT push here.
5. If remote DOES exist, run `git push -u origin main` and report the Netlify preview URL that should activate within ~90 seconds.
  </action>
  <verify>
    <automated>cd /Users/brianegan/Desktop/burkett-law && test -f index.html && grep -q '#FBF8F3' index.html && grep -q '#12294A' index.html && grep -q '#B45309' index.html && grep -q 'tel:6192502683\|tel:+16192502683' index.html && git log --oneline -1 | grep -q '01-01' && echo "PASS"</automated>
  </verify>
  <done>index.html renders with cream background + navy heading + gold CTA button visible on the Netlify preview URL; git commit for phase 01-01 exists; either pushed to origin OR clear instructions logged for Brian to create the GitHub repo.</done>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <what-built>Repo scaffold pushed to GitHub, Netlify site created + linked to repo, first auto-deploy served the placeholder homepage. This checkpoint verifies the end-to-end pipeline works BEFORE Phase 2 starts building on it — same class of check that would have caught the Chef Dorothy 84-day silent-deploy-break bug at day 1 instead of day 84.</what-built>
  <how-to-verify>
1. Open https://github.com/EchoLocalagency/burkett-law — confirm the commit is visible and files include netlify.toml, _headers, robots.txt, sitemap.xml, llms.txt, index.html, .well-known/security.txt.
2. Open Netlify dashboard: https://app.netlify.com/sites/burkett-law/deploys — confirm the most recent deploy is "Published" (green), NOT queued/failed.
3. Open the Netlify preview URL (something like https://burkett-law.netlify.app or https://<random>.netlify.app) — confirm:
   - Page background is warm cream (not white)
   - Heading "Law Office of Brian Burkett" is navy (not black)
   - "Call (619) 250-2683" is a gold pill button
4. On the preview URL, in browser devtools Network tab, click the top HTML request and inspect Response Headers. Confirm ALL SIX headers present:
   - `strict-transport-security`
   - `x-content-type-options: nosniff`
   - `x-frame-options: DENY`
   - `referrer-policy: strict-origin-when-cross-origin`
   - `permissions-policy: interest-cohort=()`
   - `content-security-policy: default-src 'self'`
5. Fetch the preview URL's robots.txt in the browser — confirm it contains "User-agent: GPTBot" and "Sitemap:" line.
6. Fetch the preview URL's sitemap.xml — confirm it parses as XML (no browser error page).
7. In Netlify Site settings → Build & deploy → Continuous deployment, confirm "Deploy Log" shows the most recent commit hash and status "Published within last 5 min of push."

If ALL 7 checks pass, type "approved". If any fail, describe which and the observed vs expected values.
  </how-to-verify>
  <resume-signal>Type "approved" to unblock Phase 2 planning, or describe specific issues (e.g. "CSP header missing X" or "deploy failed with error Y") for targeted fix.</resume-signal>
</task>

</tasks>

<verification>
Phase 1 Plan 01 verification (post-checkpoint):
- `git log --oneline` shows commit "feat(01-01): bootstrap Netlify infra + placeholder homepage"
- Netlify site auto-deployed on push — deploy status "Published"
- `curl -sI $NETLIFY_PREVIEW_URL | grep -iE 'strict-transport|content-security|x-frame|x-content-type|referrer-policy|permissions-policy'` returns all 6
- `curl -s $NETLIFY_PREVIEW_URL/robots.txt | grep -c 'GPTBot\|ClaudeBot\|PerplexityBot\|Google-Extended'` returns 4
- `grep 'pretty_urls' netlify.toml` returns `pretty_urls = false`
- No emojis in any file (grep --include='*.html' --include='*.toml' --include='*.txt' -rE '[\U0001F300-\U0001FAFF]' .)
</verification>

<success_criteria>
- git push to EchoLocalagency/burkett-law triggers a successful Netlify auto-deploy at a Netlify preview URL
- Homepage renders with the locked palette (navy #12294A + cream #FBF8F3 + gold #B45309)
- Netlify serves security headers (HSTS + CSP + X-Frame-Options + X-Content-Type-Options + Referrer-Policy + Permissions-Policy)
- netlify.toml pins pretty_urls=false at repo root
- robots.txt + sitemap.xml + llms.txt + security.txt scaffold in place
- Human confirmed via checkpoint that the deploy pipeline is live and headers present
</success_criteria>

<output>
After completion, create `.planning/phases/01-foundation-design-system-validators/01-01-SUMMARY.md` recording:
- The Netlify site URL (preview + custom domain if set)
- The initial commit SHA
- Any deviations from CSP frame-src (if GHL domain adjustment needed later)
- The .well-known/security.txt contact and expires date (so Phase 6 can renew)
</output>
