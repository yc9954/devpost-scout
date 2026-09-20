---
slug: "squat-showdown"
url: "https://devpost.com/software/squat-showdown"
title: "Squat Showdown"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 311
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Squat Showdown

> Challenge your friends and foes in an online squatting competition! ️‍🔥

[Devpost](https://devpost.com/software/squat-showdown) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[video_visual]] [[web_dom]]

**stack** express.js, mediapipe, node.js, react, render, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for squat showdown

## Body

Inspiration Squat Showdown was inspired by a desire to combine fitness and social interaction in a fun and inspiring way. I've discovered that, while many people wish to be active, it's often difficult to find motivation, especially when exercising alone. By introducing a competitive element and the opportunity to challenge others in real time, I hoped to build something that would make exercise feel more like a fun than a chore. The concept of short, intensive bursts of action, such as 30-second squat challenges, seemed like an ideal way to keep things interesting and accessible to everyone, regardless of fitness ability. What it does Create rooms to invite your opponents and hop directly into a video call to battle. With 30 seconds on the clock, my website's cutting-edge AI algorithm counts everyone's proper squats to see who can accomplish the most. The winner receives a shower of confetti and will be known to their friends as a squat showdown champion. How I built it Most of my game's UI and functionality were created using React, Express, Node, and socket.io. For squat detection, I used Mediapipe to utilize and interpret pose data. The backend is running on Render, while Vercel powers the front end. Challenges I ran into Utilizing socket.io to establish a real-time connection between players Time constraints (code is very hacky) Learning JS, CSS, and HTML while building the project (I've never used these before so building this probably isn't the best way to learn languages!) Designing the UI Accomplishments that I'm proud of Successfully building my first-ever React project without much coding experience Integrating computer vision for a fun and engaging activity What I learned How to use MediaPipe for pose detection How to never skip leg day ever again How to code What's next for Squat Showdown Adding more functionality (mute button, mobile compatibility etc.) improving UI/UX <div