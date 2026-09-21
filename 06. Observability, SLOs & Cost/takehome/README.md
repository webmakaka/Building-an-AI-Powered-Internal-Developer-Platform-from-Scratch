# Session 6 Takehome — Full Observability, Cost & AI Stack

## Dependencies — Run This First
Requires a running Kind cluster from Session 2 with Prometheus installed:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
pip3 install pyyaml requests scikit-learn --break-system-packages
```

## What to Do After the Session

### 1. Instrument an Application (20 min)

Add OpenTelemetry tracing to a sample Python application using decorators and custom spans.
Shows how to propagate trace context across services and emit structured metrics.
```bash
python3 instrument-app.py
```
Output: traced HTTP requests with span attributes, latency metrics, and structured logs.
This is the pattern your services should follow to feed data into the OTel Collector.

### 2. Configure Alerting (15 min)

Review the Prometheus alert rules and apply them to your cluster.
These rules fire when error rates exceed thresholds or SLOs are at risk of being breached.
```bash
cat alert-rules.yaml
kubectl apply -f alert-rules.yaml
```
Verify with: `kubectl get prometheusrule -n monitoring`.

### 3. Deploy HPA and VPA (15 min)

Apply Horizontal and Vertical Pod Autoscalers to automatically scale workloads based on load.
HPA adds/removes pods based on CPU/memory usage. VPA adjusts resource requests per pod.
```bash
kubectl apply -f checkout-api-hpa.yaml
kubectl apply -f checkout-api-vpa.yaml
```
Check autoscaler status with: `kubectl get hpa` and `kubectl get vpa`.

### 4. Set Up Cost Monitoring (15 min)

Validate that all workloads have proper cost allocation labels (team, cost-center, environment).
Reports cost distribution by team and flags workloads missing required labels.
```bash
python3 cost-allocation-labels.py
```
Output: per-team cost allocation summary and a list of unlabeled workloads.

Run the cost anomaly detector to identify unusual spending patterns using statistical analysis.
Uses z-score detection, spike detection, and trend analysis on simulated cost data.
```bash
python3 cost-anomaly-detector.py
```
Output: detected anomalies with severity and recommended actions.

### 5. Map Observability Personas (10 min)

Generate persona-specific Grafana dashboard configs for developers, SREs, managers, and security teams.
Each persona sees different metrics from the same observability data.
```bash
python3 observability-personas.py
```
Output: dashboard JSON files tailored to each persona's needs (latency for devs, SLAs for managers, CVEs for security).

### 6. Explore AI Agent Observability (15 min)

Study how to monitor AI agents in production — tracking latency, confidence scores,
human override rates, and error patterns using Prometheus metrics.
```bash
python3 ai-agent-observability.py
```
Output: sample metrics showing how AI agent health is measured the same way you measure services.

## Deliverable
- An SLO definition for one of your real services
- HPA configured for your most variable workload
- A plan for how you'd integrate alert correlation into your on-call workflow
