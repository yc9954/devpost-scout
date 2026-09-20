---
slug: "karma-the-reincarnation-agent-for-deprecated-services"
url: "https://devpost.com/software/karma-the-reincarnation-agent-for-deprecated-services"
title: "Karma — The Reincarnation Agent for Deprecated Services"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 924
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Karma — The Reincarnation Agent for Deprecated Services

> A multi-agent system that learns a deprecated service's hidden contracts and haunts its replacement, catching silent regressions every test misses. Gemini + Vertex AI Agent Builder + Dynatrace.

[Devpost](https://devpost.com/software/karma-the-reincarnation-agent-for-deprecated-services) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[security_privacy]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** cloud-pub-sub, cloud-run, cloud-scheduler, davis-ai, dock, dynatrace, dynatrace-mcp, fastapi, firebase-auth, firestore, gemini, gemini-2.5-flash, gemini-2.5-pro, github-actions

## How they structured the write-up

- 💡 inspiration
- 👻 what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next

## Body

Hero section 💡 Inspiration Every migration team has lived this story: You retire the old payments service. The replacement passes every unit test, integration test, and smoke test. CI is green. Load tests pass. The cutover goes smoothly. Three weeks later , a downstream service starts degrading — p95 latency climbs +540ms, throughput falls −7.8%. No alert fired. No test failed. No one can trace it. The culprit? The old service wrote a Redis summary key every 30 seconds. A downstream reporting service read that key directly. Nobody documented it. Nobody told the new team. No test checked it. Tests check the contract you wrote down . We built Karma to check the contract you forgot you had. 👻 What it does Karma is an autonomous multi-agent system that "haunts" deprecated services. It operates in two phases: Learning — while the old service is still alive, Karma analyzes up to 14 days of Dynatrace Grail telemetry and discovers its implicit behavioral contracts across 8 categories no test typically captures: latency bands, error semantics, throughput envelopes, side effects (the killer — cache writes, async tasks), timing, dependencies, resource usage, and sequencing. Every candidate contract is validated against the service's own history to reject false positives, then registered as an official Dynatrace SLO . Haunting — after cutover, Karma watches the replacement every 10 minutes. The moment a contract is silently violated, it files a ghost report : the violated contract, the measured downstream impact, a Davis AI root-cause correlation, a Dynatrace investigation notebook, a Slack alert — and a one-click draft remediation PR on GitHub with the exact diff that restores the lost behavior. The marquee finding Ghost detected — svc-payments-v3 [CRITICAL] Contract #4 violated: side_effect / cache_warming Expected: redis.SET recent_charges:summary every 30s Observed: 0 writes for 11 consecutive minutes Downstream impact: svc-reporting p95 latency: +540ms · throughput: −7.8% Root cause: cold cache forces synchronous DB fallback Davis AI confirms: ACTIVE PROBLEM P-2847 correlated. Avoided incident cost: $4,200 Every claim in that report is backed by real Dynatrace telemetry — the Redis write truly happens, the cache truly warms, and the downstream service truly degrades when it stops. How we built it Karma runs on Google Cloud's Vertex AI Agent Builder : four agents authored with the Agent Development Kit (ADK v1.0) running on Vertex AI Agent Engine , powered 100% by Gemini 2.5 (Pro for deep reasoning, Flash for high-frequency monitoring). Agent Role Model Coordinator Routes tasks via transfer_to_agent Gemini 2.5 Flash Learner Discovers contracts, creates SLOs Gemini 2.5 Pro Watcher Evaluates violation predicates every 10 min Gemini 2.5 Flash Forensic Root-cause, notebooks, ghost reports, PRs Gemini 2.5 Pro The agents talk to Dynatrace bidirectionally through the Dynatrace MCP Server : they read via Grail DQL, Davis AI analyzers, Smartscape entity resolution, and changepoint detection — and write back CUSTOM_ANNOTATION events, BizEvents, SLOs, Notebooks, and Workflows. Async pipeline: Cloud Scheduler → Watcher → Cloud Pub/Sub → Forensic (so detection never blocks investigation). Memory: Vertex AI Memory Bank keeps contracts alive across Agent Engine restarts. API: FastAPI on Cloud Run, 30+ routes, streaming ghost reports to the browser via Server-Sent Events. Frontend: Next.js 15 + TypeScript + Tailwind + ShadCN, a landing page and 6-page dashboard, Firebase Auth. Data/infra: Firestore, Google Secret Manager, Terraform, GitHub Actions with Workload Identity Federation (no long-lived keys). Self-observability: every agent run emits OTel spans and BizEvents to Dynatrace — Karma watches itself. Challenges we ran into Silent agent failures. ADK treats {identifier} in an instruction string as a session-state template variable — a stray {service_id} in a prompt raised a KeyError that killed the Gemini 2.5 Pro sub-agents before their first call , so they silently transferred without ever running their tools. We traced it through the OTel spans (only transfer_to_agent was firing) and fixed it by converting every agent instruction to an ADK InstructionProvider callable that bypasses state injection. Token-scope landmines. BizEvents and SLO creation 403'd silently because the deployed Dynatrace token was missing the bizevents.ingest and slo.write scopes — diagnosed only by probing the ingest endpoint directly, then rotating the token across Secret Manager, GitHub Actions, Agent Engine, and five Cloud Run services. DQL is strict. timeseries only accepts entity fields, count() needs a metric key, and you must alias before you sort — we iterated the Learner's query patterns against the live tenant until every category returned clean data. No fabricated data. We refused to mock the demo. We built a real three-service synthetic environment (v2 with the hidden Redis write, v3 without, and a Redis-dependent reporting service) with a k6 load generator, so every ghost report is grounded in genuine telemetry. Accomplishments we're proud of It dogfoods itself — Karma learned real behavioral contracts from its own production API and raised a custom Dynatrace problem on its own watcher's latency breach. Detection → reviewable fix in one loop — from a silent regression to a draft GitHub PR with the exact patch. A genuinely bidirectional Dynatrace integration, not just dashboards: SLOs, notebooks, workflows, and timeline annotations all written by the agents. What we learned Observability data is a far richer training signal than we expected — a service's traces encode contracts its authors never wrote down. We also learned how to make a multi-agent system trustworthy : validate every discovered contract against history, never fabricate telemetry, and make the agents observable enough to debug through their own spans. What's next Auto-discovery of migration candidates from Smartscape topology. Contract diffing across more than two service versions. Packaging the Learner as a reusable pre-cutover CI gate. <div