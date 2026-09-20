---
slug: "starkcity"
url: "https://devpost.com/software/starkcity"
title: "Starkcity"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 288
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/housing_homeless"
  - "substrate/geospatial"
---

# Starkcity

> StarkCity — own the blockchain streets, one block at a time

[Devpost](https://devpost.com/software/starkcity) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[housing_homeless]]
**substrate** [[geospatial]]

**stack** cairo, dojo, node.js, react, socket.io, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for starkcity

## Body

Splash Main menu Online Game Online Game with peers Game Properties Inspiration We wanted to merge the thrill of Monopoly with the transparency of blockchain. The idea of a city where every deal, rent, and property is verifiably onchain inspired StarkCity — a decentralized twist on a classic. What it does StarkCity lets players roll dice, buy properties, build houses, and collect rent — all powered by Starknet and Dojo . It supports online multiplayer (via sockets) and AI mode where you can play against a computer opponent. Every property, house, and hotel is represented as an ERC-1155 token , ensuring verifiable ownership. How we built it We built the core game logic using Dojo’s ECS framework , with: ERC-1155 tokens: Properties 1–40 , Houses 1001–1040 , Hotels 2001–2040 . Socket.IO server: For real-time multiplayer. React frontend: For smooth UI and game updates. AI heuristics: For single-player mode decisions. Dice rolls follow a fair random distribution: [ P(x) = \frac{1}{36}, \quad x \in [2, 12] ] Challenges we ran into Syncing onchain and offchain states in real-time. Balancing speed and decentralization. Designing the ERC-1155 ID system to map properties, houses, and hotels efficiently. Making the AI play competitively but predictably. Accomplishments that we’re proud of Built a fully onchain Monopoly experience using Dojo. Designed a clean, expandable ERC-1155 asset hierarchy. Implemented both multiplayer and AI modes in one unified system. What we learned How to model complex game systems in Dojo ECS . How to bridge offchain gameplay with onchain verification . The importance of UX design when mixing real-time actions with blockchain logic. What’s next for StarkCity We’re expanding StarkCity with: Starknet leaderboard integration Tokenized rewards and staking Community tournaments And a fully decentralized city economy <div