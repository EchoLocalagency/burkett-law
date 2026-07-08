#!/usr/bin/env python3
"""
Phase 5 blog post generator.

Writes 15 blog posts under blog/[slug].html using shared header/footer/schema
boilerplate + per-post body copy. Each post gets LegalArticle schema with
author.@id -> bio Person, backdated datePublished, dateModified = today.

Run: python3 .planning/phases/05-blog/build_posts.py
"""
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
BLOG = REPO / "blog"
DATE_MODIFIED = "2026-07-08"

# Category -> practice pillar slug
CATEGORY_PILLAR = {
    "Divorce": "divorce",
    "Child Custody": "child-custody",
    "Child Support": "child-support",
    "Spousal Support": "spousal-support",
    "Mediation": "mediation",
    "Domestic Violence": "domestic-violence",
    "Guardianship": "guardianship",
    "Family Court": "family-court",
}


def header(title: str, description: str, slug: str) -> str:
    canonical = f"https://childcustodyanddivorce.com/blog/{slug}.html"
    return f"""<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{title} — Law Office of Brian Burkett</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://childcustodyanddivorce.com/assets/img/brian-burkett-headshot.jpg">
  <meta property="og:site_name" content="Law Office of Brian Burkett">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/InterVariable.woff2" crossorigin>

  <link rel="stylesheet" href="/assets/css/tokens.css">
  <link rel="stylesheet" href="/assets/css/base.css">
  <link rel="stylesheet" href="/assets/css/header.css">
  <link rel="stylesheet" href="/assets/css/footer.css">
  <link rel="stylesheet" href="/assets/css/bio.css">
  <link rel="stylesheet" href="/assets/css/blog.css">

  <!-- GA4 slot — Phase 6 wires the real id. -->
  <!-- GA4-BEGIN
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-BURKETT_ID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-BURKETT_ID');
  </script>
  GA4-END -->
"""


def schema_block(post: dict) -> str:
    canonical = f"https://childcustodyanddivorce.com/blog/{post['slug']}.html"
    return f"""
  <!-- LegalArticle @graph: LegalArticle + BreadcrumbList. author.@id -> bio Person. -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "LegalArticle",
        "@id": "{canonical}#article",
        "headline": {post['headline_json']},
        "description": {post['description_json']},
        "url": "{canonical}",
        "mainEntityOfPage": "{canonical}",
        "datePublished": "{post['published']}",
        "dateModified": "{DATE_MODIFIED}",
        "author": {{ "@id": "https://childcustodyanddivorce.com/about.html#brian-burkett" }},
        "publisher": {{ "@id": "https://childcustodyanddivorce.com/#legalservice" }},
        "articleSection": "{post['category']}",
        "inLanguage": "en-US",
        "about": {{ "@id": "https://childcustodyanddivorce.com/practice-areas/{CATEGORY_PILLAR[post['category']]}/#service" }}
      }},
      {{
        "@type": "BreadcrumbList",
        "@id": "{canonical}#breadcrumb",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://childcustodyanddivorce.com/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://childcustodyanddivorce.com/blog/" }},
          {{ "@type": "ListItem", "position": 3, "name": {post['headline_json']}, "item": "{canonical}" }}
        ]
      }}
    ]
  }}
  </script>
</head>
"""


HEADER_HTML = """
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header role="banner">
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
      <li><a href="/about.html">About</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/contact.html">Contact</a></li>
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
  </header>
"""


FOOTER_HTML = """  <footer role="contentinfo">
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
        <li><a href="/about.html">About Brian Burkett</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="/privacy.html">Privacy Policy</a></li>
        <li><a href="/terms.html">Terms of Use</a></li>
        <li><a href="/disclaimer.html">Attorney Advertising Disclaimer</a></li>
      </ul>
    </div>

    <div class="site-footer__col site-footer__col--credentials">
      <p class="site-footer__col-heading">Credentials</p>
      <ul class="site-footer__col-list">
        <li>Licensed in California only</li>
        <li>State Bar of California, No. 220343 &mdash; admitted 2002</li>
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
  </footer>
</body>
</html>
"""


def cta_block() -> str:
    return """
        <section class="blog-post__cta">
          <h2>Talk Through Your Matter</h2>
          <p>Three ways to reach me. Pick whichever is easiest.</p>
          <div class="blog-post__cta-trio">
            <a href="tel:+16192502683" class="cta-card cta-card--phone">
              <p class="cta-card__label">Call Directly</p>
              <p class="cta-card__value">(619) 250-2683</p>
              <p class="cta-card__note">Mon-Fri 9am-6pm</p>
            </a>
            <a href="/contact.html#booking" class="cta-card cta-card--calendar">
              <p class="cta-card__label">Book a Consultation</p>
              <p class="cta-card__value">Schedule online</p>
              <p class="cta-card__note">15-minute intake call</p>
            </a>
            <a href="/contact.html#form" class="cta-card cta-card--form">
              <p class="cta-card__label">Send a Message</p>
              <p class="cta-card__value">Contact form</p>
              <p class="cta-card__note">I respond within one business day</p>
            </a>
          </div>
          <p class="blog-post__cta-disclaimer">
            Contacting the Law Office of Brian Burkett does not create an
            attorney-client relationship. Please do not include confidential or
            sensitive information in your first message.
          </p>
        </section>
"""


def render_related(related: list) -> str:
    """related is a list of dicts: {url, category, title}"""
    items = "\n".join(
        f'''            <li>
              <a href="{r['url']}">
                <span class="blog-post__related-cat">{r['category']}</span>
                <span class="blog-post__related-title">{r['title']}</span>
              </a>
            </li>'''
        for r in related
    )
    return f"""
        <section class="blog-post__related">
          <h2>Related reading</h2>
          <ul class="blog-post__related-list">
{items}
          </ul>
        </section>
"""


def render_post(post: dict) -> str:
    """Assemble the full page."""
    title = post["title"]
    description = post["description"]
    slug = post["slug"]

    body_html = post["body_html"]
    related_html = render_related(post["related"])
    published_pretty = post["published_pretty"]

    return "".join([
        header(title, description, slug),
        schema_block(post),
        HEADER_HTML,
        f"""
  <main id="main">
    <article class="blog">
      <div class="container-xl">
        <nav class="blog__breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li aria-current="page">{post['breadcrumb_short']}</li>
          </ol>
        </nav>

        <header class="blog-post__hero">
          <p class="blog-post__category">{post['category']}</p>
          <h1>{post['h1']}</h1>
          <p class="blog-post__byline">
            By <a href="/about.html">Brian Burkett</a>, Attorney at Law
            <span class="blog-post__byline-sep">&middot;</span>
            Published {published_pretty}
            <span class="blog-post__byline-sep">&middot;</span>
            Updated July 8, 2026
          </p>
        </header>

        <div class="blog-post__body">
{body_html}
        </div>

{related_html}

{cta_block()}
      </div>
    </article>
  </main>
""",
        FOOTER_HTML,
    ])


# ---------------------------------------------------------------------------
# Post data
# ---------------------------------------------------------------------------

# Related post lookup by slug for cluster linking
POST_TITLES = {
    "divorce-mediation-in-san-diego": ("Mediation", "Divorce Mediation in San Diego: How the Process Works Under California Law"),
    "how-a-divorce-attorney-navigates-california-process": ("Divorce", "How a San Diego Divorce Attorney Navigates the California Dissolution Process"),
    "california-community-property-division": ("Divorce", "California Community Property: How Marital Assets and Debts Get Divided"),
    "spousal-support-in-california-what-to-expect": ("Spousal Support", "Spousal Support in California: What to Expect at Every Stage of a Case"),
    "alimony-in-california-a-practical-guide": ("Spousal Support", "Alimony in California: A Practical Guide Under Family Code Section 4320"),
    "protecting-parental-rights-in-california-custody": ("Child Custody", "Protecting Parental Rights in California Custody Cases"),
    "child-visitation-in-california": ("Child Custody", "Child Visitation in California: Parenting Plans, Schedules, and Enforcement"),
    "what-a-california-custody-attorney-does": ("Child Custody", "What a California Custody Attorney Actually Does (Beyond the Hearing)"),
    "child-support-in-california-what-attorneys-do": ("Child Support", "Child Support in California: What an Attorney Adds to the Guideline Number"),
    "working-with-a-child-support-attorney": ("Child Support", "Working With a San Diego Child Support Attorney: What the First Six Weeks Look Like"),
    "guardianship-under-california-probate-code": ("Guardianship", "Guardianship Under the California Probate Code: A San Diego Overview"),
    "domestic-violence-restraining-orders-california": ("Domestic Violence", "Domestic Violence Restraining Orders in California: How the DVPA Works"),
    "navigating-san-diego-family-court": ("Family Court", "Navigating San Diego Family Court: A Room-by-Room Guide"),
    "preliminary-declaration-of-disclosure-california": ("Divorce", "The Preliminary Declaration of Disclosure in a California Divorce"),
    "why-hire-a-family-law-attorney-in-california": ("Family Court", "Why Hire a Family Law Attorney in California (and When You Might Not Need To)"),
}


def related_of(slug: str, cat: str, title: str) -> dict:
    return {
        "url": f"/blog/{slug}.html",
        "category": cat,
        "title": title,
    }


def rel(slug: str) -> dict:
    cat, title = POST_TITLES[slug]
    return related_of(slug, cat, title)


# ---------------------------------------------------------------------------
# POSTS (imported from posts_content.py to keep this file smaller)
# ---------------------------------------------------------------------------
import posts_content  # noqa: E402
POSTS = posts_content.POSTS


def escape_json(s: str) -> str:
    """JSON-escape a string for use inside a JSON string literal."""
    return '"' + s.replace('\\', r'\\').replace('"', r'\"') + '"'


def main() -> int:
    BLOG.mkdir(parents=True, exist_ok=True)
    for post in POSTS:
        # Pre-compute JSON-escaped fields for schema
        post["headline_json"] = escape_json(post["title"])
        post["description_json"] = escape_json(post["description"])
        html = render_post(post)
        out = BLOG / f"{post['slug']}.html"
        out.write_text(html, encoding="utf-8")
        # Also compute word count in body for sanity check
        import re
        body_text = re.sub(r"<[^>]+>", " ", post["body_html"])
        words = len(re.findall(r"\w+", body_text))
        print(f"[write] {out.name}  words={words}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
