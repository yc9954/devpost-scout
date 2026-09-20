---
slug: "hodlverse"
url: "https://devpost.com/software/hodlverse"
title: "btc-dungeon"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 280
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# btc-dungeon

> Play my retro roguelike game and get some whale alerts on the way!

[Devpost](https://devpost.com/software/hodlverse) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets


**stack** audacity, axios, duck.ai, gimp, html5, javascript, jsfxr, mempool.space, xai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for btc-dungeon
- additional information

## Body

btc-dungeon splash screen gameplay game over Inspiration A procedurally-generated dungeon in the 1980 video game Rogue, and Zelda for the Nintendo Entertainment System. What it does This game procedurally-generates a dungeon and spawns in a couple of enemies per floor. You proceed by killing all enemies (stairs appear on the floor). Every enemy is spawned in by calling https://mempool.space/api/mempool/recent . A bonus is that the user that plays this game gets a whale alert on the go. How I built it xAI Grok 3 was the main coder, I directed Grok and moderated the code and did some changes here and there. I also used Duck.ai llama 3.3 70b for some quick changes. This way I was able to leverage the free tier without hitting the rate limit. Challenges I ran into I have polished the API calls WAY too much. I didn't want to get soft blocked so I (and Grok 3) implemented the spawning of enemies and whale alert to best of my knowledge. Accomplishments that we're proud of The overall feel of the game (gfx) and the music. I do believe I have much to learn about the free tier API calls my game make but still, pretty happy about the end result. What I learned To have fun while trying, no matter the challenge. What's next for btc-dungeon I depends, if people enjoy to play btc-dungeon I will have to polish the game. :) Additional information Spawn enemies via API logic: Shrimp, max: 0.01 BTC Crab, min: 0.01, max: 0.1 BTC Squid, min: 0.1, max: 1 BTC Dolphin, min: 1, max: 10 BTC Shark, min: 10, max: 100 BTC Whale, min: 100, max: Infinity BTC <div