---
slug: "donutamagotchi"
url: "https://devpost.com/software/donutamagotchi"
title: "donutamagotchi"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 376
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# donutamagotchi

> Care for your pet by feeding it with ETH, earn $DONUT tokens!

[Devpost](https://devpost.com/software/donutamagotchi) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]]

**stack** farcaster, nextjs, react, tailwind, typescipt, viem, wagmi

## Body

Inspiration We wanted to reimagine the $DONUT mining protocol as something playable and delightful. The mechanics were already there—Dutch auction pricing, decay timers, ownership mechanics—but it felt abstract. We asked: "What if this was a tamagotchi?" A nostalgic virtual pet you actually care for, with real economic incentives. Turning boring protocol mechanics into a retro gaming experience felt perfectly aligned with Kiroween's spooky aesthetic. What It Does Donutamagotchi is a blockchain tamagotchi where you feed a virtual donut pet by purchasing ownership with ETH. Your pet's health, happiness, and energy reflect live protocol activity. The pet's mood changes dynamically—excited when you feed it, hungry during price decay, sleeping when no one owns it. While you're the caretaker, you earn $DONUT tokens. It's crypto meets nostalgia, profit meets gameplay. How We Built It Frontend: Next.js 16 + React 19 with TypeScript for type safety Styling: Tailwind CSS + canvas animations for retro pixel-art aesthetics Blockchain: Wagmi + Viem for Base network interactions, real-time contract data UX: Farcaster Miniapp SDK for seamless social integration The entire UI transformation was architected around making the complex protocol intuitive and fun. Challenges We Ran Into Type safety with Next.js routing: Strict route typing in Next.js 16 required careful type handling Real-time pet state: Synchronizing contract state, price decay timers, and visual animations Pixel art pixel-perfection: Achieving clean retro aesthetics while maintaining responsiveness across devices Economic clarity: Communicating yield rates, price mechanics, and profit potential simply Accomplishments We're Proud Of Complete thematic execution: Transformed an abstract DeFi protocol into an engaging, nostalgic game Responsive design: Pixel-perfect retro UI that works on mobile and desktop Real-time mechanics: Pet state changes reflect live blockchain data with smooth animations Accessible complexity: Made $DONUT mining economics fun without oversimplifying them What We Learned Game mechanics can make financial primitives irresistible Nostalgia (retro gaming) + novelty (crypto) = compelling user engagement Animation and visual feedback dramatically improve UX clarity TypeScript strictness catches real issues early—worth the friction What's Next for Donutamagotchi Multiplayer social features: Compete with friends' pets, trade caretaking shifts on Farcaster Pet customization: Cosmetics, skins, evolution states based on ownership streaks Governance: Let $DONUT holders vote on emission schedules and protocol changes Cross-chain expansion: Bring the game to other networks and reach more players <div