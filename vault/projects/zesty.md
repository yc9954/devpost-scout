---
slug: "zesty"
url: "https://devpost.com/software/zesty"
title: "Zesty"
hackathon: "Qloo LLM Hackathon"
organization: "Qloo"
winner: true
words: 508
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Zesty

> Zesty – The Unrecommendation Engine that flips your feed

[Devpost](https://devpost.com/software/zesty) · hackathon [[Qloo LLM Hackathon]]

## Facets

**substrate** [[structured_db]]

**stack** gemini, qloo, react, render, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zesty

## Body

Discover what you never knew you'd love Inspiration We live in a time where every app recommends the same kind of content. If you watch one romantic movie, your feed gets filled with more of the same. If you listen to mellow songs, you rarely see energetic music suggestions. This creates a bubble around our tastes. We started Zesty to break that bubble. We wanted to help people discover new things that are different from their usual likes. Not just more of the same, but something unexpected and exciting. That’s where the idea of the "Unrecommendation Engine" came from. What it does Zesty is a tool that helps people find content that is completely opposite to what they usually enjoy. Whether it’s music, movies, books, or food, Zesty uses cultural data and AI to show you something new and different. First, the user goes through a Taste Journey where they answer simple questions about what they like. Then, Zesty uses the Qloo API to fetch content that matches the farthest possible point from your current preferences. It doesn't stop there. Zesty also gives you daily reflection prompts, suggestions that push your comfort zone, and lets you track how your tastes evolve. You can even meet your "Taste Nemesis" - someone who loves what you hate - and share your journey with the community. How we built it We used React and Tailwind CSS to build the frontend and made it fast and simple with the Next.js App Router. For the backend, we chose Supabase for database, authentication, and edge functions. To generate prompts, reflections, and taste insights, we used the Gemini 1.5 Pro model. We connected it with the Qloo API, which gave us strong cultural data for recommendations. We made sure the app is light, fast, and easy to use - with a simple UI and meaningful suggestions. Challenges we ran into Finding the best way to define "opposite" tastes without making it feel random Making onboarding short but still effective in capturing taste preferences Balancing user comfort with new experiences Connecting Qloo and Gemini in a smooth way Keeping the design simple while offering deep features Accomplishments that we're proud of Creating the idea of an "Unrecommendation Engine" Connecting multiple tools like Qloo, Gemini, and Supabase into a working app Designing a smooth and playful user experience Encouraging people to try things outside their usual choices What we learned People are open to trying new things if it’s done the right way AI can be used not just to recommend more of the same, but to help users grow Cultural data adds strong value when combined with AI Exploration can be guided, not forced What's next for Zesty Build a mobile app for easier access and better user experience Add streaks and levels to keep users engaged in their discovery journey Partner with apps like Spotify, Goodreads, and Netflix for deeper integrations Launch a creator mode where users can make their own taste challenges Explore how Zesty can help in education, team-building, and diversity training <div