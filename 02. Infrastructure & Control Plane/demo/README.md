# Session 2 Demo — Control Plane Walkthrough

## Demo Overview
Provision a Kind cluster and create isolated team namespaces with quotas and RBAC.

## Dependencies — Run This First
```bash
kind create cluster --name workshop
pip3 install pulumi pulumi-kubernetes --break-system-packages
```

## Steps
```bash
# 1. Review the Pulumi cluster code
# This is the IaC definition for provisioning a Kind cluster using Pulumi's Python SDK.
cat pulumi-cluster/__main__.py

# 2. Provision a team namespace with quotas
# Creates the team-alpha namespace with resource quotas, limit ranges, network policies, and service accounts.
# This is what platform teams run so developers never have to touch cluster-level resources.
python3 namespace-provisioner.py --namespace team-alpha --env dev --team alpha
# Output: confirmation of namespace, quota, network policy, and service account creation.

# 3. Provision a second namespace
# Same provisioner, different team. Shows how one script standardizes multi-tenant isolation.
python3 namespace-provisioner.py --namespace team-beta --env dev --team beta
# Output: identical provisioning for team-beta, proving the process is repeatable.

# 4. Verify what was created
# Confirm both namespaces exist and inspect the resource quota applied to team-alpha.
kubectl get ns
kubectl describe resourcequota -n team-alpha

# 5. Apply platform admin RBAC
# Creates ClusterRoles (platform-admin, operator, audit-viewer), ServiceAccounts,
# and bindings that define who can do what across the cluster.
kubectl apply -f rbac-platform-admin.yaml
# Output: list of roles, bindings, and service accounts created.

# 6. Review the platform services that run in the control plane
# These are the shared services (ingress, cert-manager, monitoring) the platform team manages centrally.
cat platform-services.yaml
```

## Key Concepts
- One command creates namespace + quota + limit range + RBAC
- Developers never touch cluster-level resources
- Resource quotas prevent any team from starving others
