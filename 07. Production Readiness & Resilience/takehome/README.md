# Session 7 Takehome — Full Resilience Suite

## Dependencies — Run This First
Requires a running Kind cluster from Session 2 with Chaos Mesh and Velero installed:
```bash
# Chaos Mesh
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm install chaos-mesh chaos-mesh/chaos-mesh --namespace chaos-mesh --create-namespace

# Velero (see https://velero.io/docs/main/basic-install/)
# Uses MinIO as S3-compatible storage for local Kind clusters
```

## What to Do After the Session

### 1. Run More Chaos Experiments (20 min)

Apply additional chaos experiments to test different failure modes.
Pod kill terminates random pods to test self-healing. Pod failure simulates application crashes.
```bash
kubectl apply -f chaos-experiment-pod-kill.yaml
kubectl apply -f chaos-mesh-pod-failure.yaml
```
Observe recovery time. Does your service self-heal? How long does it take?
Compare recovery behavior between pod kill and pod failure scenarios.

### 2. Try Blue-Green Deployment (15 min)

Review and deploy a blue-green configuration where two full environments run side by side.
Traffic switches instantly from blue to green, with instant rollback by switching back.
```bash
cat blue-green-deployment.yaml
kubectl apply -f blue-green-deployment.yaml
```
Compare the blue-green approach with canary: blue-green is all-or-nothing, canary is gradual.
Blue-green is simpler but requires 2x resources during the switch.

### 3. Set Up Velero Backup (20 min)

Configure Velero to back up your cluster state to S3-compatible storage (MinIO for local Kind).
The schedule defines when backups run (e.g., daily at 2 AM).
```bash
kubectl apply -f velero-storage-location.yaml
kubectl apply -f velero-schedule.yaml
```
Storage location and schedule created. Verify with: `velero backup-location get`.

Run the backup automation script to create, validate, and manage backups programmatically.
Handles scheduled backups, integrity checks, retention policies, and backup reports.
```bash
python3 backup-automation.py
```
Output: backup status, validation results, and retention summary.

### 4. Validate Backups (10 min)

Run the restore validation script to verify backups can actually be restored.
A backup is only useful if you've tested that it restores correctly.
```bash
bash restore-validation.sh
```
Output: restore test results confirming data integrity.

### 5. Add Security Scanning to CI (10 min)

Review the reusable GitHub Actions workflow that adds security scanning to your CI pipeline.
Scans container images for CVEs and Kubernetes manifests for misconfigurations.
```bash
cat security-scan.yaml
```
Study how this plugs into the CI pipeline from Session 3.

### 6. Run Resilience Tests (10 min)

Run the test suite that validates SLO definitions, backup configuration, and chaos experiment YAML.
Confirms all resilience components are correctly structured and ready for production.
```bash
python3 test-resilience.py
```
All tests should pass if Session 7 components are in place.

## Deliverable
- One chaos experiment run against your test cluster with documented observations
- Velero backup schedule configured
- A production readiness checklist for one of your services
