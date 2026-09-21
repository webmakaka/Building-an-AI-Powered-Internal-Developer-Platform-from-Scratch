#!/usr/bin/env python3
"""Session 8 — Verify Module Setup

Checks that all prerequisites for Session 8 are in place.
Run: python3 verify_module.py
"""

import sys
import os

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
WARN = "\033[93mWARN\033[0m"

results = []


def check(name, passed, message=""):
    status = PASS if passed else FAIL
    results.append(passed)
    detail = f" — {message}" if message else ""
    print(f"  [{status}] {name}{detail}")


def info(name, message):
    print(f"  [{WARN}] {name} — {message}")


def main():
    print("=" * 60)
    print("Session 8 — Module Verification")
    print("=" * 60)

    print("\n--- Python ---")
    v = sys.version_info
    check("Python 3.10+", v.major == 3 and v.minor >= 10,
          f"Found {v.major}.{v.minor}.{v.micro}")

    print("\n--- Python Packages ---")
    for pkg, import_name, install in [
        ("scikit-learn", "sklearn", "scikit-learn"),
        ("pyyaml", "yaml", "pyyaml"),
    ]:
        try:
            __import__(import_name)
            check(pkg, True)
        except ImportError:
            check(pkg, False, f"pip3 install {install} --break-system-packages")

    # Optional: Anthropic API key
    print("\n--- Optional: LLM Features ---")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key:
        info("ANTHROPIC_API_KEY", "Set (Claude LLM features enabled)")
    else:
        info("ANTHROPIC_API_KEY", "Not set (TF-IDF fallback will be used — this is fine)")

    print("\n--- Demo Files ---")
    demo_dir = os.path.join(os.path.dirname(__file__), "demo")
    for f in ["rag-platform-docs.py", "incident-agent.py",
              "ai-agent-observability.py", "ai-governance-alerts.yaml"]:
        check(f, os.path.exists(os.path.join(demo_dir, f)))

    print("\n--- Takehome Files ---")
    takehome_dir = os.path.join(os.path.dirname(__file__), "takehome")
    for f in ["rag_pipeline.py", "multi_agent_system.py", "ai-guardrails.py",
              "runbook-automator.py", "backstage-ai-template.yaml",
              "alert-correlator.py", "incident_triage.py", "test-ai-agents.py"]:
        check(f, os.path.exists(os.path.join(takehome_dir, f)))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed")
    if all(results):
        print("Session 8 is ready to go!")
    else:
        print("Fix the issues above before starting Session 8.")
    print("=" * 60)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
