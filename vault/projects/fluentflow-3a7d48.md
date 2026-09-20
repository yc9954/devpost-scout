---
slug: "fluentflow-3a7d48"
url: "https://devpost.com/software/fluentflow-3a7d48"
title: "FluentFlow"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 619
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "user/legal_professional"
---

# FluentFlow

> Speak about real situations, not flashcards. Voice & text AI role-play in 7 languages with live corrections & session scores; same FluentFlow on MeDo (web) and Expo (mobile).

[Devpost](https://devpost.com/software/fluentflow-3a7d48) · hackathon [[Build with MeDo Hackathon]]

## Facets

  <sub>weak: education, scientific_research</sub>
**user** [[educator_student]] [[legal_professional]]

**stack** css, eas, elevenlabs, expo.io, google-cloud, google-gemini, javascript, medo, nativewind, navigation, reanimated, sql, supabase, tailwind

## Body

Inspiration Most people don’t fail languages because they can’t memorize words; they fail because they rarely get low-stakes spoken practice that feels like real life. Textbook apps drill vocabulary; they rarely recreate the back‑and‑forth pressure of ordering food, clearing airport confusion, or running a job interview in another language. We wanted FluentFlow: a place to rehearse whole conversations with voice, stay in specific scenarios, and still get structured feedback so every session feels like measurable progress. What it does FluentFlow is an AI-powered conversation practice across seven languages (e.g., English, Spanish, French, German, Japanese, Arabic, Hindi). Learners: Pick a scenario (ordering food, travel, interviews, and more). Practice by typing or speaking; the AI stays in character for the scene. Get per-turn feedback (corrections, more natural phrasing, short explanations). End with a session score (fluency, accuracy, confidence) plus a coach-style summary and optional share of the result. Stay motivated with streaks, history/replay, and progress views on mobile. Optionally compete on a global leaderboard or open a room-code multiplayer chat (via Supabase) for peer practice. The same product exists as FluentFlow on MeDo (web/desktop) and as this Expo / React Native app for iOS & Android, one narrative for judges: desk or pocket. How we built it Mobile: Expo (~54), React Navigation, NativeWind, Reanimated, AsyncStorage, expo-audio for recording/playback. AI: Google Gemini through a fallback chain of models in code, with a demo fallback path so live demos don’t die if the network or API hiccups (local scenario-aware lines, feedback-shaped stubs, and plausible scores, clearly flagged in-app when active). Voice output: ElevenLabs TTS was configured and wired to the chat flow. Social / cloud: Supabase (anon auth, Postgres, Realtime) for leaderboard and multiplayer rooms; SQL schema and setup live in-repo for reproducible judging. UI polish: Lucide icons via react-native-svg, so icons stay crisp on Android release builds without relying on flaky icon fonts. Web sibling: The MeDo-deployed FluentFlow delivers the browser experience; this repo delivers native UX (mic, navigation, store path). Challenges we ran into: Mobile audio across record, playback, and interruptions, moving to supported expo-audio patterns and centralized playback control. Keeping the model in character and in the target language with scenario-specific system prompts and language-quality blocks (including register hints where it matters). Shipping reliable builds: EAS environment variables must match what the app reads at build time; misaligned profiles or missing EXPO_PUBLIC_* keys showed up as “works in dev, blank in APK” until env and rebuilds were aligned. Android icon font issues with vector icon fonts in release builds were addressed by standardizing on SVG icons for primary UI. Supabase: enabling Anonymous auth, applying RLS policies, and ensuring Realtime is usable for room chat, all easy to miss in a short hackathon window. Accomplishments that we're proud of A full loop that feels demo-ready: scenario → speak/type → AI reply → feedback → score → (optional) leaderboard. Honest multilingual behavior, not just “translate this,” but stay in the target language and sound natural in context. Resilience: model fallbacks plus offline-style demo content so a judge demo can finish even under bad Wi‑Fi. One product, two surfaces: MeDo for web, and Expo for mobile, told as a single story. What we learned: Small, scenario-scoped prompts beat a single generic “language tutor” prompt in terms of trust and immersion. Voice needs explicit UX for limits, interruptions, and accessibility (labels, states). Hackathon demos punish “works on my laptop”: env + build + device checks are part of the feature. What's next for FluentFlow More scenarios, difficulty tiers, and optional CEFR-style goals. Deeper pronunciation feedback if we add richer ASR scoring. Tighter web ↔ mobile sync: shared scenario content, links from MeDo → app install, one source of truth for copy and analytics. <div