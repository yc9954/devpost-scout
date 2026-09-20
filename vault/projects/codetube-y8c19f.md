---
slug: "codetube-y8c19f"
url: "https://devpost.com/software/codetube-y8c19f"
title: "CodeTube"
hackathon: "BatchHacks (Students Only; Open-Ended)"
organization: "Batch 09"
winner: true
words: 1174
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# CodeTube

> Transform passive YouTube tutorials into interactive, AI-powered coding journeys.

[Devpost](https://devpost.com/software/codetube-y8c19f) · hackathon [[BatchHacks -Students Only- Open-Ended-]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[transcript_audio]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** nextjs?#react?#typescript?#tailwindcss?#shadcnui?#firebase?#firestore?#firebaseauth, promptapi?#summarizerapi?#writerapi?#rewriterapi?#proofreaderapi?#translatorapi, pwa?#hybridai?#offlinefirst?#aiineducation?#webapplication, vercel?#youtubeapi?#githubapi?#judge0api?#genkit?#gemininano?#chromebuiltinai

## How they structured the write-up

- 🌟 solution
- 🛠️ tech stack
- ✅ features vs apis
- 🤖 hybrid ai strategy
- 🔍 how codetube differs from existing solutions
- ⚡ network-resilient ux & offline functionality
- 🚧 challenges we faced
- 🏅 accomplishments
- 📚 what we learned
- 🚀 what’s next for codetube
- ⚙️ implementation score breakdown

## Body

Logo Architecture Course_Preview Focus_Mode Pratice_Pitch Course_Mentor Roadmap Github_Export 🚀 CodeTube Transform Passive YouTube Coding Tutorials into Interactive Courses CodeTube is a web application that converts passive YouTube coding tutorials into interactive, hands-on learning experiences . Leveraging both client-side (Chrome Built-in AI) and server-side (Gemini Nano) intelligence, it empowers creators and learners to actively engage with educational content — anytime, anywhere. 🚨 Problem Statement YouTube is the favorite classroom for today’s coders — millions learn Python, React, and AI from it. But while the content is great, the learning experience is chaotic and distracting . Meet Arjun , a college student passionate about web development. He starts watching a 2-hour React tutorial on YouTube. 🎯 Within minutes, he’s distracted by suggested videos and ads. ⌛ When he comes back, he spends 10 more minutes scrolling to find where he left off. 📝 He tries copying code snippets from the video, but it’s messy and time-consuming. 💻 He wishes he could just run the code directly while learning. 💰 When he tries paid platforms like Coursera or Udemy, he finds them too costly — and they don’t let him combine what he’s already watching on YouTube. Result? Arjun ends up watching more and practicing less , losing motivation and valuable time. This is the reality for thousands of learners who want hands-on coding but get stuck in passive, distracted learning . 🌟 Solution CodeTube transforms a static YouTube tutorial into a structured, AI-guided course with interactivity built in. AI Course Mentor 🧭: Generates learning roadmaps, prerequisites, and key concepts. YouTube Video Import 🎥: Quickly import any coding video. Automatic Chapter Detection ⏱️: Extracts video chapters and topics automatically. AI Notes & Summaries 📝: Generate and edit summaries, or dictate notes via speech-to-text. Timestamped Video Snapshots 📸: Insert clickable snapshots as visual bookmarks. Interactive Quizzes & Interview Prep ❓💼: Reinforce concepts and practice job interview questions. Focus Mode 🎯: Distraction-free UI for immersive learning. Practice Your Pitch 🎤: Get AI feedback on voice-based responses and delivery. AI Writing Tools ✍️: Proofread, rewrite, or translate notes. Code Snippet Execution 💻: Run code directly in-browser. Export to GitHub 📂: Turn your learning into portfolio-ready projects. 🛠️ Tech Stack Frontend: Next.js, React, TypeScript, Tailwind CSS, ShadCN UI Backend: Firebase Authentication, Firestore AI Layer: Hybrid setup using Chrome Built-in AI (client) & Gemini Nano via Genkit (server) APIs: YouTube API, Gemini Nano API, GitHub API, Judge0 API Hosting: Vercel ✅ Features vs APIs Feature Client-Side APIs 🌐 Server-Side APIs ☁️ Notes Import YouTube Video 🎥 ❌ ✅ YouTube API Fetch video metadata and transcript Automatic Chapter Detection ⏱️ ❌ ✅ YouTube API + Gemini Nano Detect timestamps intelligently AI-Powered Notes & Summaries 📝 ✅ Prompt, Writer, Summarizer, Proofreader, Translator, Rewriter ✅ Gemini Nano Editable and voice-assisted Course Mentor 🧭 ❌ ✅ Gemini Nano Generates learning roadmap Interactive Quizzes ❓ ✅ Prompt, Writer, Rewriter ✅ Gemini Nano Multiple-choice & conceptual Interview Prep 💼 ✅ Prompt, Writer, Rewriter ✅ Gemini Nano Technical Q&A generation Practice Your Pitch 🎤 ✅ Translator, Summary ✅ Gemini Nano Speech-to-text + feedback Focus Mode 🎯 ✅ Built-in AI ❌ Custom UI focus features Code Snippet Execution 💻 ❌ ✅ Judge0 API Run and test code Export to GitHub 📂 ❌ ✅ GitHub API Push course content automatically Proofreading / Rewriting ✍️ ✅ Proofreader, Rewriter, Writer ✅ Gemini Nano Content refinement Notes Translation 🌐 ✅ Translator API ✅ Gemini Nano Multilingual support 🤖 Hybrid AI Strategy Client-side AI (Chrome Built-in AI): Performs instant text generation, summarization, proofreading, rewriting, and translation locally on supported browsers — even offline. Server-side AI (Gemini Nano via Genkit / Firebase AI Logic): Handles advanced tasks like the Course Mentor , Quiz Generation , Interview Prep , and Speech Analysis for universal device support. Benefit: A Hybrid AI model that ensures privacy, low latency, and consistent performance — whether users are online or offline, on Chrome or other browsers. 🔍 How CodeTube Differs from Existing Solutions Existing Platforms CodeTube Passive video watching Active, chapter-based learning Manual note-taking AI-assisted notes & summaries No offline support Offline-first PWA with caching & on-device AI Static content Interactive quizzes & exercises No project integration GitHub export for instant portfolio Unguided learning AI Mentor with structured roadmap ⚡ Network-Resilient UX & Offline Functionality Offline-first PWA: Access saved courses and chapters without internet. Firestore Offline Persistence: Local read/write data caching. Background Sync: Auto-sync changes once reconnected. On-device AI: Perform text-based AI tasks offline via Chrome’s Built-in APIs. Available Offline: View/edit existing courses, notes, and code snippets. Use Chrome’s AI tools for summarizing, rewriting, and translation. Requires Internet: Import new videos, perform advanced AI operations, export to GitHub, and execute code snippets. 🚧 Challenges We Faced Syncing state between Chrome’s on-device AI and Gemini Nano server logic. Managing offline data persistence with Firestore and Background Sync. Designing an elegant UI that supports both focus and functionality . Integrating real-time video data with AI-generated summaries and notes. 🏅 Accomplishments Built a fully working hybrid AI web app . Integrated Chrome’s on-device AI APIs seamlessly. Converted videos into interactive, trackable learning modules. Added direct GitHub export for showcasing learning. Designed a minimal, distraction-free workspace optimized for focus and learning. 📚 What We Learned How to build truly hybrid AI systems combining on-device and server models. Deep integration of Gemini Nano and Chrome Built-in AI APIs . Building offline-first AI applications with background sync. Structuring unorganized video content into meaningful, interactive learning paths . 🚀 What’s Next for CodeTube Enable multimodal AI to analyze code visuals, slides, or screenshots. Introduce voice-based tutoring with real-time dialogue. Expand to non-coding domains (design, language, science tutorials). Launch a Chrome Extension for one-click YouTube integration. Add a community course-sharing hub for AI-generated learning materials. ⚙️ Implementation Score Breakdown Criteria Description Implementation Details Score (out of 10) Use of Chrome Built-in AI APIs Integration of Prompt, Writer, Rewriter, Proofreader, Summarizer, and Translator APIs Used in note generation, rewriting, quiz creation, and translation directly in the browser 10 / 10 Hybrid AI Architecture Combination of on-device (client-side) and cloud (server-side) AI Chrome Built-in AI for offline instant responses; Gemini Nano via Genkit for complex logic 9.5 / 10 Functionality & Feature Depth End-to-end learning flow — from importing videos to exporting GitHub-ready content YouTube import, chapter detection, AI summaries, quizzes, focus mode, GitHub export 9 / 10 Offline Capability PWA + local AI execution using Chrome APIs Offline-first mode with Firestore persistence and background sync 9 / 10 User Experience & Interface Simplicity, accessibility, and responsiveness Minimal UI with Tailwind, ShadCN, dynamic chaptering and visual bookmarks 8.5 / 10 Cross-Browser & Device Support Functionality maintained even without Chrome AI Automatic fallback to Gemini Nano for non-Chrome browsers 9 / 10 API Reliability & Data Flow Handling state management and async tasks cleanly Fixed stale-state issue, implemented event-based synchronization 8.5 / 10 Scalability & Hosting Production-ready deployment Deployed via Vercel + Firebase for seamless global access 9 / 10 Innovation & Uniqueness Novel use of hybrid AI to convert videos into interactive courses First-of-its-kind hybrid AI educational workspace 10 / 10 <div