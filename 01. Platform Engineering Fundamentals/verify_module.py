#!/usr/bin/env python3
"""Session 1 — Verify Module Setup

Checks that all prerequisites for Session 1 are in place.
Run: python3 verify_module.py
"""

import sys
import os
import shutil

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
WARN = "\033[93mWARN\033[0m"

results = []


def check(name, passed, message=""):
    status = PASS if passed else FAIL
    results.append(passed)
    detail = f" — {message}" if message else ""
    print(f"  [{status}] {name}{detail}")


def main():
    print("=" * 60)
    print("Session 1 — Module Verification")
    print("=" * 60)

    # Python version
    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    # Required files
    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["platform-maturity-assessment.py", "platform-config.yaml"]:
        path = os.path.join(demo_dir, f)
        check(f, os.path.exists(path))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["design-principles-checklist.py", "devex-survey.py",
              "friction-analyzer.py", "platform-kpi-collector.py"]:
        path = os.path.join(takehome_dir, f)
        check(f, os.path.exists(path))

    # Summary
    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 1 is ready to go!")
    else:
        print("Fix the issues above before starting Session 1.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
