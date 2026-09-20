---
slug: "degenjack"
url: "https://devpost.com/software/degenjack"
title: "DegenJack"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 424
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# DegenJack

> DegenJack is a smart contract that gives users the chance of multiplying their MATIC holding by up to 4x. It is a play-to-earn game wherein players have to play 2 hands of the HiLo card game.

[Devpost](https://devpost.com/software/degenjack) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** alchemyapi, chainlink, ethers.js, figma, ipfs, keepers, openzeppelin, react, solidity, spheron, vrf, wagmi.sh

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for degenjack

## Body

NFT Minting site Landing Page Inspiration We've seen and played a lot of games on web2 and web3. What was cool about web3 games is that they were community owned and everything was focused around the communities. We wanted to build something that resonated with this idea. What it does DegenJack is a smart contract that allows users to play our take on the HiLo card game. As a player, you stand the chance of multiplying your bet amount by upto 4x. Since the game is a smart contract by itself, every action is a transaction. This includes card flips and placing bets. How we built it The game contract uses Chainlink VRF to draw random card values. Based on the cards drawn and the bet that the player made, they win or lose their hand. The payout multiplier for wins depends on the drawn card and the probability of winning the bet that they made. We also have Degenjack Supporter NFTs, the sales of which are used to fund the game treasury. The media for the NFT is stored on IPFS. When a bet is made in the game, a portion of it is taken as a commission - part distributed to the Builders team (managed with a Payment Splitter contract), and part to the NFT holders. This is distributed amongst the NFT holders on a weekly cadence, and this schedule is managed with Chainlink Keepers. The game UI has been built on React, and uses ethers.js and wagmi.sh to interact with the contract. The app has been deployed on Spheron. Challenges we ran into We faced a number of challenges while building DegenJack. Here's a list of a few of them: Figuring out an economic model to make the treasury self-sustaining. Finding the rights tools to build with. Connecting the game contract with the NFT contract. Automating holders rewards to NFT holders. Working on a Web3 project in general. Accomplishments that we're proud of This whole project is an accomplishment for us. When we started out, we just had an idea of what we want the final product to look like with no clue about how we're going to go about building it. Slowly, everything started coming together and now here we are. In a matter of a couple of months, we've gone from ideation to implementation to completion. What's next for DegenJack We are now focused on understanding the legalities of a game like this. It's essential we figure this out so that we can launch the project on mainnet. <div