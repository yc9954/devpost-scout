---
slug: "batmon-nanana"
url: "https://devpost.com/software/batmon-nanana"
title: "BatMon:NaNaNa"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 361
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# BatMon:NaNaNa

> **BatMon:NaNaNa** is a fully on-chain strategy game in which the player programs their own monsters which he uses to battle agains and capture new monsters with more advanced skills.

[Devpost](https://devpost.com/software/batmon-nanana) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** chainlink, hardhat, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for batmon:nanana

## Body

Landing Page Play Page Match Playout Inspiration The game was inspired by the popular Pokemon game. What it does The BatMon:NaNaNa game asks the question of what kind of game can be built purely on-chain. The goal of the game is to capture all of the monsters inside it. It is organized in levels, with each level containing a new monster. The player must conquer the monster on the current level in order to advance to the next one. Each monster has a unique set of skills which can be used to form sequences - giving rise to programmable Battle Monsters - BatMon. The player programs their own monster using these sequences and unleashes them. How we built it The project uses Chainlink's VRFv2 The chosen chain is : Polygon Mumbai (Solidity contracts developed/deployed using Hardhat) There are two main smart contracts - BatMon (contains all of the game logic) and ProgressNFT (associates an NFT with the progress in the game) The frontend was built using React Game Flow explained The layer registers - performs a transaction which mints an NFT associated with their progress in BatMon Player is presented with an opposing monster (their stats and skills) Player chooses their monster and programs it Player starts the battle - performs a transaction which stores the match metadata and calls the requestRandomWords() function Player waits for the fulfillRandomWords(...) to get called and is automatically redirected to see how the match was played out (once the random number is known, the outcome of the match can be determined) If the player has won he claims the monster (transaction which performs on-chain validation that the match was won and if successful captures the monster) The player moves back to step 2 Challenges we ran into Making it all work together :) Incorporating the whole game logic in one smart contract (it was especially hard enabling the programming of player's monsters) Debugging of hard to catch bugs in the contracts Accomplishments that we're proud of Finishing the hackathon What we learned A lot about Chainlink's VRFv2 and Polygon chain What's next for BatMon:NaNaNa More monsters, more complex patterns/sequences Player vs Player Tournaments ... <div