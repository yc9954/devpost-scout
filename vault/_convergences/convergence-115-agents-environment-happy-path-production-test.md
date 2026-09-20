---
tags:
  - "convergence"
projects: 3
hackathons: 2
---

# 3 projects, 2 hackathons, one claim

**Shared vocabulary** agents, environment, happy, path, production, test

### [[time-traveler-w3cxp0]] — Time-Traveler
> a change that passes every test can still be catastrophic because the test environment differs from production in the one dimension that matters, which is scale

*GitLab AI Hackathon* · problem: validation runs against data that does not resemble the data it will meet

### [[redagent]] — RedAgent
> we test agents by walking the happy path and rarely place them in an environment that is actively trying to break them, which is the only environment production resembles

*GitLab AI Hackathon* · problem: verification covers intended behaviour and omits adversarial conditions entirely

### [[gauntlet-wlv7og]] — Gauntlet
> agents are tested on the happy path, so they forget or never knew what they were not supposed to do, and the failure surfaces only once someone hostile is on the other side

*Elasticsearch Agent Builder Hackathon* · problem: evaluation covers intent and omits adversarial pressure entirely
