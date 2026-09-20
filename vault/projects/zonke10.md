---
slug: "zonke10"
url: "https://devpost.com/software/zonke10"
title: "Zonke10"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 134
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Zonke10

> Build, reload, win: a fast 2-player line-battle inside Reddit.

[Devpost](https://devpost.com/software/zonke10) · hackathon [[Fun and Games with Devvit Web]]

## Facets


**stack** css-modules/tailwind, devvit-web-(interactive-posts), eslint, express-(template), html5-canvas-api, prettier, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration We wanted a snackable, Reddit-native 1v1 game that feels like a schoolyard pencil game: quick turns, easy to spectate, and fun to replay. Devvit Web + Interactive Posts was the perfect canvas—no installs, just open a post and play. What it does Zonke10 is a turn-based duel. Each turn you launch a ball; wherever it lands between grid lines progresses that line’s stick-soldier for the active player (Head → Body → L-Arm → R-Arm → L-Leg → R-Leg). Once a soldier is complete on a line, future landings on that same line add bullets . At 10 bullets the soldier shoots and wins that line . When all five lines are decided, the player with more lines wins. How we built it Devvit Web (Interactive Post) with React + TypeScript rendered into <div