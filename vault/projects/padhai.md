---
slug: "padhai"
url: "https://devpost.com/software/padhai"
title: "PadhAI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 337
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# PadhAI

> PadhAI: From prompt to narrated and animated lectures, instantly.

[Devpost](https://devpost.com/software/padhai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** chatgpt, groq, javascript, manim, openai, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for padhai

## Body

Inspiration “PadhAI” (padhai = “study” in Hindi) was born from a simple idea: turn any topic into a clear, animated mini‑lecture—instantly. Teachers and learners spend too much time storyboarding, animating, and narrating; we wanted studio‑quality explanations without production overhead. What it does Converts a prompt into a time‑aligned lecture video: Manim animations + synchronized narration. Uses a shot‑based timeline (scenes → shots with start times) to guarantee narration/visual sync. User friendly UI with chat history, instant replays, and browser TTS. How we built it Frontend: React + Vite (VideoPlayer, ChatPanel, Sidebar), Web Speech API for TTS scheduling by shot start times. Backend: Node.js + Express; calls an OSS LLM via Groq; assembles Manim code; executes Manim; serves generated MP4s. Prompting: “Maestro” system prompt returns JSON with manim_header, scenes[shots], and manim_footer. Reliability: Code sanitization (quote fixes), camera‑animation shims for Manim version differences, Windows‑safe cleanup. Challenges we ran into Manim compatibility: camera.animate not available on some builds; added safe fallbacks and timing preservation. JSON → Python hygiene: over‑escaped quotes breaking strings; added robust unescaping and indentation normalization. Windows file locks (EBUSY) during cleanup of partial media; added resilient deletion and retries. Timeline trust: ensuring animation durations meet narration length; enforced waits/padding. Accomplishments that we’re proud of Shot‑based timeline that makes narration and visuals deterministically sync. Clean, accessible UX that feels familiar and fast. Fully local render pipeline (Manim + browser TTS) using free tiers. Defensive backend: sanitization, fallbacks, and portability fixes. What we learned LLM‑to‑code is powerful but fragile—small escaping/indent errors can break renders. Cross‑version portability in Manim requires careful camera handling. Windows dev ergonomics (file locking, CRLF) need explicit handling. Clear contracts (timeline schema) make complex AI outputs reliably usable. What’s next for PadhAI -Fine tune OpenAI GPT OSS with manim codes and synchronized narrations Real TTS streaming and audio–video mux (ffmpeg) for shareable, packaged lectures. Template library for common pedagogy patterns (graphs, processes, proofs). Sandbox execution (Docker/containers) and security hardening. Persistence (saved prompts, edits, versions) and collaboration. CI for lint/tests and a one‑click cloud deploy path. <div