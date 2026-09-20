---
slug: "metawarehouse"
url: "https://devpost.com/software/metawarehouse"
title: "deBunker"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 569
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/patient_family"
  - "substrate/geospatial"
---

# deBunker

> A decentralized VR-ready metaverse, connecting people in immersive, interactive spaces.

[Devpost](https://devpost.com/software/metawarehouse) · hackathon [[Supernova]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[vision_ocr]]
**domain** [[health_clinical]] [[housing_homeless]]
**user** [[patient_family]]
**substrate** [[geospatial]]

**stack** c#, javascript, unity, webrtc, webxr

## How they structured the write-up

- intro
- inspiration
- how is it made
- things we're proud of
- challenges we ran into
- what we learned
- what's next for debunker

## Body

Intro deBunker is another crucial step on the road to decentralised, community-owned immersive VR spaces. Built by the creators of The Island Collective, it strives to go one step further in terms of interaction, communication and performance. In a move away from the tropical topside, this steel and concrete subterranean shelter has several game rooms, each containing one of our current experiments. The main attraction is a two-player baseball trainer, where one person takes charge of loading the pitching machine while the other gets in some batting practice. Inspiration A need for decentralised, p2p meeting places, Quentin Tarantino, the sound of my neighbour's leaking gutter and a desire to fire baseballs at my friends. How is it made This experience is the result of the careful orchestration of the Unity game engine, WebXR and WebRTC, plus a whole load of patient development hours crafting cutting-edge interaction, communication and rendering tools that, when integrated with the Internet Computer’s canister architecture, let you walk around inside the blockchain, and have a chat with your friend while you train your baseball swing. Things we're proud of This space brings a few key developments that we're proud to have developed especially for the Supernova Hackathon. Jedi model for far-near iteration; trigger distance wields, grip for near carry and grip-while-trigger for bringing distant objects into the hand. This was inspired by watching people face-plant into tables while trying to pick things up. Performance level-up; now able to maintain 72 fps on Quest 2 without audio streaming and more than 60 fps with audio. New techniques for building-scale optimisation were also developed, leading to shorter load times and lower latency while simultaneously increasing complexity. Fully spatial VR audio streaming; the feed from the other person's microphone is broadcast from their avatar, allowing for directional sound and roll-off. The localised sound gives a whole new level of immersion and interactivity. New underground environment with high-performance textures, improved occlusion mapping and lighting optimisation. Challenges we ran into Streaming to Unity's AudioSource component and blending tools and logic from the multithreaded browser environment and the single-threaded Unity loop. There are still limitations to this approach, resulting in a one-second audio latency, but we are now extremely close to a more high performance solution. The WebRTC signaling server is not yet running on a canister, although progress has been made in identifying the most promising routes to solve this, as well as improving the scalability and performance of the p2p network. This experience was tested on Firefox Reality and Wolvic. Differences between browsers put cross-compatibility out of reach for this hackathon - Chrome currently has an issue receiving audio (desktop platform). In Oculus browser (VR), there is also an issue receiving interaction events. What we learned There is still a huge amount to learn and explore when it comes to social interaction and gaming on the Internet Computer. Everything from the hardware-driven optical depth-of-field to non-deterministic game mechanics informs the design and development of the VR metaverse. What's next for deBunker The future is extremely bright with lots of possible avenues to explore, both above ground and below. In features such as cross-canister operability (from Candid) and the use of fungible tokens, we can improve the reach and breadth of the framework. With non-fungible tokens and liquid democratic systems of the SNS, we can strengthen the personal relationships within the community, guiding membership and recognition for community leaders. <div