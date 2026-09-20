---
slug: "remixable-world-obbyland"
url: "https://devpost.com/software/remixable-world-obbyland"
title: "Remixable World: ObbyLand"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 554
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Remixable World: ObbyLand

> ObbyLand is a remixable world for Horizon Worlds: drop-in obstacles, ability potions, currencies, and ready-to-use shapes—plus a sample level—so creators can ship fun obbies in hours, not weeks!

[Devpost](https://devpost.com/software/remixable-world-obbyland) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** horizonworld, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for remixable world: obbyland

## Body

Remixable World: ObbyLand Inspiration We love how fast obbies can deliver pure fun , but building them from scratch takes time: physics tuning, collectible logic, UI, performance, onboarding creators… ObbyLand was born to remove that friction so anyone can remix, learn, and ship a quality obby—fast. What it does ObbyLand is a remixable toolkit for Horizon Worlds that lets creators go from empty scene to playable obby in minutes. Drop-in obstacles: moving platforms, spinners, crushers,swinging hammers, timed spikes—each with tweakable speed, power, and timing. Ability potions: plug-and-play High Speed , Double Jump , Custom Scale , Low Gravity with configurable duration, cooldown, and visual feedback. Collectible currencies: coins/gems and puzzle piece with pickup SFX/VFX, auto-count UI, and more for make gameplay even more engaging. Ready-to-use shapes: a cohesive library of stylized blocks, trims, rails, and stairs with preset materials and snap-friendly pivots. Also a script for help you to change their color/texture, even runtime! Sample level: a compact course that demonstrates best practices—checkpoints, potion timing, and risk-vs-reward routes. Remix-first UX: color-coded gizmos, in-world tooltips, sensible defaults, and clean naming to make editing painless. How we built it We used Meta Horizon World's Desktop Editor and Horizon's TypeScript Library with Gizmos. Modular prefabs & events: every system talks via simple events like OnCoinCollect , OnPotionGet , OnObstacleHit , making pieces interchangeable. Creator controls: in-world config panels for speeds, durations, spawn rates, and scoring—no code edits required. Performance-minded design: pooled collectibles, timer batching, lightweight materials etc. Consistent art pass: a small, reusable shape kit with unified scale and style so levels look coherent out of the box. Test & iterate loop: short playtest cycles, quick tweak panels, and baked “challenge ramps” to validate difficulty curves. Challenges we ran into Network & physics feel: keeping movement and hazards fair under latency while preserving snappy controls. Potion balance: making abilities powerful and level-friendly without trivializing obstacles. Creator onboarding: distilling many options into defaults that “just work,” then exposing depth progressively. Mobile performance: reducing draw calls and script overhead while retaining punchy visuals and feedback. Accomplishments that we're proud of Zero-to-playable in under five minutes using only the sample world and prefab swaps. A cohesive obstacle library that mixes and matches cleanly through common events. Clear, remix-friendly structure —labeled hierarchies, comments, and tooltips that empower new creators. A fun, teach-by-example sample level that doubles as a template for pacing and flow. What we learned Sensible defaults beat endless options. Most creators keep the defaults if they feel great. Feedback matters. Tiny SFX/VFX cues on pickups and hazards dramatically improve readability. Design for remixing. Names, pivots, and snap points save hours across many creators. Docs + examples win. A short sample level teaches more than a long document. What’s next for Remixable World: ObbyLand More themes & biomes: ice, lava, neon, cloud, factory—complete with matching shapes and hazards. Leaderboards & timers: speedrun mode, ghost replays, checkpoint splits. Expanded abilities: wall-run, dash, magnet, double-jump—tuned for level fairness. Progression hooks: simple reward vendors and cosmetic unlocks powered by collectible currencies. Creator guides: short, visual tutorials and best-practice checklists. Community packs: curated obstacle/shapes packs from creators (with credit). Link to the world: https://horizon.meta.com/world/795754750283697 Showcase Video: https://www.youtube.com/watch?v=445RGk_Djgc Join our Discord for ObbyLand! Share feedback, pitch new ideas, and help shape the remixable obby toolkit. Playtests, sneak peeks, and creator tips inside. 👉 https://discord.gg/7XEjH7UhUy <div