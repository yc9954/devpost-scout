---
slug: "guardian-ai-governed-incident-response"
url: "https://devpost.com/software/guardian-ai-governed-incident-response"
title: "Guardian — AI-Governed Incident Response"
hackathon: "Airia AI Agents Hackathon"
organization: "airia"
winner: true
words: 1296
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/developer"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Guardian — AI-Governed Incident Response

> 5-node autonomous pipeline: triages P1 alerts, fetches runbooks, gets HITL approval, spins up war rooms, and auto-generates DORA/SOX post-mortems — all in under 12 seconds.

[Devpost](https://devpost.com/software/guardian-ai-governed-incident-response) · hackathon [[Airia AI Agents Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[human_in_the_loop]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[finance_payments]] [[health_clinical]] [[security_privacy]]
**user** [[developer]] [[government_staff]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** airia-agent-studio, airia-compliance-automation, airia-document-generator, airia-governance-dashboard, airia-hitl-node, airia-knowledge-graph, airia-mcp-gateway, atlassian-confluence, atlassian-jira, claude-3.5-sonnet, dora-article-11, jest, node.js-20-esm, pagerduty-events-api-v2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for guardian

## Body

Incidents dashboard — Guardian-triggered P1 alerts appear the moment the webhook fires. Incident detail — [GUARDIAN] payment-gateway degradation automatically classified, assigned and escalating. Guardian pipeline canvas (v15.00 · Published) — all five nodes wired end-to-end in Airia Agent Studio. Run steps — each node completes in sequence; entire pipeline succeeds in 3.6 seconds. Run timeline — Gantt view of node execution: Triage (61ms) → Runbook (664ms) → HITL Gate (285ms) → War Room (2.3s) → Compliance (64ms). Node 02 retrieves the exact runbook from Confluence via the Airia MCP Gateway + Knowledge Graph. Slack Guardian DM — multiple war-room activation messages arrive for each triggered incident. War room channel — #inc-*-payment-gateway auto-created, fully briefed: triage result, runbook steps, Jira ticket, HITL approver, and on-cal. Priority Highest, labelled dora-tracked + guardian-automated, linked to the Guardian audit session — zero manual input. Pipeline JSON output — full audit trail: HITL decision, war-room URLs, and compliance_status: DORA_SOX_COMPLIANT — all in one structur. Inspiration Fifteen years working inside Dutch financial institutions — watching P1 incidents at 2:47 AM unfold the same way every time. The first 12 minutes are pure coordination: who owns this? What severity? Where is the runbook? Create the Slack channel. Open the Jira ticket. Page the on-call team. Transaction failures accumulate while engineers scramble. That 12-minute overhead is not just inefficient — it is a compliance liability. The EU's Digital Operational Resilience Act (DORA Article 11) requires financial institutions to document every AI-assisted decision in their incident management workflow. Manual processes produce no audit trail. Neither do most agentic AI tools. Guardian was built to eliminate the overhead and produce the compliance record simultaneously. What it does Guardian is a 5-node autonomous incident response pipeline that handles the entire coordination phase — triage, runbook retrieval, human approval, war room setup, and regulatory post-mortem — without a single manual step. Node 01 — Triage Sentinel : Receives the PagerDuty webhook and applies deterministic P1/P2/P3 threshold logic in Python (same input always yields the same classification). Claude 3.5 Sonnet then generates a human-readable explanation of the reasoning — not a black box. Node 02 — Runbook Agent : Queries Confluence through Airia's MCP Gateway using semantic Knowledge Graph search. Zero credentials in code — all stored in Airia's vault. Returns the top runbook steps in under 2 seconds. Node 03 — HITL Gate : Uses Airia's MCP Apps (launched Feb 12, 2026) to render an interactive Slack approval card with clickable Approve / Escalate / Reject buttons. DORA Article 11 requires human oversight before automated action. Every approval is timestamped and tied to an identity — this is the compliance audit entry. Node 04 — War Room Coordinator : Spawns nested SlackSubAgent + JiraTicketSubAgent in parallel. Creates the #inc-*-payment-gateway channel, posts the AI-generated incident brief, and opens a Priority: Highest Jira ticket with all context pre-filled. Completes in under 4 seconds after approval. Node 05 — Compliance Narrator : Triggered on resolution. Generates a post-mortem with a full AI decision audit trail — every model call, its input data, reasoning, confidence score, and whether a human overrode it. Output: compliance_status: DORA_SOX_COMPLIANT . Your compliance officer can sign it. Your auditor will accept it. Zero manual coordination. Full regulatory audit trail. Automatically. How we built it Built entirely on Airia Agent Studio using 16 distinct platform features across the 5-node pipeline: Webhook Trigger → receives PagerDuty Events API v2 alerts Python Code Blocks ×5 → deterministic severity logic, orchestration AI Model Calls → Claude 3.5 Sonnet for reasoning and post-mortem generation Structured Output → type-safe JSON schema enforcement between all nodes Agent Variables → incident context passed through pipeline without re-prompting Knowledge Graph → semantic runbook search across Confluence RUNBOOKS space MCP Gateway → zero-credential connections to Confluence, Jira, and Slack MCP Apps → interactive Slack HITL approval card (Airia's newest feature) Human-in-the-Loop Node → 15-minute timeout with auto-escalation Nested Agent Architecture → Slack + Jira sub-agents executing in parallel Slack Bot Deployment → war room channel creation + HITL message delivery API Endpoint Deployment → production webhook receiver for PagerDuty Document Generator → 6-section post-mortem PDF with compliance template Governance Dashboard → full AI decision audit trail, timestamped per node Compliance Automation → DORA Article 11 + SOX Section 404 record generation Airia Community ×3 → Triage Sentinel, War Room Coordinator, Compliance Narrator All production secrets live in Airia's secrets vault. Zero credentials in code. Challenges we ran into MCP Apps discovery : Airia's MCP Apps launched February 12, 2026 — mid-build. Integrating interactive Slack buttons through an undocumented feature required active changelog monitoring and live platform testing, not local emulation. HITL + nested agent timing : The HITL Gate introduces variable human latency. Coordinating that with deterministic nested agent output (channel + ticket in ≤5s after approval) required careful Agent Variables schema design across nodes 03 → 04. DORA/SOX accuracy : The Compliance Narrator had to produce content a real compliance officer would accept. This required mapping each pipeline event to specific DORA Article 11 sub-requirements and SOX 404 IT General Controls — back to the primary legislation, not generic checklists. Knowledge Graph indexing latency : Confluence updates took up to 90 seconds to reflect in semantic search. Added a fallback cached runbook JSON in Airia Knowledge Base for demo resilience. Accomplishments that we're proud of The Governance Dashboard moment : Building an AI system that produces a machine-readable, auditor-acceptable explanation for every decision it made — with input data, model version, confidence score, and human override status — is what DORA Article 11 actually requires. Most AI incident tools don't produce this. Guardian does, automatically. MCP Apps HITL card : Getting interactive Approve / Escalate / Reject buttons working through Airia's newest feature — pausing the pipeline, capturing approver identity, and resuming with the decision in Agent Variables context — creates a demo moment that visibly impresses engineers who have built Slack integrations before. 127 passing tests : Every node has full unit coverage including P1/P2/P3 boundary conditions, critical-service multiplier logic, HITL timeout paths, and error handling. The pipeline is not just a demo — it is production-grade. 3 forkable Community modules that work standalone without any Airia dependency. The adapter layer in Triage Sentinel normalises PagerDuty, OpsGenie, Datadog, CloudWatch, and Prometheus — genuinely reusable, not theoretically reusable. What we learned Design compliance-first, not compliance-after : Guardian was designed with DORA Article 11 as a hard requirement from Day 1. The HITL gate is not optional. The governance logging is not an add-on. Every node's output schema carries audit-relevant data forward. If compliance is bolted on at the end, it shows. Airia's platform depth rewards investment : Using 16 distinct features forced deep engagement with every layer. The Knowledge Graph + MCP Gateway combination for runbook retrieval is substantially more powerful than a direct Confluence API call — semantic search produces better matches for edge-case alert patterns. The 40% failure statistic is a design constraint, not a tagline : Every engineering decision — deterministic algorithm before AI call, cached fallbacks, zero credentials in code, variable timing handling — is a direct counter to the failure modes that explain the 40%. What's next for Guardian Multi-cloud ingestion : AWS CloudWatch, Datadog, and OpsGenie adapters alongside PagerDuty. The Triage Sentinel Community module's normalisation layer is already structured for this. Predictive triage : Run Node 01 against Datadog anomaly streams before PagerDuty fires — alert engineers 2–3 minutes before threshold breach. Multi-jurisdiction compliance : HIPAA (healthcare), FISMA (government), and MAS TRM (Singapore finance) forks of the Compliance Narrator. The frameworks/ directory in the Community module is already structured for this. Real-time Governance Dashboard : Surface the AI decision audit trail live during the incident — not just in the post-mortem PDF — for compliance-team visibility during active response. <div