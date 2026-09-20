---
slug: "explainanything"
url: "https://devpost.com/software/explainanything"
title: "ExplainAnything"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 604
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# ExplainAnything

> AI-powered learning platform that explains any topic at 3 levels, generates quizzes, flashcards, study plans, creative content, and lets you challenge friends — powered by DeepSeek v4 Pro.

[Devpost](https://devpost.com/software/explainanything) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** deepseek-ai-deepseek-v4-pro, esbuild, express.js, firebase, firestore, framer-motion, node.js, nvidia-nim, openai-sdk, pino, pnpm, react, shadcn-ui, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next

## Body

Inspiration Most learning tools give you a wall of text and call it an explanation. We wanted something that felt like that one brilliant friend who could explain anything — the friend who uses specific analogies, reveals the surprising history, and actually makes you say "oh THAT'S why it works like that." We also noticed that passive reading doesn't build retention. So we asked: what if every topic came with a full learning experience — quizzes, flashcards, creative formats, spaced repetition, and social challenges — all generated on the fly? What it does Enter any topic — from "Binary Search" to "Photosynthesis" to "Keynesian Economics" — and ExplainAnything builds an entire learning experience around it: 3-level explanations (Beginner → Advanced) with analogies, misconceptions, what-if scenarios, history, and a difficulty meter AI-graded quizzes — 4 progressive MCQs + 1 open-ended conceptual question, with specific AI feedback on your written answer Flashcards — 10 Anki-style cards per topic with spaced repetition tracking Creative modes — learn via AI-generated Story, Rap, Podcast transcript, Debate, Mnemonic, Timeline, ELI5, or Haiku Study plans & learning paths — day-by-day schedules and full curriculum generators for any goal Shareable challenges — create a quiz, share a link, see a head-to-head result Gamification — XP, levels, streaks, streak shields, mastery badges, leaderboard Productivity tools — Pomodoro timer, ambient sounds, command palette (⌘K), keyboard shortcuts, bookmarks How we built it Frontend : React + Vite + Tailwind CSS v4 + TanStack Query + 55 shadcn/ui components. Client-side gamification (XP, SRS, streaks) lives entirely in localStorage and communicates via custom DOM events — no global state library. Backend : Node.js + Express (TypeScript) deployed as Vercel Serverless Functions. Zod validates every request body. Pino handles structured logging. AI : DeepSeek v4 Pro via NVIDIA NIM's OpenAI-compatible endpoint — we use the standard OpenAI SDK pointed at https://integrate.api.nvidia.com/v1 . Every single AI call returns structured JSON, enforced via response_format: { type: "json_object" } . The prompts explicitly ban phrases like "In computer science..." and mandate specific, surprising analogies with characters and stakes. Database : Firebase Firestore for conversations, learning sessions, weak concept aggregation, leaderboard entries, and shareable challenges (7-day TTL, 10-char hex IDs). Architecture : pnpm monorepo with 6 shared workspace packages — the AI client, DB layer, Zod schemas, and React hooks are all separate packages that both the frontend and backend consume. Challenges we faced Dotenv loading order : In an ESM monorepo bundled with esbuild, dotenv.config() runs after top-level module code in workspace packages, which caused Firebase to throw before credentials were loaded. The fix was a dedicated env.ts module imported first to guarantee load order. Prompt reliability : Getting DeepSeek to return valid JSON consistently at temperature: 1.0 required adding explicit Markdown fence stripping, fallback parse error handlers, and disabling chain-of-thought via chat_template_kwargs: { thinking: false } . New Firestore database : On a fresh database, orderBy queries with no documents return NOT_FOUND (gRPC code 5) instead of an empty snapshot. We added graceful catches that return [] until the first document is created. What we learned Deep prompt engineering is a real engineering discipline — banning specific bad patterns by name, specifying character counts, mandating story structure, and defining output contracts produces dramatically better AI output than generic prompts. We also learned that NVIDIA NIM's OpenAI-compatible layer lets you swap frontier models (DeepSeek, LLaMA, Mistral) with zero SDK changes. What's next Authentication — currently single-user; add Firebase Auth for multi-user profiles and persistent cloud XP Vercel deployment — already configured, ready to go live Voice mode — text-to-speech for explanations and listen-while-commuting Collaborative study rooms — real-time multiplayer challenges <div