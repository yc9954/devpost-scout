---
slug: "outer-space-alice-tvl8w6"
url: "https://devpost.com/software/outer-space-alice-tvl8w6"
title: "Outer Space Alice"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 265
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/structured_db"
---

# Outer Space Alice

> Ask Outer Space Alice where she is – she will tell you the position of the ISS orbiting the earth and a fun fact.

[Devpost](https://devpost.com/software/outer-space-alice-tvl8w6) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

  <sub>weak: realtime_stream, runtime_tool_creation</sub>
**substrate** [[structured_db]]
  <sub>weak: geospatial</sub>

**stack** .net, alexa, amazon-polly, amazon-web-services, c#, lambda, mongodb, node.js

## Body

Outer Space Alice is a fun Alexa skill for kids. The story follows Alice, a teenage astronaut on the International Space Station. Kids can ask her where she is and Alice will give them the real ISS position orbiting the earth and a fun fact about the location. Alice’s companion is a robot named Pierre - he has some fascinating facts about oceans, continents and countries. With Outer Space Alice, kids learn about the International Space Station, geography, languages and other fun facts about the world. The Outer Space Alice technical architecture, uses the NASA orbital tracking data to locate the International Space Station. The real time position of the ISS is calculated every two minutes and matched in the Outer Space Alice geospatial database. The Outer Space Alice database stores the boundaries of all oceans, seas, continents, countries and major cities. Every two minutes, new audio is dynamically generated from hundreds of audio files for each location, time of day and weather conditions. The audio is saved in pieces which is used to create a custom experience for each user based on their interaction history and position in the Outer Space Alice Story. The voice of Pierre uses Amazon Polly to read out the geographic and space facts stored in the Outer Space Alice database. Key language phrases from 10 languages are also spoken by Amazon Polly Voices. All of the questions are logged so Alice can answer the questions correctly and improve over time. The growing collection of fun facts about the world, languages and music, will keep kids interested and learning. <div