---
slug: "nova-legends"
url: "https://devpost.com/software/nova-legends"
title: "Nova Legends"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 391
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Nova Legends

> Dominate the legends arena in this 2D top-down multiplayer shooter where medieval combat is redefined by tactical precision. Powered by our own 100% custom-made engine all built from scratch.

[Devpost](https://devpost.com/software/nova-legends) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[geospatial]] [[video_visual]]

**stack** java, socket, vultr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for nova legends

## Body

Inspiration We wanted to revisit the classic medieval genre but with the mechanical intensity of a modern top-down shooter. The goal was to create a competitive arena where skill and positioning matter more than stats, all while proving that a custom-built engine can deliver a tighter, more specialized experience than a generic one. What it does Nova Legends is a multiplayer 2D top-down shooter where players compete to become the ultimate knight. It features ranged and close combat, real-time chatting, and a map generator. Every sword slash, movement, and interaction is handled by our internal services to ensure the gameplay feels good, fun and responsive. How we built it The project is powered by our 100% custom-made engine. Rather than using pre-built software, we engineered every core service from scratch: Physics & Animation: A custom physics engine and custom animation service designed specifically for 2D top-down games. Camera System: A dual-mode camera featuring Focus Mode for precision combat and Unfocused Mode for map awareness. Audio & UI: Implementation of Spatialized Sounds for directional cues and a custom UI framework, including a native chat service. Networking & Deployment: The multiplayer architecture follows a Server-Authoritative model deployed on Vultr cloud servers. To ensure absolute synchronization and game integrity, the server handles all core logic and physics calculations. The clients function as streamlined interfaces, focused on capturing player inputs and rendering high-fidelity visual feedback based on the server's real-time data. Challenges we ran into Building a "from scratch" engine meant we couldn't rely on built-in tools for networking or collision. Synchronizing Online Multiplayer and ensuring the Custom Physics remained consistent across different clients was a major challenge. Accomplishments that we're proud of We are incredibly proud of the seamless integration of our custom services. Seeing the Scoreboard, Chat, and Physics engine work in harmony on a live Vultr server was a huge milestone. Successfully implementing a spatialized sound system and a custom map generator within our own ecosystem were also major technical wins. What's next for Nova Legends We built a solid foundation. Next, we plan to develop the Map Generator with more biomes, introduce a variety of medieval projectile types (fire-arrows, throwing axes, ...), and refine the Animation Service for even smoother character states. The ultimate goal is to scale the server architecture to support a massive "Battle Royale" style game mode. <div