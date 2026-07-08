#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD block to the 5 top-level pages that lack it.

Pages: about, contact, disclaimer, privacy, terms. Each is one hop from
home, so the breadcrumb is Home -> <Page Name>.

Injected right before </head> to sit alongside the primary schema block
without touching anything else.
"""
import pathlib

ROOT = pathlib.Path("/Users/brianegan/Desktop/burkett-law")

PAGES = {
    "about.html": ("About Brian Burkett", "https://childcustodyanddivorce.com/about.html"),
    "contact.html": ("Contact", "https://childcustodyanddivorce.com/contact.html"),
    "disclaimer.html": ("Attorney Advertising Disclaimer", "https://childcustodyanddivorce.com/disclaimer.html"),
    "privacy.html": ("Privacy Policy", "https://childcustodyanddivorce.com/privacy.html"),
    "terms.html": ("Terms of Use", "https://childcustodyanddivorce.com/terms.html"),
}


def block(name: str, url: str) -> str:
    return f"""
  <!-- Phase 6 · SEO-06: BreadcrumbList schema. Every non-home page carries this. -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://childcustodyanddivorce.com/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{name}",
        "item": "{url}"
      }}
    ]
  }}
  </script>
"""


def main():
    for rel, (name, url) in PAGES.items():
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        if '"BreadcrumbList"' in text:
            print(f"skip {rel} (already has BreadcrumbList)")
            continue
        if "</head>" not in text:
            print(f"MISS {rel} (no </head>)")
            continue
        new = text.replace("</head>", block(name, url) + "</head>", 1)
        p.write_text(new, encoding="utf-8")
        print(f"FIX  {rel}")


if __name__ == "__main__":
    main()
