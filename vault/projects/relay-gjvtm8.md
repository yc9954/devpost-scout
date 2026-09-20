---
slug: "relay-gjvtm8"
url: "https://devpost.com/software/relay-gjvtm8"
title: "RELAY"
hackathon: "Slack Agent Builder Challenge"
organization: "Salesforce"
winner: true
words: 722
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# RELAY

> RELAY manages Slack Connect channels for CSMs

[Devpost](https://devpost.com/software/relay-gjvtm8) · hackathon [[Slack Agent Builder Challenge]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[housing_homeless]] [[labor_employment]] [[transportation]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** alembic, anthropic, asyncpg, celery, claude, docker, fastapi, github-api, hubspot-api, model-context-protocol, pgvector, postgresql, pydantic, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration Customer success management has been migrating into Slack Connect channels. The shared channel between a vendor and its customers has become the place where renewals are won or lost, and it is also the surface where questions go unanswered longest, buried under status updates and side threads until a customer follows up a second time. We wanted to find out whether an agent could sit inside that channel and do the unglamorous work a good CSM does to ensure no questions fall through: notice the message that genuinely needs a reply, understand who is asking and what is at stake, gather the context scattered across the CRM, the docs, and the codebase, and draft a grounded answer, all without ever posting to a customer on its own. What it does RELAY is a Slack-native customer success agent for teams managing Slack Connect customer channels. It: Watches registered customer channels and classifies each incoming message, creating a tracked question only when one is actually being asked. Tracks SLA risk per account and alerts the account owner by DM before the response window closes, rather than after it has been missed. Assembles an evidence bundle for every question from HubSpot, from indexed GitHub and documentation via pgvector semantic search, and from permission-aware Slack search. Drafts a cited reply that the CSM reviews inside a Slack modal, with stale-source warnings shown inline so the reviewer can see when a document behind a citation has since changed. Posts only after a human approves, then stores the resolution as memory that informs similar questions later. RELAY never sends messages without human approval, only drafts, cites, and flags issues How we built it The backend is Python 3.12 on FastAPI, with Slack Bolt handling the OAuth, Events API, interactivity, App Home, and slash-command surface. A Celery and Redis worker pool runs classification, retrieval, drafting, and source sync off the request path so Slack always gets an immediate ack. State lives in PostgreSQL 15 with pgvector for embeddings, SQLAlchemy 2 async over asyncpg, and Alembic migrations. Tenant isolation is enforced at the database through row-level security keyed on the workspace, and every workspace, connector, and CRM token is encrypted at rest with AES-256-GCM. Draft generation runs on the Anthropic Claude SDK against an evidence bundle built from Voyage embeddings, the HubSpot API, the GitHub API, and Slack's real-time search. RELAY also exposes its context tools through a Model Context Protocol server, so an assistant like Claude can reach question, account, and evidence context through a governed interface rather than raw queries. The whole system deploys to Railway as a web and worker pair. We built it with a two-agent workflow, using Codex and Claude in tandem against a plan-by-plan PRD, with a human review gate at each plan boundary. Challenges we ran into I do not come from a technical background and have no real coding experience, so almost every architectural decision was something I had to reason about conceptually rather than from experience, making this a slow learning process. I also wanted to experiment with multi-agent and multi-harness building rather than lean on a single assistant, which took time to learn to coordinate. Multi-tenant safety was the other challenge: getting row-level security, encrypted tokens, and permission-aware Slack search to hold together under real Slack Connect conditions took a lot of work. Accomplishments that we're proud of The core loop is validated end to end in a real Slack Connect workspace, from install and channel registration through HubSpot and GitHub sync, SLA alerting, cited draft review, and approved posting. In beta use, it recorded a 100% SLA-met rate with a median time-to-send of three minutes across the questions it handled, while never once posting to a customer without a human approving first. This validation was extremely rewarding as it showed potential for actual real-world use. What we learned I had never deployed an actual agent before this, so a large share of the work was learning tools I had never touched, from Railway for hosting the web and worker services to the queueing, the database, and the connector APIs that make the thing real rather than local. What's next Direct Google OAuth for Drive and Docs, richer admin and team management, a denser multi-account dashboard, and the path from private beta to a self-serve Slack Marketplace listing. <div