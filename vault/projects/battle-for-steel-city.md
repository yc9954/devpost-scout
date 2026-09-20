---
slug: "battle-for-steel-city"
url: "https://devpost.com/software/battle-for-steel-city"
title: "Zone Wars: Battle for Steel City"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 658
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Zone Wars: Battle for Steel City

> "Battle for Steel City: Zone Wars" is a fast-paced, competitive 5v5 and Free-for-All multiplayer shooter set in the gritty, cyberpunk-inspired bottom zones of Steel City. Choose your side NFF or BZF.

[Devpost](https://devpost.com/software/battle-for-steel-city) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**domain** [[transportation]]
**substrate** [[geospatial]]
  <sub>weak: sensor_telemetry</sub>

**stack** adobe-illustrator, blender, photoshop, typescript

## How they structured the write-up

- inspiration
- 🎯 symmetrical map design
- 🪖 three-weapon loadouts (inspired by gears of war )
- 💥 power weapon spawns
- 🧠 team strategy emphasis
- 🐞 projectile bug after launch
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zone wars: battle for steel city

## Body

Game Controls Game Weapons Map Selection Lobby2 District one, map 1 Lobby 1 Inspiration 🎮 Inspiration Hey, RJ_the_Creator here! I previously built a world called Battle for Steel City: Zone One , part of a larger universe I’ve been developing across Horizon Worlds. The vision includes 4–5 interconnected worlds that span narrative arcs, shared assets, and evolving gameplay systems. Zone Wars was always intended to be the centerpiece of the universe — the fast-paced, replayable, chaos-filled PvP game that funnels players into the calmer, more exploration-driven open-world zones (Zone 1–3). Everything is tied together with cross-world objectives, daily missions, and a branching narrative that evolves with the players. Zone Wars' core gameplay was inspired by classic PS1-era shooters and Xbox 360’s Gears of War . The symmetry of Gears’ multiplayer maps really stuck with me — each team starts on opposite sides with identical layouts and meets in the middle where the chaos ensues. 🔫 How I Built It We built the core experience with the following gameplay pillars in mind: 🎯 Symmetrical Map Design Each match begins with both teams on equal footing, featuring three mid-lane paths for: Flanking Sniping Close-range brawls 🪖 Three-Weapon Loadouts (inspired by Gears of War ) We followed a loadout structure of: Pistol : Lightweight, fast reload Rifle : Mid-range all-purpose Shotgun : Devastating up close Each weapon comes with: Damage Profiles Movement Speed Penalties Jump Height Modifiers Mathematically, we balanced player speed based on weapon weight using a simple scale: $$ v = v_0 - (w \cdot \alpha) $$ Where: ( v ) is current speed ( v_0 ) is base speed ( w ) is weapon weight factor ( \alpha ) is a constant (balance multiplier) 💥 Power Weapon Spawns Game-changing heavy weapons include: Boom Launcher Mindshredder Sniper Storm Machine Gun These have high: Damage Output Fire Rate Blast Radius They spawn on timers to drive map control and team coordination. 🧠 Team Strategy Emphasis Zone Wars is built around cooperative play , with success depending on: Positioning Timing Weapon awareness Map control 🎨 Progression System "Season Pass" for players looking to level up faster and earn exclusive monthly rewards. 🎨 Unlock-able weapon skins 🎭 Cosmetic masks 🧠 XP-based leveling 🗓️ Planned seasonal content A simple XP gain model used: $$ XP = k \cdot (K + A + O) $$ Where: ( K ) = Kills ( A ) = Assists ( O ) = Objectives Completed ( k ) = scaling multiplier 🔧 Challenges We Faced 🐞 Projectile Bug After Launch Shortly after launch in February , Horizon introduced a projectile bug: Shots would pass through players without registering damage 1–2 players per match became invincible Games felt broken and unfair Player retention dropped fast This bug lasted weeks , and by the time it was resolved, our momentum had vanished. We lost visibility on menus and searches, making organic traffic near impossible. 📚 What We Learned ⏳ Timing is Everything A great launch window can be ruined by bugs. First impressions matter. ⚖️ Balance is Critical Equal maps Tactical weapon design Defined team roles These all contribute to fair, fun PvP. 🔁 Progression Drives Retention Unlockables and leveling systems provide motivation to return. 🧱 Don’t Give Up Even when traffic dies, if the game’s core is solid , it’s worth rebuilding. 🔄 What’s Next We're relaunching Zone Wars as part of the Meta Horizon Creator Competition with: 🔧 Fixed bugs and improved weapon feedback 📱 Mobile-friendly UI ✨ Enhanced visual polish 💥 Rebalanced power weapons 🔓 New progression unlocks 🌍 Cross-world integration with Steel City universe 🕒 Planned seasonal and narrative events We still believe Zone Wars can be one of Horizon’s best competitive shooters — and now, we’re back and pushing harder than ever to prove it. What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for Zone Wars: Battle for Steel City <div