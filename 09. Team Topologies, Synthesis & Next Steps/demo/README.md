# Session 9 Demo — Workshop Synthesis, Team Topologies & Next Steps

## Demo Overview
Visualize how your platform mirrors your org structure, establish a KPI baseline,
and measure ongoing platform and AI impact.

## Steps
```bash
# 1. Team topology visualization (Conway's Law in practice)
# Maps your organization into the four Team Topologies types: stream-aligned, platform,
# enabling, and complicated-subsystem teams. Visualizes interaction modes between them.
python3 team-topology-generator.py
# Output: team map showing which teams own what, how they interact (collaboration, X-as-a-Service,
# facilitating), and where your platform structure matches (or conflicts with) your org structure.

# 2. Collect platform KPIs
# Collects the four DORA metrics: deployment frequency, lead time, MTTR, and change failure rate.
# These are the industry-standard measures of engineering productivity.
python3 platform-kpi-collector.py
# Output: current metric values and performance band (elite, high, medium, low).
# Compare with your Session 1 baseline to measure improvement.

# 3. Measure AI impact (if AI features were adopted)
# Quantifies the value of AI platform features: time saved on doc searches, incidents triaged faster,
# alert noise reduced, and runbook automation coverage.
python3 measure-ai-impact.py
# Output: AI impact metrics in business terms — hours saved, incidents resolved faster, cost avoided.
# Use these numbers when presenting platform ROI to leadership.
```

## Key Concepts
- Conway's Law: your platform will mirror your org structure — design both intentionally
- Team Topologies: stream-aligned teams consume the platform, platform teams build it, enabling teams bridge the gap
- Measure before you build: you need a baseline to prove value
- DORA metrics are the industry standard for engineering productivity
- Present to leadership in business terms: hours saved, cost reduced
- Re-run at 30/60/90 days to show progress
