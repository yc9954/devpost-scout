---
slug: "vapor-protocol"
url: "https://devpost.com/software/vapor-protocol"
title: "Vapor Protocol"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 538
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Vapor Protocol

> Vapor Protocol helps users exchange tokens or fiat for gas on different chains without needing to go through a centralized party.

[Devpost](https://devpost.com/software/vapor-protocol) · hackathon [[TreeHacks 2023]]

## Facets

**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** css, html, react, solidity, webflow

## How they structured the write-up

- critical notes:
- what inspired you?
- if we had more time
- how we built our project
- challenges we faced

## Body

Landing page (1/2) Landing page (2/2) App page Critical notes: Website MUST be viewed between 67% and 75% on any Mac or Windows laptop Website What inspired you? We were inspired to build this project to solve one of the most core problems experienced by native and non-native Crypto users. Needing native gas to process transactions on a new chain is a nightmare to acquire and necessitates a centralized exchange that the user can interact with (with all the pain points of CEXs like KYC and delays). We’ve figured out a way to use Zetachain’s cross-chain swaps to be able to send gas to any chain as long as you have some tokens on one chain. This way, users don’t have to route through CEX and acquire gas without touching a custodial actor. If we had more time One of the best ways to improve our product would be to incorporate fiat onramps so users don’t have to have any existing tokens on any chain to split gas across chains. Integrating Stripe or Ramp Network would be simple to do but we ran out of time to look into it. This feature would make our product fully abstracted for the Web3 newbie, allowing them to start with gas on any chain they wanted using the fiat money they already possess. How we built our project On the backend, we implemented a Solidity smart contract that conducted cross-chain swaps. This contract would first take the native token on the first chain and use the Uniswap quoter and router to swap it into ZETA tokens on the first chain. Then, we would use Zetachain’s cross chain messaging Connector API to send the ZETA tokens to a second chain. On receiving these tokens on the second chain, the smart contract would deconstruct the message, then use the Uniswap quoter and router again to swap the ZETA tokens back into the desired native token on the second chain. On the frontend, we used a combination of Webflow and React. We used Webflow to make a landing page that described many of the features of our project as well as a sample user flow. For the actual smart contract interaction, we linked the Webflow landing page to a React page that uses web3.js to interact with the smart contracts. Setting up the smart contracts was quite involved. First, we had to deploy this contract onto every single chain that we wanted to potentially swap tokens into. Then, we had to call the setInteractorByChainId function so that each contract would know where its counterparts on other chains lived. After all of this was set up, swaps were ready to be made by the user. Challenges we faced This was the first time any of us had dealt with programming on the blockchain across chains. Thinking in terms of sending messages across chains was quite challenging but also very rewarding once we understood the programming paradigms. Our biggest difficulty was the transaction not succeeding on the other side of the bridge. While we have a few guesses as to why that may be, we had difficulty navigating the block explorer and the documentation, so we were unable to understand exactly why transactions were failing. <div