---
slug: "githired"
url: "https://devpost.com/software/githired"
title: "Githired"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 320
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
---

# Githired

> Git-Hired uses AI to analyze real GitHub activity — projects, commits, and code quality — to show startups who’s genuinely skilled. We replace résumés and traditional coding tests with proof of work.

[Devpost](https://devpost.com/software/githired) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** brightdata, chromadb, claude, letta, nextjs, python, react, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for githired

## Body

Inspiration Most startups don’t care how well you solve a random algorithm problem — they care how quickly and effectively you can ship real code. But today’s hiring tools still test engineers in ways that say nothing about how they actually build. That’s why we built Git-Hired — the future of hiring developers. What it does You create a smart application form and share it anywhere — LinkedIn, Handshake, your own site. Our AI turns every application into a live portfolio that analyzes real commits, filters out filler pushes, and ranks candidates based on true technical ability. If you like what you see, send them a coding assessment that mimics how developers really work — with AI as a co-pilot. Yes, we allow the use of AI during our assessments, because let's be real- nobody actually writes each and every line of code manually anymore! How we built it Frontend: Next.js, React, TypeScript, Node.js Backend: Python, FastAPI, Bright Data, GitHub REST API, ChromaDB, Elastic Search for semantic embeddings AI + Analytics: Custom GitHub analyzer, NLP-based code parsing, contribution heatmaps, AI Coding assistant in Letta Cloud with memory Challenges we ran into Parsing GitHub data reliably across different repo structures Avoiding false positives when evaluating commit quality Building an AI assistant that helps — without handing out answers Integrating multiple APIs and ensuring real-time updates Accomplishments that we're proud of Fully functional end-to-end AI hiring workflow GitHub data --> live portfolio generation Smart rankings that surface best-fit developers AI-assisted coding assessments integrated directly into the platform What we learned The best developers don’t always have the best resumes AI can be a powerful equalizer when used ethically Real-world hiring problems need more empathy and context than just code What's next for Githired Expand analysis beyond GitHub (LeetCode, Stack Overflow, etc.) Add recruiter dashboards with performance insights Build candidate feedback + improvement analytics Launch beta with partner startups and university recruiters <div