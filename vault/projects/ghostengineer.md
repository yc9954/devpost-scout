---
slug: "ghostengineer"
url: "https://devpost.com/software/ghostengineer"
title: "GhostEngineer"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 537
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/educator_student"
---

# GhostEngineer

> Students don't learn to code by writing perfect code. They learn by breaking things.

[Devpost](https://devpost.com/software/ghostengineer) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[health_clinical]]
**user** [[educator_student]]

**stack** groq, jsonbin, llama-3.3-70b-versatile, react, supabase, supabase-realtime, tailwind-css, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ghostengineer

## Body

Inspiration I kept noticing the same pattern: students can write code but freeze when something breaks. Debugging is the most important skill in engineering — and almost nobody teaches it directly. I wanted to build something that made debugging a first-class skill, not an afterthought. Duolingo made language learning addictive through repetition and feedback loops. GhostEngineer does the same for debugging. What it does GhostEngineer is an AI-powered debugging training platform for STEM students. AI-generated buggy challenges across Arduino, Python, and Circuits at 3 difficulty levels Ghost Mode — adaptive learning that tracks which bug types you keep missing and targets them in future challenges Battle Arena — real-time multiplayer where two students race to diagnose the same broken code first Teacher Dashboard — classroom mode with live analytics: average scores by topic, most missed concepts, and individual weak spot tracking 3-tier hint system , timed challenges, AI mentor personalities, and a global leaderboard How we built it Layer Tech Frontend React + Vite + Tailwind CSS AI Groq API (llama-3.3-70b-versatile) — chosen for its low latency Realtime Supabase (Battle Arena + Teacher Dashboard live updates) Leaderboard JSONBin API Adaptive Logic localStorage + custom weakness-tracking algorithm Deployment Vercel The adaptive learning loop works like this: Student submits a diagnosis Groq evaluates it and returns bugs_found and bugs_missed Missed bugs are categorized (timing, syntax, logic, pin assignment, etc.) Weakness scores update in localStorage Next challenge generation passes top weak categories to Groq, which seeds bugs from those areas Challenges we ran into Consistent AI output — getting Groq to always return structured JSON with clean bug metadata took significant prompt engineering. Malformed responses broke the evaluation pipeline silently. Realtime sync in Battle Arena — handling race conditions when both players submit simultaneously required careful Supabase Realtime channel management. Meaningful adaptive difficulty — early versions just made challenges harder; the real insight was targeting bug type weaknesses, not just difficulty level. Solo time pressure — designing, building, and polishing every feature alone in a hackathon window meant ruthless scoping decisions. Accomplishments that we're proud of The full Ghost Mode adaptive loop works end-to-end — weakness profile genuinely changes future challenge generation Battle Arena with room codes works in real-time with no perceptible lag Teacher Dashboard gives educators something actually useful: not just scores, but which concepts a class is struggling with Shipped a complete, multi-feature product solo in one hackathon What we learned Prompt engineering for structured output is a skill in itself — especially when the downstream app depends on parsing that output reliably Supabase Realtime is remarkably easy to integrate once you understand channel subscriptions Adaptive learning doesn't need a complex ML model — a simple category score system with localStorage is surprisingly effective The best hackathon features are ones that feel magical to demo but have simple implementations underneath What's next for GhostEngineer Expand to more languages — JavaScript, C++, and SQL debugging challenges Classroom challenge assignments — teachers assign specific bug-type challenges to the whole class Spaced repetition scheduling — resurface weak categories at optimal review intervals (like Anki, but for bugs) Voice diagnosis mode — students explain the bug out loud, AI evaluates spoken reasoning School/district dashboard — aggregate analytics across multiple classrooms <div