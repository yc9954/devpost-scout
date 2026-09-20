---
slug: "ultimate-party-game-template-uptg"
url: "https://devpost.com/software/ultimate-party-game-template-uptg"
title: "Ultimate Party Game Template"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 312
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Ultimate Party Game Template

> Ultimate Party Game Template handles all party-game flow, lobby, scoring, respawn, AFK, late joins, so remixers only build minigames. Drop in logic + config, the framework runs the rest.

[Devpost](https://devpost.com/software/ultimate-party-game-template-uptg) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** typescript

## How they structured the write-up

- about the project

## Body

Logo Our how to play UI Our lobby display UI with ready checking Collect the coins minigame Lobby area Minigame Creation About the Project We built this framework because we love party games, the kind of quick, fun loops where friends can jump in, play a round, and move on. Our inspiration was to make creating new minigames as simple and approachable as possible, even for developers with little experience. What We Learned How to design clean tooling around Horizon Worlds that reduces boilerplate. How to use policies (scoring, end conditions, respawns, countdowns) as pluggable modules, giving every minigame consistent rules. How to drive UI entirely through a typed event bus, using bridges to separate logic from presentation. How to apply TypeScript strongly for clarity and safety in game scripts. How We Built It A thin base class ( MinigameBase ) coordinates policies and lifecycle, so authors only need to override a few hooks. An orchestrator ( DB_WorldOrchestrator ) controls session states, teleports, timers, and reporting. A router ( RoundRouter ) runs one minigame at a time, listens for outcomes, and handles cleanup. Config-driven flow ( DB_Config , DB_MinigameConfig ) sets lobby, round, intermission, and results timing without extra code. AutoVars (our own tool): we created DB_AutoVars.ts to eliminate repetitive prop wiring. It auto-sets references, validates data, and gives minigame authors strongly typed access with almost zero setup. This was one of the biggest boosts to developer experience. Challenges Designing a framework that is both scalable and approachable. Ensuring that even a new developer can copy the template, fill in a few hooks, and immediately ship a minigame. Balancing flexibility (local events for power users) with simplicity (sensible defaults for everyone else). In the end, we delivered a framework where the lifecycle is clean, the policies are modular, the UI is event-driven, and our custom AutoVars system keeps authoring friction low. <div