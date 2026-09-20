---
slug: "tile-slide-with-builder"
url: "https://devpost.com/software/tile-slide-with-builder"
title: "Tile Slide with Builder"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 825
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
---

# Tile Slide with Builder

> Reddit's daily brain-twisting tile challenge builder

[Devpost](https://devpost.com/software/tile-slide-with-builder) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]

**stack** css3, devvit, html5, javascript, scss

## How they structured the write-up

- 🎯 inspiration
- 🎮 what it does
- 🛠️ how i built it
- 🔥 challenges i ran into
- 🏆 accomplishments i'm proud of
- 📚 what i learned
- 🚀 what's next for tile slide with builder

## Body

Main Menu Builder Menu Testing a Level Before Publishing Animated "How To Play " Section Game Play Tile Slide - Reddit's Community Puzzle Playground 🎯 Inspiration Remember that feeling when you finally solve a puzzle that's been haunting you for hours? Now imagine creating that experience for thousands of Redditors. Tile Slide was born from a simple question I had: "What if every Reddit post could be a unique, playable puzzle created by the community?" After experimenting with block mechanics in my previous game, I discovered Devvit WebViews opened up incredible possibilities. I wanted to build something deceptively simple - a game you'd understand in 10 seconds but still be playing 10 days later. 🎮 What it does Tile Slide transforms each Reddit post into an interactive 6×6 puzzle battlefield. Players manipulate five distinct tile types: Arrow Tiles - Click to launch them in their direction, bulldozing everything in their path Power Arrows (2x Push) - Orange tiles that push twice, adding strategic depth Cracked Tiles - Fragile pieces that shatter on click or can be pushed strategically Drill Tiles - Click to create new holes, opening up creative solutions Block Tiles - Stubborn pieces that only move when pushed Holes - Your targets to clear the board But here's the twist: Every Redditor is also a level designer. The built-in editor lets you craft puzzles and publish them instantly as playable Reddit posts. Each level maintains its own leaderboard, turning every puzzle into a competitive arena where every second matters. 🛠️ How I built it I crafted Tile Slide using vanilla JavaScript with modular design patterns, keeping everything lightweight and dependency-free. The frontend runs on pure JS with SCSS for responsive and maintainable styles. The game uses Devvit WebViews for seamless Reddit integration, with server functions handling data persistence through Redis. Each level is stored as JSON, while leaderboards leverage Redis sorted sets for real-time updates. I implemented custom tile physics with smooth CSS transform animations, absolute positioning for pixel-perfect movement, and a transform-based scaling system that maintains gameplay quality across all devices. The entire game loads in under a second, even on mobile connections. 🔥 Challenges I ran into The Tile Chain Reaction Problem : Implementing push mechanics where arrows could push multiple tiles in sequence without skipping or overlapping required reverse-iteration through tile chains and careful state management. Double Arrow Complexity : Power arrows that push twice needed special handling - finding the arrow's new position after first push, then triggering a second push with proper animation timing. WebView ↔ Reddit Communication : Initially I used timeouts for async operations. Learned to wrap Devvit callbacks in Promises for cleaner, more reliable data flow. Responsive Tile Positioning : Tiles use absolute positioning for animations, making responsive design challenging. I solved this by scaling entire game board containers at different breakpoints rather than individual tiles. Level Data Persistence : Storing complex JSON structures (6×6 arrays with tile states) in Redis while maintaining fast retrieval for the leaderboard system was trickier than expected. 🏆 Accomplishments I'm proud of Shipped a complete game in 7 days with 12+ tile types, full animations, and sound Built a zero-friction level editor - no login, no uploads, just create and publish Achieved sub-second load times even with animated backgrounds and sound assets Created truly responsive gameplay - works flawlessly from iPhone SE to 4K monitors Implemented real-time per-level leaderboards using Redis sorted sets Zero external dependencies for core gameplay (pure vanilla JS) 📚 What I learned Devvit WebViews are incredibly powerful : The ability to run full web apps inside Reddit posts opens up possibilities I hadn't imagined Community features > Solo features : The level builder became more popular than the campaign mode within hours of testing Performance matters on mobile : Optimizing from transform: scale() to container-based scaling improved mobile FPS by 40% Redis is more versatile than expected : Using it for both JSON blob storage (levels) and sorted sets (leaderboards) in one app Simple mechanics scale better : Arrow tiles are easy to understand but create emergent complexity when combined 🚀 What's next for Tile Slide with Builder Immediate Updates: Ice Tiles : Slide until they hit something Teleporter Pairs : Strategic warping across the board Switch Tiles : Toggle walls on/off Level Voting System : Best puzzles rise to the top Community Features: Daily Challenge Mode : One puzzle, entire subreddit competing Puzzle Packs : Curated collections by difficulty Ghost Mode : See how top players solved it Co-op Puzzles : Two players, one board, chaos ensues Technical Roadmap: Implement undo/redo system using Command pattern Add replay functionality for leaderboard runs WebSocket support for real-time multiplayer Level solution validator to ensure all published puzzles are solvable Tile Slide isn't just a game—it's Reddit's first community-powered puzzle platform. Every post is playable, every Redditor is a designer, and every solve is a chance to claim the leaderboard. Ready to slide? Your puzzle awaits! 🎮 <div