---
slug: "gotour-vr"
url: "https://devpost.com/software/gotour-vr"
title: "GOTOUR VR"
hackathon: "World Hackathon Day"
winner: true
words: 846
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# GOTOUR VR

> Cross Platform Realtime Full Dive WebVR with Smart Assistant to Visualize and Experience Tourism Objects Virtually but Realistically.

[Devpost](https://devpost.com/software/gotour-vr) · hackathon [[World Hackathon Day]]

## Facets

**mechanism** [[structural_withholding]] [[voice_speech]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** 360, ar/vr, assistant, cinema4d, css, figma, firebase, google-cloud, google-maps, html, javascript, mozilla-web-speech-api, pwa, realtime-database

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for gotour vr

## Body

Landing Page Tourism Information Detail List of Tourism Objects Gallery 360 View (VR Mode On) 360 View (VR Mode Off) Integrated Multiplayer VR Room Inspiration I'm really inspired by how amazing AR/VR could change and evolve the current technology into the next level where it can change how we interact with everything, starting from interacting on media, our daily activities, people and even places where we can travel, the true power of Virtual Reality is that we can create an infinite world with no any constraint or boundary which is the greatest approach to do something that we cant do in the real world at a usual state especially in this epidemic where most places are closed. So because of this, it inspire me to build such WebVR called GOTOUR VR. What it does This WebVR will create an infinite world where we can travel to any listed tourism objects as much as we can with a more engaging way to interact, more interesting, and more realistic but virtually experience. GOTOUR VR Architecture This WebVR is be able to : Experience tourism objects virtually but realistically. Get tourism objects detail information. Send message to the tourism object. Call the tourism object. Get a route and direction to get to the tourism object. Set VR Mode to make the experience more realistic. Interact with other people inside VR Room by moving their avatar and talking with their microphone. VR Mode Flow How I built it I built this WebVR with these frameworks and tech-stacks : Aframe Js Aframe Js is the core of WebVR javascript library that i use for this project. Networked Aframe Networked Aframe is a powerful Aframe Js component that used for integrating WebRTC into our WebVR with a very easy and simple way! in this case our WebVR will be able to send a realtime data socket into our WebVR which can create a multiplayer world that many users can join, send and update user's 3D avatar position and user's voice to the WebVR, at this state this WebVR can be a pure virtual world that we can interact with. Firebase Realtime Database and Hosting Since this is Virtual Reality Project, it is essential to use Realtime Technology so that we don't have to keep refresh the page which will take a high load and rendering time, in this case i'm using Firebase Realtime Database to read and store the data that needed in this project, and also i host this WebVR in Firebase Hosting since Firebase is powerful, so i can integrate more feature with other Firebase technology easily in the future. Mozilla Web Speech API In order to make the assistant can speak and understand what we are saying, i'm using Mozilla Web Speech API since this is the easiest way to implement Text-To-Speech and Speech-To-Text with a good example. Figma For the 2D assets that i need to put on the 3D world of WebVR, i'm using Figma since it is really simple but powerful. Cinema 4D For the 3D assets that i'm using, especially for the assistant avatar, i'm using Cinema 4D, since it is really easy to use with a great performance for the result, at least i'm already used to with this long time ago. Challenges I ran into Challenges that i ran into are really a lot! those are : Rendering Time So this is the rendering graph in WebVR, rendering time is one of the biggest challenge to build WebVR especially with a lot of assets, models, and complex system, and so far this still be the weakness of this WebVR since i'm still focus on building the WebVR first rather than make it lighter with some techniques and some libraries. Requirements and Compatibility Since WebVR technology is still kind of new, and this is a Cross Platform project so there are a lot of compatibility issues, especially users who are using old browser, phone, operating system, slow internet speed might having a various issue, in that case i was trying a lot of browser with various versions to get the best performance when i'm recording this for the video. Accomplishments that I'm proud of Accomplishments that i'm proud of is even with those challenges i was really excited that i was be able to built such a WebVR since to be honest i never seen other WebVR like this, so i'm so happy that all my AR/VR experiements and hardwork really paid me off with how this project has been built successfully, even there are still need a lot of improvements. What I learned Innovation is really important, that's where all successful story is coming from, in that case we should not afraid of failure because everything has its own pace to get to the finish goal, remember that consistency is the key :D What's next for GOTOUR VR Performance Improvements Compatibility Improvements Add more Tourism Objects Add a user authentication Improve the multiplayer feature where all people can gather together, meet and talking together in the tourism virtually with their own avatar. <div