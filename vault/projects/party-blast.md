---
slug: "party-blast"
url: "https://devpost.com/software/party-blast"
title: "ModStorm Block Party"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 584
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/web_dom"
---

# ModStorm Block Party

> A competitive VR voxel party where players meet in a shared lobby and battle through rapid-fire free-for-all mini games, mixing fast VR action with quick build-and-break gameplay.

[Devpost](https://devpost.com/software/party-blast) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[web_dom]]
  <sub>weak: document_pdf</sub>

**stack** amazon-web-services, javascript, node.js, three.js, webrtc, websockets, webxr

## Body

ModStorm Block Party is a fast-paced collection of short, frantic multiplayer party games built to be instantly playable across VR, mobile, and desktop. Inspired by classic local party games, it captures the thrill of simple rules, quick rounds, and chaotic competition with friends. We wanted to bring that energy to VR without friction. No App install or updates. Players just click a link, form a party, and jump into a rotating mix of challenges. Built with our JavaScript engine that uses the lightweight Three.js renderer, WebSockets for real-time multiplayer, WebRTC for voice chat, and WebXR support to deliver a VR-first social experience. This allowed us to focus on designing the mini-games and fine-tune the VR experience. Mini-games span four categories: collection, building, destruction, and free-for-all. Collection challenges have players gather scattered or moving targets throughout the arena. Building rounds task players with assembling creations quickly to avoid falling. Destruction challenges create chaos as players smash opponents’ builds while defending their own. Free-for-all rounds push players to out-survive, out-score, and out-maneuver friends in fast-paced arenas. Players progress through rounds together, earning points toward a final score, keeping sessions lively, replayable, and ideal for social play. Block Party’s performance profile is a key strength. The experience is around 30MB, loads quickly in the browser, and runs the same JavaScript across VR, mobile, and desktop. The multiplayer stack supports thousands of players with low latency, and WebXR ensures VR players interact naturally with controllers, while others can play via touch, keyboard, or gamepad. Challenges Faced: To stay on schedule, we prototyped a new mini-game every day, balancing creativity, gameplay variety, and technical constraints. Building a robust multiplayer party system required coding for matchmaking, session persistence, and smooth transitions. Frequent multiplayer VR playtests ended up taking a significant portion of our schedule. Keeping the mini-games small in scope also proved challenging, as developing in VR sparks so many creative ideas that simply couldn’t fit within our timeline. Looking Ahead: Expand mini-game mechanics with team modes, co-op challenges, and light puzzle rounds that provide quick mental resets between the more action-heavy sequences. Unique party avatars , replacing the default avatar to let players express individuality. Hands with Arm IK , enabling natural gestures for more immersive VR embodiment. Browser-based Editor , opening UGC creation so players can contribute mini-games to the Block Party rotation. Over time, ModStorm Block Party aims to become a living party hub - part competitive game, part social space, and part community-driven creation platform - all instantly accessible on the open web. Instructions: Type the game url into a Quest Browser tab Click the VR button to enter Immersive Mode - Note this will require one-time clicking the permission popup To enable Voice Chat , click the Microphone icon on the control menu attached to the left controller - Note this will require one-time clicking the permission popup 2-4 players gather in the center ring on the raised platform Click Start Party to begin Players are assigned to a random team color In the Round Lobby step on the center Green Button to start each mini-game After each game, players return to the Round Lobby Competition is complete after 9 games Click Return to HUB to form a new party Know Issues: (Rare) An error popup regarding the audio context, “play() failed because user didn’t interact with the document.” Refreshing the browser tab fixed the issue. (Very Rare) the Three.js controller factory failed to load the GLTF models. Refreshing the browser fixed this issue. <div