# Session 8 Demo — AI-Augmented Platforms

## Demo Overview
The capstone AI session. Explore the full spectrum of AI platform capabilities —
from document search to multi-agent incident response to governance.

## Dependencies — Run This First
```bash
pip3 install scikit-learn pyyaml --break-system-packages
# Optional (for LLM features): export ANTHROPIC_API_KEY=your-key-here
```

## Steps
```bash
# 1. AI-POWERED: RAG document search (no API key)
# Indexes your platform documentation using TF-IDF and answers natural language queries.
# Runs sample queries automatically and shows retrieved docs with relevance scores.
python3 rag-platform-docs.py
# Output: ranked search results for each query. New developers find answers instantly instead of searching wikis.

# 2. AI-POWERED: Multi-agent incident response
# Simulates a production incident handled by three specialized agents working in sequence:
# Triage Agent (severity, blast radius) → Diagnosis Agent (root cause) → Remediation Agent (fix actions).
# Each agent has a specific role, with human-in-the-loop approval for critical actions.
python3 incident-agent.py
# Output: full incident timeline showing triage, diagnosis, and recommended remediation steps.

# 3. AI-POWERED: Agent observability metrics
# Demonstrates how to monitor AI agents the same way you monitor services:
# latency per agent call, confidence scores, human override rates, and error tracking.
python3 ai-agent-observability.py
# Output: sample Prometheus metrics showing agent health, performance, and governance indicators.

# 4. Review AI governance alerts
# Prometheus alert rules that fire when AI behavior drifts: confidence drops below threshold,
# human override rate spikes (agents making bad suggestions), or agent latency exceeds SLO.
cat ai-governance-alerts.yaml
# These alerts treat AI agents as first-class services with the same observability standards.
```

## Key Concepts
- RAG: AI searches your platform docs — no more stale wikis, no API key needed
- Multi-agent: specialized agents for triage, diagnosis, remediation working together
- Human-in-the-loop: AI suggests, humans approve critical actions
- Observability for AI: you need to monitor AI agents just like you monitor services
- Governance alerts: automated warnings when AI confidence drops or override rates spike
- Start local (TF-IDF, heuristics), add LLMs (Claude) when the workflow is proven
