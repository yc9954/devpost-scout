---
slug: "leap-craft"
url: "https://devpost.com/software/leap-craft"
title: "Leap Craft"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 445
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
---

# Leap Craft

> LeapCraft: Create challenging platform levels, play others' creations, then modify them with your own twist in this collaborative game of HORSE community challenge.

[Devpost](https://devpost.com/software/leap-craft) · hackathon [[Hack Reddit 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]

**stack** devvit, phaser.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for leapcraft

## Body

Inspiration The inspiration for LeapCraft came from classic platformer level editors and the game of HORSE in basketball, where players take turns mimicking increasingly difficult shots. I wanted to create a collaborative game-building experience where the community continually evolves levels through a chain of creative modifications. What it does LeapCraft is a platform game creator with a twist: players can create levels from scratch or modify existing ones in a game of HORSE. HORSE mode: Each round, players try to complete the current level. Once enough completions occur, a new round begins with one player's modifications becoming the new challenge. This creates an evolving game that gets progressively more creative as the community contributes. Leve creator: Create a level with platforms, hazards, and interactive elements, submit it for others to play. Play someone else's created levels and beat it How I built it LeapCraft was built using: React for the UI components and state management Phaser.js for the game engine and physics Mantine for UI components with a pixel art aesthetic Devvit API for Reddit integration and data persistence Custom event system for communication between React and Phaser The architecture separates the game logic from the UI, allowing seamless transitions between play and edit modes. Redis is used to store level data, player statistics, and round progression information. Challenges I ran into Component boundaries : Managing state between React and Phaser required careful planning. I implemented an EventBus system that bridges the gap between these systems. Physics quirks : Getting platformer physics to feel right was surprisingly difficult. Issues with player sticking to moving platforms, reliable collision detection, and jump mechanics required extensive testing. Game persistence : Tracking user modifications and ensuring fair progression through rounds meant designing a robust state management system with appropriate permissions. Horse game logic : Implementing the round progression system with proper validation required careful tracking of players and their edits. Accomplishments that I am proud of Creating a full platformer game engine with level editor in a short timeframe Implementing collision detection and responsive controls Building an intuitive editor with visual component placement and configuration Designing a collaborative game structure that encourages creativity Successfully integrating with Reddit's API for community features What I learned This project deepened my understanding of: Game physics and collision systems in browser environments State management across disparate systems (React + Phaser) UX considerations for creative tools Community-driven content creation systems Optimizing real-time interactions in web applications What's next for LeapCraft More component types (enemies, checkpoints, power-ups) Enhanced visual themes and customization Level sharing and voting systems Player leaderboards and achievements Time trials and speedrun features Mobile support for playing (if not editing) levels <div