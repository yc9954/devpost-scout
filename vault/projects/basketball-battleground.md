---
slug: "basketball-battleground"
url: "https://devpost.com/software/basketball-battleground"
title: "Basketball Battleground"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 347
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Basketball Battleground

> Climb the ranks, earn XP, unlock exclusive balls and goals! Play longer for bonus XP and complete side missions to level up faster. Show off your grind in style.

[Devpost](https://devpost.com/software/basketball-battleground) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[realtime_stream]]

**stack** meta, typescript

## How they structured the write-up

- 🚀 about the project
- 🎯 what inspired me
- 🛠️ how i built it
- 📚 what i learned
- 🔥 challenges i faced
- 🧠 side features
- 🏁 the formula behind progression

## Body

🏀 Basketball Battleground – Swipe N’ Score 🚀 About the Project Basketball Battleground started as a simple swipe-to-shoot mobile concept. I wanted to blend arcade-style gameplay with a progression system that rewards skill and time investment — a mix of NBA Jam energy and Call of Duty-style ranks . The goal was to make a casual basketball game feel competitive, rewarding, and alive. 🎯 What Inspired Me The inspiration came from: Classic arcade basketball games Mobile games that balance grind and cosmetic rewards My love for progression systems where each level unlocks something meaningful I wanted players to feel like their time and skill mattered , and that every shot brought them closer to glory — both visually and numerically. 🛠️ How I Built It Game Engine : Meta Horizon Worlds Programming : TypeScript + Horizon APIs Rank System : I created a scalable XP-based rank class with 50+ titles, each with required XP, color data, and unlocks. Unlockables : I connected ball and goal textures to XP rank events with networked texture triggers. UI : Designed responsive HUDs to reflect progress, power-ups, and unlocks dynamically. 📚 What I Learned How to structure progression logic cleanly in TypeScript Binding and rendering dynamic UI components efficiently in Horizon Worlds Creating scalable unlock systems that work across multiplayer environments Handling cross-device UI scaling for mobile and VR users 🔥 Challenges I Faced Designing a progression curve that feels rewarding but not grindy Balancing visual clarity in a HUD that shows score, XP, power-ups, and streaks Handling real-time texture changes without frame drops or sync issues Keeping the XP logic modular and extensible as I added side missions and bonuses 🧠 Side Features Play Time Bonus : Players earn bonus XP the longer they play Side Missions : Optional tasks that grant XP boosts and speed up rank progression Mobile Optimization : UI scales to mobile screen-safe areas automatically 🏁 The Formula Behind Progression Using XP interpolation logic to calculate how close a player is to their next rank: const percentage = (currentXP - currentRank.xpRequired) / (nextRank.xpRequired - currentRank.xpRequired) <div