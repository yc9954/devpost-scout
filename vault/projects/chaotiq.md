---
slug: "chaotiq"
url: "https://devpost.com/software/chaotiq"
title: "ChaotIQ"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 512
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# ChaotIQ

> ChaotIQ turns any learning topic into a fast-paced multiplayer quiz with powerups, sabotages, and real-time competition—making studying chaotic, fun, and unforgettable.

[Devpost](https://devpost.com/software/chaotiq) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** chatgpt, css, html, javascript, node.js, socket.io

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chaotiq

## Body

Homepage Join a quiz Sabotage popup Power up Host a Quiz Lobby Inspiration ChaotIQ was inspired by a simple thought: why does studying feel like a chore when games feel like an adventure? As students ourselves, we realized that most learning platforms are passive, predictable, and—let’s be honest—boring. I wanted to build something that felt chaotic, competitive, and fun while still helping people learn. The “Make Learning Fun” hackathon theme pushed us to rethink education as a shared, playful experience rather than a solo grind. I imagined a world where quizzes feel like battles, study groups feel like game lobbies, and learning feels like leveling up. That became the blueprint for ChaotIQ. What it does ChaotIQ turns any study topic into a chaotic multiplayer quiz battle. Players can: Create a quiz room based on any topic Select their grade level (Middle School, High School, or College) Compete with friends in real time Use power-ups and sabotages to help themselves or disrupt others The result? A high-energy learning game where every round is unpredictable, competitive, and ridiculously fun. How we built it I built ChaotIQ using: Node.js + Express for the backend Socket.IO for real-time multiplayer communication OpenAI APIs to generate topic-specific quiz questions HTML/CSS/JS for the front-end Each player connects to a shared game room. The host triggers the quiz, and the server manages the question sequence, scoring, and item effects. The client listens for updates and displays everything in real time with a clean, responsive UI. Challenges we ran into I faced plenty of chaos while building ChaotIQ: Real-time sync issues: Making sure every player’s screen updated in sync required careful socket event handling. Question generation consistency: Ensuring OpenAI always returned valid JSON took multiple formatting and validation layers. Game balance: Designing power-ups and sabotages that were fun but not unfair took experimentation. Accomplishments that we're proud of Built a fully functional multiplayer quiz game from scratch Achieved smooth, real-time gameplay Created a unique power-up system that adds strategy and chaos Designed a clean, modern UI with responsive modals Implemented topic- and grade-aware question generation using AI Turned studying into something people actually want to do Seeing the game playable and fun for the first time was incredibly rewarding. What we learned We learned how powerful real-time interactivity can be when blended with education. We learned how to structure multiplayer logic, validate AI-generated content, and build user interfaces that feel lively and intuitive. And most importantly, we learned how creativity, teamwork, and chaos can transform a simple quiz into a memorable experience. What's next for ChaotIQ I'm excited to expand ChaotIQ beyond topic-based quizzes. Next steps include: Allowing users to paste YouTube links and automatically generate quizzes from lecture videos Letting players upload PDFs, lecture notes, or slides to auto-create question sets Adding more power-ups, animations, and game modes Creating public rooms, leaderboards, voice chats, and long-term progression Adding visual themes and accessibility improvements ChaotIQ is just getting started—our goal is to turn studying into the most fun part of learning, and we’re excited to keep building toward that vision. <div