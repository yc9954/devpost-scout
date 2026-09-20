---
slug: "cattack"
url: "https://devpost.com/software/cattack"
title: "Cattack!"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 400
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# Cattack!

> Explore hostile planets, collect cosmic cat companions, and claw your way to the top in this space-faring card battle adventure.

[Devpost](https://devpost.com/software/cattack) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** phaser.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cattack!

## Body

Main Gameplay Explore for Cards & Coins Free Claim Booster Booster & Upgrades Shop Inspiration I really wanted to make a game about collecting cats in space. I love roguelike deck-builders, so I wondered what it would look like if you replaced jokers with quirky cat companions and built a casual card game around that concept. What it does In Cattack!, you explore different planet maps, dodge alien invaders, shoot lasers, and collect loot like gold, food, and cards. When you encounter NPCs, you enter a three-turn card battle where you play poker hands to score points called Nips and Mults. You can equip up to three Cat Cards that act like passive modifiers, giving you score boosts or card retriggers. You can track your collection in the Catdex, buy items in the shop, and open daily booster packs. You can also challenge other users to beat you- which lets other users play asynchronously against you. How we built it I used Phaser 3 for the exploration maps and the card battle canvas, and wrapped it in React to handle some of the UI. Lots- and I mean, lot of drawing pixel art. Every Cat Card and Exploration map was drawn by me. Challenges we ran into Time limitations. 1 months to define a concept and bring it entirely to life was an extremely challenging test of my endurance. The game began as a space runner and gradually morphed into what it ultimately became. I also had never made and implemented a tileset before, so that was a massive undertaking. Accomplishments that we're proud of I am really happy with the card math engine. Getting retriggers, custom hands, and cat multipliers working correctly without bugs took a lot of work. What we learned I learned that balancing card multipliers is incredibly hard. I had to separate hand-evaluation logic from the actual graphics so I could run quick math tests without rendering the screen. I also learned how to manage asset loading carefully so the game runs smoothly and quickly on mobile browsers. What's next for Cattack! I want to add real-time PvP so players can battle each other live. I want to expand on Exploration immensely and add procedurally generated planet layouts so exploration doesn't feel repetitive, and I plan on adding way more Cat Cards, skins, and ways for users to not only participate- but contribute as well. <div