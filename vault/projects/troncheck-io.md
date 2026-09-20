---
slug: "troncheck-io"
url: "https://devpost.com/software/troncheck-io"
title: "Shatranj"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 314
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Shatranj

> The classic game of chess with a modern prize for winning.

[Devpost](https://devpost.com/software/troncheck-io) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets


**stack** chakraui, chess.js, ethers, next.js, postgresql, python, react, socket.io, solidity, truffle

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for shatranj

## Body

Inspiration We know that Chess games are widely popular today. What if we can make it more interesting and attract more users to play? So I came up with the idea to stake tokens. Whoever wins takes it all. What it does Shatranj is the Web3 implementation of the popular Web2 Application, chess.com. Shatranj increases the incentive and the stake to play this classic ancient game with Ib3 tokens I call Ashrafi (ancient coins in India) $ASHF. Both players of the game that connect using our special matchmaking algorithm agree on a bid amount and the winner of the game takes all the $ASHF (game token) in the prize pool. In short, Shatranj is the Ib3 implementation of the popular Ib2 Application, chess.com. How I built it I used Figma for UI designing. For Frontend, I used next.js and Chakra UI, and chess.js. For the Backend, I used python, PostgreSQL, and AWS. For the web3 part I have used : Ethers Truffle Solidity Metamask Web3 Token Ganache-CLI (For Testing Purposes) Polygon Network ASHF - ERC20 Token Deployed on Polygon Network Challenges I ran into Handling the Chess Board moves was a challenge for us and I had to pick between writing the code from scratch or using a pre-existing library. For Shatranj, I chose to have the best elements from both worlds and I ended up using chess.js and react-chessboard. Implementing the architecture was a difficult task too. IbSocket doesn't come with CORS inbuilt and I took a significant amount of time to resolve the CORS errors. Another issue was connecting MetaMask and minting contracts as well as the deployment of the local blockchain. Accomplishments that we're proud of The UI of the app and its functionality. What I learned Building a full-stack app on web3. What's next for Shatranj Converting this project to TRON/BTTC and releasing it publicly as soon as possible. <div