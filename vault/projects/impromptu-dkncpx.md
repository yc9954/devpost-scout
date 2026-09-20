---
slug: "impromptu-dkncpx"
url: "https://devpost.com/software/impromptu-dkncpx"
title: "Impromptu"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 645
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "substrate/video_visual"
---

# Impromptu

> An AI prompt guesser game. Turn words into art, art into points!

[Devpost](https://devpost.com/software/impromptu-dkncpx) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
**substrate** [[video_visual]]

**stack** express.js, git, github, google-analytics, javascript, kiro, node.js, npm, openai, react, replicate, socket.io, together

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for impromptu

## Body

Let the games begin! Inspiration We've all played Pictionary , but what if the artist was an AI? That's the spark that led to Impromptu. I wanted to create a game that combines the social fun of guessing games with the unpredictability of AI-generated art. Sometimes AI creates exactly what you expect, sometimes it's hilariously wrong - and that's where the magic happens. What it does Impromptu is a multiplayer guessing game where players take turns creating text prompts, AI generates images from those prompts, and everyone else tries to guess the original words. It's like reverse Pictionary - instead of drawing what you're thinking, you're thinking about what the AI drew. Players join rooms, take turns being the prompt giver and earn points based on how well others can guess their prompts. Prompt givers get more points when their prompts are challenging but fair. How I built it I built Impromptu entirely with Kiro as my AI coding partner. Here's my tech stack: Frontend : React with Socket.io for real-time multiplayer Backend : Node.js with Express handling game logic AI Integration : Multiple providers (Together.ai, Fal.ai, Replicate) for cost-effective image generation Real-time : Socket.io managing rooms, turns, and synchronized game state Kiro helped me structure the entire project through steering files that guided everything from security practices to game balance. The most impressive part was how Kiro generated complex multiplayer logic and AI provider abstraction in single conversations! Challenges I ran into Cost Management : AI image generation can get expensive fast. I solved this by implementing multiple providers with automatic fallback - replacing DALL E in version 0 with Replicate AI models. Real-time Synchronization : Keeping game state consistent across multiple players was tricky. Socket.io helped, but I had to carefully handle asynchronous movements and edge cases. Scoring Fairness : How do you fairly score similarity between guesses and prompts? I combined string similarity algorithms with semantic analysis to reward both exact matches and creative interpretations. Accomplishments that I am proud of Built a complete multiplayer game from scratch in days, not weeks Implemented smart cost optimization saving ~80% on AI generation costs Created a game that's actually fun to play (2000+ users already!) Maintained clean, production-ready code throughout development What I learned AI-Assisted Development : Kiro's steering system is incredibly powerful. Having consistent guidance files meant every piece of generated code followed our established patterns and best practices. Multiplayer is Hard : Real-time games have so many edge cases. Players disconnect, networks lag, browsers crash - handling all these gracefully is an art form. State Management Complexity : Managing game state across multiple clients taught me about the intricacies of distributed systems. I learned to think in terms of eventual consistency, optimistic updates, and conflict resolution - concepts that apply far beyond gaming into any real-time collaborative application. AI Art is Unpredictable : Sometimes the AI creates exactly what you expect, sometimes a "red car" becomes a "crimson vehicle with wheels." That unpredictability is actually what makes the game fun. Technology Should Connect, Not Isolate : In our increasingly digital world, I realized how important it is to build tech that brings people together. Watching friends laugh at AI's interpretation of "flying pizza" reminded me that the best technology creates shared moments and genuine human connection, not endless scrolling alone. What's next for Impromptu Customisation : Let players choose categories like "animals," "food," or "sci-fi" and make their own avatars AI Variety : Experiment with different AI models for varied art styles, plus let players upload their own photos to create personalized artwork. Imagine prompts generating images in your friend group's style or featuring your actual faces - "Sarah riding a dragon" could literally show Sarah from your uploaded photos riding a dragon in the art style of your group's vacation pics. Mobile App : Native mobile experience for better accessibility <div