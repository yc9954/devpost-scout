---
slug: "block-tap"
url: "https://devpost.com/software/block-tap"
title: "Block Tap"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 438
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Block Tap

> Tap directional blocks to slide them off the board. 9 levels, 27 stars, progress saved. Think before you tap, wrong moves cost hearts!

[Devpost](https://devpost.com/software/block-tap) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets


**stack** hapticfeedbackapi, lensstudio, persistentstorageapi, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for block tap

## Body

Inspiration Block Tap was inspired by classic "slide-away" and logic puzzle games that look simple at first glance but require careful thinking and planning. I wanted to create a minimalist puzzle experience where each move matters, while also designing a game that encourages players to return over time through progression and replayability. The idea was to focus on direction, blocking, and timing , rather than speed or reflexes. What it does Block Tap is a level-based puzzle game where players must clear all blocks from the board. Each block contains an arrow indicating the direction it will move (up, right, down, or left). When a block is tapped, it slides in its direction — but only if nothing is blocking its path . To progress: Players must clear all blocks in a level Levels are unlocked sequentially Each level can earn up to 3 stars based on performance Players can replay levels to improve their star rating The game features 9 unique levels , each with a different puzzle layout and increasing difficulty. How I built it Block Tap was built entirely using Lens Studio with TypeScript . Key systems include: Directional movement logic with path detection Block interaction and collision handling Sequential level unlocking Star-based scoring system Persistent storage to save: the highest unlocked level star ratings per level total stars collected All progression is saved, allowing players to leave and return without losing their progress. Challenges I ran into One of the main challenges was designing puzzles that feel fair but challenging , especially on a mobile screen. Another challenge was managing game state correctly: ensuring blocks only move when their path is clear handling edge cases where a wrong move could block progress maintaining consistent progression data using persistent storage Balancing difficulty while keeping the experience enjoyable on a vertical interface required several iterations. Accomplishments that I'm proud of Building a complete long-form puzzle game in Lens Studio Implementing persistent progression across sessions Designing 9 handcrafted puzzle levels Creating a replay system that encourages optimization and mastery Delivering a clean and focused UX suitable for mobile play What I learned Through Block Tap, I learned how to: Design long-term gameplay loops on Snapchat Manage persistent data safely and effectively Create logical puzzles with increasing difficulty Balance simplicity, challenge, and replayability This project deepened my understanding of game design and state management in Lens Studio. What's next for Block Tap Future improvements could include: Additional puzzle levels New block mechanics (rotating blocks, teleporters...) Daily or timed challenges Visual themes and cosmetic variations Block Tap has strong potential to grow into a larger long-form puzzle experience. <div