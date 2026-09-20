---
slug: "hardy-world-poker"
url: "https://devpost.com/software/hardy-world-poker"
title: "Hardy World Poker"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 951
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Hardy World Poker

> Hardy World Poker: Texas Hold'em mobile experience. Play against intelligent AI, climb global leaderboards, and compete across 6 world cities.

[Devpost](https://devpost.com/software/hardy-world-poker) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**domain** [[developer_tools]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[video_visual]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hardy world poker

## Body

Hardy World Poker Inspiration Hardy World Poker was inspired by the desire to create an immersive, multiplayer poker experience within Horizon Worlds. The goal was to build a fully-featured Texas Hold'em poker game that combines classic card game mechanics with modern UI/UX design, complete with persistent player statistics, leaderboards, and multiple buy-in tiers representing major cities around the world. What it does Hardy World Poker is a complete Texas Hold'em poker game featuring: Multi-tiered Buy-In System : Players can choose from 6 different cities with varying buy-in amounts (1K, 5K, 10K, 25K, 50K, 100K), each representing a major world city (Las Vegas, New York, London, Tokyo, Dubai, Monaco) Full Poker Gameplay : Complete Texas Hold'em implementation with betting rounds, blinds, side pots, all-in scenarios, and hand evaluation AI Opponents : Intelligent AI players with different personalities (Tight, Aggressive, Loose, Balanced) that make realistic decisions based on hand strength Persistent Statistics : Player stats are tracked and saved, including hands played, wins, losses, and chip counts Global Leaderboard : Top 10 players are ranked globally based on chip count, stored in world-level persistent storage Beautiful UI : Modern, Instagram-inspired design with smooth animations, gradient effects, and responsive layouts Loading System : Comprehensive loading screen that tracks initialization progress (images, data, player info) Crash Protection : Robust system to prevent chip loss if players exit unexpectedly How we built it The project was built using: TypeScript : Core game logic, state management, and AI decision-making NoesisGUI/XAML : UI framework for creating responsive, data-bound interfaces Horizon Worlds API : Network events, persistent storage, and world management Object-Oriented Architecture : Modular design with separate classes for: PokerOverlay : Main game controller and UI management PokerGameState : Game state management (players, pot, betting rounds) PokerActions : Hand evaluation and game controller logic PokerAI : AI decision-making with personality-based behavior ServerManager : Server-side logic for persistent storage and leaderboard management PokerImageLoader : Optimized parallel image loading with exponential backoff PokerTimer : Turn timer with countdown and expiration handling Key Technical Features : Pre-computed combination indices for fast hand evaluation (40-50% performance improvement) Dynamic AI delays based on decision complexity (40-60% faster turns) Lazy initialization of heavy objects for faster startup Debounced network events to reduce network spam Parallel image loading with retry logic Robust side pot calculation for all-in scenarios Type-safe chip management with validation Challenges we ran into Hand Evaluation Performance : Initially, recursive combination generation was too slow. Solved by pre-computing combination indices for 7-card and 6-card hands. Side Pot Calculation : Complex scenarios with multiple all-in players at different levels required careful algorithm design to correctly distribute pots. Chip Management : Preventing chip loss on unexpected exits required implementing a crash protection system with periodic syncing of effective total chips. AI Decision Making : Making AI players feel realistic while maintaining game balance required fine-tuning hand strength assessment and personality-based decision logic. Network Event Spam : Frequent saves were causing network congestion. Implemented debouncing to batch saves and reduce network calls by 60-80%. Type Safety : Ensuring chip values were always numbers (not strings) required careful validation throughout the codebase to prevent string concatenation bugs. Leaderboard Optimization : Limiting leaderboard to top 10 players while efficiently updating required careful threshold calculation and conditional updates. UI Responsiveness : Ensuring smooth animations and responsive layouts across different screen sizes while maintaining performance. Accomplishments that we're proud of Complete Poker Implementation : Successfully built a full-featured Texas Hold'em game with all standard rules and edge cases handled Performance Optimizations : Achieved significant performance improvements through algorithm optimization and lazy loading Robust State Management : Implemented reliable game state management that handles complex scenarios like multiple all-ins and side pots Beautiful UI/UX : Created an intuitive, visually appealing interface with smooth animations and clear feedback Persistent Data System : Built a reliable system for saving player stats, chips, and leaderboard data that survives world restarts AI Intelligence : Developed AI players that feel realistic and challenging without being predictable Crash Protection : Implemented a robust system to prevent data loss even if players exit unexpectedly Multi-tier Gameplay : Created an engaging progression system with different buy-in levels representing world cities What we learned Performance Matters : Pre-computation and caching can dramatically improve performance in computationally intensive operations like hand evaluation Type Safety is Critical : Careful type validation prevents subtle bugs like string concatenation instead of numeric addition Network Optimization : Debouncing and batching network events significantly reduces server load and improves user experience State Management Complexity : Poker game state management requires careful handling of edge cases, especially with all-in scenarios and side pots UI/UX Design : Creating intuitive interfaces requires balancing information density with clarity, and animations can greatly enhance user experience Persistent Storage Patterns : World-level vs player-level storage requires different strategies, and careful design prevents data loss AI Behavior Design : Creating believable AI requires balancing randomness with strategy, and personality traits add depth to gameplay What's next for Hardy World Poker Tournament Mode : Implement tournament-style gameplay with multiple tables and progressive elimination Player Customization : Allow players to customize their table themes, and card designs Achievement System : Add achievements and badges for various accomplishments (winning streaks, big pots, etc.) Social Features : Implement friend lists, private tables, and chat functionality Advanced Statistics : More detailed stats tracking including VPIP, PFR, aggression factor, and hand history Mobile Optimization : Optimize UI for mobile VR devices Sound Design : Add immersive sound effects and background music Tutorial System : Interactive tutorial for new players to learn poker rules Daily Challenges : Daily challenges and missions to keep players engaged Cross-World Leaderboards : Expand leaderboard system to track players across multiple world instances <div