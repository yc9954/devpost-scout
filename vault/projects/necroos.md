---
slug: "necroos"
url: "https://devpost.com/software/necroos"
title: "Necroos"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 300
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# Necroos

> Windows 95 from beyond the grave

[Devpost](https://devpost.com/software/necroos) · hackathon [[Kiroween]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** awsamplify, kiro, react, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for necroos

## Body

Inspiration Nostalgia for Windows 95 mixed with a love for horror games. I wanted to create something that starts familiar and comforting, then slowly becomes unsettling—like your childhood computer got possessed. What it does NecroOS is a browser-based Windows 95 simulator that progressively haunts itself. Boot up, log in, and interact with familiar apps like Notepad and Minesweeper—but with a dark twist. The more you use it, the more corrupted it becomes through a "haunt level" system that triggers glitches, jump scares, and a very disturbed Clippy assistant. How we built it React 19 + TypeScript with Zustand for state management. Used Kiro's spec system to plan everything upfront, then leveraged steering docs to teach Kiro my patterns once. Kiro generated components with comprehensive property-based tests using fast-check. Built 15+ fully-tested components in 2 weeks with 95%+ coverage. Challenges we ran into Coordinating visual glitches across multiple windows without killing performance. Browser autoplay policies blocking audio. Making jump scares effective but not annoying. Property-based testing helped catch edge cases in the haunt level system that would've been bugs otherwise. Accomplishments that we're proud of Production-quality code with strict TypeScript and comprehensive testing Smooth 60fps animations even with multiple glitching windows The HauntingOrchestrator service that coordinates all horror effects Property-based tests that actually caught real bugs Building a complex system in 2 weeks that would've taken months solo What we learned Spec-driven development with AI is powerful—defining correctness properties upfront made testing almost automatic. Steering docs eliminate repetition. Property-based testing catches edge cases traditional tests miss. Kiro isn't just autocomplete—it understands architecture when given proper context. What's next for NecroOS Real audio files (currently placeholders) More applications (Paint, File Explorer) Multiplayer haunting (share your cursed desktop) Mobile support with touch-based jump scare triggers AI-generated Clippy responses for dynamic horror dialogue <div