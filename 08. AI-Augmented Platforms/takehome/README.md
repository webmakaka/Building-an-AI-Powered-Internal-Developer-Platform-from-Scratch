# Session 8 Takehome — Build Your AI Platform Stack

## Dependencies — Run This First
```bash
pip3 install scikit-learn pyyaml --break-system-packages
# Optional (for LLM-powered features): export ANTHROPIC_API_KEY=your-key-here
```

## What to Do After the Session

### 1. Build a Full RAG Pipeline (30 min)

Build a complete Retrieval-Augmented Generation pipeline that combines TF-IDF retrieval with LLM-powered answers.
Without an API key, review the architecture and study the TF-IDF fallback that runs locally.
```bash
python3 rag_pipeline.py
```
Note: Requires ANTHROPIC_API_KEY for LLM features.
Output: end-to-end RAG flow from document indexing to query answering.

### 2. Explore Multi-Agent Orchestration (20 min)

Study the four-agent incident response architecture: Investigation, Classification, Remediation, Communication.
Each agent has a defined role, inputs, outputs, and escalation criteria.
```bash
cat multi_agent_system.py
```
Map how agents hand off to each other and where human approval gates sit.

### 3. Set Up AI Guardrails (15 min)

Enforce safety boundaries on AI-generated actions: rate limits, confidence thresholds, blocked operations,
and mandatory human approval for destructive actions (delete, scale-to-zero, production changes).
```bash
python3 ai-guardrails.py
```
Output: guardrail evaluation results showing which actions pass and which are blocked.

### 4. Automate a Runbook (20 min)

Convert a markdown runbook into structured, executable steps with diagnostic checks and approval gates.
The automator parses your existing runbook and adds safety controls automatically.
```bash
python3 runbook-automator.py
```
Output: structured runbook with categorized steps (diagnostic vs. action) and human approval requirements.

### 5. AI-Generated Service Templates (15 min)

Study how AI generates Kubernetes service configuration from a natural language description.
The template shows the input prompt, generated YAML, and how conftest validates the output.
```bash
cat backstage-ai-template.yaml
```
This is the same validation pipeline from Session 3 applied to AI-generated code.

### 6. Correlate Your Alerts (15 min)

Feed alert data into the correlation engine and see how it reduces noise.
Groups related alerts into incidents with root cause analysis using heuristic pattern matching.
```bash
python3 alert-correlator.py
```
Output: raw alerts grouped into correlated incidents with severity and root cause summary.

### 7. Run AI Agent Tests (10 min)

Run the test suite that validates the AI agent components: incident triage, RAG pipeline,
guardrails, and agent observability metrics.
```bash
python3 test-ai-agents.py
```
All tests should pass, confirming the AI stack is correctly wired together.

## Deliverable
- Identify one runbook to automate with AI
- Document 3 guardrails for any AI platform action
- Write an AI adoption plan: what to add first, what to wait on
- Run incident-agent and document how the triage → diagnosis → remediation flow maps to your on-call process
