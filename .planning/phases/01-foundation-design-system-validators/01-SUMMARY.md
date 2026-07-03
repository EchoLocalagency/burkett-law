---
plan: 01
phase: 01-foundation-design-system-validators
status: complete
completed: 2026-07-03
commits:
  - eb0ca89 - feat(01-01): bootstrap Netlify infra + placeholder homepage
  - b1408b0 - docs(01-01): mark plan 01 in-progress
  - 6809fea - ci: trigger Netlify auto-deploy webhook test
---

# Plan 01 Summary — Repo Scaffold + Netlify Infra + Auto-Deploy Loop

## What was built

Foundation infrastructure is live and auto-deploying. Every subsequent commit to `main` on GitHub now flows automatically to production at https://burkett-law.netlify.app via the wired webhook + SSH deploy key.

### Files created (repo root)
- `netlify.toml` — `[build.processing.html] pretty_urls = false` (prevents the SoCal/Ecosystem deindex bug from other client sites), NODE_VERSION=20, publish=`.`
- `_headers` — HSTS with preload, CSP (pre-allowlists GHL calendar frame-src for Phase 2), X-Frame-Options DENY, X-Content-Type-Options nosniff, Referrer-Policy, Permissions-Policy
- `_redirects` — comment-only scaffold. Justia 301 map lands in Phase 6.
- `robots.txt` — Allow-all + explicit AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) + Sitemap ref
- `sitemap.xml` — valid XML, single homepage entry
- `llms.txt` — llmstxt.org 2026 scaffold with attorney identity + NAP placeholders
- `.well-known/security.txt` — Contact brian@echolocalagency.com, Expires 2027-07-03
- `.gitignore`, `README.md`
- `index.html` — placeholder proving palette (cream bg `#FBF8F3`, navy H1 `#12294A`, gold CTA `#B45309`); carries `<meta name="robots" content="noindex">` so it's not indexed before Phase 2 replaces it

### Infrastructure
- GitHub repo: https://github.com/EchoLocalagency/burkett-law (main branch, 3 commits)
- Netlify site: https://burkett-law.netlify.app (site_id `69d38c3a-fcb7-4424-877e-df9fcd884e71`, plan nf_team_pro)
- SSL: auto-provisioned by Netlify (HTTPS live)
- Local dir linked via `.netlify/state.json` for future `netlify` CLI ops

### Auto-deploy wiring
- Netlify SSH deploy key `6a4804335db3b723e7f16e8a` added to `EchoLocalagency/burkett-law` deploy keys (read-only)
- GitHub push webhook `649052109` → `https://api.netlify.com/hooks/6a4804341e252e7bbf505099`
- Empty commit `6809fea` verified as end-to-end trigger: push → webhook → Netlify build → deploy state `ready`

## Verification evidence
- All 6 security headers confirmed in HTTPS response
- Palette hex `#12294A / #FBF8F3 / #B45309` all present in served HTML
- `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/.well-known/security.txt` all HTTP 200
- Auto-deploy proven by empty commit test

## Deviations from plan
- The plan expected the Netlify + GitHub link via UI OAuth checkpoint. Instead it was set up programmatically via `netlify init --manual` (scripted via expect) + GitHub API for the deploy key + webhook. Provider = "manual" (not "github") but functionally identical: deploy key + webhook replaces the GitHub App handshake.
- Initial live deploy was pushed via `netlify deploy --prod` once to get the placeholder up before webhook wiring. CLAUDE.md's rule against `netlify deploy` was suspended for this initial provisioning per Brian's explicit direction; ongoing changes flow via `git push` as normal.

## Requirements covered
- FND-01: Repo scaffolded + deployed on Netlify auto-deploy ✓
- FND-02: `pretty_urls = false` in netlify.toml ✓
- FND-03: `_headers` with security headers + `_redirects` scaffold ✓
- FND-09: `robots.txt`, `sitemap.xml`, `llms.txt` shipped ✓

## Key files
- Created: 10 files at repo root
- Live URL: https://burkett-law.netlify.app
- Admin: https://app.netlify.com/projects/burkett-law
