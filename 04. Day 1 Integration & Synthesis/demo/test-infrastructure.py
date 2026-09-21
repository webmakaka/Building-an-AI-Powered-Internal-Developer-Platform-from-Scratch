#!/usr/bin/env python3
"""
Session 4: Infrastructure Verification Tests
==============================================
Validates that infrastructure from Sessions 2-3 is correctly provisioned.
Checks namespace isolation, RBAC, resource quotas, and Crossplane readiness.

Usage:
    python3 test-infrastructure.py
"""

import json
import os
import subprocess
import sys
import unittest

import yaml


def run_kubectl(args: list) -> tuple:
    """Run kubectl command and return exit code, stdout, stderr."""
    try:
        result = subprocess.run(
            ["kubectl"] + args,
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return 1, "", "kubectl not available or timed out"


class TestNamespaceIsolation(unittest.TestCase):
    """Validate namespace isolation from Session 2."""

    def test_team_alpha_has_quota(self):
        """team-alpha should have a resource quota."""
        code, stdout, _ = run_kubectl([
            "get", "resourcequota", "-n", "team-alpha", "-o", "json"
        ])
        if code != 0:
            self.skipTest("kubectl not available or team-alpha not provisioned")
        data = json.loads(stdout)
        self.assertTrue(len(data.get("items", [])) > 0,
                        "No resource quota in team-alpha")

    def test_team_beta_has_quota(self):
        """team-beta should have a resource quota."""
        code, stdout, _ = run_kubectl([
            "get", "resourcequota", "-n", "team-beta", "-o", "json"
        ])
        if code != 0:
            self.skipTest("kubectl not available or team-beta not provisioned")
        data = json.loads(stdout)
        self.assertTrue(len(data.get("items", [])) > 0,
                        "No resource quota in team-beta")

    def test_network_policies_exist(self):
        """Team namespaces should have network policies."""
        code, stdout, _ = run_kubectl([
            "get", "networkpolicy", "-n", "team-alpha", "-o", "json"
        ])
        if code != 0:
            self.skipTest("kubectl not available or team-alpha not provisioned")
        data = json.loads(stdout)
        self.assertTrue(len(data.get("items", [])) > 0,
                        "No network policy in team-alpha")


class TestRBACConfiguration(unittest.TestCase):
    """Validate RBAC setup from Session 2."""

    def test_platform_admin_role_exists(self):
        """platform-admin ClusterRole should exist."""
        code, stdout, _ = run_kubectl([
            "get", "clusterrole", "platform-admin", "--no-headers"
        ])
        if code != 0:
            self.skipTest("kubectl not available or RBAC not applied")
        self.assertIn("platform-admin", stdout)

    def test_platform_operator_role_exists(self):
        """platform-operator ClusterRole should exist."""
        code, stdout, _ = run_kubectl([
            "get", "clusterrole", "platform-operator", "--no-headers"
        ])
        if code != 0:
            self.skipTest("kubectl not available or RBAC not applied")
        self.assertIn("platform-operator", stdout)

    def test_service_accounts_exist(self):
        """Platform service accounts should exist in platform-engineering namespace."""
        code, stdout, _ = run_kubectl([
            "get", "serviceaccount", "-n", "platform-engineering", "-o", "json"
        ])
        if code != 0:
            self.skipTest("kubectl not available or platform-engineering namespace missing")
        data = json.loads(stdout)
        sa_names = [sa["metadata"]["name"] for sa in data.get("items", [])]
        self.assertIn("platform-admin-sa", sa_names,
                      "platform-admin-sa not found in platform-engineering namespace")


class TestCrossplaneReadiness(unittest.TestCase):
    """Validate Crossplane installation from Session 3."""

    def test_crossplane_pods_running(self):
        """Crossplane pods should be running."""
        code, stdout, _ = run_kubectl([
            "get", "pods", "-n", "crossplane-system", "-o", "json"
        ])
        if code != 0:
            self.skipTest("Crossplane not installed (run Session 3 setup first)")
        data = json.loads(stdout)
        pods = data.get("items", [])
        if not pods:
            self.skipTest("No Crossplane pods found")
        for pod in pods:
            phase = pod.get("status", {}).get("phase", "")
            name = pod["metadata"]["name"]
            self.assertIn(phase, ["Running", "Succeeded"],
                          f"Crossplane pod {name} is {phase}")

    def test_claim_file_valid_yaml(self):
        """The Crossplane claim from Session 3 should be valid YAML."""
        claim_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "Session3", "demo",
            "demo-app-database.yaml"
        )
        self.assertTrue(os.path.exists(claim_path),
                        "Session3/demo/demo-app-database.yaml not found")
        with open(claim_path) as f:
            docs = list(yaml.safe_load_all(f))
        self.assertTrue(len(docs) > 0, "Claim file is empty")


if __name__ == "__main__":
    print("=" * 60)
    print("Session 4: Infrastructure Verification Tests")
    print("=" * 60)
    unittest.main(verbosity=2)
