---
phase: 01-foundation-design-system-validators
plan: 05
type: execute
wave: 4
depends_on: [02, 03, 04]
files_modified:
  - privacy.html
  - terms.html
  - disclaimer.html
autonomous: false
requirements: [FND-10]

must_haves:
  truths:
    - "/privacy.html renders with CCPA/CPRA California-specific privacy disclosures, describes actual data collection (Netlify Forms + GA4 + GHL CRM + tel: dial + calendar embed), links from footer"
    - "/terms.html renders with a real Terms of Use appropriate to a solo California family-law attorney's marketing site, links from footer"
    - "/disclaimer.html renders with Cal Bar Rule 7.1-7.5 attorney advertising disclaimer, licensed-in-California-only statement, and no-attorney-client-relationship notice, links from footer"
    - "All three legal pages copy the base.html template (header + footer + tokens + fonts inherited)"
    - "All three legal pages pass Cal Bar lint + fabrication validator + identity guard"
    - "All three pages linked from the footer legal column render at expected paths (no 404 from footer)"
  artifacts:
    - path: "privacy.html"
      provides: "Privacy Policy — CCPA + CPRA California Consumer Rights + data collection disclosures"
      min_lines: 60
      contains: "California Consumer Privacy Act"
    - path: "terms.html"
      provides: "Terms of Use for the marketing website"
      min_lines: 40
      contains: "Terms of Use"
    - path: "disclaimer.html"
      provides: "Attorney Advertising Disclaimer per Cal Bar Rule 7.1-7.5"
      min_lines: 40
      contains: "attorney advertising"
  key_links:
    - from: "includes/footer.html"
      to: "privacy.html + terms.html + disclaimer.html"
      via: "<a href> in firm links column"
      pattern: "privacy.html"
    - from: "privacy.html"
      to: "contact page (mailto or /contact/)"
      via: "'How to reach us' section link"
    - from: "disclaimer.html"
      to: "California State Bar"
      via: "External link to https://www.calbar.ca.gov/"
---

<objective>
Ship the three legal pages the footer links to: /privacy.html (CCPA + CPRA California disclosures reflecting actual data collection on this site), /terms.html (Terms of Use), and /disclaimer.html (Cal Bar Rule 7.1-7.5 attorney advertising disclaimer). All three copy templates/base.html so header + footer + tokens + fonts are inherited automatically.

Purpose: California is aggressive on CCPA/CPRA enforcement, and California State Bar advertising rules are enforced separately. Every footer link must resolve to a real page (no 404s). These three pages plus the sitewide disclaimer band (Plan 04 footer) satisfy FND-10 and give the site a real legal surface before content generation starts in Phase 2.

Output: Three static HTML pages at repo root. Each is a `container-md` prose block using .prose styles + tokens; no new components required.
</objective>

<execution_context>
@/Users/brianegan/.claude/get-shit-done/workflows/execute-plan.md
@/Users/brianegan/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/STACK.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/PITFALLS.md
@/Users/brianegan/Desktop/burkett-law/.planning/phases/01-foundation-design-system-validators/02-PLAN.md

<interfaces>
<!-- Data collection surface (drives the Privacy Policy accuracy) -->

The site collects PII via these vectors (per PROJECT.md + STACK.md):
1. Netlify contact form (Phase 2) — name, email, phone, matter type, message
2. GA4 analytics — page views, referrer, device, city-level geo, engagement events (form_submit, phone_click, calendar_view, calendar_booked)
3. GHL CRM (post-launch) — form submissions may be forwarded to GHL for lead pipeline tracking
4. GHL calendar embed — booking data (name, email, phone, appointment time) collected by GHL widget iframe
5. tel: dial — metadata only (no automated capture; call logs live in Retell/Twilio post-launch)
6. Server logs — Netlify's access logs (IP, user-agent, path) retained ~7 days for abuse

The site does NOT: sell PI, share PI with data brokers, use cross-site tracking cookies, deploy retargeting pixels, or use behavioral advertising. (These CCPA-specific "we do NOT" statements matter — CA AG has enforced against sites that don't say what they don't do.)

Base template pattern (all three pages follow):
- Copy templates/base.html
- Replace {{ page_title }} with "Privacy Policy" / "Terms of Use" / "Attorney Advertising Disclaimer"
- Replace {{ page_description }} with a short SEO description
- Replace {{ page_path }} with "/privacy.html" / "/terms.html" / "/disclaimer.html"
- Replace {{ page_h1 }} + {{ page_lead }} — but body of each page is more structured than a single lead paragraph, so use container-md + .prose wrapping <section> blocks
- Leave GA4 slot commented (Phase 6 wires real id)
- Leave schema slot with a WebPage JSON-LD block (see below)

WebPage schema pattern (per STACK.md — every legal page ships a simple WebPage node):
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Page Title]",
  "url": "https://childcustodyanddivorce.com/[path]",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Law Office of Brian Burkett",
    "url": "https://childcustodyanddivorce.com/"
  }
}
```

Publish date: 2026-07-03 (site initialization date); Last Updated: 2026-07-03. These are visible on-page and in `dateModified` on schema.
</interfaces>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Create privacy.html + terms.html</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/privacy.html,
    /Users/brianegan/Desktop/burkett-law/terms.html
  </files>
  <action>
Copy /Users/brianegan/Desktop/burkett-law/templates/base.html to /Users/brianegan/Desktop/burkett-law/privacy.html. Fill placeholders + replace `{{ page_h1 }}` main section with the privacy policy content below.

`privacy.html` head substitutions:
- `{{ page_title }}` → `Privacy Policy`
- `{{ page_description }}` → `Privacy Policy for the Law Office of Brian Burkett (childcustodyanddivorce.com) — data collected, how it's used, California Consumer Privacy Act rights, and how to reach us.`
- `{{ page_path }}` → `/privacy.html`
- `{{ og_image_path }}` → `/assets/img/og-default.jpg` (leave as placeholder; Phase 6 generates real OG image)
- Uncomment SCHEMA-BEGIN block and insert WebPage JSON-LD (per interfaces block) with name "Privacy Policy" and url "https://childcustodyanddivorce.com/privacy.html".

`privacy.html` <main> content (replace `<div class="container-lg">...</div>` in template with):

```html
<div class="container-md">
  <article class="prose">
    <p class="site-meta"><em>Last updated: July 3, 2026</em></p>
    <h1>Privacy Policy</h1>
    <p>This Privacy Policy describes how the Law Office of Brian Burkett ("we," "us," or "our") collects, uses, and safeguards information when you visit <a href="https://childcustodyanddivorce.com">childcustodyanddivorce.com</a> or interact with our office. This site is a California-based solo law practice; California residents have specific rights under the California Consumer Privacy Act (CCPA) as amended by the California Privacy Rights Act (CPRA), summarized below.</p>

    <h2>Information We Collect</h2>
    <p>We collect only the information you provide voluntarily and information necessary to operate the site. Specifically:</p>
    <ul>
      <li><strong>Contact form submissions.</strong> When you complete our contact form, we collect the fields you enter (typically your name, email address, telephone number, the general subject or matter type, and the message you send). This information is transmitted to us through Netlify Forms.</li>
      <li><strong>Calendar bookings.</strong> If you schedule a call using our online calendar, the calendar provider (GoHighLevel) collects the appointment information you provide, including name, email, phone number, and time slot.</li>
      <li><strong>Website analytics.</strong> We use Google Analytics 4 (GA4) to understand aggregate site usage. GA4 collects data such as pages viewed, referring source, device type, general geographic region (typically city or state level), and interactions such as form submissions or button clicks. We use GA4's basic configuration; we do not enable Google Signals, cross-site advertising features, or user-level identity linking.</li>
      <li><strong>Server logs.</strong> Our hosting provider (Netlify) automatically records standard web server information — the IP address that requested a page, the browser user-agent, the requested URL, and the response status — for a short retention window used for troubleshooting and abuse prevention.</li>
      <li><strong>Telephone calls.</strong> If you call the office, standard telephone metadata (calling number, call duration, timestamp) is captured by our telephone service provider. Call content is not recorded unless you are informed at the start of the call.</li>
    </ul>

    <h2>How We Use Information</h2>
    <p>We use the information described above only for the following purposes:</p>
    <ul>
      <li>Responding to your inquiry, scheduling a consultation, or providing information about our services.</li>
      <li>Sending appointment confirmations, follow-up messages, or replies to messages you initiate.</li>
      <li>Analyzing aggregate site usage to improve navigation, content, and page performance.</li>
      <li>Detecting and preventing spam, abuse, and unauthorized access to the site.</li>
      <li>Complying with our legal, ethical, and professional obligations as a California attorney.</li>
    </ul>

    <h2>What We Do Not Do</h2>
    <p>We do not sell your personal information. We do not share your personal information with data brokers. We do not use cross-site tracking cookies or behavioral advertising pixels. We do not use your form submissions or contact information for marketing to third parties. Submitting the contact form does not, by itself, add you to any marketing list.</p>

    <h2>Your California Privacy Rights (CCPA / CPRA)</h2>
    <p>If you are a California resident, you have the following rights regarding personal information the office collects about you:</p>
    <ul>
      <li><strong>Right to know</strong> what personal information we have collected about you, the categories of sources, and the purposes of collection.</li>
      <li><strong>Right to delete</strong> personal information we have collected from you, subject to certain exceptions required by our professional obligations as attorneys (for example, we may need to retain records to satisfy conflict-check or ethical obligations).</li>
      <li><strong>Right to correct</strong> inaccurate personal information we hold about you.</li>
      <li><strong>Right to opt out of the sale or sharing</strong> of your personal information. As noted above, we do not sell or share personal information for cross-context behavioral advertising; this right is preserved regardless.</li>
      <li><strong>Right to limit use of sensitive personal information.</strong> We do not use sensitive personal information beyond the purposes reasonably necessary to provide the services you request.</li>
      <li><strong>Right to non-discrimination</strong> for exercising any of these rights.</li>
    </ul>
    <p>To exercise any of these rights, contact us using the details in the "Contact Us" section below. We will respond within the timeframe required by law.</p>

    <h2>Cookies and Tracking Technologies</h2>
    <p>Our website uses a small number of cookies for essential functions and for analytics via GA4. No third-party advertising or retargeting cookies are set. Most browsers allow you to block cookies through your settings; doing so may affect analytics accuracy but will not prevent you from using the site or submitting our contact form.</p>

    <h2>Third-Party Services</h2>
    <p>We use the following third-party services to operate the site. Each is governed by its own privacy policy:</p>
    <ul>
      <li>Netlify (hosting, form processing) — <a href="https://www.netlify.com/privacy/">netlify.com/privacy</a></li>
      <li>Google Analytics 4 (site analytics) — <a href="https://policies.google.com/privacy">policies.google.com/privacy</a></li>
      <li>GoHighLevel (calendar bookings) — <a href="https://www.gohighlevel.com/privacy-policy">gohighlevel.com/privacy-policy</a></li>
    </ul>

    <h2>Data Retention</h2>
    <p>Contact form submissions and calendar bookings are retained as long as reasonably necessary to respond to your inquiry, provide requested services, and meet our record-keeping obligations as attorneys. Aggregate analytics data is retained per Google Analytics 4 defaults. Server access logs are retained by Netlify per its standard operational retention.</p>

    <h2>Children's Privacy</h2>
    <p>This site is intended for adults. We do not knowingly collect personal information from anyone under the age of 18. If you believe a minor has provided personal information through the site, please contact us and we will delete it.</p>

    <h2>Security</h2>
    <p>The site is served over HTTPS with modern security headers. Contact form data is transmitted securely to Netlify's servers. No data transmission over the internet is perfectly secure, and we cannot guarantee absolute security; however, we take reasonable steps to protect the information you provide.</p>

    <h2>Changes to This Policy</h2>
    <p>We may update this Privacy Policy from time to time. When we do, we will update the "Last updated" date at the top of this page. Material changes will be announced on the site.</p>

    <h2>Contact Us</h2>
    <p>To exercise your California privacy rights, ask about this policy, or submit a privacy request, please reach the office at:</p>
    <p>
      Law Office of Brian Burkett<br>
      591 Camino De La Reina, Suite 821<br>
      San Diego, CA 92108<br>
      <a href="tel:+16192502683">(619) 250-2683</a>
    </p>
    <p><em>This Privacy Policy is not legal advice. If you have questions about your specific privacy rights, please consult qualified counsel.</em></p>
  </article>
</div>
```

Copy templates/base.html to /Users/brianegan/Desktop/burkett-law/terms.html. Fill placeholders similarly:
- `{{ page_title }}` → `Terms of Use`
- `{{ page_description }}` → `Terms of Use for the Law Office of Brian Burkett website (childcustodyanddivorce.com).`
- `{{ page_path }}` → `/terms.html`
- Schema block: WebPage with name "Terms of Use" + url

`terms.html` <main> content:

```html
<div class="container-md">
  <article class="prose">
    <p class="site-meta"><em>Last updated: July 3, 2026</em></p>
    <h1>Terms of Use</h1>
    <p>Welcome to the website of the Law Office of Brian Burkett. By accessing or using this site, you agree to these Terms of Use. If you do not agree, please do not use the site.</p>

    <h2>Purpose of This Site</h2>
    <p>This website is provided for general informational purposes only. It describes the practice of attorney Brian Burkett, licensed in the State of California, based in San Diego, California. Information on this site is <strong>not legal advice</strong>. Every legal situation is unique. You should consult a qualified attorney about your specific circumstances before making any decision.</p>

    <h2>No Attorney-Client Relationship</h2>
    <p>Viewing this website, sending a message through the contact form, scheduling a consultation, calling the office, or any other unilateral communication does not create an attorney-client relationship between you and the Law Office of Brian Burkett. An attorney-client relationship is formed only after both you and the office have signed a written engagement agreement.</p>

    <h2>Do Not Send Confidential Information Until Engaged</h2>
    <p>Please do not send confidential or time-sensitive information through the contact form, email, or any other channel before a written engagement agreement is in place. Information you send before engagement may not be protected by the attorney-client privilege and could create conflicts of interest that prevent us from representing you.</p>

    <h2>Attorney Advertising</h2>
    <p>This website constitutes attorney advertising under the California Rules of Professional Conduct. See our <a href="/disclaimer.html">Attorney Advertising Disclaimer</a> for details.</p>

    <h2>Accuracy and Currency of Information</h2>
    <p>We make reasonable efforts to keep information on this site accurate and current. Family law in California is complex and changes over time; content may not reflect the most recent developments. Do not rely on any statement here as a substitute for professional legal advice.</p>

    <h2>Links to Third-Party Sites</h2>
    <p>This site may link to third-party websites for convenience. We do not endorse and are not responsible for the content, accuracy, or privacy practices of any linked site.</p>

    <h2>Intellectual Property</h2>
    <p>The content, design, and code of this site are the property of the Law Office of Brian Burkett except where credited otherwise. You may view and share links to public pages for personal, non-commercial purposes. Any other use requires our written permission.</p>

    <h2>Jurisdiction and Governing Law</h2>
    <p>This site is operated from California. Any dispute arising from your use of this site is governed by California law and shall be resolved in the state or federal courts located in San Diego County, California.</p>

    <h2>Modifications</h2>
    <p>We may update these Terms of Use at any time by posting a revised version on this page. Continued use of the site after changes are posted constitutes acceptance of the revised terms.</p>

    <h2>Contact</h2>
    <p>Questions about these Terms of Use? Contact:</p>
    <p>
      Law Office of Brian Burkett<br>
      591 Camino De La Reina, Suite 821<br>
      San Diego, CA 92108<br>
      <a href="tel:+16192502683">(619) 250-2683</a>
    </p>
  </article>
</div>
```

CRITICAL:
- Every reference to the firm uses "Law Office of Brian Burkett" (matches clients.json brand_name).
- NAP block in each page uses character-identical address string from Plan 04 interfaces.
- No "our team" / "our attorneys" (would trigger Cal Bar lint — validator will fail commit).
- No numeric fabrication (validator will fail commit if a year, statistic, or "since [year]" appears without content_facts.md entry).
- No emojis anywhere.
- Colors + fonts come from base + tokens — no per-page style block needed.
- `<p class="site-meta">` — that's a new class that isn't styled anywhere; leave it — it renders as prose caption via default styles + `.prose` inheritance. Do NOT add a new CSS file for one line.
  </action>
  <verify>
    <automated>cd /Users/brianegan/Desktop/burkett-law && test -f privacy.html && test -f terms.html && grep -q 'California Consumer Privacy Act' privacy.html && grep -q 'CPRA' privacy.html && grep -q 'do not sell your personal information' privacy.html && grep -q 'no attorney-client relationship\|No Attorney-Client Relationship' terms.html && grep -q 'Do not send confidential\|Do Not Send Confidential' terms.html && grep -q '591 Camino De La Reina, Suite 821' privacy.html && grep -q '591 Camino De La Reina, Suite 821' terms.html && grep -q 'site-header\|Universal header' privacy.html && grep -q 'site-footer\|Universal footer' privacy.html && bash scripts/run_all_validators.sh privacy.html terms.html && echo "PASS"</automated>
  </verify>
  <done>privacy.html contains CCPA/CPRA disclosures, actual data-collection description, do-not-sell statement, character-identical NAP, and inherits header + footer. terms.html contains no-attorney-client-relationship notice, do-not-send-confidential-info notice, character-identical NAP, and inherits header + footer. Both pass all three validators (zero violations).</done>
</task>

<task type="auto">
  <name>Task 2: Create disclaimer.html + commit + validate</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/disclaimer.html
  </files>
  <action>
Copy /Users/brianegan/Desktop/burkett-law/templates/base.html to /Users/brianegan/Desktop/burkett-law/disclaimer.html. Fill placeholders:
- `{{ page_title }}` → `Attorney Advertising Disclaimer`
- `{{ page_description }}` → `California State Bar attorney advertising disclaimer for the Law Office of Brian Burkett (childcustodyanddivorce.com).`
- `{{ page_path }}` → `/disclaimer.html`
- Schema block: WebPage with name "Attorney Advertising Disclaimer" + url

`disclaimer.html` <main> content:

```html
<div class="container-md">
  <article class="prose">
    <p class="site-meta"><em>Last updated: July 3, 2026</em></p>
    <h1>Attorney Advertising Disclaimer</h1>
    <p>This website is attorney advertising within the meaning of the California Rules of Professional Conduct. It is published by the Law Office of Brian Burkett, a California attorney licensed to practice law in the State of California.</p>

    <h2>Not Legal Advice</h2>
    <p>Information on this website is provided for general informational purposes and is not intended as legal advice. Family law is fact-specific; the outcome of any legal matter depends on the particular circumstances of that case, the applicable law, and the judgment of the assigned judicial officer. No content on this site should be treated as a substitute for the advice of a qualified attorney familiar with your specific situation.</p>

    <h2>No Attorney-Client Relationship</h2>
    <p>Reading this site, sending a message through the contact form, calling the office, scheduling a consultation, or any other unilateral communication does not create an attorney-client relationship. An attorney-client relationship is created only when you and the Law Office of Brian Burkett have signed a written engagement agreement.</p>

    <h2>Past Results</h2>
    <p>Prior results do not guarantee a similar outcome. Every case is different, and the outcome of any legal matter is dependent on many variables. Descriptions of the practice or its focus do not constitute a promise of any particular result.</p>

    <h2>Jurisdiction</h2>
    <p>Brian Burkett is licensed to practice law only in the State of California. The office serves clients primarily in San Diego County. This website is not intended to solicit clients from jurisdictions in which Brian Burkett is not licensed to practice.</p>

    <h2>Testimonials and Endorsements</h2>
    <p>Any client testimonial or endorsement on this site reflects the experience of that particular client and is not a promise, guarantee, or prediction about the outcome of any other case. Testimonials are used only with the express permission of the client and are not paid.</p>

    <h2>Confidential Information</h2>
    <p>Do not send confidential information through the contact form, email, or any other channel until a written engagement agreement is in place. Communications sent before engagement may not be protected by the attorney-client privilege and could create conflicts of interest.</p>

    <h2>Verification of Bar Standing</h2>
    <p>You may verify the bar standing of any California attorney, including Brian Burkett, at the State Bar of California's website: <a href="https://www.calbar.ca.gov/" rel="external">calbar.ca.gov</a>.</p>

    <h2>Contact</h2>
    <p>
      Law Office of Brian Burkett<br>
      591 Camino De La Reina, Suite 821<br>
      San Diego, CA 92108<br>
      <a href="tel:+16192502683">(619) 250-2683</a>
    </p>
  </article>
</div>
```

Run validators on all three pages:
```bash
cd /Users/brianegan/Desktop/burkett-law && bash scripts/run_all_validators.sh privacy.html terms.html disclaimer.html
```
Must exit 0 (zero violations). If a violation fires, fix the specific text — do NOT weaken the validator.

Update sitemap.xml to include the three legal pages. Read current sitemap.xml, add three `<url>` entries (privacy.html, terms.html, disclaimer.html) with `<lastmod>2026-07-03</lastmod>` alongside the existing homepage entry.

Commit:
```bash
git add privacy.html terms.html disclaimer.html sitemap.xml
git commit -m "feat(01-05): legal pages — privacy + terms + attorney advertising disclaimer" -m "" -m "Ships /privacy.html (CCPA/CPRA compliant, describes actual data collection surface — Netlify Forms, GA4, GHL, Netlify logs, tel: dial), /terms.html (no attorney-client relationship + do-not-send-confidential notice + California jurisdiction), and /disclaimer.html (Cal Bar Rule 7.1-7.5 attorney advertising, no-guarantee language, testimonial policy, verify-bar-standing link). All three pages copy templates/base.html so they inherit header + footer + tokens + fonts. All three pass Cal Bar lint + fabrication + identity guard."
```
Push if origin exists.
  </action>
  <verify>
    <automated>cd /Users/brianegan/Desktop/burkett-law && test -f disclaimer.html && grep -q 'attorney advertising' disclaimer.html && grep -q 'Prior results do not guarantee' disclaimer.html && grep -q 'calbar.ca.gov' disclaimer.html && grep -q 'No Attorney-Client Relationship' disclaimer.html && grep -q '591 Camino De La Reina, Suite 821' disclaimer.html && grep -q 'privacy.html' sitemap.xml && grep -q 'terms.html' sitemap.xml && grep -q 'disclaimer.html' sitemap.xml && bash scripts/run_all_validators.sh privacy.html terms.html disclaimer.html && echo "PASS"</automated>
  </verify>
  <done>disclaimer.html contains "attorney advertising" statement, "Prior results do not guarantee a similar outcome" verbatim, "No Attorney-Client Relationship" section, "Verification of Bar Standing" link to calbar.ca.gov, character-identical NAP. sitemap.xml includes all three legal URLs. All three files pass all three validators.</done>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <what-built>Three legal pages ship at /privacy.html, /terms.html, /disclaimer.html. Each renders with the universal header + footer, is written for California jurisdiction (CCPA/CPRA + Cal Bar Rule 7.1-7.5), reflects the actual data-collection surface of THIS site (not boilerplate), and links back cleanly from the footer. All three pass the fabrication + Cal Bar + identity validators.</what-built>
  <how-to-verify>
After the git push, open the Netlify preview URL. Verify each of the following:

1. `<preview>/privacy.html` renders:
   - Universal navy header at top with phone chip
   - "Privacy Policy" H1, "Last updated: July 3, 2026" caption
   - Sections: Information We Collect, How We Use Information, What We Do Not Do, Your California Privacy Rights (CCPA / CPRA), Cookies, Third-Party Services, Data Retention, Children's Privacy, Security, Changes to This Policy, Contact Us
   - Character-identical NAP in Contact Us section
   - Universal navy footer at bottom
2. `<preview>/terms.html` renders:
   - "Terms of Use" H1
   - Sections including No Attorney-Client Relationship + Do Not Send Confidential Information Until Engaged
3. `<preview>/disclaimer.html` renders:
   - "Attorney Advertising Disclaimer" H1
   - "Prior results do not guarantee a similar outcome" appears verbatim
   - Verify link to calbar.ca.gov works (opens in new context)
4. Click through EACH footer link on any page — "Privacy Policy," "Terms of Use," "Attorney Advertising Disclaimer" — confirm each lands on the correct page (no 404).
5. Human read-through: skim each page for California-specific language. Confirm nothing reads generic (e.g., no "US law" instead of "California law"; no "our firm" language).
6. Optional legal read: Burkett reads all three pages for jurisdictional accuracy before Phase 7 cutover. Note issues here for a later polish plan if any surface.

Type "approved" if all 6 checks pass, or describe specific text that needs revision.
  </how-to-verify>
  <resume-signal>Type "approved" to close Phase 1 or describe corrections for a follow-up commit before moving to Phase 2.</resume-signal>
</task>

</tasks>

<verification>
Phase 1 Plan 05 verification:
- All three files exist at /Users/brianegan/Desktop/burkett-law/{privacy.html,terms.html,disclaimer.html}
- sitemap.xml lists all three legal URLs
- `bash scripts/run_all_validators.sh privacy.html terms.html disclaimer.html` exits 0
- Each page references the character-identical NAP "591 Camino De La Reina, Suite 821, San Diego, CA 92108"
- Human confirmed via checkpoint that pages render, footer links work, California-specific language is present, and no 404 from footer.
</verification>

<success_criteria>
- Three legal pages ship, all footer links resolve (no 404)
- privacy.html covers CCPA + CPRA + describes actual data collection (Netlify Forms, GA4, GHL calendar, server logs, tel: metadata) — not boilerplate
- terms.html covers no-attorney-client-relationship + do-not-send-confidential + California jurisdiction
- disclaimer.html covers Cal Bar Rule 7.1-7.5 attorney advertising + prior-results disclaimer + testimonial policy + link to calbar.ca.gov
- All three pages inherit universal header + footer (visual consistency)
- All three pages pass Cal Bar lint + fabrication + identity guard
- sitemap.xml updated to include the three legal URLs
</success_criteria>

<output>
After completion, create `.planning/phases/01-foundation-design-system-validators/01-05-SUMMARY.md` recording:
- Publish + last-updated date used ("July 3, 2026") — for future refresh cadence
- Note: All three pages are California-jurisdiction-specific. If Burkett ever adds a second state, they need substantive rewrites, not just an addition.
- Note: These pages assume the data collection surface from PROJECT.md + STACK.md. If Phase 2 wires additional third parties (e.g., Segment, Hotjar), privacy.html must be updated to list them BEFORE those tools go live.
- Note: This closes Phase 1. Phase 2 (bio + homepage + contact) is unblocked.
</output>
