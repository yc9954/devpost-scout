---
slug: "vibe-survivor-hderg9"
url: "https://devpost.com/software/vibe-survivor-hderg9"
title: "Vibe Survivor"
hackathon: "Chroma Awards: AI Film, Music Videos, and Games"
organization: "ElevenLabs"
winner: true
words: 765
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# Vibe Survivor

> A fast-paced geometry survival game built entirely with AI tools—code, art, and sound all generated through vibe-coding. A zero-experience creator bringing a full game to life using only AI.

[Devpost](https://devpost.com/software/vibe-survivor-hderg9) · hackathon [[Chroma Awards- AI Film- Music Videos- and Games]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** canvasapi, claudecode, codex, css3, elevenlabs, es6, html5, javascript, pixellab, vanilajs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what’s next for vibe survivor
- closing

## Body

Vibe Survivor Vibe Survivor – Project Story Inspiration Vibe Survivor began in June 2025, when I set out to learn how to build apps and games using only AI tools. I came from a non-software background, working in pharmaceutical supply chain, but I wanted to challenge myself: Could I create a full game from scratch using AI as my only development partner? That question became the heart of the project. The idea of “vibe-coding”—bringing my vision and energy while AI handled the technical execution—became the creative spark that drove everything forward. The result is a fast-paced geometry survival game where every line of code, every sound, and every pixel was generated through collaboration with AI. What It Does Vibe Survivor is a chaotic, action-focused survival game inspired loosely by the “Vampire Survivor” genre but with its own identity. Key features include: Dodge-based movement with an active dash mechanic Merge-style weapon upgrades that combine into powerful hybrid weapons Waves of geometric enemies with escalating difficulty Boss encounters that require precision, timing, and pattern awareness Everything—from weapon behaviors to enemy AI to hit detection to wave logic—runs on vanilla JavaScript , making the game accessible, lightweight, and fast. How We Built It The entire project was built exclusively with AI tools: Coding Workflow Claude Code Used for high-level planning, architecture design, debugging, conceptualization, and long-form reasoning. OpenAI Codex CLI (GPT-5.1 Codex) Used for execution-heavy tasks, generating large portions of the 13,000+ lines of JavaScript, and rapidly implementing features from structured plans. VS Code Used as the command center for reviewing AI-generated code, performing cleanup, and managing Git activity. This synergy—planning with Claude Code, executing with Codex—became the core development loop. The whole game grew in layers of iterative prompt cycles. Art Pipeline All visuals were produced using PixelLab AI , including: player and enemy sprites upgrade icons UI elements environmental visuals and effects Each asset was generated through prompts specifying size, style, and transparency. Audio Pipeline Every sound effect and all background music were created with ElevenLabs , including: weapon sounds dash effects item pick-ups boss alerts retro synthwave background tracks Technical Notes Projectile behavior, motion, and enemy tracking were built using vector math such as: [ \vec{d} = \frac{\vec{p} {\text{target}} - \vec{p} {\text{player}}}{\left| \vec{p} {\text{target}} - \vec{p} {\text{player}} \right|} ] AI assistance made it possible to understand, generate, and adjust these mechanics despite having no coding background. Challenges We Ran Into Building a full game with AI still required real problem solving. Major challenges included: Managing a single growing JavaScript file that reached over 13,000 lines Fixing logic bugs that cascaded through multiple systems Balancing enemy waves and boss fights, especially Boss #7 Keeping performance smooth as waves intensified Iterating art and sound assets until they matched the game’s tone Learning how to write prompts that guided AI effectively The development wasn’t automatic—it was a collaboration that demanded clarity, experimentation, and patience. Accomplishments We're Proud Of Building a complete, playable game as someone with zero prior coding experience Using AI alone to generate all code, sound, music, and visuals Creating full gameplay systems: dash mechanics, XP, upgrades, merges, bosses, and item trees Producing a highly polished project in just two months Turning AI tools into a functional, real-world development pipeline Submitting the finished game to the Chroma Awards The moment the game fully came to life—playable, fast, and fun—was a milestone I will never forget. What We Learned This project taught me: How to collaborate with AI as a true development partner How to structure ideas into executable plans How to debug with reasoning rather than technical expertise How game systems work under the hood How audio, visuals, and code can come together through AI How powerful the synergy between Claude Code and Codex CLI can be Most importantly, I learned that creative ambition combined with AI support can unlock skills far outside one’s background. What’s Next for Vibe Survivor The project is just getting started. Upcoming ideas include: Mobile builds (Android/iOS) using wrappers like Capacitor New weapons, merge paths, and bosses Expanded passive upgrade systems Difficulty modes and endless survival A global leaderboard with account login Optimization for smoother late-game performance A more detailed story and expanded visual world Vibe Survivor began as an experiment in AI-assisted creativity. Now it’s evolving into a long-term passion project with endless potential. Closing Creating Vibe Survivor has been one of the most exciting and creative journeys of my life. Built entirely through synergy with AI tools, this project represents what’s possible when imagination meets modern AI. Have fun, survive the chaos, and enjoy the vibe. Samson VibeCreAI <div