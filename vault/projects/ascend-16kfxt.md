---
slug: "ascend-16kfxt"
url: "https://devpost.com/software/ascend-16kfxt"
title: "Ascend"
hackathon: "Sky’s the Limit - Cloud9 x JetBrains Hackathon"
organization: "Cloud9"
winner: true
words: 502
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Ascend

> Fun in 5 seconds! Stack. Ascend. Compete!

[Devpost](https://devpost.com/software/ascend-16kfxt) · hackathon [[Sky-s the Limit - Cloud9 x JetBrains Hackathon]]

## Facets

**mechanism** [[benchmark_measured]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** javascript, react, three.js, vite

## How they structured the write-up

- 💡 inspiration
- 🕹️ what it does
- ⚙️ how i built it
- 🏆 fit for category: event mini-game

## Body

Ascend - Stack to the Stars 🌌 💡 Inspiration I wanted to capture the pure, adrenaline-fueled focus of classic arcade games but modernize it for the esports generation. The inspiration came from the desire to create the ultimate "queue-killer"—a game so simple you can learn it in a second, but so addictive you’ll lose track of time. I envisioned a game perfect for an event booth: high-energy, visually mesmerizing, and instantly competitive. I wanted players to feel that satisfying "snap" of a perfect move, rewarding precision with a sensory rush of sound and light. 🕹️ What it does Ascend is a rhythm-based 3D precision stacker. The Goal : Build the tallest tower possible by stacking moving blocks on top of each other. The Review : Any part of the block that overhangs the tower is sliced off, making the target smaller and the game harder. The Rush : Hitting "Perfect" placements triggers a satisfying synth harmonic and visual pulse. Stringing them together grows your block back, rewarding "flow state." The Glory : A local leaderboard tracks the top scores, instantly creating a competitive environment for anyone passing by. ⚙️ How I built it I prioritized performance and aesthetics to match the Cloud9/JetBrains brand of excellence. Core Engine : Built with React for state management and UI overlays. Visuals : Powered by Three.js . I used orthographic cameras and custom shaders/lighting to create a clean, "esports-ready" aesthetic with glassmorphism UI elements (Translucent, futuristic). Audio : I used Tone.js to create procedural audio. The music isn't a static loop; it evolves. As your combo increases, the synthesis engine generates higher harmonies, making the audio react dynamically to your skill level. Deployment : I engineered a unique build step that bundles the entire React+Three.js application into a single, portable game.html file . This means the game can run offline on any booth laptop or tablet without complex server setups or installation. 🏆 Fit for Category: Event Mini-Game Ascend was designed from the ground up to be the diverse attraction at a Cloud9 & JetBrains booth: Fast & Engaging (Speed) : Start-to-finish sessions take 30 seconds to 2 minutes. Instant restart mechanics ("Pop" animation on the Play button) encourage "just one more try." No load times. Intuitive & Accessible (Simplicity) : One-Button Control : Play with the Spacebar , a mouse click, or a touchscreen tap. Zero Learning Curve : If you can see the block moving, you know how to play. No tutorials needed. Thematic & Competitive (Hype) : Live Leaderboard : The integrated high-score system displays the top 10 runs right on the main screen. This naturally creates a "King of the Hill" dynamic at the booth, where fans compete to knock the current leader off the board. Visual Polish : The neon-on-dark visuals and smooth 60FPS animations fit perfectly with the high-tech vibe of a VCT or LCS event. Ascend isn't just a game; it's a competition in a bottle, ready to engage fans the moment they walk up to the booth. <div