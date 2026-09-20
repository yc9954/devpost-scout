---
slug: "webhangin"
url: "https://devpost.com/software/webhangin"
title: "WebHangin'"
hackathon: "United Hacks V6"
organization: "Hack United"
winner: true
words: 803
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# WebHangin'

> For UnitedHacks, we've made WebHangin'. It's a 3D web hangout space where you can just chill around people while you do your own thing.

[Devpost](https://devpost.com/software/webhangin) · hackathon [[United Hacks V6]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]
  <sub>weak: structured_db, web_dom</sub>

**stack** next.js, react, rust, typescript, webrtc

## Body

the character screen hangin with friends explore the city chat with gamers -->> PLAY NOW <<-- Github: https://github.com/FrankLaterza/webhangin 👋 WebHangin! For UnitedHacks, we've made WebHangin'. It's a 3D web hangout space where you can just chill around people while you do your own thing. We loved recent social games like WEBFISHING but were sad to see the lack of staying power. We feel that there should always be a low-social-barrier way to find people with similar interests and hobbies. The difficulty part is many hobbies such as musical instruments, single player games, or even software development are largely solitary. We aimed to make a platform that brings back the feeling of hangin' out with your friends in a discord call while you're doin' your thing. We built a 3D multiplayer world where you create a custom character and walk around with WASD controls. We have features like spatial audio, screensharing, and themed rooms with a probably overengineered backend for a hackathon project 🧙‍♂️ What it does? You hop in, make a little cat/dog character, pick some colors + a face, and type what you’re up to (like “gaming” or “watching a movie”). Then WebHangin drops you into a themed room that matches. From there it’s basically a tiny social game. The big difference vs a normal call is that you don’t have to be “on” the whole time. You can drift between conversations, sit near the jukebox, wander off, or just exist in the same space as other people while you do your own thing. 🤔 How we built it? We split it into a Rust backend + a web frontend. The backend is Rust (Actix) and handles the realtime stuff: player state, WebSocket signaling, and sorting people into rooms based on what they typed. The frontend is Next.js + Three.js, and it renders the 3D world + the animated GLTF characters. For voice + screen sharing we used WebRTC, routed through Rheomesh SFU, and we threw a ridiculous amount of ICE servers at it (16 total: 13 STUN + 3 TURN) because WebRTC loves failing in new and exciting ways. Spatial audio is intentionally simple — it’s just distance-based volume falloff based on player positions, updated ~60 times per second. ♟️ Challenges we ran into WebRTC being WebRTC: The hardest part was just getting people connected reliably. Sometimes it would work instantly, and sometimes you’d just… not connect. We fixed most of that by implementing ICE racing across all 16 servers, with parallel gathering + timeouts + fallback to whichever server responded first. Spatial audio weirdness across browsers: Our first version used HTML audio and just set .volume, but some browsers didn’t behave nicely with MediaStreams. We tried going “proper” with Web Audio API + GainNode, then realized we didn’t need anything fancy yet. We went back to simple volume falloff and it honestly felt better anyway. Room routing without making it complicated: We wanted people doing similar stuff to end up together, but we didn’t want it to be some heavy matchmaking system. We ended up doing simple keyword matching on activity strings (“gaming” → gaming room, “movie” → cinema, etc) and creating themed rooms dynamically. 🏆 Accomplishments that we're proud of We got fast connection times after ICE racing + timing instrumentation We managed to glue together Rust backend + WebSockets + SFU WebRTC + Three.js with only minor explosions Added screen sharing as an in-world object (the tablet) so it feels like part of the space instead of a random UI popup Made a Gaussian Splat-based map / environment work inside the world, which ended up looking way cooler than we expected for a hackathon build Modeled / rigged / animated our own assets in Blender (customized character), then got them playing nicely with Three.js Pulled off a clean deploy behind NGINX + HTTPS, serving both the realtime multiplayer server and the site and lots of easter eggs :) 🧠 What we learned Rheomesh SFU simplifies WebRTC by handling the complexity of peer connection management while keeping latency low... sometimes Cookie-based persistence is surprisingly effective for maintaining character state across sessions without database overhead Simple linear distance falloff (volume = 1 - distance/radius) works better than complex inverse-square for game-like spatial audio 🤞What's next for WebHangin We have so many more ideas for the future of WebHangin! We want to add true directional audio with Web Audio API PannerNode for left/right ear positioning. Our environments can expand with more themed rooms (beach, forest, office) and interactive objects beyond the jukebox. We could add user accounts with persistent avatars, friend lists, and private rooms. We also want to add more character types beyond cats and implement animations for wave/dance emotes. We're so proud of what we've accomplished with WebHangin and are looking forward to the next set of challenges! <div