---
slug: "pixisle"
url: "https://devpost.com/software/pixisle"
title: "PixIsle"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 467
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# PixIsle

> PixIsle is a real-time collaborative pixel art editor where users can create, erase, and share their art on an infinite canvas.

[Devpost](https://devpost.com/software/pixisle) · hackathon [[Hack Reddit 2025]]

## Facets

**mechanism** [[realtime_stream]]

**stack** devvit, pixijs, sass, solidjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pixisle

## Body

Preview NyanCat Inspiration PixIsle was inspired by Reddit’s r/place. I’ve always been fascinated by how thousands of people came together to build something incredible, one pixel at a time. But I started wondering... what if there was no limit on the canvas? No limit on how many pixels you could draw? What if the creativity didn’t pause, didn’t reset and just kept flowing? That’s how PixIsle was born - a shared, ever-growing space where anyone can jump in, collaborate, and leave their mark in real time. What it does PixIsle is a real-time, collaborative pixel art editor with a canvas that stretches as far as you want to go. You can pan in any direction and just keep going. Is it truly infinite ? That’s up to you to find out. 😄 ✅ Add and erase pixels effortlessly. 🎨 Choose from a variety of colors to express their creativity. 👥 Collaborate in real time with others from around the world. 📤 Share their artwork as a post in the subreddit. 🌎 Watch pixel art evolve dynamically as the community contributes. How I built it PixIsle was built using SolidJS for its fine-grained reactivity, making real-time updates feel instant and smooth. For rendering, I went with PixiJS, which handles thousands of pixels efficiently without breaking a sweat. Styling is done with SASS, giving us the flexibility to keep things clean and scalable. Challenges I ran into One of the toughest parts was making sure real-time updates stayed smooth and synced for everyone, without any lag. Since the canvas can go on forever, I had to get smart with performance, using culling to only render what’s on screen, and chunk-based loading to load/unload parts of the canvas as you move around. On top of that, storing pixel data in Redis had to be super efficient to keep everything fast and snappy. Accomplishments that I'm proud of I’m super proud of how smooth the experience feels, even with real-time edits from different users, it just works. The Reddit integration via Devvit also makes it really easy for people to share their creations and connect with the community. What I learned I learned a ton about real-time synchronization, performance optimization, and how small improvements can completely change the experience. Working with Redis taught me how to handle large-scale data efficiently, and building with Devvit gave me a great intro to integrating web apps with Reddit. Every little piece added up to make a big difference. What's next for PixIsle 🛡️ Moderation tools to keep the canvas safe and welcoming 👤 Leaderboards to showcase top contributors 📱 A mobile-friendly version so anyone can join in, anywhere 🎯 Community challenges to spark creativity and bring people together PixIsle is just getting started and I can’t wait to see how the canvas evolves. <div