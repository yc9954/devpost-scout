---
slug: "pixelsandbox"
url: "https://devpost.com/software/pixelsandbox"
title: "PixelSandbox"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 205
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
---

# PixelSandbox

> Pixel Sandbox is a real-time falling-sand simulation for Reddit where you build worlds, freeze time, and share your creations as playable posts.

[Devpost](https://devpost.com/software/pixelsandbox) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]

**stack** devvit, react, rust, webassembly

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for pixel sandbox

## Body

Inspiration classic falling-sand games like Powder Game user-generated content platforms like Super Mario Maker bringing creative physics toys to Reddit communities What it does A falling-sand physics simulator where users paint with 18+ materials (sand, water, fire, lava, plants, etc.) and watch them interact in real-time. Users can share their creations as Reddit posts, and anyone can load those builds, modify them, and share their own versions—creating a chain of community remixes. Users get to experiment with physics, create art, and build upon each other's work, all natively on Reddit. How we built it Devvit Web, Rust/WASM for physics simulation, React Challenges we ran into Getting smooth 60fps physics simulation in WebAssembly while keeping the bundle size small for Reddit's platform was tricky. Also implementing the build sharing system so users could seamlessly load and remix each other's creations. Accomplishments that we're proud of Creating a full physics sandbox with 18 interactive materials and a complete sharing system in a short time. The remix feature where users can build on each other's work turned out really well! What's next for pixel sandbox More materials and interactions! A level browser within the in game UI. Really Any cool feature I can think of implementing 😁 <div