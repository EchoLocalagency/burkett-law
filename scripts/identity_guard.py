#!/usr/bin/env python3
"""Per-client identity guard.

Ensures every HTML file:
  1. Uses only GA4 ids listed in clients.json[<site>].allowed_ga4_ids
  2. Contains no cross-client brand strings from clients.json[<site>].banned_cross_client_strings

Motivated by the Mr Green -> Arcadian GA4 pollution incident (June 2026) and
the 2026-06-23 identity guard rebuild. This is the guard.
"""
import argparse
import json
import re
import sys
from pathlib import Path

GA4_RX = re.compile(r"G-[A-Z0-9]{10}")

# Strip HTML comments + style blocks (but NOT scripts — GA4 ids live in script tags
# and cross-client brand strings can too). Preserves line numbers.
STRIP = re.compile(
    r"<!--.*?-->|<style[^>]*>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def strip_non_content(text: str) -> str:
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return STRIP.sub(blank, text)


def scan(path: Path, allowed_ga4, banned_strings):
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [f"{path}:0:0: READ_ERROR: {e}"]
    stripped = strip_non_content(raw)
    violations = []
    for m in GA4_RX.finditer(stripped):
        gid = m.group(0)
        if gid not in allowed_ga4:
            line = stripped.count("\n", 0, m.start()) + 1
            violations.append(
                f"{path}:{line}:0: [IDENTITY][GA4_MISMATCH] '{gid}' not in allowed_ga4_ids"
            )
    lower = stripped.lower()
    for s in banned_strings:
        needle = s.lower()
        idx = lower.find(needle)
        while idx != -1:
            line = stripped.count("\n", 0, idx) + 1
            violations.append(
                f"{path}:{line}:0: [IDENTITY][CROSS_CLIENT] '{s}' (banned cross-client string)"
            )
            idx = lower.find(needle, idx + 1)
    return violations


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True, help="Site slug from clients.json")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if not args.files:
        return 0
    repo = Path(__file__).resolve().parent.parent
    clients_path = repo / "scripts" / "clients.json"
    if not clients_path.exists():
        print(
            "[IDENTITY] scripts/clients.json missing — cannot enforce identity guard.",
            file=sys.stderr,
        )
        return 2
    clients = json.loads(clients_path.read_text(encoding="utf-8"))
    if args.site not in clients:
        print(f"[IDENTITY] site '{args.site}' not in clients.json", file=sys.stderr)
        return 2
    cfg = clients[args.site]
    allowed_ga4 = set(cfg.get("allowed_ga4_ids", []))
    banned = list(cfg.get("banned_cross_client_strings", []))
    all_violations = []
    for f in args.files:
        p = Path(f)
        if not p.exists() or p.suffix.lower() not in {".html", ".htm"}:
            continue
        all_violations.extend(scan(p, allowed_ga4, banned))
    for v in all_violations:
        print(v, file=sys.stderr)
    if all_violations:
        print(
            f"\n[IDENTITY] {len(all_violations)} identity violation(s). Fix before commit.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
