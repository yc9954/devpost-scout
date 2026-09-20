---
slug: "falcon-shgxn9"
url: "https://devpost.com/software/falcon-shgxn9"
title: "Falcon"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 417
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Falcon

> FALCON lets you fly drones and wild machines in MR or on VR levels. Turn your room into an airfield or dive into virtual worlds. Take on thrilling challenges solo or with friends-anytime.

[Devpost](https://devpost.com/software/falcon-shgxn9) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

  <sub>weak: realtime_stream, simulation_digital_twin</sub>
**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** blueprints, c++, eos, meta, unreal-engine

## How they structured the write-up

- challenges we ran into
- accomplishments that we're proud of

## Body

Inspiration We wanted to create the ultimate mini flying experience-something joyful, social, and deeply tactile. Mixed Reality felt like the perfect medium: a way to transform an ordinary room into a playful flight arena. Our inspiration came from classic RC aircraft, modern arcade-style racing, and the desire to make a physical space come alive through intuitive hand interactions. What it does FALCON turns the player’s real environment into a dynamic MR flight zone. Players fly multiple types of RC vehicles, race through handcrafted tracks, or enjoy physics-driven balloon challenges. Through colocation, multiple players can local fly together in the same room, sharing one synchronized mixed-reality space. In VR, players can compete in full multiplayer sessions across Racing Mode or Balloon Mode. Players can also build their own custom race tracks in VR and MR enviroment, supporting creativity and replayability. How we built it We built FALCON using the Meta Horizon OS Mixed Reality stack, focusing on precise spatial alignment, robust colocation, and performant physics interactions. The MR flight system required custom logic for obstacle detection, room sensing, and dynamic pathing based on the player’s space. For multiplayer, we implemented synchronized aircraft states, shared environments, and cross-mode networking. Track creation tools were built as lightweight, intuitive in-world editors powered by snapping, validation, and real-time simulation. Challenges we ran into Achieving stable colocation for multiple players in small physical spaces. Building engaging controls for many diffrent categories of vehicles. Ensuring synchronized physics across multiplayer sessions. Creating track-building tools that remain accessible to casual players. Accomplishments that we're proud of A highly responsive MR flight system that feels natural and tactile. Distinct gameplay modes offering both competitive and cooperative experiences. A creative system for building custom race tracks inside the headset. A polished, social experience supported by expressive avatars and intuitive interactions. What we learned We learned how crucial spatial consistency is for social MR experiences, and how small variations in real-world environments can influence perceived gameplay quality. We also gained valuable experience in building scalable multiplayer architecture, designing intuitive hand-based controls, and optimizing physics for mixed-reality conditions. Most importantly, we saw how creativity tools empower players and significantly increase engagement. What's next for FALCON We plan to expand multiplayer support, introduce more vehicles types, deepen progression systems, and add advanced co-creation tools for building multiplayer arenas. We also intend to refine MR mapping and introduce new physics-driven interactions to further enhance immersion. Our long-term goal is to make FALCON the definitive virtual/mixed-reality flying playground-accessible, social, and endlessly replayable. <div