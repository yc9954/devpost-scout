---
slug: "figura"
url: "https://devpost.com/software/figura"
title: "Figura"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 576
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Figura

> Decentralized Digital Game Store using smart contracts to facilitate a marketplace and uses ChainLink oracle nodes for game price pegging, as well as on chain purchase webhooks.

[Devpost](https://devpost.com/software/figura) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: web_dom</sub>

**stack** avalanche, chainlink, css, ethers, hardhat, html, javascript, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for figura

## Body

Contract Interaction Cover Page Game Submission Page Game Store Inspiration My first conversation I ever had with my partner was at a local gaming convention. He talked about his love of gaming and his dream to publish a blockchain game on a particular PC game store. They recently banned all blockchain technology from their platform. He was absolutely crushed, and I wanted to make sure he could still achieve his dream, so I decided to make Figura. While I was researching and designing this project, I learned how traditional game marketplaces sometimes have hostile practices that impact both the publisher and player. Centralized marketplaces tend to focus primarily on profits, this causes smaller publishers to often be overlooked compared to their larger counterparts . Players who use those marketplaces are at the mercy of sometimes confusing ownership and return policies. There are over 3 billion video game players in the world, and currently, there is no marketplace that focuses on blockchain based gaming, Figura is here to change that. What it does Figura is a decentralized gaming marketplace that empowers both the player and the publisher. It works as two different NFTS, the first being the Game Directory NFT which is like the library of games, each token is a unique game submitted by a developer or studio, and the other is the Figura NFT, which acts as a record of purchase of the game sold in a given Game Directory NFT. This is done by minting a new Figura NFT only when a player executes the mint function providing which Game Directory NFT token to purchase and enough ETH to match the dollar amount the developer set (this is stored in the Game Directory NFT). How I built it I used Chainlink in the smart contracts to facilitate Oracle requests like converting prices to USD and doing webhook game server authentication. I created the contracts using solidity and hardhat. I built the front end using React and Ethers.js. I also used Metamask for testing. Challenges we ran into Not enough time! I work full time and did this project solo so I wish I had more time to improve the UI and add more necessary features like implementing a DAO to prevent spam games and downloading and running games using React Native. Accomplishments that I'm proud of I'm really proud of the smart contract design. I know that blockchain is the future, and to help be a part of that by creating a solution for players to have their DRM on chain that's transferable is really cool. It also helps publishers because entire game markets can be traded amongst publishers. What we learned I learned how to use (and appreciate) chainlink. I didn't understand what a decentralized Oracle network was before the hackathon, and now after using it for my project, I'm really excited to see other use cases. What's next for Figura Other than my partner publishing his game, I am planning to add/incorporate the following: Have downloadable game installers so that players can play the games they buy Implement a DAO to facilitate the curation, rating, and featuring of games Add validation logic to the submission page Have a user library that utilizes opensea’s API to display the NFTs in their wallet Add game categories to the submission page and marketplace Add webhooks to the submission page so publishers can monetize their works directly on Figura Update the marketplace to include prices <div