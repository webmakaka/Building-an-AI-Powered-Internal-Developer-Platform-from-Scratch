# Session 3 Takehome — CI/CD Pipelines & Policy Authoring

## Dependencies — Run This First
Requires a running Kind cluster from Session 2.
```bash
# Install conftest and pre-commit if not already installed
brew install conftest               # macOS (or see https://www.conftest.dev/install/)
pip3 install pre-commit --break-system-packages
```

## What to Do After the Session

### 1. Study the CI/CD Pipeline Architecture (20 min)

Review how GitHub Actions reusable workflows chain together to form a complete CI/CD pipeline.
Each file handles one stage: build/test, security scan, and deploy.
```bash
cat backend-pipeline.yml          # Orchestration workflow
cat reusable-workflows/build-and-test.yaml
cat reusable-workflows/security-scan.yaml
cat reusable-workflows/deploy.yaml
```
Map how these workflows chain together via workflow_call.
The orchestrator calls each reusable workflow in sequence — teams get consistent pipelines without copy-pasting YAML.

### 2. Write Your Own Conftest Policy (20 min)
Study `deny-privileged-containers.yaml` and `require-tests-passed.rego`.
Write a new policy that enforces a label (e.g., `team` must be present).
Test it: `conftest test your-manifest.yaml -p your-policy/`

### 3. Set Up Pre-Commit Hooks (10 min)

Review the pre-commit config that runs conftest and YAML linting on every git commit.
This ensures policy violations are caught on the developer's machine, not in CI.
```bash
cat .pre-commit-config.yaml
pip3 install pre-commit --break-system-packages
pre-commit install
```
After `pre-commit install`, every `git commit` will automatically validate manifests against your policies.

### 4. Explore Guardrails (15 min)

Run the guardrail validator — a Flask webhook that validates infrastructure claims against org policies.
It enforces rules like "production-tier databases can only be created in production namespaces".
```bash
python3 guardrail-validator.py
```
The output shows which claims pass and which are rejected, with reasons.

Run infrastructure tests to validate the complete provisioning workflow.
```bash
python3 test-infrastructure.py
```
Tests verify claim application, readiness, secret creation, and app connectivity.

## Deliverable
- A custom Rego policy that enforces one of your org's rules
- Pre-commit hooks configured to run conftest on every commit
