---
slug: "penfight-world-id-is-in-details"
url: "https://devpost.com/software/penfight-world-id-is-in-details"
title: "KiKi Color!"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 749
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# KiKi Color!

> Expand your territory, color the map, eliminate others! An infinite competitive arena.

[Devpost](https://devpost.com/software/penfight-world-id-is-in-details) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[geospatial]]

**stack** blender, typescript, vr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kiki color!

## Body

Inspiration Paper.io and other io-style games, with infinite collectibles and gameplay that keeps going as new players join and are eliminated. This is my first Meta world ever, and also my first tap-to-move game! I also noticed Meta Worlds does not have a game like this currently so I decided to fill the gap of "easy to learn, hard to master" games which succeed at being infinite and still fun! What it does Super smooth experience with only 1 finger needed, maybe even playable with just one toe. Just touch the screen where-ever! When I asked my relative's 4 year old to try, I found they were even able to get the hang of it instantly. A tap-to-move portrait game: players spawn with a circle of territory color and then keep making loops to expand their territory. A percentage bar at the top of the screen tracks how much of the map is covered. Try to reach 100 percent to win! Collect food items that give auto-boosts to territory creation, plus other special power-ups around the map. Be careful: if another player cuts or touches your trail while you’re making a loop, you’re eliminated! You can eliminate others the same way by hitting their trail. It's an infinite game designed like an .io experience for infinite competitiveness. It's super easy to control and you can pick up your phone whenever and start playing. How we built it Blood, sweat, and TypeScript. Firstly I started by doing a lot of research and planning the style and gameplay with physical plans and Meta's AI to help bounce ideas around. Meta GenAI 3D models was used especially for the map and creating small decorations, plus GenAI was used to organize large parts of the project and generate small collectibles. Some decorations were rendered from Blender and the project mechanisms was all built inside the Meta Horizon editor along with VS Code for the actual scripts of the project. Challenges we ran into Keeping tap-to-move easy and connected to the core mechanic, plus debugging multiplayer code for up to eight players. Initially it was difficult to create the color-trail mechanism for spawning territory. At first I wanted to spawn full stamped shapes of the territory, but eventually switched to spawning territory blocks to keep it fast and intuitive. Also faced general multiplayer sync issues, timing challenges, and making sure territory capture stayed readable and responsive. Accomplishments that we're proud of It's UNIQUENESS is our proudest aspect. So far I haven’t seen any Meta world that uses tap-to-move in this mobile-style, open-and-play way, so we take pride in being the first of its kind. I tried to make the game mechanisms as smooth as possible for the player while standing out by being completing different, and for tap-to-move to feel natural throughout gameplay. I believe to have somewhat succeeded! Making a whole working game within a month while everyone is chilling for Christmas or Thanksgiving is also no easy feat, haha, lot's of zero sleep nights. What we learned Handling input for portrait-style gameplay, syncing fast movement across players, refining trail collision rules, and balancing speed versus territory control. Also succeeded at learning how to use AI asset workflows efficiently without losing control of the core mechanic. I learnt that creating a world is a combo of 3d, 2d, code, editing, game design and everything in between so you have to be detailed. What's next for KiKi Color! Upgrades to characters, new skins, new maps, and additional infinite modes like team-vs-team or 1v1. Doing event-themed maps, Christmas and Ice Age-themed maps with more creative hazards and powerups. Also I want to make the purchasable shop skins for colorful trails, and adding wearable avatar items could be cool, especially creative hats to fit the top-down tap-to-move aesthetic. I was very close to adding the actual skins and equipable rainbow trail in the shop but was honestly tight for time, though the basic shop is set up. Next I will definitely be honing in on the backend and then having the shop UI fully made. Also new anti-power ups that a player could throw or sabotage others with. Each mode built on the same coloring-territory core but with new obstacles, pacing, and competitive layers to enrich the overall experience. I want to really hone in with multiplayer aspects by encouraging player leagues and drive with new skins, as I find this encourages playing the most: collecting status symbols (skins), competitive loops, and general fun uniqueness. <div