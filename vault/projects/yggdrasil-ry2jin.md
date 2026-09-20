---
slug: "yggdrasil-ry2jin"
url: "https://devpost.com/software/yggdrasil-ry2jin"
title: "YGGDRASIL"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 855
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# YGGDRASIL

> "Grow your knowledge, branch by branch." Short, on-brand, and matches your landing page tagline.

[Devpost](https://devpost.com/software/yggdrasil-ry2jin) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
**substrate** [[geospatial]] [[structured_db]]

**stack** ai, api, css, deepseek-v3, express.js, featherless, javascript, node.js, react, render, rest, supabase, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for yggdrasil

## Body

Inspiration School has always been weird for me. Sitting through lessons that moved too fast or too slow, cramming for tests, forgetting everything a week later, learning felt like something happening to me rather than something I was building or actively participating in. I kept wondering what it would take to actually retain knowledge, to feel like progress was real and visible instead of just a grade on a paper. Around the same time, I noticed how various apps like fitness, meditation, even language learning apps had cracked something education hadn't, streaks, visual progress, the small dopamine hit of seeing a chain of consistency. Why didn't learning feel like that? Yggdrasil is my attempt to fix the experience I struggled with — turning learning into something you can see grow, branch by branch, and something that gently calls you back when you drift away from it. What it does You plant a "seed", any topic you want to learn. An AI generates a structured curriculum, branching into topics and sub-topics, each represented as a node on a growing tree. Complete a lesson and pass its check to unlock the next node and watch a new leaf bloom. Stop learning for too long, and your tree starts to wilt, a visual, emotional nudge to come back and keep growing. Your dashboard shows your whole "forest", every topic you're learning, its progress, and its health at a glance. Your profile tracks streaks, total nodes mastered, and your learning history over time. How I built it Frontend: React + Vite + Tailwind CSS, with an animated SVG tree that visually represents curriculum progress — each leaf maps to a node, color and glow reflecting mastery status. Backend: Node.js + Express handles curriculum generation, lesson delivery, progress tracking, and decay calculations. Database & Auth: Supabase for user accounts, tree/node data, and progress persistence. AI: featherless.ai running DeepSeek-V3 generates the branching curriculum structure and lesson content dynamically based on the topic and difficulty level chosen at onboarding. Deployment: Frontend on Vercel, backend on Render, connected via environment-based config. Challenges I ran into The decay/wilting mechanic was the hardest part to get right, both technically and from a UX standpoint. Technically, it required tracking per-node and per-tree "last active" timestamps and running decay calculations that update a tree's visual state (Growing → Wilting → Dormant) without constant server polling. From a design standpoint, the challenge was making decay feel motivating rather than punishing, wilting needed to nudge users back without feeling like a setback, the same way my own struggles in school felt like setbacks rather than nudges toward better habits. Getting the AI to reliably generate well-structured, branching curricula, rather than flat lists also took a lot of prompt iteration, since the entire tree visualization depends on that structure being consistent and predictable. Accomplishments that I'm proud of Going from a single idea — "what if learning felt like growing a tree" — to a fully working, deployed product with real AI-generated curricula, persistent accounts, and a visual system that actually reflects your progress and habits. The tree itself, with leaves that bloom as you master content and wilt as you neglect it, ended up feeling exactly like the emotional hook I imagined at the start. I'm also proud of taking the design seriously iterating on the landing page, navbar, dashboard, and tree view until the whole experience felt cohesive and intentional rather than like a typical hackathon prototype. What I learned I learned a lot about structuring AI-generated content so it's both flexible (works for any topic) and predictable enough to drive a UI reliably, getting the curriculum generation to consistently output something a tree visualization could map onto took real iteration. I also learned how much design and "feel" matter even for a hackathon project, small details like typography, spacing, and color completely change whether something feels like a toy or a real product. And I got hands-on experience with the full deployment pipeline — connecting a Vite frontend on Vercel to an Express backend on Render, environment variables, CORS, and the small things that go wrong along the way. What's next for Yggdrasil Spaced repetition reviews — instead of just marking a node "complete," periodically resurface mastered nodes as quick reviews to reinforce retention and slow decay naturally Richer node content — quizzes, flashcards, and interactive checks beyond reading, so "mastery" reflects deeper understanding More interactive trees — clicking, zooming, and exploring individual leaves and branches, with animations for growth, blooming, and wilting that make the tree feel like a living thing rather than a static progress bar Full gamification — XP, levels, achievements, seasonal "growing challenges," and maybe even rare leaf/tree variants for long streaks — turning the forest into something genuinely fun to maintain, not just a tracker Social forests — see friends' trees, compare progress, and gift seeds to each other Smarter decay — tune decay rates based on topic difficulty and a user's historical learning pace, rather than a flat timeline Mobile app — the responsive web experience is a start, but a native app would make daily check-ins even more frictionless <div