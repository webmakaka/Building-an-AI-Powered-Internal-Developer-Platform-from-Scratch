# Session 6 Demo — Observability, SLOs, Cost + AI Alert Correlation

## Demo Overview
Deploy the OTel collector, review an SLO definition, run cost analysis,
and try AI-powered alert correlation.

## Dependencies — Run This First
Requires a running Kind cluster (from Session 2) with Prometheus installed:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
pip3 install pyyaml requests --break-system-packages
```

## Steps
```bash
# 1. Review the OTel collector config (receivers, processors, exporters)
# The OpenTelemetry Collector is the single entry point for all telemetry — metrics, traces, and logs.
# This config defines what data it receives, how it processes it, and where it sends it.
cat otel-collector-config.yaml

# 2. Deploy the collector
# Deploys the OTel Collector as a Kubernetes Deployment in the monitoring namespace.
# Once running, applications send telemetry here instead of directly to Prometheus/Jaeger/Loki.
kubectl apply -f otel-collector-deployment.yaml
# Output: deployment and service created. Verify with: kubectl get pods -n monitoring

# 3. Review an SLO definition with Sloth
# Sloth converts simple SLO YAML (service, objective, error ratio) into Prometheus recording rules.
# This definition says "auth-service must have 99.9% availability over 30 days".
cat sloth-auth-service-slo.yaml

# 4. Run cost analysis
# Analyzes resource usage across namespaces and generates a cost allocation report.
# Shows which teams are consuming the most resources and where waste exists.
python3 cost-analyzer.py
# Output: per-namespace cost breakdown with recommendations for optimization.

# 5. AI-POWERED: Correlate noisy alerts into root causes
# Takes a flood of raw alerts and groups them into correlated incidents using heuristic analysis.
# 50 raw alerts become 3 incidents, each with a root cause summary and affected services.
python3 alert-correlator.py
# Output: grouped incidents with root cause analysis. Reduces alert fatigue dramatically.
```

## Key Concepts
- OTel Collector is the single entry point for all telemetry
- Sloth generates Prometheus recording rules from simple SLO YAML
- Cost visibility is a platform responsibility, not an afterthought
- AI alert correlation reduces alert fatigue by grouping related alerts automatically
- Runs locally with heuristics; optionally add an LLM for advanced pattern recognition
