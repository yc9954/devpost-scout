---
slug: "zeroday"
url: "https://devpost.com/software/zeroday"
title: "SpectreAI"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 922
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# SpectreAI

> Bot issues flood your Slack. SpectreAI investigates autonomously, converses with users, and fixes bots via CLI — developers only decide, never dig

[Devpost](https://devpost.com/software/zeroday) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]]
**domain** [[developer_tools]] [[disaster_emergency]] [[finance_payments]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** github-contents-api, gpt-4.1-mini, jira-api, python, slack-api, uipath-action-centre, uipath-coded-agents-(python), uipath-integration-service, uipath-maestro, uipath-orchestrator, xml

## How they structured the write-up

- inspiration
- what it does
- how i built it
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spectreai

## Body

Bot down to Draft PR — fully automated in under 2 minutes. SpectreAI multi-agent architecture — Maestro orchestrating Investigation, Coding, and Escalation agents Draft PR raised automatically — XAML patch with full root cause and confidence score in the description Inspiration Every RPA team knows this pain. A bot fails in production. An end user messages the support channel. A developer drops everything, digs through Orchestrator logs, finds the broken XAML line, patches it, raises a PR — all while the user waits with zero visibility. That's 2–4 hours of developer time, every single failure. I built SpectreAI to eliminate that loop entirely. What it does SpectreAI is a multi-agent agentic system orchestrated by UiPath Maestro. A single Slack message triggers a fully automated pipeline: Maestro classifies the request as a bug or enhancement InvestigationAgent runs a 3-layer log fetch (job logs, business exception logs, transaction item logs), queries SpectreKB (a knowledge base that learns from every past diagnosis), and produces a structured root cause analysis with a confidence score CodingAgent fetches the XAML via GitHub API (no cloning), produces a surgical patch, validates the XML, commits via API, and raises a labelled Draft PR The developer wakes up to a PR — not a crisis Three paths are fully covered: Happy Path — high-confidence bug → automatic XAML patch → Draft PR Escalation Path — low confidence → Slack buttons → user escalates → Jira ticket + Action Centre task Enhancement Path — not a bug → Jira enhancement ticket auto-created → Slack confirmation sent How I built it Layer Technology Orchestration UiPath Maestro (BPMN process) Investigation Python Coded Agent — Orchestrator API, SpectreKB, GPT-4.1 mini Code patching Python Coded Agent — GitHub API, XML validation, Draft PR Trigger Slack shortcut → Maestro event listener Ticketing Jira via UiPath Integration Service Human review UiPath App (Action Centre) The CodingAgent never clones the repo. It fetches XAML files via the GitHub API, sends them to the reasoning engine for a surgical patch, validates the XML before any commit, and only touches the repo if the patch is clean. No broken code ever reaches the repository. How we built it We started with the orchestration layer — designing the Maestro BPMN process to handle all routing logic before writing a single line of agent code. This forced us to think clearly about every path upfront: bug vs enhancement, high vs low confidence, fix done vs fix not done. The Investigation Agent was built as a Python Coded Agent with three distinct log fetch layers — job logs, exception logs, and transaction item logs — all merged into a single context window before hitting the reasoning engine. SpectreKB was layered on top to inject past diagnosis patterns, giving the agent institutional memory across failures. The Coding Agent was the hardest piece. We deliberately avoided cloning the repo — every file fetch, commit, and PR creation goes through the GitHub Contents API. This meant building a robust patch pipeline: fetch XAML → reasoning engine produces surgical diff → XML validation → base64 encode → SHA-based commit → Draft PR with labels and full context in the description. The entire system is wired together through UiPath Integration Service — Slack for triggers and notifications, Jira for ticket creation, and Action Centre for human review on escalation paths. Challenges we ran into GitHub API without cloning — building a reliable XAML patch workflow using only the GitHub Contents API required careful handling of base64 encoding, SHA-based commits, and XML validation before every write SpectreKB context injection — making the reasoning engine use past diagnoses without hallucinating required careful prompt engineering and structured output enforcement Maestro BPMN routing — wiring Slack triggers, agent invocations, Jira integration, and the Action Centre app into a single coherent BPMN process required iterative debugging of bindings and entry points UiPath token scopes — navigating PAT scopes and robot token permissions for Orchestrator API access was a significant blocker that required working around missing LLM scope assignments Accomplishments that we're proud of Zero repo cloning — the CodingAgent patches production XAML entirely through the GitHub API. No local environment, no clone, no risk of stale code. XML validation before every commit — broken XAML never touches the repository. The agent validates the patched file before writing a single byte to GitHub. End-to-end in under 2 minutes — from Slack message to Draft PR, the entire happy path completes in under 2 minutes with no human intervention. Three fully working paths — Happy Path, Escalation, and Enhancement all work end-to-end in a live demo, not just in theory. SpectreKB — a knowledge base that gives the reasoning engine memory of past diagnoses, making every subsequent investigation smarter than the last. Human-in-the-loop at exactly the right moment — escalation is a user decision via interactive Slack buttons, not an automated assumption. The system knows what it doesn't know What we learned UiPath Maestro is a genuinely powerful orchestration layer for multi-agent systems — the BPMN model maps naturally to agentic routing logic Reasoning engines are most reliable when given structured output schemas with confidence scoring — open-ended LLM calls produce inconsistent results in production The best agentic systems keep humans in the loop at exactly the right moment — not too early, not too late What's next for SpectreAI Auto-merge for high-confidence fixes after CI passes SpectreKB learning from every diagnosis automatically Proactive monitoring — detect failures before they hit the queue Expand to any UiPath process in the org, not just Invoice Processing <div