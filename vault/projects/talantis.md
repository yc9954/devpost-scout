---
slug: "talantis"
url: "https://devpost.com/software/talantis"
title: "Talantis"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 829
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Talantis

> Talantis maps internship pipelines for companies and students, showing where talent flows between schools and industry. Explore trends and uncover hidden opportunities with Talantis' Atlas model.

[Devpost](https://devpost.com/software/talantis) · hackathon [[LA Hacks 2026]]

## Facets

**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: sensor_telemetry</sub>

**stack** agentverse, claude, fastapi, figmamake, javascript, next.js, python, react, render, supabase, tailwindcss, uagents, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- asi:one challenge
- figma make challenge
- cognition challenge
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for talantis

## Body

Talantis home page Talantis explore page Talantis submit page Talantis Atlas on Agentverse Using Figma Make to experiment with the hero section designs. Using Figma Make to draft the metrics and analytics. Using Figma Make to prototype a submission form. Talantis A legendary island of talents. Every company is looking in the same places. We show you the ones no one has mapped yet. Inspiration Every summer, thousands of students land internships — but their journeys are scattered across LinkedIn posts, group chats, and isolated networks. We saw that the patterns already exist : which schools feed which companies, which pipelines are growing, and which talent pools remain hidden. Talantis was built to make those invisible pathways visible . What it does Talantis is a talent intelligence platform for companies and students that maps internship pipelines between universities and companies through an interactive interface. It features Atlas , an AI guide that answers natural-language questions, compares hiring patterns, and uncovers overlooked talent pools using real data. How we built it Frontend: Next.js + Tailwind CSS Backend: FastAPI on Vercel serverless functions Database: Supabase (Postgres) with custom RPCs AI: Claude Sonnet 4.5 via Anthropic API, in a multi-turn agentic tool-use loop Agent layer: Fetch.ai uAgents + Chat Protocol, hosted on Render Distribution: Registered on Agentverse, discoverable through ASI:One Atlas operates over six tools , three for each audience: Recruiter-side — companies asking about pipelines: filter_internships — direct factual queries compare_companies — head-to-head pipeline comparisons find_similar_schools ★ — pipeline gap analysis (hidden coastlines) Student-side — students asking about realistic options: find_target_companies — companies tiered by realism analyze_school_at_company — your school's track record at a specific company discover_career_paths ★ — paths students like you take (hidden pathways) Atlas runs a multi-turn reasoning loop, automatically detects audience from language, and synthesizes results from one or more tools into a single grounded answer. ASI:One Challenge Talantis Atlas — Agentverse Profile: https://agentverse.ai/agents/details/agent1qw9srfevfplt27z6du7xns4venmtafdezxnujl3ksamz03qwud9yurhc0hv/profil Talantis Atlas — ASI:One Shared Chat Session: https://asi1.ai/shared-chat/cd572643-48d0-4020-a7ee-679eb37f9e2 Atlas is a single-agent six-tool orchestration that detects audience from language and serves both recruiters and students with the same data from opposite vantages. Active, ASI Available, and reachable from anywhere on the agent web. Figma Make Challenge We used Figma Make to offload much of our frontend / UI design process, letting us iterate quickly without getting bottlenecked on design decisions. Instead of manually designing every component, we leveraged it to: Rapidly prototype layouts Experiment with UI elements and visual density Explore atmospheric, visually complete interfaces Test multiple design directions early — layout structure, component hierarchy, brand cohesion By streamlining design iteration, we intentionally shifted our focus toward higher-impact work: building the backend (FastAPI + Supabase), implementing Atlas's AI tool-calling system with the Claude API , and deploying / registering the agent on Fetch.ai Agentverse . Cognition Challenge The toil being eliminated is talent research — a genuinely painful, repetitive knowledge-work workflow that hits three groups: Students spend hours on LinkedIn manually figuring out which companies recruit from their school Career advisors field the same placement questions over and over, digging through outdated spreadsheets Recruiters try to understand which schools feed into specific roles — currently done by hand or via expensive data subscriptions Talantis automates this end-to-end. Instead of two hours of manual research, you ask Atlas one question and get a grounded, data-backed answer in seconds. And because Atlas is a registered agent, it plugs into whatever workflow the person already uses — no new app to learn. Why this is competitive for Cognition: the toil isn't just "searching." It's the entire loop — find the data source → verify it's current → cross-reference across universities → synthesize into an answer → repeat for the next question. Atlas collapses that whole loop into a single agent interaction. Challenges we ran into Turning scattered, real-world placement data into a clean, queryable dataset Designing intuitive ways to explore complex pipeline relationships Building reliable multi-turn AI interactions with consistent context Ensuring outputs were both accurate and actionable Audience detection — same data, two perspectives, one Atlas Accomplishments that we're proud of Made hidden internship pipelines visible and explorable Built Atlas, an AI system that dynamically selects tools and reasons across multiple steps Modeled real internship flows across 54 companies × 31 universities (1,334 records) Registered Atlas on Agentverse with the Chat Protocol, discoverable from ASI:One Delivered a product with clear value for recruiters, students, and institutions What we learned How to build AI systems that reason over structured data without hallucinating numbers The importance of clean data modeling for meaningful insights How to balance UX, data, and AI in one product How to design and ingest a brand voice into an LLM system prompt Rapid prototyping under hackathon constraints What's next for Talantis Expand dataset coverage across more years, companies, and universities Add deeper analytics: trend tracking, role-specific insights, geographic breakdowns Improve visualizations and filtering Enhance Atlas with richer reasoning and personalization Further integrate into the agentic web ecosystem Talantis · LA Hacks 2026 <div