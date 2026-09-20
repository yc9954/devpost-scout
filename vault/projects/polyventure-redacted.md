---
slug: "polyventure-redacted"
url: "https://devpost.com/software/polyventure-redacted"
title: "PolyVenture"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 306
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# PolyVenture

> Retro adventure game in which the user is trapped inside a simulation.

[Devpost](https://devpost.com/software/polyventure-redacted) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: structural_withholding</sub>

**stack** solidity, spheron, vue, web3js

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- what's next for polyventure [redacted]

## Body

Thumbnail Inspiration PolyVenture is a retro adventure game combining web3 technology with a classic adventure. The user plays through the game and finds items that will help him further in his quest. These items that the player finds are minted as NFTs. The further the users gets in the game the better items they will receive. How we built it There are 2 smart contracts that power the NFT section of the dapp. The first contract mints an access pass and the second contract mints items that the user finds in the game. The access pass allows the users to experience a full playthrough and mint the items along the way. At the end of the chapter they will receive a new access pass. This access pass system allows for building multiple episodes of the game during a longer period of time (eg allows to release a chapter every month). The NFT data is hosted on IPFS using Pinata. The frontend is built using Vue and is deployed both on IPFS through Spheron (polyventure-czuvuk.spheron.app) as well as on Netlify (polyventure.xyz) Challenges we ran into We want to ensure users are not rushed through the game to just mint the NFTs instantly. We created a play pass system that guarantees any user to mint their items, the only requirement is them having the play pass in their wallet. The other challenge was syncing from blockchain back to the frontend in case users receive items from others without querying too often. Within the item smart contract a status check was implemented to quickly get all minted items for a particular user. ERC721Enumerable was implemented to be able to get NFT balances of users play passes. What's next for PolyVenture [REDACTED] Chapter 2 is being worked on and plans are made to release the game on Polygon mainnet. <div