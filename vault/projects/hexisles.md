---
slug: "hexisles"
url: "https://devpost.com/software/hexisles"
title: "HexIsles"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 402
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# HexIsles

> A real-time community-driven world-building game using Pixelart style Hex tiles!

[Devpost](https://devpost.com/software/hexisles) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: agriculture_food</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** devvit, kiro, phaser.js, solidjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for hexisles

## Body

Loading World Tile Browser Farm Coast Flora Community Create Inspiration I have always been fascinated by collaborative creativity and how people online can come together to build something beautiful and unpredictable. Inspired by r/place and classic hex-based strategy games, I wanted to create a shared space where anyone could shape a living world. That idea became HexIsles, a real-time collaborative world builder using pixel art hex tiles. What it does HexIsles is a real-time community-driven world-building game using pixel art hex tiles. Players can place tiles on a shared canvas, choosing from more than a thousand tiles across four layers: ground, transitions, roads and rivers, and objects. They can also create their own tiles, publish them to the community, and use tiles made by others. For focused creativity, users can switch to private worlds and use an integrated chat for coordination. How I built it I built HexIsles with SolidJS and TailwindCSS for the front end, and PhaserJS for rendering and grid management. The backend runs on Devvit Web and uses its real-time services to handle collaboration between players. Redis is used for fast and efficient storage of world states and tile updates. One of the biggest accelerators during development was Kiro. Its specs feature allowed me to quickly implement the UI and required APIs. It also made handling communication between the SolidJS frontend and Phaser scenes much easier, significantly improving development speed and iteration time. Challenges I ran into One of the challenges I faced was handling the hex grid-based tiling system, especially with pixel art tiles that required precise alignment. After some tweaking with Kiro, I was able to figure out the math for accurate conversions between world coordinates and hex coordinates. Another major challenge was efficiently loading and rendering base64-encoded images inside Phaser scenes, which Kiro helped me with. Building an intuitive tile creation and publishing flow took several design iterations to make it accessible and seamless for players. Accomplishments that I'm proud of I am proud of building a full real-time collaborative experience from scratch. Creating a system where players can not only build maps but also design and share pixel art hex tiles feels rewarding. What's next for HexIsles Next, I plan to add a creator marketplace for sharing and monetizing pixel art tiles using an in-game currency. I also want to introduce procedural world generation and improved moderation tools to enhance collaboration and community safety. <div