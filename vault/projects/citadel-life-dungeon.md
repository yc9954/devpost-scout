---
slug: "citadel-life-dungeon"
url: "https://devpost.com/software/citadel-life-dungeon"
title: "Citadel: LIFE//DUNGEON"
hackathon: "Pixel Forge AI Hackathon ($18,000+ in Prizes)"
organization: "Pixel Forge"
winner: true
words: 870
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Citadel: LIFE//DUNGEON

> An AI-powered life-skills RPG that turns real-world challenges into fun adventures, teaching kids how to make smart decisions, spot scams, manage money, solve problems, and navigate everyday life.

[Devpost](https://devpost.com/software/citadel-life-dungeon) · hackathon [[Pixel Forge AI Hackathon -18-000- in Prizes-]]

## Facets

**mechanism** [[deterministic_policy]] [[simulation_digital_twin]]
**domain** [[health_clinical]] [[housing_homeless]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** gemini, html5, next.js, react, tailwindcss, typescript, vercel, webaudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for citadel: life//dungeon

## Body

New Run Landing Real-life Dungeons Scam Bureaucracy Inspiration Real-world problems often feel like games where the rules are unclear and the difficulty changes without warning. Scams, job interviews, financial pressure, bureaucracy, and medical paperwork all require decision-making under stress. We wanted to turn these situations into something people could safely practice. This led to LIFE//DUNGEON — an adaptive RPG where the dungeons are real-world problems and the AI acts as the Game Master. Instead of simply telling players what the correct answer is, the game observes how they think, learns their behavioural patterns, and creates future scenarios around their weaknesses. What it does LIFE//DUNGEON contains five real-world survival dungeons: The Scam — identifies urgency, authority manipulation, and suspicious requests. The Bureaucracy — teaches players to resolve contradictions and verify authoritative information. Financial Survival — tests decision-making and reasoning under a fixed budget. The Job Hunt — simulates an adaptive AI interviewer that challenges vague or contradictory answers. The Medical Maze — teaches players to navigate paperwork, coverage, and appointments without providing medical diagnosis. Every decision affects the player's stress, time, cash, skills, and future difficulty. Players also earn salvage after each run and use it to build an 8×5 safe house. Different structures provide gameplay perks that directly affect future runs. The game also includes an evidence board, red-flag tagging, adaptive difficulty, a Field Manual, achievements, player progression, procedural pixel-art scenes, and shareable result cards. How we built it The game is built with Next.js, React, and TypeScript , with Gemini 3.7 Flash serving as the AI Game Master. The architecture deliberately separates AI creativity from deterministic game rules: React Browser ↓ Next.js API ↓ Gemini 3.7 Flash ↓ Structured JSON / Game Master Turn ↓ Game Engine ↓ Run State + Player Profile Gemini generates the story, characters, scenarios, and judgement, while the game engine handles actual state changes. Every AI response is validated, sanitised, clamped, and checked before it can affect the game. We used JSON-schema constrained structured outputs so every Game Master response follows a predictable format. The entire experience is designed around a procedural pixel-art aesthetic. Scenes are rendered programmatically using Canvas, with dithering, lighting, parallax, CRT effects, and atmospheric backgrounds. No image assets are required. Player progression, safe-house construction, achievements, run history, and profiles persist through LocalStorage , meaning the game requires no database or authentication. Challenges we ran into The biggest challenge was making an AI-driven game reliable. An LLM can generate creative scenarios, but allowing it to directly modify game state could easily break the rules. We solved this by making the AI propose changes rather than directly control state . The engine sanitises every response, clamps numerical values, removes invalid actions and evidence, and forces a loss when the timer reaches zero. Another challenge was Gemini API rate limits and latency. A single turn can take around 10–20 seconds, so we created rotating Game Master status messages to make the waiting period feel intentional rather than like a frozen interface. We also implemented API key rotation for demos. Finally, we wanted the game to feel like a cohesive RPG rather than a collection of AI prompts. This required building a unified visual system, procedural pixel-art scenes, sound effects, progression systems, a safe house, achievements, and persistent player modelling around the AI core. Accomplishments that we're proud of Built five fully playable adaptive dungeons around real-world problems. Created an AI Game Master that remembers behavioural patterns and adapts future scenarios. Implemented deterministic game rules around a probabilistic AI layer. Built an 8×5 safe house where structures provide measurable gameplay advantages. Created red-flag tagging and reasoning-based grading instead of simply judging right/wrong answers. Built a live AI interviewer that detects vague answers and contradictions. Created procedural pixel-art environments with zero shipped image assets . Implemented shareable 1200×630 result cards. Achieved 58/58 engine self-test assertions . Passed 14/14 browser smoke tests with zero console or page errors. Verified the Game Master and explanation endpoints against the live Gemini API. What we learned We learned that building an AI game is less about generating impressive responses and more about designing the boundary between AI creativity and deterministic software . The AI is excellent at creating unpredictable situations and judging reasoning, but it should not be trusted with critical game state. Putting a strict engine between the model and the player made the experience much more reliable. We also learned that failure can be more valuable than success. LIFE//DUNGEON intentionally rewards players even when they lose because every failed run reveals a behavioural weakness that can be trained in the next run. Most importantly, we learned that AI can be used not just to answer questions, but to create personalised environments where people can practice thinking under pressure . What's next for Citadel: LIFE//DUNGEON The next step is turning LIFE//DUNGEON into a larger personal survival-training platform. We want to add more dungeons covering areas such as negotiation, online safety, travel disruptions, housing, workplace conflicts, and emergency planning. We also want deeper player modelling, more sophisticated adaptive difficulty, multiplayer/co-op scenarios, richer safe-house progression, and long-term skill tracking. The ultimate goal is simple: Don't just tell people how to handle the real world. Let them practice surviving it. <div