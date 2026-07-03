#!/usr/bin/env python3
"""Cal Bar Rule 7.1-7.5 copy lint.

Scans HTML files for language that violates California State Bar advertising rules.
Blocks: superlative unverifiable claims, "specialist"/"expert" absent CA Board
certification, guarantee language, multi-person pronouns for a solo practice,
and tone anti-patterns.

Exits non-zero if any pattern matches. Prints file:line:col + pattern label.
"""
import argparse
import re
import sys
from pathlib import Path

PATTERNS = [
    ("RULE_7_1_SUPERLATIVE",
     r"\b(best|top[- ]rated|leading|#1|number one)\s+(divorce|family[ -]?law|custody|attorney|lawyer|firm)\b"),
    ("RULE_7_2_SPECIALIST", r"\bspecialist\b"),
    ("RULE_7_2_SPECIALIZES", r"\bspecializes?\s+in\b"),
    ("RULE_7_2_EXPERT", r"\bexpert\b(?!ise)"),
    ("RULE_7_1_GUARANTEE", r"\bguarantee[sd]?\b"),
    ("RULE_7_1_WE_WIN", r"\bwe (will )?win\b"),
    ("RULE_7_1_BEST_OUTCOME", r"\bbest outcome\b"),
    ("RULE_7_1_PROVEN_RESULTS", r"\bproven results?\b"),
    ("RULE_7_5_SOLO_TEAM", r"\bour (team|attorneys|firm|lawyers|partners|associates)\b"),
    ("TONE_AGGRESSIVE", r"\baggressive (representation|attorney|lawyer|advocate)\b"),
    ("TONE_FIGHT", r"\bfight (for you|back|the other side)\b"),
    ("TONE_URGENCY", r"\bcall now before it['’]s too late\b"),
]

COMPILED = [(label, re.compile(pat, re.IGNORECASE)) for label, pat in PATTERNS]

# Strip <!-- ... --> and <script>...</script> and <style>...</style> from content.
# Preserves line numbers by replacing non-newline chars with spaces.
STRIP = re.compile(
    r"<!--.*?-->|<script[^>]*>.*?</script>|<style[^>]*>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def strip_non_content(text: str) -> str:
    """Replace comments/scripts/styles with same-length whitespace to preserve line numbers."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return STRIP.sub(blank, text)


def scan(path: Path):
    """Return list of violation strings for a file."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [f"{path}:0:0: READ_ERROR: {e}"]
    stripped = strip_non_content(raw)
    violations = []
    for label, rx in COMPILED:
        for m in rx.finditer(stripped):
            line = stripped.count("\n", 0, m.start()) + 1
            col = m.start() - stripped.rfind("\n", 0, m.start())
            violations.append(f"{path}:{line}:{col}: [CAL_BAR][{label}] '{m.group(0)}'")
    return violations


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if not args.files:
        return 0
    all_violations = []
    for f in args.files:
        p = Path(f)
        if not p.exists() or p.suffix.lower() not in {".html", ".htm"}:
            continue
        all_violations.extend(scan(p))
    for v in all_violations:
        print(v, file=sys.stderr)
    if all_violations:
        print(
            f"\n[CAL_BAR] {len(all_violations)} violation(s). Fix before commit.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
