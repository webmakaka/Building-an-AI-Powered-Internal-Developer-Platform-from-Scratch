# Session 3 — IaC, Policy & CI/CD

**Day 1 | Session 3 of 4**

## Overview

Self-service infrastructure meets shift-left security. You'll set up Crossplane so developers can provision databases with a 10-line YAML claim, write OPA/Rego policies that catch violations before code reaches the cluster, and see how AI can generate Kubernetes configuration from natural-language descriptions — with the same policy engine validating the output.

## What You'll Learn

- Crossplane XRDs, Compositions, and Claims for self-service infra
- Policy-as-Code with OPA, Conftest, and Gatekeeper
- Writing Rego policies and testing with conftest
- AI-generated service templates with policy validation
- CI/CD pipeline architecture with GitHub Actions reusable workflows
- Pre-commit hooks for shift-left validation

## Knowledge Prerequisites

- Everything from Sessions 1-2 (running cluster, namespaces, RBAC)
- Understand what Helm is (Kubernetes package manager — installs things into your cluster)
- Know what CI/CD pipelines are and why they matter
- Basic understanding of policy enforcement (e.g., "don't allow containers to run as root")
- Familiarity with GitHub Actions or any CI system (at a conceptual level)

## Tools Required

- kubectl, Helm (for Crossplane), conftest, pre-commit, Python 3

<br/>

## Verify Your Setup

```bash
$ python verify_module.py
============================================================
Session 3 — Module Verification
============================================================

--- Python ---
  [PASS] Python 3.10+ — Found 3.10.12

--- CLI Tools ---
  [PASS] kubectl — Client Version: v1.30.0
  [PASS] Helm — version.BuildInfo{Version:"v3.19.4", GitCommit:"7cfb6e486dac
  [PASS] conftest — Conftest: 0.70.1
  [PASS] pre-commit — pre-commit 4.6.2

--- Cluster Components ---
  [PASS] Crossplane namespace — Installed

--- Python Packages ---
  [PASS] flask

--- Demo Files ---
  [PASS] xrd-postgresql.yaml
  [PASS] composition-postgresql.yaml
  [PASS] demo-app-database.yaml
  [PASS] backstage-ai-template.yaml
  [PASS] crossplane-providers.yaml

--- Takehome Files ---
  [PASS] backend-pipeline.yml
  [PASS] guardrail-validator.py
  [PASS] test-infrastructure.py
  [PASS] .pre-commit-config.yaml

============================================================
Results: 16/16 checks passed
Session 3 is ready to go!
============================================================
```

<br/>

```shell
$ {
    docker pull xpkg.upbound.io/crossplane-contrib/function-patch-and-transform:v0.7.0
    docker pull xpkg.upbound.io/crossplane-contrib/provider-helm:v0.18.1
    docker pull xpkg.upbound.io/crossplane-contrib/provider-kubernetes:v0.13.0
}
```

<br/>

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Crossplane XRD + Composition, database claim, conftest policies, AI Backstage template |
| [takehome/](takehome/) | GitHub Actions pipelines, Rego policy authoring, pre-commit hooks, guardrail validator |

<br/>

## Quick Start

```bash
// Demo
$ cd demo

// Install Crossplane providers that connect XRDs to actual cloud resources
$ kubectl apply -f crossplane-providers.yaml

// Define the developer-facing API: what parameters they can set when requesting a database
$ kubectl apply -f xrd-postgresql.yaml

# Map the developer's simple claim to the actual underlying resources
$ kubectl apply -f composition-postgresql.yaml

# Submit a 10-line database claim — this is the developer experience
$ kubectl apply -f demo-app-database.yaml

# Run policy checks against intentionally bad manifests (missing labels, privileged containers, etc.)
$ conftest test conftest-tests/test-manifests.yaml -p conftest-tests/

# Take-home exercises
$ cd takehome

# Validate infrastructure claims against org policies (prod-tier only in prod namespaces, etc.)
$ python guardrail-validator.py

# Test the full infrastructure provisioning workflow: apply claim, verify readiness, check secrets
$ python test-infrastructure.py
```

<br/>

## Key Takeaway

Developers submit 10 lines of YAML, the platform provisions the database. Conftest catches violations before code reaches the cluster. AI generates config, but it passes through the same policy gate as human-written code.

## Go Deeper

This session covers Chapters 6-7 of *The Platform Engineer's Handbook*
