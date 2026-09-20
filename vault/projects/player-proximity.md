---
slug: "player-proximity"
url: "https://devpost.com/software/player-proximity"
title: "Player Proximity"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 231
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Player Proximity

> Player Proximity is a tool for horizon world that helps track interesting player activities in the world and sends it efficiently to all players.

[Devpost](https://devpost.com/software/player-proximity) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**substrate** [[geospatial]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for player proximity

## Body

Inspiration I got curious about similar games that uses they proximity system and got inspired to bring it to horizon worlds. What it does Player Proximity uses a system called Interest Management to send interesting player activities to other players in the world. This system is efficient since it divides the world into a grid and only sends changes that occur in the player's cell and adjacent cells making it scalable for large player games. How we built it The system has 3 main components, the Server, the Client and the Controller. The server does the monitoring of player activities and decides when to send changes to clients that need them. The client uses the data to display the location the interest is coming from. The controller is where most config is done. Challenges we ran into The system is challenging to design and develop. One notable challenge is manipulating the Custom UI to display in the direction of the interest. Accomplishments that we're proud of I like how the whole system came together and work well. Especially the multi-server setup which you can use to set different ranges for interests. What we learned I had to learn about Interest Management system to be able to develop the tool. What's next for Player Proximity The system can easily be extended to monitor items in the world and also for maps. <div