---
slug: "cognilink-ai"
url: "https://devpost.com/software/cognilink-ai"
title: "CogniLink AI"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 797
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# CogniLink AI

> CogniLink AI orchestrates multiple specialized AIs to solve complex tasks by breaking down prompts into sub-tasks, using the best AI for each, and aggregating results into one unified output.

[Devpost](https://devpost.com/software/cognilink-ai) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[social_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** chatgpt, claude, cohere, github, make.com

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments
- what we learned
- market validation
- roadmap
- architecture (make.com scenario)
- what’s next immediately
- vision
- links

## Body

User Interface How it will answer queries Automated Feedback form Proof Proof Proof Proof Proof Proof Proof Proof Proof Proof Full Architecture FlowChart Simplified CogniLink AI — Devpost Submission Inspiration While applying to college, I kept switching between AI tools for writing, research, and images. Each switch meant re-explaining context and manually stitching outputs. That fragmentation wastes time and hides the real potential of AI collaboration. CogniLink AI asks a simple question: what if AIs could work together like a coordinated team, so users describe the goal once and the system orchestrates the best combination of models to deliver it? What It Does CogniLink AI is an AI orchestration layer that decomposes complex prompts into sub-tasks, routes each sub-task to the most capable model, runs tasks in parallel when possible, and merges the outputs into one coherent result. Core capabilities Request classification for task types (writing, coding, research, image). Intelligent routing to specialized models. Parallel execution with timeout and retry logic. Normalization and aggregation of heterogeneous outputs. Feedback loop with auto-acknowledgment and analytics. Token-based usage tracking for transparent metering. Example Prompt: “Create a startup pitch with visuals for an eco-friendly water bottle.” Pitch text → ChatGPT. Market insights → Cohere. Product mockups → Dreamlike Photoreal 2.0. Aggregator composes a single deliverable. How We Built It Stack Frontend: HTML/CSS/JavaScript (static, GitHub Pages). Orchestration: Make.com (webhooks, router, HTTP modules, JSON parsing, tools). Integrated AIs: OpenAI (ChatGPT 4o/4o-mini via AI Grants India credits), Cohere (text processing), Dreamlike Photoreal 2.0 (images). Data/Comms: Google Sheets (feedback), Make.com email automation. Process Architecture design: webhook intake → analyzer → router → parallel model calls → normalization → aggregation → response. Workflow automation in Make.com for classification, parallelization, error handling, and aggregation. API integrations and auth; JSON transformation; rate-limit handling. UI built from scratch and iterated with tester feedback. Feedback pipeline: submit → log → personalized email. Cost Built on free tiers and grant credits; total spend $0. Challenges Starting from zero coding background; learned APIs, JSON, and debugging rapidly. Free-tier rate limits and intermittent API errors; implemented retries and fallbacks. Make.com operation limits; optimized scenario steps. Output aggregation from different models and formats; built deterministic merge rules. Early rule-based classifier accuracy; iterated prompt logic and routing criteria. Time management alongside exams; relied on disciplined MVP scope. Accomplishments Deployed a working multi-model orchestration prototype. Internal tests show up to ~80% faster completion vs. manual tool switching. Zero-cost infrastructure with reliable pipelines. Automated end-to-end feedback system without custom backend. What We Learned Web basics (HTML/CSS/JS), REST API integration, workflow automation, JSON/data handling. Prompt design and model specialization; when to route vs. chain. MVP discipline and user-driven iteration; feedback loops matter more than features. Resourcefulness: grants and free tiers can carry a serious prototype. Market Validation Shortly after launch and hackathon submissions, a well-funded platform publicly shipped a “smart routing” feature similar to CogniLink’s thesis. That independent convergence validated the problem. Our differentiation is orchestration rather than simple switching: Their approach: choose one “best” model per request; users manually try others. CogniLink: break the request into sub-prompts, run multiple models in parallel and/or sequence, and synthesize a single answer. Roadmap Phase 2: Dynamic Chain Processing (next 3 months) Sequential AI-to-AI collaboration where each step consumes the previous step’s output. Context preservation across the chain. Demo flows like “Find trending tech news → write LinkedIn post → generate header image → propose hashtags.” Phase 3: Advanced Orchestration (6 months) Multi-modal automation (text, image, video, audio). Conflict-aware aggregation with scoring and reconciliation. More robust infrastructure for higher volume. Phase 4: Ecosystem (12 months) Open API and plugin architecture for third-party model providers. Marketplace of orchestration templates and revenue sharing. Longer Term Auth, personalization, usage dashboards. Mobile apps with voice input and notifications. Team workspaces and enterprise features. Architecture (Make.com Scenario) Inbound: Webhook receives user request. Analysis: JSON parsing and lightweight classification determine sub-tasks. Router: Branching logic selects models per sub-task. Parallel calls: HTTP requests to OpenAI, Cohere, Dreamlike, etc. Normalization: JSON adapters unify formats. Aggregation: Merge policies produce a single response. Feedback & Metrics: Logging to Google Sheets; automated emails; token usage tracking. Outbound: Webhook returns the final answer. (An exported image of the Make.com scenario is included in the submission gallery as the required architecture diagram.) What’s Next Immediately Harden classifier prompts and routing thresholds. Expand integrations (speech, video, research, data analysis). Grow to 100+ structured beta testers and publish case studies. Vision As models proliferate, the value shifts from individual tools to coordination. CogniLink’s goal is to become the neutral conductor that turns many specialized AIs into one reliable system, from simple text tasks to fully automated multi-modal creation. Links Live Prototype: https://ayushgupta-0108.github.io/CogniLink-AI/AuthBeta.html Website: https://ayushgupta-0108.github.io/CogniLink-AI/ Demo Video: https://drive.google.com/file/d/16yvfJdSYWzN1cVLoIy6-CTRXvY81rKmc/view GitHub: https://github.com/ayushgupta-0108/CogniLink-AI Feedback Form: https://forms.gle/wKHPr7rc3sKkuifm7 LinkedIn: https://linkedin.com/in/ayush-gupta-209a59343 Contact: ayush0108.gupta@gmail.com Built by an 18-year-old self-taught creator. Orchestration over isolation. <div