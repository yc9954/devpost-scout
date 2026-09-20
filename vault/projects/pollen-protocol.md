---
slug: "pollen-protocol"
url: "https://devpost.com/software/pollen-protocol"
title: "Pollen Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 475
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Pollen Protocol

> OpenZeppelin for the Lens Protocol

[Devpost](https://devpost.com/software/pollen-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** hardhat, solidity, vite, vitepress, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pollen protocol

## Body

Inspiration Lens Protocol is a decentralized social graph in which everything is an NFT. Your posts are NFTs, when you follow someone you get a follow NFT The development of the Pollen Protocol and Modules is inspired by these facts about the Lens Protocol: There are no standard modules that should be there by default for users to use There is no standard way to develop and propose a custom module to the ecosystem Simple modules like NFT-gated follow, Token Reward distribution on Reposting, etc. is not there in the Lens Protocol. What it does Pollen Modules is a suite of standard modules to be used by the Lens Protocol. OpenZeppelin was crucial for the adoption and development of Ethereum, Pollen Modules are the OpenZeppelin for Lens. The possibilities for the Lens Protocol to be extended are endless. In its current iteration, Pollen has the following seven modules with more to come in the future: Follow Modules NFT-Gated Multiple NFT Gated (AND) Multiple NFT Gated (OR) Profile Gated (AND) Profile Gated (OR) Reference (Repost) Modules Limited Rewards (Equally distributed Rewards on Repost) Limited Rewards Exponential (Exponentially Decreasing Rewards with each new Repost) Along with the Pollen modules, there is Pollen Protocol which is a fork of Lens Protocol purely for whitelisting and running the Pollen Modules to be battle-tested before being proposed to the Lens Community for whitelisting. How we built it The development took me through exploring the core of Lens Protocol. The modules were written within a fork of Lens Protocol, following the conventions set by the modules written by the core team. These modules were then tested and the whole fork of Lens, Pollen Protocol was deployed to a testnet. Challenges we ran into I have had three pivots around my idea since the inception. The main issue was understanding how a social network like Lens works and then understanding the internals of the protocol to develop my modules for it in the right manner. Accomplishments that we're proud of The founder of Aave and Lens Protocol, Stani Kulechov actually replied to my tweet with validation for the project and suggestion of going for a grant: https://twitter.com/StaniKulechov/status/1554117575679811585 . He also had a suggestion for a good module that can be made: https://twitter.com/StaniKulechov/status/1554117020169523203 . What we learned The Lens Protocol is newly launched. A module ecosystem needs to continue to develop new modules, rethink existing ones and carry the whole community forward. It is not a one-man job but a community effort. What's next for Pollen Protocol Development of more standard modules Further Interaction with Stani (Founder, Aave & Lens) and the Lens Protocol team on Discord to get mentorship on the right course of action for this module ecosystem Creating content related to Module development and Github templates, to make it easier to onboard new module developers into the Lens Ecosystem <div