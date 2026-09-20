---
slug: "gameguru"
url: "https://devpost.com/software/gameguru"
title: "GameGuru"
hackathon: "Junction 2017"
winner: true
words: 408
team_size: 5
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# GameGuru

> We provide highly personalised coaching to players of Squad so that they would never want to quit!

[Devpost](https://devpost.com/software/gameguru) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** networkx, numpy, pandas, pygame, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gameguru

## Body

Battle replay Inspiration We were inspired by the endless complexity of the 50x50 online shooting game tactics and the fact that human brain can only process tiny fraction of what happens real-time on the battlefield. We thought that our expertise in complexity science, analysis of complex networks and visualziation skill can help us demystify the gameplay for players. We imagined, once we provide players with an analysis of how they have played and how they can improve it, they will be hooked and never want to quit! What it does We use data from previous games a player has played, and build metrics which quantify their performance in individual as well as team level. We also provide visualizations of the dynamics of past games, which are more simplified and easier to grasp that a full replay of the game. These help players to understand importance of teamwork and improve their consciousness of tactical aspects of the game and what they need to do to perform better in next games. How we built it We decided that our end product, should have two dimensions: metrics and visualiztions. None of the two would be sufficient to coach a player towards a better gameplay. But we always communicated between the two sub-projects and shared processed data. In the end, the visualization and the data analytics which produce the metrics come nicely together to give a full picture to the player. Challenges we ran into Lack of metadata, which forced us to find new solutions and a new direction for our project. For example, we did not have the information in which team the player belong to. Accomplishments that we're proud of Being totally new to pygame it was exciting to see that we were able to create something cool and actually working with it. We also got through the problems with the original data set and managed to transform the data so that we could present it in a nice way. What we learned Time flies while you code and things don't always work like you expect. What's next for GameGuru Inclusion of team and squad member data would open totally new opportunities for analyzing the team and squad effectiveness. One interesting insight could be to monitor the situational awareness of a squad, i.e. are the squad members looking at the correct directions and covering all possible angles to minimize the risk of being flanked and taken out by surprise. <div