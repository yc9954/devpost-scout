---
slug: "clanker-town"
url: "https://devpost.com/software/clanker-town"
title: "Clanker Town"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 204
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/supply_logistics"
  - "substrate/geospatial"
---

# Clanker Town

> Clanker Town is a simulation / web-browser video game which lets player enter the town filled with other autonomous AI agents communicating between each other, gathering resources and trading.

[Devpost](https://devpost.com/software/clanker-town) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[supply_logistics]]
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** elastic-search, letta, mcp, move, react, sui, ts

## How they structured the write-up

- overview
- memory

## Body

Clankeeer logo Clnker screenshot talking to clanker Clanker Town Deployed Sui testnet package: 0x6be6a9f260939c73bdfb9ee3b6fe780e4bcde06b2f4c5ec3d90ca710b511b2a0 Overview Clanker Town is a simulation / web-browser video game which lets player enter the town filled with other autonomous AI agents communicating between each other, gathering resources and trading. Game Loop When player start the game they are dropped into a new match with few AI agents with distinctive personas and character traits, wallets and resources in the inventory. Initially all generators are not owned by anyone and can be captured either by agents or the player, once that happens the generator starts generating resources which can be claimed periodically, once agent/player has enough rsources they can upgrade the generator. Hostility / Friendliness In order to progress faster in game player can either start acting hostile by capturing agent's generator or be friendly to them, befriend them and bargain for lgood terms for trading rsources with them. Memory In order to have context about the game, vision about the real-time world entities around agent, different level of trust / hostility towards the player and other agents, Clanker Town uses Letta for memory blocks and Elastic Search to find geospatial data about all items, agents, player on the map. <div