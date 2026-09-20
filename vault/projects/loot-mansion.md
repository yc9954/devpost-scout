---
slug: "loot-mansion"
url: "https://devpost.com/software/loot-mansion"
title: "Loot Mansion"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 534
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Loot Mansion

> Loot Mansion is a chaotic, co-op VR heist game where you and your crew break into a haunted estate to collect valuable loot and escape alive.

[Devpost](https://devpost.com/software/loot-mansion) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

  <sub>weak: realtime_stream</sub>
  <sub>weak: geospatial, video_visual</sub>

**stack** blender, horizon, typescript

## Body

Loot Mansion World Photo Gameplay Shot2 Gameplay Shot1 Gameplay Shot3 Inspiration I was inspired by games like R.E.P.O., Devour, and Dark Hours. I’ve always loved the idea of extraction-style gameplay — sneaking in, grabbing loot, and escaping under pressure — especially with a fun, chaotic twist. I wanted to create something that could be played solo or with friends, and that worked across VR, Desktop, and Mobile. The spooky-but-silly tone of Loot Mansion grew from there: part haunted house, part wild treasure hunt. What it does Loot Mansion is a fast-paced, co-op party game where players break into a haunted estate to grab as much loot as they can and escape alive. Some loot may have odd side effects, and there's always something lurking in the halls. Each round gets tougher as more loot is collected, and players have to work together — or split up — to survive. Escape only becomes possible after hitting the loot goal, and failing to get out in time comes with consequences. How I built it I built Loot Mansion solo and focused on creating modular systems that could handle loot collection, player health, extraction logic, and round-based scaling. One of the biggest components was designing a custom NavMesh Agent enemy that could patrol, detect players using vision logic, chase them aggressively, and handle attack behavior cleanly. The UI, revive system, and item mechanics were also custom-built to work across platforms and encourage replayability. Challenges I ran into One of the biggest challenges was working with NavMesh Agents, since I had never used them before. Getting smooth, responsive pathfinding and enemy logic took a lot of iteration. Designing the round scaling system was also complex — it needed to make each session feel more intense without becoming frustrating. Balancing all of that while staying on schedule for the contest was tough, especially as the feature list kept growing. Accomplishments that I'm proud of I’m proud of how smooth and reactive the NavMesh Agent system turned out. It chases players effectively, and the way it integrates with the loot system creates real tension. I’m also proud of the round scaling logic — it makes each match feel like a growing challenge, encouraging players to communicate and plan on the fly. Everything in the project is modular, so adding new maps, enemies, or mechanics in the future will be easy. What I learned This project taught me how to work with NavMesh Agents from the ground up, and how to build gameplay systems that feel dynamic and replayable. I also learned a lot about structuring code for performance and readability, supporting cross-platform play, and designing a game that works well both solo and with other players. What's next for Loot Mansion I plan to release scheduled updates tied to holidays and seasonal events to keep the experience fresh throughout the year. I'm also exploring the idea of world streaming in the future to support multiple haunted locations. New cosmetics will be added to the in-game shop, along with more loot types and strange loot effects to keep players guessing. The NavMesh Agent will also receive scalable abilities, making each round feel more intense and unpredictable as the difficulty increases. <div