---
slug: "artifical-guruji"
url: "https://devpost.com/software/artifical-guruji"
title: "Artifical Guruji"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 335
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Artifical Guruji

> Clarity, Discipline, Insight — On Demand

[Devpost](https://devpost.com/software/artifical-guruji) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** inngest, neondb, next.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- deployed link : https://guruji-chi.vercel.app/
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for artificial guruji
- team members
- ai tools used

## Body

Landing page Roadmap Dashboard Inspiration Most students waste time searching through half-baked explanations, YouTube videos, or AI answers that sound confident but teach nothing. The goal was simple: build an AI teacher that gives real understanding, not generic summaries. Something that behaves like a strict but reliable mentor — fast, clear, and accurate. What it does Artificial Guruji turns any question into a clear, structured explanation. It breaks down concepts, shows examples, highlights mistakes you might make, and adapts the depth based on your level. Whether it's code, math, theory, or exam prep, it gives answers that actually teach instead of hallucinating. How we built it We combined an LLM pipeline with a custom explanation framework — concept breakdown, stepwise reasoning, analogies, and misconception detection. Stack: Frontend: Next.js Backend: Next.js AI Layer: LLM with custom prompting + retrieval for accurate domain knowledge Deployment: GCP (Cloud Run + database) The goal was clarity-first responses, not generic AI chat. Deployed link : https://guruji-chi.vercel.app/ Challenges we ran into Getting the AI to explain instead of ramble Eliminating hallucinations without killing speed Designing prompts that adapt explanations based on user level Building a fast UI while juggling streaming and context management Balancing feature creep vs. actual learning impact Accomplishments that we're proud of Built an AI tutor that actually teaches instead of dumping text Made explanations consistent across topics Reduced hallucinations through a structured reasoning flow Achieved fast responses even with domain retrieval Delivered a clean, minimal UX What we learned Bigger model doesn’t guarantee better teaching Explanation quality depends on structure, not just model power Users value clarity and speed over fancy features Retrieval drastically boosts trust when done right What's next for Artificial Guruji Personalized learning paths based on user mistakes Code execution and math-step verification Concept graph for recommended next topics Subject-specific modes (DSA mode, ML mode, Math mode) Mobile app with offline saved explanations Team Members Mohit Goyal Angel Gupta AI Tools Used Cursor - IDE for fixing ui and functionality of few features <div