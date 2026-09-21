#!/usr/bin/env python3
"""Session 9 — Verify Module Setup

Checks that all prerequisites for Session 9 are in place.
Run: python3 verify_module.py
"""

import sys
import os

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

results = []


def check(name, passed, message=""):
    status = PASS if passed else FAIL
    results.append(passed)
    detail = f" — {message}" if message else ""
    print(f"  [{status}] {name}{detail}")


def main():
    print("=" * 60)
    print("Session 9 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- Python Packages ---")
    for pkg, import_name, install in [
        ("pyyaml", "yaml", "pyyaml"),
        ("scikit-learn", "sklearn", "scikit-learn"),
    ]:
        try:
            __import__(import_name)
            check(pkg, True)
        except ImportError:
            check(pkg, False, f"pip3 install {install} --break-system-packages")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["team-topology-generator.py", "platform-kpi-collector.py",
              "measure-ai-impact.py"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["platform-maturity-assessment.py", "cost-analyzer.py",
              "friction-analyzer.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    # Check Session 1 baseline exists
    print("\n--- Cross-Session ---")
    s1_demo = os.path.join(os.path.dirname(__file__), "..", "Session1", "demo",
                           "platform-maturity-assessment.py")
    check("Session 1 baseline script reachable", os.path.exists(s1_demo),
          "Can compare Day 1 vs Day 2 scores")

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 9 is ready to go!")
    else:
        print("Fix the issues above before starting Session 9.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
