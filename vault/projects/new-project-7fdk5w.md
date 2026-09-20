---
slug: "new-project-7fdk5w"
url: "https://devpost.com/software/new-project-7fdk5w"
title: "ClineReel - Create promotional videos"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 875
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ClineReel - Create promotional videos

> Imagine being able to create promo videos for your products instantly

[Devpost](https://devpost.com/software/new-project-7fdk5w) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[labor_employment]] [[security_privacy]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** cline, fastapi, kilocode, react, tailwind, vite

## How they structured the write-up

- watch cline skills promo video
- watch kilo-code slack integration promo video
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clinereel — create promotional videos

## Body

Watch cline skills promo video https://youtu.be/lTSUSxcU8eI Watch Kilo-code slack integration promo video https://youtu.be/7QVZEGLtG9A Inspiration Every startup, indie hacker, and developer has faced the same frustrating bottleneck: you build something incredible, but creating a polished promotional video to showcase it takes hours of scripting, editing, and design work — or hundreds of dollars hiring someone. We asked ourselves: what if you could just paste a URL and get a professional promo video back in minutes? The idea of turning Cline from a developer assistant into a fully autonomous, headless code-generation engine — one that writes, compiles, and renders React video components without any human intervention — was too exciting to pass up. What it does ClineReel instantly transforms any website into a polished promotional video. You paste a URL, and our multi-agent AI pipeline takes over: it scrapes the site, analyzes the product's value proposition, writes a creative storyboard, generates AI voiceovers, and then — here's the magic — autonomously writes and renders a full Remotion video in React, scene by scene, from scratch. No templates. No manual editing. Just a URL in, and a ready-to-share MP4 out. How we built it ClineReel is a five-stage pipeline orchestrated by a FastAPI backend with a React + Vite + Tailwind frontend: Scraping — We use Firecrawl to extract titles, descriptions, feature lists, and gallery images from any website. Analyzing — GPT-4o with structured output parsing (via Pydantic models) extracts the hook, core value proposition, and tech stack from the scraped data. Storyboarding — A second GPT-4o agent acts as a creative director, designing a scene-by-scene storyboard complete with visual concepts, animation notes, and voiceover scripts. Audio Generation — ElevenLabs generates per-scene AI voiceovers and we layer in background music tracks. Rendering — This is where the magic happens. We generate a TASK_BRIEF.md from the storyboard, spin up an isolated working directory, and invoke Cline headlessly as a subprocess (cline -y --timeout 900). Cline reads the brief, autonomously creates React/TypeScript scene components, downloads assets, and runs npx remotion render to produce the final MP4. The key architectural insight: Cline is not an interface — it's infrastructure. We treat it as a programmable code-generation component, communicating entirely through file-based contracts (TASK_BRIEF.md), running in auto-approve mode inside isolated sandboxes with symlinked node_modules for efficiency. And finally, we couldn't have done it without Kilo Code CLI . We used Claude Opus 4.5 with Kilo code's CLI to build out the entire project Challenges we ran into Making Cline truly headless — Cline is designed for interactive use. Getting it to run autonomously as a subprocess with reliable output, proper timeouts, and error handling required careful orchestration and a file-based communication pattern. Structured output from LLMs — Ensuring GPT-4o consistently returns valid, schema-compliant JSON for storyboards and analysis required strict Pydantic models and retry logic for context-length edge cases. Isolation between jobs — Each agentic render gets its own working directory (~/.remotion-agentic/work-{job_id}/) to prevent conflicts, but managing symlinked dependencies and cleanup across concurrent jobs was tricky. End-to-end latency — Chaining five AI-powered stages (scraping → analysis → storyboarding → audio → rendering) while keeping the user informed required a real-time polling system with granular stage detail reporting. Accomplishments that we're proud of Cline as a programmable component — We believe this is one of the first projects to treat an AI coding agent not as a chat tool, but as headless infrastructure that can be invoked programmatically to generate and execute production code on demand. Fully autonomous video creation — From a raw URL to a rendered MP4 with custom React components, AI voiceovers, and downloaded product imagery — with zero human intervention in between. Graceful degradation at every stage — No ElevenLabs key? Videos still render without voiceovers. Image download fails? A placeholder is used. Cline times out? The error propagates cleanly to the frontend. The system never crashes silently. What we learned AI agents are most powerful when composed, not isolated. Chaining GPT-4o for reasoning, Firecrawl for data extraction, ElevenLabs for audio, and Cline for code generation created something none of them could do alone. File-based contracts are underrated. Using TASK_BRIEF.md as the interface between our orchestrator and Cline made the system debuggable, human-readable, and reliable. Structured output parsing changes everything. Using OpenAI's structured output mode with Pydantic schemas eliminated an entire class of JSON parsing bugs and prompt injection risks. The "coding agent as infrastructure" paradigm has massive untapped potential. Most people think of Cline and similar tools as interactive assistants — but running them headlessly as subprocess components opens up entirely new categories of automation. What's next for ClineReel — Create promotional videos More video styles — Explainer videos, product demos, comparison ads, and social media shorts (vertical 9:16 format). Live preview — Stream Remotion's render preview to the frontend so users can watch their video being built in real time. Cloud sandboxing — Move Cline execution to cloud-based sandboxes for parallel rendering and better scalability. User editing — Let users tweak the storyboard, swap images, or adjust voiceover scripts before the final render. One-click publishing — Direct export to YouTube, TikTok, X, and LinkedIn with platform-optimized formats and captions. Custom branding — Upload logos, brand colors, and fonts to make every video on-brand from the start. <div