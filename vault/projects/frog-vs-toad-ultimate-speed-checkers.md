---
slug: "frog-vs-toad-ultimate-speed-checkers"
url: "https://devpost.com/software/frog-vs-toad-ultimate-speed-checkers"
title: "Frog vs Toad: Ultimate Speed Checkers - A Leap Forward"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 661
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Frog vs Toad: Ultimate Speed Checkers - A Leap Forward

> New updates for a Player level system, interactive Onboarding, as well as dynamic World progression.

[Devpost](https://devpost.com/software/frog-vs-toad-ultimate-speed-checkers) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**substrate** [[code_repository]] [[video_visual]]

**stack** blender, horizon, typescript

## How they structured the write-up

- 🐸 frog vs toad: ultimate speed checkers -- a leap forward
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for frog vs toad: ultimate speed checkers

## Body

🐸 Frog vs Toad: Ultimate Speed Checkers -- A Leap Forward A new update brings progression for Players, Teams, and even the World. Inspiration We built the original Frog vs Toad to reimagine Checkers as a fast, fun, social party game—something tactile, chaotic, and instantly understandable. Players could walk up, tap a piece, and play with no turns and no waiting. But we kept asking ourselves... What if the world changed when your team won? What if every match made the park look different? What if you could race up a leaderboard with your fellow frogs and toads—and hear a victory song when you hit the top? This update is our answer to all of that. What it does At first glance, it’s still the same game: Find a board. Choose Frog or Toad side. Capture all your opponent’s pieces. Easy, right? But now… 🧠 You earn XP every time you capture or win. 📈 You level up, unlocking funny new rank titles and privileges as you go. 🟢 You can switch teams anytime—your active team is the one with more XP. 🌍 Your wins change the world for everyone. Trees, banners, and details all shift based on which side is currently winning. 🎉 If your team wins 12 matches first, the Leap Ladder resets, and your whole team gets bonus XP, a laser light show, and an absurdly catchy rap anthem. Yup. You heard me. 🔐 Higher-level players unlock VIP access to Club Croaklord. 🧭 New players get a flyover onboarding tour, complete with camera sweeps and button guides. It’s like a theme park intro for speed checkers. In short: the name Frog vs Toad now actually means something. The battle is real. The race is on. How we built it This update stretched our systems design quite a bit. Here’s what went into it: A custom XP and level progression system tied to player actions Dual-team logic that tracks XP for frogs and toads separately Dynamic team alignment based on your personal progress World Persistent Variables to change the environment across all instances A reworked onboarding system using fixed-position cameras Bonus XP + race logic with live Leap Ladder tracking and faction-wide effects Laser VFX and audio syncing for our team victory moments A dynamic UI system with persistent Bindings, faction icons, XP bars, and tooltips And yes… there's a rap anthem for each team. Challenges we ran into Making XP feel fun but not punishing We didn’t want players to feel locked into a team or discouraged after a loss. That led to our flexible “whichever side you’re winning with is your team” system. Teaching players what’s new without boring them That’s where the onboarding flyover came in—a mix of UI and 3D visuals to keep things immersive but clear. Making the environment evolve in a way that’s noticeable but not overwhelming Persistent state systems are powerful, but if no one notices the changes, what’s the point? Syncing rewards across everyone When the Leap Ladder gets won, we wanted everyone on that team to feel it—through light, sound, and XP. Accomplishments that we're proud of *Turning our silly checkers game into a world with actual, ongoing conflict *Creating a team-based system that doesn’t force commitment, but still feels meaningful *Designing a mobile UI that feels alive and responsive—even with a small screen *Hearing testers shout, “Wait—did the trees just change?!” after a team win What we learned *Persistent systems = big impact (even for small details) *Players love XP when it’s fast, fair, and visual *People will switch teams mid-rank What's next for Frog vs Toad: Ultimate Speed Checkers We’ve got a lot planned. 🧓 A Coach NPC who hangs out in the park and teaches players how to play (he’s seen some things) 🎩 Hats, badges, and other Frog/Toad flair at the corner vendor 🕹️ New powerups and hazard tiles 🌎 Event-based world states (seasonal vibes? Tournament arcs?) 🐸 VR support—coming soon, with cross-play in mind <div