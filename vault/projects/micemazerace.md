---
slug: "micemazerace"
url: "https://devpost.com/software/micemazerace"
title: "MiceMazeRace"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 512
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# MiceMazeRace

> Race your mouse to the finish by drawing its path! Dodge obstacles, brave tricky terrain, grab cheese, and challenge friends with custom-made mazes and tracks.

[Devpost](https://devpost.com/software/micemazerace) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**substrate** [[geospatial]] [[web_dom]]

**stack** cursor, devvit, elevenlab, phaser.js, typescript, warp

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for micemazerace

## Body

find the way out create map compete with other players What it does MiceMazeRace is a fast-paced maze and racetrack game where you guide mice by drawing their path. The faster you draw, the faster your mouse runs — but beware of tricky terrains, obstacles, and cheese that slows you down! Compete against ghost players, dodge hazards, fly off ramps, bounce off walls, and create your own tracks for others to play. 🎮 How to Play Draw a Path Start at the starting point (mouse’s initial position). End at the checker finish area . The faster your stroke, the faster your mouse will run. Navigate Terrains 🌿 Grass | Normal speed 🏖️ Sand | Slower movement 🦨 Mud | Very slow 🪨 Stone | Normal speed 💧 Water | Slippery steering Watch Out for Obstacles 🧀 Cheese : Your mouse grows bigger and slows down. ⬛ Walls : Block your path unless you find a way around. Use Special Items 🟩 Bouncy Wall : Collide and bounce back with force. 🟦 Ramp : Jump over walls or gaps for shortcuts. Race & Compete After drawing your path, watch your mouse run. Compare against ghost players (other players’ best runs). Aim for the shortest completion time! 🛠️ Track Editor Create your own custom maps with terrains, obstacles, and items. Share your creations so other players can try, race, and compete. 🏆 Game Rules The path must begin at the starting point and end at the checker finish area. Shorter time = higher score. Obstacles and terrain penalties apply to all players equally. Inspiration The map making mechanic is inspired by Flappy Goose. The idea of the game is inspired by classic Mouse Trap and classic top down racing game. While doing research I also found out that the game is similar to Draw Race 2 How we built it The map is built on top of Devvit Phaser template, with TypeScript and vanilla html css. AI-powered IDE like Cursor and Warp helped a lot in completing the project on time. Icons and graphics are created using Recraft and Google's ImageGen. Sound effects are created using ElevenLabs. Challenges we ran into Time constraint is the biggest challenge as I need to build the game from scratch in two weeks time, with only 1-3 hours everyday. Balancing speed vs. control, making terrains feel unique, handling collisions with obstacles, and ensuring the map editor was simple but flexible for creative players. Devvit is relatively new, which means the documentation will be updated frequently. Accomplishments that we're proud of We created a fun, intuitive control system where drawing feels natural, built a working level editor, and designed mechanics like cheese pickups that add both humor and strategy. What we learned Using Devvit to create UGC in Reddit is fun. This is also my first time using Phaser.js to build a game. What's next for MiceMazeRace More terrains and items (ice, conveyor belts, teleport pads) Mouse skins and cosmetic upgrades A community hub for sharing and rating tracks Notification/Auto comment if best record is broken Improved graphics <div