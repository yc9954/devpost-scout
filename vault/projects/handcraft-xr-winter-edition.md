---
slug: "handcraft-xr-winter-edition"
url: "https://devpost.com/software/handcraft-xr-winter-edition"
title: "HandCraft XR: Winter Edition"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 591
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# HandCraft XR: Winter Edition

> A cozy Mixed Reality sandbox where you build a festive miniature Christmas Market with nothing but your hands—calm, tactile, and full of holiday magic.

[Devpost](https://devpost.com/software/handcraft-xr-winter-edition) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** havok, iwsdk, three.js, typescript, webxr

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for handcraft xr

## Body

Build tiny world right on your table Pick objects from the tablet Snap them on the surface Decorate Decorate more :) Inspiration I love programming, VR, and building things. Naturally, I wondered: why not create a little thematic playground - something like virtual LEGO? A winter theme felt perfect: quiet snow, warm lights, and a tiny Christmas Market that you can bring to life piece by piece. What it does HandCraft XR is a calm Mixed Reality sandbox where you use natural hand gestures to build a festive miniature Christmas Market on a virtual table. You can: Pick blocks from a floating tablet Pinch to spawn them in your hand Scale, rotate, and position them intuitively Snap pieces onto the table or attach decorations to other objects Grab and throw away unwanted pieces Watch snow fall and clouds drift overhead Build a peaceful winter village that automatically saves and loads It’s simple, tactile, and relaxing - a tiny holiday world you create with your hands. How I built it The experience is built specifically for Meta Quest devices using Immersive Web SDK, Three.js, WebXR, and a fully hand-tracked interaction system. It runs in the Quest Browser without installation. All interactions use the WebXR Hand Tracking API, and the trailer footage was recorded directly from a Meta Quest 3 in a standalone mode. Core systems include: A custom pinch-based spawning mechanic Two-hand scaling/rotation with visual outlines Snapping logic for table placement and decoration attachment A virtual tablet UI with paginated block icons A lightweight lighting setup optimized for standalone performance Instanced meshes, dynamic batching, BVH acceleration, and adaptive shadow update system for smooth WebXR performance Automatic save/restore via local storage All assets and interactions were designed to run comfortably and consistently on standalone devices through the browser. Challenges I ran into Performance in WebXR : Standard materials and shadows were too heavy, so lighting had to be redesigned around lighter, more stable options. Missing features in Immersive Web SDK : To achieve the interaction patterns and stability I needed, I studied, forked, and extended the SDK: https://github.com/evstinik/immersive-web-sdk Limited time for content : The block library is curated but small, so prioritizing which items give the most “holiday feel” was important. Accomplishments that I'm proud of A fully hand-tracked building system that feels natural and intuitive A single-pass outline effect implemented via the stencil buffer Efficient shadows using an adaptive, on-demand shadow system with a dedicated micro shadow camera Smooth performance even with many objects, shadows, mixed reality, physics and UI A cozy, relaxing atmosphere Getting it all done within limited time, while keeping the core experience polished Made it from scratch in just a month during the competition What I learned How to structure a WebXR project using ECS architecture How stencil buffers work How to identify CPU or GPU bottlenecks, and distinguish vertex-bound from fragment-bound performance issues How to build a dynamic batching system with BatchedMesh and improve interactions using instance-based BVH structures How to optimize shadows to be able to run on standalone Quest 3 device What's next for HandCraft XR Future improvements I'm excited about: WebRTC-based multiplayer building with friends Sharing worlds or exporting creations Night mode with warm lights and glowing decorations People and animated elements to bring the Christmas Market to life More interaction types (stacking, attaching objects, advanced snaps) Expanded sound design with more satisfying feedback and ambience Additional themed kits (Horror Mansion, City, etc.) This version lays the foundation, and I'm excited to grow it into a richer, more expressive Mixed Reality building experience. <div