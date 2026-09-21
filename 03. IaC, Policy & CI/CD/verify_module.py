#!/usr/bin/env python3
"""Session 3 — Verify Module Setup

Checks that all prerequisites for Session 3 are in place.
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


def check_command(name, cmd):
    path = shutil.which(cmd)
    if path:
        try:
            version_flag = "version" if cmd in ("kubectl", "helm", "kind", "pulumi") else "--version"
            result = subprocess.run(
                [cmd, version_flag], capture_output=True, text=True, timeout=10
            )
            ver = (result.stdout + result.stderr).strip().split("\n")[0][:60]
            check(name, True, ver)
        except Exception:
            check(name, True, f"Found at {path}")
    else:
        check(name, False, "Not installed")


def main():
    print("=" * 60)
    print("Session 3 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- CLI Tools ---")
    check_command("kubectl", "kubectl")
    check_command("Helm", "helm")
    check_command("conftest", "conftest")
    check_command("pre-commit", "pre-commit")

    # Crossplane installed in cluster
    print("\n--- Cluster Components ---")
    try:
        result = subprocess.run(
            ["kubectl", "get", "ns", "crossplane-system", "--no-headers"],
            capture_output=True, text=True, timeout=10
        )
        check("Crossplane namespace", result.returncode == 0,
              "Run: helm install crossplane crossplane-stable/crossplane -n crossplane-system --create-namespace"
              if result.returncode != 0 else "Installed")
    except FileNotFoundError:
        check("Crossplane namespace", False, "kubectl not available")

    print("\n--- Python Packages ---")
    try:
        import flask
        check("flask", True)
    except ImportError:
        check("flask", False, "pip3 install flask --break-system-packages")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["xrd-postgresql.yaml", "composition-postgresql.yaml",
              "demo-app-database.yaml", "backstage-ai-template.yaml",
              "crossplane-providers.yaml"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["backend-pipeline.yml", "guardrail-validator.py",
              "test-infrastructure.py", ".pre-commit-config.yaml"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 3 is ready to go!")
    else:
        print("Fix the issues above before starting Session 3.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
