---
slug: "love-island-to-die-for"
url: "https://devpost.com/software/love-island-to-die-for"
title: "Love Island: To Die For!"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 793
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/legal_justice"
  - "user/legal_professional"
---

# Love Island: To Die For!

> You thought you were off to enjoy a fun, exciting dating show experience... but something has gone terribly wrong. Now, it's up to you to figure out what happened!

[Devpost](https://devpost.com/software/love-island-to-die-for) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[legal_justice]]
**user** [[legal_professional]]

**stack** janitor.ai, next.js, python, react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for love island: to die for

## Body

Inspiration What if your favorite reality TV dating show took a dark turn? We were inspired by the dramatic storytelling of shows like Love Island and the intrigue of murder mystery visual novels like Ace Attorney. We wanted to create an interactive narrative experience that combines romance and solving mysteries — two of the most compelling, aspirational, and fun experiences in storytelling! What it does "Love Island: To Die For!" is an AI-powered murder mystery visual novel where you play as the newcomer to a reality show investigating the death of Hunter, one of your fellow contestants. You interrogate four suspect-contestants, each with their own motives, alibis, and secrets. Through turn-based conversations, you must piece together the truth from a web of romantic rivalries, hidden relationships, and carefully constructed lies. The game features both traditional individual "dates" with characters, and a unique feature for our gameplay: group conversations where suspects interact with each other. Here you can compete for romantic affection, but also engage with different conversation dynamics that reveals specific information . With a progress bar tracking your remaining turns, you must use your questions wisely to uncover the whodunnit! How we built it We built a full-stack application with a Python backend and Next.js/React/Tailwind frontend. The backend uses JanitorAI's LLM API to power dynamic, context-aware character responses that are finetuned perfectly for immersive storytelling. We also developed from scratch a multi-agent context management and memory system, in order to incorporate detailed personality profiles, backgrounds, and conditional secrets that are revealed based on conversation topics. We created a relationship system that tracks connections between characters, enabling us to update agent context and create consistent and believable inter-character interactions, while also progressively revealing clues. The frontend features a pixel-art visual novel aesthetic with smooth animations and custom components for dialogue boxes, character headshots, and progress tracking. And — of course — we designed an intricate murder mystery plot with multiple suspects, each with their own secrets and interconnected relationships that unfold naturally through gameplay. Challenges we ran into Creating believable, consistent AI characters was surprisingly difficult — we had to carefully craft system prompts that maintained personality while allowing for natural conversation flow and controlled information revelation. Balancing the mystery difficulty was another challenge: we needed to ensure clues were discoverable but not too obvious, and that different conversation paths could still lead to solving the mystery. Managing conversation state and context across multiple characters and conversation turns required careful state management. We also struggled with timing the reveal of secrets — characters needed to feel reluctant to share information but eventually crack under the right questioning. Accomplishments that we're proud of We're incredibly proud of the rich, dynamic narrative we created with four distinct characters and complex relationships. Our bespoke multiagent context management system was both lightweight and complex enough to create a genuinely evolving narrative experience — and a great learning experience. The relationship system we built allows characters to reference each other authentically and reveal different information based on who else is present in group conversations. We also love our pixel-art UI that sets the vibe perfectly! What we learned We learned that context engineering for multiagent narrative games requires a completely different approach than typical chatbot applications — you need to manage character consistency not just with the main character but with N possible other live relationships and conversation history. Especially for our needs, we learned (through doing!) how do achieve this with minimal token usage. On the technical side, we gained experience with streaming LLM responses in real-time UIs, managing complex state in React, and designing turn-based conversation systems. We also learned valuable lessons about game design — something half our team was doing for the first time this hackathon! We learned how to plant clues, create red herrings, and structure satisfying mysteries, all on the job. We discovered the importance of conditional information revelation and how to structure character descriptions to enable emergent storytelling. What's next for Love Island: To Die For We want to expand the game with multiple episodes featuring different murder mysteries and new casts of characters. We plan to add a deduction system where players can formally accuse suspects and present evidence, with different endings based on whether you correctly identify the killer. Voice acting and character animations would bring the personalities to life even more. We'd love to implement a memory system where characters remember previous conversations across multiple playthroughs, creating meta-narrative experiences. Adding branching storylines where player choices affect character relationships and unlock different plot paths would increase replayability. Finally, we want to create a level editor that lets players craft their own murder mysteries with custom characters, relationships, and secrets, turning LIT:DF into a platform for community-created interactive mysteries. <div