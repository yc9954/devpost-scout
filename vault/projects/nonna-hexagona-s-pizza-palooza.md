---
slug: "nonna-hexagona-s-pizza-palooza"
url: "https://devpost.com/software/nonna-hexagona-s-pizza-palooza"
title: "Nonna Hexagona's Pizza-Palooza"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 375
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Nonna Hexagona's Pizza-Palooza

> A puzzle game where players rearrange hextiles to find pizza toppings and help Nonna deliver hexagonal pizzas. Includes delightful narration, hand-crafted puzzles and wry Italian humor! Buon appetito!

[Devpost](https://devpost.com/software/nonna-hexagona-s-pizza-palooza) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**substrate** [[geospatial]]

**stack** affinity, horizon, houdini, noesis, typescript

## How they structured the write-up

- my inspiration
- my game
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for nonna?

## Body

It's Baron von Prickles!!! Ew!!! Milan Fashion Week-worthy outfits Many different level designs! Nonna helps you the whole way! My Inspiration I've always loved hexagon-based games, there's something so satisfying about their tessellation. I was pondering Italian brainrot and the idea came to me - pizza delivery with Nonna Hexagona! From there the idea of the pineapple as the villain was too good to pass up! And Nonna is based on my auntie!! My Game Players rotate and swap hexagonal road tiles to create routes through charming countryside. When roads connect, the avatar automatically navigates the network to gather toppings and complete deliveries. Haptics, sound, particles, and snappy animations make every tap feel addictive. Nonna Hexagona narrates the adventure with sass and warmth, and leaderboards let you challenge friends to see who can deliver the most pizzas (without pineapple). How I built it I started with Houdini to model and texture fully modular hex tile modules, as well as create a level design interface with a data-driven level pipeline exporting TypeScript-ready code. Then I ported the system into Horizon Worlds and from there gradually built up systems, scripting for all aspects of interactivity - pathfinding, FX management, Collectable tracking etc. I gradually upgraded the look over the weeks. Noesis for UI. Music is my own composition, Gen AI for sound FX and other asset generation. Challenges I ran into Some of the Noesis back-and-forward was a struggle. Also getting to grips with Local vs Default scripts and what they can and can't do! Accomplishments that I'm proud of I am very proud of the dynamic pathfinding system that uses Hex-grid coordinates. Combined with different types of collectables, a car that follows waypoints - there's a lot going on under the hood to create the experience, and I'm so happy that it all chugs along! What I learned I learned basically everything from scratch! I had never worked with Worlds, Typescript, or Noesis so there was a lot of reading documentation and madly throwing things together - I'm so happy with the result though! What's next for Nonna? I definitely would love to add more puzzles, even though there's 18. I would love to add Quests. Perhaps I can add gelato levels where tiles freeze! <div