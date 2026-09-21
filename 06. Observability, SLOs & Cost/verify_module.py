#!/usr/bin/env python3
"""Session 6 — Verify Module Setup

Checks that all prerequisites for Session 6 are in place.
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
    print("Session 6 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- Python Packages ---")
    for pkg, import_name, install in [
        ("pyyaml", "yaml", "pyyaml"),
        ("requests", "requests", "requests"),
        ("scikit-learn", "sklearn", "scikit-learn"),
    ]:
        try:
            __import__(import_name)
            check(pkg, True)
        except ImportError:
            check(pkg, False, f"pip3 install {install} --break-system-packages")

    print("\n--- CLI Tools ---")
    for cmd in ["kubectl", "helm"]:
        check(cmd, shutil.which(cmd) is not None,
              "Installed" if shutil.which(cmd) else "Not installed")

    # Prometheus installed
    print("\n--- Cluster Components ---")
    try:
        result = subprocess.run(
            ["kubectl", "get", "ns", "monitoring", "--no-headers"],
            capture_output=True, text=True, timeout=10
        )
        check("Prometheus (monitoring namespace)", result.returncode == 0,
              "Installed" if result.returncode == 0
              else "Run: helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --create-namespace")
    except FileNotFoundError:
        check("Prometheus (monitoring namespace)", False, "kubectl not available")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["otel-collector-config.yaml", "otel-collector-deployment.yaml",
              "sloth-auth-service-slo.yaml", "cost-analyzer.py", "alert-correlator.py"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["instrument-app.py", "alert-rules.yaml", "checkout-api-hpa.yaml",
              "checkout-api-vpa.yaml", "cost-allocation-labels.py",
              "cost-anomaly-detector.py", "observability-personas.py",
              "ai-agent-observability.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 6 is ready to go!")
    else:
        print("Fix the issues above before starting Session 6.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
