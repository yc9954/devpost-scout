---
slug: "project-citadel"
url: "https://devpost.com/software/project-citadel"
title: "Project Citadel"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 520
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Project Citadel

> Project Citadel fixes the weakest links in the Solana DeFi ecosystem by bringing the hottest projects straight to your desktop without browsers or web-hosts in between.

[Devpost](https://devpost.com/software/project-citadel) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[code_repository]] [[structured_db]]

**stack** dotnet, linux, macos, solnet, solnet.mango, solnet.pyth, solnet.serum, windows

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for project citadel
- get in touch

## Body

Inspiration The base inspiration for Project Citadel boils down to the slight annoyance that is the current DeFi ecosystem. Not only do you need to have several bookmarks to visit all your favorite project apps but you still end up relying on the good old spreadsheet to sum it all up. To add to this, we realized that the entire DeFi ecosystem is also relying on the current Web2 not having any downtime nor being censored by central powers. What it does At its heart, Project Citadel aggregates several products into one single app: Wallet Swaps (Serum OBs and Raydium) - planned DEXs (Currently Serum fully working, Mango close to being production ready) Portefolio Management (Aggregate positions, open orders, etc) Farming/Staking - planned Beyond functionality wise, Citadel is your best hedge against censorship. Its a full fledged cross platform Desktop Client. How we built it The story of Project Citadel starts in the last hackathon. We planned on building it back then, but realized there were big holes in tooling. Back then Solana SDKs were lacking, so we started by building Solnet as our submission. Over the past two months we quit our jobs and kept building supporting tooling for the ecosystem - Solnet.Serum , Solnet.Pyth , Solnet.Mango . This hackathon, we were finally equipped to start Citadel. A desktop application built using dotnet , Avalonia , our several Solnet.* libraries, and aggregated data from on-chain sources - Mango, Serum and Pyth - and a couple of 3rd party providers - CoinGecko and Bonfida. The current state of the app took approximately 6 cumulative man-weeks, as the remainder of the time was spent in other projects or base integration libraries. Challenges we ran into The timing of the hackathon was one of the biggest challenges. We had several ongoing commitments that we couldn't drop when it was announced, the Mango library development had just started and we found out at the last minute that we needed to integrate with Pyth as well. Beyond timing, the most pressing issues were avoiding RPC shanenigans and access to historical OHLCV data. What we learned Our learning experiences were mostly technical - on the Solana ecosystem they were mostly related to the Mango inner workings, as the Solnet libraries left us with some previous precious knowledge, and a deeper knowledge of the Avalonia framework. Beyond technical aspects, we have to admit that we learned a bit too late how to tackle scope creep. What's next for Project Citadel This is nothing but the start for Citadel. In short, our future roadmap looks like: Improving the base libraries (mainly Solnet.Mango and Solnet.Serum) with the experience gained from the hackathon. Cleanup the Mango experience Add support to Swap UI/UX improvements - hopefully a full featured branding Launch a DAO to dictate project future - which protocols to integrate, design changes, etc Sometime after/during the swap integration, we want to have our first close beta and after the UX/UI improvments the first open beta. Beyond the roadmap, we have some big challenges ahead, namely licensing and open sourcing. Get in touch Twitters: @project_citadel @hoaktrades @qtmoses Discord <div