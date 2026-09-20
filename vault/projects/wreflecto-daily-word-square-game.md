---
slug: "wreflecto-daily-word-square-game"
url: "https://devpost.com/software/wreflecto-daily-word-square-game"
title: "Wreflecto - A Daily Word Square Game"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 935
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Wreflecto - A Daily Word Square Game

> Inspired by an ancient word puzzle, Wreflecto is like sudoku meets wordle. Test your word skills, earn flairs, climb leaderboards, build streaks and share solutions in this addictive brain teaser.

[Devpost](https://devpost.com/software/wreflecto-daily-word-square-game) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** css, devvit, html, javascript, react, redditapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wreflecto - a daily word square game

## Body

Reddit Post With Splash Screen Landing Page for Choosing Game or Viewing Leaderboards Example Wreflecto Game Viewing Specific Hall Of Fame Leaderboards Wreflecto - A Daily Word Square Game Inspired by an ancient word puzzle, Wreflecto is like sudoku meets wordle. Test your word skills, earn flairs, climb leaderboards, build streaks and share solutions in this addictive brain teaser. Inspiration My wife loves puzzles. Every now and then she would sketch a word puzzle inspired by one of the world's oldest word puzzles (Sator Square). I shared her sketch on Reddit and hundreds responded with their unique solutions. I turned her paper puzzle into a digital daily game you can play right here on Reddit and share your unique solution, compare with others, track your streak and stats, earn medals and achievements, and most importantly - HAVE FUN! What it does Wreflecto brings one of the word's oldest puzzles, the Sator Square, to Reddit with two unique gameplay modes - symmetrical word squares in Mirror mode or intersecting word squares in Cross mode. Built directly into Reddit, users can play daily puzzles, build streaks, earn achievements, share solutions as comments, and compete on leaderboards. The game works seamless on mobile, tablet, and desktop, and has already generated excellent community engagement with hundreds of Redditors sharing creative solutions and strategies. The game creates a vibrant daily community ritual where redditors: Solve fresh daily puzzles. Build streaks, earn achievements and flairs, and compete on leaderboards. Share their unique solutions as Reddit comments. Engage in discussions about different solution approaches. How we built it Wreflecto is built on Devvit using React, TypeScript, Javascript, html and css, creating a seamless Reddit-native experience. The architecture includes: Frontend : React components with Tailwind CSS with additional vanilla Javascript, html and css for responsive gameplay, real-time word validation, and smooth animations. Backend : Express server handling puzzle generation, user statistics, and leaderboard management. Data Layer : Redis integration for persistent user progress, streaks, and cross-device synchronization. Game Logic : Custom word validation service. Mobile and Desktop Experience : Provides unique keyboard experience for desktop while keeping high performant mobile experience. Shared the original pen & paper version on Reddit, received hundreds of solution attempts and feedback comments, then built features and prototypes based on actual reddit engagement and feedback. It combines fresh recurring puzzles from the game with unique UGC from user's solutions. Devvit and Redis helped bring leaderboards, comments, comparisons, awards, flairs to the game without any need for user credentials creation and management. Challenges we ran into Cross-Platform Compatibility : Creating delightful UX with responsive gameplay that works seamlessly across mobile, tablet, and desktop with optimized touch controls for mobile but keyboard and mouse keys for desktop users. Complex State Management : Implementing daily puzzle persistence while maintaining smooth gameplay across device switches and session interruptions required careful Redis integration and state synchronization. Real-time Achievement Tracking : Building live leaderboards and achievement tracking that update instantly across all players while maintaining data consistency. Accomplishments that we're proud of Proven Reddit Engagement : Before building the Reddit version, the game's early posts garnered hundreds of comments with users sharing and comparing solutions, validating the concept's Reddit appeal. Example posts: r/words - 100s of comments with people trying the game and writing their solution. r/ENGLISH - many word enthusiasts trying the puzzle and replying with their solution and discussing with others. r/iosgaming - several people downloading the game and trying. Community-Driven Features : After posting the pen and paper version, Redditors organically started using Reddit spoiler tags to share their solutions, creating suspenseful reveals. This community behavior is what inspired the spoiler-style sharing directly included into the game, making solution sharing feel naturally Reddit-native. Polished Reddit Integration : Polished, production-ready game that feels like a natural part of Reddit, with intuitive sharing mechanisms, leaderboards, and community features. Built robust architecture handling real-time validation, cross-device persistence, and complex leaderboard calculations while maintaining excellent performance. Delightful UX and Engaging Gameplay : Designed a clean, minimalist, and beautiful interface with intuitive gameplay, smooth animations, instant feedback, and satisfying visual cues that make puzzle-solving satisfying. Multiple redditors have commented on the clean design and beautiful interface . Privacy-first Social Features : Not collecting data that the app doesn't need. Designing sharing mechanisms that respect user consent and preferences. Sharing is limited to r/wreflecto and provide clear communication for opting in and opting out. Balancing Difficulty and Variety : The 5x5 is hard and difficult. The 4x4 is easy and super engaging but in Mirror because first letter is irrelevant, this poses a challenge in providing variety. So included logic to generate 5x5 on weekends to keep variety. This will be further refined based on engagement. What we learned Cross-Device UX Design : Different platforms require fundamentally different interaction patterns. What feels intuitive on mobile (touch/swipe) breaks desktop flow, requiring platform-specific UI approaches without overcomplicating the codebase. Reddit Community Support : Redditors actively participate in reddit-y experiences. Sharing a hand-drawn puzzle image generated hundreds of enthusiastic responses and support. Persistent State Management : Balancing accessibility to past puzzles while preserving legitimate streak progression required thoughtful logic and consideration. Platform API Constraints : Reddit's API limitations (splash screen image restrictions, button overlay) forced creative workarounds. What's next for Wreflecto - A Daily Word Square Game Collaborative Solving : Team puzzle modes where multiple redditors can contribute to solving larger, more complex word squares. Monthly Tournaments : Monthly Reddit competitions with special flairs and recognition for top performers. Community Partnerships : Engage with language learning and vocabulary subreddits and communities to link word results to actual definition/pronunciation etc. <div