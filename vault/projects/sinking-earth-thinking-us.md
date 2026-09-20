---
slug: "sinking-earth-thinking-us"
url: "https://devpost.com/software/sinking-earth-thinking-us"
title: "Sinking Earth (Thinking Us)"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 470
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Sinking Earth (Thinking Us)

> To save the Sinking Earth, we must become Thinking Us. Let's perform missions and make reasonable consumption to protect the Earth. Enjoy in real time with people around the world.

[Devpost](https://devpost.com/software/sinking-earth-thinking-us) · hackathon [[Global Gamers Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[supply_logistics]]
**user** [[general_public]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** firebase, flame, flutter, riverpod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sinking earth (thinking us)

## Body

You are a resident of Sinking Earth. Save electricity and earn reward coins by playing the mini game of unplugging unused plugs! To survive on a sinking earth, complete environmental missions to earn coins, which you can exchange for daily necessities. Inspiration We wanted to incorporate as many real-world elements related to environmental, economic, and social factors into the game as possible, and we thought a simulation game would be suitable. Sinking Earth allows users to experience and utilize various sustainable development elements centered around the environment as game mechanics. What it does "Sinking Earth" is a simulation game themed around environmental protection and survival. Players must maintain their environmental score for 7 days before the Earth sinks, while also purchasing essentials to survive. In the game, players can choose from various professions, each with unique abilities and victory conditions. Players' choices shape the outcome of the game and can determine the fate of the Earth. Join forces to save the Earth and create a new future together! How we built it For user account management, we leveraged Firestore, a robust database system provided by Firebase. As for the game development, we employed the Flame engine, a versatile game engine compatible with Flutter, and integrated it with Real-time Firebase services. This combination allowed us to create a seamless user experience with real-time updates and interactions in the game environment. Challenges we ran into In order to implement real-time multiplayer gaming, we intended to use Nakama as the game backend. However, we determined that using Nakama in Flutter was not yet stabilized, and we had to overhaul the project that was already well underway. Since then, we proceeded without a backend and used a method of reading and writing to a real-time database. Accomplishments that we're proud of Flame's collider did not have a feature to prevent passing through like a wall. Therefore we had to calculate directly based on the intersection of the character collider and the wall collider. It was a very difficult and trial-and-error process, but it was satisfying to have implemented the collision feature ourselves. I read this reference, and I hope you find it helpful in similar situations. What we learned While developing this game, we explored environmental policies from various countries and incorporated them into our code. We learned that even for similar items, consumers can make environmentally friendly choices if they are a little more aware. We realized that we are not just coders, but we can also manifest our commitment to the environment through our code. What's next for Sinking Earth (Thinking Us) I would like to start by improving the multiplayer environment to run more smoothly. I want to diversify the user experience by allowing players to choose the number of participants and the types of maps available in the game. <div