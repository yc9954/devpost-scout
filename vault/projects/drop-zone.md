---
slug: "drop-zone"
url: "https://devpost.com/software/drop-zone"
title: "Drop Zone"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 622
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Drop Zone

> Tap, stop, survive! Take turns dodging obstacles and racing gravity to outscore your opponent.

[Devpost](https://devpost.com/software/drop-zone) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

  <sub>weak: deterministic_policy</sub>
**substrate** [[video_visual]]

**stack** javascript, lensstudio, ts

## Body

Inspiration We wanted to create a fun, competitive AR experience that brings friends together through Snapchat Spectacles. The idea came from classic arcade games where timing and reflexes are everything. We thought, what if we combined the thrill of a descending obstacle course with turn-based multiplayer, letting friends compete head-to-head in augmented reality? The result is a game that's easy to pick up but hard to master, perfect for quick competitive sessions. What it does Drop Zone is a turn-based multiplayer AR game for Snapchat Spectacles where two players take turns navigating a hanging character through an obstacle-filled descent. Players tap to start and stop their movement, carefully timing their way past obstacles while collecting points along the way. Each player gets 3 rounds (6 turns total), and the player with the highest score at the end wins! Key Features: Turn-based multiplayer gameplay via Snapchat's Connected Lenses Tap-to-move mechanic with precise timing controls Dynamic obstacle courses that reset each round Point collection system with finish bonuses Animated score counting and dramatic final verdict Immersive audio and haptic feedback Real player names fetched from Snapchat profiles How we built it We built Drop Zone using Lens Studio with JavaScript for all game logic. The architecture includes: Turn-Based System: Integrated with Snapchat's Turn-Based API for seamless multiplayer, handling session persistence, player switching, and game state synchronization Physics & Collision: Custom collision detection system for obstacles, collectible points, and finish line triggers Round Management: Modular round manager that activates different obstacle/point configurations per turn Animation System: Smooth score count-up animations using delta-time based incrementing Camera System: Dynamic camera follow with configurable smoothing for immersive gameplay Audio & Haptics: Layered sound effects and haptic feedback for satisfying game feel Challenges we ran into State Persistence: Managing game state across turns in a turn-based multiplayer environment was tricky. We had to carefully serialize/deserialize scores, turn counts, and round data between sessions. Collision Detection: Getting reliable collision detection for the hanging body across multiple colliders required building a recursive child-search system and handling both overlap and collision events. Player Name Fetching: Working with asynchronous player info APIs while ensuring fallback names display correctly if the data isn't available yet. Timing & Feel: Balancing the tap-stop delay, movement speed, and speed multipliers to make the game feel challenging but fair took many iterations. Accomplishments that we're proud of Polished Game Feel: The combination of animated scores, random result messages ("Nailed It!", "Crashed!"), audio cues, and haptic feedback creates a satisfying arcade experience Clean Turn-Based Flow: Seamless handoff between players with proper state management—no bugs or data loss between turns Scalable Architecture: The round manager system makes it easy to add new obstacle configurations without touching core game code First-Name Display: Personal touch of showing just the first name from players' Snapchat profiles makes it feel more intimate and fun What we learned Lens Studio's Turn-Based API: Deep understanding of session variables, turn management, and async player data fetching AR Game Design: Designing for Spectacles requires thinking about player comfort, timing, and visual clarity differently than traditional games State Machine Design: Building a robust game state system (IDLE → MOVING → PAUSED → WIN/GAME_OVER → TURN_END) that handles all edge cases Iterative Polish: Small details like score animations and random victory phrases make a huge difference in player satisfaction What's next for Drop Zone More Rounds & Obstacles: Expanding to more diverse obstacle types—moving platforms, rotating barriers, speed zones Power-Ups: Collectible items that grant shields, slow-motion, or bonus multipliers Leaderboards: Global leaderboards to compete beyond just your friend Custom Avatars: Let players choose different characters with unique animations Single Player Mode: Time attack mode for solo practice Themed Courses: Seasonal themes (Halloween, Winter, etc.) with unique visuals and obstacles <div