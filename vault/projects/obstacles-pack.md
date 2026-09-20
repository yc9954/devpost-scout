---
slug: "obstacles-pack"
url: "https://devpost.com/software/obstacles-pack"
title: "Interactive Asset - Obstacles Pack"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 232
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
---

# Interactive Asset - Obstacles Pack

> A drag-and-drop set of modular traps and hazards. Mobile-optimized, low-memory, multiplayer-ready. Tweak speed, timing, and difficulty to build replayable courses in minutes.

[Devpost](https://devpost.com/software/obstacles-pack) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[deterministic_policy]]

**stack** horizonworlds, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for interactive asset - obstacles pack

## Body

Inspiration Creators in Horizon Worlds spend too much time rebuilding basic obstacles. We wanted a drop-in pack that’s fun, flexible, and Mobile-friendly so anyone can ship a replayable course fast. What it does A modular set of traps and hazards—spinners, crushers, breakable floors, moving walls—each with tweakable speed, timing, damage, reset, and rules. Works in single or multiplayer, stays within Mobile budgets, and snaps together to build whole levels in minutes. How we built it Using Horizon Worlds library in TypeScript and gizmos, we designed lightweight, event-driven state machines for each obstacle. We added creator-facing parameters, object pooling for resets, simple primitives for low complexity, and example scenes that demonstrate best practices. Challenges we ran into Balancing physics feel vs. network sync, keeping performance solid on Mobile, and making controls powerful without overwhelming new creators. Naming, defaults, and docs mattered more than expected. Accomplishments that we're proud of Stable 60FPS on Mobile in multiplayer test rooms, zero-setup prefabs that “just work,” and clear docs + sample courses that let first-time users publish in under an hour. What we learned Tiny tuning knobs (timers, wind-ups, coyote time) dramatically improve fairness and fun. Good defaults, consistent naming, and visual hints reduce creator friction. What's next for Interactive Asset - Obstacles Pack More obstacle types (lasers, jumping pads, conveyors), themed variants, leaderboard hooks, more advanced checkpoint/respawn modules, and built-in difficulty presets for quick balancing. <div