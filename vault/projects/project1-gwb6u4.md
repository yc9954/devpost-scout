---
slug: "project1-gwb6u4"
url: "https://devpost.com/software/project1-gwb6u4"
title: "Parallel"
hackathon: "United Hacks V6"
organization: "Hack United"
winner: true
words: 619
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Parallel

> Post a choice, let the world decide, and see the future through AI. Every vote builds a profile of your true character. Stop overthinking and start scrolling your destiny.

[Devpost](https://devpost.com/software/project1-gwb6u4) · hackathon [[United Hacks V6]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: transportation</sub>
**user** [[legal_professional]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** css, fastapi, gemini, java, node.js, postgresql, python, railway, react, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned:
- what's next for parallel:
- disclaimer

## Body

Code Extract Code Extract locked out locked in Inspiration We've all been there - staring at our phone at 2am, wondering "should I send that text?" or "should I quit my job?" Everyone has opinions, but who's actually good at giving advice? We wanted to build something that turns everyday dilemmas into a game where you prove you're the friend with the best judgment - or find out you're really not. What it does Parallel is TikTok for tough decisions. You scroll through real dilemmas from real people - breakups, career moves, risky texts - and vote on what they should do. Every vote earns or loses you points based on whether you match an AI's reasoning. Post your own decisions, watch the votes roll in, then come back later to share what actually happened. Climb the leaderboard, unlock AI personality insights, and compete in 2-week seasons to prove you're the best decision-maker in the room. How we built it React for the frontend with a dark/coral design system that feels premium and addictive. FastAPI handles everything on the backend - auth, real-time database, hosting, and cloud functions. We integrated Gemini's API to evaluate every decision posted (Still In Development), giving us an AI judge that stays hidden until users share their outcomes. The feed uses swipe mechanics and snap scrolling for that TikTok-style dopamine hit. Everything updates in real-time so you see votes and rankings change live. Challenges we ran into Bringing ideas from the drawing board to reality is something that our team didn't have much experience with, and the transition into execution surfaced significant friction within our group dynamics. We frequently encountered internal disagreements regarding feature prioritization and design choices, which forced us to develop new conflict-resolution skills to keep the project moving. This was further complicated by our integration of AI-assisted development; while these tools accelerated our output, they also introduced "hallucinations" and inconsistent code that required more human oversight than we initially expected. Ultimately, these hurdles acted as a crash course in project management, teaching us that technical expertise is only half the battle when navigating the gap between a vision and a finished product. Accomplishments that we're proud of: The app feels good. Every animation is smooth, every interaction has weight. We built a scoring system that actually makes you care about your rank. The real-time leaderboard creates genuine FOMO. And we nailed the core loop - post, vote, earn, climb - that keeps you coming back. It's not just functional, it's genuinely fun to use. What we learned: Real-time databases are powerful but unforgiving - one listener leak and your app becomes a memory hog. Postgresql transactions are essential for anything competitive. AI integration isn't just about API calls - it's about prompt engineering and managing user expectations. And most importantly: good design isn't about adding features, it's about making every interaction feel intentional and satisfying. What's next for Parallel: Video decisions (record yourself explaining your dilemma), ai and advanced filter moderation features, forum style comment threads for spicy debates, achievements and badges for hitting milestones, push notifications when someone votes on your decision, and maybe the biggest one - letting users bet points on their votes to go double-or-nothing. We also want verified "experts" in categories who can weigh in with special votes. Long term? This becomes the place everyone goes when they genuinely can't decide something. DISCLAIMER If Gemini doesn't work, then our API key has run out. The profile analysis uses metrics derived from post history and interactions, therefore the accuracy of the analytics should be taken lightly until a more in-depth user profile is available to Gemini. Due to Capcut restrictions the video is a screen recording. <div