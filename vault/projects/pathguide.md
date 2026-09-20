---
slug: "pathguide"
url: "https://devpost.com/software/pathguide"
title: "pathguide"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 943
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/geospatial"
---

# pathguide

> PathGuide AI guides students with personalized roadmaps, skill tests, industry insights, and university matches—making career decisions simple, clear, and completely tailored to their goals.

[Devpost](https://devpost.com/software/pathguide) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
  <sub>weak: benchmark_measured</sub>
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[education]] [[mental_health]] [[transportation]]
**user** [[developer]] [[educator_student]] [[general_public]] [[researcher]] [[social_worker]]
**substrate** [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** class-variance-authority, cloud, clsx, css, eslint, google, gpt-4o, gpt-4o-search-preview, html, javascript, lucide, next.js-15, node.js-18+, openai

## How they structured the write-up

- core functionality
- ai tools disclosure
- data handling & privacy
- final note
- interview cake
- exponent (try exponent)
- codecraft / codecrafters
- nordvpn
- incogni
- ✔ final note

## Body

Roadmap mode: Creates a personalized, step-by-step learning path for any career or skill based on the user’s background, level, and goals. Roadmap mode: Understand the concept and explore free learning resources. Industry Insights mode: Delivers real-time news, research breakthroughs, funding updates, new startups, Gov policies and market trends. University Mode: Finds the best universities and programs worldwide with verified links, admission requirements, research strengths, etc... University mode: admission process. Quiz Mode:Generates a custom quiz based on the user’s roadmap and evaluates their strengths, weaknesses, and recommended next steps. PathGuide AI — Project Description + AI Tools Disclosure I built PathGuide AI because I’ve personally struggled with choosing the right programs, understanding career paths, and figuring out what to study next. Every time I wanted clarity, I had to jump across 10–15 websites and still ended up confused. I wanted to create something I wish I had years ago — a simple, intelligent platform that genuinely guides students and career-changers with clarity. PathGuide AI is an all-in-one guidance platform designed to help students understand what to study , what skills they need , which universities fit them , and how to plan their learning journey . Instead of giving generic advice, PathGuide has focused “modes” that each solve a real problem students face today. Core Functionality 🧭 Roadmap Mode – Personalized Learning Paths Creates tailored learning paths for any domain — software engineering, ML, medicine, renewable energy, finance, culinary arts, aviation, and more. PathGuide asks a few background questions in a friendly tone, understands the user’s level, then generates a structured 5–8 stage roadmap with topics, resources, timelines, and explanations. 🌍 Industry Insights Mode – Live Market Awareness Provides real-time news, research updates, funding rounds, startup activity, and major breakthroughs from trusted sources (e.g., Reuters, TechCrunch, government sites, Nature, university research pages). Students can quickly see what’s happening in the industry they want to enter. 🎓 College Explorer Mode – Smart University Discovery Finds real universities worldwide with verified program links , admission requirements, faculty highlights, research strengths, and official application portals. Users can click straight through to official pages instead of wasting time searching manually. 🧪 Test Me Mode – Adaptive Skill Assessment Generates quizzes tailored to the user’s roadmap and stated level, then returns detailed feedback on: strengths weaknesses topic-wise performance recommended resources to improve AI Tools Disclosure PathGuide uses two OpenAI models: GPT-4o and GPT-4o-search-preview , each with a clear role. 🤖 GPT-4o Used for: Roadmap creation Conversational intake Quiz generation Quiz scoring and feedback General academic and career counseling Why: GPT-4o provides strong natural language understanding, handles nuanced context, and produces structured outputs (like JSON roadmaps and question sets) with high reliability. Temperatures: Roadmap intake: 0.8 (more conversational and flexible) Quiz generation: 0.4 (more structured) Quiz evaluation: 0.3 (precise and analytical) 🌐 GPT-4o-search-preview Used for: University search and profiling Industry insights and trend analysis Real-time resource discovery Validating current industry requirements Why: It performs live web search and pulls data only from legitimate, high-quality sources. All outputs (universities, news, research, opportunities) come with direct source links so users can verify everything themselves. Temperatures: Industry insights: 0.2 (accuracy first) College search: 0.3 (small flexibility, accuracy prioritized) Data Handling & Privacy No user accounts, profiles, or personal identifiers are stored. Roadmaps and quiz results are kept locally in the browser for ~1 hour and then effectively discarded. All communication with OpenAI is over encrypted channels. API keys are stored only in server-side environment variables , never in the public repo or client code. Final Note PathGuide AI is built for students who feel lost, career-changers who don’t know where to begin, and anyone trying to make sense of an overwhelming amount of information. The goal is simple: turn confusion into a clear, personalized path — one roadmap at a time. ⭐ Feedback on Tools Explored During the Event (Post-Event Survey) Interview Cake I tried out Interview Cake’s coding questions and their detailed hint-driven explanations. The way they break down a problem step-by-step inspired how I designed PathGuide’s “Test Me” mode. Their reasoning approach (not just the final answer) helped me think about feedback design for students. Feedback: I’d love to see more beginner-friendly warm-up questions to help absolute beginners ease into coding. Similar tools explored: ✔ Interview Cake ✔ Byte by Byte Exponent (Try Exponent) I explored Exponent’s mock interview system, coaching content, and role-specific interview prep. It helped me understand how structured career paths and skill evaluations could be incorporated into PathGuide. Feedback: A clearer “role progression map” (e.g., Junior → Mid → Senior) would make their guidance even more helpful. Similar tools explored: ✔ Exponent ✔ IGotAnOffer CodeCraft / CodeCrafters I looked at their project-based learning paths and how they outline required skills, checkpoints, and progression. This influenced PathGuide’s roadmap logic (pre-skills → core skills → advanced). Feedback: More frequent micro-assessments between modules would help learners track progress more naturally. NordVPN Not a learning platform, but I used NordVPN during research phases—especially for accessing region-specific university resources. It worked fast and reliably. Feedback: A quicker toggle (or a small desktop widget) would make switching regions even smoother. Incogni I reviewed Incogni’s privacy removal service to understand how to keep PathGuide’s data practices clean and student-safe. It reinforced the importance of not storing any user data. Feedback: A small developer-focused checklist on privacy best practices would be amazing for early-stage builders. ✔ Final Note These tools were not built into the project, but exploring them definitely shaped how I approached learning flows, assessments, privacy, and student experience. They helped me think more deeply about what makes a guidance platform genuinely useful for learners — clear structure, realism, privacy, and progression. <div