#!/usr/bin/env python3
"""Pairwise word-set Jaccard similarity between all 20 location pages.
Prints word counts + the max similarity pair. Exits non-zero if any pair >= 0.70.
"""
import re
import sys
from pathlib import Path
from itertools import combinations

ROOT = Path(__file__).resolve().parent.parent
STOP = set("""
a an the and or but of on in for to with by from as at is are was were be been being have has had do does did
this that these those i my me you your we our us they them their he she his her it its
if then so than not no yes will would should could can may might shall must
who what which where when why how
one two three four five six seven eight nine ten
""".split())

STRIP = re.compile(r"<[^>]+>", re.DOTALL)
SCRIPT_STRIP = re.compile(
    r"<script[^>]*>.*?</script>|<style[^>]*>.*?</style>|<!--.*?-->",
    re.DOTALL | re.IGNORECASE,
)
TOKEN = re.compile(r"[a-zA-Z]{3,}")


def visible_words(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    # Strip scripts/styles/comments
    raw = SCRIPT_STRIP.sub(" ", raw)
    # Strip HTML tags
    txt = STRIP.sub(" ", raw)
    words = [w.lower() for w in TOKEN.findall(txt)]
    words = [w for w in words if w not in STOP]
    return words


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main():
    pages = sorted((ROOT / "san-diego").glob("*/*/index.html"))
    print(f"Found {len(pages)} pages.\n")
    data = {}
    for p in pages:
        words = visible_words(p)
        data[p] = (len(words), set(words))
    print("Word counts (visible, stopwords removed):")
    for p, (n, _) in data.items():
        rel = p.relative_to(ROOT)
        print(f"  {n:5d}  {rel}")
    print()
    print("Pairwise Jaccard (word-set) similarity:")
    max_sim = 0.0
    max_pair = (None, None)
    over_70 = []
    for (p1, (_, s1)), (p2, (_, s2)) in combinations(data.items(), 2):
        j = jaccard(s1, s2)
        if j > max_sim:
            max_sim = j
            max_pair = (p1, p2)
        if j >= 0.70:
            over_70.append((j, p1, p2))
    print(f"  MAX similarity: {max_sim:.4f}")
    print(f"  MAX pair: {max_pair[0].relative_to(ROOT)}  |  {max_pair[1].relative_to(ROOT)}")
    if over_70:
        print(f"\n{len(over_70)} pair(s) at or above 0.70 threshold:")
        for j, p1, p2 in over_70:
            print(f"  {j:.4f}  {p1.relative_to(ROOT)}  |  {p2.relative_to(ROOT)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
