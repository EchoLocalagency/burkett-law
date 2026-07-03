#!/usr/bin/env python3
"""Content-fabrication validator.

Scans HTML files for unverified numeric claims, award claims, "since [year]"
claims, statistics, and solo-pretending-to-be-team patterns. Any hit that isn't
whitelisted in scripts/content_facts.md blocks the commit.

Exists because YMYL (family law) can't ship fabricated claims — Mr Green
steam/enzyme/180F incident, June 2026, cost a 39-file scrub.
"""
import argparse
import re
import sys
from pathlib import Path

PATTERNS = [
    ("FAB_YEARS_OR_COUNT",
     r"\b(over |more than )?\d{2,}\+?\s*(years?\s+of\s+(experience|practice)|cases|clients|families|matters)\b"),
    ("FAB_AWARD",
     r"\b(recognized|awarded|named|voted)\s+.{0,40}(top|best|leading|super\s+lawyer|rising\s+star)\b"),
    ("FAB_SINCE_YEAR", r"\bsince\s+\d{4}\b"),
    ("FAB_PERCENTAGE",
     r"\b\d{1,3}\s*%\s+(success|win|favorable|satisfaction)\b"),
    ("FAB_SOLO_TEAM", r"\bLaw\s+Office\s+of\s+Brian\s+Burkett\s+Team\b"),
]

COMPILED = [(label, re.compile(pat, re.IGNORECASE)) for label, pat in PATTERNS]

STRIP = re.compile(
    r"<!--.*?-->|<script[^>]*>.*?</script>|<style[^>]*>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def strip_non_content(text: str) -> str:
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return STRIP.sub(blank, text)


def load_allowlist(facts_path: Path):
    """Read content_facts.md; return set of lower-cased short strings to accept as verified."""
    if not facts_path.exists():
        return set()
    text = facts_path.read_text(encoding="utf-8", errors="replace").lower()
    return set(t.strip() for t in text.split("\n") if t.strip())


def scan(path: Path, allowlist):
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [f"{path}:0:0: READ_ERROR: {e}"]
    stripped = strip_non_content(raw)
    violations = []
    for label, rx in COMPILED:
        for m in rx.finditer(stripped):
            match_text = m.group(0).lower().strip()
            # Whitelisted if a content_facts.md line contains the match text
            if any(match_text in line for line in allowlist):
                continue
            line = stripped.count("\n", 0, m.start()) + 1
            col = m.start() - stripped.rfind("\n", 0, m.start())
            violations.append(
                f"{path}:{line}:{col}: [FABRICATION][{label}] '{m.group(0)}' — add to scripts/content_facts.md if verified"
            )
    return violations


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if not args.files:
        return 0
    repo = Path(__file__).resolve().parent.parent
    allowlist = load_allowlist(repo / "scripts" / "content_facts.md")
    all_violations = []
    for f in args.files:
        p = Path(f)
        if not p.exists() or p.suffix.lower() not in {".html", ".htm"}:
            continue
        all_violations.extend(scan(p, allowlist))
    for v in all_violations:
        print(v, file=sys.stderr)
    if all_violations:
        print(
            f"\n[FABRICATION] {len(all_violations)} unverified claim(s). Add to scripts/content_facts.md (with Burkett verification) or rewrite.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
