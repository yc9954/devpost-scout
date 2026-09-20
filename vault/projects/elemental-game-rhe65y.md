---
slug: "elemental-game-rhe65y"
url: "https://devpost.com/software/elemental-game-rhe65y"
title: "Elem Game"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 623
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Elem Game

> Elem Game is a web3-based strategy game leveraging elemental battles and Mana management, with decentralized mechanics, it offers a trustless

[Devpost](https://devpost.com/software/elemental-game-rhe65y) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]]

**stack** kiro, pixi.js, react, solidity, symbiotic, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for elemental game

## Body

Inspiration The inspiration came from the idea of rethinking how an MMORPG could function within a decentralized architecture. We're exploring a way to build a game world without a central server, while also eliminating the need for players to manage wallets or understand the transaction mechanics typical of Web3 architectures that hinder user adoption. The goal is to create a true Web3 game , where: the rules are fixed and formalized, and changes occur through a predefined consensus; participation is permissionless but governed by established rules applied equally to all; security and resilience are a result of the architecture, not moderation; the player experience is smooth and familiar, like a traditional MMORPG, without compromising Web3 properties. Elem Game is a minimally implemented game mechanic created as a starting point for developing the project’s architectural solutions. It serves as a testbed for interaction principles, user experience, and technical integration with decentralized infrastructure. It is not a final game, but an interactive framework upon which a full MMORPG system will be layered. The second step is an infrastructure that enables gasless gameplay while preserving the properties of decentralized systems. What it does Elem Game is the client and foundational user interface for the future Web3 MMORPG. As part of the hackathon, we developed an interactive prototype that serves as: a tutorial for new players , explaining the rules, mechanics, and internal logic of the game through battle sessions; a UX foundation , intended for future integration with decentralized infrastructure. This is not just a demo — it’s the core interface for a new kind of MMORPG , where the blockchain is hidden under the hood and the surface presents a familiar, intuitive, and responsive game UX. How we built it Development was carried out entirely within the Kiro IDE , which served not just as an editor, but as a full-fledged development coordination platform — from concept to implementation. To achieve the current result, we used various Kiro modes: Vibe, Spec, Steering files, and ready-made MCP servers. This allowed us to avoid building a server from scratch and focus directly on logic, UX, and layer interaction. The technical implementation was based on the following stack: React + TypeScript — client architecture and business logic; PIXI.js — turn-based combat rendering with animations and effects; Solidity + Foundry — test contracts for mana, progress, and achievements. Challenges we ran into The biggest challenge wasn’t technical complexity, but a shift in mindset . We interacted with the code not just as a technical tool but as an extension of our ideas, thanks to the capabilities of Kiro. When tools allow you to turn ideas directly into results, knowing how the tech works becomes secondary — what matters most is a deep understanding of the domain, logical formalization, and clarity of thought. This requires a different discipline: only knowing what needs to be done matters — not how to do it. In this mode, traditional roles blur: the designer becomes an architect of interaction and user experience, while the engineer becomes an explorer who can work through multiple hypotheses simultaneously. This development approach isn’t just about working with technology — it’s adapting to an environment where the idea is the highest value . And that turned out to be the greatest challenge for our team. What's next for Elemental Game Short-term: PvP mechanics : real-time synchronous battles via WebSocket; Elemental fusion : creating new creatures from those already collected; Leaderboards and guilds : social layer with tournaments; Expanded achievements : new levels and time-limited quests. Long-term: Transition to an open MMORPG model : open persistent world; SDK for third-party games : expanding the architecture for other projects; Cross-chain progress sync : seamless transitions between networks without data loss. <div