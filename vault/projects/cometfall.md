---
slug: "cometfall"
url: "https://devpost.com/software/cometfall"
title: "Cometfall"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 462
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Cometfall

> A strange comet caused monsters to roam the countryside. Defend your land throughout the night against magical monsters, exploring, learning spells, gathering materials and crafting better equipment.

[Devpost](https://devpost.com/software/cometfall) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]] [[education]]
**substrate** [[code_repository]] [[video_visual]]

**stack** desktop, mobile, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cometfall

## Body

Inspiration A lot of old-school RPGs, of course. What it does Without making the world too large, and keeping the gameplay loop short, trying to introduce exploration and storytelling in a single player experience. Gives players enough tools to experiments with different weapons, craftable weapon levels and spells. How we built it I'm new to typescript, my experience being mainly C++ and C#. I've typing furiously for many, many hours over the last two months. This ambitious project has a lot of moving parts. I've used a variety of sourcing for assets, including making some myself, using mesh gen AI, image gen and buying a bunch for CGTrader. Challenges we ran into A lot. I need some scripts to be local in order to control the camera for cutscenes, as an example, but navigating the local vs server execution on some scripts has been a challenge. I ran into lots of architectural issues until I cleaned-up my network messaging APIs. Also, having to animate creatures using rigid pieces in typescript is a challenge. The final result isn't great, especially since the meshes are hard cut into segments without hiding the seam with a ball & joint, but at least their have some life. I ran into strange issues with saving persistent variables of object type that didn't repro in the Desktop Editor, so I had to scramble at the last minute to convert most of the saved state to number variables. Accomplishments that we're proud of I feel the more mysterious mood of the world comes across reasonably well. Also, CustomUI is pretty great for animating properties, and it enables a dynamic UI really nicely. I like the visuals and the lighting. It is very deliberate, with a wide spectrum of dark, foreboding as well as well-lit welcoming locations. The audio ambiance for the various locations also sets the tone pretty well. Especially the caves. What we learned Everything. This is my first time building in Meta Horizon, and coding in typescript. Also, ramping up on Blender after many years of not using 3D modeling software (since 3D Studio Max) and so on... our tech industry expression "drinking from the firehose" feels very applicable here. If I can participate in another creator contest, it'll feel good to have a decent codebase to pull from and knowing 100x more about every aspect of building games in the Desktop Editor. What's next for Cometfall A fair amount of scope had to be trimmed to fit in the contest timeframe. Harvesting crystal from the mines, for instance. Limited ranged spells for the player. Better procedural animation for the monsters. Different monster difficulties with appropriate rewards. Leveling up players stats, like health, damage and spell cooldowns. There's a lot more than can be done here. <div