---
slug: "arcana-seed-lodge"
url: "https://devpost.com/software/arcana-seed-lodge"
title: "Arcana Seed Lodge"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 377
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "substrate/geospatial"
---

# Arcana Seed Lodge

> Brain wallet and optional signer using maps + masonic symbols

[Devpost](https://devpost.com/software/arcana-seed-lodge) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**substrate** [[geospatial]]

**stack** rust, tauri, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what's next for arcana seed lodge

## Body

Arcana Seed Lodge Intro Screen Arcana Wallet View Geohash Seed Encoding Interface Choosing Masonic Symbols for Passphrase Optional Story Part 1 Optional Story Part 2 Inspiration ❓ What Can Jesse James Teach Us About Bitcoin Self-Custody? Jesse James and the Knights of the Golden Circle buried billions in treasure across America using cryptic Freemason maps and esoteric symbols. Their methods weren’t just folklore—they were secure, location-based memory systems. What it does 🧭 Arcana Seed Lodge A location-based Bitcoin wallet generator inspired by memory palaces, outlaw treasure maps, and the human mind. All in a cross platform desktop experience. Arcana Seed Lodge applies that same logic to Bitcoin. We replace abstract wordlists with personal geography and story-driven rituals—because humans remember places better than random words. 🎯 Why It Matters BIP39 changed the game, but memorizing random words isn’t natural for most people. Bitcoin deserves better UX—one that aligns with human memory. Arcana turns your locations and your story into a deterministic Bitcoin seed that you can recover anywhere. No altcoins. No crypto. Just pure Bitcoin self-custody, inspired by outlaw wisdom. 🛠️ What It Does 🌍 Turns six meaningful locations into a BIP39-compatible Bitcoin seed 📜 Adds optional passphrase entropy using actual Freemason symbols 🧾 Supports PSBT signing workflows (e.g., Sparrow Wallet) 🎮 Includes a fun RPG-style narrative to guide new users through the ritual 💻 Tech Stack TypeScript + Vite for a fast, reactive frontend Tauri for secure offline desktop builds Pure client-side key generation (no server round-trips) Geohash-based entropy for deterministic, location-based seed derivation Challenges we ran into Creating a completely offline map server and search engine was a bit too much for the scope of this project..but.... we will be back :) Creating builds for all devices: lack of access to windows machine means it was the only platform we couldn't build for release 1. Once again we will be back :) Accomplishments that we're proud of Turned a map into an offline signer/wallet! What's next for Arcana Seed Lodge full security hardening offline maps suitable build with ease of use on offline raspberry pis and similar devices removing all online dependencies using offline LLMs to assist in memorization, quizzing and mnemonics the ability to use world landmarks as well as places of personal significance <div