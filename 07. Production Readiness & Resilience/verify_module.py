#!/usr/bin/env python3
"""Session 7 — Verify Module Setup

Checks that all prerequisites for Session 7 are in place.
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
    print("Session 7 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- CLI Tools ---")
    for cmd in ["kubectl", "helm"]:
        check(cmd, shutil.which(cmd) is not None,
              "Installed" if shutil.which(cmd) else "Not installed")

    # Chaos Mesh installed
    print("\n--- Cluster Components ---")
    try:
        result = subprocess.run(
            ["kubectl", "get", "ns", "chaos-mesh", "--no-headers"],
            capture_output=True, text=True, timeout=10
        )
        check("Chaos Mesh namespace", result.returncode == 0,
              "Installed" if result.returncode == 0
              else "Run: helm install chaos-mesh chaos-mesh/chaos-mesh -n chaos-mesh --create-namespace")
    except FileNotFoundError:
        check("Chaos Mesh namespace", False, "kubectl not available")

    # Velero
    check("velero CLI", shutil.which("velero") is not None,
          "Installed" if shutil.which("velero") else "See https://velero.io/docs/main/basic-install/")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["chaos-network-delay.yaml", "canary-deployment.yaml",
              "chaos-runner.py", "rollback-controller.py", "runbook-automator.py"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["chaos-experiment-pod-kill.yaml", "chaos-mesh-pod-failure.yaml",
              "blue-green-deployment.yaml", "velero-storage-location.yaml",
              "velero-schedule.yaml", "backup-automation.py",
              "restore-validation.sh", "security-scan.yaml", "test-resilience.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 7 is ready to go!")
    else:
        print("Fix the issues above before starting Session 7.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
