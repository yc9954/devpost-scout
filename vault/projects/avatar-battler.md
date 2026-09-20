---
slug: "avatar-battler"
url: "https://devpost.com/software/avatar-battler"
title: "Avatar Arena"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 891
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
---

# Avatar Arena

> Avatars attack! Battle your friends in this turn-based combat simulation game. https://www.reddit.com/r/AvatarsArena/comments/1ojnnxn/avatar_arena/

[Devpost](https://devpost.com/software/avatar-battler) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]

**stack** devvit, express.js, javascript, kiro, kiro-ai, leantween, node.js, reddit, redis, typescript, unity, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- core game systems
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next
- 🔗 links

## Body

Avatar Arena A Reddit-integrated turn-based battle game built with Unity + Devvit ▶ Play Now on r/AvatarsArena Inspiration Reddit’s avatar community (like r/AvatarTrading ) is one of the most creative corners of the platform — full of users showing off, customizing, and trading their digital identities. We wanted to turn that energy into something interactive: what if you could actually battle using your Reddit avatar? Avatar Arena was born from that question — combining community identity, creative expression, and game design into a quick, satisfying turn-based experience built entirely for Reddit. What It Does Avatar Arena lets Redditors bring their avatars to life and fight community opponents. Each enemy is a real Reddit user — artists, staff, and known accounts from across the site. Players can: ⚔️ Battle across 3 difficulty levels (Easy / Medium / Hard) 💰 Earn XP and gold from victories 🧩 Level up to boost stats and unlock stronger attacks ⚡ Use the SP (Strategic Points) system to unleash special moves 🧠 Preview and reroll enemies , viewing their stats and rewards 🧍‍♂️ Fight real Reddit avatars — pulled directly from Reddit’s API Every match is quick, strategic, and personal — your Reddit identity becomes your fighter. How We Built It 🎮 Frontend (Unity WebGL) Built the battle system and UI in Unity Integrated LeanTween for smooth animations and timing Designed a responsive, mobile-friendly layout optimized for Reddit embeds Added dynamic damage text , turn indicators , and attack feedback for polish 🌐 Backend (Devvit + Express.js + Redis) Devvit powers Reddit authentication and avatar retrieval Express.js server handles battle logic, XP, and persistence Redis stores user progression, stats, and gold Implemented retry logic with exponential backoff to prevent authentication failures (401s) from interrupting gameplay 🤖 AI-Accelerated Development (Kiro) We developed alongside Kiro , an AI coding assistant that served as our “pair programmer.” Kiro helped us: Scaffold and debug Unity ↔ JS ↔ Node.js communication layers Auto-generate API test panels and mock data systems Iterate rapidly on battle balance and difficulty curves Generate and format documentation Kiro became an integral co-developer throughout the hackathon — accelerating iteration while letting us focus on creativity and balance. Core Game Systems ⚔️ Battle Mechanics 4 Actions: Attack, Defend, Special, Heal SP (Strategic Points) govern special moves Balanced pacing for 3–7 turn battles Randomized damage adds variety to each round 🎚️ Difficulty System Easy / Medium / Hard modes affect: Enemy HP and attack power Gold and XP rewards Risk level indicators (Low / Balanced / High) Reroll system for new opponents 🧍‍♀️ Player Progression Persistent stats via Redis: level, gold, XP Level-ups increase HP, SP, and attack stats Gold can be spent on upgrades in future updates 🖼️ Avatar Integration Pulls Reddit avatars directly from the Reddit API Implements cache-busting for up-to-date visuals Supports fallback for users without custom avatars Real-time avatar swapping in battles and menus Challenges We Ran Into 🔧 Technical Integration Challenges Unity ↔ JavaScript ↔ Server Communication Creating a seamless three-layer communication system required precision. We learned to handle UTF8ToString conversions carefully and standardize naming conventions to avoid data mismatches. Authentication & Session Management Expired JWT tokens occasionally broke the flow — we solved it by adding transparent retry logic with exponential backoff. The player never sees an error; it just works. ⚔️ Game Balance & Pacing Our first battles dragged on for up to 12 turns! Through iterative tuning, we refined formulas until we hit the sweet spot: Easy: 3–4 turns Medium: 4–6 turns Hard: 6–8 turns 🎨 UX and Animation Flow Coordinating animations, text feedback, and UI transitions without overwhelming the player took fine-tuning. We learned that animation timing and easing can make or break immersion. 📊 Data Architecture We decided to curate 65+ “real Reddit users” as enemies — recognizable avatars that feel meaningful to battle. Curated content provided a stronger connection than procedurally generated foes. Accomplishments We’re Proud Of 🚀 Fully playable MVP deployed directly on Reddit 🎮 Integrated Unity WebGL + Devvit + Redis into one ecosystem 👥 65+ curated community avatars as opponents 🧠 Balanced, responsive, mobile-friendly gameplay 🤖 Successfully used Kiro AI for full-stack collaboration — from idea to polish What We Learned We learned that community-first design is key to Reddit-based projects — and that AI can be a true co-pilot when managed thoughtfully. From a technical perspective: AI collaboration + version control = power combo. Kiro was used for everything : scripting, testing, iteration, debugging, and documentation. Iterative balance > theoretical optimization. Real playtesting led to better pacing than formulas did. Error handling is part of UX. Retry logic and fail-safes improved experience more than any new feature. Platform constraints drive creativity. Devvit’s sandbox pushed us to find elegant, minimal solutions. In short: AI helped us think faster — but design discipline kept the project human. With good version tracking and human review, tools like Kiro can be essential for future hackathon-scale projects. What’s Next 🧩 Inventory system & item shop 🏆 Player-vs-Player battles 🧑‍🤝‍🧑 Community tournaments and leaderboards 🪄 Special events for Reddit avatar artists 📱 Full mobile optimization We’re excited to keep expanding Avatar Arena into a fully community-driven experience — a game built by Redditors, for Redditors. 🔗 Links Play now: https://www.reddit.com/r/AvatarsArena/ Built for: Community Games 2025 Hackathon Tech Stack: Unity WebGL · Devvit · Express.js · Redis · TypeScript · LeanTween <div