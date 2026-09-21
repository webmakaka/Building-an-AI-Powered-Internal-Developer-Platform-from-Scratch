# Session 4 Demo — Day 1 Verification

## Demo Overview
Run all three test suites to verify the integrated platform works end-to-end.

## Dependencies — Run This First
Requires a running Kind cluster with namespaces (Session 2) and Crossplane (Session 3).

## Steps
```bash
# 1. Cluster health
# Validates that cluster nodes are Ready, system pods are running, team namespaces exist,
# resource quotas are applied, and Pulumi/Crossplane config files are in place.
python3 test-cluster-health.py
# Output: pass/fail per check. Failures tell you exactly which Session 2/3 step was missed.

# 2. Infrastructure verification
# Tests namespace isolation (quotas, network policies), RBAC configuration (roles, service accounts),
# and Crossplane readiness (pods running, claim files valid).
python3 test-infrastructure.py
# Output: pass/fail per check. Skips gracefully if a component isn't installed yet.

# 3. Policy validation
# Runs offline policy checks against compliant and non-compliant manifests.
# Verifies that conftest correctly catches missing labels, privileged containers, and untrusted registries.
python3 test-policies.py
# Output: all 6 tests should pass, confirming your policy engine works as expected.
```

## Key Concepts
- Three test suites validate the three pillars: runtime, infra, policy
- In production, these run in CI as platform smoke tests
- If any fail, you know exactly which layer has a problem
