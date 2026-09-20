---
slug: "thread-square"
url: "https://devpost.com/software/thread-square"
title: "Thread Square"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 462
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
---

# Thread Square

> A subreddit-specific community experience app where you express yourself with your unique Snoo avatar while interacting with other community members in real-time like never before!

[Devpost](https://devpost.com/software/thread-square) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]

**stack** devvit, react, reddit, web

## How they structured the write-up

- inspiration
- what it does
- what’s next for threadsquare

## Body

Demo PlayThrough on iPhone From static threads to real-time threads — that’s ThreadSquare. Inspiration The traditional Reddit experience is powerful for discussion but limited by its static nature. Posts and comments happen over time, not in real-time. You can’t see who’s online, you can’t move through a shared space, and you can’t feel the presence of your community. We wanted to change that. ThreadSquare was born from the idea that a subreddit could be more than a scroll of threads — it could be a living world . A space where members don’t just read each other’s words, but walk beside each other, chat naturally, and connect instantly. By blending the familiarity of Reddit with the immediacy of multiplayer worlds, ThreadSquare reimagines what subreddit interaction can be — no refreshes, no waiting, no static posts. Just a continuous, living community experience built on Devvit. What It Does ThreadSquare turns your subreddit into a real-time, interactive hangout space powered by Reddit’s Devvit platform. Every user appears as their unique Snoo avatar inside a 50x50 procedurally generated world filled with grass, mushrooms, and rocks. Users can move freely, chat in real-time, react with emojis, and explore together. Messages appear as floating chat bubbles above avatars, fading naturally after a few seconds, creating fluid, spontaneous interactions. Emoji reactions are visible to everyone, allowing instant, expressive communication. The system ensures smooth community flow with smart spawning — new users always appear on empty tiles — and collision detection to prevent overlapping or clipping through obstacles or other avatars. A live member list shows who’s online and where they are, while clicking any Snoo reveals that user’s Reddit profile. Moderation and safety are core to the experience. ThreadSquare integrates directly with Reddit’s moderation system. Moderators can ban users instantly, review reports via Modmail, and enforce actions in real-time — with no refresh needed. Banned users are immediately removed from the space, and moderators can choose between temporary or permanent bans with custom messages. ThreadSquare supports up to 2,000 concurrent users per room, with Redis-powered state management and Devvit realtime channels ensuring seamless updates across all clients. The result is a subreddit experience that feels alive. From static threads to real-time communities — that’s ThreadSquare. What’s Next for ThreadSquare Next, ThreadSquare will go beyond social presence and start integrating Reddit content directly into the world. Users will be able to interact with subreddit posts while remaining inside the ThreadSquare space — reading, voting, or commenting without leaving the environment. We’re also planning private rooms for smaller group discussions, moderator tools for managing community interactions, and event systems for live AMAs, polls, and meetups inside the space. ThreadSquare’s long-term vision is to make subreddit interaction immersive — not just about consuming content, but about living inside the community. <div