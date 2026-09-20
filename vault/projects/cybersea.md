---
slug: "cybersea"
url: "https://devpost.com/software/cybersea"
title: "CyberSea"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 369
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/transportation"
  - "substrate/geospatial"
---

# CyberSea

> Battleship on the blockchain, powered by ZK and AI. Your moves and ships are kept private thanks to ZK, so no more guessing if your opponent is peeking! And with AI, the game gets even more thrilling.

[Devpost](https://devpost.com/software/cybersea) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** ai, full-on-chain-game, mud, openai, zk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cybersea

## Body

game Inspiration Imagine playing a game of Battleship, but with a unique twist - it's blockchain-powered, driven by Zero-Knowledge Proof (ZK), and enhanced by Artificial Intelligence (AI). It's like the classic game, but with a cooler and smarter edge. Thanks to ZK technology, your moves and fleet information remain private, eliminating the guesswork of whether your opponent is peeking! What's more, with AI, the game becomes even more thrilling. It learns your strategies and challenges you in novel ways every time. Additionally, you have ownership of your fleet and can trade ships with other players. It's Battleship with a tech-savvy, modern spin that turns every match into a brand new adventure. What it does CyberSea is a full-chain naval warfare game where players can engage in battles at sea against AI or other players. How we built it We adopt MUD as the core architecture and divide it into PVE and PVP modes. In PVE mode, players will play against OpenAI bots by invoking OpenAI through Chainlink Functions . Players' ship coordinates are kept confidential via zero-knowledge proof , so that the AI cannot cheat even off-chain. Challenges we ran into The PVP mode has not been fully developed yet. Accomplishments that we're proud of We have integrated various cutting-edge technologies together in a very short period of time, including zero-knowledge proof , on-chain game engine MUD ， Functions , and AI . This appears to be an extremely innovative product. What we learned We now have a deeper understanding of the power of Chainlink Functions. It allows AI not only to play games on-chain, but also to study opponents on-chain and defeat Player 2 with the thinking of Player 1. Everything is done on-chain. More importantly, we incorporated zero-knowledge proof to make the game fairer without worrying about cheating due to the transparency of blockchains. What's next for CyberSea As a product combining zero-knowledge proof, AI, blockchain and gaming, we will continue building and developing CyberSea to attract more users on Layer 2, allowing more people to experience the integration of AI and blockchain games, while seamlessly getting in touch with zero-knowledge proof. We will lower the threshold for the game and conduct more and better work. <div