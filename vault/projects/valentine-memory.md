---
slug: "valentine-memory"
url: "https://devpost.com/software/valentine-memory"
title: "Valentine Memory"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 461
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Valentine Memory

> A Valentine's Bitmoji memory game! Memorize the cards, match pairs as fast as you can, then challenge a friend. Best time wins, do you have the sharpest memory?

[Devpost](https://devpost.com/software/valentine-memory) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** bitmojistickers, javascript, lensstudio, turnbasedapi, turnbasedplayerinfo

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for memory match

## Body

Inspiration Memory Match was inspired by classic memory card games we all played as kids — but reimagined as a competitive, social experience for Snapchat. I wanted to combine the nostalgia of memory games with the turn-based challenge format , where two friends can compete head-to-head without needing to be online at the same time. The Valentine's theme felt perfect: hearts, love, and a playful rivalry between friends. What it does Memory Match is a turn-based memory game where two players compete to find all matching pairs in the shortest time. Here's how it works: The game shows 12 cards featuring the player's own Bitmoji in Valentine-themed poses Players have a few seconds to memorize the card positions Cards flip face-down, and the timer starts Players tap cards to reveal them and find matching pairs Once all 6 pairs are found, the timer stops The player sends a Snap to challenge a friend The friend plays the same game, and the best time wins At the end, Bitmoji animations celebrate the winner — or console the loser! How I built it Memory Match was built entirely in Lens Studio using JavaScript . Key features include: Bitmoji Sticker integration using TurnBasedPlayerInfo to display each player's personalized avatar Turn-based system to pass the game state between players via Snaps Memorization phase with animated "Memorize" text before gameplay starts Real-time timer tracking each player's performance Pair matching logic with animations: correct pairs scale up, incorrect pairs flip back Haptic feedback (TapticEngine) when a match is found Winner/loser screen comparing both players' times with animated Bitmoji results All game state (player times, winner) is saved and transferred using Snapchat's Turn Based API with persistent User and Global Variables. Challenges I ran into One major challenge was preventing race conditions when players tap cards too fast. Tapping three or more cards simultaneously caused animations to break and cards to lock up. Another challenge was dynamically switching Bitmoji between players. Accomplishments that I'm proud of Building a fully functional turn-based multiplayer game in Lens Studio Integrating personalized Bitmoji that adapt to each player automatically Creating smooth card flip, scale, and result animations Delivering a polished Valentine's theme with haptic feedback and animated UI What I learned Through Memory Match, I learned how to: Use TurnBasedPlayerInfo to dynamically load different users' Bitmoji at runtime Manage asynchronous game state between two players using Turn Based Variables This project strengthened my understanding of turn-based mechanics, Bitmoji integration, and state management in Lens Studio. What's next for Memory Match Future improvements could include: Different themes (Halloween, Birthday, Summer...) for seasonal events More card layouts (4x4, 5x4 grids) for harder difficulty Best-of-3 rounds for extended gameplay sessions Memory Match has the potential to become a social game friends can enjoy ! <div