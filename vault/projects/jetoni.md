---
slug: "jetoni"
url: "https://devpost.com/software/jetoni"
title: "JetOni"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 203
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "substrate/sensor_telemetry"
---

# JetOni

> A 3D multiplayer tag game on Reddit (Devvit). In a procedurally generated city, players become Chasers or Runners. Can the Runners escape the jetpack-powered Chasers?

[Devpost](https://devpost.com/software/jetoni) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**substrate** [[sensor_telemetry]]

**stack** three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jetoni

## Body

Inspiration A mashup of traditional Japanese tag ("Onigokko") and sci-fi parkour, inspired by the technical challenge of building a high-performance 3D game on Reddit. What it does JetOni delivers a first-person, asymmetric 3D tag experience where jetpack-equipped hunters pursue dashing runners in a massive, procedurally generated urban environment, all running natively on Reddit. How we built it We built JetOni using Three.js for 3D rendering and the Devvit platform for Reddit-native deployment and state management, utilizing TypeScript and a procedural city generator. Challenges we ran into Integrating real-time, high-performance WebGL within the Devvit iframe constraints was challenging, especially optimizing physics and synchronizing complex 3D state for multiplayer. Although achieving multiplayer state management was initially difficult, we realized this using Devvit's real-time features. Accomplishments that we're proud of We are proud of creating one of the first truly interactive, high-fidelity 3D games running entirely within the Reddit ecosystem, proving the Devvit platform's capability for complex applications. What we learned We gained deep knowledge of WebGL performance optimization for social media platforms and mastering Devvit's server-client communication for real-time multiplayer game state. What's next for JetOni For the next stage, we are planning elements such as adding stages and items to further immerse players. <div