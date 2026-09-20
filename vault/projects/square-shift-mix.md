---
slug: "square-shift-mix"
url: "https://devpost.com/software/square-shift-mix"
title: "Square Shift Mix"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 424
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Square Shift Mix

> Fast and addictive puzzle game where players place different shaped blocks on an 8×8 grid, chase high scores, unlock visual styles, and compete with friends on the leaderboard.

[Devpost](https://devpost.com/software/square-shift-mix) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** audio-components, custom-game-logic, javascript, leaderboard, lens-studio, screentransform-ui-system

## How they structured the write-up

- inspiration
- how it works
- what i built
- challenges
- what i learned

## Body

Inspiration Square Shift Mix was inspired by the viral block puzzle games that are very simple to understand but highly addictive to play. The goal was to recreate that style of game inside Lens Studio, focusing more on visual clarity, immediate response, and player feedback rather than building a complex game. How it works Players place blocks of different shapes on an 8×8 grid. When a row or column is completed, it clears with an animation and increases the score. If several clears happen in a row, a combo system activates, multiplying the points and encouraging players to think before placing pieces instead of doing it randomly. As the score increases, the visual style of the board changes dynamically, unlocking new themes during the same play session. This creates a very clear sense of progression and keeps the game visually interesting. A leaderboard is also included so players can compete with friends and try to beat each other’s scores, increasing replayability. What I built The main goal of this project was to create a complete game system inside Lens Studio: Custom grid and piece placement logic A ghost preview system to show where a piece can be placed before dropping it A combo-based scoring system inspired by modern puzzle games A dynamic theme system that updates all existing tiles in real time Smooth line clear animations using temporary ghost elements A “no moves left” detection system that avoids false game overs A complete game over sequence with animations, sound, vibration feedback, and leaderboard submission From a technical perspective, the project was organized into three main scripts: One script to manage the pieces (dragging, shape logic, and placement validation) One script for random spawning (generating a batch of pieces while avoiding duplicates and preventing impossible packs) One main script for the rest of the game systems (grid state, scoring, combos, theme changes, clears, game over flow, and leaderboard) Challenges One of the biggest challenges was managing all the states and timing inside Lens Studio. Coordinating piece placement, line clears, animations, scoring, and game-over checks without conflicts required careful control over when each system runs. Another challenge was making the game feel visually clear and easy to understand, so players always know why they gained points or why they lost without needing instructions. What I learned This project pushed me to treat Lens Studio like a small real-time game engine. I learned how to organize complex game logic, control timing and animations, and design clear visual feedback to create a polished and highly replayable experience. <div