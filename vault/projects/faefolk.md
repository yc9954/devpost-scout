---
slug: "faefolk"
url: "https://devpost.com/software/faefolk"
title: "FaeFolk"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 719
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# FaeFolk

> FaeFolk is an NFT-based role-playing game where you use your NFTs to craft tools & equipment, train your skills and ultimately fight your way through dungeons and find treasure.

[Devpost](https://devpost.com/software/faefolk) · hackathon [[Supernova]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** gdscript, godot, ic, motoko, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for faefolk

## Body

GIF GIF GIF Inspiration Faefolk was inspired by Stardew Valley, a pixel-style, slice of life game that has been enjoyed by gamers for over 10 years. We wanted to bring this experience to the blockchain, and the Internet Computer was the most effective path to bring the vision to life. What it does In its current iteration, Faefolk allows users to farm, craft and build in a multiplayer, procedurally generated, persistent world. While much of what it will be is not yet built, the internet computer offers a unique opportunity to enhance game play loops by incorporating blockchain technology into the user experience. The current demo will demonstrate the minting of real NFTs by harvesting trees and stone, along with a procedurally generated world that users can play in with their friends. How we built it We built Faefolk using the Godot game engine, GDscript, Rust, and Motoko. We use web sockets and a centralized server for multiplayer communication, and NFTs are minted and persisted on the Motoko canisters. Godot is a particularly great match for the Internet Computer given its open source nature and its ability to use any programming language. Challenges we ran into To say that a month was not enough time to build this project is an understatement. Games take quite a while to actually bring to production. That being said, some of the challenges we faced were communication with the Internet Computer. Because we do not want our game to run exclusively on the web, we could not just build an HTML5 export, so we had to use Rust libraries to communicate with the Internet Computer. This is a problem because the Rust HD wallet library could not digest 12 word phrases from popular wallets like Plug, so user Principles could not be imported from web wallets like Plug. For the demo, we have hard coded principles, so we can demonstrate the minting of NFTs across the game and in our own NFT marketplace. Another challenge we faced was multiplayer. Outside of turn-based games, no blockchain is fast enough to handle real time multiplayer, so we had to settle for a Web2 solution to handle multiplayer communication. Godot has a fabulous, high-level multiplayer API that is not compatible with HTML5, so at a future point in development, we will have to build our own communication protocol so we can export an HTML5 version of the game that can be hosted on the IC. On the personnel front, our artist disappeared midway through, and the artist we hired to replace her lives in the Ukraine and has been unavailable for obvious reasons. Also, two developers of the four developer team have not been able to commit time to the project for personal reasons, so the remaining two were challenged with completing a project that was scoped for four developers. Accomplishments that we're proud of This is the first real gaming project the team has worked on. From what I have heard from other game developers, the fact that our game is enjoyable with this level of technological complexity is impressive. We are proud of our Rust implementation. While Godot allows you to use any language, it’s easier said than done. Rust allows us to bring the IC in all its utility to any platform that Godot can compile for. Yes, this means consoles, which may be a first for the blockchain. What we learned We learned what Rust could and could not do. We also learned the limitations of Godot, from its finicky tile mapping system to how picky its HTML5 export is and how it handles multiple threads and asynchronous communication. We also learned how great of an engine Godot is on top of all this. The node system makes things very modular and maintainable, and its community shares a lot of synergy with the IC community. What's next for FaeFolk Every great journey starts with the first step, and when it’s all said and done, Faefolk will not just be known as a great blockchain game but as a great game. We have already started conversations with experts in tokenomics and economies in RPG-based games, accelerator programs, and that crazy guy at the bar that told us about his artist friend who could be a useful replacement for those we left behind. <div