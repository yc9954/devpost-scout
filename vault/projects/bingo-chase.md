---
slug: "bingo-chase"
url: "https://devpost.com/software/bingo-chase"
title: "Bingo Chase"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 931
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Bingo Chase

> Compete in exciting multiplayer Bingo Chase matches with unique patterns, XP progression, and leaderboards in Horizon Worlds via Mobile!

[Devpost](https://devpost.com/software/bingo-chase) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[video_visual]]

**stack** typescript

## How they structured the write-up

- what i learned
- how i built it
- challenges faced

## Body

Bingo Chase was born from a desire to bring the classic, social experience of Bingo to Mobile in a NEW WAY! Traditional Bingo games are often passive—you sit, listen, and mark numbers. I wanted to transform this into an active, engaging experience where players physically move through a 3D space to collect numbered balls, making every game feel like an adventure. The inspiration came from watching people play games in Horizon Worlds and noticing how physicality makes even simple activities more engaging. Combining the strategic pattern-matching of Bingo with immersive movement mechanics created something entirely new—a game where skill, speed, and spatial awareness matter just as much as luck. What I Learned Building Bingo Chase taught me invaluable lessons about reactive programming , multiplayer architecture , and performance optimization . Reactive UI Architecture The Horizon Worlds framework uses a reactive binding system similar to React, where UI updates automatically when data changes. I learned to design with Binding and AnimatedBinding objects, creating a clean separation between game state and presentation. This meant implementing a centralized BingoGameStateManager that manages 60+ bindings for everything from called numbers to popup animations. Multiplayer Network Synchronization Coordinating game state across multiple players in real-time was fascinating. I implemented a custom network event system ( BingoNetworkEvents ) to handle player ready states, ball calls, win conditions, and pattern selections. The challenge was ensuring all players see the same game state simultaneously while handling network latency gracefully. Performance Optimization in VR I learned to optimize animations, reduce binding recalculations through caching, and batch UI updates. The countdown screen animations were particularly challenging—I had to reduce animation durations and simplify effects multiple times to maintain smooth performance. TypeScript Architecture I developed a modular architecture where each class lives in its own module, following clean separation of concerns. The codebase includes specialized managers for screens, game state, win conditions, patterns, audio, camera effects, and more—each handling a specific responsibility. How I Built It Bingo Chase is built with TypeScript using the Horizon Worlds API , featuring a multi-layered architecture: Core Systems Game Logic Layer: BingoGameStateManager - Centralized state management with reactive bindings BingoWinConditions - Pattern matching and win validation (10 different patterns) BingoCardGenerator - Algorithmic card generation ensuring valid Bingo cards BingoCaller - Number calling system with proper Bingo ball distribution VR Interaction Layer: BingoBallSpawner - Spawns 75 physical balls in 3D space using navmesh placement BingoPlayerInput - Handles Player Input interactions and ball collection BingoCameraEffects - Dynamic camera effects for running, jumping, and landing UIArrow - 3D arrow pointing players toward collectible balls UI/UX Layer: BingoScreenManager - Manages transitions between lobby, countdown, game, and stats screens BingoLobby - Player ready system and navigation BingoGameScreen - Interactive Bingo card with real-time updates BingoCountdownScreen - Animated countdown with pattern display BingoPopupManager - Ball collection feedback and winner announcements Multiplayer Layer: BingoNetworkEvents - Centralized network event definitions XPManagerServer/Client - Persistent XP and progression system LeaderboardsManager - Player ranking and statistics Progression System: Unlimited XP levels with exponential scaling Pattern-based XP rewards (easier patterns = less XP, harder = more) Persistent player stats across sessions Leaderboard tracking Technical Highlights The game features 10 unique Bingo patterns (Any Line, Four Corners, Letter X/T/L, Diamond, Postage Stamp, Outer Edge, Plus Sign, Full Card), each with different difficulty levels and XP rewards. Players physically move through the VR world to collect numbered balls, making strategic decisions about which balls to prioritize. The UI is fully reactive—when a number is called, all players' cards update instantly. The system uses AnimatedBinding for smooth transitions and Binding.derive() for computed values like "can call Bingo" states. Challenges Faced 1. Circular Dependencies Early in development, BingoLobby and LocalPlayer created a circular import dependency, forcing both modules to compile simultaneously at world start. I resolved this by extracting interfaces and using dependency injection patterns, though some architectural coupling remains due to framework requirements. 2. Performance Maintaining high FPS with complex UI animations and 75+ physical objects was difficult. I implemented several optimizations: Animation caching via AnimationCache to reuse animation objects Binding caching to avoid recalculating derived values Reduced animation durations (cut countdown animations from 400ms to 150-300ms) Simplified visual effects while maintaining polish 3. Multiplayer State Synchronization Ensuring all players see consistent game state required careful event ordering. Network events for ball calls, wins, and player states needed to be broadcast reliably and processed in the correct order. I implemented a queue system for uncollected balls and validation checks to prevent race conditions. 4. Ball Spawning at Scale Spawning 75 physical balls with physics simulation could cause performance issues. I implemented staggered spawning with delays, navmesh validation to ensure proper placement, and error handling for failed spawns to prevent the system from getting stuck. 5. Pattern Validation Complexity Validating win conditions for 10 different patterns required creating a flexible grid-based system. The BingoWinConditions class uses boolean grids to represent patterns, allowing for easy extension and validation. The challenge was making it performant while supporting complex patterns like "Diamond" (13 cells) and "Outer Edge" (16 cells). 6. Reactive UI Performance With 60+ bindings updating frequently, I had to be strategic about which values derive from others and which are cached. The BingoGameStateManager maintains separate cached values for performance-critical paths (like checking if a player can call Bingo) while still using reactive bindings for UI updates. Master Bingo Chase represents months of iteration, testing, and refinement. It's a complete multiplayer game with progression systems, leaderboards, and polished UX—all built to run smoothly in the demanding VR environment. The result is a game that transforms a classic pastime into an active, engaging VR experience. <div