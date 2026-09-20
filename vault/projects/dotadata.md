---
slug: "dotadata"
url: "https://devpost.com/software/dotadata"
title: "DotaData"
hackathon: "GRID Esports DataJam 23"
organization: "GRID Esports"
winner: true
words: 299
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# DotaData

> Visualize data from historical and live Dota 2 games.

[Devpost](https://devpost.com/software/dotadata) · hackathon [[GRID Esports DataJam 23]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** grid-api, nextjs, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dotadata

## Body

Inspiration I drew inspiration from game analytics and recap websites that impressed me with their user-friendly and visually intuitive design, particularly their ability to quickly identify the standout players on each team. What it does DotaData provides real-time access to detailed Dota 2 game data, including player information, hero choices, items, KDA stats, and net worth. The standout feature is the live map, which offers a dynamic view of player positions on the map. How we built it The app was built using React and Next.js and harnessed the power of the GRID Open Platform API for gathering Dota 2 game data. Challenges we ran into One of the challenges I ran into was working with the jsonl files. I did not know how to interpret them and it also gave me trouble when uploading to github, so I decided to abandon working with those files altogether. To make sure my project still showcases the potential of "live" data, I went on to use GRID's Open Platform API to get live Dota 2 data. Accomplishments that we're proud of The main feature I am proud of is the live map feature. I took the coordinates from the api and scaled them so that they worked with my picture of the map. I was able to retrieve the x and y coordinates of the players and plot them on my map. What we learned I learned how to craft GraphQL queries to efficiently request specific data from an API. What's next for DotaData I really wanted to be able to graph xp and gold over time in addition to implementing a win probability prediction that updates alongside the live game data. I want there to be a better way to see who the top performers within each team is. <div