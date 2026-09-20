---
slug: "wordpaths"
url: "https://devpost.com/software/wordpaths"
title: "Wordpaths"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 662
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Wordpaths

> Play daily puzzles, create your own word challenges, and climb the leaderboard. Simple rules, endless connections.

[Devpost](https://devpost.com/software/wordpaths) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]]

**stack** devvit, typescipt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for word paths

## Body

Application introduction Game interface Leaderboard Create Path Word Paths — Devvit Web App Inspiration The inspiration for the Word Paths Devvit Web App stemmed from a desire to bring engaging, interactive gaming experiences directly into Reddit communities. We envisioned a game that was not only fun and challenging but also deeply integrated with Reddit's unique social fabric. The idea of a word transformation puzzle , where players think and connect words at a time, felt like a perfect fit for a community-driven platform. The goal was to create a seamless, in-feed experience that encouraged both individual play and community participation through user-generated content and competitive leaderboards. What it Does Word Paths is a captivating word transformation puzzle game designed specifically for Reddit communities using Devvit Blocks. It allows users to play directly within Reddit posts, eliminating the need to navigate away from the platform. The core gameplay involves creating a path from startWord into an endWord by thinking of a current word that should relate to previous word in some way or form. Key Features User-Created Puzzles: Community members can submit their own startWord and endWord pairs for new puzzles. Approved puzzles automatically generate new Reddit posts. Dynamic Leaderboard: Points reward shorter paths and faster completion times. A real-time leaderboard fosters friendly competition. New Puzzles: Automatically posts a new puzzle daily at a scheduled time. Moderation Tools: Tools for moderators to review and manage user-submitted puzzles. How We Built It The Word Paths app was built using the Devvit web framework , leveraging TypeScript for robust and scalable code. Key Components main.tsx : Defines the interactive UI (using Blocks like VStack , Button , TextInput ). Manages local state with useState and communicates with backend via useMessage . action.ts : Server-side message handler. Configures addMenuItem and addSchedulerJob for puzzle creation, moderation, and automation. game.ts : Encapsulates core game logic (puzzle data, runs, leaderboard). Handles validation, scoring, and persistence using Redis. submission.ts : Manages user-created puzzles — validation, moderation, and creating interactive Reddit posts via the Reddit API. devvit.json : Central config file defining app permissions, triggers, menu items, and scheduler. Challenges We Ran Into Devvit Blocks Specifics: Learning its unique component model and state management and the feature we should've taken advantage of that we got to know later on . Real-time Interaction: Ensuring smooth gameplay within Reddit posts via efficient message passing. Data Persistence & Scalability: Designing Redis structures for runs, leaderboards, and submissions. Moderation Workflow: Implementing puzzle validation, moderation queues, and automated post creation. Word Validation: Current validation is basic; expanding to dictionary or graph-based checks is challenging. Accomplishments We’re Proud Of Seamless Reddit Integration: A fully interactive game within Reddit posts. Community-Driven Content: Empowering users to create puzzles and drive engagement. Robust Backend Logic: Reliable mechanics and scalable data management. Automated Engagement: Daily puzzles that keep players returning. Comprehensive Architecture: Modular, maintainable, and extensible design. What We Learned Devvit Blocks Development: Deep insights into building on Reddit with its limitations and strengths. Client-Server Communication: Best practices for async UI ↔ backend messaging. Redis for Game State: Effective use of Redis (e.g., sorted sets for leaderboards). Modular Design: Benefits of breaking features into smaller modules ( game.ts , submission.ts , etc.). Community Features: Designing for user submissions and moderation. What’s Next for Word Paths Enhanced Word Validation: Integrating dictionary APIs or word graphs. Shifting to Devvit blocks: We will shift our application to devvit blocks to enable in feed play, creating posts by user, daily new puzzles embedded in posts . Pathfinding Algorithm: Auto-check shortest paths and offer hints. Themed Puzzles & Categories: E.g., animals, food, history . User Profiles & Achievements: Stats tracking, badges, milestones. Improved UI/UX: Animations, smoother navigation, better feedback. Advanced Moderation Tools: A moderator dashboard within Devvit. Internationalization: Multi-language support. Deeper Reddit Integration: User flair for achievements, custom awards for top players. We believe Word Paths has the potential to become a beloved part of Reddit communities, fostering engagement and a love for word puzzles. <div