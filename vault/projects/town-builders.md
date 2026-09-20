---
slug: "town-builders"
url: "https://devpost.com/software/town-builders"
title: "Town Builders"
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 695
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# Town Builders

> Place blocks to build with your friends anything, anywhere using Town Builders, a geospatial and augmented reality game prototype.

[Devpost](https://devpost.com/software/town-builders) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** babylonjs, babylonnative, libdatachannel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for town builders

## Body

Demo in Paris at Jardin du Luxembourg Inspiration This Minecraft Earth trailer describes the core ideas behind Town Builders. Although it inspired me for key functionnalities such as building, multiplayer and geospatial capabilites, I want to make it my own with a unique gameplay design after the submission. The Minecraft Earth game was aborted in 2021. It did not reach the functionnalities one could see in the reveal trailer. And it seems to me that the hype was not followed by a game at the level of the community expectancy. As I am myself a minecrafter, I jumped on the idea of creating a better blocky game after experiencing with WebXR last September. I want to make a game close to its community, with a modding API and events to empower every player's creativity. Technically, I want to focus on multiplayer and networking as it enables to share geospatial experiences not only in AR games but also in architecture for instance as this project could become a framework for multi user/player AR experiences. I was already trying solutions, and experimenting since October 2022 and I finally chose to start from bottom around January 1st 2023 with a new stack described below. I saw the contest on the Google ArCore documentation front page that same week and started rushing for the contest. What it does We can place a building area, geospatially located, with anyone around able to join using the app. Then we can place and break blocks. The multiplayer is unstable as for now and works best with 2 players. How I built it I used BabylonJs with a fork of BabylonNative for the rendering and core functionnalites including augmented reality with ArCore, ArCore Geospatial and networking. I upgraded the version of ArCore used by BabylonNative to v1.35.0 in order to use geospatial anchors. I also included libdatachannel to enable multiplayer networking through WebRTC and signaling WebRTC via websocket. I compiled libdatachannel with OpenSSL from the AAR ndk port . The gameplay was developed in JavaScript and exposed to the JavaScript runtime after a compression using Webpack making it easier to import. The backend part is a Python websocket server sending each message to every other connected client. An additionnal STUN/TURN server, Violet is used to ensure WebRTC connection establishment. I am hosting the backend myself. Challenges I ran into Understanding the architecture of BabylonNative while including libdatachannel was a though challenge. Delivering a somehow usable game was another difficult point. Even with the few provided functionnalities working as expected, the game is far from done. Asking my girlfriend her phone to debug multiplayer for several hours. Accomplishments that I am proud of Developping a base for almost each core functionnality. There is for now a base for networking, rendering a GUI through BabylonGUI, placing and breaking blocks and last but not least, doing it geospatially! This enables further developments in every directions while knowing that every functionnality can be improved. Developing the project while attending class was very challenging. What I learned This whole project and dependencies where very new to me, I learned a lot and everyday. Here are a few: I learned some C++ while adding a NativeRTC plugin or extending ArCore implementation to my BabylonNative modification. I also learned about the WebRTC specification and signaling. I improved my 3D and BabylonJs skills. I learned that GLTF 3D file format is right-handed and BabylonJs is left-handed by default. It is useful when importing meshes. It was also a great experience to work under a short deadline and to test the app with my friends. What's next for Town Builders As I had this project in mind for a few months now, here is an overview of the upcoming developments and functionnalities: A better multiplayer using Django, Django Channels and Redis as a backend for signaling and storing players data and constructions. A use of the Depth API for the supported phones to display blocks behind people or environnment. Terrain anchors automatically created in public parks and places using geographic data. And with these developements will come: A lot of gameplay functionnalities on every scope: collecting of resources, persitent builds, events... <div