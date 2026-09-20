---
slug: "delta-v-racing"
url: "https://devpost.com/software/delta-v-racing"
title: "Delta-V Racing"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 446
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Delta-V Racing

> Old-school graph-paper vector racing — plan your velocity or crash. Build tracks, challenge the community, climb the leaderboard.

[Devpost](https://devpost.com/software/delta-v-racing) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[web_dom]]

**stack** devvit, phaser.js, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- the "hook"
- what's next for delta-v racing

## Body

How to Delta-V Race Inspiration I was directly inspired by the old graph paper and pencil vector racing game. Draw a track and race against your friends. See this article for some history: https://en.wikipedia.org/wiki/Racetrack_(game) What it does As a player, it challenges you to understand the physics model and plan your route around the track accordingly. There are per-track leaderboards, and you race against "ghosts" of other players. There is also an F1 inspired overall leaderboard for the biggest bragging rights. As a track designer, you can challenge other Redditors with your own ideas brought to life in the editor. How I built it Devvit Web (Reddit's developer platform) for the app shell and hosting, Phaser 4.1.0 for rendering and the game loop, Matter.js (bundled with Phaser) for collision physics, Hono for the backend API, and Devvit's built-in Redis for storage. Track data — both hand-authored tutorial tracks and community submissions — runs through one shared format end-to-end, converted from source JSON into the runtime layout. Challenges I ran into Some Phaser tutorials assumed an older version and threw me off a few times. There were a couple of workarounds required where we had to use raw requestAnimationFrame/DOM, or Phaser's lower-level primitives. Accomplishments that I'm proud of Just getting it done. I can't count the number of game projects I've gotten to the 80 or 90% point and just couldn't push over the finish line. This is my first hackathon entry and having that deadline forced me to stay on track and avoid feature creep. I'm also just thrilled with how it turned out! What I learned Devvit is pretty cool! Using it was the smoothest part of this experience. Developing the client and server code at the same time was straightforward and ended up great. It was fun to see some of Phaser's features in action. This is the largest project I've done in Typescript. The "Hook" I took "Games with a hook" to heart. There are lots of things to hook players in and bring them back for more. The Daily track listing shows future tracks that will be unlocked on a given day. You can't play them yet, but you can be enticed to make sure to come back tomorrow. The editor is another hook. You've made a track, now you've got to keep checking back in to see how the community is doing on it. Has someone already beaten your ghost? More ideas for tracks to build? Keep coming back and show off your creativity! What's next for Delta-V Racing Car customization, position marker and trail graphics customization. Anything else the community thinks would be a worthy update will be considered. <div