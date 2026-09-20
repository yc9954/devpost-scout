---
slug: "oneline-nr4l1c"
url: "https://devpost.com/software/oneline-nr4l1c"
title: "Oneline"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 845
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/retail_commerce"
  - "user/small_business"
---

# Oneline

> Draw it in one continuous line!

[Devpost](https://devpost.com/software/oneline-nr4l1c) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[retail_commerce]]
**user** [[small_business]]

**stack** devvit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for one line
- acknowledgments

## Body

Game Post Game Start Drawing Complete Drawing Submission Drawing Results Leaderboard Word Submission Inspiration The inspiration for this game came from wanting to create a more relaxed and casual drawing experience that wasn't focused on who is the best artist. The idea was simple: almost anyone can draw one line, and if it looks great, that's awesome - but if it looks terrible, that's part of the fun too. Traditional drawing games often intimidate people who don't consider themselves artists, but with the one-line constraint, everyone starts on equal footing. It's about creativity within constraints, not artistic perfection. What it does Players are challenged to draw words using a single continuous line without lifting their finger or mouse, then share their creations with the community for others to guess. The game features: One-line drawing constraint : All drawings must be created in a single continuous stroke Progressive difficulty system : Players unlock harder words as they level up Community interaction : Other players guess your drawings and you guess theirs XP and leveling system : Skill-based progression with achievements and bonuses In the feed : Plays directly within Reddit posts with full community features Mobile-optimized experience : Touch-friendly interface with immersive mode support How we built it Frontend (React 19 + TypeScript) Built with React 19 and TypeScript for type safety and modern React features Custom HTML5 Canvas implementation for drawing with one-line constraint validation Tailwind CSS for responsive, mobile-first styling State management using React hooks with persistent user progress Multiple game screens: main menu, drawing challenge, gallery, leaderboards Backend (Express + Devvit APIs) Express.js server handling game logic and data persistence Redis integration via Devvit's Redis API for user progress and drawing storage Word management system with community submissions and voting Real-time leaderboards using Redis sorted sets Smart guess validation and XP calculation system Progressive Difficulty System : The game features a dynamic word pool that adapts to player skill level. Words are categorized by difficulty (Beginner → Master), and players unlock more challenging content as they progress. Challenges we ran into Mobile Immersive Mode : One of the biggest technical challenges was creating a seamless mobile experience within Reddit's WebView environment. I implemented a sophisticated handoff system between inline and immersive modes, allowing users to draw in fullscreen on mobile while maintaining state consistency. Accomplishments that we're proud of Design Philosophy The one-line constraint democratizes the drawing experience. Players of all skill levels can participate and have fun, which was my core goal from the beginning. Community Features I built a complete social ecosystem with leaderboards, achievements, word submissions, and community voting - all integrated seamlessly with Reddit's existing social features. What we learned WebView Development Challenges Working within Reddit's WebView taught me about the complexities of embedded web applications, especially around mobile gesture handling. Community-Driven Game Design Building for Reddit's platform taught me how to design features that leverage existing community dynamics while adding new interactive elements. Real-time State Management Managing game state across multiple screens and modes, especially with the immersive handoff system, taught me valuable lessons about state synchronization and data consistency. What's next for One Line Enhanced Drawing Tools Multiple brush sizes and colors while maintaining the one-line constraint Expanded Social Features Team drawing challenges where multiple players contribute to one drawing Custom word packs created by communities Gamification Improvements Seasonal events with special word themes Prestige system for high-level players The game represents a successful fusion of creative constraint, community interaction, and technical innovation, proving that simple concepts can create engaging experiences when executed thoughtfully within the right platform. Acknowledgments While the core game mechanics, and backend systems are completely original, I've incorporated some excellent open source UI components to enhance the visual experience: Wheel of Doom Visual Components : Original spinning wheel mechanics and Grim Reaper SVG artwork by Ryan Mulligan Used under MIT License for the visual foundation of our interactive wheel system I've extensively modified and integrated these components with our custom game logic, Redis state management, and Reddit API integration Wheel of Doom License Copyright (c) 2025 by Ryan Mulligan (https://codepen.io/hexagoncircle/pen/bGqVyxm) Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. <div