---
slug: "janus-5dfi9a"
url: "https://devpost.com/software/janus-5dfi9a"
title: "Janus"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 797
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Janus

> An autonomous GitHub maintainer that runs your whole backlog — triages, reviews, and ships — and asks you exactly one question a day.

[Devpost](https://devpost.com/software/janus-5dfi9a) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
**domain** [[health_clinical]] [[media_journalism]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** alibaba-cloud, alibaba-oss, asyncio, asyncpg, caddy, dashscope, docker, ecs, fastapi, github-api, github-apps, httpx, jwt, openai

## How they structured the write-up

- inspiration
- what it does
- the trust model (the actual idea)
- how i built it
- challenges i ran into (the honest section)
- what i learned
- what actually happened

## Body

Inspiration Maintaining an open-source project is a background job that never clocks out. My project FlaskBlog sits at 190+ stars with real users — and the issue backlog grows faster than I can clear it while working full-time and studying. One manual cleanup pass cleared 15 stale issues and shipped v3.0.0… and it started filling right back up. The cleanup isn't the hard part. The never stops part is. Existing bots are either fully autonomous (terrifying) or ask permission for everything (pointless). A bot that asks 100 questions a day is not an autopilot — it's a chore generator with extra steps. So I built the one I actually wanted. What it does Janus is a GitHub App that runs the entire maintenance lifecycle by itself: triages and labels issues, closes junk with a reasoned comment, nudges vague reports, reviews community PRs, plans fixes, and reads screenshots with vision — and pings my phone only for the one action that's genuinely hard to undo. The design KPI is literally questions per day , target ~1. The trust model (the actual idea) Escalation is gated on reversibility, never on the model's self-confidence. LLMs are badly calibrated; I never ask "how sure are you?" Instead every capability has an autonomy level based on how cheap it is to undo. Label an issue → auto . Close spam with a reopen note → auto . Open a PR → auto (the PR is the review surface). Merge to main → ask . Close a human's PR → ask (social blast radius). Demotion, never promotion. On any uncertainty or failed check, the action drops exactly one level. The model can never argue its way up to more autonomy. The merge gate has no LLM in it. Auto-merge is decided by deterministic checks — path allowlists, size caps, protected paths, CI green, and a change class computed mechanically from file paths. The model may propose a class; the gate derives its own and ignores it. How I built it Backend: Python + FastAPI webhook receiver → event queue → orchestrator, on Alibaba Cloud ECS , with PostgreSQL for the audit + approvals store and Caddy for TLS. Models via Qwen Cloud (OpenAI-compatible endpoint), routed by task tier: qwen3.6-plus for triage/review, qwen3.7-max (thinking) for planning, qwen3-coder-plus for codegen, qwen3-vl-plus for reading screenshot bug reports. Audit trail in Alibaba OSS: every action archived as a dated JSON object; Telegram approval cards link to presigned OSS URLs so I can inspect full context from my phone. Codegen runs in a hardened Docker sandbox (all caps dropped, memory-capped, destroyed after each job). Challenges I ran into (the honest section) The sandbox strangled itself. apt-get install git needs setgroups , a capability I'd just dropped for security. My own guardrail killed my own setup — fixed by using a base image that already ships git. A "success" that wasn't. The push step chained commit && push in one shell string and read the wrong exit code, so it opened a PR against a branch that was never pushed (422). Lesson: a success signal must reflect real state. The bot almost signed as a stranger. Commits authored to a bare no-reply email can collide with a real person's identity; fixed to the App's provably un-claimable bot identity. A codegen call with no ceiling. Issues got a perfect plan comment and then… no PR, silently. A single qwen3-coder-plus call for a trivial change returned 63K tokens — then 427K on retry — because thinking-mode ran with no max_tokens cap, blowing the per-event budget after the tokens were spent, so codegen aborted quietly. Two lessons: a per-event budget isn't a safety limit if one call can exceed it in a single shot (you need a per-call ceiling too), and silent is the worst failure mode an autonomous system can have. The LLM hiding in a "deterministic" gate. My v1 merge gate assigned the change class with the model — a probabilistic input smuggled into a "deterministic" check. Fixed to pure path-matching. That one function is the project's core claim. What I learned Smart models are what make autonomous defaults safe — you cap spend with token budgets, not by downgrading the brain. And the interesting engineering problem in agents isn't the model; it's deciding where the human goes . What actually happened A real external contributor found Janus's implementation plans on two issues and opened PRs implementing them. Janus autonomously reviewed and approved both (the contributor's own comment: "Janus has approved it" ); I merged after a glance. And the one thing that reached my phone all week was a single card: close a human's PR? → ask. Questions that day: one. Exactly the KPI. Built solo in one week for the Qwen Cloud Global AI Hackathon, Track 4. <div