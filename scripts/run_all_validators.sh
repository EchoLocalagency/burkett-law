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
