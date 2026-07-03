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
