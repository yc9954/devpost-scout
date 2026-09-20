---
slug: "word-soro"
url: "https://devpost.com/software/word-soro"
title: "Word Soro"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 180
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
---

# Word Soro

> Drag 3+ letters to form words and try to clear the grid!

[Devpost](https://devpost.com/software/word-soro) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[deterministic_policy]]

**stack** devvit, gsap, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for word soro

## Body

Game Logo Inspiration Mashup between a classic Word Search and Same Game / Candy Crush mechanics What it does Word Soro is a timed 3-minute word puzzle where all players receive the same deterministic 6x6 grid of 36 letters. Words must be at least three letters long, formed from contiguous adjacent tiles without reusing the same tile. Valid words are confirmed against a server-side dictionary, and when words are cleared, letters above fall down due to gravity. The objective is to clear the entire grid before the timer expires, with scoring based on word length tiers and an additional bonus for a full clear. How we built it Devvit platform, Typescript, Vite, GSAP Challenges we ran into Still haven't figured out the cron job for scheduling daily puzzles.. but have a command to do it manually Accomplishments that we're proud of The gameplay and performance What we learned How to efficiently search a long dictionary What's next for Word Soro Getting the game approved by Reddit. Then having a cron for daily puzzles automatically posted as new reddit threads. <div