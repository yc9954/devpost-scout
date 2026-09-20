---
slug: "stonefall"
url: "https://devpost.com/software/stonefall"
title: "Stonefall"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 638
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Stonefall

> Get yourself on the Grid through skill and patience.

[Devpost](https://devpost.com/software/stonefall) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[structured_db]] [[video_visual]]

**stack** react, react-three-drei, react-three-fiber, redis, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stonefall

## Body

Custom Devvit Blocks with stats and achievements Start of Gameplay Grid View Inspiration Stonefall originally got it's inspiration from Jenga but soon transformed into a more classic stacking game like Tetris and Stack. The game was designed specifically for Reddit's Devvit platform, with a focus on the social sharing and community aspects that make games viral on Reddit. The visual style is inspired by Tron's neon aesthetic with clean, minimalistic 3D blocks and glowing effects. What it does Stonefall is a precision-based 3D tower stacking game where players must master both position AND rhythm. Here's how it works: Core Mechanic: Blocks slide in 2 directions across the screen Challenge: Players must tap at the perfect moment to align the position with the tower below Scoring: Points are awarded for successful placements, with bonuses for perfect position alignment, adding massive multipliers for achieving perfection Social Integration: Built on Reddit's Devvit platform, allowing players to share their towers, compete on leaderboards, and view other players' creations in a shared 3D world How we built it Technology Stack: Frontend: React with @react-three/fiber for 3D rendering using Three.js 3D Graphics: Three.js with custom shaders, post-processing effects (bloom, outline), and optimized instanced rendering Backend: Node.js/Express server running on Reddit's Devvit platform Database: Redis for real-time leaderboards, game sessions, and tower placement data Key Technical Features: Performance Optimization: Instanced mesh rendering, object pooling, and adaptive quality settings 3D Tower World: Spatial placement system allowing players to explore others' towers in a shared grid Visual Effects: Tron-inspired neon outlines, particle effects, and post-processing for polished presentation Challenges we ran into Platform Constraints: Redis limitations: Needed careful data structure design for efficient leaderboards and tower storage Technical Challenges: Deterministic Simulation: Achieving perfect parity between client preview and server verification across different devices and browsers Performance Optimization: Rendering hundreds of 3D boxes while maintaining 60fps on mobile devices and creating a seamless 60fps gameplay experience across different devices and hardware 3D Spatial Placement: Creating an intuitive system for placing towers in shared 3D space Game Design Challenges: Social Features: Designing leaderboards and tower sharing that encourage engagement without toxicity Accomplishments that we're proud of Technical Achievements: Advanced 3D Rendering: Created a polished Three.js experience with custom shaders, post-processing, and optimized performance Scalable Architecture: Built a system that can handle concurrent players and tower placements Game Design Wins: Visual Polish: Achieved the Tron-inspired aesthetic with glowing outlines, particle effects, and smooth animations Social Integration: Successfully integrated with Reddit's platform for seamless sharing and community features Platform Integration: Reddit Native: Built specifically for Devvit Performance: Optimized for Reddit's mobile app environment with adaptive quality settings Viral Mechanics: Designed sharing and leaderboard features that encourage organic growth What we learned Technical Insights: 3D Web Performance: Advanced techniques for optimizing Three.js applications, including instancing, LOD systems, and shader optimization Platform Constraints: How to work within strict platform limitations while still delivering rich experiences Game Design Lessons: Social Mechanics: The power of spatial tower placement in creating emergent social interactions Visual Communication: The critical importance of clear visual feedback for precision timing games Mobile-First Design: Optimizing for touch controls and small screens without sacrificing gameplay depth Development Process: Iterative Design: The value of rapid prototyping and continuous playtesting for fine-tuning game feel Performance Budgets: Setting and maintaining strict performance targets for web-based 3D games What's next for Stonefall Immediate Roadmap (Phase 1): Fixing bugs and creating smooth gameplay on lower end devices Tournament System: Scheduled competitions with special rewards and recognition Advanced Analytics: Detailed player statistics and improvement tracking Spectator Mode: Watch replays of top players with cinematic camera angles Anti-Cheat: Deterministic system for server verification of created towers Medium-term Features (Phase 2): Global Leaderboards: Cross-subreddit competition and seasonal rankings Custom Themes: Player-customizable visual themes and block styles Long-term Vision (Phase 3): User-Generated Content: Custom block shapes, themes, and game modes <div