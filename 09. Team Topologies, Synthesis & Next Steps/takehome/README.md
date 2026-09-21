# Session 9 Takehome — Your 30/60/90 Day Plan

## Immediate Actions (This Week)

### 1. Map Your Team Topology (20 min)

Identify your stream-aligned, platform, enabling, and complicated-subsystem teams.
Visualize how they interact and where your platform structure matches your org structure.
```bash
python3 ../demo/team-topology-generator.py
```
Document the interaction modes between teams. Does your platform structure
match your org structure? Where are the mismatches? These gaps are where friction lives.

### 2. Re-Run the Maturity Assessment (10 min)

Take the same assessment you ran on Day 1 and score your org again.
Your scores may not have changed, but your understanding of what each dimension means has.
```bash
python3 platform-maturity-assessment.py
```
Compare with your Day 1 score. The gap between "where we are" and "where we want to be" should now feel actionable.

### 3. Establish Cost Baseline (15 min)

Run the cost analyzer to capture your current resource usage and cost distribution across teams.
This baseline lets you measure cost optimization impact at 30/60/90 days.
```bash
python3 cost-analyzer.py
```
Output: per-namespace cost breakdown. Save this report for your leadership presentation.

### 4. Document Friction Points (15 min)

Re-run the friction analyzer with a workflow relevant to your team.
Compare with your Session 1 results to see if your understanding of the bottlenecks has evolved.
```bash
python3 friction-analyzer.py --workflow onboarding
```
Output: ranked friction points with time impact. These drive your 30-day action plan.

## Your 30/60/90 Day Roadmap

### 30 Days
- [ ] Identify top 3 friction points
- [ ] Map your team topology and interaction modes
- [ ] Pick ONE golden path to build first
- [ ] Set up Kind cluster for experimentation
- [ ] Deploy basic namespace provisioner
- [ ] Establish KPI baseline

### 60 Days
- [ ] Build first Backstage software template
- [ ] Implement one Crossplane XRD for self-service
- [ ] Add conftest to CI pipeline
- [ ] Deploy HPA for most variable service
- [ ] Define first SLO
- [ ] Pilot AI doc search (RAG) for your platform docs

### 90 Days
- [ ] Onboard second team to the platform
- [ ] Run first chaos experiment
- [ ] Measure adoption rate and developer satisfaction
- [ ] Evaluate AI alert correlation for your on-call workflow
- [ ] Present results to leadership
- [ ] Plan next quarter's platform roadmap

## Resources
- Book: [The Platform Engineer's Handbook](https://peh-packt.platformetrics.com/) (Packt, 2026)
- Book Code: [github.com/achankra/peh](https://github.com/achankra/peh)
- Platform Engineering community: platformengineering.org
- CNCF Platform WG: tag-app-delivery.cncf.io
