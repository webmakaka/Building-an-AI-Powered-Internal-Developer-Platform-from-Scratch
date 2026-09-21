#!/usr/bin/env python3
"""Session 4 — Verify Module Setup

Checks that all prerequisites for Session 4 (Day 1 Integration) are in place.
Run: python3 verify_module.py
"""

import sys
import os
import shutil
import subprocess

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
    print("Session 4 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- CLI Tools ---")
    for cmd in ["kubectl", "helm"]:
        check(cmd, shutil.which(cmd) is not None,
              "Installed" if shutil.which(cmd) else "Not installed")

    # Verify cluster is running
    print("\n--- Cluster Status ---")
    try:
        result = subprocess.run(
            ["kubectl", "cluster-info"], capture_output=True, text=True, timeout=10
        )
        check("Cluster reachable", result.returncode == 0,
              "Cluster is running" if result.returncode == 0 else "Cannot reach cluster")
    except FileNotFoundError:
        check("Cluster reachable", False, "kubectl not installed")

    # Verify Sessions 2-3 setup
    try:
        result = subprocess.run(
            ["kubectl", "get", "ns", "--no-headers"], capture_output=True, text=True, timeout=10
        )
        namespaces = result.stdout.strip().split("\n") if result.stdout.strip() else []
        ns_names = [ns.split()[0] for ns in namespaces if ns.strip()]
        check("Team namespaces exist", any("team" in ns for ns in ns_names),
              "Namespaces from Session 2 present" if any("team" in ns for ns in ns_names)
              else "Run Session 2 demo first")
    except FileNotFoundError:
        check("Team namespaces exist", False, "kubectl not installed")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["test-cluster-health.py", "test-infrastructure.py", "test-policies.py"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 4 is ready to go!")
    else:
        print("Fix the issues above before starting Session 4.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
