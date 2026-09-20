---
slug: "snake-speed-game"
url: "https://devpost.com/software/snake-speed-game"
title: "Island Dash"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 464
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Island Dash

> Island Dash is a fast-paced incremental racer. Dash across 4 islands, absorb Energite to get faster, discover secrets, and race others to prove you’re the fastest.

[Devpost](https://devpost.com/software/snake-speed-game) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** genai, horizon-worlds, meta, typescript, worlds-desktop-editor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- special thanks
- what’s next for island dash

## Body

Inspiration 3D Sonic games, Super Mario Odyssey, and Roblox-style speed simulators. What it does Core loop: Absorb Energite to level up and permanently increase your speed. Exploration: Each island hides collectible Stars. Stars boost how much speed you gain from Energite. Daily quests: Every day you get 3 new quests for a big Energite bonus. Races: Join timed races to earn Gems. The more players join, the more Gems you can win. Time trials: Beat parkour courses within a time limit to unlock extra Stars. Some trials require a certain speed. Cosmetics: Spend Gems on player trails. Trail Shops are hidden on the islands. Trails stay unlocked forever, but only one can be active. Progression: Increase your player level to unlock portals to the next island. There are a total of 4 islands with different environments to explore. How we built it We leaned heavily on GenAI to speed up world building: All terrains were generated with GenAI. We created seven islands with different prompts and settings, and used four of them as the main worlds. The world islands were generated as circular 150×150 terrains and then manually upscaled to feel bigger, while the tutorial and race islands use a rectangular layout. GenAI also helped with texture creation (e.g. wooden crates for time trials, wooden ocean bridge/decking). We generated ambient audio to quickly get a cohesive atmosphere. Music: All main tracks were self-composed by Dinco in GarageBand. Only the race celebration track is copyright-free third-party music. Challenges we ran into World capacity limits (especially vertex count) make large, explorable maps tricky. The GenAI generated ocean didn’t come with an even height, so we had to adjust and re-place parts of the world accordingly. Getting all mechanics to work reliably in a multiplayer setting was challenging. Accomplishments we’re proud of We designed the Tutorial Island to get players into the core loop in under 20 seconds, with clear instructions right at spawn. Players start to have fun and know what to do immediately. We’re proud of the overall look & feel. The islands feel alive and worth exploring, and the UI is colorful and easy to read. We managed to take GenAI generated terrain and polish it so it actually works for gameplay, not just as a visual demo. What we learned How to get the most out of the different GenAI tools. Some of them are amazing, while others produce meshes with way too many vertices. How to build great-looking camera animations. Special thanks Thanks to these creators for their shared community assets, which we used in this project: Winning Celebration by natashagubernov (we swapped the music and extended the scripting logic) Bouncy_clouds by ShaneShameless What’s next for Island Dash More island worlds and race tracks Animated race obstacles Rebirth / Prestige system <div