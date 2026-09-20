---
slug: "tfguardian"
url: "https://devpost.com/software/tfguardian"
title: "TFGuardian"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 720
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# TFGuardian

> 5 AI agents that review your Terraform like a real platform engineering team

[Devpost](https://devpost.com/software/tfguardian) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[measured_ablation]] [[multi_agent]] [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** checkov, claude-(anthropic), fastapi, gitlab-duo-agent-platform, gitleaks, go, google-cloud-run, infracost, python, react, terraform, tfsec, workload-identity-federation

## How they structured the write-up

- inspiration

## Body

dark mode Inspiration Every week, platform engineering teams ship 50+ Terraform merge requests. Only a fraction get reviewed. Security vulnerabilities, cost overruns, and compliance gaps ship to production unchecked — invisible until something breaks. We asked: what if a team of AI agents could review every single MR, just like a real platform engineering team? ## What it does TFGuardian is 5 specialized AI agents on the GitLab Duo Agent Platform that review Terraform infrastructure automatically: Platform Engineer — Scans dependencies with tfoutdated (our custom Go CLI), auto-fixes version constraints, runs terraform validate and plan SecOps — Audits security with tfsec, gitleaks, and checkov. Finds and auto-fixes vulnerabilities, commits changes FinOps — Calculates real infrastructure costs using infracost with GCP pricing API GreenOps — Analyzes carbon footprint using Google Cloud's published Carbon Free Energy data across 45 regions Architect — Compiles everything into a Review Board report with a governance verdict and posts it directly on the merge request One @mention triggers all five agents. Results from our latest run: 18 security vulnerabilities fixed, costs reduced from $556/mo to $18/mo, and 96% carbon emission reduction. ## How we built it GitLab Duo Agent Platform — 5 sequential AgentComponents with context passing, routers, and AGENT_DONE markers for reliable transitions Anthropic Claude — Powers all agents with tool use, extended thinking, and multi-step reasoning. Each agent calls 5-7 real CLI tools autonomously Real security tools — tfsec (static analysis), gitleaks (secret detection), checkov (CIS compliance) — not hallucinated findings Real cost tool — infracost with GCP pricing API for actual dollar amounts Custom Go CLI — tfoutdated, built from scratch, scans Terraform dependencies, detects breaking changes, and auto-fixes version constraints Live Dashboard — React + FastAPI at tfguardian.live with GitLab OAuth, MR list with agent status detection, one-click trigger scan, real-time flow visualization, per-agent log filtering, full report viewer with mermaid diagrams, and an Azure AI Foundry-style Flow Editor for prompt engineering Google Cloud — Cloud Run hosting, Workload Identity Federation (zero-secret auth), Artifact Registry, deployed via official Google GitLab Components Policy-as-Code — AGENTS.md defines hard rules (BLOCK), soft rules (REVIEW_REQUIRED), and recommendations with environment-specific policies for sandbox, staging, and production ## Challenges we ran into Making 5 agents reliably hand off context and produce a unified 10K+ character report on the merge request The GreenOps agent had all carbon data in its prompt, so Claude skipped tool calls entirely — we had to force explicit commands AI Catalog caches flow YAML aggressively — changes require git tags to force sync OAuth tokens expire every 2 hours but signed cookie sessions last 24 hours — built auto-refresh with token rotation Parsing raw GitLab job traces to classify which actions belong to which agent required AGENT_DONE markers and a multi-pass parser ## Accomplishments that we're proud of All 5 agents work end-to-end — from @mention to 10K+ Review Board report posted on the MR, fully automated Real tools, real results — tfsec found 18 vulnerabilities, infracost calculated actual GCP pricing, Google CFE data for 45 regions Custom Go CLI — tfoutdated published on GitHub, handles dependency scanning, breaking change detection, and auto-fix Live dashboard — tfguardian.live lets you watch agents work in real-time, trigger scans with one click, edit agent prompts, and export reports as PDF Zero-secret deployment — GCP Workload Identity Federation means no service account keys anywhere in the pipeline Policy governance — deterministic verdict system (BLOCK/REVIEW/PASS/SAFE) with Claude Reasoning Trace explaining every decision ## What we learned The GitLab Duo Agent Platform is genuinely powerful for multi-agent orchestration, but prompt engineering for reliable tool-calling flows requires iteration Real security scanners (tfsec, checkov) find significantly more issues than LLM-only analysis — the combination of AI reasoning + real tools is the sweet spot Policy-as-code governance needs deterministic rules in structured documents, not just free-form AI judgment Building a live dashboard that parses agent traces in real-time taught us that agent observability is as important as agent capability ## What's next for TFGuardian AWS and Azure provider support (currently GCP-focused) Parallel agent execution — FinOps and GreenOps could run simultaneously Integration with GitLab merge request approval rules — BLOCK verdict automatically prevents merge Prompt A/B testing in the Flow Editor — compare different prompt versions side by side Historical trend dashboards — track security posture, cost, and carbon footprint over time <div