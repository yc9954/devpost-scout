---
slug: "junie-s-arcade"
url: "https://devpost.com/software/junie-s-arcade"
title: "JUNIE'S ARCADE"
hackathon: "Sky’s the Limit - Cloud9 x JetBrains Hackathon"
organization: "Cloud9"
winner: true
words: 1013
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# JUNIE'S ARCADE

> Three legendary challenges. One elite arena. Push your limits and claim your spot on the leaderboard.

[Devpost](https://devpost.com/software/junie-s-arcade) · hackathon [[Sky-s the Limit - Cloud9 x JetBrains Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** jetbrains, junie, next.js, phaser.js, postgresql, prisma, react, s3, tailwind, three.js, typescript, vercel, webstorm

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for junie's arcade

## Body

JetBrains WebStorm - Junie (JetBrains AI Coding Agent) | My credit remain when Use AI Pro My credit remain when Use AI Ultimate Main Page Gallery page Card on Gallery Leaderboard page Merchandise page Capture your moment with the Exclusive Merchandise from Timor-Leste Junie's Arcade - Devpost Submission Category: Category 4 - Event Mini-Game Live Demo: https://www.juniearcade.fun Repository: https://github.com/ajitonelsonn/Junie_Arcade Inspiration As a developer from Timor-Leste, I wanted to create something that brings people together through competition and fun. When I saw the Cloud9 x JetBrains hackathon Category 4 challenge -- build a mini-game for fans at LCS or VCT event booths -- I immediately imagined an arcade experience that captures the excitement of esports. The idea was simple: what if fans waiting at an event booth could compete in a quick tournament across multiple games, earn Champion Points, and see their name climb a live leaderboard? That's how Junie's Arcade was born -- named after JetBrains' AI Coding Agent that helped me build it. What it does Junie's Arcade is a 3-in-1 mini-game tournament platform designed for event booths. Players compete across three fast-paced games, each under 2 minutes: Jump Master (50 seconds) -- A platformer where players jump over bug obstacles, collect Cloud9 logos and coins, with progressive difficulty that increases speed every 10 seconds. Reflex Arena (50 seconds) -- A reaction game where players click good targets (stars, coins, gems, trophies) while avoiding bad ones (bugs, viruses, bombs). Features a combo system up to 5x and a reaction time bonus for clicks under 250ms. Memory Match (100 seconds) -- A card-matching puzzle with League of Legends and VALORANT champion cards. Players build combos by matching pairs consecutively, with bonuses for speed, accuracy, and perfect games. After each game, players receive a personalized Achievement Card they can download or share via QR code. The platform uses a Champion Points system to normalize scores across all three games and create a fair overall leaderboard. Players who complete all three games are ranked higher, driving engagement and encouraging fans to try every game. Top 3 players at GDC events win authentic Timor-Leste merchandise -- handwoven traditional bracelets and scarves -- connecting my culture to the global gaming community. How I built it I developed Junie's Arcade using JetBrains WebStorm with Junie (JetBrains AI Coding Agent) throughout the entire process. Junie helped me accelerate development by improving code quality, generating game logic, and creating comprehensive documentation. Tech Stack: Layer Technologies Framework Next.js 16, React 19, TypeScript Game Engine Phaser 3 3D Graphics Three.js, React Three Fiber, React Three Drei Styling Tailwind CSS 4, Framer Motion Database PostgreSQL with Prisma ORM Storage AWS S3 (achievement card images) Deployment Vercel Development Process: Planning -- Documented all ideas and tasks in the Idea_and_task_and_hackathon/ folder before writing any code Game Development -- Built three games using Phaser 3 with progressive difficulty systems, combo mechanics, and sound effects Backend -- REST API with API key authentication, rate limiting, input validation, and duplicate score prevention Achievement System -- Auto-generated personalized cards with player scores, country flags, random hero backgrounds, and QR codes for sharing Leaderboard -- Champion Points algorithm that normalizes different scoring ranges across games, with country filtering and real-time updates Art & Design -- Created all visual assets using Grok AI (mascot generation) and Canva (logos, game targets, achievement cards, merchandise designs) Art & Design Resources: Asset Tool Link Junie Mascot (AI-generated) Grok AI View Mascot & Logo Canva View Game Targets Canva View Merchandise Designs Canva View Game Cards Canva View Challenges I ran into Balancing three different scoring systems -- Each game produces vastly different score ranges. I solved this by creating the Champion Points system that converts raw scores into normalized rank-based points (1st place = 100 points, regardless of game). Progressive difficulty tuning -- Making games feel challenging but fair in under 2 minutes required extensive playtesting. Each game has carefully tuned difficulty curves that ramp up every 10 seconds. Session management -- Ensuring players can only play each game once per session while maintaining a smooth flow between games. Implemented localStorage-based session tracking with unique Player IDs generated per tournament run. Achievement card generation -- Rendering personalized cards with dynamic data (scores, ranks, country flags, random hero backgrounds) and making them downloadable/shareable via QR codes required combining HTML-to-image conversion with AWS S3 storage. Performance optimization -- Running Phaser 3 games within a Next.js React application while maintaining smooth 60fps gameplay, especially on the Reflex Arena's late-game chaos with 6-8 simultaneous targets. Accomplishments that I'm proud of Complete tournament experience -- Not just one game, but a full 3-game tournament with Champion Points, achievement cards, and a global leaderboard The Champion Points system -- A fair ranking algorithm that normalizes different scoring systems and rewards players who complete all three games Achievement cards with social sharing -- Personalized cards with QR codes that fans can save and share on social media Cultural connection -- Incorporating Timor-Leste merchandise as prizes, connecting my heritage to the global gaming community Comprehensive documentation -- Over 6 detailed documentation files covering gameplay, scoring mechanics, API reference, database schema, and system architecture with Mermaid diagrams Built with Junie -- Leveraged JetBrains' AI Coding Agent throughout development, demonstrating how AI tools can accelerate game development What I learned Phaser 3 game development within a Next.js/React environment -- handling game lifecycle, asset loading, and state synchronization between the game engine and React components Designing fair competitive systems -- How to create scoring mechanics that are balanced, progressive, and fun across different game types AI-assisted development workflow -- Using Junie in WebStorm to rapidly iterate on game mechanics, improve code quality, and generate documentation Event-oriented UX design -- Building for a booth context means prioritizing speed, instant engagement, and zero onboarding friction What's next for Junie's Arcade Daily/Weekly leaderboard resets for ongoing event competitions Additional mini-games to expand the tournament format Spectator mode for displaying live gameplay on booth screens Team tournaments where groups compete together for combined Champion Points Integration with Cloud9 & JetBrains event infrastructure if selected as the winning project <div