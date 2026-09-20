---
slug: "lasertag-zombies-update"
url: "https://devpost.com/software/lasertag-zombies-update"
title: "Lasertag - Operator & Scene Meshing prototypes"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 403
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# Lasertag - Operator & Scene Meshing prototypes

> Lasertag is a game that turns any space into a laser tag arena for you and your friends. This prototype update brings live scene meshing, NPCs, long-distance occlusion, and a desktop server app.

[Devpost](https://devpost.com/software/lasertag-zombies-update) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]]

**stack** unity

## How they structured the write-up

- live scene meshing
- long-distance visual occlusion
- npcs
- desktop server app

## Body

Lasertag turns any space into a laser tag arena for you and your friends. It's an experiment in lowering the friction and time-to-fun of colocated multiplayer experiences; it tries to 'just work.' The game scans your space into a signed distance volume as you play using the DepthAPI and automatically connects players using the Colocation Discovery API. This submission is a work-in-progress update to the game with several goals: Make the game easier to use when playing with a dozen players. Make the game more robust in large spaces with better bullet collision and accurate occlusion. Support single-player with NPCs that respond to the live scanned environment. These were some ambitious goals for this hackathon, and the performance and robustness of these features is not yet ready for release. However, I think it'd be a shame to not submit what I've accomplished this past month. Some of these features also aren't as user-facing as something like new game modes or weapons, but I want to lay a solid technical foundation down before worrying more about fun features. Update features Live scene meshing Reads physical environment at runtime via DepthAPI Multithreaded surface net mesher Created in chunks with time-sliced mesh generation Powers other features further down Issues: need some method for decimation and occlusion culling as triangle counts can choke GPU To view: In Settings tab ➔ Debugging ➔ enable 'draw scan mesh' Long-distance visual occlusion Created with low-resolution render pass of scene meshes Allows you to see far-away objects that DepthAPI occlusion would normally occlude. Issues: needs some method for chunk mesh decimation and occlusion culling as triangle counts can choke GPU To view: You can view the depth texture itself in Settings tab ➔ Debugging ➔ enable 'debug mode' NPCs Uses live scene mesh chunks to generate nav-meshes Allows zombie NPCs to hunt players down Issues: Nav-mesh updates cause significant stutters. I either need to decimate idle mesh chunks or implement my own pathfinding system. To view: Host or join a game In Settings tab ➔ NPCs (experimental) ➔ enable 'calculate nav-mesh' Spawn zombies from Objects tab (cube icon) ➔ green skull icon. Desktop server app Makes the game easier to use with dozens of players Start matches and save map layouts Todo: should show headset & controller battery levels To view: download the desktop operator from here and use with the release version of the game (not the competition branch)! <div