---
slug: "debet-kyacl3"
url: "https://devpost.com/software/debet-kyacl3"
title: "deBetting"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 504
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/legal_justice"
---

# deBetting

> Football betting app with use of Chainlink Node and Yearn protocol to multiply the prize pool

[Devpost](https://devpost.com/software/debet-kyacl3) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[legal_justice]]

**stack** chainlink, docker, express.js, goerli, javascript, metamask, node.js, postgresql, react.js, solidity, usedapp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for debetting

## Body

Landing page Matches page Inspiration The motivation was the lack of a real, decentralized solution for sports betting available on the market (major solutions are actually centralized), and we also found the revenues for winners unattractive. What it does The project to be sent as hackaton work is a football betting app. Betting is performed fully on blockchain and Chainlink Oracle is used for feeding smartcontracts with match results - external adapter connects to football results api. Moreover, the pool of tokens sent by the user to bet is sent to Yearn protocol, which makes tokens ‘work’ additionally, generating more income for players. For additional revenue from using the app, is a dedicated “BET” token for those who win the game. Core functionalities Getting information about upcoming matches Betting for match results: Team A wins, Team B wins, Draw Depositing and withdrawal of DAI token (to bet/to get prize) Buying and minting BET tokens to boost your vote App logic remarks Users can bet only once for a single match, depositing DAI tokens Betting app does not store any tokens, it sends them directly to Yearn protocol Each winner gets 1 BET token. After collecting 1000+ BET tokens, they can count on increased prize Increased prize is from Yearn-ed surplus, airdropped to winners proportionally to BET token ownership to total supply How we built it Smartcontracts - deployed to Goerli Ethereum testnet. They are divided by: betting app logic, integration with Chainlink Oracle, ERC20 “BET” token and integration with Yearn protocol Frontend - connects to backed for cached data and with blockchain to allow users interact with the application Backend - caches necessary information to guarantee app performance and reduce usage costs and takes role of External Adapter for feeding the Chainlink node Chainlink node - the Chainlink module that processes requests from smartcontracts, connects with external API and feeds smartcontracts back with match results Challenges we ran into Yearn protocol is not available on Goerli testnet - we had to mock it unless having the project deployed on Ethereum mainnet. We have a strategy to test the app on mainnet fork with real yearn adapter, and at goerli while testing chainlink oracle. Bugs in Chainlink Node, but fortunately we overcame them :) e.g. https://github.com/smartcontractkit/chainlink/issues/7684 (we used strings instead) Accomplishments that we're proud of Despite the project is for educational purpose, we managed to develop a beautiful design Successfully tested all the app components, despite the fact that Yearn is not available on Goerli. Making valuable relations between team members. We successfully made a permissionless solution that is not yet available on the market (not that attractive as ours) What we learned Fruitful team work in Scrum Using Chainlink Oracles, running Chainlink Node Writing jobs for Chainlink Node in TOML Integrating frontend with smartcontracts using ethers.js framework Using Yearn protocol from smartcontracts What's next for deBetting The project has a huge potential to be commercialized and deployed to mainnet, although it requires a serious legal and business development - that might be challenging. <div