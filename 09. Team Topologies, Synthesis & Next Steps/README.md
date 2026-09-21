# Session 9 — Team Topologies, Synthesis & Next Steps

**Day 2 | Session 5 of 5**

## Overview

The final session brings everything together. You'll map your organization into Team Topologies (stream-aligned, platform, enabling, complicated-subsystem), collect DORA metrics as your post-workshop KPI baseline, and measure AI impact in business terms. This is where you build the 30/60/90-day plan you'll take back to your team.

## What You'll Learn

- Conway's Law: your platform will mirror your org structure — design both intentionally
- Team Topologies: four team types and three interaction modes
- DORA metrics: deployment frequency, lead time, MTTR, change failure rate
- AI impact measurement: hours saved, incidents resolved faster, cost avoided
- Building a 30/60/90-day platform adoption roadmap
- Presenting platform ROI to leadership

## Knowledge Prerequisites

- Everything from Sessions 1-8
- Understand Conway's Law (system design mirrors org communication structure)
- Know what Team Topologies are (stream-aligned, platform, enabling, complicated-subsystem)
- Familiar with DORA metrics as the industry standard for engineering productivity
- Comfortable presenting technical value in business terms (hours saved, cost reduced)

## Tools Required

- Python 3, pyyaml, scikit-learn (same setup from previous sessions)

## Verify Your Setup

```bash
python3 verify_module.py
```

## Contents

| Folder | What's Inside |
|---|---|
| [demo/](demo/) | Team topology generator, platform KPI collector, AI impact measurement |
| [takehome/](takehome/) | Maturity re-assessment, cost baseline, friction re-analysis, 30/60/90-day roadmap |

## Quick Start

```bash
# Demo
cd demo

# Map your org into Team Topologies types and visualize interaction modes
python3 team-topology-generator.py

# Collect DORA metrics: deployment frequency, lead time, MTTR, change failure rate
python3 platform-kpi-collector.py

# Quantify AI impact in business terms: hours saved, incidents resolved faster
python3 measure-ai-impact.py

# Take-home exercises
cd takehome

# Re-run the maturity assessment — compare with your Day 1 score
python3 platform-maturity-assessment.py

# Capture cost baseline for 30/60/90-day tracking
python3 cost-analyzer.py

# Re-analyze friction points — has your understanding of bottlenecks evolved?
python3 friction-analyzer.py --workflow onboarding
```

## Key Takeaway

Measure before you build, measure after you ship, and present in business terms. The maturity assessment, DORA metrics, and AI impact numbers are your ammunition for getting leadership buy-in. Re-run at 30/60/90 days to prove the platform's value.

## Platform Engineering Adoption & Stickiness — Resource Guide

A curated collection of resources organized by the problems you'll face when adopting and scaling platform engineering. Every link has been verified as of April 2026.

---

### Foundational Frameworks & Models

These define the vocabulary and mental models the industry uses. Read these first.

| Problem | Resource | Link |
|---|---|---|
| No shared language for team structure and interaction | *Team Topologies* — Matthew Skelton & Manuel Pais (book) | [teamtopologies.com](https://teamtopologies.com/) |
| Don't know what "mature" looks like for a platform | CNCF Platform Engineering Maturity Model | [tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) |
| Need an industry definition of what a platform actually is | CNCF Platforms White Paper | [tag-app-delivery.cncf.io/whitepapers/platforms](https://tag-app-delivery.cncf.io/whitepapers/platforms/) |
| No framework for measuring developer productivity holistically | The SPACE of Developer Productivity — Forsgren et al. (ACM Queue, 2021) | [queue.acm.org/detail.cfm?id=3454124](https://queue.acm.org/detail.cfm?id=3454124) |
| Teams keep measuring the wrong things | DORA Capabilities: Platform Engineering | [dora.dev/capabilities/platform-engineering](https://dora.dev/capabilities/platform-engineering/) |
| Need data to justify platform investment to leadership | Accelerate State of DevOps Report 2024 | [dora.dev/research/2024/dora-report](https://dora.dev/research/2024/dora-report/) |
| Want the latest DORA research including AI + platform quality | Accelerate State of DevOps Report 2025 | [cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| Architecture doesn't match org structure | Conway's Law — Martin Fowler | [martinfowler.com/bliki/ConwaysLaw.html](https://martinfowler.com/bliki/ConwaysLaw.html) |

---

### Platform as a Product

If developers don't voluntarily adopt your platform, it's dead. These resources teach product thinking for internal platforms.

| Problem | Resource | Link |
|---|---|---|
| Platform exists but nobody uses it — no product thinking | "Mind the Platform Execution Gap" — Evan Bottcher (Martin Fowler's site) | [martinfowler.com/articles/platform-prerequisites.html](https://martinfowler.com/articles/platform-prerequisites.html) |
| Don't know how to apply product management to an internal platform | Product Management for Internal Developer Platforms — platformengineering.org | [platformengineering.org/blog/product-management-for-internal-developer-platforms](https://platformengineering.org/blog/product-management-for-internal-developer-platforms) |
| Platform adoption is mandated, not voluntary — developers resent it | Platform as a Product (PlatformCon talk) | [platformengineering.org/talks-library/platform-as-a-product](https://platformengineering.org/talks-library/platform-as-a-product) |
| No clear definition of what an IDP is | What is an Internal Developer Platform? | [internaldeveloperplatform.org/what-is-an-internal-developer-platform](https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/) |
| Want to see how Spotify built and scaled Backstage | Celebrating Five Years of Backstage — Spotify Engineering | [engineering.atspotify.com/2025/4/celebrating-five-years-of-backstage](https://engineering.atspotify.com/2025/4/celebrating-five-years-of-backstage) |
| Evaluating developer portals beyond Backstage | Portal IQ — Platformetrics portal comparison tool | [portal-iq.platformetrics.com](https://portal-iq.platformetrics.com/) |

---

### Cognitive Load & Developer Experience

Platform stickiness comes from reducing friction. These resources explain why and how.

| Problem | Resource | Link |
|---|---|---|
| Teams are overwhelmed — too many tools, too much context switching | "Whose Cognitive Load Is It Anyway?" — platformengineering.org | [platformengineering.org/blog/cognitive-load](https://platformengineering.org/blog/cognitive-load) |
| Platform team doesn't know where developer friction actually is | How Platform Teams Reduce Cognitive Load — Team Topologies newsletter | [teamtopologies.com/news-blogs-newsletters/2024/6/10/newsletter-june-2024-how-platform-teams-reduce-cognitive-load](https://teamtopologies.com/news-blogs-newsletters/2024/6/10/newsletter-june-2024-how-platform-teams-reduce-cognitive-load) |
| Need to understand cognitive load as an organizational design tool | Team Cognitive Load — IT Revolution | [itrevolution.com/articles/cognitive-load](https://itrevolution.com/articles/cognitive-load/) |
| Monolith vs microservices debate is missing the real issue | "Monoliths vs Microservices is Missing the Point — Start with Team Cognitive Load" — IT Revolution | [itrevolution.com/team-cognitive-load-team-topologies](https://itrevolution.com/team-cognitive-load-team-topologies/) |
| Platform is too thick — doing too much, moving too slow | What is a Thinnest Viable Platform (TVP)? — Team Topologies | [teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp](https://teamtopologies.com/key-concepts-content/what-is-a-thinnest-viable-platform-tvp) |
| Microsoft's research on what actually drives developer productivity | Developer Experience at Microsoft | [developer.microsoft.com/en-us/developer-experience](https://developer.microsoft.com/en-us/developer-experience) |

---

### Team Topologies in Practice

Moving from theory to implementation. Case studies, patterns, and practical guidance.

| Problem | Resource | Link |
|---|---|---|
| Don't know which team type to start with | The Four Team Types from Team Topologies — IT Revolution | [itrevolution.com/articles/four-team-types](https://itrevolution.com/articles/four-team-types/) |
| Need a step-by-step adoption guide | Get Started with Team Topologies in 8 Steps — IT Revolution | [itrevolution.com/articles/get-started-with-team-topologies-in-8-steps](https://itrevolution.com/articles/get-started-with-team-topologies-in-8-steps/) |
| Want real-world examples of Team Topologies adoption | Team Topologies Case Studies | [teamtopologies.com/examples](https://teamtopologies.com/examples) |
| Need to design platform-centric org with domain thinking | Designing Platform-Centric Organizations — Team Topologies blog | [teamtopologies.com/news-blogs-newsletters/designing-platform-centric-organizations-with-domain-thinking-and-team-topologies](https://teamtopologies.com/news-blogs-newsletters/designing-platform-centric-organizations-with-domain-thinking-and-team-topologies) |
| Platform strategy needs executive-level framing | Designing and Executing a Platform Strategy — Team Topologies | [teamtopologies.com/platform-engineering](https://teamtopologies.com/platform-engineering) |
| Want a real-world TVP journey (Trade Me case study) | Trade Me's Journey Towards a Thinnest Viable Platform | [teamtopologies.com/industry-examples/trade-me-journey-towards-a-thinnest-viable-platform](https://teamtopologies.com/industry-examples/trade-me-journey-towards-a-thinnest-viable-platform) |
| Five years of lessons from Team Topologies adoption | Team Topologies: Five Years of Transforming Organizations — IT Revolution | [itrevolution.com/articles/team-topologies-five-years-of-transforming-organizations](https://itrevolution.com/articles/team-topologies-five-years-of-transforming-organizations/) |

---

### Platform Value & Metrics

Proving ROI and justifying continued investment. These help you speak leadership's language.

| Problem | Resource | Link |
|---|---|---|
| Can't articulate platform ROI to leadership | Unlocking the True Value of Your IDP Investments — IT Revolution | [itrevolution.com/articles/unlocking-the-true-value-of-your-internal-developer-platform-investments](https://itrevolution.com/articles/unlocking-the-true-value-of-your-internal-developer-platform-investments/) |
| Need concrete metrics beyond DORA | Platform Engineering Impact on Developer Productivity — DORA 2024 Takeaways | [middlewarehq.com/blog/platform-engineering-impact-on-developer-productivity-dora-report-2024-trends-and-takeaways](https://middlewarehq.com/blog/platform-engineering-impact-on-developer-productivity-dora-report-2024-trends-and-takeaways) |
| 70% of platform teams fail to deliver impact — why? | Why Up to 70% of Platform Engineering Teams Fail — The New Stack | [thenewstack.io/why-up-to-70-of-platform-engineering-teams-fail-to-deliver-impact](https://thenewstack.io/why-up-to-70-of-platform-engineering-teams-fail-to-deliver-impact/) |
| Hidden adoption crisis: developers bypass the platform | The Hidden Adoption Crisis in Platform Engineering | [medium.com/devops-ai-decoded/the-hidden-adoption-crisis-in-platform-engineering](https://medium.com/devops-ai-decoded/the-hidden-adoption-crisis-in-platform-engineering-and-how-to-actually-fix-it-cd3afec3042e) |
| Gartner's take on why platform engineering matters | Why Gartner Recommends Platform Engineering — Humanitec | [humanitec.com/blog/gartner-internal-developer-platforms-platform-engineering](https://humanitec.com/blog/gartner-internal-developer-platforms-platform-engineering) |
| Team Cognitive Load is a hidden crisis in tech orgs | Team Cognitive Load: The Hidden Crisis — IT Revolution | [itrevolution.com/articles/team-cognitive-load-the-hidden-crisis-in-modern-tech-organizations](https://itrevolution.com/articles/team-cognitive-load-the-hidden-crisis-in-modern-tech-organizations/) |

---

### Industry Reports & Trend Analysis

Stay current on where the industry is heading.

| Problem | Resource | Link |
|---|---|---|
| Need the definitive annual state of DevOps data | DORA Accelerate State of DevOps Report 2024 (full PDF) | [services.google.com/fh/files/misc/2024_final_dora_report.pdf](https://services.google.com/fh/files/misc/2024_final_dora_report.pdf) |
| Want to understand the 2025 shift from rankings to archetypes | Announcing the 2025 DORA Report — Google Cloud Blog | [cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) |
| Need the cloud/DevOps trends landscape | InfoQ Cloud and DevOps Trends Report 2025 | [infoq.com/articles/cloud-devops-trends-2025](https://www.infoq.com/articles/cloud-devops-trends-2025/) |
| Platform engineering evolution from DevOps — academic perspective | Toward Platform Engineering, the Evolution of DevOps — Wiley (2026) | [onlinelibrary.wiley.com/doi/abs/10.1002/smr.70108](https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.70108) |
| What does Microsoft think platform engineering is? | What is Platform Engineering? — Microsoft Learn | [learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering](https://learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering) |
| ThoughtWorks lessons from the trenches | The Evolution of Platform Engineering — ThoughtWorks | [thoughtworks.com/insights/blog/platforms/the-evolution-of-platform-engineering--lessons-from-the-trenches](https://www.thoughtworks.com/insights/blog/platforms/the-evolution-of-platform-engineering--lessons-from-the-trenches) |

---

### Community & Ongoing Learning

Stay connected after the course. These are the communities where practitioners share what actually works.

| Problem | Resource | Link |
|---|---|---|
| Need a community of platform engineers to learn from | PlatformEngineering.org — 25k+ member community | [platformengineering.org](https://platformengineering.org/) |
| Want conference talks from platform practitioners | PlatformCon — largest PE conference (free, virtual + in-person) | [platformengineering.org/events](https://platformengineering.org/events) |
| Need a curated list of PE tools and resources | Awesome Platform Engineering (GitHub) | [github.com/shospodarets/awesome-platform-engineering](https://github.com/shospodarets/awesome-platform-engineering) |
| Want another curated tooling list focused on IDP components | Awesome Platform Engineering Tools (GitHub) | [github.com/seifrajhi/awesome-platform-engineering-tools](https://github.com/seifrajhi/awesome-platform-engineering-tools) |
| Want to browse internal platform patterns and examples | Internal Platforms — community resource collection | [internalplatforms.com/resources.html](https://internalplatforms.com/resources.html) |
| CNCF Platform Engineering community initiatives for 2026 | CNCF Platform Engineering Technical Community Group | [cloudnativeplatforms.com](https://cloudnativeplatforms.com/) |
| Video tutorials and talks on platform engineering | Platform Engineering YouTube channel | [youtube.com/channel/UCKjVI0LawDxHaXSBMBOK1tA](https://www.youtube.com/channel/UCKjVI0LawDxHaXSBMBOK1tA) |

---

### AI & Platform Engineering — Thought Leadership

How AI is reshaping platform engineering strategy, adoption, and operations.

| Problem | Resource | Link |
|---|---|---|
| Need a comprehensive view of AI's role in platform engineering today | State of AI in Platform Engineering 2025 — Platformetrics & platformengineering.org whitepaper | [platformengineering.org/blog/state-of-ai-in-platform-engineering-2025](https://platformengineering.org/blog/state-of-ai-in-platform-engineering-2025) |
| Want to understand how GenAI informs platform strategy | "How Generative AI Informs Platform Engineering Strategy" — Ajay Chankramath, The New Stack | [thenewstack.io/how-generative-ai-informs-platform-engineering-strategy](https://thenewstack.io/how-generative-ai-informs-platform-engineering-strategy/) |
| Exploring whether platforms can accelerate AI adoption | "Can Platform Engineering Accelerate AI Adoption?" — Ajay Chankramath, The New Stack | [thenewstack.io/can-platform-engineering-accelerate-ai-adoption](https://thenewstack.io/can-platform-engineering-accelerate-ai-adoption/) |
| Need to make the case for PE as a developer experience investment | "Why Platform Engineering Leads to a Better Developer Experience" — Ajay Chankramath, The New Stack | [thenewstack.io/platform-engineering-leads-to-a-better-developer-experience](https://thenewstack.io/platform-engineering-leads-to-a-better-developer-experience/) |
| Want domain-driven approaches to next-gen platform engineering | "Domain Driven, AI-Augmented: Next Frontier in Platform Engineering" — Platformetrics | [platformengineering.org/blog/domain-driven-ai-augmented-the-next-frontier-in-platform-engineering](https://platformengineering.org/blog/domain-driven-ai-augmented-the-next-frontier-in-platform-engineering) |
| Need to understand why domain thinking matters for platforms | "The Need for Domain Driven Platform Engineering" — Platformetrics | [platformengineering.org/blog/the-need-for-domain-driven-platform-engineering](https://platformengineering.org/blog/the-need-for-domain-driven-platform-engineering) |
| Want a model for quantifying platform ROI | Platformetrics ROI Model — Platform investment analysis framework | [platformetrics.com/thought-leadership](https://platformetrics.com/thought-leadership.html) |

---

### Books

| Problem | Resource | Link |
|---|---|---|
| Need the complete platform engineering reference (this course's companion) | *The Platform Engineer's Handbook* — Ajay Chankramath (Packt, 2026) | [Amazon](https://www.amazon.com/Platform-Engineers-Handbook-developer-focused-streamline/dp/1806380137) |
| Need a practical guide to building effective platform teams and practices | *Effective Platform Engineering* — Ajay Chankramath, Sean Alvarez, Bryan Oliver, Nic Cheneweth (Manning, 2025) | [Amazon](https://www.amazon.com/Effective-Platform-Engineering-Ajay-Chankramath/dp/1633436497) \| [effectiveplatformengineering.com](https://effectiveplatformengineering.com/) |
| Need the foundational org design framework | *Team Topologies* — Matthew Skelton & Manuel Pais (IT Revolution, 2019) | [Amazon](https://www.amazon.com/Team-Topologies-Organizing-Business-Technology/dp/1942788819) |
| Need the research behind DORA metrics | *Accelerate* — Nicole Forsgren, Jez Humble, Gene Kim (IT Revolution, 2018) | [Amazon](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339) |
| Need the DevOps transformation narrative | *The Phoenix Project* — Gene Kim, Kevin Behr, George Spafford (IT Revolution, 2013) | [Amazon](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/1942788290) |
| Need the modern successor to The Phoenix Project | *The Unicorn Project* — Gene Kim (IT Revolution, 2019) | [Amazon](https://www.amazon.com/Unicorn-Project-Developers-Disruption-Thriving/dp/1942788762) |
| Need to understand flow-based delivery | *Flow Engineering* — Steve Pereira & Andrew Davis (IT Revolution, 2024) | [Amazon](https://www.amazon.com/Value-Stream-Clarity-Steve-Pereira/dp/1950508455) |
| Need Site Reliability Engineering foundations | *Site Reliability Engineering* — Betsy Beyer et al. (O'Reilly, 2016) | [Amazon](https://www.amazon.com/Site-Reliability-Engineering-Production-Systems/dp/149192912X) \| [Free online](https://sre.google/sre-book/table-of-contents/) |

---

## Go Deeper

This session covers Chapter 14 of [*The Platform Engineer's Handbook*](https://peh-packt.platformetrics.com/), which goes further into organizational design for platform teams, advanced adoption strategies, and measuring platform engineering ROI at scale. See the [book repo](https://github.com/achankra/peh) for the full code samples.

[Back to Course Overview](../README.md)
