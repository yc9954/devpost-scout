---
slug: "potions-pack"
url: "https://devpost.com/software/potions-pack"
title: "Interactive Asset - Ability Potions"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 253
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# Interactive Asset - Ability Potions

> Plug-and-Play Power-Ups. Double Jump, High Speed, Low Gravity, Custom Scale. Multiplayer-ready; tweak duration, intensity, cooldowns,and auto-respawn to unlock new routes and speedrun meta in minutes.

[Devpost](https://devpost.com/software/potions-pack) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[security_privacy]]
**substrate** [[geospatial]]

**stack** horizonworlds, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for interactive asset - ability potions

## Body

Inspiration Creators spend too long wiring basic power-ups. We wanted drop-in, Mobile-friendly potions that instantly unlock new routes, speedrun lines, and playful physics—without custom scripting. What it does Adds Double Jump, High Speed, Low Gravity, and Custom Scale abilities via drag-and-drop potion pickups. Each potion supports duration, intensity, cooldown, auto-respawn, and clear VFX. Works in single or multiplayer with network-safe state replication and sensible defaults. How we built it Using Horizon Worlds’ visual scripting and gizmos, we created a lightweight manager on the player that applies timed modifiers (jump count, gravity scale, max speed, player scale). Potions are prefabbed with states, object pooling for reset, and creator-exposed parameters for quick tuning. Simple meshes and VFX keep poly/texture budgets low. Challenges we ran into Balancing stacking interactions (e.g., Speed + Low Gravity), keeping movement changes smooth in multiplayer, preserving comfort when scaling the player, and maintaining mobile performance while broadcasting status to all clients. Accomplishments that we're proud of Zero-setup prefabs that “just work,” consistent behavior in multiplayer test rooms, stable Mobile performance, and sample scenes that help first-time creators publish a buffed course in under an hour. What we learned Tiny UX cues (pickup SFX, countdown hints, fade-out) dramatically improve clarity. Safe defaults beat total freedom, and per-ability caps prevent edge-case exploits. Clear naming and grouped parameters reduce creator friction. What's next for Interactive Asset - Ability Potions More abilities (Shield, Magnet, Glide, Wall-Run Boost), HUD buff icons and timers, checkpoint integration, team/zone rules, leaderboard hooks, and difficulty presets for one-click balancing. <div