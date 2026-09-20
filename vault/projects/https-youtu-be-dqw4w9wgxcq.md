---
slug: "https-youtu-be-dqw4w9wgxcq"
url: "https://devpost.com/software/https-youtu-be-dqw4w9wgxcq"
title: "Relay"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 434
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Relay

> Postman AI Agent Automation that transforms vague and slow product requirements into detailed pull requests in 30 seconds

[Devpost](https://devpost.com/software/https-youtu-be-dqw4w9wgxcq) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[legal_professional]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** digitalocean, fastapi, node.js, postman, postman-ai-agent, postman-flows, python, ripgrep, slack-api, snowflake, snowflake-cortex

## How they structured the write-up

- inspiration
- 🏆 accomplishments that we’re proud of
- 💡 what we learned

## Body

Inspiration Our project solves a real problem that we, SWE interns to PMs face: vague product requirements and incompatible interpretations. Engineers have to decode and figure out: Clarifying requirements back and forth Searching which files to change Writing acceptance criteria Creating boring boilerplate PRs What it does This is how our Agent System works: PM in Slack: "Fix React version issue" Postman AI Agent processes the request Ripgrep finds relevant code files (Settings.tsx, theme.ts) snowflake cortex ai generates PR code (≤30 lines) GitHub PR created automatically Slack notifies team with reasoning trace Dashboard shows history and the current usage of current pr's and of snowflake in general Result: PR + acceptance criteria + impacted files in 30 seconds. Tech Stack | Core Orchestration -Postman AI Agent + Flows | Code Search | Ripgrep API (Node.js/Express) | PR Generation | MIstral Large | PR Creation | GitHub REST API | Notifications | Slack Webhooks + Block Kit | Dashboard | Next.js 16 + Express backend Perfect — here’s your Devpost-ready version (slightly reduced for length, but still polished, professional, and readable for judges). You can paste this directly into the “Accomplishments / Learnings / What’s next” sections of your Devpost submission. 🏆 Accomplishments that we’re proud of Autonomous AI Orchestration: The Postman AI Agent plans and executes the full workflow end-to-end, choosing and invoking Ripgrep, Claude, GitHub, and Slack automatically. Deep Postman Ecosystem Use: Integrated 12+ Postman tools AI Agent Block, Flow Modules, Actions, HTTP blocks, Mock Servers, Monitors, and Analytics. Multi-API Coordination: Combined 4 external APIs with proper error handling, retries, and dynamic branching. Smart Conflict Detection: Scans open PRs, compares overlapping files, and assigns a merge-risk score (0–100%). Transparent Reasoning: Every AI decision, tool call, and prompt is logged in Postman Analytics — complete traceability. Live Slack Integration: /impact → PR created → team notified — all in real time. Next.js Dashboard: Displays PR history, conflict hotspots, and risk metrics in a clean, production-ready UI. 30-Second E2E: From Slack command to GitHub PR creation in under 30 seconds. 💡 What we learned AI Agent > Decision Blocks: One AI block replaced 50+ manual logic branches. Prompt Engineering is everything: Multiple iterations made Claude’s PR output concise and reliable. Conflict detection is nuanced: Fuzzy path matching and risk scoring were key. Slack UX matters: Block Kit formatting made AI notifications actionable. Reusable Flow Modules: Each tool (Ripgrep, GitHub, Claude, Slack) can plug into future projects. API resilience: Handling rate limits, retries, and errors across four APIs took careful planning. Local testing hurts: ngrok’s constant URL changes reinforced the need for true cloud deployment. <div