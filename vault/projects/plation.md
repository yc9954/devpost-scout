---
slug: "plation"
url: "https://devpost.com/software/plation"
title: "plation"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 417
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# plation

> An on-chain prediction market for inflation using Chainlink Keepers and the Truflation inflation oracle.

[Devpost](https://devpost.com/software/plation) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets


**stack** chainlink, infura, python, solidity, truflation

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for plation

## Body

Inspiration Inflation has been a big issue recently, and its been difficult to be able to get a prediction without it usually coming from singular experts, so I decided a prediction market could be a solution to being able to aggregate predictions and possibly come closer to accurate predictions for changes in inflation. What it does plation is a prediction market, where users can either bet 'Over' or 'Under' if they believe that inflation will either increase or decrease respectively. At the end of a given time period, the prediction is closed, and winners receive their initial bet back and their respective shares of the losing pool, or in the case of no change, all bets are refunded. How we built it The smart contracts for plation were written in Solidity and are deployed to the Rinkeby testnet, the UI for plation web-app was written in Javascript, there is also a seperate off-chain keeper that is written in Python which handles all the payout calculations. The technology used in the smart contracts includes: 1 Chainlink client to retrieve the Truflation inflation index, and 2 Chainlink keepers to time the closing of predictions and to keep the inflation index up to date. Challenges we ran into A couple of challenges that I ran into during the course of the project was a bit of a steep learning curve when it came to the front-end side of the dApp, I hadn't used Web3.js before. The other challenge I ran into was getting the Chainlink keeper to work with the PredictionHandler contract, there were quite a few failed attempts before I got the correct modifier on the contract. Accomplishments that we're proud of The accomplishment which I am most proud of is to have gotten all the contracts deployed and working together as the system I had designed and have the web-app up and running and able to be used. What we learned I've learnt a lot about the entire stack of dApps and Web3, what it takes to be able to put a dApp together and how much effort goes into large projects. What's next for plation Next steps for plation would be, To bring the python keeper script onto a Chainlink Keeper so that everything is On-Chain, Find a way to remove any custody as currently the Python keeper still needs a private key stored on an environment with the script to initiate payouts. Include other markets for inflation, and possibly a probability density function for predictions. <div