---
slug: "rummager"
url: "https://devpost.com/software/rummager"
title: "Rummager"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 418
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
---

# Rummager

> A cozy singleplayer portrait mode survival crafting adventure game. Tap to explore, harvest resources, craft items, build workstations and unlock portals to new islands.

[Devpost](https://devpost.com/software/rummager) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**domain** [[agriculture_food]]
  <sub>weak: supply_logistics</sub>

**stack** biome, horizon, noesis, typescript

## Body

Banner Grassy Island Rocky Island Icy Island Sandy Island Flamy Island Inspiration We were heavily inspired by the games Forager and Animal Crossing, and wanted to bring a cozy base-builder to Meta Horizon. We were very excited to be working with the new Noesis APIs and thought this would be a fantastic experience to do it in. The main goal was to create something easy to pick up for five minutes, make progress on your world or quests, and come back later. What it does Rummager is a singleplayer survival crafting game where players tap to move, harvest resources, craft items and buildings, complete quests, and unlock portals to new islands. Featuring an elaborate questing system, dynamic day-night cycle, persistent world and complex base building. How we built it We designed all UIs directly in Noesis, splitting them into unique layers for each appropriate gameplay mechanic. The world is composed of five distinct islands, with random resource spawning via asset pooling. The player moves via a tap-to-move mechanic, with interactions on objects through a context menu, and avoids obstacles via a Navmesh. The world is divided into a grid which aligns all buildings, with rotation on a selected center cell of the object. Challenges we ran into Given how recently the Noesis APIs were introduced, we encountered a number of issues which required workarounds. The primary issue is related to interactions between the focused interaction mode and taps on Noesis UIs, where taps became registered as drags after interacting with any UI element. Accomplishments that we're proud of We're most proud of how fast we learnt to use Noesis and how well it came together is such a short time. The time of day and navigation is also something we're really proud of, but what takes the cake is the inventory to placement of buildings system. All of that coupled with the amazing soundtrack changing between islands and the dynamic popup displaying the name of the island it all feels like cozy adventure game that we really are proud of. What we learned Mobile-first design - especially with portrait - taught us that the UI needs a lot of thought on how to create an effective, functional and beautiful user experience. We also heavily focused on asset pooling as an optimization to ensure resource spawning was snappy. What's next for Rummager More islands, more quests, more advanced recipes and of course more upgrades for your pickaxe, as well as enchantments to further increase the depth of gameplay. <div