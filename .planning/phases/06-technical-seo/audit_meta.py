#!/usr/bin/env python3
"""Sitewide meta audit for Phase 6.

Extracts per HTML page: <title>, <meta description>, canonical, all H1s, OG tags, JSON-LD schema types.
Reports pages with violations (title > 60, desc > 160, missing/duplicated fields, > 1 H1, missing canonical/OG/JSON-LD).

Usage:
  python3 .planning/phases/06-technical-seo/audit_meta.py
"""
from __future__ import annotations
import json
import pathlib
import re
import sys

ROOT = pathlib.Path("/Users/brianegan/Desktop/burkett-law")
EXCLUDE_DIRS = {".git", ".planning", ".netlify", "assets", "node_modules", "scripts", "templates", "includes"}


def find_html_files(root: pathlib.Path):
    for p in sorted(root.rglob("*.html")):
        parts = set(p.relative_to(root).parts)
        if parts & EXCLUDE_DIRS:
            continue
        yield p


def extract(text: str) -> dict:
    def m(pattern, flags=re.I | re.S):
        r = re.search(pattern, text, flags)
        return r.group(1).strip() if r else None

    title = m(r"<title>(.*?)</title>")
    desc = m(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']')
    canonical = m(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']')
    og_title = m(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']')
    og_desc = m(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']')
    og_url = m(r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\'](.*?)["\']')
    og_image = m(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']')
    twitter_card = m(r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\'](.*?)["\']')

    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", text, re.I | re.S)
    h1s = [re.sub(r"<[^>]+>", "", h).strip() for h in h1s]

    schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', text)

    ga4_present = bool(re.search(r"googletagmanager\.com/gtag/js\?id=", text))
    ga4_ids = re.findall(r'gtag/js\?id=(G-[A-Z0-9_]+)', text)

    return {
        "title": title,
        "title_len": len(title) if title else 0,
        "description": desc,
        "description_len": len(desc) if desc else 0,
        "canonical": canonical,
        "og_title": og_title,
        "og_description": og_desc,
        "og_url": og_url,
        "og_image": og_image,
        "twitter_card": twitter_card,
        "h1_count": len(h1s),
        "h1s": h1s,
        "schema_types": schemas,
        "ga4_present": ga4_present,
        "ga4_ids": ga4_ids,
    }


def main():
    files = list(find_html_files(ROOT))
    results = {}
    for f in files:
        rel = str(f.relative_to(ROOT))
        results[rel] = extract(f.read_text(encoding="utf-8"))

    violations = []
    titles = {}
    descs = {}
    canonicals = {}
    for rel, r in results.items():
        vs = []
        if not r["title"]:
            vs.append("MISSING_TITLE")
        elif r["title_len"] > 60:
            vs.append(f"TITLE_TOO_LONG({r['title_len']})")
        if not r["description"]:
            vs.append("MISSING_DESC")
        elif r["description_len"] > 160:
            vs.append(f"DESC_TOO_LONG({r['description_len']})")
        if not r["canonical"]:
            vs.append("MISSING_CANONICAL")
        if not r["og_title"]:
            vs.append("MISSING_OG_TITLE")
        if not r["og_description"]:
            vs.append("MISSING_OG_DESC")
        if not r["og_url"]:
            vs.append("MISSING_OG_URL")
        if not r["og_image"]:
            vs.append("MISSING_OG_IMAGE")
        if r["h1_count"] == 0:
            vs.append("NO_H1")
        elif r["h1_count"] > 1:
            vs.append(f"MULTIPLE_H1({r['h1_count']})")
        if not r["schema_types"]:
            vs.append("NO_SCHEMA")
        if not r["ga4_present"]:
            vs.append("NO_GA4")

        if r["title"]:
            titles.setdefault(r["title"], []).append(rel)
        if r["description"]:
            descs.setdefault(r["description"], []).append(rel)
        if r["canonical"]:
            canonicals.setdefault(r["canonical"], []).append(rel)

        if vs:
            violations.append((rel, vs))

    # Duplicate detection
    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in descs.items() if len(v) > 1}
    dup_canon = {k: v for k, v in canonicals.items() if len(v) > 1}

    report = {
        "total_pages": len(files),
        "pages_with_violations": len(violations),
        "duplicate_titles": dup_titles,
        "duplicate_descriptions": dup_descs,
        "duplicate_canonicals": dup_canon,
        "violations": {rel: vs for rel, vs in violations},
        "per_page": results,
    }

    out = ROOT / ".planning/phases/06-technical-seo/audit_meta_report.json"
    out.write_text(json.dumps(report, indent=2))
    print(f"Total pages: {len(files)}")
    print(f"Pages with violations: {len(violations)}")
    print(f"Duplicate titles: {len(dup_titles)}")
    print(f"Duplicate descriptions: {len(dup_descs)}")
    print(f"Duplicate canonicals: {len(dup_canon)}")
    print(f"Report: {out}")
    if violations:
        print("\n--- Violations by page ---")
        for rel, vs in violations:
            print(f"  {rel}: {', '.join(vs)}")
    if dup_titles:
        print("\n--- Duplicate titles ---")
        for k, v in dup_titles.items():
            print(f"  {k[:80]!r}: {v}")
    if dup_descs:
        print("\n--- Duplicate descriptions ---")
        for k, v in dup_descs.items():
            print(f"  {k[:80]!r}: {v}")


if __name__ == "__main__":
    main()
