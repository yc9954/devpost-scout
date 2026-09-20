---
slug: "friendly-feud"
url: "https://devpost.com/software/friendly-feud"
title: "Hivemind"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 567
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/financial_record"
---

# Hivemind

> An on-chain multiplayer polling game where you try to guess what the other players will choose for a chance to win big.

[Devpost](https://devpost.com/software/friendly-feud) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[transportation]]
**substrate** [[financial_record]]

**stack** chainlink-keepers, chainlink-vrf, ethers, hardhat, javascript, lucky-machines-railway, node.js, openzeppelin, react, solidity, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hivemind

## Body

Hivemind logo concept Demo play through screen shot Demo play through final screen Hivemind Mockup Frontend Inspiration We build on-chain gaming and infrastructure tools, and a great way to find the needs of a toolset is by making some real stuff and seeing where the problems lie. We wanted to make some sort of a mass trivia game to test out some massive on-chain player transportation and think about hidden information in the context of blockchain. We have used Polygon for all of our previous projects, and that has always worked out well, so this was a great place to try out something new. What it does Hivemind is an on-chain multiplayer polling game where you try to guess what the other players will choose for a chance to win big. Players answer a poll question and guess what they think the crowd will choose. If they guess correctly, they win points. There is an option for users to enter with a fee in MATIC, which gets added to a prize pool and distributed to the top ranked players at the end of the game. How we built it We wrote all the game logic with smart contracts in solidity. Deployments and contract interactions were handled with Hardhat, Ethers, and Web3. We prototyped frontend player interfaces with Unreal Engine and React. The demo included in this submission was built with React and Node. On-chain integrations included Chainlink VRF for randomness and Chainlink Keepers for a game loop, OpenZeppelin for access control, and Lucky Machines Railway for transporting groups of players between, and connecting, contracts. Challenges we ran into It was difficult getting a frontend to respond to on-chain events and keep local state up through all rounds and to the final results. At times transactions were taking too long to complete and would accidentally hit a timeout in the game. This is something that would potentially need to be adjusted to the current conditions of the network before each game. Accomplishments that we're proud of We got the game contracts performing well and made a fairly involved keeper interface that queues and manages a number of games, game rounds, and incoming requests (a problem that exists in most on chain games), we were able to implement a simple on-chain hidden information game, and we were able to make use of our Railway library to connect the lobby, game rounds, and winner contracts and send groups of players between them! What we learned We learned that listening to events can require different techniques between different chains and too many user transactions can detract from the gameplay experience. We will be experimenting with the use of meta-transactions to avoid user gas, and more keeper interactions to abstract away many on chain interactions. What's next for Hivemind We would love to see some more community built interfaces for this game. Our interface is a workable demo, but we think there is room for so much more, and that’s a big reason for on-chain games to exist: one backend, many frontends. We will take what we learned and developed here to continue to build out our on-chain gaming and infrastructure tools. note: the demo video shows a play through on goerli testnet, but the project is currently deployed on Polygon Mumbai testnet. All contracts are on Mumbai and here is a brief video play through of the game on there. <div