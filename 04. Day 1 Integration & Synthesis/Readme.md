# Session 4 — Day 1 Integration & Synthesis

**Day 1 | Session 4 of 4**

## Overview

Day 1 wraps up by proving everything works together. Three test suites validate the three pillars you've built: runtime (cluster health), infrastructure (Crossplane resources), and policy (Gatekeeper constraints). This is the integration checkpoint — if all tests pass, your platform foundation is solid.

## What You'll Learn

- End-to-end platform verification patterns
- Three-pillar testing: runtime, infrastructure, policy
- How platform teams use smoke tests in CI
- Debugging cross-layer issues

## Knowledge Prerequisites

- Everything from Sessions 1-3 (cluster, namespaces, Crossplane, policies)
- Understanding of integration testing as a concept
- Familiarity with what "smoke tests" are and why platform teams run them

## Tools Required

- kubectl, Python 3 (same setup from Sessions 2-3)

## Verify Your Setup

```bash
$ python verify_module.py
============================================================
Session 4 — Module Verification
============================================================

--- Python ---
  [PASS] Python 3.10+ — Found 3.10.12

--- CLI Tools ---
  [PASS] kubectl — Installed
  [PASS] helm — Installed

--- Cluster Status ---
  [PASS] Cluster reachable — Cluster is running
  [PASS] Team namespaces exist — Namespaces from Session 2 present

--- Demo Files ---
  [PASS] test-cluster-health.py
  [PASS] test-infrastructure.py
  [PASS] test-policies.py

============================================================
Results: 8/8 checks passed
Session 4 is ready to go!
============================================================
```

<br/>

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Three validation test suites: cluster health, infrastructure, policies |
| [takehome/](takehome/) | Consolidation guide: review notes, identify first component to implement, prepare for Day 2 |

<br/>

## Quick Start

<br/>

```shell
$ cd demo
```

<br/>

```shell
// Validate cluster health: nodes Ready, system pods running, namespaces, quotas, Pulumi/Crossplane config
$ python test-cluster-health.py
============================================================
Session 4: Cluster Health Tests
============================================================
test_nodes_ready (__main__.TestClusterHealth)
All cluster nodes should be in Ready state. ... ok
test_platform_engineering_namespace_exists (__main__.TestClusterHealth)
Platform engineering namespace should exist from RBAC setup. ... skipped 'kubectl not available or RBAC not applied yet'
test_resource_quotas_applied (__main__.TestClusterHealth)
Resource quotas should be set on team namespaces. ... FAIL
test_system_pods_running (__main__.TestClusterHealth)
Critical kube-system pods should be running. ... ok
test_team_namespaces_exist (__main__.TestClusterHealth)
Team namespaces from Session 2 should exist. ... FAIL
test_composition_exists (__main__.TestCrossplaneConfig) ... ok
test_crossplane_namespace_exists (__main__.TestCrossplaneConfig)
Crossplane system namespace should exist if Crossplane was installed. ... ok
test_xrd_exists (__main__.TestCrossplaneConfig) ... ok
test_main_py_exists (__main__.TestPulumiConfig) ... ok
test_pulumi_yaml_exists (__main__.TestPulumiConfig) ... ok
test_requirements_exists (__main__.TestPulumiConfig) ... ok

======================================================================
FAIL: test_resource_quotas_applied (__main__.TestClusterHealth)
Resource quotas should be set on team namespaces.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-cluster-health.py", line 77, in test_resource_quotas_applied
    self.assertTrue(len(items) > 0, "No resource quota found in team-alpha")
AssertionError: False is not true : No resource quota found in team-alpha

======================================================================
FAIL: test_team_namespaces_exist (__main__.TestClusterHealth)
Team namespaces from Session 2 should exist.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-cluster-health.py", line 61, in test_team_namespaces_exist
    self.assertIn("team-beta", ns_names, "team-beta namespace not found (run Session 2 first)")
AssertionError: 'team-beta' not found in ['crossplane-system', 'default', 'kube-node-lease', 'kube-public', 'kube-system', 'local-path-storage', 'team-alpha'] : team-beta namespace not found (run Session 2 first)

----------------------------------------------------------------------
Ran 11 tests in 0.379s

FAILED (failures=2, skipped=1)
```

<br/>

```
// Verify infrastructure: namespace isolation, RBAC roles, Crossplane readiness
$ python test-infrastructure.py
============================================================
Session 4: Infrastructure Verification Tests
============================================================
test_claim_file_valid_yaml (__main__.TestCrossplaneReadiness)
The Crossplane claim from Session 3 should be valid YAML. ... ok
test_crossplane_pods_running (__main__.TestCrossplaneReadiness)
Crossplane pods should be running. ... ok
test_network_policies_exist (__main__.TestNamespaceIsolation)
Team namespaces should have network policies. ... FAIL
test_team_alpha_has_quota (__main__.TestNamespaceIsolation)
team-alpha should have a resource quota. ... FAIL
test_team_beta_has_quota (__main__.TestNamespaceIsolation)
team-beta should have a resource quota. ... FAIL
test_platform_admin_role_exists (__main__.TestRBACConfiguration)
platform-admin ClusterRole should exist. ... skipped 'kubectl not available or RBAC not applied'
test_platform_operator_role_exists (__main__.TestRBACConfiguration)
platform-operator ClusterRole should exist. ... skipped 'kubectl not available or RBAC not applied'
test_service_accounts_exist (__main__.TestRBACConfiguration)
Platform service accounts should exist in platform-engineering namespace. ... FAIL

======================================================================
FAIL: test_network_policies_exist (__main__.TestNamespaceIsolation)
Team namespaces should have network policies.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-infrastructure.py", line 68, in test_network_policies_exist
    self.assertTrue(len(data.get("items", [])) > 0,
AssertionError: False is not true : No network policy in team-alpha

======================================================================
FAIL: test_team_alpha_has_quota (__main__.TestNamespaceIsolation)
team-alpha should have a resource quota.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-infrastructure.py", line 46, in test_team_alpha_has_quota
    self.assertTrue(len(data.get("items", [])) > 0,
AssertionError: False is not true : No resource quota in team-alpha

======================================================================
FAIL: test_team_beta_has_quota (__main__.TestNamespaceIsolation)
team-beta should have a resource quota.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-infrastructure.py", line 57, in test_team_beta_has_quota
    self.assertTrue(len(data.get("items", [])) > 0,
AssertionError: False is not true : No resource quota in team-beta

======================================================================
FAIL: test_service_accounts_exist (__main__.TestRBACConfiguration)
Platform service accounts should exist in platform-engineering namespace.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/marley/tmp/peh-course/Session4/demo/test-infrastructure.py", line 102, in test_service_accounts_exist
    self.assertIn("platform-admin-sa", sa_names,
AssertionError: 'platform-admin-sa' not found in [] : platform-admin-sa not found in platform-engineering namespace

----------------------------------------------------------------------
Ran 8 tests in 0.414s

FAILED (failures=4, skipped=2)
```

<br/>

```
// Run offline policy checks: compliant vs. non-compliant manifests, conftest integration
$ python test-policies.py
============================================================
Session 4: Policy Validation Tests
============================================================
test_conftest_compliant_passes (__main__.TestConftestIntegration)
Compliant manifests should pass conftest validation. ... ok
test_compliant_deployment_passes (__main__.TestPolicyValidation)
Compliant deployment should have labels, limits, and approved registry. ... ok
test_missing_labels_detected (__main__.TestPolicyValidation)
Deployments without required team label should be flagged. ... ok
test_no_limits_detected (__main__.TestPolicyValidation)
Deployment without resource limits should be flagged. ... ok
test_privileged_container_detected (__main__.TestPolicyValidation)
Privileged container should be flagged. ... ok
test_untrusted_registry_detected (__main__.TestPolicyValidation)
Images from untrusted registries should be flagged. ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.179s

OK
```

<br/>

## Key Takeaway

If any test fails, you know exactly which layer has a problem. In production, these same tests run in CI as platform smoke tests after every change.

## Go Deeper

Day 1 covers the foundational layers from Chapters 1-7 of *The Platform Engineer's Handbook*
