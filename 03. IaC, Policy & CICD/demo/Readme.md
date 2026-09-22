# Session 3 Demo — Self-Service IaC + Shift-Left Policies + AI Templates

## Demo Overview
Submit a self-service database claim, catch policy violations with conftest,
and explore AI-generated service configuration.

## Dependencies — Run This First
Requires a running Kind cluster with Crossplane installed (from Session 2):
```bash
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm install crossplane crossplane-stable/crossplane --namespace crossplane-system --create-namespace
```

## Steps
```bash
# 1. Review the Crossplane XRD (the "menu" developers see)
# An XRD defines what parameters a developer can set when requesting infrastructure.
# Think of it as a simplified API: name, size, version — nothing about the underlying provider.
cat xrd-postgresql.yaml

# 2. Review the Composition (what the platform team wrote behind the scenes)
# The Composition maps the developer's simple claim to the actual cloud resources.
# Platform team maintains this complexity so developers never see it.
cat composition-postgresql.yaml

# 3. Submit a database claim (the developer experience)
# This is all a developer writes: 10 lines of YAML requesting a PostgreSQL database.
# Crossplane handles provisioning, credentials, and connection secrets automatically.
cat demo-app-database.yaml
kubectl apply -f demo-app-database.yaml
# Output: the claim is accepted. Crossplane provisions resources in the background.

# 4. Run conftest to catch a bad manifest
# conftest evaluates Kubernetes manifests against OPA/Rego policies BEFORE they reach the cluster.
# The test manifests intentionally violate policies (missing labels, privileged containers, no resource limits).
conftest test conftest-tests/test-manifests.yaml -p conftest-tests/
# Output: FAIL/WARN for each violation — this is shift-left validation in action.

# 5. Review the Rego policy that caught it
# This is the actual policy code. Rego is the policy language for OPA.
# Study how deny rules enforce required labels, block privileged containers, and require resource limits.
cat conftest-tests/policy.rego

# 6. AI-POWERED: Review the AI-generated service template
# Demonstrates how AI can generate boilerplate Kubernetes config from a natural language description.
# The platform validates AI-generated output with the same conftest policies as human-written code.
cat backstage-ai-template.yaml
```

## Key Concepts
- Developer submits 10 lines of YAML, platform provisions the database
- conftest catches violations BEFORE code reaches the cluster
- AI templates: developers describe their service in plain English, AI generates the Kubernetes config
- The platform validates AI-generated output with the same policies as human-written code
