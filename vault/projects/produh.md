---
slug: "produh"
url: "https://devpost.com/software/produh"
title: "ProDuh! - The “duh” way to ship smarter"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 404
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
---

# ProDuh! - The “duh” way to ship smarter

> ProDuh! is a multi-agent, LLM-powered command center for PMs. It unifies Discovery→Operate, works with Jira/ADO, automates busywork, and turns strategy into shippable stories—fast.

[Devpost](https://devpost.com/software/produh) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[multi_agent]]
  <sub>weak: cross_origin_web, human_in_the_loop, sensor_fusion, structural_withholding</sub>
  <sub>weak: transportation</sub>
  <sub>weak: frontline_worker</sub>
  <sub>weak: sensor_telemetry, structured_db</sub>

**stack** adk, agentic-architecture, ai-agent, gemini, google, google-cloud, llm, openai, postgresql, prompt-engineering, react, sql

## Body

Inspiration 💡 PMs lose hours to copy/paste glue across Jira/ADO, Confluence, email, and chats. Strategy/KPIs rarely flow into stories—sprints drift from goals. Migrations (e.g., Jira ↔ ADO) create tool chaos and duplicated work. Lost in pages: decisions and context get buried across dozens of Confluence/Docs pages—ProDuh anchors a single canonical page per phase, auto-links related artifacts, and keeps My Notes attached so nothing gets lost. We wanted an AI layer that removes busywork so PMs can focus on decisions and people. 🖥️ What it does Multi-agent, LLM-powered command center for the PM lifecycle: Discovery → Strategy → Backlog → Jira Enhancements → GTM → Release → Operate. App-agnostic: works with Jira or ADO (plus Confluence, MS Graph, ServiceNow, GitHub read). Strategy → KPIs → Stories: turns goals into Jira/ADO-ready stories with AC, tasks, and QA checklist. Jira Enhancements: RICE/WSJF hints, dependency detection, DoD checklist. Docs & Notes: auto-create/update Confluence pages; My Notes for links and references. Human-in-the-loop with optional autonomous runs for repeatable flows. 😎 How we built it Multi-agent orchestration (Google ADK concepts + LLMs) with capped loops for determinism. Prompt engineering (e.g., DevelopmentTasksPrompt) to guarantee Jira-ready formats. Universal adapter layer for Jira/ADO parity; drivers for Confluence, MS Graph, ServiceNow, GitHub (read). Mock analytics CSV to prove KPI→Operate feedback. Node/Express backend, TypeScript/React frontend, JSON I/O for demo reliability. 🆘 Challenges we ran into Normalizing Jira vs ADO schemas and status flows. Balancing autonomy vs. oversight (keeping PM in control). Enforcing consistent acceptance criteria and story quality. Avoiding “LLM drift” → added guardrails and ≤3 loop cap. Keeping the demo fast while integrating multiple systems. 🚀 Accomplishments that we're proud of End-to-end flow from messy discovery notes to structured KPIs to Jira/ADO-ready stories. Priority & dependency intelligence that actually changes planning conversations. App-agnostic adapters so PMs can manage mixed stacks. Tight 2-minute demo that shows real PM pain disappearing. 📕 What we learned PMs don’t want another tool—they want a command center that talks to their tools. Clear, enforced output schemas beat clever prompts alone. Small QA micro-agents (requirements checks, DoD) deliver outsized value. Strategy telemetry must be designed before shipping, not after. 📈 What’s next for ProDuh! Deeper analytics loop: auto tracking plans, KPI binding, Operate insights. Risk & compliance agent for regulated environments. Roadmap coherence checks to catch drift early. Org policy packs (naming, AC/DoD templates, GTM checklists). Bi-directional Jira↔ADO sync with conflict resolution. Enterprise hardening: SSO, SOC2 guardrails, PII redaction. <div