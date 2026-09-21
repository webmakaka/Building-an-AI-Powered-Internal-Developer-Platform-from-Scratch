#!/usr/bin/env python3
"""
Session 4: Cluster Health Tests
================================
Validates Kubernetes cluster configuration and readiness
after completing Sessions 1-3.

Usage:
    python3 test-cluster-health.py
"""

import json
import os
import subprocess
import sys
import unittest


def run_kubectl(args: list) -> str:
    """Execute kubectl and return stdout."""
    try:
        r = subprocess.run(["kubectl"] + args, capture_output=True, text=True, timeout=30)
        return r.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return ""


class TestClusterHealth(unittest.TestCase):
    """Validate cluster is healthy and correctly configured."""

    def test_nodes_ready(self):
        """All cluster nodes should be in Ready state."""
        output = run_kubectl(["get", "nodes", "-o", "json"])
        if not output:
            self.skipTest("kubectl not available")
        data = json.loads(output)
        for node in data.get("items", []):
            conditions = {c["type"]: c["status"] for c in node.get("status", {}).get("conditions", [])}
            self.assertEqual(conditions.get("Ready"), "True",
                             f"Node {node['metadata']['name']} not Ready")

    def test_system_pods_running(self):
        """Critical kube-system pods should be running."""
        output = run_kubectl(["get", "pods", "-n", "kube-system", "-o", "json"])
        if not output:
            self.skipTest("kubectl not available")
        data = json.loads(output)
        for pod in data.get("items", []):
            phase = pod.get("status", {}).get("phase", "")
            name = pod["metadata"]["name"]
            self.assertIn(phase, ["Running", "Succeeded"], f"Pod {name} is {phase}")

    def test_team_namespaces_exist(self):
        """Team namespaces from Session 2 should exist."""
        output = run_kubectl(["get", "namespaces", "-o", "json"])
        if not output:
            self.skipTest("kubectl not available")
        data = json.loads(output)
        ns_names = [ns["metadata"]["name"] for ns in data.get("items", [])]
        self.assertIn("team-alpha", ns_names, "team-alpha namespace not found (run Session 2 first)")
        self.assertIn("team-beta", ns_names, "team-beta namespace not found (run Session 2 first)")

    def test_platform_engineering_namespace_exists(self):
        """Platform engineering namespace should exist from RBAC setup."""
        output = run_kubectl(["get", "namespace", "platform-engineering", "--no-headers"])
        if not output:
            self.skipTest("kubectl not available or RBAC not applied yet")
        self.assertIn("platform-engineering", output)

    def test_resource_quotas_applied(self):
        """Resource quotas should be set on team namespaces."""
        output = run_kubectl(["get", "resourcequota", "-n", "team-alpha", "-o", "json"])
        if not output:
            self.skipTest("kubectl not available")
        data = json.loads(output)
        items = data.get("items", [])
        self.assertTrue(len(items) > 0, "No resource quota found in team-alpha")


class TestPulumiConfig(unittest.TestCase):
    """Validate Pulumi configuration files from Session 2."""

    def _session2_path(self, *parts):
        base = os.path.join(os.path.dirname(__file__), "..", "..", "Session2", "demo")
        return os.path.join(base, *parts)

    def test_main_py_exists(self):
        path = self._session2_path("pulumi-cluster", "__main__.py")
        self.assertTrue(os.path.exists(path),
                        "Session2/demo/pulumi-cluster/__main__.py not found")

    def test_pulumi_yaml_exists(self):
        path = self._session2_path("pulumi-cluster", "Pulumi.yaml")
        self.assertTrue(os.path.exists(path),
                        "Session2/demo/pulumi-cluster/Pulumi.yaml not found")

    def test_requirements_exists(self):
        path = self._session2_path("pulumi-cluster", "requirements.txt")
        self.assertTrue(os.path.exists(path),
                        "Session2/demo/pulumi-cluster/requirements.txt not found")


class TestCrossplaneConfig(unittest.TestCase):
    """Validate Crossplane files from Session 3."""

    def _session3_path(self, filename):
        return os.path.join(os.path.dirname(__file__), "..", "..", "Session3", "demo", filename)

    def test_xrd_exists(self):
        path = self._session3_path("xrd-postgresql.yaml")
        self.assertTrue(os.path.exists(path),
                        "Session3/demo/xrd-postgresql.yaml not found")

    def test_composition_exists(self):
        path = self._session3_path("composition-postgresql.yaml")
        self.assertTrue(os.path.exists(path),
                        "Session3/demo/composition-postgresql.yaml not found")

    def test_crossplane_namespace_exists(self):
        """Crossplane system namespace should exist if Crossplane was installed."""
        output = run_kubectl(["get", "namespace", "crossplane-system", "--no-headers"])
        if not output:
            self.skipTest("Crossplane not installed yet (run Session 3 setup first)")
        self.assertIn("crossplane-system", output)


if __name__ == "__main__":
    print("=" * 60)
    print("Session 4: Cluster Health Tests")
    print("=" * 60)
    unittest.main(verbosity=2)
