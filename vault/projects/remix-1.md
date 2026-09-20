---
slug: "remix-1"
url: "https://devpost.com/software/remix-1"
title: "Escape Room Remix"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 819
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Escape Room Remix

> Escape Room Remix: Open-source escape game for creators-any skill level! Remix puzzles, no scripting needed! Add style, collaborate & innovate. Mobile/VR optimized, reusable for endless adventures.

[Devpost](https://devpost.com/software/remix-1) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**substrate** [[geospatial]]

**stack** blender, grok, metaaudioaigen, metagenaii, typescript

## How they structured the write-up

- about the project
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i’m proud of
- what i learned
- what is next for escape room remix

## Body

Main Thumbnail 1 Item Building that can be easily removed for remixing Video Linked in Submission Riddle Panel Asset No Scripting required Color Sequence Panel Asset Spot the Difference Asset for all devices Lever Puzzle asset Key Pad Asset Collect Items and Place Asset Game Master Huds Asset within the world Asset within the world Asset within the world Escape Room Remix: Project Story About the project Escape Room Remix is a plug and play template for Meta Horizon Worlds that lets anyone (from day one creators to advanced builders) publish a custom escape room with no scripting required . Every puzzle, UI, sound, and effect is configurable in the Properties panel. The world includes step by step instructions, a written guide, and a video walkthrough. The entire shell (walls, floor, decor) is grouped for one click removal , so creators can drop in a theme and go live. Inspiration I’ve helped many Horizon creators with PVP games and escape rooms. The biggest blocker is usually scripting . I never charge for help; at most I ask for a small logo in the lobby. I wanted a template that removes that blocker: create, re theme, and publish without opening a script . This platform changed my life. It gave me purpose, brought my kids and me closer, and even led me to my girlfriend. None of them write code, but they all have strong ideas. I built this with them in mind: could they remix it with zero help from me? That became the bar. What it does No scripting puzzle system: a Riddle Panel with up to four riddles (optional randomization per instance). Hint flows: buy a hint with IWP or spend in game tokens. Drop in theming: swap the entire environment while puzzle prefabs stay intact. Guided setup: in world labels, scrollable UI panels, links to docs, and a full A to Z video. Accessible UX: large, readable spatial UI that works on mobile and VR. Remix ready: clear naming, grouped assets, linked scripts you never need to edit. Nearly everything is exposed as props. In short: plug, theme, publish and still ship something unique. How I built it Tech stack: TypeScript with Horizon APIs (UI, triggers, audio, particles, variables, network and local events). I used Meta Gen AI tools and other assistants to speed up tricky TypeScript. Simple Architecture: each challenge or element is self-contained with labeled props and linked docs for deeper customization. The entire map is one unit so can be easily removed, only leaving the riddle/ escape room elements. Property panel driven: riddles, sounds, effects, costs, and colors all live in the Properties panel. Guides everywhere: tooltips, on asset notes, signage, plus a companion doc and video. Performance and UX: sensible defaults, minimal draw calls where possible, and clear feedback (SFX, VFX, toasts). Optional monetization: IWP hint panel or a in world token system. A tiny design equation guided me: [ \text{Friction} \approx \frac{\text{Steps to Publish}}{\text{Clarity of Guidance}} ] I reduced steps and increased clarity until friction felt close to zero. Challenges I ran into Making assets creator friendly meant fighting my own habits. My idea of “easy” had drifted from what new creators feel. I pictured my kids and my girlfriend building a world on their own. Even moving an item or wiring a sound can feel overwhelming at first. That lens reshaped the UX: clearer names, zero code, better defaults, and property only workflows. This is the first time I built with creators as the primary audience. The world exists to be remixed and remastered by anyone who wants to publish a puzzle or escape experience. Accomplishments I’m proud of The ease and remix-ability . Scripts are pre-linked and never need to be opened . You can customize, re theme, and publish by editing only the Properties panel. It feels plug and go, yet the end result is still yours. Delivering power without complexity is the win. I’m proud to help creators create and publish their vision without writing a single line of code. What I learned I leveled up TypeScript patterns and leaned on Meta Gen AI for code and audio. More importantly, I learned to design for: Creators (clear docs, zero scripting setup, embedded video links) Players (fun, readable, responsive) Past me (the version that would have shipped many more rooms if a remixable template existed) Not everyone learns at the same pace. Designing for accessibility means spotting confusion early and removing it. What is next for Escape Room Remix More remixing. I want community requests for new puzzle styles and riddles, tie ins with parkour, and expansions into maze and adventure style layouts. The goal is to unlock creativity by removing the fear of scripting. Under the hood it is advanced TypeScript; on the surface it is welcoming, customizable, and fast. If this helps even one new creator press Publish with confidence, it is doing its job. <div