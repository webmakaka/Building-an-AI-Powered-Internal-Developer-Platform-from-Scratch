# Session 2 — Infrastructure & Control Plane

**Day 1 | Session 2 of 4**

## Overview

This is where hands meet keyboard. You'll spin up a Kind cluster, provision team namespaces with resource quotas and RBAC, and write your first piece of infrastructure-as-code using Pulumi with the Python SDK. By the end, you'll have the multi-tenant foundation that every IDP builds on — isolated namespaces with guardrails that prevent teams from stepping on each other.

## What You'll Learn

- Kubernetes cluster provisioning with Kind
- Infrastructure as Code with Pulumi (Python SDK)
- Namespace isolation with ResourceQuotas and LimitRanges
- Platform-level RBAC (admin vs. developer roles)
- Control plane architecture for multi-tenancy

## Knowledge Prerequisites

- Understand what containers are and why they exist (Docker basics)
- Know what Kubernetes is at a high level: clusters, nodes, pods, namespaces
- Comfortable reading YAML files
- Basic understanding of RBAC (role-based access control) as a concept
- Familiarity with infrastructure-as-code as a concept (Terraform, Pulumi, etc.)

## Tools Required

- Docker Desktop, Kind, kubectl, Python 3, Pulumi

## Verify Your Setup

```bash
$ python verify_module.py
```

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Kind cluster setup, Pulumi modules, namespace provisioner, RBAC, platform services |
| [takehome/](takehome/) | Build your own control plane: multi-env config, developer RBAC, test app deployment, validation tests |

## Quick Start

```bash
# Create the Kind cluster — the Kubernetes foundation for the entire workshop
$ kind create cluster --name workshop

# Demo
$ cd demo
$ pip install pulumi pulumi-kubernetes --break-system-packages

# Create team-alpha namespace with resource quotas, network policies, and service accounts
$ python namespace-provisioner.py --namespace team-alpha --env dev --team alpha

# Same provisioner for team-beta — proves the process is standardized and repeatable
$ python namespace-provisioner.py --namespace team-beta --env dev --team beta

# Apply platform admin RBAC: ClusterRoles, ServiceAccounts, and bindings
$ kubectl apply -f rbac-platform-admin.yaml

# Take-home exercises
$ cd takehome

# Apply a scoped developer role (read pods/logs, deploy apps — cannot modify RBAC or delete namespaces)
$ kubectl apply -f rbac-developer-role.yaml

# Deploy a sample app to verify the cluster, RBAC, and quotas work end-to-end
$ kubectl apply -f demo-app-deployment.yaml

# Run cluster health checks: nodes Ready, system pods running, namespaces exist
$ python test-cluster-health.py
```

## Key Takeaway

One command creates a namespace + quota + limit range + RBAC. Developers never touch cluster-level resources. This is the foundation every subsequent session builds on.

## Go Deeper

This session covers Chapters 4-5 of *The Platform Engineer's Handbook*

