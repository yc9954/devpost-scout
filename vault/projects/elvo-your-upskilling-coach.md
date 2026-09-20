---
slug: "elvo-your-upskilling-coach"
url: "https://devpost.com/software/elvo-your-upskilling-coach"
title: "ELVO - your upskilling coach"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 604
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ELVO - your upskilling coach

> People get lost trying to learn alone. Elvo fixes that with a personal, conversational coach that guides your entire learning journey. Talk, understand, and progress every day.

[Devpost](https://devpost.com/software/elvo-your-upskilling-coach) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** exa.ai, gemini, groq, jina, netlify, react, react-flow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for elvo – your upskilling coach

## Body

projects page home chat realtime discover page for tips,news and makeing them aware. ELVO – Your Upskilling Coach Live now: elvoai.netlify.app Inspiration So many students start their learning journeys without a clear map. and end up with confusiosn. I have seen all of my classmates falling into same situation of what to do and where to start an dhow to do. Existing tools often overwhelm or assume prior knowledge. ELVO was born from a vision to provide every student or individual regardless of background a confident, step-by-step path to skills and growth, all in one approachable platform with conversational based learning. What it does ELVO is built around two core student-empowering components, plus universal chat: Projects (Personal Upskilling Journeys) When a student picks a new goal (e.g., “Learn web design”), ELVO consults in a friendly way, then creates a smart, week-wise roadmap broken down into achievable steps. Progress is visualized, and every project is a living folder students can revisit, pause, or build alongside new interests mirroring real-life multitasking. Student Benefit: Students don’t face vague to-do lists they get dynamic, visual guidance that adapts to their pace, making big goals feel manageable. Discover (AI-Powered Feed & Industry Insights) Students can explore a curated daily feed with: Bite-sized learning tips tailored to their interests, The latest tools and productivity hacks, Personalized industry news, trends, and career inspiration. Student Benefit: Instead of endless surfing, students stay updated and inspired, discovering new opportunities and broadening their horizons all while focusing on their own projects. Smart Chat & Exploration At any point, students can switch to conversation mode for explanations, advice, or motivation no need to feel stuck or lost. Student Benefit: Seamless “ask & learn” for clarification, context, and ongoing discovery, all integrated into their learning journey. How we built it Frontend: Custom React app (40% coded with Copilot/Copilot+, remaining hand-built and styled) Project Journeys: Built using ReactFlow to visualize week/day-level progress inside each “project” folder, letting students track and unlock their own roadmap Backend: Netlify serverless functions integrating Groq for fast AI (multi-model) chat, Exa for web/contextual lookup, Gemini for image/gen, Claude and Lovable for logic Discover Feed: AI-driven aggregation and reformatting (via APIs and Exa search) delivering daily, relevant “discover” and industry content True solo build, designed for scalability and expanded use Challenges we ran into Mapping and managing multiple, parallel, and nested projects for students with several goals Designing an adaptive feed that feels fresh and relevant, not generic or overwhelming Ensuring smooth, “always available” chat and guidance across dynamic learning journeys and the discover feed Accomplishments that we're proud of Created an integrated space for students to launch (and manage) multiple upskilling journeys, not just one static roadmap Built a non-intimidating "discover" feed for ongoing curiosity and motivation Deployed a working demo that blends chat, project, and discover workflows solo, end-to-end What we learned Breaking student goals into visual, achievable “project” journeys reduces overwhelm and builds real momentum Personalization goes beyond chat it’s about continuously surfacing new relevant ideas via a daily discover feed Building for students’ multitasking, curiosity, and evolving goals leads to higher engagement What's next for ELVO – your upskilling coach Crowdsourced discover feeds from real learners and experts, not just AI Community “project templates” so users can share/remix learning journeys Real-time progress sharing, accountability, and feedback within each project More accessible UX, mobile-ready design, and public open source ELVO brings together focused learning journeys and an endless well of inspiration/discovery so every student moves forward with confidence, curiosity, and community. Live now: elvoai.netlify.app try this in desktop for better ui expereince as the mobile ux is unnder development <div