---
slug: "gamemaster-vk6oju"
url: "https://devpost.com/software/gamemaster-vk6oju"
title: "Gamemaster"
hackathon: "Building Privacy in Web3 - Powered by Partisia's MPC"
organization: "Partisia Blockchain Foundation"
winner: true
words: 476
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/financial_record"
---

# Gamemaster

> Gamemasters create "Arcades", consisting of one or more games. Users can sign up to play the Arcades. The Gamemaster will control the progress of the games. Each games give or take points.

[Devpost](https://devpost.com/software/gamemaster-vk6oju) · hackathon [[Building Privacy in Web3 - Powered by Partisia-s MPC]]

## Facets

**substrate** [[financial_record]]

**stack** netlify, partisia, rust, tailwind, typescript

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- what we learned
- what's next for gamemaster

## Body

Inspiration The idea is to showcase the capabilities of Partisia Blockchain in a way that is practical. Some of the games implemented can also be done on a regular Blockchain, but some aspects are nicer to work with based on private data. How we built it Backend: All states are stored on the Blockchain. The idea was to build games that showcase various unique capabilities of Partisia Blockchain - even if it is infeasible in this setting. Frontend: Nextjs + RSC + Tailwind. Currently only works with the Partisia Blockchain Wallet and only on testnet. The user can customize their Arcades, and deploy it to the chain with a single click. After deployment, users with a link can access the game and sign up. The Gamemaster is responsible of ending and starting the next games. Challenges we ran into Contract issues It was a bit difficult to understand the flow of the rust macros. Maybe a sequence diagram chart could help visualising the different events. Sometimes the Rust compiler infers the type of numbers, but the ZK compiler doesn't in the same way ( let i: u32 =0; let b = i * 2 fails using ZK compiler) Tried to modularize the game logic, but couldn't immediately get it to work - examples of more complex projects would be nice. UI The PBC wallet doesn't return tx hash, etc, until after the user clicks "return", which makes the user experience quite bad. Could poll for new transactions for the user account, but would be better to return the tx hash right away so the UI can update accordingly Gas Issues Some of the showcased concepts doesn't work well in practice, because the gas fees would be too high. The game design will need small adjustments to be feasible on mainnet. It is hard to know the gas cost - would be neat if there is a better way to estimate it, or a way to assert the gas costs in Java tests. What we learned The Java contract tests are extremely useful to minimize the feedback loop. It would be nice if we had a way to spin up a "real" local (temporary) blockchain - would make the UI easier to test and develop. What's next for Gamemaster There are many ways to continue the project: Limit player signup to a whitelist or based on NFTs Add prize pool that is paid out when the game ends More games to choose from Championship structure where winners get an NFT that allows to compete for bigger prizes in next tier Adding support for mainnet (Currently, only testnet is supported) Adding support for more wallets More engaging UX with animations etc., making it feel more like a game Validation on frontend of contract digest to make sure users aren't tricked into doing transactions on a malicious contract <div