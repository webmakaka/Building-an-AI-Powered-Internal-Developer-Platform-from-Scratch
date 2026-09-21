# Session 7 Demo — Chaos Engineering, Progressive Delivery + AI Runbooks

## Demo Overview
Inject network latency with Chaos Mesh, deploy a canary with automated rollback,
and try AI-powered runbook automation.

## Dependencies — Run This First
Requires a running Kind cluster (from Session 2) with Chaos Mesh installed:
```bash
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm install chaos-mesh chaos-mesh/chaos-mesh --namespace chaos-mesh --create-namespace
```

## Steps
```bash
# 1. Review the chaos experiment definition
# This YAML defines a network delay experiment: 100ms latency injected into api-service pods.
# Chaos experiments discover how your system breaks before users do.
cat chaos-network-delay.yaml

# 2. Apply it (adds 100ms latency to api-service pods)
# Kubernetes applies the ChaosExperiment CRD. Chaos Mesh intercepts pod traffic and injects the delay.
kubectl apply -f chaos-network-delay.yaml
# Output: chaosexperiment created. The delay is now active on matching pods.

# 3. Run the chaos orchestrator to monitor
# Orchestrates chaos experiments with safety controls: monitors impact, auto-pauses if error rates spike,
# and collects metrics on recovery time.
python3 chaos-runner.py
# Output: experiment status, observed latency impact, and recovery timeline.

# 4. Deploy a canary
# Deploys a canary version alongside the stable version. Traffic is split (e.g., 10% to canary).
# If the canary's error rate or latency exceeds thresholds, it gets rolled back automatically.
kubectl apply -f canary-deployment.yaml
# Output: canary deployment created alongside the stable version.

# 5. Run the automated rollback controller
# Monitors the canary deployment's health metrics and automatically rolls back if thresholds are breached.
# No human intervention needed — the controller watches error rates and latency in real time.
python3 rollback-controller.py
# Output: monitoring status, health checks, and rollback decisions (promote or rollback).

# 6. AI-POWERED: Convert a markdown runbook to executable steps
# Parses an existing markdown runbook and converts it into structured, executable diagnostic and action steps.
# AI adds safety checks automatically and identifies which steps need human approval vs. auto-execute.
python3 runbook-automator.py
# Output: structured runbook with diagnostic steps, action steps, and approval gates.
```

## Key Concepts
- Chaos experiments discover how your system breaks before users do
- Canary + rollback controller = automated safe deployments
- AI runbook automation takes your existing markdown runbooks and makes them executable
- Safety built in: AI identifies which steps need human approval vs. auto-execute
- This is NOT replacing SREs — it's giving them a co-pilot
