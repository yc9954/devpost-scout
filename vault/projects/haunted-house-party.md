---
slug: "haunted-house-party"
url: "https://devpost.com/software/haunted-house-party"
title: "Haunted House Party"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 557
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Haunted House Party

> Knock thrice if you dare. Each door reveals a random 3D challenge—slice pumpkins or sprint through endless tombs. Fail, and you’re cast into the foggy graveyard. A Kiro + Three.js Halloween thrill.

[Devpost](https://devpost.com/software/haunted-house-party) · hackathon [[Kiroween]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** kiro, react-three, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for haunted house party

## Body

Game banner Tomb Runner game Haunted House Hero Pumpkin slicer game Inspiration I’m a web developer, fascinated by web animations, and earlier this year I took a Three.js course that introduced me to building a haunted house scene with graves. That small class project stuck with me. I kept thinking: What if the house wasn’t just scenery? What if every door hid a mystery? That spark led to Haunted House Party, a Halloween mini-game world where you knock, enter, and never know what happens next. I elevated the original idea by making the door fully openable and turning the scene into a playable experience. And because I wanted a modern web workflow, I rebuilt it in React Three Fiber. What it does Players knock three times on a door, triggering a random 3D mini-game inside a dark room — from slicing flying pumpkins to running through endless tomb tunnels. If they fail, they can retry or get kicked back into the foggy graveyard hub to start again. Every door becomes a new dare. How we built it Using Kiro, the hackathon sponsor’s AI development tool, I transformed my original Three.js haunted house code into React Three Fiber. I created early steering documents to set the tone, mechanics, and atmosphere for all future rooms. I vibe-coded most of the experience and sourced lightweight free 3D models. Because React Three Fiber doesn’t have Three.js’s built-in GUI, I frequently used Kiro’s vibe chat to test assets, preview animations, and troubleshoot issues. I also wrote detailed specs for each mini-game so the AI could make accurate suggestions. To keep the codebase clean, I built Kiro agent hooks that automatically delete tests and files tied to removed assets. Throughout the build, I constantly instructed the AI to optimize code and scene setup. Challenges we ran into Heavy optimization work: 3D assets quickly affect device performance. I had to delete many original models and replace them with extremely lightweight ones, max 8MB. My laptop froze and shut down multiple times before I realized it was time to optimize. Animation troubleshooting: Some animation bugs required digging directly into model files because AI couldn’t always detect the exact issue. Long specs → long waits: Writing specs first meant waiting through up to 17 AI tasks before I could test changes. Finding the right assets: High-quality, lightweight, Halloween-themed 3D assets are surprisingly hard to source. Accomplishments that we're proud of The initial loading animation — AI nailed exactly the eerie vibe I wanted. Getting all the mini-games functional and fun. Designing each game’s unique look and feel. Successfully optimizing the scenes enough for smooth gameplay. The zoom-into-the-door animation, which took a lot of iteration. (I originally wanted a skeleton hand dragging players in, but I couldn’t find a good asset.) What we learned I learned to think and build fast — if one approach fails, pivot immediately. I got significantly better at React Three Fiber and scene management. I learned how powerful Kiro is for fast iteration: whenever I couldn’t find a piece of code or understand a behavior, I asked Kiro. Most importantly, I learned how to create a complete game experience from start to finish. What's next for Haunted House Party More games. More levels. Increasing difficulty. More interactivity. And eventually — multiplayer. The haunted house still has many doors left to open. <div