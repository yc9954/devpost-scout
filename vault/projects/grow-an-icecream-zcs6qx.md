---
slug: "grow-an-icecream-zcs6qx"
url: "https://devpost.com/software/grow-an-icecream-zcs6qx"
title: "CandyHunt!"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 721
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# CandyHunt!

> Scavenge hunt for candy while avoiding ice screams and exciting hazards! Multiplayer and multi-rounds friendly!

[Devpost](https://devpost.com/software/grow-an-icecream-zcs6qx) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**user** [[government_staff]]
**substrate** [[geospatial]] [[video_visual]]

**stack** ai, blender, meta

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for candyhunt!

## Body

Inspiration CandyHunt! began with a playful question: what if candy could chase you instead of you chasing it? The idea came from sketching silly concepts where desserts turned into enemies. The image of ice cream slimes slowly sliding toward the player, both funny and slightly menacing, became the heart of the design. The project was inspired by a desire to build something lighthearted but also flexible enough that anyone could customize it. The goal was not just to make a game but to create a system where round length, enemies, and collectables could be tuned without digging into code. What it does CandyHunt! is a round-based collection game where the player scrambles to pick up items while avoiding hazards and hungry slime-like enemies. Almost every element is editable. Round duration can be set in the Game Manager by simply typing in the number of seconds. Hazards can be tweaked so they either barely push the player or launch them across the map. Enemies can be adjusted in speed and in how much they slow the player on contact. Collectables are designed as empty mechanics that can be replaced with any prop, from chocolate bars to glowing crystals. Their total number is editable, so you can create short collection rounds with ten items or large hunts with hundreds. Quests and leaderboards are also flexible, making it easy to design new goals and scoring systems. Even the music can be swapped, so each round has its own atmosphere. How we built it The game was built around modularity. The Game Manager acts as the hub for timing and music, which means round settings can be changed in one place. Collectables were implemented as empty objects with collision mechanics layered on top. This allowed them to be swapped for any 3D prop without breaking functionality. Slime enemies were coded with a simple pursuit algorithm, but every critical variable such as speed, acceleration, and slowdown effect was exposed in the inspector. Hazards were given knockback physics that could be scaled to match the intended difficulty. During testing this sometimes resulted in absurd scenarios where a hazard would fling the player halfway across the level, which reinforced the importance of editable force values. Challenges we ran into Enemy balance was one of the biggest issues. The first slime prototypes were too fast, making rounds frustrating rather than fun. Allowing live adjustment of their speed solved the problem. Hazard physics were also difficult to stabilize, since early versions caused infinite bouncing against walls. Collectables initially broke when we swapped in a seasonal pumpkin model, so the system had to be rebuilt around empty mechanics to prevent prop-specific errors. Leaderboards and quests also conflicted at first, as score updates triggered quest events in loops. Rewriting the event system fixed that. Accomplishments that we're proud of We are proud of building a system that is not rigid but modular. Most of the game’s mechanics can be altered through inspector panels without editing scripts. The ice cream slimes turned from a joke sketch into enemies that are genuinely funny to watch and challenging to evade. The Game Manager makes round creation fast and intuitive. Most importantly, CandyHunt! feels like a toolbox where hazards, enemies, and collectables are pieces to be arranged, not fixed rules. What we learned The project reinforced the importance of exposing key variables. Letting designers directly change values like enemy speed, knockback strength, or round length made iteration faster and more creative. We learned that enemy balance is about creating tension rather than raw difficulty. We also discovered that modular architecture saves time when things break, since systems can be adjusted independently without collapsing the whole project. The experience shifted our perspective toward treating game design as building frameworks for others to extend, not just finished products. What's next for CandyHunt! Future work will expand the roster of enemies beyond slimes, such as sticky caramel blobs that trap players or gummy bears that multiply when hit. Hazards will evolve into interactive elements like collapsing cookie bridges or sugar rush boosts that temporarily increase speed. Quests will grow more complex, chaining multiple objectives into progressive challenges. The leaderboard will eventually support global competition rather than just local ranking. Difficulty scaling will be tied to math-driven formulas, such as exponential growth in enemy speed with each collectable gathered: <div