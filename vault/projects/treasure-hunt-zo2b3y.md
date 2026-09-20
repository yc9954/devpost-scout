---
slug: "treasure-hunt-zo2b3y"
url: "https://devpost.com/software/treasure-hunt-zo2b3y"
title: "Treasure Hunt"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 392
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Treasure Hunt

> Fully on chain P2P treasure hunt using oasis' sapphire chain

[Devpost](https://devpost.com/software/treasure-hunt-zo2b3y) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**substrate** [[financial_record]] [[geospatial]]

**stack** phaser.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for treasure hunt

## Body

Inspiration I had been looking at ZK Proofs for sometime and have been thinking for sometime how to store secret information on chain so that a game can be fully on chain. Looking at dark forest, I got an idea if we can use ZK proofs to suggest player if they are near a solution or not with fixed responses. Tried this out in Solana using lightening protocol. In Oasis' sapphire protocol, implementation became a lot easier as there is option to hide data on chain. What it does It is a P2P treasure hunt where player 1 can hide a treasure in 8x8 maze and player 2 gets n number of moves to find the treasure. After each move, contract gives hint to the player 2 if they are farther/nearer/at same distance from the treasure. Player gets the option to bet some ROSE coins where winner gets the combined money in the pot minus the development fee. How we built it Challenges we ran into Coming from Solana background it took some time getting used to EVM standards. Took some time to get phaser running together with react events On the contract level, faced a specific issue where a person can guess their location is correct or not based on estimated gas fee for transaction. Accomplishments that we're proud of To get the frontend and contract complete in short span of time Also able to make a playable game which is fully on chain What we learned Only hiding the data on chain does not give complete anonymity. Sometimes gas fees can help users predict the outcome of a transaction before it is submitted. Also with this game concept, I got a lot more clarity on how to go about making a fully on chain game What's next for Treasure Hunt Make a procedurally generated 2.5d island where player can place treasure and multiple players can join and search for the treasure in a fixed time period. Island will have more features/obstacles and different type of generic clues which can help participants to search for the treasure Full map will generated with on chain data and participants progress will be saved on chain as well Think of a way to create a P2E system as well and have a way to monitize the system to setup games for end players <div