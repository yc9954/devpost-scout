---
slug: "tactical-toe"
url: "https://devpost.com/software/tactical-toe"
title: "Tactical Toe"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 440
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Tactical Toe

> What if Tic Tac Toe had Hearthstone spells? Meet Tactical Toe: Use Morph to steal, Poison to burn, and Ward to protect. Stop playing for draws—start playing for blood. Snap a duel now!

[Devpost](https://devpost.com/software/tactical-toe) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** javascript, lensstudio, snapchat, turnbasedcomponent

## How they structured the write-up

- inspiration
- what tactical toe does
- what we learned
- what's next for tactical toe

## Body

GIF Tactical Toe: Tic Tac Toe Reinvented with Hearthstone Spells! Inspiration As a huge fan of Hearthstone, I’ve always loved the depth of card games, but I wanted to make that experience easy to play for everyone, even those without much gaming experience. Traditional Tic Tac Toe often feels repetitive because it ends in so many draws. My goal was to fix that by adding a "Hearthstone touch"—introducing simple spells that turn a basic grid into a strategic duel that anyone can pick up in seconds. What Tactical Toe Does Tactical Toe transforms classic Tic Tac Toe into a fast, mind-game duel played via Snapchat Snaps. Players take turns to either place their piece on an empty cell OR cast one spell from their hand. Spells have delayed effects that only resolve at the start of your next turn, giving the opponent a full turn to react. The 4 Spells (2 use each per player): Morph — Steal an enemy piece on your next turn (converts to your symbol and counts for your lines). Poison Blade — Destroy an enemy piece at the start of your next turn. Arcane Ward — Protect your piece from Morph, Poison & destroys during the opponent’s next full turn. Purify — Instantly remove ALL spells/effects from one of your pieces. How to Win Get 3 of your pieces in a row (horizontal, vertical, diagonal). No more forced draws — strategy, bluffs and clever counters decide the game. Gameplay Flow You receive a Snap with the current board. Place a piece OR cast a spell → end turn → send Snap back. Opponent responds → spells tick → new threats appear. Quick 4–8 turn duels (~2–5 minutes). Perfect for Snapchat: async, social, and replayable with friends. No servers, no waiting — just pure tactical fun. What we learned Rapidly mastered Lens Studio JS scripting and async Turn-Based logic in weeks, creating lean state management for seamless Snap duels. Solved performance creatively: used video animations for spells instead of heavy VFX to deliver premium TCG feel while staying lightweight on mobile. Game design breakthrough: one-turn spell delays eliminated Tic Tac Toe’s predictable draws, turning the grid into a tense bluffing and strategic duel. What's next for Tactical Toe Turn-Based Replay Top priority: turn-based replay system so players can watch spell casts in real-time when opening the Snap — full back-and-forth mind games. Game Balancing & Meta Monitor playtests to fine-tune spell availability / “mana” feel. Keep it beginner-friendly while rewarding deep mastery and outsmarting friends. Visual & Polish Upgrades More game juice, visuals and haptic feedback, and expand the card library with new tactical options. <div