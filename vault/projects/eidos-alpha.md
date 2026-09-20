---
slug: "eidos-alpha"
url: "https://devpost.com/software/eidos-alpha"
title: "EIDOS-alpha"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 850
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# EIDOS-alpha

> Turn live lectures into study-ready kits

[Devpost](https://devpost.com/software/eidos-alpha) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** 2.0, better-auth, css, equation, google-gemini-2.0-flash, html2canvas, jspdf, katex, lucide, modules, mongodb, next.js, prisma, react-markdown

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eidos
- team information
- update (june 2026):

## Body

Thumbnail Light Mode - Interface Section Interface How it works Study modes Features Section Built with Google Gemini 3 Inspiration Ever sat in a lecture, scribbling notes so fast you missed what the professor actually said? Or recorded a 90-minute class only to never watch it again because... who has time? That was us. Every day. We were tired of: Choosing between listening and writing Messy notes scattered across apps Hours of recordings with no efficient way to study from them Exam season chaos with disorganized materials EIDOS came from genuine frustration. We wanted a study buddy that could watch lectures with us, take perfect notes, quiz us, and explain things when we got confused. Less time organizing, more time learning. What it does EIDOS (Educational Intelligence & Dynamic Optimization System) turns learning chaos into clarity. Core Features Live Capture : Record lectures, capture frames, transcribe speech in real-time, generate structured AI notes AI Course Generator : Input a topic → get complete courses with chapters, lessons, quizzes, and final exams Video Lectures : Slide-based presentations with animated whiteboard drawings and human-like AI narration Study Sessions : Upload documents, chat with an AI tutor that understands YOUR materials AI Tutor : Voice-activated assistant you can interrupt mid-sentence (say "hey" or "wait") Certificates : Pass the final exam → download your certificate How we built it ⚡ Gemini 3 Integration EIDOS is built entirely on Google Gemini 3 . Every AI feature in the platform is powered by the Gemini 3 API via the official @google/generative-ai SDK. We utilized specific capabilities of the gemini-3-flash-preview model to handle distinct complex tasks: Structured JSON Output (JSON Mode): We enforce strict JSON schemas for generating Courses, Quizzes, and Exams . This ensures that the generated content can be parsed programmatically to create interactive UI elements like progress bars, quiz forms, and certificate validation. Streaming & Real-time Generation: For Notes and Written Lectures , we utilize Gemini's streaming capabilities. Instead of making the user wait for a spinner, content is streamed token-by-token directly to the frontend, creating a responsive "magic" effect. Multimodal Vision Capabilities: In Study Sessions , users can upload PDF documents or images. We pass these directly to Gemini 3 as base64 inline data, allowing the AI to "see" charts, diagrams, and text within uploaded study materials to answer specific questions. Text-to-Speech (TTS): For our Video Lectures , we integrated gemini-2.5-flash-lite to generate natural, human-like narration that syncs with the generated slide content. Tech Stack Layer Technology Framework Next.js 14+ (App Router) Frontend React 19, TypeScript Styling CSS Modules + Design Tokens Database MongoDB + Prisma ORM Auth Better-Auth AI Model Google Gemini 3 Flash Preview AI SDK Google Generative AI Node.js SDK 3D Three.js / React Three Fiber Math KaTeX Key Implementation Details Speech Recognition : Web Speech API with auto-restart logic for reliability AI Prompts : 100+ lines of carefully crafted instructions for natural-sounding narration Streaming : Server-Sent Events for real-time content generation Certificates : html2canvas + jsPDF for downloadable PDFs Challenges we ran into Making AI sound human Early versions sounded robotic Weeks of prompt iteration: contractions, filler words, rhetorical questions, personal touches Speech API reliability Web Speech API stops randomly, throws errors, differs across browsers Built auto-restart logic and extensive error handling AI Tutor interrupt detection Detecting "hey" or "stop" while text-to-speech is playing Canceling speech synthesis and resuming listening without false positives Streaming JSON from Gemini Parsing partial responses while maintaining valid markdown Careful buffer management required Course generation pipeline Multi-step generation: outline → chapters → lessons → quizzes Progress updates and failure handling at each stage Accomplishments that we're proud of Live Capture generates comprehensive notes from 20+ minute recordings AI Tutor with voice interruption actually works smoothly Full course generation with video lectures and embedded quizzes Polished UI with glassmorphism, animations, dark/light themes Comprehensive documentation (API, architecture, components, user guides) What we learned Prompt engineering is an art - specificity about format, tone, length matters Browser APIs are powerful but inconsistent - expect edge cases Streaming beats spinners - users prefer seeing content appear gradually TypeScript saves time - caught bugs before they happened Good architecture pays off - easy to extend and debug What's next for EIDOS [ ] Advanced analytics and learning streaks [ ] Collaborative study workspaces [ ] Multiple AI model support [ ] Offline mode with sync [ ] Spaced repetition flashcards [ ] Enhancement Team Information Kaleemullah Younas Role: Full-Stack AI Engineer - GITHUB Muhammad Umer Role: Web Developer & Devops - GITHUB Contact Primary Contact Email: EMAIL Disclaimer This is an MVP (Minimum Viable Product) deployed using free-tier services. As a result, the live version may occasionally face 429 errors or rate limits. We plan to upgrade to paid tiers or some proprietary models in the future for a more reliable experience. Update (June 2026): The live demo link is currently unavailable. The application was previously hosted using free cloud credits, which have since expired, and the hosting instance has been decommissioned. The source code and project details still remains available for review. Thank you for your understanding. <div