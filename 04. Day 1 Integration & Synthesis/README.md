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
python3 verify_module.py
```

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Three validation test suites: cluster health, infrastructure, policies |
| [takehome/](takehome/) | Consolidation guide: review notes, identify first component to implement, prepare for Day 2 |

## Quick Start

```bash
$ cd demo

# Validate cluster health: nodes Ready, system pods running, namespaces, quotas, Pulumi/Crossplane config
$ python test-cluster-health.py

# Verify infrastructure: namespace isolation, RBAC roles, Crossplane readiness
$ python test-infrastructure.py

# Run offline policy checks: compliant vs. non-compliant manifests, conftest integration
$ python test-policies.py
```

## Key Takeaway

If any test fails, you know exactly which layer has a problem. In production, these same tests run in CI as platform smoke tests after every change.

## Go Deeper

Day 1 covers the foundational layers from Chapters 1-7 of *The Platform Engineer's Handbook*
