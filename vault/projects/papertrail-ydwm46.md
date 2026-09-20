---
slug: "papertrail-ydwm46"
url: "https://devpost.com/software/papertrail-ydwm46"
title: "PaperTrail"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 310
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "user/researcher"
---

# PaperTrail

> PaperTrail is an AI research assistant that uses deep memory architectures to learn and adapt to your interests, reading style, and goals to curate personalized academic paper recommendations.

[Devpost](https://devpost.com/software/papertrail-ydwm46) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[labor_employment]]
**user** [[researcher]]

**stack** claude, css, jina, letta, next.js, postgresql, react, shadcn, sonnet4.5, supabase, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- accomplishments
- what i learned
- what's next for papertrail

## Body

Inspiration As a researcher, I find literature review tedious and impersonal. Generic search yields piles of irrelevant results. What if an AI agent learns how you learn, captures your interests and dislikes, reads papers in parallel, and surfaces what matters? I built PaperTrail to bring deep personalization to research discovery. What it does PaperTrail uses multi-agent orchestration with persistent memory. Describe a research topic and it: Searches the papers Scores paper relevance against your interests, goals, expertise, and feedback Returns relevant, personalized recommendations Learns from feedback to refine future suggestions and become more personal Reads specific papers on demand and answers questions in real time Sleeptime compute generates insights over previous conversations, further personalizing the agent. All personalized through a memory layer that adapts to your workflow. How I built it Multi-agent orchestration (Letta): supervisor agent generates targeted queries; workers fetch papers via Jina AI and evaluate in parallel. Deep memory architecture (Letta): profiles store interests, dislikes, goals, expertise, explanation style; conversation history; and feedback tables linking votes to preferences. Personalized scoring: workers use memory blocks to align recommendations to your profile. Real-time learning: each vote updates the user model, shaping future recommendations. Challenges Latency: parallel worker evaluations enabled fast, accurate recommendations. Personalization: memory blocks encoding interests, dislikes, expertise, and style lifted precision. Threading fine-grained preferences into agent prompts reliably. Accomplishments Deep personalization with feedback loops. Smooth real-time paper reading and Q&A. Clear UX that hides multi-agent complexity. Results improve with usage. What I learned Modern LLM orchestration frameworks are powerful. Memory matters: persistent user context beats session-only approaches for quality. Multi-agent systems call for careful supervisor–worker coordination and state handling. What's next for PaperTrail Broader coverage: expand beyond arXiv (Google Scholar, semantic scholar). Fine-tuning with user feedback data. Collaboration features to share recommendations. Read-paper sessions with collaborative learning and notes. Big picture: personalized research that learns with you. <div