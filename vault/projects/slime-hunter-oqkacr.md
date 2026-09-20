---
slug: "slime-hunter-oqkacr"
url: "https://devpost.com/software/slime-hunter-oqkacr"
title: "Slime Hunter"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 455
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Slime Hunter

> Slime Hunter: A roguelike in Horizon Worlds where 50+ slimes chase players, with buffs, bosses, and endless replayability

[Devpost](https://devpost.com/software/slime-hunter-oqkacr) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets


**stack** typescript, worldeditor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for slime hunter

## Body

Inspiration Slime Hunter was inspired by classic roguelike games, particularly Brotato and Monster Survive . While developing Hunter Quest link , we realized Horizon Worlds’ performance limits were worth challenging. Our goal was to deliver a vertical‑screen roguelike experience with true randomness and progression. By unleashing massive waves of monsters to chase the player, we sought to create stronger pressure and immersion, echoing the fast‑paced, wave‑based combat that defined our inspirations while pushing the boundaries of the platform. What it does Players take the role of Slime Hunter , using bows and crossbows to fight waves of slimes. After each wave, they receive 3 random buffs and can choose 1 to upgrade. With more than 50 buff options , players can build diverse playstyles. Over 50 monsters can chase the player simultaneously, creating intense and thrilling combat loops. How we built it Used Worlds Desktop Editor to build the project framework VSCode for coding Blender for model optimization and creation Maya for character animations Unity to generate AssetBundles Photoshop for textures AI to solve coding issues and generate textures I created a 3D lobby where players can check leaderboards and tasks, and access my other recommended worlds. Walking into the slime cave starts the game. The combat system is complete: players fight with bows or crossbows, and after each wave they can upgrade once. My previously published Buff system plugin was integrated quickly. In addition, I added daily login rewards, a store, and a skin shop . Challenges we ran into The biggest challenge was performance when 50+ dynamic enemies chased the player simultaneously, especially advanced ones firing projectiles Pathfinding lag : Horizon’s NavAgent lagged with 10 enemies. Reduced animation overhead: slimes use only 1 bone, all share one animation set Compressed AssetBundle: 10 slime types total only 2MB Replaced NavMesh with math-based logic, adding algorithms to prevent overlap Model switching lag : Switching all enemy models at once caused stutter. Even frame refresh couldn’t fix it. I solved this by hiding model switching during buff selection, making the process seamless. These optimizations allowed us to achieve stable gameplay with 50+ monsters chasing the player . Accomplishments that we're proud of We successfully achieved stable gameplay with 50+ monsters chasing the player simultaneously , showcasing a major technical breakthrough in Horizon Worlds. Combined with randomized buffs and progression, Slime Hunter delivers the core roguelike experience of randomness, growth, and replayability. What we learned We realized that true creativity often emerges from constraints. By treating optimization as both a technical and design challenge, we unlocked new ways to enhance gameplay. What’s next for Slime Hunter Currently, the mode is single-player, but our goal is to support 1–5 players. Multiplayer testing will be our next step. <div