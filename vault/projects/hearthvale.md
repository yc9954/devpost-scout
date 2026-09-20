---
slug: "hearthvale"
url: "https://devpost.com/software/hearthvale"
title: "Hearthvale"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 693
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Hearthvale

> A cozy village your whole subreddit builds together — farm, trade, and raise a castle that only grows when the community does.

[Devpost](https://devpost.com/software/hearthvale) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[agriculture_food]] [[civic_government]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]]

**stack** devvit, hono, phaser.js, redis, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- the hook
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hearthvale
- built during the hackathon

## Body

Main Page Mobile View Village Hall level 0 Dessert Biome Village Hall level 3 Autumn Biome Inspiration Every subreddit is already a village — people show up daily, tend their corner, and build something none of them could alone. Hearthvale makes that literal: one persistent world per subreddit that only grows if the community grows. What it does Hearthvale is a shared, persistent village living inside a Reddit post. Every member settles a homestead on the same map, farms and crafts on real-time timers, and trades in a village market where prices move with scarcity — sell your wheat and it fills the stockpile that your neighbor's windmill grinds into flour. Nobody can do it alone by design: the Village Hall — a castle at the center of the map — needs both pooled resources AND population to level, and each level unlocks new land, village-wide perks, and a visibly bigger castle for everyone. This is a game about interaction, not solo play. Your prices are set by what others sell. Your windmill starves unless someone farms. Your boosts help neighbors' plots. New land arrives only when new villagers do — so every player becomes a recruiter. And the game talks back into the subreddit: milestones post as comments, level-ups and Hall stages offer one-tap share-to-comments, top contributors win naming rights over Hall levels, level titles become user flair, and a daily auto-post drops the market report and weather into the feed so the comment section becomes the village's town square ("we need two more villagers!", "bricks are paying triple, someone build a kiln"). A spotlight-guided tour walks brand-new players from first tap to first sale; a 17-goal quest journal hands you the next objective for weeks; streaks, daily weather, rotating festivals, and golden "Perfect Harvest" windows (tap during the sparkle for double) give every single day a reason to come back. Every subreddit's village is unmistakably its own: seeded terrain generation makes each map unique, moderators set the village's name, color theme, and crest from a mod menu, players paint their roofs and dress their villagers — and the whole community paints a shared 24x16 pixel mural, r/place-style, at 12 pixels per villager per day. The hook Four things change while you're away: your timers finish, market prices move, the Hall inches forward, and the weather/festival roll over — and the daily post puts that delta directly in the feed. The deeper hook is collective: land, perks, and the castle itself are gated on the village acting together. How we built it Devvit Web + Phaser 4 for the isometric world (Kenney's CC0 Sketch Town art, per-village seeded terrain), a Hono serverless backend with all state in per-installation Redis, realtime channels for live neighbor activity, and the scheduler for daily weather/festival posts. All production math is lazy (computed from timestamps — no ticking); the market uses marginal pricing (structurally arbitrage-proof — verified by a 210-case property test); ~280 unit tests cover the economy. We also built a local mock-server harness so the full game is playable outside Reddit for fast iteration. Challenges we ran into Making a co-op economy legible in 30 feed-seconds. We cut two complete systems (a wandering trader, festival voting) after playtests showed complexity without joy, rebuilt onboarding three times (tutorial then quest journal then spotlight tour), and redesigned the collective goal into a single Clash-of-Clans-style Village Hall when players couldn't see what the village was working toward. Accomplishments that we're proud of A genuinely interdependent economy (specialize, trade through the stockpile, chase shortages) that a first-timer can enjoy without understanding it; a world that visibly grows with its community; and a hand-crafted look where no two villages are alike. What we learned Feed-first design is its own discipline: every mechanic had to earn its place in a 30-second session, and every retention hook worked better shown than explained. What's next for Hearthvale A village orders board (co-op requests), seasonal events, cross-village visiting, and mod-configurable Hall perks. Built during the hackathon Everything — the project was started and completed entirely inside the submission window (~90 commits: economy, multiplayer server, renderer, onboarding, art integration, and a local dev harness). <div