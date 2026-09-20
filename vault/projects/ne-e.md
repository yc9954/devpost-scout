---
slug: "ne-e"
url: "https://devpost.com/software/ne-e"
title: "Ne'e"
hackathon: "Junction 2017"
winner: true
words: 318
team_size: 5
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "substrate/sensor_telemetry"
---

# Ne'e

> An easy way for coaches to see the state fatigue of the players live during a game.

[Devpost](https://devpost.com/software/ne-e) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**substrate** [[sensor_telemetry]]

**stack** java, jquery, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ne'e

## Body

Ne'e a new way to measure fatigue Choose the type of sport you are managing Manage your team and update their information See the level of fatigue of the player live during the match Perparim fatigue level during a football match iPad implementation; tracking other vitals of the team members Inspiration Motion tracking has become everyday life in sports and implementations are commercially available to individuals. Yet, there is great lack in extension to team activities, where a group of people collectively train or compete for a common goal. We want to fix this and propose a solution that serves as the first step towards tracking a group of people and platform for statistics. What it does Our webapp will allow coaches manage multiple teams and to see biometric data in real time about all the members of the active team. We also computed the ne'e factor which allows us to tell at which state of fatigue the player is. How we built it We decided to do the data analysis in python, to allow us to calibrate the nee factor for the different players of our team. Using Java to get the data from the sensors. The web app is built in react to allow usage on all devices. PubNub to post and retrieve the data Challenges we ran into Getting data, most of our work has been done on generated data to simulate the players Accomplishments that we're proud of Visually compelling UI, allows to quickly know which player is tired during the game and would need to change. Ne'e factor that allows us to know the fatigue level of the user, based upon the activity and the BPM of the player. Independent of the number of players What we learned There is a lot that can be done in team sport concerning sensor data. What's next for Ne'e Take over the world of course <div