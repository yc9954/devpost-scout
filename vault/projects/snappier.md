---
slug: "snappier"
url: "https://devpost.com/software/snappier"
title: "Snappier"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 771
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Snappier

> Show Snappier your workflow once by recording your screen. AI figures out what you did and why, then automates it across any connected app. That's it.

[Devpost](https://devpost.com/software/snappier) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[government_staff]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** ai, anthropic-claude-(workflow-planning-&-execution), api, chrome, clerk, cloudflare, composio, extensions, framer-motion-ai/llm:-google-gemini-(video-understanding), gemini, openai-whisper-(transcription), r2, react-19, react-flow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snappier

## Body

Homepage Recording Connect Tools Transcription Timestamps Inspiration Most people can't automate their work because automation tools require programming skills. You need to understand APIs, data mapping, and conditional logic. Meanwhile, those same people teach their coworkers how to do things all the time by just showing them. We wanted to make automation work the way humans naturally teach: by demonstration, not configuration. What it does Snappier turns screen recordings into automated workflows in 3 steps: Record — Perform your workflow once in the browser. Our Chrome extension captures everything (e.g., scrape LinkedIn → add to Google Sheets → send Slack message) Generate — AI watches the video and builds the automation. Gemini extracts what you did, Claude figures out the API calls, and we map it to 100+ SaaS tools via Composio Run — One click executes the entire workflow across your connected apps. Run it again anytime, or schedule it automatically No drag-and-drop builders. No field mapping. Just show us once and we automate it forever. How we built it Frontend: Next.js 15 + React 19 + TypeScript + Tailwind CSS + React Flow (interactive workflow graphs) AI Pipeline: Google Gemini (gemini-3-pro-preview) for multimodal video understanding. Analyzes recordings frame-by-frame to extract structured steps with intent, confidence scores, and timestamps Claude Haiku for fast intent summarization and noise filtering to remove accidental clicks Claude Sonnet for workflow execution reasoning with tool-use calling OpenAI Whisper for audio transcription for narrated workflows Vercel AI SDK as unified interface for all LLMs with structured output (Zod schemas) Integrations: Composio provides 100+ pre-built SaaS tool integrations with OAuth and tool-calling APIs Cloudflare R2 for scalable video storage Clerk for user authentication Chrome Extension: Manifest V3 extension that captures screen video (WebM) + granular DOM events (clicks, keyboard, navigation) Architecture: Multi-modal step extraction (AI vision + DOM events + audio) → Intent summarization → Tool detection via URL pattern matching → Workflow generation → Composio execution with full audit logs Challenges we ran into Video understanding reliability – Getting Gemini to consistently extract structured steps from noisy screen recordings took extensive prompt engineering and low-temperature sampling (0.2) Intent vs. action gap – Users click buttons in the browser, but workflows need to call APIs . Bridging "clicked the blue button" to "send_email via Gmail API" required semantic reasoning with Claude Noise filtering – We didn't realize how many accidental clicks, scrolls, and micro-adjustments users make. Our AI had to learn to ignore 80% of recorded actions OAuth at scale – Managing connections across 100+ SaaS tools (each with different auth flows) was only feasible thanks to Composio's abstraction layer Real-time workflow editing – Keeping the React Flow graph, step list, and video player synchronized while the user edits was a complex state management challenge Accomplishments that we're proud of Multi-modal AI fusion – We combined video, DOM events, and audio into a single coherent understanding. Each modality validates the others (if Gemini sees a click AND the DOM recorded a click, high confidence) End-to-end working demo – From recording to execution, the full pipeline works. You can actually record a workflow and run it against real SaaS APIs Intent-aware automation – We don't just replay mechanical actions. Snappier understands what you were trying to accomplish and finds the best API-level way to do it Control flow detection – Our AI detects loops ("for each row in this spreadsheet...") and conditionals, not just linear sequences Production-ready architecture – Cloudflare R2 storage, Clerk auth, comprehensive test suite (Vitest), type-safe throughout What we learned Multimodal > unimodal – Video analysis alone misses context. DOM events alone can't infer intent. Audio alone is ambiguous. Together, they're powerful. Low-temperature LLMs are essential – For structured extraction, we needed temperature=0.2 or lower. Creativity kills reliability here. Tool abstractions unlock scale – Building 100+ integrations from scratch would've been impossible. Composio's tool-calling abstraction made it feasible. Users are noisy – Humans don't realize how many random clicks, back-buttons, and scrolls they do. Filtering signal from noise is 80% of the challenge. Video-first is fundamentally different – Teaching by demonstration feels more natural than form-based builders. It's how we teach humans; why not computers? What's next for Snappier Runtime control flow – Execute loops and conditionals, not just detect them Scheduled workflows – Cron-style automation (run every morning, every week, etc.) Team collaboration – Share workflow libraries across organizations Workflow marketplace – Discover and remix workflows from the community Mobile recording – iOS/Android screen recording support Advanced parameter inference – Better extraction of dynamic values (names, emails, dates) from recordings Multi-step editing – Visual graph editor to rearrange, add, or remove steps post-recording <div