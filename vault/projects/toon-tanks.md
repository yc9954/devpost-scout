---
slug: "toon-tanks"
url: "https://devpost.com/software/toon-tanks"
title: "Blast Riders"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 588
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Blast Riders

> Blast Riders! The ultimate battlefield between you, your opponents, and.... a volcano? That's right! Join this fight and be the sole survivor, outlasting other players and nature dangers.

[Devpost](https://devpost.com/software/toon-tanks) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**mechanism** [[structural_withholding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[housing_homeless]] [[transportation]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[video_visual]]

**stack** adobe-illustrator, blender, photoshop, substance-painter, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blast riders

## Body

Cover Page Win page Mobile Phone Landing page Vehicle selection Game play - danger zones Game play Spectator view Collage Inspiration I came up with the idea when I was researching what makes a mobile game successful. And some key concepts kept popping up: rapid decision making and short game loops. I played a lot of games (Packman included), and the idea was conceived. Original name of the game was Toon Tanks, but we decided to pivot to something more generic to allow for future growth and variations: Blast Riders. What it does The core mechanic is simple: The vehicles are always in constant movement. This is to motivate quick thinking and rapid decision making (players can't stall the game by staying in one corner for example). Vehicles can move in any direction on the grid, except backwards (the streets of the city are too narrow for that maneuver anyways!) Shoot at other vehicles to affect their health levels. Colliding with other vehicles also affects health. Staying in dangerous/contaminated areas affects health as well. How we built it Using Meta Horizon Desktop Editor, Blender, Illustrator and Visual Studio Code. From RexRod: I'm a digital 3D artist that specializes in environment design. I first created a grid for the city, then I custom modeled all the city sections. A housing neighborhood, downtown businesses area, then finally the industrial area next to the power plant where the toxic waste comes into play. I modeled every small detail in the city, the windows, the bushes in yards, and trees. I specialize in bake lighting and mesh optimization. So for each building I baked the environment info from Blender model high-poly version into low poly version of the buildings for optimization. Bringing down the entire city from 147,000 vertices to 12,000 vertices. Each building 2k vertices down to 47 vertices, without losing detail. I did this with the entire distance environment, mountains, volcano, and lobby area. From PigeonNo12: On the scripting side the major challenge was to keep the number of RPC calls in check, since the vehicles are in constant movement. I decided to keep the avatars as spectators, giving us additional budget and rendering capacity for all the dynamics in the world. There is still room for optimizations, but this is something that we will continue to improve as we grow the game. Challenges we ran into Time for sure! We did try to commit to a big project and eventually reduced the scope and features. We ran into some platform issues, but we were able to work around them to finish the game. Accomplishments that we're proud of The camera angle that we chose allowed RexRod to develop a technique to maximize visual quality with minimal impact on performance. On the ideation and scripting side, I'm proud of creating a game with a unique mechanic never seen in Worlds. We both aspire for others' reaction to be: "Is that Horizon Worlds!!!??", and we think we accomplished it! What we learned A big lesson learned from this project was optimization, for both scripting and building. For building the process of creating stylized assets and baking textures; and for scripting how to develop with performance in mind keeping RPC calls under control. What's next for Blast Riders Increase the number of power-ups Incorporate daily rewards Adding skins to vehicles (and vehicles!) Adding monetization for customizing vehicles Adding more dynamic elements to surprise the player (drops from the sky, more danger elements) Adding more feedback for player states (eliminations, more callouts) <div