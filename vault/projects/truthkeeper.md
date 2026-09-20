---
slug: "truthkeeper"
url: "https://devpost.com/software/truthkeeper"
title: "TruthKeeper"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 694
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# TruthKeeper

> Your stack is lying to itself. TruthKeeper is the agent that listens.

[Devpost](https://devpost.com/software/truthkeeper) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[provenance_signing]] [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]]

**stack** bigquery, cloud-run, fastapi, fivetran, gemini, google-adk, hubspot, model-context-protocol, neon, nextjs, postgresql, python, salesforce, shadcn-ui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for truthkeeper

## Body

Title card — "Your stack is lying to itself" The green "✓ Approved" live writeback The 5-disagreement feed with € amounts The D1 hero — €89 + three corrective actions Inspiration Every B2B company runs on a dozen SaaS tools — Salesforce, Stripe, HubSpot, and more — and every one of them quietly disagrees with the others. Salesforce says a customer churned; Stripe is still billing them; HubSpot is still sending onboarding emails. Nobody notices — until the customer emails, furious, or finance finds the leak months later. If a company doing 20 million a year loses even a small fraction of revenue to these silent disagreements, that's somewhere between 200,000 and 600,000 dollars every year — invisibly . There are dashboards for whether your servers are up, but nothing watching whether your systems are telling the same truth. That gap — operational truth monitoring — is the thing we set out to build. What it does TruthKeeper is an autonomous cross-system reconciliation agent. It does three things: Onboards itself to your stack. Through Fivetran's official MCP server, the agent discovers your connected systems, introspects their schemas, profiles the data, then proposes an entity model (how Customer, Subscription, and Invoice map across systems) and learns your vocabulary. You review and approve, and the result persists as a per-company agent spec. Same agent, different companies, different specs. Reconciles. It runs the spec's discrepancy rules across the synced data and finds where systems disagree — for example, a Salesforce account marked Churned that still has an active Stripe subscription. Explains and acts. Each disagreement comes with a plain-language explanation of how it arose, a monetary impact estimate, and drafted corrective actions. Approve one and it writes back to the live system (Stripe, Salesforce, or HubSpot) through a real executor — with every approval audited to Postgres. In the demo, the agent catches Acme Corp : marked churned in Salesforce but still on an active, billing Stripe subscription — 89 euros a month leaking — and drafts the three-system fix (cancel the Stripe subscription, confirm the Salesforce status, remove from the HubSpot sequence). One human tap executes it against the live systems. How we built it Agent: Google's Agent Development Kit (ADK) with Gemini 2.5 Pro on Vertex AI. Partner integration: Fivetran's official MCP server attached as an ADK tool — structurally load-bearing for onboarding (without it, schema discovery and the entity-model proposal can't happen). Data: Fivetran into BigQuery. Backend: Python + FastAPI on Cloud Run. Frontend: Next.js, Tailwind, and shadcn/ui on Vercel. State: Postgres on Neon (per-company specs + the approval audit log). Write-back: Stripe, Salesforce (OAuth 2.0 JWT Bearer), and HubSpot. Production: even the demo stays in Google's ecosystem — the cinematic cold open was generated with Google Veo on Vertex AI, and the narration uses Google Cloud Text-to-Speech . Challenges we ran into Making Fivetran MCP structurally required at the foundation of onboarding — real MCP usage against a live account, not compliance theater. Keeping rule SQL deterministic over snake_case Fivetran tables so reconciliation returns the right rows live. Migrating Salesforce auth to OAuth 2.0 JWT Bearer, because username-password OAuth is silently blocked on modern Agentforce and Developer Edition orgs. And making write-back idempotent and auditable with a deterministic violation hash that keys an append-only Postgres approvals table, so actions survive cache evictions and reopened dialogs. Accomplishments that we're proud of A real agent that shapes itself per company — entity model and vocabulary are inferred from the customer's own data, not hand-coded. Closed-loop, human-in-the-loop corrective action against three live SaaS systems, fully audited. And a clear, named category: operational truth monitoring . What we learned Reliability beats AI purity for a demo that has to work live. Let the agent do the genuinely agentic work — discovery, entity mapping, vocabulary, explanation, monetary impact — and keep the parts that must be exact, like rule SQL and action dispatch, deterministic. What's next for TruthKeeper A meta-agent that also synthesizes the reconciliation rules per company, not just the entity model and vocabulary. A single "total at risk" number across all disagreements. And more connected systems, plus a second company to show the per-company variation. <div