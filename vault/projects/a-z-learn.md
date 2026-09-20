---
slug: "a-z-learn"
url: "https://devpost.com/software/a-z-learn"
title: "A-Z Learn: Adaptive Neurodivergent Learning Platform"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1238
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# A-Z Learn: Adaptive Neurodivergent Learning Platform

> Have you ever felt like traditional classes turn even the most interesting topics into nap time? A-Z Learn solves this problem by creating personalized lessons revolving around your interests!

[Devpost](https://devpost.com/software/a-z-learn) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** fastapi, nextjs, postgresql, pygame, python, sentence-transformers, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a-z learn

## Body

Settings Page Lesson with scientific calculator built-in Implemented Game Dashboard Home Page Logo Inspiration One in five students in the U.S. is neurodivergent and the traditional "read the textbook, answer the worksheet" model fails almost all of them. Students with ADHD don't lack intelligence; they lack a reason to care right now. Every learning science study points to the same fix: connect the material to something the student actually cares about! We built A-Z Learn because we believe the gap between "I hate math" and "I love math" is mostly a context problem. A student who knows every drop rate in Minecraft can absolutely understand probability, they just need the lesson to meet them where they are. What it does A-Z Learn is an AI-powered STEM education platform designed for neurodivergent learners in grades K-12. Here's what happens when a student uses it: Pick your world. Choose an interest (Basketball, Minecraft, Video Games, Social Media) and a STEM topic (Probability, Genetics, Linear Equations, Python Basics, and more). The platform serves a lesson written specifically for that combination. Follow the quest. Every lesson opens with a hook, which is just a 1-2 sentence story written in the student's language and then three "quests": narrative-driven open response questions. This means that there aren't any multiple choice, or dropdown based questions! As a result, every student has to critically think and construct a response based on their knowledge. Get scored by real NLP. Answers are evaluated by a three-layer pipeline running on the backend: keyword overlap (ruleset), TF-IDF cosine similarity, and semantic embedding similarity via sentence-transformers (all-MiniLM-L6-v2). The final score is a weighted blend (20% ruleset / 30% TF-IDF / 50% NLP), graded as Correct, Partially Correct, or Incorrect. No LLM API calls, it's fully self-hosted inference. Play the STEM Treasure Hunter game. For math topics, students can open a custom interactive game embedded directly in the lesson. It's a 7-step coordinate geometry and probability challenge with a live grid, tiered difficulty (slopes → equations → systems → probability vault), a Gold economy, and full undo history. Earning Gold converts to real XP through a built in shop. Build a learning streak. Completed quests save to the database with XP earned and a grade. Daily streaks, a leaderboard, and achievement badges keep students coming back. Teachers can contribute. Educators can apply for a contributor account and add new lessons directly to the curriculum, pairing any interest with any STEM topic, as long as they follow our contributor guidelines built around the NLP scoring pipeline's requirements. How we built it Backend: FastAPI (Python). The NLP scoring engine runs at startup — it pre-fits a TF-IDF vectorizer over all model answers and loads the sentence-transformer model once, so inference is fast at request time. The evaluate() function runs all three scorers in sequence and returns a detailed breakdown: per-question keyword matches, cosine scores, and NLP scores alongside the weighted final grade. Auth: Google OAuth via Supabase with a full PKCE flow. The backend generates the verifier/challenge pair, initiates the redirect, and exchanges the auth code for a session. The resulting JWT flows to the frontend and gates all authenticated routes (profile, lesson history, contributor application). Database: Supabase (PostgreSQL). Three tables: users (profile, XP, streak, last active date), lesson_history (completed quests with scores), and developers (contributor applications). XP and streak updates happen transactionally after every completed lesson. Curriculum: The lesson content in data.json has been read through and optimized by us. Every lesson follows a strict structure: hook, 3 quests with model answers, quick check, final answer, which is designed around what the NLP scorer needs to grade accurately. Thirteen interest/topic combinations are live at launch. STEM Treasure Hunter: The game exists in two versions — a standalone pygame desktop app (built first as a proof of concept) and a full React port embedded in the web app. The web version uses a custom game engine in a React hook ( useGameEngine ) with a canvas-rendered coordinate grid ( TreasureCoordinateGrid ), step-level undo history, and a Gold-to-XP economy routed through the backend. Frontend: Next.js with TypeScript and Tailwind. Auth state lives in a React context. Lesson state flows through sessionStorage between the quest picker and the active lesson page. An accessibility context wraps the whole app for neurodivergent-first design. Challenges we ran into NLP scoring calibration. Raw semantic similarity scores from sentence-transformers cluster around 0.3–0.9 for topically related texts, not 0–1. A student's answer about basketball probability and the model answer both score high similarity to each other but not at the extremes of the range. We had to normalize the output to spread signal across the full scoring range, and tune the weighting between the three scorers so partial credit actually felt fair. PKCE OAuth without a frontend redirect. Most Supabase auth tutorials assume the client initiates OAuth. We needed the backend to own the entire flow (verifier generation, redirect, code exchange) and then hand a token to the frontend. Getting cookies, CORS, and Supabase's session exchange to cooperate across two different origins took careful debugging. Porting pygame to React. The Treasure Hunter game started as a Python pygame app with tight event loops and direct pixel drawing. Rebuilding it in React meant extracting the game logic into a pure state machine hook, rendering the grid as an SVG/canvas component, and wiring keyboard events through React's synthetic event system. The coordinate-to-pixel math had to be exact or the graphed lines wouldn't pass through the correct plotted points. Making lessons actually score well. Early model answers written like textbooks scored poorly against normal student language. We rewrote them in natural student phrasing — shorter sentences, key terms without jargon — specifically because the cosine scorer compares student prose against model prose, not against a knowledge base. Accomplishments that we're proud of A fully self-hosted NLP scoring pipeline that gives students meaningful feedback without any LLM API calls. A custom interactive math game in pygame that turns coordinate geometry into a treasure hunt with real stakes (Gold that converts to XP). Hand-checked lessons across 13 interest/topic combinations, each with a hook, three graded quests, a quick check, a final answer, and an open-source contributor framework so teachers can extend the curriculum. A complete auth system (PKCE OAuth → JWT → Supabase) with XP, streaks, leaderboard, and achievements working end-to-end. What we learned Building the NLP pipeline taught us that "semantic similarity" is not the same as "answer correctness." A student can use semantically similar words in a completely wrong context. The three-layer approach of keywords first, then surface-level TF-IDF, then deep embedding excels because each catches different failure modes, and the weighting matters a lot. We also learned that curriculum design is similarly difficult to engineering. Writing a lesson that a neurodivergent middle schooler will actually stay with, that connects authentically to their interest, and that produces model answers the NLP scorer can grade fairly took a substantial amount of double checking and optimizing. What's next for A-Z Learn Expand the lesson library across more interest/topic combinations (Fitness + Science Fundamentals, Formula 1 + Physics, Music + Math) Live contributor review queue so approved teachers can publish lessons directly Misconception detection — flag when a student's answer matches the common wrong belief rather than the correct one Adaptive difficulty — surface harder quests once a student consistently scores Correct on a topic Accessibility panel improvements for dyslexia-friendly fonts, reduced motion, and high contrast modes <div