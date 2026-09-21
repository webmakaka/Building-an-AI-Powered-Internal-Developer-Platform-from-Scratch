# Session 6 — Observability, SLOs & Cost Management

**Day 2 | Session 2 of 5**

## Overview

You can't run a platform blind. This session deploys the OpenTelemetry Collector as the single entry point for all telemetry, defines SLOs with Sloth that generate Prometheus recording rules, runs cost analysis and anomaly detection scripts, and demonstrates AI-powered alert correlation that reduces 50 noisy alerts down to 3 root-cause incidents.

## What You'll Learn

- OpenTelemetry Collector: receivers, processors, exporters
- SLO definitions with Sloth (YAML to Prometheus rules)
- Cost allocation, anomaly detection, and per-team showback
- AI alert correlation: grouping related alerts into root-cause incidents
- HPA / VPA for autoscaling
- Observability personas (developer, SRE, platform, leadership)

## Knowledge Prerequisites

- Everything from Sessions 1-5
- Understand the three pillars of observability: metrics, logs, traces
- Know what Prometheus is (metrics collection and alerting)
- Basic understanding of SLOs/SLIs (service level objectives and indicators)
- Familiarity with what autoscaling means (HPA scales pods horizontally, VPA adjusts resource requests)

## Tools Required

- kubectl, Helm (Prometheus stack), Python 3

## Verify Your Setup

```bash
python3 verify_module.py
```

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | OTel Collector config + deployment, Sloth SLO definition, cost analyzer, AI alert correlator |
| [takehome/](takehome/) | App instrumentation, alert rules, HPA/VPA, cost monitoring, AI agent observability, persona mapping |

## Quick Start

```bash
# Demo
cd demo

# Deploy the OTel Collector — single entry point for all metrics, traces, and logs
kubectl apply -f otel-collector-deployment.yaml

# Review an SLO definition: "auth-service must have 99.9% availability over 30 days"
cat sloth-auth-service-slo.yaml

# Analyze resource usage across namespaces and generate a per-team cost breakdown
python3 cost-analyzer.py

# AI alert correlation: groups 50 noisy alerts into 3 root-cause incidents
python3 alert-correlator.py

# Take-home exercises
cd takehome

# Add OpenTelemetry tracing to a sample app with custom spans and metrics
python3 instrument-app.py

# Apply a Horizontal Pod Autoscaler to automatically scale pods based on CPU/memory
kubectl apply -f checkout-api-hpa.yaml

# Detect cost anomalies using statistical analysis (z-score, spike, trend detection)
python3 cost-anomaly-detector.py

# Monitor AI agents with Prometheus metrics: latency, confidence, override rates
python3 ai-agent-observability.py
```

## Key Takeaway

Cost visibility is a platform responsibility, not an afterthought. AI alert correlation reduces alert fatigue by grouping related signals automatically — runs locally with heuristics, optionally add an LLM for advanced pattern recognition.

## Go Deeper

This session covers Chapters 10-11 of [*The Platform Engineer's Handbook*](https://peh-packt.platformetrics.com/), which goes further into production observability patterns, OpenCost for Kubernetes cost management, and advanced SLO strategies. See the [book repo](https://github.com/achankra/peh) for the full code samples.

[Back to Course Overview](../README.md)
