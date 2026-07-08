#!/usr/bin/env python3
"""Regenerate sitemap.xml from the actual on-disk page inventory.

Rules:
- Excludes thanks.html (noindex confirmation page) + any /404.html.
- `/`, `/practice-areas/`, `/blog/`, `/san-diego/**/` — collapsed to trailing-slash form
  (no `index.html`) to match live serving.
- `lastmod` = repo `git log -1 --format=%cs -- <file>` for that specific file (falls back to today
  if git returns empty).
- Sorted by path so diffs are stable.
"""
from __future__ import annotations
import pathlib
import subprocess

ROOT = pathlib.Path("/Users/brianegan/Desktop/burkett-law")
BASE = "https://childcustodyanddivorce.com"
EXCLUDE_DIRS = {".git", ".planning", ".netlify", "assets", "node_modules", "scripts", "templates", "includes"}
EXCLUDE_FILES = {"thanks.html", "404.html"}


def find_html_files():
    for p in sorted(ROOT.rglob("*.html")):
        parts = set(p.relative_to(ROOT).parts)
        if parts & EXCLUDE_DIRS:
            continue
        if p.name in EXCLUDE_FILES:
            continue
        yield p


def loc_for(path: pathlib.Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return BASE + "/"
    if rel.endswith("/index.html"):
        return BASE + "/" + rel[: -len("index.html")]
    return BASE + "/" + rel


def lastmod_for(path: pathlib.Path) -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        s = result.stdout.strip()
        return s or "2026-07-08"
    except Exception:
        return "2026-07-08"


def build():
    urls = []
    for f in find_html_files():
        urls.append((loc_for(f), lastmod_for(f)))
    urls.sort(key=lambda x: x[0])

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    return len(urls), "\n".join(lines)


if __name__ == "__main__":
    n, xml = build()
    (ROOT / "sitemap.xml").write_text(xml)
    print(f"sitemap.xml: {n} URLs")
