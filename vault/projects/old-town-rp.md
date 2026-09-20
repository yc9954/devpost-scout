---
slug: "old-town-rp"
url: "https://devpost.com/software/old-town-rp"
title: "Old Town RP"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 762
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
---

# Old Town RP

> Step into the wildest Western town in Horizon! 🏆 Level up, get rich, and make your mark in the dusty streets of Old Town. Will you be the sheriff, the outlaw, or the legend? 🌟

[Devpost](https://devpost.com/software/old-town-rp) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[geospatial]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for old town rp

## Body

Inspiration I really like RP games and anything grindy. I have a world called Night Life RP that has gotten over 150,000 visits — woohoo! The idea behind Old Town RP was to capture some of the elements that made Night Life RP successful but bring a whole new flavor to it. I've always wanted to create a world like this, and now it's finally happening. What it does In Old Town RP , players can experience a wide range of activities: Level up and earn in-game currency Buy new guns and upgrade their arsenal Play a bottle shooting mini-game Engage in PVP combat Deliver goods across the map Hunt animals for fur and sell it for money Play blackjack at the local saloon Stop a moving train to steal its valuable loot Rob stores for extra cash Compete on leaderboards Claim daily rewards Navigate everything easily with a clean, intuitive UI Additionally, Old Town RP features IWPs (In-World Purchases) for in-game currency, and a special Gamepass that permanently grants players 2x earnings from all activities. How I built it I built Old Town RP using the Horizon Worlds editor and Horizon's custom TypeScript API. The world design and placement were created inside the editor, while all the core mechanics like leveling, currency management, and activities were scripted with TypeScript. I also generated sound effects using the built-in Gen AI sound tool to give the world a unique and immersive atmosphere. Challenges we ran into Scripting Old Town RP was a major learning experience. One of the biggest challenges was handling UI updates — sometimes the UI would display the same values for all players or not show any values at all. As development continues behind the scenes, I'm currently dealing with some TypeScript errors that are causing a new mini-game for the world to not work exactly the way I want. Each hurdle has been a chance to learn and improve the overall structure of the project. Accomplishments that we're proud of Honestly, I love all of it. I didn’t think I could pull off this project — especially not alone, and definitely not entirely in TypeScript — but I doubted myself more than I should have. I'm especially proud of the mobile-focused UI. I really enjoyed creating it, even though I wasn't thrilled about the mobile push at first despite being in Horizon for over 4 years. Now? I’m having a blast. Some of my favorite milestones: Learning new tricks like using getEntitiesByTag Figuring out how to change UI values per player, whether local or networked Getting IWPs to work in TypeScript — tough but super rewarding Scripting the UFO gun (that was seriously fun) Streamlining UI by avoiding unnecessary buttons on grabbable entities Designing clear systems for earning money and leveling up — using visuals to make sure it’s accessible even to younger players or those who struggle with reading Seeing all the mechanics work together — from progression to the gamepass — lit a fire in me. I'm now working on a few mobile-only games because of how much I enjoyed this experience. What we learned I learned that everything I created in VR, I could also bring to mobile — and that realization completely changed how I approach world-building. I’ve grown to love the desktop editor. It gave me the precision and flexibility I needed to make a mobile-friendly game. Using the Gen AI tools in the editor to generate sample scripts helped a ton — I was able to take those samples and evolve them into fully working systems. This project showed me I could take on bigger challenges and really own the entire development process. What's next for Old Town RP These features may or may not make it into the game before the deadline, but I'm actively working on: A Spin the Bottle mini-game that moves mobile players into first-person view during the event A High Noon Duel where players can face off in quick-draw battles A Giant Chicken Hunt , using the Unity asset from our folders, where a giant chicken spawns and attacks players — players can shoot it and earn a good amount of fur and XP (it should be hilarious) More guns to expand player options A full Poker UI game More IWPs that add convenience or cosmetic perks without creating a "pay-to-win" environment Wearables and eventually Horizon Avatar clothes once the feature becomes available If the world does well, I'll also personally pop into player instances to gather feedback, listen to recommendations, and optimize the world even further. <div