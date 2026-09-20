---
slug: "portalz-into-the-metaverse"
url: "https://devpost.com/software/portalz-into-the-metaverse"
title: "Portalz: Into the Metaverse"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 458
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "substrate/video_visual"
---

# Portalz: Into the Metaverse

> Portalz: Into the Metaverse is a single player mobile platformer with 20 chaotic levels full of traps, collectibles, and mind-bending obstacles. One player. Twenty worlds. Can you handle the madness?

[Devpost](https://devpost.com/software/portalz-into-the-metaverse) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]]
**substrate** [[video_visual]]

**stack** adobe-creative-suite, blender, photoshop, typescript

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for portalz: into the metaverse

## Body

Jungle Jumble Crystal Caverns Breezy Bridges Volcano Valley Portal Room North Portal Room South Loading Screen Minigame Inspiration The inspiration for Portalz comes from the fast paced and action packed platformers born from the fifth generation of video game consoles. Games like Super Mario 64, Banjo-Kazooie, and Crash Bandicoot inspire many of the gameplay elements found in Portalz. One moment you are dodging arrows and dispatching enemies in over the shoulder follow perspective, and the next moment you are jumping across huge gaps and hunting collectibles high and low in a side scroll section. Smash crates, collect pineapples and gems, and complete the time attack to earn all 3 stars for each level! How we built it In order to support a total of 20 different unique levels, we made use of the World Streaming in the Desktop Editor. By dynamically spawning in each sublevel in at the player's request and back out upon level completion, every level and world has it's own unique personality and platforming experience, and it allowed us to jam pack a ton of content into the game. We also made use of the Camera API for seamless switching between follow camera, side scrolling camera, as well as custom rigged cutscenes. We made use of Custom UI in two different cases. The first is a simple mute/unmute button on-screen to control global BGM/SFX volume with a quick tap, and the other is a minigame loading screen that allows the player to tap to smash crates for a chance at extra lives while the sublevel loads in. Challenges we ran into One of the main challenges after getting acquainted with the World Streaming system was coming up with a fun and rewarding way to stay occupied while the level loads in. We came up with the minigame loading screen idea to give the player a chance to farm a few extra lives before the level begins and it turned out to not only overcome the challenge but introduced an awesome minigame loop into the game at the same time. Accomplishments that we're proud of Having 20 unique 3D levels with tons of obstacles, enemies, collectibles, and intense platforming all throughout each one is something we are very proud of. What we learned We learned a ton about making use of various TypeScript APIs in the Desktop Editor including World Streaming, Camera, and Custom UI. On the 3D modelling and scene building side, the team learned tons about optimizing models and textures for mobile, and how to leverage the power of the new Meta Gen AI tools in the Desktop Editor. What's next for Portalz: Into the Metaverse We plan to add new obstacles and fully rigged enemies, and another biome with 5 new levels. <div