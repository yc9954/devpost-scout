---
slug: "mathbombs"
url: "https://devpost.com/software/mathbombs"
title: "MathBombs"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 395
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/accessibility"
  - "substrate/video_visual"
---

# MathBombs

> Math game you can't win.

[Devpost](https://devpost.com/software/mathbombs) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[accessibility]]
**substrate** [[video_visual]]

**stack** react, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- what's next for untitled

## Body

Inspiration I’ve always enjoyed games that make learning fun and engaging. Classic typing games like TypeRacer inspired me, but I wanted to create something that sharpens mental math skills in a playful, visually appealing way. The idea of defending a village from falling bombs by solving math problems quickly felt like a perfect blend of excitement and education. I also wanted the game to be fully offline and accessible to everyone, anywhere. What it does MathBombs is an offline, single-page web game where players protect a village from falling bombs by solving math problems. Each bomb displays a math equation; typing the correct answer blasts the bomb before it hits the ground. Players have three lives (represented by hearts), and the game ends when all lives are lost. The game features a main menu with name input, level selection (Easy, Medium, Hard), and an adjustable bomb speed slider. The gameplay is fast, fun, and helps improve mental math skills. How I built it I built MathBombs using Vite, React, and Tailwind CSS for a fast, modern, and responsive experience. All game logic and assets are handled locally, so the game works completely offline. The UI is designed with floating modals and panels, using a custom color palette and provided image assets for bombs, blasts, hearts, village, and backgrounds. State management is handled with React hooks. Animations for falling bombs and blasts are implemented with CSS and JavaScript. Math problems are generated locally, and the game logic ensures smooth gameplay and instant feedback. Challenges we ran into Balancing difficulty: Designing math problems and bomb speeds that are challenging but not overwhelming for all levels. Ensuring smooth animations: Making sure bomb movement and blast effects are fluid across devices and browsers. Input focus management: Keeping the answer input always focused for fast-paced gameplay. Asset integration: Seamlessly integrating all provided images and ensuring they scale well on different screen sizes. Responsive design: Making the game look and play great on both desktop and mobile devices. What's next for Untitled Adding a leaderboard for local high scores. Introducing new types of math problems and power-ups. Adding sound effects and background music for a more immersive experience. Supporting multiplayer or challenge modes for friendly competition. Making the game even more accessible with keyboard-only and screen reader support. Packaging the game as a PWA for easy installation on any device. <div