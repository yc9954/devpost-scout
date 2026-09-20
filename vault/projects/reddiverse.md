---
slug: "reddiverse"
url: "https://devpost.com/software/reddiverse"
title: "Reddiverse"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 1091
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Reddiverse

> The first multiplayer voxel game engine built natively for Reddit, where communities explore, build, and invent new game mechanics together inside interactive posts.

[Devpost](https://devpost.com/software/reddiverse) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[genomic_bio]] [[geospatial]] [[video_visual]]

**stack** devvit, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i proud of
- what i learned
- what's next for reddiverse

## Body

Multiplayer Mobile friendly joystick controls Desert Smart Blocks Beware of snail. If they touch you, you dead Inspiration Reddit is home to creativity, from pixel art battles to story-driven roleplay communities. I asked: what if I could bring that same community driven spirit into a fully explorable 3D voxel world, right inside a Reddit post? That idea became Reddiverse: a multiplayer voxel engine that combines Minecraft-style building with Reddit’s collaborative DNA. My goal was to push the limits of Devvit and prove that complex, real-time 3D experiences could live directly on the platform. What it does Reddiverse is a real-time multiplayer voxel game engine that transforms Reddit posts into interactive 3D spaces. It’s a platform for what I call UGW (User Generated Worlds) and UGG (User Generated Games) . User Generated Worlds (UGW): Explore and build in procedurally generated worlds with three distinct biomes (Greenery, Desert, and Mountains). Each world features a fully synchronized 15-minute day/night cycle with dynamic lighting, atmospheric effects, and a procedural cloud system. User Generated Games (UGG): The Smart Block system is the engine's core, enabling anyone to create custom game logic. You can design puzzles, obstacle courses, or adventure maps by creating blocks that manage player health, set win conditions, assign badges, create custom physics, and even modify the world itself—all without writing a single line of code. Multiplayer Foundation: The engine includes a multiplayer system allowing users to explore and build together. It’s built on a custom polling architecture to function within Devvit's platform constraints. Mobile Support: A fully responsive design with touch controls ensures a seamless experience on both desktop and mobile devices. The Immortal Snail: Inspired by the famous Reddit hypothetical, every world is persistently hunted by slow-moving snails. It will follow the nearest player, and if it touches you, you die. Don't let it touch you. How I built it Reddiverse is built on a modern tech stack, leveraging the power of React, Three.js, and TypeScript for the frontend, with an Express.js and Node.js backend. The entire experience is integrated into Reddit's Devvit platform . For the terrain generation, I implemented a sophisticated multi-layered Perlin noise system, inspired by the techniques used in games like Minecraft. As explained in this helpful YouTube video , I use a combination of 2D noise fields for terrain shaping (continentalness, erosion, peaks) and 3D noise fields for generating complex cave systems. The world is divided into chunks (64x64x96 blocks) that are dynamically loaded and unloaded as the player moves. I heavily optimized the rendering pipeline with instanced meshes and material caching to handle the sheer number of blocks on screen. Given that the Devvit platform does not support WebSockets (yet), I had to develop an adaptive polling system for multiplayer. This system dynamically adjusts the polling frequency based on connection quality to manage the real-time data exchange between players. Positional interpolation is used to make the sync smooth. Challenges I ran into Developing this solo came with a unique set of challenges, but each one was a valuable learning opportunity: The Case of the Ghostly Padding: I spent a good chunk of time debugging an issue where my Tailwind CSS updates weren't being reflected in the actual design. After much head-scratching, I discovered this was a known issue with Tailwind v4 and I had to implement a workaround. Will it Blend? (or rather, Will it Run?): I was initially unsure if Devvit could handle the performance demands of a real-time 3D voxel engine. I started with a very conservative approach, but when that worked, I decided to risk it and implement a full-fledged voxel generation system. To my delight, it held up! The WebSocket Whoopsie: The lack of WebSocket support on Devvit was a major hurdle for the multiplayer system. I had to get creative and develop the adaptive polling system from scratch to provide a functional real-time experience. The "Lobby" Feature That Was Actually a Bug: For a while, I had a persistent bug where players couldn't remove terrain blocks in the initial spawn chunk. I was this close to branding it as a "feature" (the "uneditable lobby area"), but thankfully, I managed to squash the bug in the end. Accomplishments that I proud of As a solo developer, I'm incredibly proud of what I've managed to build with Reddiverse. The Smart Block System: This is the heart of Reddiverse and what enables the "User Generated Games" (UGG) concept. Giving users the power to create their own game mechanics is what makes this project more than just a building game. The Terrain Generation Engine: The multi-layered Perlin noise system creates beautiful and varied landscapes, forming the canvas for "User Generated Worlds" (UGW). Embracing Reddit Culture: By integrating features like the Immortal Snail , the project isn't just on_Reddit, it's _of Reddit. It shows a deep understanding of the community culture the platform is built on. More reddit inside jokes will be added too. Building a Multiplayer Foundation: Implementing a functional real-time multiplayer architecture within Devvit's technical constraints was a significant challenge, and I'm proud of the system I developed. Pushing the Boundaries of Devvit: I'm proud to have built such a complex and feature-rich application on the Devvit platform, showcasing its potential for creating truly immersive and interactive experiences. What I learned That sometimes, you just have to take a risk. My decision to go for a full voxel generation system was a gamble, but it paid off in the end. The Strength of Devvit Devvit is more powerful than it looks, but you need to be creative to work around its constraints. The power of a modular architecture. My modular biome and block systems make it easy to add new content and features to the game. What's next for Reddiverse I have a lot of exciting plans for the future of Reddiverse: Performance Improvements: Smarter chunk streaming, better latency handling, potential support for true streaming once Devvit expands. Hope to work along with Devvit team to find solutions for it. Content Expansion: I plan to add more biomes, 3D player models based on Reddit avatars (Snooavatars), a weapons system, and even more NPCs(we already have snails btw). Monetization: To add support for Reddit payments so users can monetize access to their worlds. Rich Features I want to add an in-game chat system, configurable spawn points, and a world-sharing feature to make it easier for users to connect and collaborate. 3D Snooavatars: Snooavatar-based 3D characters. Using either image to 3d AI models, or just by wrapping up the image as texture on 3d model. <div