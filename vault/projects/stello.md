---
slug: "stello"
url: "https://devpost.com/software/stello"
title: "Stello"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 636
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Stello

> Learn by doing. Progress by thinking.

[Devpost](https://devpost.com/software/stello) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** framer-motion, javascript, react, supabase, tailwindcss, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stello

## Body

Stello Inspiration I kept noticing the same pattern around students (including me) opening ChatGPT the moment a STEM problem got hard. Not to understand it. Just to get the answer and move on. The learning wasn't happening, it was being skipped and that bothered me. AI is genuinely powerful, but the way most students interact with it is making them worse at thinking, not better. I wanted to change that. What if AI refused to give you the answer? What if instead, it asked you exactly the right question to make your brain figure it out? So I built Stello: a platform where every STEM topic becomes a mission with real stakes. Suddenly you're not doing homework. You're on a quest. What it does Stello is an AI-powered STEM quest platform for teens aged 13–18. Students choose a subject (Mathematics, Physics, Chemistry, or Biology), then accept a story-driven mission built around real curriculum concepts. Inside each mission, STELLA, a Socratic AI tutor powered by Claude (Anthropic) guides them through 3 puzzles. She never gives direct answers. Instead, she diagnoses exactly what's wrong in a student's thinking and asks one targeted question that nudges them toward the solution themselves. How we built it I vibecoded it totally using lovable with the Frontend: React + Tailwind CSS + Framer Motion for animations. The design system uses a deep space navy palette with electric violet, cosmic teal, and gold accents, with hand-drawn doodle SVGs floating across every page as background elements. AI Engine: Claude API (claude-sonnet-4-6) by Anthropic. STELLA's behavior is defined by a carefully engineered system prompt that enforces Socratic-only responses, she receives the mission context, the puzzle, and the student's attempt, then responds with a guiding question, never the answer. Backend: Supabase handles authentication, session persistence, and the PostgreSQL database, storing user profiles, XP, mission progress, streaks, badges, group memberships, and daily bonus completions with Row Level Security. Hosting: Vercel for instant deployment and mobile-responsive delivery. Challenges we ran into The hardest challenge was engineering STELLA's AI behavior correctly. A generic "hint system" is easy to build, but a truly Socratic AI that diagnoses a specific misconception from a specific wrong answer and responds with exactly one targeted question is a much harder prompt engineering problem. Getting STELLA to stay in character (teen mentor voice, narrative-wrapped hints, no answer leakage) across all subjects required significant iteration. Session persistence across page refreshes in Supabase also took multiple attempts to get right, making sure auth state was globally available without redundant fetches on every route. Accomplishments that we're proud of STELLA actually works as a Socratic tutor, she pushes back, she nudges, she celebrates, and she never just hands over the answer The mission narrative design makes STEM feel genuinely urgent and engaging "save the Mars colony" hits differently than "solve this gas law problem" Built a full-stack app with auth, real-time XP, leaderboards, groups, and 32 playable missions as a solo developer. What we learned I learned that the most impactful thing AI can do in education isn't answering questions, it's asking them. The Socratic method is thousands of years old, and wrapping it in a modern AI that knows your exact misconception makes it more powerful than ever. I also learned a huge amount about prompt engineering, Supabase RLS, React state management across protected routes, and how to scope a product ruthlessly when building solo under deadline pressure. What's next for Stello Computer Science missions (currently locked at Level 5 full curriculum coming next) Teacher dashboard: assign missions, track class progress, see where students are getting stuck Voice mode: students speak their reasoning aloud, STELLA responds, practicing verbal explanation (the Feynman technique) Expanded language support for non-English speaking students Mobile app (React Native) for fully offline mission play School partnerships to bring Stello into actual classrooms <div