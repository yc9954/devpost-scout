---
slug: "dota2-map-summarizer"
url: "https://devpost.com/software/dota2-map-summarizer"
title: "Dota2 Map Summarizer"
hackathon: "GRID Esports DataJam 23"
organization: "GRID Esports"
winner: true
words: 343
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Dota2 Map Summarizer

> This tool helps to generate the summary of the game through the map and player cards. We are hoping it can be used to generate useful thumbnail for live streams and attract more viewers to crazy games

[Devpost](https://devpost.com/software/dota2-map-summarizer) · hackathon [[GRID Esports DataJam 23]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dota2 map summarizer

## Body

Inspiration I was a big e-sports fan since TI 5 and I always appreciated sheer amount of effort required to produce a good live stream for an event. Over the years, there was an improvement in stats, replays, player cams, etc. However, one thing stayed the same, thumbnails suck Just by looking at the thumbnail, it’s very hard to understand the state of the game. It might have some crazy performance, weird items like diffusal on Gyrocopter or extremely off-meta heroes, but without actually clicking on the stream, I will never know what’s happening and hence most likely will miss the stream entirely. So, this inspired us to create Dota 2 map summarizer. What it does Dota 2 map summarizer features a map to display the status of towers, player cards with hero images, KDA, net-worth and of course items. And all of this gets updated in real-time using the GRID dataset. How we built it We used Python/Pandas to filter through data and then we used the new data in our React front end. Challenges we ran into We really tried to create a tool that could update the image in real-time, however, due to time constraints, it is currently somewhat static. It means it only works given a batch of data. Accomplishments that we're proud of We believe that working with such a large dataset + making the front end within just a week was a big accomplishment. It might not look the prettiest, but it efficiently tells the story and will most likely attract new viewers. What we learned Combining React and Python is not the easiest and learning React in less than a week was not the greatest choice. However, the time pressure made us really think what the core of the project is and how to scale down our expectations. What's next for Dota2 Map Summarizer I hope to finish the real-time data processing for a much smoother experience and create a heat-map history for better insight into what was happening on the map during the game. <div