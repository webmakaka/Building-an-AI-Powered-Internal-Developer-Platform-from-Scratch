#!/usr/bin/env python3
"""Session 5 — Verify Module Setup

Checks that all prerequisites for Session 5 are in place.
Run: python3 verify_module.py
"""

import sys
import os
import shutil

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
    print("Session 5 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- Python Packages ---")
    for pkg, import_name, install in [
        ("scikit-learn", "sklearn", "scikit-learn"),
        ("flask", "flask", "flask"),
        ("pyyaml", "yaml", "pyyaml"),
    ]:
        try:
            __import__(import_name)
            check(pkg, True)
        except ImportError:
            check(pkg, False, f"pip3 install {install} --break-system-packages")

    print("\n--- CLI Tools ---")
    check("kubectl", shutil.which("kubectl") is not None,
          "Installed" if shutil.which("kubectl") else "Not installed")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["project-bootstrapper.py", "rag-platform-docs.py",
              "catalog-info.yaml", "app-config.yaml", "audit_logger.py"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["onboarding-api.py", "validate-workflow.py", "test-onboarding.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 5 is ready to go!")
    else:
        print("Fix the issues above before starting Session 5.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
