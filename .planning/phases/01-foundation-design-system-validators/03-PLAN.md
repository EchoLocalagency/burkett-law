---
phase: 01-foundation-design-system-validators
plan: 03
type: execute
wave: 2
depends_on: [01]
files_modified:
  - scripts/validate_fabrication.py
  - scripts/lint_cal_bar.py
  - scripts/identity_guard.py
  - scripts/run_all_validators.sh
  - scripts/clients.json
  - scripts/content_facts.md
  - scripts/tests/fixtures/clean_sample.html
  - scripts/tests/fixtures/violate_cal_bar_sample.html
  - scripts/tests/fixtures/violate_fabrication_sample.html
  - scripts/tests/fixtures/violate_identity_sample.html
  - scripts/tests/test_validators.sh
  - .git/hooks/pre-commit
autonomous: true
requirements: [FND-11, FND-12]

must_haves:
  truths:
    - "Running scripts/lint_cal_bar.py against violate_cal_bar_sample.html exits non-zero and prints the specific banned patterns hit"
    - "Running scripts/validate_fabrication.py against violate_fabrication_sample.html exits non-zero and lists the fabricated claims"
    - "Running scripts/identity_guard.py against violate_identity_sample.html exits non-zero when it finds Mr Green's GA4 id, Arcadian's brand string, or a hardcoded GA4 id not in clients.json"
    - "Running all three validators against clean_sample.html exits zero"
    - "Attempting `git commit` on a staged file containing 'specialist' or 'guaranteed' or 'our team' or an unauthorized GA4 id is blocked by pre-commit hook"
    - "The blocked commit shows the specific validator + line that failed"
  artifacts:
    - path: "scripts/validate_fabrication.py"
      provides: "Content-fabrication regex validator (invented case counts, guarantee language, unsourced credentials, statistics without citation)"
      min_lines: 100
      contains: "def scan"
    - path: "scripts/lint_cal_bar.py"
      provides: "Cal Bar Rule 7.1-7.5 lint (specialist, guaranteed, best, top-rated, our team, expert-as-noun)"
      min_lines: 80
      contains: "specialist"
    - path: "scripts/identity_guard.py"
      provides: "Per-client identity guard (GA4 id must match clients.json entry; no cross-client brand strings)"
      min_lines: 80
      contains: "clients.json"
    - path: "scripts/clients.json"
      provides: "Per-client config (site slug, GA4 id, brand strings, allowed sameAs domains) — Burkett only for now"
      contains: "burkett"
    - path: "scripts/content_facts.md"
      provides: "Whitelist of Burkett-verified facts (bar admission year, bar number, JD school, undergrad, memberships) — validator allowlist source"
    - path: "scripts/run_all_validators.sh"
      provides: "Single entry point running all three validators over given files"
    - path: ".git/hooks/pre-commit"
      provides: "Pre-commit hook running run_all_validators.sh on staged .html files, blocking commit on non-zero exit"
  key_links:
    - from: ".git/hooks/pre-commit"
      to: "scripts/run_all_validators.sh"
      via: "bash exec on staged HTML files"
      pattern: "run_all_validators"
    - from: "scripts/identity_guard.py"
      to: "scripts/clients.json"
      via: "JSON load reads site's allowed GA4 id"
      pattern: "clients.json"
    - from: "scripts/validate_fabrication.py"
      to: "scripts/content_facts.md"
      via: "Reads allowlist of Burkett-verified numeric claims"
      pattern: "content_facts"
---

<objective>
Ship the three validator scripts that gate every content commit for the rest of the project: (1) Cal Bar Rule 7.1-7.5 copy lint (specialist, guaranteed, our team, best, top-rated, expert-as-noun, superlative unverifiable claims), (2) content-fabrication validator (invented case counts, statistics without citation, unsourced credentials, "since [year]" claims not verified, guarantee language, multi-person pronouns for a solo attorney), and (3) per-client identity guard (correct GA4 id from clients.json, no cross-client brand strings). Wire them into a pre-commit hook so a commit that violates any rule is blocked with a specific error.

Purpose: These three lints are the ENTIRE reason Phase 1 exists before Phase 2. Every YMYL content-generation phase downstream (bio → homepage → practice pillars → location pages → blog) MUST pass these on commit. The Mr Green fabrication incident (steam/enzyme/180°F claims that shipped and required a 39-file scrub) and the Mr Green → Arcadian GA4 pollution incident directly motivate these validators. Cal Bar Rule 7.1 violations are a bar complaint risk, not hypothetical. Ship the validators BEFORE writing a single real content page.

Output: Three Python scripts, one shell entry point, a clients.json, a content_facts.md allowlist, four test fixture HTMLs, a test runner shell script, and a wired .git/hooks/pre-commit. Every subsequent plan can rely on `bash scripts/run_all_validators.sh <file>` as the gate.
</objective>

<execution_context>
@/Users/brianegan/.claude/get-shit-done/workflows/execute-plan.md
@/Users/brianegan/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@/Users/brianegan/Desktop/burkett-law/.planning/PROJECT.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/PITFALLS.md
@/Users/brianegan/Desktop/burkett-law/.planning/research/STACK.md
@/Users/brianegan/CLAUDE.md

<interfaces>
<!-- Cal Bar + fabrication + identity regex list — extracted from PITFALLS.md Pitfalls 1, 3, and 11. Use verbatim. -->

Cal Bar Rule 7.1-7.5 BANNED patterns (case-insensitive, block commit):
- `\b(best|top[- ]rated|leading|#1|number one)\s+(divorce|family[ -]?law|custody|attorney|lawyer|firm)\b` — Rule 7.1 unsupported superlative
- `\bspecialist\b` — Rule 7.2 (unless CA Board of Legal Specialization certified — Burkett is not)
- `\bspecializes?\s+in\b` — Rule 7.2
- `\bexpert\b(?!ise)` — Rule 7.2 (block "expert" as noun; allow "expertise")
- `\bguarantee[sd]?\b` — Rule 7.1 (block "guarantee", "guarantees", "guaranteed")
- `\bwe (will )?win\b` — Rule 7.1
- `\bbest outcome\b` — Rule 7.1
- `\bproven results?\b` — Rule 7.1
- `\bour (team|attorneys|firm|lawyers|partners|associates)\b` — Rule 7.5 (Burkett is solo)
- `\baggressive (representation|attorney|lawyer|advocate)\b` — tone anti-pattern (DESIGN.md §12.2)
- `\bfight (for you|back|the other side)\b` — tone anti-pattern
- `\bcall now before it['']s too late\b` — false urgency

Fabrication patterns (block commit unless whitelisted in content_facts.md):
- `\b(over |more than )?\d{2,}\+?\s*(years?\s+of\s+(experience|practice)|cases|clients|families|matters)\b` — round-number claims must appear in content_facts.md
- `\b(recognized|awarded|named|voted)\s+.{0,40}(top|best|leading|super\s+lawyer|rising\s+star)\b` — award claims must be in content_facts.md
- `\bsince\s+\d{4}\b` — "since [year]" claim must be in content_facts.md
- `\b\d{1,3}\s*%\s+(success|win|favorable|satisfaction)\b` — percentage claim
- `\bLaw\s+Office\s+of\s+Brian\s+Burkett\s+Team\b` — solo practice pretending to be a team

Identity guard patterns:
- Any GA4 measurement id matching `G-[A-Z0-9]{10}` that is NOT listed in clients.json for this site.
- Known cross-client contamination strings (whichever the current site is NOT):
  - "Mr Green" / "MrGreen" / "mrgreenturfclean" (Mr Green Turf & Clean)
  - "Arcadian" / "arcadian-landscape"
  - "Ecosystem Lands" / "ecosystem-lands" / "ecosystemlands"
  - "SoCal Artificial Turfs" / "socal-artificial-turfs"
  - "Top Tier Custom Floors" / "toptiercustomfloors"
  - "Chef Dorothy" / "chefdorothy" / "primalplates"
  - "Tri City Turf" / "tricityturf"
  - "Integrity Pro" / "integritypro"
  - "Psychic Experience" / "psychicexperiencesd"
- Any "Echo Local" mention outside a footer credit line (Echo Local is Brian's agency, not Burkett)

clients.json schema (Burkett entry only for now):
```json
{
  "burkett-law": {
    "domain": "childcustodyanddivorce.com",
    "brand_name": "Law Office of Brian Burkett",
    "attorney_name": "Brian Burkett",
    "ga4_id": "G-BURKETT_PLACEHOLDER",
    "phone_e164": "+16192502683",
    "phone_display": "(619) 250-2683",
    "address_full": "591 Camino De La Reina, Suite 821, San Diego, CA 92108",
    "address_lines": {
      "street": "591 Camino De La Reina, Suite 821",
      "city": "San Diego",
      "state": "CA",
      "zip": "92108"
    },
    "hours_display": "Mon-Fri 9am-6pm",
    "allowed_ga4_ids": ["G-BURKETT_PLACEHOLDER"],
    "banned_cross_client_strings": [
      "Mr Green", "MrGreen", "mrgreenturfclean",
      "Arcadian", "arcadian-landscape",
      "Ecosystem Lands", "ecosystem-lands", "ecosystemlands",
      "SoCal Artificial Turfs", "socal-artificial-turfs",
      "Top Tier Custom Floors", "toptiercustomfloors",
      "Chef Dorothy", "chefdorothy", "primalplates",
      "Tri City Turf", "tricityturf",
      "Integrity Pro Washers", "integritypro",
      "Psychic Experience", "psychicexperiencesd",
      "G-PGEDP44QR4", "G-9T6N22F4XK", "G-BEYTH5X88Q"
    ]
  }
}
```

content_facts.md schema (Burkett-verified allowlist — empty until Brian fills):
```markdown
# Burkett Content Facts Allowlist

Any numeric claim (years of experience, case count, awards, "since [year]", etc.) in site content must appear here. If a fact isn't in this file, the fabrication validator will block commit. Facts added here require Brian's verification that they trace to the Justia archive or Burkett direct.

## Verified numeric claims

<!-- PENDING (Phase 2 gap — see STATE.md open gaps): Burkett's exact bar credentials still unconfirmed. Fill this file before Phase 2 bio page can pass validator. -->

## Verified awards / recognitions

None yet.

## Verified "since [year]" claims

None yet.
```
</interfaces>
</context>

<tasks>

<task type="auto" tdd="true">
  <name>Task 1: Write validator test fixtures + entry-point runner</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/clean_sample.html,
    /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_cal_bar_sample.html,
    /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_fabrication_sample.html,
    /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_identity_sample.html,
    /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh,
    /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh,
    /Users/brianegan/Desktop/burkett-law/scripts/clients.json,
    /Users/brianegan/Desktop/burkett-law/scripts/content_facts.md
  </files>
  <behavior>
    - clean_sample.html has zero banned patterns and passes all three validators (exit 0).
    - violate_cal_bar_sample.html contains "specialist", "guaranteed outcome", "best divorce attorney in San Diego", and "our team" — Cal Bar validator MUST exit non-zero listing each violation.
    - violate_fabrication_sample.html contains "20+ years of experience", "recognized as a top custody attorney", "since 2005", "95% success rate" — fabrication validator MUST exit non-zero.
    - violate_identity_sample.html contains "G-PGEDP44QR4" (Mr Green's GA4 id), a reference to "Mr Green" the brand, and "Ecosystem Lands" — identity guard MUST exit non-zero listing each.
    - test_validators.sh runs all three validators against all four fixtures and asserts the correct exit codes; exits 0 if all four assertions pass, non-zero otherwise.
    - run_all_validators.sh takes files as args, invokes each of the three validators, returns non-zero if ANY validator returns non-zero.
  </behavior>
  <action>
Create the FOUR fixtures FIRST (TDD RED phase — these represent the behavior we're locking down):

`clean_sample.html`: A minimal <!doctype html>...</html> page mentioning "Brian Burkett, Attorney at Law" + a plain "San Diego family law" line + a factual "Admitted to California State Bar" line WITHOUT the year (so fabrication doesn't fire without content_facts entry). Zero banned patterns. Contains one placeholder GA4 comment `<!-- GA4-BEGIN ... G-BURKETT_PLACEHOLDER ... GA4-END -->` (using Burkett's allowed id per clients.json).

`violate_cal_bar_sample.html`: Same skeleton as clean_sample.html but with body containing these five specific test strings, each on its own line so line numbers report distinctly:
- "Brian is a specialist in family law." (Rule 7.2)
- "We guarantee the best outcome for your divorce." (Rule 7.1)
- "The best divorce attorney in San Diego." (Rule 7.1 superlative)
- "Our team is committed to fighting for you." (Rule 7.5 + tone)
- "We will win your case." (Rule 7.1)

`violate_fabrication_sample.html`: Skeleton + body containing:
- "20+ years of experience in San Diego Superior Court." (fabrication — round number, needs allowlist)
- "Recognized as a top custody attorney by SD Legal Weekly." (fabrication — award claim, needs allowlist)
- "Serving families since 2005." (fabrication — "since [year]" claim, needs allowlist)
- "95% success rate on contested divorces." (fabrication — statistic)
- "The Law Office of Brian Burkett Team is here to help." (solo pretending to be a team)

`violate_identity_sample.html`: Skeleton + body + head containing:
- `<script async src="https://www.googletagmanager.com/gtag/js?id=G-PGEDP44QR4"></script>` (Mr Green's GA4 id — must fire identity guard)
- "Mr Green Turf & Clean has served San Diego..." (cross-client contamination)
- "About Ecosystem Lands" (cross-client contamination)

`clients.json` at /Users/brianegan/Desktop/burkett-law/scripts/clients.json: Copy VERBATIM from the interfaces block.

`content_facts.md` at /Users/brianegan/Desktop/burkett-law/scripts/content_facts.md: Copy VERBATIM from the interfaces block. This is deliberately empty of numeric claims — the intent is that Phase 2 (bio) fills it FIRST, then the bio page can pass the fabrication validator.

`run_all_validators.sh` at /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh:
```bash
#!/bin/bash
# Runs all three validators against provided file paths. Non-zero exit if ANY fails.
# Usage: bash scripts/run_all_validators.sh <file> [<file> ...]
# Called by .git/hooks/pre-commit with the list of staged .html files.

set -o pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STATUS=0

if [ "$#" -eq 0 ]; then
  echo "run_all_validators.sh: no files given; nothing to check." >&2
  exit 0
fi

python3 "$SCRIPT_DIR/lint_cal_bar.py" "$@" || STATUS=$?
python3 "$SCRIPT_DIR/validate_fabrication.py" "$@" || STATUS=$?
python3 "$SCRIPT_DIR/identity_guard.py" --site burkett-law "$@" || STATUS=$?

if [ "$STATUS" -ne 0 ]; then
  echo "" >&2
  echo "One or more validators failed. Commit blocked." >&2
  echo "Fix the issues above and re-stage the file(s)." >&2
fi
exit $STATUS
```
Make executable: `chmod +x /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh`

`test_validators.sh` at /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh:
```bash
#!/bin/bash
# Regression suite for the three validators. Run after any validator change.
# Asserts the fixtures behave as documented.
set -u
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
FIXTURES="$SCRIPT_DIR/fixtures"
FAILED=0

assert_pass() {  # $1 = validator cmd, $2 = fixture, $3 = label
  if $1 "$2" >/dev/null 2>&1; then
    echo "  ok   $3 on $(basename $2)"
  else
    echo "  FAIL $3 should PASS on $(basename $2)"
    FAILED=$((FAILED+1))
  fi
}
assert_fail() {  # $1 = validator cmd, $2 = fixture, $3 = label
  if ! $1 "$2" >/dev/null 2>&1; then
    echo "  ok   $3 on $(basename $2)"
  else
    echo "  FAIL $3 should FAIL on $(basename $2)"
    FAILED=$((FAILED+1))
  fi
}

echo "Cal Bar lint:"
assert_pass "python3 $REPO_ROOT/scripts/lint_cal_bar.py" "$FIXTURES/clean_sample.html" "cal_bar clean"
assert_fail "python3 $REPO_ROOT/scripts/lint_cal_bar.py" "$FIXTURES/violate_cal_bar_sample.html" "cal_bar violate"

echo "Fabrication validator:"
assert_pass "python3 $REPO_ROOT/scripts/validate_fabrication.py" "$FIXTURES/clean_sample.html" "fabrication clean"
assert_fail "python3 $REPO_ROOT/scripts/validate_fabrication.py" "$FIXTURES/violate_fabrication_sample.html" "fabrication violate"

echo "Identity guard:"
assert_pass "python3 $REPO_ROOT/scripts/identity_guard.py --site burkett-law" "$FIXTURES/clean_sample.html" "identity clean"
assert_fail "python3 $REPO_ROOT/scripts/identity_guard.py --site burkett-law" "$FIXTURES/violate_identity_sample.html" "identity violate"

if [ "$FAILED" -eq 0 ]; then
  echo ""
  echo "All 6 validator assertions passed."
  exit 0
fi
echo ""
echo "$FAILED validator assertions FAILED."
exit 1
```
Make executable.

At this point the tests EXIST but the validator scripts do NOT. Running test_validators.sh will fail with "command not found" on the python invocations — that is the expected RED state. Task 2 implements the validators to make tests pass (GREEN).
  </action>
  <verify>
    <automated>test -f /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/clean_sample.html && test -f /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_cal_bar_sample.html && test -f /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_fabrication_sample.html && test -f /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_identity_sample.html && test -f /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh && test -f /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh && test -f /Users/brianegan/Desktop/burkett-law/scripts/clients.json && test -f /Users/brianegan/Desktop/burkett-law/scripts/content_facts.md && test -x /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh && python3 -c "import json; d=json.load(open('/Users/brianegan/Desktop/burkett-law/scripts/clients.json')); assert d['burkett-law']['brand_name'] == 'Law Office of Brian Burkett'" && grep -q 'specialist' /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_cal_bar_sample.html && grep -q '20+ years' /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_fabrication_sample.html && grep -q 'G-PGEDP44QR4' /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_identity_sample.html && echo "PASS"</automated>
  </verify>
  <done>All four fixtures exist, test_validators.sh + run_all_validators.sh exist and are executable, clients.json is valid JSON with Burkett entry, content_facts.md exists with allowlist scaffold. Running test_validators.sh at this point returns non-zero (validators not implemented yet — expected RED).</done>
</task>

<task type="auto" tdd="true">
  <name>Task 2: Implement the three validator scripts (GREEN — make tests pass)</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/scripts/lint_cal_bar.py,
    /Users/brianegan/Desktop/burkett-law/scripts/validate_fabrication.py,
    /Users/brianegan/Desktop/burkett-law/scripts/identity_guard.py
  </files>
  <behavior>
    - Each script: `python3 <script>.py <file> [<file> ...]` — scans given files, prints one line per violation with file:line:col plus the pattern label, exits non-zero on any violation, exits 0 on none.
    - Cal Bar lint runs the 12 regex patterns from the interfaces block against each file's text (case-insensitive on English words). Skips content inside `<!-- ... -->` HTML comments and inside <script>/<style> tags.
    - Fabrication validator runs the 5 fabrication regexes; for each hit, checks whether the matched string appears in content_facts.md; if it does, ignore (whitelisted); otherwise report violation.
    - Identity guard: takes `--site <slug>` flag, loads clients.json, iterates:
      1. GA4 id extraction: for every `G-[A-Z0-9]{10}` in the file (skipping HTML comments), check membership in `clients.json[<slug>].allowed_ga4_ids`. Non-member = violation.
      2. Cross-client brand strings: for every entry in `clients.json[<slug>].banned_cross_client_strings`, case-insensitive substring search against the file body. Any hit = violation.
    - All three scripts return exit 0 if no files provided (defensive — pre-commit shouldn't fail on empty file list).
  </behavior>
  <action>
Implement all three validators. Use only stdlib (re, sys, json, pathlib, argparse). No external dependencies — must run on Brian's system Python 3 without pip installs.

`scripts/lint_cal_bar.py`:
```python
#!/usr/bin/env python3
"""Cal Bar Rule 7.1-7.5 copy lint.

Scans HTML files for language that violates California State Bar advertising rules.
Blocks: superlative unverifiable claims, "specialist"/"expert" absent CA Board
certification, guarantee language, multi-person pronouns for a solo practice,
and tone anti-patterns.

Exits non-zero if any pattern matches. Prints file:line:col + pattern label.
"""
import argparse, re, sys
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

# Strip <!-- ... --> and <script>...</script> and <style>...</style> from content
STRIP = re.compile(
    r"<!--.*?-->|<script[^>]*>.*?</script>|<style[^>]*>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def strip_non_content(text: str) -> str:
    """Replace comments/scripts/styles with same-length whitespace to preserve line numbers."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return STRIP.sub(blank, text)


def scan(path: Path) -> list[str]:
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
        print(f"\n[CAL_BAR] {len(all_violations)} violation(s). Fix before commit.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`scripts/validate_fabrication.py`:
```python
#!/usr/bin/env python3
"""Content-fabrication validator.

Scans HTML files for unverified numeric claims, award claims, "since [year]"
claims, statistics, and solo-pretending-to-be-team patterns. Any hit that isn't
whitelisted in scripts/content_facts.md blocks the commit.

Exists because YMYL (family law) can't ship fabricated claims — Mr Green
steam/enzyme/180F incident, June 2026, cost a 39-file scrub.
"""
import argparse, re, sys
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


def load_allowlist(facts_path: Path) -> set[str]:
    """Read content_facts.md; return set of lower-cased short strings to accept as verified."""
    if not facts_path.exists():
        return set()
    text = facts_path.read_text(encoding="utf-8", errors="replace").lower()
    return set(t.strip() for t in text.split("\n") if t.strip())


def scan(path: Path, allowlist: set[str]) -> list[str]:
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
        print(f"\n[FABRICATION] {len(all_violations)} unverified claim(s). Add to scripts/content_facts.md (with Burkett verification) or rewrite.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`scripts/identity_guard.py`:
```python
#!/usr/bin/env python3
"""Per-client identity guard.

Ensures every HTML file:
  1. Uses only GA4 ids listed in clients.json[<site>].allowed_ga4_ids
  2. Contains no cross-client brand strings from clients.json[<site>].banned_cross_client_strings

Motivated by the Mr Green -> Arcadian GA4 pollution incident (June 2026) and
the 2026-06-23 identity guard rebuild. This is the guard.
"""
import argparse, json, re, sys
from pathlib import Path

GA4_RX = re.compile(r"G-[A-Z0-9]{10}")
STRIP = re.compile(
    r"<!--.*?-->|<style[^>]*>.*?</style>",
    re.DOTALL | re.IGNORECASE,
)


def strip_non_content(text: str) -> str:
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return STRIP.sub(blank, text)


def scan(path: Path, allowed_ga4: set[str], banned_strings: list[str]) -> list[str]:
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
        print(f"[IDENTITY] scripts/clients.json missing — cannot enforce identity guard.", file=sys.stderr)
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
        print(f"\n[IDENTITY] {len(all_violations)} identity violation(s). Fix before commit.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Make all three executable: `chmod +x scripts/lint_cal_bar.py scripts/validate_fabrication.py scripts/identity_guard.py`.

Run `bash /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh` — MUST print "All 6 validator assertions passed." and exit 0. This is GREEN.

If any assertion fails, adjust the regex or fixture (NEVER both in the same fix — one at a time) and re-run until 6/6 pass.
  </action>
  <verify>
    <automated>chmod +x /Users/brianegan/Desktop/burkett-law/scripts/lint_cal_bar.py /Users/brianegan/Desktop/burkett-law/scripts/validate_fabrication.py /Users/brianegan/Desktop/burkett-law/scripts/identity_guard.py && bash /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh</automated>
  </verify>
  <done>All 6 assertions in test_validators.sh pass (clean fixture passes all three validators, each violate fixture fails its corresponding validator). Zero regex changes needed to make tests pass mean the interfaces block was right. If regex was tuned, note in SUMMARY.</done>
</task>

<task type="auto">
  <name>Task 3: Wire pre-commit hook + verify block-on-violation</name>
  <files>
    /Users/brianegan/Desktop/burkett-law/.git/hooks/pre-commit
  </files>
  <action>
Create `/Users/brianegan/Desktop/burkett-law/.git/hooks/pre-commit`:
```bash
#!/bin/bash
# Pre-commit hook for burkett-law: runs the three validators on staged HTML files.
# Bypass in emergency with `git commit --no-verify` (do NOT normalize this — track it).

set -o pipefail
REPO_ROOT="$(git rev-parse --show-toplevel)"
STAGED_HTML=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.html?$' || true)

if [ -z "$STAGED_HTML" ]; then
  exit 0
fi

# Convert to absolute paths for run_all_validators.sh
ABS_FILES=""
for f in $STAGED_HTML; do
  ABS_FILES="$ABS_FILES $REPO_ROOT/$f"
done

bash "$REPO_ROOT/scripts/run_all_validators.sh" $ABS_FILES
```
Make executable: `chmod +x /Users/brianegan/Desktop/burkett-law/.git/hooks/pre-commit`

Verify the hook blocks a bad commit:
1. Copy `scripts/tests/fixtures/violate_cal_bar_sample.html` to `_test_bad.html` at the repo root.
2. `cd /Users/brianegan/Desktop/burkett-law && git add _test_bad.html`
3. Attempt `git commit -m "should be blocked"` — MUST exit non-zero, MUST print [CAL_BAR][RULE_7_2_SPECIALIST] and [CAL_BAR][RULE_7_1_GUARANTEE] etc. to stderr.
4. `git reset HEAD _test_bad.html && rm _test_bad.html`

Then verify the hook allows a clean commit:
1. Copy `scripts/tests/fixtures/clean_sample.html` to `_test_good.html`.
2. `git add _test_good.html`
3. Attempt `git commit -m "should pass"` — MUST succeed (exit 0).
4. Roll back: `git reset --soft HEAD~1 && git reset HEAD _test_good.html && rm _test_good.html`

Then commit the actual scripts + fixtures + hook + configs:
1. `git add scripts/ .git/hooks/pre-commit` — NOTE: `.git/hooks/` is NOT tracked by git; do NOT try to `git add` it. Instead, copy the pre-commit hook to `scripts/git-hooks/pre-commit` and add THAT to the repo as the source-of-truth, plus a `scripts/install_hooks.sh` that symlinks/copies it into `.git/hooks/`. Adjust the file list accordingly:
   - Create `scripts/git-hooks/pre-commit` with the same content as `.git/hooks/pre-commit`.
   - Create `scripts/install_hooks.sh`:
     ```bash
     #!/bin/bash
     # Install repo git hooks into .git/hooks/
     REPO_ROOT="$(git rev-parse --show-toplevel)"
     cp "$REPO_ROOT/scripts/git-hooks/pre-commit" "$REPO_ROOT/.git/hooks/pre-commit"
     chmod +x "$REPO_ROOT/.git/hooks/pre-commit"
     echo "Installed pre-commit hook."
     ```
   - Make install_hooks.sh executable.
2. Update README.md footer with one line: "After clone: run `bash scripts/install_hooks.sh` to install the pre-commit validators."
3. `git add scripts/ README.md`
4. `git commit -m "feat(01-03): content-fabrication + Cal Bar Rule 7.1 lint + identity guard + pre-commit hook" -m "" -m "Three validator scripts (lint_cal_bar, validate_fabrication, identity_guard) + clients.json + content_facts.md allowlist + 4 test fixtures + test_validators.sh regression suite + scripts/git-hooks/pre-commit + scripts/install_hooks.sh. Motivated by Mr Green fabrication scrub (39 files), Mr Green -> Arcadian GA4 pollution, and California State Bar Rule 7.1-7.5 exposure. Every content commit downstream must pass all three before Netlify auto-deploys."`
5. Push if origin is set: `git push`.
  </action>
  <verify>
    <automated>test -x /Users/brianegan/Desktop/burkett-law/.git/hooks/pre-commit && test -f /Users/brianegan/Desktop/burkett-law/scripts/git-hooks/pre-commit && test -x /Users/brianegan/Desktop/burkett-law/scripts/install_hooks.sh && cd /Users/brianegan/Desktop/burkett-law && cp scripts/tests/fixtures/violate_cal_bar_sample.html /tmp/_hook_test_bad.html && git add /tmp/_hook_test_bad.html 2>/dev/null; RESULT=$(bash scripts/run_all_validators.sh /tmp/_hook_test_bad.html 2>&1; echo "EXIT:$?"); rm -f /tmp/_hook_test_bad.html; echo "$RESULT" | grep -q "EXIT:1" && echo "$RESULT" | grep -q "CAL_BAR" && echo "PASS"</automated>
  </verify>
  <done>.git/hooks/pre-commit exists and is executable, scripts/git-hooks/pre-commit exists as tracked source, scripts/install_hooks.sh exists as installer, `bash scripts/run_all_validators.sh <bad_file>` exits 1 and lists CAL_BAR violations. Feature commit 01-03 exists in git log.</done>
</task>

</tasks>

<verification>
Phase 1 Plan 03 verification:
- `bash /Users/brianegan/Desktop/burkett-law/scripts/tests/test_validators.sh` prints "All 6 validator assertions passed." and exits 0.
- `bash /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/violate_cal_bar_sample.html` exits 1 with CAL_BAR violations printed.
- `bash /Users/brianegan/Desktop/burkett-law/scripts/run_all_validators.sh /Users/brianegan/Desktop/burkett-law/scripts/tests/fixtures/clean_sample.html` exits 0.
- Pre-commit hook is installed at `.git/hooks/pre-commit` and source-of-truth at `scripts/git-hooks/pre-commit`.
- Clean sample fixture uses only "G-BURKETT_PLACEHOLDER" (the id listed in clients.json allowed_ga4_ids) and contains no cross-client strings — identity guard passes.
</verification>

<success_criteria>
- Three validator scripts (lint_cal_bar, validate_fabrication, identity_guard) run cleanly on clean fixture and block appropriately on each violating fixture
- clients.json has Burkett entry with GA4 allowed_ids + full banned_cross_client_strings list including known contaminating brand names and known other-client GA4 ids
- content_facts.md exists as an empty allowlist; Phase 2 (bio) is the first plan that MUST fill it before its bio page can pass fabrication validator
- Pre-commit hook wired via scripts/git-hooks/pre-commit + install_hooks.sh, and installed at .git/hooks/pre-commit
- test_validators.sh regression suite passes (6/6 assertions)
- Feature commit 01-03 exists
</success_criteria>

<output>
After completion, create `.planning/phases/01-foundation-design-system-validators/01-03-SUMMARY.md` recording:
- Any regex adjustments made vs the interfaces block (should be zero if fixtures/patterns matched)
- Note that content_facts.md is DELIBERATELY EMPTY — Phase 2 (bio) must add entries for Burkett's bar admission year, bar number, JD school, undergrad school, and any verified experience claims BEFORE the bio page can pass fabrication validator. This is the intended forcing function.
- Confirm clients.json GA4 id is a placeholder (G-BURKETT_PLACEHOLDER) — Phase 6 (Analytics) replaces with the real GA4 id after property is created
- Confirm Brian must run `bash scripts/install_hooks.sh` on every fresh clone
</output>
