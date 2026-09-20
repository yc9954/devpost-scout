---
slug: "jam-join-a-metronome"
url: "https://devpost.com/software/jam-join-a-metronome"
title: "J.A.M. | Join A Metronome"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 248
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# J.A.M. | Join A Metronome

> Lets bands play remotely together with a globally synced metronome. Use any streaming platform to perform live for the socially distanced world!

[Devpost](https://devpost.com/software/jam-join-a-metronome) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: web_dom</sub>

**stack** css, html, jquery

## How they structured the write-up

- the problem
- the solution
- how it's built
- challenges
- accomplishments
- backlog - phase 1.1
- backlog - phase 2.0

## Body

JAM Desktop View The Problem All musicians are out of work! We've seen bedroom livestreams explode in the last 10 days. Bands can play together from the same place but we haven't figured out playing together remotely. The Solution JAM plays a 4/4 click track that is in sync with all other devices in the world. Pick a tune, play to the click and the audience hears it all happen live. How it's built It is a simple Javascript function. It uses the device's internal clock to keep time. Challenges 1) While the tempo is generally perfect, the exact timing varied about 500ms between devices. This was solved with the slider that nudges the track forward or back. 2) General understanding of the platform. People assumed they could login and join a proverbial "jam room." Non-musicians didn't know it was a problem. Accomplishments It works! Backlog - Phase 1.1 Converting the audio mechanism to use Web Audio, which is more precise than the JS setInterval used now. Get sound working on mobile Better landing page + how it works video. Enhanced browser support Commissioned art for the background 3/4 and 6/8 time signatures Custom drum kits MixPanel Integration for behavior tracking Backlog - Phase 2.0 Proper integration with a streaming solution Automated tempo sync Ability to play backing tracks along with musicians - Will help singers to stay in key if playing alone. Test general relativity by having one player play from a high-speed train or plane. <div