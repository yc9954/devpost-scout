---
slug: "drift-detect"
url: "https://devpost.com/software/drift-detect"
title: "Drift Detect"
hackathon: "Airia AI Agents Hackathon"
organization: "airia"
winner: true
words: 787
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/legal_justice"
  - "user/developer"
  - "user/legal_professional"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Drift Detect

> Catch scope creep before it costs you.

[Devpost](https://devpost.com/software/drift-detect) · hackathon [[Airia AI Agents Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[legal_justice]]
**user** [[developer]] [[legal_professional]] [[social_worker]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** airia, slackbot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for drift detect

## Body

DriftDetect SOW parser Inspiration If you work in a client services agency, consultancy, or software development firm, you know the single most dangerous phrase in the industry: "Hey, can we just add this one quick feature?" Scope creep is a silent killer. It drains profitability, exhausts engineering teams, and damages client relationships. The core problem usually isn't malicious intent; it's a lack of shared understanding. While project managers and stakeholders spend weeks negotiating a 30-page Statement of Work (SOW), the actual engineers and account managers dealing with the day-to-day requests rarely consult it. We were inspired to build Drift Detect to solve this exact disconnect. We wanted to build an automated referee—an AI system that sits right where the daily conversations happen (Slack), reads the original contract, and instantly flags when a casual request crosses the boundary into unbilled work. What it does Drift Detect is a multi-agent workflow that acts as a real-time boundary enforcer for your projects, built entirely on the Airia platform and integrated directly into Slack. Our solution consists of two targeted agents: The SOW Parser (The Intake Engine): Users simply paste a heavy, jargon-filled legal contract (Statement of Work) into a Slack direct message. The parsing agent instantly analyzes the text, extracting the explicit In-Scope Deliverables , Out-of-Scope Exclusions , and Assumptions , creating a structured, machine-readable project baseline. The Drift Detect Orchestrator (The Monitor): Once the baseline is established, project teams continually monitor their daily communications. When a client or team member asks for a new feature, a project manager can send that request in a direct message to the Drift Detect bot. The Orchestrator evaluates the request against the saved scope boundary map and instantly replies, letting the team know if the request is safely "In-Scope" or if it represents "Scope Drift" that requires a Change Order. How we built it We built the entire intelligence layer using Airia Agent Studio , leveraging its powerful multi-agent workflow capabilities. Platform: Airia Agent Studio Interface: Slack Bot Webhooks Architecture: We designed a sequential pipeline. The first node (The SOW Parser) utilizes an LLM prompted for strict data extraction to turn unstructured text into a JSON boundary map. This data is held in memory and passed to the Orchestrator node. The Orchestrator acts as an active agent, taking conversational input via Slack direct messages and referencing the stored memory to evaluate intent against the rigid ruleset. Deployment: We utilized Airia's Webhook Events API to deploy the agents directly into a live Demo Slack Workspace, ensuring a zero-friction experience for the end-user. Challenges we ran into Integrating a multi-agent pipeline into a conversational Slack interface presented several unique challenges: Context Management: Ensuring the Orchestrator agent accurately remembered the precise boundaries established by the SOW Parser agent required careful prompt engineering and workflow structuring within Airia to pass context cleanly between nodes. Slack UI Constraints: Airia's default behavior for multi-step workflows often forces replies into Slack threads. We had to embrace this constraint and design our user experience around it, realizing that threading long SOW summaries is actually a superior UX for keeping main channels clean. Deployment Nuances: Navigating the difference between public OAuth distribution and private Webhook integrations took time, ultimately leading us to create a dedicated Demo Workspace to showcase the "Airia Everywhere" capability without forcing judges to configure API tokens. Accomplishments that we're proud of We are incredibly proud of seamlessly bridging the gap between rigid legal documents and casual workplace chat. Proving that an AI agent can successfully interpret a complex, $\$280,000$ corporate agreement and then enforce those technical boundaries through a simple Slack direct message feels like a massive step forward for project management. We are also proud of our deployment execution—delivering a working, verifiable Slack integration that perfectly fits the "Airia Everywhere" category. What we learned Building Drift Detect was a masterclass in Agent Orchestration . We learned that breaking down a complex problem into specialized agents (a Reader vs. an Enforcer) produces vastly superior results compared to forcing one massive prompt onto a single AI model. We also gained deep practical experience integrating Airia workflows directly into enterprise communication tools like Slack via Webhooks. What's next for Drift Detect The current iteration handles natural language text parsing beautifully. Next, we plan to: Direct File Ingestion: Allow the SOW Parser to ingest raw PDF and DOCX files directly via Slack file uploads. Jira/Linear Integration: If the Orchestrator detects "Scope Drift," we want it to automatically generate a drafted "Change Request" ticket in Jira and send it to the Account Manager for review. Financial Impact Estimation: Enhance the Drift Detect bot to estimate the cost of the requested drift based on the hourly rates established in the original SOW. <div