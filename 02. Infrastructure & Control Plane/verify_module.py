#!/usr/bin/env python3
"""Session 2 — Verify Module Setup

Checks that all prerequisites for Session 2 are in place.
Run: python3 verify_module.py
"""

import sys
import os
import shutil
import subprocess

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
WARN = "\033[93mWARN\033[0m"

results = []


def check(name, passed, message=""):
    status = PASS if passed else FAIL
    results.append(passed)
    detail = f" — {message}" if message else ""
    print(f"  [{status}] {name}{detail}")


def check_command(name, cmd, min_version=None):
    """Check if a CLI tool is available."""
    path = shutil.which(cmd)
    if path:
        try:
            version = subprocess.run(
                [cmd, "version"] if cmd in ["kubectl", "kind", "helm", "pulumi"] else [cmd, "--version"],
                capture_output=True, text=True, timeout=10
            )
            ver_str = (version.stdout + version.stderr).strip().split("\n")[0][:60]
            check(name, True, ver_str)
        except Exception:
            check(name, True, f"Found at {path}")
    else:
        check(name, False, "Not installed")


def main():
    print("=" * 60)
    print("Session 2 — Module Verification")
    print("=" * 60)

    # Python version
    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    # CLI tools
    print("\n--- CLI Tools ---")
    check_command("Docker", "docker")
    check_command("Kind", "kind")
    check_command("kubectl", "kubectl")
    check_command("Pulumi", "pulumi")

    # Python packages
    print("\n--- Python Packages ---")
    for pkg, import_name in [("pulumi", "pulumi"), ("pulumi-kubernetes", "pulumi_kubernetes")]:
        try:
            __import__(import_name)
            check(pkg, True)
        except ImportError:
            check(pkg, False, "pip3 install {} --break-system-packages".format(pkg))

    # Kind cluster running
    print("\n--- Cluster ---")
    try:
        result = subprocess.run(
            ["kind", "get", "clusters"], capture_output=True, text=True, timeout=10
        )
        clusters = result.stdout.strip().split("\n") if result.stdout.strip() else []
        has_workshop = "workshop" in clusters
        check("Kind cluster 'workshop'", has_workshop,
              "Run: kind create cluster --name workshop" if not has_workshop else "Running")
    except FileNotFoundError:
        check("Kind cluster 'workshop'", False, "Kind not installed")

    # Required files
    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["namespace-provisioner.py", "rbac-platform-admin.yaml", "platform-services.yaml"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["multi-env-config.yaml", "rbac-developer-role.yaml",
              "demo-app-deployment.yaml", "test-cluster-health.py", "test-rbac-permissions.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    # Summary
    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 2 is ready to go!")
    else:
        print("Fix the issues above before starting Session 2.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
