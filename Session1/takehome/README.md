# Session 1 Takehome — Deep Platform Analysis

## What to Do After the Session

### 1. Run the Full Assessment (15 min)

Evaluate your platform against the 12 design principles from the book (API-first, self-service, guardrails, etc.).
Pass in the sample platform config to see which principles are met and which need work.

```bash
$ python design-principles-checklist.py ../demo/platform-config.yaml
```
The output shows a pass/fail for each principle with recommendations.
Use this to prioritize which design principles to address first.

### 2. Survey Your Developers (30 min setup)

Run an interactive CLI survey that collects developer feedback on onboarding, deployments, docs, and tooling.
Each question is scored 1-5 and rolled up into a composite DevEx score (0-100).

```bash
$ python devex-survey.py
```
Customize the survey questions for your org and send to 5-10 developers.
Collect responses over 1 week — this data feeds your platform business case.

### 3. Analyze Friction Points (15 min)

Map a specific developer workflow step by step and identify where time is wasted.
The onboarding workflow traces everything from "new hire joins" to "first deployment".

```bash
$ python friction-analyzer.py --workflow onboarding
```
The output highlights the top friction points ranked by time impact.
These are your quick wins — the first things to automate with your platform.

### 4. Establish Your Baseline KPIs (15 min)

Collect the four DORA metrics (deployment frequency, lead time, MTTR, change failure rate) for your current state.
These are the industry-standard metrics for engineering productivity.

```bash
$ python platform-kpi-collector.py
```
Record these numbers. You'll compare against them at 30/60/90 days to prove platform ROI.

## Deliverable
Write a 1-page "Platform State of the Union" for your team:
- Current maturity score (from assessment)
- Top 3 friction points (from analyzer)
- Proposed first golden path
