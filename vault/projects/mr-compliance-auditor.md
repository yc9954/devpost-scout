---
slug: "mr-compliance-auditor"
url: "https://devpost.com/software/mr-compliance-auditor"
title: "MR Compliance Auditor"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1142
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/media_journalism"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# MR Compliance Auditor

> AgentHero audits GitLab projects for SOC 2 compliance - per-MR audit with three agents, periodic project-wide reports, compliance advisor in Duo Chat and live monitoring dashboard on Google Cloud.

[Devpost](https://devpost.com/software/mr-compliance-auditor) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[media_journalism]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]]

**stack** claude-sonnet-4.6-(anthropic), flask, gitlab-duo-agent-platform, gitlab-graphql-api, gitlab-rest-api, google-bigquery, google-cloud-run, google-cloud-scheduler, google-pub/sub, looker-studio, python, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- why it matters
- challenges we ran into
- accomplishments we are proud of
- what we learned
- what's next for agenthero
- google cloud integration
- anthropic integration

## Body

Inspiration SOC 2 audits are painful not because the controls are complicated, but because the evidence is scattered. Every merge request needs documented authorization, independent review, test results, and security scanning. Most teams find out something is missing weeks before the audit, when it costs real time and money to fix. We wanted something that catches this at the point of change — inside the workflow developers already use, not in a separate compliance tool nobody opens. What it does Mention AgentHero in any MR comment and three agents run in sequence. Evidence Collector makes 15+ API calls with GraphQL fallbacks - pulling approvals, diffs, commits, pipeline results, security scans, vulnerabilities, linked issues, branch protection, and policy files. Compliance Analyst maps everything to all nine SOC 2 Common Criteria (CC1-CC9), scores each PASS/PARTIAL/FAIL and checks what we call the Golden Thread - four links that must exist for every production change: a linked issue (authorization), commits (implementation), test results (verification), and independent approval (review). It writes contextual risk analysis: not "SAST missing" but "you changed payment code and secret detection is not configured — this specific change exposes credentials to anyone with repo access." Auto-Fixer creates a pull request with files it can generate automatically (MR template, .gitignore) and opens a setup issue with instructions for files that need team input - CODEOWNERS, SECURITY.md, INCIDENT_RESPONSE.md. A Periodic Audit flow scans all merged MRs in any time window, detects direct pushes to main and generates a full SOC 2 Type II report with executive summary, exceptions table, and compliance score. A Compliance Advisor in Duo Chat answers questions like "Are we SOC 2 ready?" and "What should we fix first?" by reading all existing audit reports. Every audit result flows automatically to Google Cloud. BigQuery stores the history. Looker Studio shows the compliance trend. A live badge in the README shows the current score. When it drops below threshold, an email alert fires. How we built it GitLab Duo Agent Platform - two flows and one chat agent, all defined in YAML. The per-MR flow chains three AgentComponent agents with shared conversation history. The periodic audit runs as a single agent - multi-agent handoffs over long operations lost too much context, so single-agent collect-and-report was more reliable. Claude Sonnet 4.6 (Anthropic) powers all agents via the Duo Agent Platform. The core prompt engineering challenge: LLMs treat numbered steps as optional and drain token budget on long chat outputs before making tool calls. What worked - mandatory completion sequences with explicit forbidden states and generating reports internally so the agent has tokens left to call the tool. Google Cloud - six services handle continuous monitoring: Cloud Run (sync function, badge server, alert function), BigQuery (compliance data warehouse), Pub/Sub (alert routing), Cloud Scheduler (5-minute polling), Looker Studio (dashboard). The entire stack deploys with one script ( gcp/deploy.sh ). Why it matters Security and compliance are exactly the kind of high-volume, high-stakes, low-visibility work that eats engineering time without producing features. Every team has a compliance backlog. Nobody has time to audit every MR manually. AgentHero removes that bottleneck - the evidence is collected and scored automatically, at merge time, every time. Challenges we ran into The approvals API lies. When approvals_before_merge = 0 , the approved_by array is always empty — even after someone clicks Approve. We found this through repeated failed tests. Fix: parse MR system notes instead, which GitLab creates regardless of approval settings. 403 on every useful endpoint. Branch protection and approval rules require Maintainer role. We added GraphQL fallbacks for every restricted endpoint, plus the notes-based approval fallback — three layers total. This made the tool more robust than if we had had full access from the start. Agents skipping tool calls. The Compliance Analyst wrote full audit reports as chat text, exhausted its context window, then stopped without posting anything. Fix: generate the report internally, call the tool without printing first. Silent truncation. create_issue descriptions get cut off with no error. Fix: short description in the issue body, full report as a follow-up comment. Accomplishments we are proud of AgentHero is not another code review tool. GitLab already has code review. What it does not have is a compliance layer that tracks evidence across the entire change lifecycle - from the issue that authorized the work, through the commit, the tests, the approval and into the audit trail. That gap is what AgentHero fills. Most existing compliance tools produce reports that nobody reads. They flag generic issues, miss the context of what actually changed and generate so much noise that teams stop acting on findings. The reports end up archived, the problems stay unfixed and the audit still fails. AgentHero produces reports that read like a real audit - specific findings tied to specific changes with actionable recommendations and a clear compliance score. Because the reports are useful, they get used. What we learned Making LLM agents reliable means designing prompts where the correct behavior is the only path that makes grammatical sense. Agents skip steps when the prompt gives them an easy exit - close that exit and they stop skipping. API gaps at lower permission levels are a useful forcing function. Working around them with fallback chains made the tool work in realistic service-account environments, not just ideal ones. What's next for AgentHero Automatic CODEOWNERS generation from git blame history Slack and Teams integration for compliance alerts SOC 2 Type II evidence package export as PDF ISO 27001 and GDPR framework support Multi-project compliance dashboard for engineering managers Google Cloud integration AgentHero uses six Google Cloud services for continuous compliance monitoring: Cloud Scheduler triggers a sync every 5 minutes Cloud Run (sync function) polls GitLab API, parses AgentHero:score= metrics from issue comments, writes to BigQuery — deduplicated by note ID BigQuery stores every audit result with scores, findings, timestamps, and MR metadata Cloud Run (badge server) queries BigQuery and serves a live color-coded SVG badge (green >=70, yellow >=40, red <40) Pub/Sub routes alerts when periodic score drops below 50 or per-MR score drops to 3 or below Cloud Run (alert function) subscribes to Pub/Sub and sends email via Gmail Looker Studio connects to BigQuery for the live compliance dashboard All infrastructure is scripted in gcp/deploy.sh — one command, idempotent, deploys everything. Anthropic integration All agents run on Claude Sonnet 4.6 via the GitLab Duo Agent Platform. The core contribution on the Anthropic side was figuring out how to make Claude reliably execute multi-step tool sequences under real constraints: limited context window, no persistent memory between agent turns, and a platform that provides no feedback when a tool call is skipped. The prompt patterns we developed - mandatory completion sequences, forbidden-state instructions, internal report generation — are directly transferable to any Claude-based agent that needs to complete a workflow reliably rather than just produce a good response. <div