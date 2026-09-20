---
slug: "nine-legends-pro-qp9o74"
url: "https://devpost.com/software/nine-legends-pro-qp9o74"
title: "Nine Legends Pro"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 803
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/legal_justice"
---

# Nine Legends Pro

> Nine Legends brings the classic strategy of Nine Men’s Morris to Snapchat with AR, haptics, Bitmoji, and smart AI. Play friends or train solo in a premium social gaming experience.

[Devpost](https://devpost.com/software/nine-legends-pro-qp9o74) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[legal_justice]]

**stack** aimode, audioinstructions, bitmoji, leaderboard, lensstudio, turnbasedgame

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nine legends pro

## Body

Game Title Game Instructions Play with AI Game Mode Play with Friends (Turn Based Game) Leaderboard & Game Restart functionality Nine Legends Pro: Project Summary Inspiration Nine Men's Morris is one of the oldest strategy games in history, dating back to the Roman Empire. Our inspiration was to modernize this ancient classic for the AR era on mobile. We wanted to transform a simple wood-and-stone board game into a dynamic, personalized experience directly within the Snapchat app. By integrating Bitmojis and asynchronous multiplayer, we aimed to bridge the gap between historical gameplay and modern social interaction on smartphones. What it does Nine Legends Pro is a high-fidelity AR digital version of "Nine Men's Morris" optimized for the Snapchat experience. Strategic Board Play: Players compete on a 24-point grid, placing and moving nine "Legends" (coins) to form mills (rows of three) in the game. Mill Mechanics: Forming a mill allows a player to capture an opponent's piece, with the goal of reducing the enemy to just two pieces or blocking all their moves. Game Modes: Single Player: Face off against a sophisticated AI with three difficulty levels ( Easy , Medium , Hard ). Multiplayer: Play locally or challenge friends across the globe using Snap's Turn-Based API . Multimodal Guidance: Comprehensive onboarding through both Textual Instructions on-screen and synchronized Audio Guidance , ensuring players understand the rules and their next moves instantly. Social Competition: Integrated Global Leaderboard allow players to track their wins and compete for the top spot among friends and global "Legends." Personalized Visuals: Real-time Bitmoji integration represents players on the board, with dynamic avatars that react to the game state. Immersive Feedback: Features smooth mobile-optimized animations, glow-indicators for valid moves, spatial audio, and haptic feedback. Smart Move Suggestions: In the movement phase, the system analyzes board state in real time and highlights all valid destinations when a coin is selected. How we built it Engine: Built using Lens Studio 5.15.3 , utilizing the latest AR capabilities available on modern iOS and Android devices. Logic: Developed a complex game engine in JavaScript , handling board state management, mill detection, and AI decision-making. AI Strategy: The AI uses a weighted priority system ( PLACEMENT_PRIORITY ) to value intersections and strategic hubs over corners, creating a challenging opponent even at "Medium" difficulty. Multiplayer Sync: Leveraged the Turn-Based API to serialize board states into JSON payloads, allowing for seamless cross-session play between Snapchat users. Instruction System: Developed a state-aware instruction manager that triggers specific audio cues and textual overlays based on the game phase (Placement vs. Movement) to guide the player's journey. Social Loop: Utilized Snap's API to implement global and friend-based leaderboards, encouraging repeat play and healthy competition. Move Suggestion Engine: Implemented a rule-based validator that detects all legal moves during the movement phase and visually highlights them when a coin is selected. UI/UX: Implemented a premium UI system with dynamic scoreboards designed for vertical mobile screens. Challenges we ran into State Serialization: Managing the synchronization of 24 board positions, multiple game phases (Place, Move, Remove), and player-specific data across asynchronous turns required a robust custom serialization/deserialization logic. Visual Glitches: We encountered "ghost coins" where pieces would briefly overlap during fast-paced movement animations. This was resolved by implementing a strict state-lock and animation-callback system. Mobile AR Optimization: Ensuring that complex spatial audio and instruction triggers worked reliably across a wide range of mobile hardware required significant debugging and fine-tuning of AudioComponent behaviors. AI Reset Logic: A subtle bug where AI states wouldn't fully reset when switching between Multiplayer and Solo modes required a complete overhaul of the game's initialization sequence. Accomplishments that we're proud of Robust Multiplayer: Successfully implemented a full-scale board game that maintains perfect state across days-long social matches. Accessibility & Onboarding: Created a dual-modality instruction system (audio/text) that makes an ancient strategy game easy for anyone to pick up and play in seconds. Competitive Infrastructure: Built a working leaderboard system that turns a classic board game into a global competition. Responsive AI: Created an AI opponent that feels "human" and provides a genuine challenge without feeling unfair. What we learned AR Social Loops: We learned how to design turn-based interactions that encourage social engagement through the "Send Snap" flow. API Depth: Gained deep expertise in Snap's MultiplayerManager and TurnBasedManager APIs, including handling edge cases like spectators and full-room notifications. Performance Budgeting: Learned the importance of optimizing script execution and asset analysis to maintain a high frame rate in complex AR scenes on mobile. What's next for Nine Legends Pro Customizable Boards: Allowing players to unlock new board skins, 3D environments, and personalized coin materials. Voice-Activated Moves: Exploring the use of Voice ML to allow hands-free gameplay for a more immersive Lens experience. Social Emotes: Adding the ability for Bitmojis to perform "celebration" or "defeat" emotes based on the game's outcome. <div