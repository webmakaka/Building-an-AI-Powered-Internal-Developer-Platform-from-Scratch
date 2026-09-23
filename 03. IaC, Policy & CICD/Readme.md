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

## Verify Your Setup

```bash
$ python verify_module.py
```

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Crossplane XRD + Composition, database claim, conftest policies, AI Backstage template |
| [takehome/](takehome/) | GitHub Actions pipelines, Rego policy authoring, pre-commit hooks, guardrail validator |

## Quick Start

```bash
# Demo
$ cd demo

# Install Crossplane providers that connect XRDs to actual cloud resources
$ kubectl apply -f crossplane-providers.yaml

# Define the developer-facing API: what parameters they can set when requesting a database
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

## Key Takeaway

Developers submit 10 lines of YAML, the platform provisions the database. Conftest catches violations before code reaches the cluster. AI generates config, but it passes through the same policy gate as human-written code.

## Go Deeper

This session covers Chapters 6-7 of *The Platform Engineer's Handbook*
