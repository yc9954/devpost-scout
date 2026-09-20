---
slug: "fomo-91dnsu"
url: "https://devpost.com/software/fomo-91dnsu"
title: "FOMO"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 476
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# FOMO

> FOMO reveals where people are gathering and what’s buzzing there: turning curiosity into the urge to show up and connect.

[Devpost](https://devpost.com/software/fomo-91dnsu) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** chatgpt, firebase, firestore, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fomo

## Body

Inspiration We’re more separated than ever. We stick to the same small circles: or worse, lock ourselves in our rooms and watch life happen from a screen. We know things are happening out there, but we rarely know where, or how to step in. Our app changes that. When you open it, you see high-energy areas on a map, places where people are actually gathering. From there, you can see what people there are talking about, what’s buzzing, what you’re missing out on. You don’t jump in right away. You can watch. Listen. Get the vibe. And if something catches your attention, you can ask a question tied to that location: a way to reach out without forcing yourself into the room. It’s about lowering the barrier between isolation and participation, helping people feel connected to what’s happening around them, before they decide to step in. What it does You open the app and immediately see where it’s busy. Tap a hotspot to see what people there are discussing, and if something catches your interest, you can ask the crowd a question tied to that location. How we built it We split the app by features, each person owning a core function, then agreed on how everything would connect before stitching it together and testing first independently and then the full flow in Xcode Simulator. Challenges we ran into Getting started was harder than expected. We had settled on an iOS app, but not everyone had a Mac, which limited tooling and slowed early progress. We also had to work within uneven iOS experience across the team, figure out a realistic tech stack we could actually ship with and untangle several Git messes. Accomplishments that we're proud of Since we weren’t fully familiar with the language, parts of the original architecture turned out to be hard to achieve with our stack, which created an early roadblock that we had to untangle. Even with last-minute changes and fine-tuning, we still managed to bring everything together and finish the project: including implementing user tracking so we could actually follow real user flows. What we learned We learned a lot from working with a map API and live location data, especially around handling permissions, real-time updates, and keeping the UI responsive as data changes. We also gained hands-on experience with asynchronous programming using async/await, learning how to manage timing issues and ensure data loads smoothly without blocking the app or breaking user flows. What's next for FOMO Next, we want to expand FOMO by adding user profiles that people can build up over time, along with the ability to follow friends and see their activity. We also plan to improve chat monitoring by introducing roles like admins or moderators, and allow businesses to create their own locations in the app, host events, and share updates directly with users. <div