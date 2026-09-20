---
slug: "changeshield-ai-a-splunk-agentic-changeops-commander"
url: "https://devpost.com/software/changeshield-ai-a-splunk-agentic-changeops-commander"
title: "ChangeShield AI: Splunk Agentic ChangeOps Commander"
hackathon: "Splunk Agentic Ops Hackathon"
organization: "Splunk"
winner: true
words: 725
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# ChangeShield AI: Splunk Agentic ChangeOps Commander

> Splunk-grounded AI agents that catch risky deployments before they become incidents, scoring deploy risk, finding root cause, and writing human-approved fixes back to Splunk.

[Devpost](https://devpost.com/software/changeshield-ai-a-splunk-agentic-changeops-commander) · hackathon [[Splunk Agentic Ops Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** mcp, splunk, splunk-ai-assistant, splunk-ai-toolkit, splunk-enterprise, splunk-mcp-server

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for changeshield ai

## Body

Inspiration Most production incidents don't start as mysterious failures — they start as ordinary deployments. Teams already have the deploy events, logs, metrics, traces, and security signals in Splunk, but the answer to "is this change safe to ship, and if it breaks, why?" is scattered across dashboards and tribal knowledge. We wanted to move agentic operations earlier — before a risky change becomes an incident and make every AI conclusion provable from Splunk data. What it does ChangeShield AI turns Splunk into an agentic ChangeOps control plane. For a deployment (reference scenario: checkout-v42 ) it: Scores pre-deploy risk (0–100) from latency forecasts, error spikes, payment-queue saturation, historical similarity to past rollbacks, and security context. Runs a pipeline of AI agents that query Splunk live through the Splunk MCP Server . Produces an evidence-bound RCA — every claim links to the exact SPL, MCP tool, source index, row count, and sample rows. No hallucination. Renders a live "war room": animated risk gauge, SLO forecast, service signals, a blast-radius graph, and an incident timeline. Proposes remediation (rollback, feature-flag disable, notify on-call, postmortem) behind a human-approval gate , then writes the approved decision back to Splunk ( index=changeshield_agent_audit ).  How we built it Backend: a FastAPI orchestrator coordinating specialized agents — query planner, preflight risk, anomaly/forecast, security context, correlation/RCA, remediation, and an optional hosted-model summarizer. Real Splunk integration (not simulated): Splunk Enterprise 10.4 + MCP Server 1.2. Agents call MCP tools ( splunk_run_query , splunk_get_* , saia_* ) over JSON-RPC using the MCP Server's encrypted bearer tokens . Telemetry is ingested via HEC ; indexes, lookups, and saved searches are provisioned over the REST API ; index discovery and ad-hoc search use the official Splunk SDK for Python . Evidence ledger binds every agent claim to its query result; unit and golden tests reject any claim without evidence. Frontend: Next.js + React, recharts (SLO forecast), reactflow (blast-radius graph), and Server-Sent Events for the live agent-event stream. AI: the Splunk MCP Server drives the agents; AI Assistant for SPL ( saia_* ) generates and explains SPL; AI Toolkit / ML-SPL paths back forecasting and outlier detection. Challenges we ran into We insisted on running against a real Splunk + MCP runtime instead of a mock — which surfaced a string of issues a fake would have hidden: The MCP Server authenticates with RSA-encrypted bearer tokens minted from its token endpoint; we had to implement that flow. MCP tool argument contracts differed from our assumptions ( type vs indexes , saved_searches vs savedsearches , the query arg, TLS verification) — every real call failed until aligned. | lookup service_catalog.csv needs a lookup definition that wasn't installed, so the SLO check silently errored. Our evidence layer truncated results to the first rows, which dropped the most-recent incident peak of a time series — so risk under-fired on real data. risk_tags ingested as a JSON array became an unmatchable multivalue field; a historical-similarity subsearch had no time range and missed past incidents. HEC ingestion is asynchronous, so analysis launched right after seeding hit an indexing race — we made the seed step wait for searchable data. Splunk-hosted foundation models live in Splunk Cloud Services, so on local Enterprise we built the hosted-model path as an opt-in, evidence-grounded integration with graceful fallback. Accomplishments that we're proud of A genuinely end-to-end run on real Splunk + real MCP : checkout-v42 scores High (77/100) with four evidence-linked reasons, a payment-router root cause, and a human-approved audit writeback. Evidence-bound by construction — no operational claim survives without Splunk evidence. A broad, real Splunk developer-tools footprint: MCP Server + Python SDK + REST API + HEC + packaged knowledge objects. What we learned "Works in the demo" and "works on Splunk" are very different problems — the truth lives in the real runtime. MCP is a powerful, uniform way to give agents governed access to Splunk, but tool contracts and auth must be exact. Grounding every AI claim in queryable evidence is the difference between a plausible assistant and a tool an operator can trust. What's next for ChangeShield AI Connect Splunk Cloud hosted models for the executive-summary and natural-language investigation paths. Drive analysis from live CI/CD deploy webhooks instead of a seeded scenario. Expand the policy engine and wire real rollback / feature-flag providers behind the approval gate. Saved-search-backed continuous monitoring and alerting. <div