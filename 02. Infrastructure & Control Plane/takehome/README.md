# Session 2 Takehome — Build Your Control Plane

## Dependencies — Run This First
```bash
# Docker Desktop must be running
# Install Kind and kubectl if not already installed
brew install kind kubectl   # macOS
pip3 install pulumi pulumi-kubernetes --break-system-packages
```

## What to Do After the Session

### 1. Set Up Your Own Kind Cluster (10 min)

Create a fresh cluster to experiment with independently from the workshop cluster.
```bash
kind create cluster --name my-platform
```

### 2. Create Multi-Environment Config (15 min)

Review the multi-environment configuration that defines dev/staging/prod namespace templates.
Study how resource quotas and limits differ across environments.
```bash
cat multi-env-config.yaml
```

### 3. Apply Developer RBAC (10 min)

Apply a scoped developer role (read pods, logs, exec into containers — but cannot delete namespaces or modify RBAC).
The service account gives CI/CD pipelines a least-privilege identity.
```bash
kubectl apply -f rbac-developer-role.yaml
kubectl apply -f service-account.yaml
```
Verify the roles were created with `kubectl get clusterrole` and `kubectl get serviceaccount -A`.

### 4. Deploy a Test Application (10 min)

Deploy a simple app to confirm the cluster, RBAC, and quotas work together end-to-end.
This validates that a developer-scoped service account can deploy within its namespace.
```bash
kubectl apply -f demo-app-deployment.yaml
```
Check the pod is running: `kubectl get pods -A`.

### 5. Run Validation Tests (10 min)

Verify RBAC configs are correctly structured (file existence, required fields, valid YAML).
```bash
python3 test-rbac-permissions.py
```
Results show pass/fail for each RBAC validation check.

Run cluster health tests to confirm nodes are ready and system pods are running.
```bash
python3 test-cluster-health.py
```
All tests should pass if your cluster is healthy and Session 2 steps were completed.

## Deliverable
A running Kind cluster with:
- 2+ team namespaces with resource quotas
- Developer RBAC roles applied
- A test application deployed
- All health checks passing
