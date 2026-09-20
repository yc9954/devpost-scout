---
slug: "devgenius"
url: "https://devpost.com/software/devgenius"
title: "Agent Anansi"
hackathon: "AI in Action"
organization: "Google"
winner: true
words: 575
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Agent Anansi

> Agent Anansi: The world's first AI-powered CI/CD that cares about your code AND your team - six specialized agents make development faster, safer, and more human

[Devpost](https://devpost.com/software/devgenius) · hackathon [[AI in Action]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[video_visual]]

**stack** cloudrun, gemini-2.0-flash, gitalb-ci, google-agent-development-kit, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for agent anansi

## Body

Detailed Architecture gitlab ci actions(all 6 agents) Simple Architecture Inspiration As someone deeply passionate about DevOps and AI, I was frustrated by the fragmented and reactive nature of traditional CI/CD workflows. While automation is widespread, intelligence is often lacking — developers still manually review code, hunt down security issues, or burn out in silence. Inspired by African mythology, I envisioned Agent Anansi as a digital spider weaving intelligent threads through the CI/CD pipeline. I wanted to create a practical, scalable, and human-centered DevOps assistant powered by AI agents that could do more than just automate — it could think , optimize , and care . What it does Agent Anansi is a fully automated, AI-powered CI/CD assistant that integrates directly into GitLab pipelines. It consists of 6 specialized agents , each handling a different facet of modern software delivery: 🔍 Issue Triage Agent – Automatically categorizes and prioritizes issues. 🔀 Code Review Agent – Reviews merge requests and code changes. 🔐 Security Scan Agent – Scans the codebase for vulnerabilities and insecure dependencies. ⚡ CI Optimizer Agent – Analyzes pipeline performance and recommends optimizations. 📚 Documentation Generator Agent – Auto-generates API and project documentation. 💚 Burnout Detector Agent – Monitors developer patterns to detect signs of burnout. Each agent generates structured JSON reports, and all insights are aggregated into a single job that visualizes the results. This creates an intelligent feedback loop on every commit or merge request. How I built it The project is built with: Python 3.11 for agent logic and REST endpoints. Google Cloud (Google AI Studio, Google Agent Development Kit + Cloud Run) to deploy the agents and host the intelligence layer. GitLab CI/CD for deep integration and automation across code analysis and deployment. Google Gemini Flash 2.0 as the core LLM for natural language understanding and reasoning. I wrote modular HTTP handlers for each AI agent and designed the pipeline to be fail-tolerant and trigger-based (main branch, MRs, or manually). All AI responses are formatted into machine-readable reports stored as CI artifacts. Challenges I ran into Burnout Detection Design: Quantifying developer wellness using commit metadata was novel, and required creative metrics design to avoid false positives. YAML Management: Handling shared configuration for multiple agents and ensuring secure, minimal Docker environments without bloating image sizes was tricky. Accomplishments that I'm proud of Created 6 fully working AI agents with real endpoints and live results integrated into GitLab pipelines. Designed a developer wellness AI agent — a feature I haven’t seen in any mainstream CI/CD tool. Successfully deployed everything to Google Cloud Run , making the platform truly plug-and-play for any GitLab team. The final demo script brings the results to life with detailed feedback, artifact reports, and a beautiful console showcase. What I learned The power of multi-agent AI systems is in their composition. Each agent is simple, but together they orchestrate complex DevOps decisions. Even solo, you can ship a full-stack AI product with CI/CD, cloud infra, and usable interfaces if you focus on automation and reuse. Monitoring developer wellness can and should be part of the CI/CD process. It’s not just about code — it’s about people. What's next for Agent Anansi Natural Language Feedback: Add conversational UIs for developers to query the agents' findings via comments or Slack. More Metrics: Expand burnout detection with deeper git analytics and optional developer journaling. Team Dashboards: Build a web-based dashboard showing trends across pipelines, team health, and optimization over time. <div