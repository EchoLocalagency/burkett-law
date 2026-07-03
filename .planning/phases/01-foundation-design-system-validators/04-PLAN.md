---
phase: 01-foundation-design-system-validators
plan: 04
type: execute
wave: 3
depends_on: [02, 03]
files_modified:
  - assets/css/header.css
  - assets/css/footer.css
  - assets/js/nav.js
  - includes/header.html
  - includes/footer.html
  - templates/base.html
autonomous: false
requirements: [FND-07, FND-08]

must_haves:
  truths:
    - "Phone link uses E.164 format `tel:+16192502683` per PITFALLS.md UX guidance (Rule: broken tel: on international dialers) — supersedes literal FND-08 wording `tel:6192502683` and the ROADMAP success-criterion wording. Display form `(619) 250-2683` unchanged."
    - "Universal header renders on a copy of templates/base.html with logo, 4-item nav (Home, Practice Areas, About, Blog, Contact — wait, 5 including logo=home; 4-item nav per FND-08 = Practice Areas / About / Blog / Contact), a gold phone chip linking to tel:+16192502683, and a mobile hamburger toggle"
    - "Universal footer renders with the character-identical NAP '591 Camino De La Reina, Suite 821, San Diego, CA 92108' and phone '(619) 250-2683', hours, four columns (Firm / Practice Areas / Firm links / Credentials), a Cal Bar Rule 7.1 disclaimer band, and copyright"
    - "Footer disclaimer contains 'This website is attorney advertising', 'Information on this site is not legal advice', 'Contacting the Law Office of Brian Burkett does not create an attorney-client relationship', 'Past results do not guarantee a similar outcome', 'Licensed in California only'"
    - "Header + footer HTML pass all three validators (Cal Bar lint, fabrication, identity guard) with zero violations"
    - "Mobile nav drawer opens on hamburger click, closes on Escape, focus trap works, and skip-link still first tab stop"
  artifacts:
    - path: "includes/header.html"
      provides: "Universal header HTML fragment — every page copies this into <header role=banner>"
      contains: "tel:+16192502683"
    - path: "includes/footer.html"
      provides: "Universal footer HTML fragment — every page copies this into <footer role=contentinfo>"
      contains: "591 Camino De La Reina, Suite 821, San Diego, CA 92108"
    - path: "assets/css/header.css"
      provides: "Header component styles (sticky navy, 72px desktop / 64px mobile, gold phone chip pill, hover states, mobile drawer)"
      min_lines: 80
    - path: "assets/css/footer.css"
      provides: "Footer component styles (navy bg, 4-column grid → 2 tablet → 1 mobile, disclaimer band, copyright)"
      min_lines: 60
    - path: "assets/js/nav.js"
      provides: "Vanilla-JS mobile hamburger toggle + Escape-to-close + focus trap"
      min_lines: 40
    - path: "templates/base.html"
      provides: "Updated to include header.css + footer.css links and inline the includes/header.html + includes/footer.html content in banner/contentinfo landmarks"
      contains: "header.css"
  key_links:
    - from: "templates/base.html"
      to: "includes/header.html + includes/footer.html"
      via: "Hand-inlined into <header>/<footer> landmarks (manual copy — no build system)"
    - from: "includes/header.html"
      to: "assets/js/nav.js"
      via: "<script defer src>"
      pattern: "nav.js"
    - from: "includes/footer.html"
      to: "privacy.html + terms.html + disclaimer.html"
      via: "<a href> in footer legal-links column"
      pattern: "privacy.html"
---

<objective>
Ship the universal header and footer that every page on the site consumes. Header = sticky navy bar with logo, 4-item nav, and a gold phone chip. Footer = 4-column info block with character-identical NAP, hours, and the Cal Bar Rule 7.1 sitewide disclaimer band. Base template is updated so a future page just copies the base.html and gets header + footer for free.

Purpose: Every page on the site (bio, homepage, practice pillars, location pages, blog posts, contact, legal) needs a consistent header + footer. Character-identical NAP is a hard GBP + BrightLocal trust signal (any drift = local penalty per PITFALLS.md Pitfall 9). The Cal Bar Rule 7.1 sitewide disclaimer is a legal requirement, not a nice-to-have. Ship both here so Phase 2 (bio + homepage + contact) doesn't invent its own.

Output: Two HTML include fragments, two CSS component files, a tiny nav.js for the mobile drawer, and an updated base.html template that already has header + footer wired.
</objective>

<execution_context>
@/Users/brianegan/.claude/get-shit-done/workflows/execute-plan.md
@/Users/brianegan/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/DESIGN.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/ARCHITECTURE.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/PITFALLS.md
@/Users/brianegan/Desktop/burkett-law/.planning/phases/01-foundation-design-system-validators/02-PLAN.md
@/Users/brianegan/Desktop/burkett-law/.planning/phases/01-foundation-design-system-validators/03-PLAN.md

<interfaces>
<!-- Canonical NAP (character-identical everywhere, per PITFALLS.md Pitfall 9) -->

Brand: "Law Office of Brian Burkett"
Address (one line, format-locked): "591 Camino De La Reina, Suite 821, San Diego, CA 92108"
Phone tel: "+16192502683" (E.164 — never spaces or parens per PITFALLS.md UX)
Phone display: "(619) 250-2683"
Email: (from clients.json — TBD at Phase 2; footer uses office phone for now)
Hours display: "Mon-Fri 9am-6pm"

Nav items (4 per FND-08, per ARCHITECTURE.md IA — logo→home doesn't count as a nav item):
- "Practice Areas" → /practice-areas/
- "About"          → /attorney-bio/
- "Blog"           → /blog/
- "Contact"        → /contact/

Practice pillars (for footer column, 8 links per DESIGN.md §6.5):
- Divorce → /practice-areas/divorce/
- Child Custody → /practice-areas/child-custody/
- Child Support → /practice-areas/child-support/
- Spousal Support → /practice-areas/spousal-support/
- Mediation → /practice-areas/mediation/
- Domestic Violence → /practice-areas/domestic-violence/
- Guardianship → /practice-areas/guardianship/
- Family Court → /practice-areas/family-court/

Cal Bar Rule 7.1 sitewide disclaimer text (from DESIGN.md §6.5 + PITFALLS.md Pitfall 3):
"This website is attorney advertising. Information on this site is not legal advice. Contacting the Law Office of Brian Burkett does not create an attorney-client relationship. Past results do not guarantee a similar outcome. Licensed in California only."

Header behavior (DESIGN.md §6.4):
- 72px desktop, 64px mobile height
- Sticky top with backdrop-blur after 40px scroll
- Ink-800 background, cream-50 text
- Logo left: Fraunces 600 22px "BURKETT" + gold divider + smaller "family law"
- 4 nav links right (desktop): Inter 500 15px, cream-50 at 80% opacity, hover = 100% + gold-500 underline
- Gold pill phone chip far right: `gold-100` bg + `ink-900` text + phone icon + display number
- Mobile: hamburger button left of phone chip; menu drawer slides from top

Footer behavior (DESIGN.md §6.5):
- ink-800 background, cream-50 text
- 4-column grid desktop / 2-column tablet / 1-column mobile
- Column 1 (Firm): wordmark, address, tel:, hours
- Column 2 (Practice Areas): 8 links
- Column 3 (Firm links): About, Blog, Contact, Privacy, Terms, Disclaimer
- Column 4 (Credentials): "Licensed in California only", CA State Bar profile link (placeholder — bar number Phase 2), SD County Bar Assoc mention (if member — placeholder)
- Full-width disclaimer band above copyright: ink-900 bg, cream-50 at 70% opacity, italic, caption size
- Copyright: "© 2026 Law Office of Brian Burkett"
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Header component (include + CSS + nav.js)</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/includes/header.html,
    /Users/brianegan/Desktop/burkett-law/assets/css/header.css,
    /Users/brianegan/Desktop/burkett-law/assets/js/nav.js
  </files>
  <action>
Create /Users/brianegan/Desktop/burkett-law/includes/header.html (the HTML fragment that gets pasted into every page's `<header role="banner">`):

```html
<div class="site-header container-xl">
  <a href="/" class="site-header__logo" aria-label="Law Office of Brian Burkett — Home">
    <span class="site-header__logo-mark">BURKETT</span>
    <span class="site-header__logo-divider" aria-hidden="true">|</span>
    <span class="site-header__logo-caption">family law</span>
  </a>

  <button type="button" class="site-header__hamburger" id="nav-toggle"
          aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
  </button>

  <nav id="site-nav" class="site-header__nav" aria-label="Primary">
    <ul class="site-header__nav-list">
      <li><a href="/practice-areas/">Practice Areas</a></li>
      <li><a href="/attorney-bio/">About</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/contact/">Contact</a></li>
    </ul>
  </nav>

  <a href="tel:+16192502683" class="site-header__phone" aria-label="Call the Law Office of Brian Burkett at (619) 250-2683">
    <svg class="site-header__phone-icon" width="16" height="16" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
    </svg>
    <span>(619) 250-2683</span>
  </a>
</div>

<script defer src="/assets/js/nav.js"></script>
```

Create /Users/brianegan/Desktop/burkett-law/assets/css/header.css. Style verbatim per DESIGN.md §6.4:

```css
/* Universal header. Sticky, navy, cream text, gold phone chip. */

header[role="banner"] {
  position: sticky;
  top: 0;
  z-index: var(--z-header);
  background: var(--color-surface-dark);
  color: var(--color-text-on-dark);
  border-bottom: 1px solid rgba(214, 201, 179, 0.2);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.site-header {
  display: flex;
  align-items: center;
  gap: var(--space-6);
  height: 64px;
  padding-inline: var(--space-4);
}

@media (min-width: 768px) {
  .site-header { height: 72px; padding-inline: var(--space-6); }
}

/* Logo */
.site-header__logo {
  display: inline-flex;
  align-items: baseline;
  gap: var(--space-2);
  color: var(--color-text-on-dark);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: 1.375rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  margin-right: auto;
}

.site-header__logo-mark { color: var(--cream-50); }
.site-header__logo-divider { color: var(--gold-500); font-weight: 400; }
.site-header__logo-caption {
  font-family: var(--font-body);
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: var(--tracking-eyebrow);
  text-transform: uppercase;
  color: var(--cream-50);
  opacity: 0.75;
}

/* Nav */
.site-header__nav-list {
  display: none;
  list-style: none;
  gap: var(--space-6);
  padding: 0;
  margin: 0;
}

@media (min-width: 768px) {
  .site-header__nav-list { display: flex; }
}

.site-header__nav-list a {
  color: var(--cream-50);
  opacity: 0.85;
  font-family: var(--font-body);
  font-size: 0.9375rem;
  font-weight: 500;
  text-decoration: none;
  padding: var(--space-2) 0;
  transition: opacity var(--duration-fast) var(--ease-out),
              text-decoration-color var(--duration-fast) var(--ease-out);
}

.site-header__nav-list a:hover,
.site-header__nav-list a[aria-current="page"] {
  opacity: 1;
  text-decoration: underline;
  text-decoration-color: var(--gold-500);
  text-decoration-thickness: 2px;
  text-underline-offset: 6px;
}

/* Phone chip */
.site-header__phone {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-5);
  background: var(--gold-100);
  color: var(--ink-900);
  border: 1px solid var(--gold-600);
  border-radius: var(--radius-pill);
  font-family: var(--font-body);
  font-size: 0.9375rem;
  font-weight: 600;
  text-decoration: none;
  transition: background var(--duration-fast) var(--ease-out),
              color var(--duration-fast) var(--ease-out);
}

.site-header__phone-icon { color: var(--gold-700); }
.site-header__phone:hover { background: var(--gold-600); color: var(--cream-50); }
.site-header__phone:hover .site-header__phone-icon { color: var(--cream-50); }

/* Hamburger (mobile only) */
.site-header__hamburger {
  display: inline-flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
  width: 44px;
  height: 44px;
  background: transparent;
  border: none;
  color: var(--cream-50);
  cursor: pointer;
  padding: 0;
  order: 2;
}

.site-header__hamburger-bar {
  display: block;
  width: 22px;
  height: 2px;
  background: currentColor;
  transition: transform var(--duration-base) var(--ease-out),
              opacity var(--duration-fast) var(--ease-out);
}

@media (min-width: 768px) {
  .site-header__hamburger { display: none; }
}

/* Mobile drawer */
@media (max-width: 767px) {
  .site-header__nav {
    position: fixed;
    inset: 64px 0 auto 0;
    background: var(--cream-50);
    color: var(--ink-900);
    padding: var(--space-6);
    transform: translateY(-100%);
    transition: transform var(--duration-slow) var(--ease-in-out);
    z-index: var(--z-drawer);
    box-shadow: var(--shadow-lg);
  }
  .site-header__nav[data-open="true"] { transform: translateY(0); }
  .site-header__nav-list {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
  }
  .site-header__nav-list a {
    color: var(--ink-900);
    opacity: 1;
    font-size: 1.125rem;
    display: block;
    padding: var(--space-3) 0;
    border-bottom: 1px solid var(--edge-200);
  }
}
```

Create /Users/brianegan/Desktop/burkett-law/assets/js/nav.js:

```javascript
/* Mobile nav drawer toggle. Progressive enhancement — nav works without JS via keyboard tab. */
(function () {
  'use strict';

  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!toggle || !nav) return;

  function open() {
    nav.setAttribute('data-open', 'true');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close menu');
    document.body.style.overflow = 'hidden';
    var firstLink = nav.querySelector('a');
    if (firstLink) firstLink.focus();
  }

  function close() {
    nav.setAttribute('data-open', 'false');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
    document.body.style.overflow = '';
    toggle.focus();
  }

  toggle.addEventListener('click', function () {
    var expanded = toggle.getAttribute('aria-expanded') === 'true';
    if (expanded) { close(); } else { open(); }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      close();
    }
  });

  // Close on nav link click (mobile UX)
  nav.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (window.matchMedia('(max-width: 767px)').matches) close();
    });
  });
})();
```

CRITICAL:
- No inline `<script>` bodies. nav.js is external + `defer` per DESIGN.md §10.4 INP rule.
- `tel:` link uses E.164 `+16192502683` (PITFALLS.md UX pitfall — parens/spaces can break dialers).
- Character-identical display phone "(619) 250-2683" — do not deviate.
- All colors reference tokens (grep base.css: no `#[0-9A-Fa-f]{6}` should be a matching pattern in header.css either).
- Skip link (added in base.css Plan 02) remains the FIRST tab stop — do not compete for it.
  </action>
  <verify>
    <automated>test -f /Users/brianegan/Desktop/burkett-law/includes/header.html && test -f /Users/brianegan/Desktop/burkett-law/assets/css/header.css && test -f /Users/brianegan/Desktop/burkett-law/assets/js/nav.js && grep -q 'tel:+16192502683' /Users/brianegan/Desktop/burkett-law/includes/header.html && grep -q '(619) 250-2683' /Users/brianegan/Desktop/burkett-law/includes/header.html && grep -q 'aria-controls="site-nav"' /Users/brianegan/Desktop/burkett-law/includes/header.html && grep -q 'aria-expanded' /Users/brianegan/Desktop/burkett-law/includes/header.html && ! grep -E '#[0-9A-Fa-f]{6}' /Users/brianegan/Desktop/burkett-law/assets/css/header.css && wc -l /Users/brianegan/Desktop/burkett-law/assets/css/header.css | awk '{exit ($1 < 80)}' && echo "PASS"</automated>
  </verify>
  <done>Header include has logo + 4-item nav + gold phone chip + accessible hamburger with correct ARIA (expanded, controls, label); header.css uses tokens only (no hex literals); nav.js provides toggle + Escape close + link-click close.</done>
</task>

<task type="auto">
  <name>Task 2: Footer component (include + CSS)</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/includes/footer.html,
    /Users/brianegan/Desktop/burkett-law/assets/css/footer.css
  </files>
  <action>
Create /Users/brianegan/Desktop/burkett-law/includes/footer.html:

```html
<div class="site-footer container-xl">
  <div class="site-footer__grid">

    <div class="site-footer__col site-footer__col--firm">
      <p class="site-footer__wordmark">
        <span class="site-footer__mark">BURKETT</span>
        <span class="site-footer__caption">family law</span>
      </p>
      <address class="site-footer__nap">
        <span class="site-footer__nap-line">591 Camino De La Reina, Suite 821</span>
        <span class="site-footer__nap-line">San Diego, CA 92108</span>
        <a href="tel:+16192502683" class="site-footer__nap-link">(619) 250-2683</a>
      </address>
      <p class="site-footer__hours">Mon-Fri 9am-6pm</p>
    </div>

    <div class="site-footer__col site-footer__col--practice">
      <p class="site-footer__col-heading">Practice Areas</p>
      <ul class="site-footer__col-list">
        <li><a href="/practice-areas/divorce/">Divorce</a></li>
        <li><a href="/practice-areas/child-custody/">Child Custody</a></li>
        <li><a href="/practice-areas/child-support/">Child Support</a></li>
        <li><a href="/practice-areas/spousal-support/">Spousal Support</a></li>
        <li><a href="/practice-areas/mediation/">Mediation</a></li>
        <li><a href="/practice-areas/domestic-violence/">Domestic Violence</a></li>
        <li><a href="/practice-areas/guardianship/">Guardianship</a></li>
        <li><a href="/practice-areas/family-court/">Family Court</a></li>
      </ul>
    </div>

    <div class="site-footer__col site-footer__col--links">
      <p class="site-footer__col-heading">Firm</p>
      <ul class="site-footer__col-list">
        <li><a href="/attorney-bio/">About Brian Burkett</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy.html">Privacy Policy</a></li>
        <li><a href="/terms.html">Terms of Use</a></li>
        <li><a href="/disclaimer.html">Attorney Advertising Disclaimer</a></li>
      </ul>
    </div>

    <div class="site-footer__col site-footer__col--credentials">
      <p class="site-footer__col-heading">Credentials</p>
      <ul class="site-footer__col-list">
        <li>Licensed in California only</li>
        <li>State Bar of California
          <!-- BIO-VERIFY: bar admission year + bar number confirmed by Burkett in Phase 2 -->
        </li>
        <li>San Diego family law focus</li>
      </ul>
    </div>

  </div>

  <div class="site-footer__disclaimer">
    <p>
      This website is attorney advertising. Information on this site is not legal advice.
      Contacting the Law Office of Brian Burkett does not create an attorney-client relationship.
      Past results do not guarantee a similar outcome. Licensed in California only.
    </p>
  </div>

  <div class="site-footer__copyright">
    <p>&copy; 2026 Law Office of Brian Burkett. All rights reserved.</p>
  </div>
</div>
```

Create /Users/brianegan/Desktop/burkett-law/assets/css/footer.css (per DESIGN.md §6.5):

```css
/* Universal footer. Navy bg, cream text, 4-col grid, Cal Bar disclaimer band. */

footer[role="contentinfo"] {
  background: var(--color-surface-dark);
  color: var(--color-text-on-dark);
  margin-top: var(--space-24);
}

.site-footer {
  padding-block: var(--space-16) var(--space-6);
}

.site-footer__grid {
  display: grid;
  gap: var(--space-10);
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .site-footer__grid { grid-template-columns: 1fr 1fr; }
}

@media (min-width: 1024px) {
  .site-footer__grid { grid-template-columns: repeat(4, 1fr); }
}

.site-footer__wordmark {
  font-family: var(--font-display);
  font-size: 1.375rem;
  font-weight: 600;
  margin-bottom: var(--space-4);
}

.site-footer__mark { color: var(--cream-50); }
.site-footer__caption {
  display: block;
  font-family: var(--font-body);
  font-size: 0.8125rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: var(--tracking-eyebrow);
  opacity: 0.75;
}

.site-footer__nap {
  font-style: normal;
  font-size: 0.9375rem;
  line-height: 1.7;
  color: var(--cream-50);
  opacity: 0.9;
}

.site-footer__nap-line { display: block; }

.site-footer__nap-link {
  color: var(--gold-500);
  text-decoration: none;
  font-weight: 600;
  margin-top: var(--space-2);
  display: inline-block;
}

.site-footer__nap-link:hover { color: var(--cream-50); }

.site-footer__hours {
  margin-top: var(--space-3);
  font-size: 0.9375rem;
  opacity: 0.85;
}

.site-footer__col-heading {
  font-family: var(--font-body);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: var(--tracking-eyebrow);
  color: var(--gold-500);
  margin-bottom: var(--space-4);
}

.site-footer__col-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.site-footer__col-list a {
  color: var(--cream-50);
  opacity: 0.85;
  text-decoration: none;
  font-size: 0.9375rem;
}

.site-footer__col-list a:hover {
  opacity: 1;
  text-decoration: underline;
  text-decoration-color: var(--gold-500);
  text-underline-offset: 4px;
}

.site-footer__disclaimer {
  margin-top: var(--space-12);
  padding-block: var(--space-8);
  border-top: 1px solid rgba(214, 201, 179, 0.15);
  border-bottom: 1px solid rgba(214, 201, 179, 0.15);
  background: var(--ink-900);
  margin-inline: calc(var(--space-6) * -1);
  padding-inline: var(--space-6);
}

.site-footer__disclaimer p {
  font-size: 0.8125rem;
  line-height: 1.7;
  color: var(--cream-50);
  opacity: 0.7;
  font-style: italic;
  max-width: 68ch;
  margin-inline: auto;
  text-align: center;
}

.site-footer__copyright {
  margin-top: var(--space-6);
  text-align: center;
}

.site-footer__copyright p {
  font-size: 0.8125rem;
  color: var(--cream-50);
  opacity: 0.6;
}
```

CRITICAL:
- Footer NAP MUST be character-identical to the interfaces block address string (also lands in Phase 2 schema).
- Cal Bar disclaimer includes all five required sentences verbatim.
- No links to legal pages that don't exist yet — Plan 05 creates privacy.html, terms.html, disclaimer.html.
- No fabricated credentials in credentials column — Bar admission year + bar number left as HTML comment `BIO-VERIFY` marker for Phase 2 to fill after Burkett confirms.
- All colors via tokens.
  </action>
  <verify>
    <automated>test -f /Users/brianegan/Desktop/burkett-law/includes/footer.html && test -f /Users/brianegan/Desktop/burkett-law/assets/css/footer.css && grep -q '591 Camino De La Reina, Suite 821, San Diego, CA 92108' <(cat /Users/brianegan/Desktop/burkett-law/includes/footer.html | tr -s ' ' | tr '\n' ' ') || (grep -q '591 Camino De La Reina, Suite 821' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'San Diego, CA 92108' /Users/brianegan/Desktop/burkett-law/includes/footer.html) && grep -q 'tel:+16192502683' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q '(619) 250-2683' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'This website is attorney advertising' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'Information on this site is not legal advice' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'attorney-client relationship' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'Past results do not guarantee a similar outcome' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -q 'Licensed in California only' /Users/brianegan/Desktop/burkett-law/includes/footer.html && grep -c 'practice-areas/' /Users/brianegan/Desktop/burkett-law/includes/footer.html | awk '{exit ($1 < 8)}' && ! grep -E '#[0-9A-Fa-f]{6}' /Users/brianegan/Desktop/burkett-law/assets/css/footer.css && echo "PASS"</automated>
  </verify>
  <done>Footer include has NAP (character-identical), phone tel: + display, hours, all 8 practice-area links, all 6 firm/legal links (About, Blog, Contact, Privacy, Terms, Disclaimer), all 5 sentences of the Cal Bar Rule 7.1 disclaimer, copyright. footer.css uses tokens only.</done>
</task>

<task type="auto">
  <name>Task 3: Wire header + footer into base template + validate</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/templates/base.html
  </files>
  <action>
Modify /Users/brianegan/Desktop/burkett-law/templates/base.html:

1. In the `<head>`, after the existing `<link rel="stylesheet" href="/assets/css/base.css">`, add:
```html
  <link rel="stylesheet" href="/assets/css/header.css">
  <link rel="stylesheet" href="/assets/css/footer.css">
```

2. Replace the placeholder `<header role="banner">...</header>` block with:
```html
  <header role="banner">
{{ INLINE_HEADER }}
  </header>
```
Then physically inline the entire contents of `includes/header.html` in place of `{{ INLINE_HEADER }}` (no template engine — this is a copy). The result: `<header role="banner">` immediately contains the `.site-header container-xl` div and everything from the header include.

3. Similarly replace the placeholder `<footer role="contentinfo">...</footer>` block with an inline copy of `includes/footer.html`.

4. Add one comment above the header explaining the pattern:
```html
  <!-- Universal header. Copy verbatim from includes/header.html on every page. Changes to the header MUST update includes/header.html AND every page. -->
```

5. Add the same pattern comment above the footer.

Run validators against the updated base template:
```bash
cd /Users/brianegan/Desktop/burkett-law
bash scripts/run_all_validators.sh templates/base.html
```
MUST return zero violations. If a violation fires (e.g., an accidental phrase caught by Cal Bar lint), fix the specific text — do NOT weaken the lint pattern.

Commit:
```bash
git add includes/ assets/css/header.css assets/css/footer.css assets/js/nav.js templates/base.html
git commit -m "feat(01-04): universal header + footer + nav.js" -m "" -m "Sticky navy header (logo + 4-item nav + gold phone chip + mobile drawer) and 4-column footer with character-identical NAP + Cal Bar Rule 7.1 disclaimer band. Base template inlines both. Phone tel: uses E.164 (+16192502683) per PITFALLS.md UX pitfall."
```
Push if origin exists.
  </action>
  <verify>
    <automated>cd /Users/brianegan/Desktop/burkett-law && grep -q 'header.css' templates/base.html && grep -q 'footer.css' templates/base.html && grep -q 'site-header' templates/base.html && grep -q 'site-footer' templates/base.html && grep -q '591 Camino De La Reina' templates/base.html && grep -q 'This website is attorney advertising' templates/base.html && bash scripts/run_all_validators.sh templates/base.html && echo "PASS"</automated>
  </verify>
  <done>base.html includes both stylesheets, inlines the full header + footer HTML, contains the character-identical NAP and the Cal Bar disclaimer, and passes all three validators (Cal Bar lint, fabrication, identity guard) with zero violations. Feature commit exists.</done>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <what-built>Universal header + footer wired into base template. Every page copied from base.html now gets: sticky navy header with 4-item nav + gold phone chip + accessible hamburger, and a 4-column navy footer with character-identical NAP + hours + 8 practice-area links + legal links + Cal Bar Rule 7.1 sitewide disclaimer + copyright.</what-built>
  <how-to-verify>
Push has already landed on Netlify. Copy templates/base.html to a temp `_headerfooter_preview.html` at repo root, git-commit it, push, and open the Netlify preview URL for that file. Then:

1. Open the preview URL — confirm:
   - Header is sticky navy, "BURKETT | family law" logo top-left, four nav items (Practice Areas, About, Blog, Contact), gold pill "(619) 250-2683" top-right
   - Footer is navy, 4 columns on desktop (Firm / Practice Areas / Firm / Credentials), NAP shows exact "591 Camino De La Reina, Suite 821" then "San Diego, CA 92108"
   - Full-width disclaimer band with the exact 5 sentences visible in italic
2. Resize the browser to ~500px wide:
   - Nav collapses; hamburger appears left of phone chip; footer stacks to single column
3. Tap/click the hamburger:
   - Menu slides down from the top, full-width, cream background with dark links
   - Focus jumps to the first nav link
   - Escape key closes the menu; focus returns to hamburger
4. Tap "Practice Areas" in mobile menu — link navigates (will 404 since practice pages are Phase 3; that's expected — just confirm the link fires).
5. Tap the phone chip on mobile — dialer opens with 6192502683.
6. Keyboard-only test: reload page, press Tab. First tab stop MUST be "Skip to main content" (visible on focus). Second tab stop MUST be the logo. Nav items follow in order.
7. Right-click page → View Source. Search for:
   - `role="banner"` (present)
   - `role="contentinfo"` (present)
   - `aria-expanded="false"` (initial state on hamburger)
   - `aria-controls="site-nav"` (on hamburger)
   - `aria-label="Primary"` (on nav)
8. Devtools → Elements → click the `<header>` — Computed background color should be navy (`rgb(18, 41, 74)` = #12294A). Same for footer.
9. After verification, delete the temp preview file and commit the deletion, or just don't push it originally (git rm the local file).

If all 9 checks pass, type "approved". If not, describe the observed vs expected discrepancy.
  </how-to-verify>
  <resume-signal>Type "approved" to unblock Plan 05 execution (legal pages) and Phase 2 planning. Describe any header/footer issue for targeted fix.</resume-signal>
</task>

</tasks>

<verification>
Phase 1 Plan 04 verification:
- All 4 files exist (includes/header.html, includes/footer.html, assets/css/header.css, assets/css/footer.css, assets/js/nav.js) plus base.html updated.
- `bash scripts/run_all_validators.sh templates/base.html includes/header.html includes/footer.html` returns zero violations.
- Character-identical NAP in footer matches interfaces block string exactly.
- Cal Bar Rule 7.1 disclaimer contains all 5 required sentences (grep for each).
- No hex color literals in header.css or footer.css.
- `tel:` links use E.164 format `+16192502683` (no spaces / parens).
- Human confirmed responsive header + footer render + hamburger behavior via checkpoint.
</verification>

<success_criteria>
- Universal header + footer render on any page copied from base.html
- Character-identical NAP "591 Camino De La Reina, Suite 821, San Diego, CA 92108" + phone display "(619) 250-2683"
- Sitewide Cal Bar Rule 7.1 disclaimer band contains all 5 required sentences
- 4-item primary nav (Practice Areas / About / Blog / Contact) — no home-item, logo is home link
- Gold phone chip pill with icon + accessible tel:+16192502683 link
- Mobile hamburger toggles drawer with Escape-to-close and focus-return
- All CSS references tokens (no hex literals)
- All three validators (Cal Bar, fabrication, identity) pass on updated base.html
</success_criteria>

<output>
After completion, create `.planning/phases/01-foundation-design-system-validators/01-04-SUMMARY.md` recording:
- The final NAP string (for character-comparison against future GBP + BrightLocal writes)
- Any adjustments to the sitewide disclaimer text (should be zero)
- Note: "Bar admission year + bar number are BIO-VERIFY placeholders in footer credentials column. Phase 2 (bio) MUST fill these AND update content_facts.md allowlist to pass fabrication validator."
- Note: Phase 5 (Legal pages) is the sibling wave 3 plan; both share zero file overlap.
</output>
