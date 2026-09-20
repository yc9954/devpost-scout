---
slug: "7ball"
url: "https://devpost.com/software/7ball"
title: "7ball"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 280
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# 7ball

> Decentralized and automated lottery game, where users have to guess 7 numbers correctly to win jackpot or at least 3 to qualify for smaller reward.

[Devpost](https://devpost.com/software/7ball) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets


**stack** chainlink, hardhat, react, solidity, typescript

## How they structured the write-up

- what it does
- how it works
- game rules

## Body

front section game section What it does 7ball is decentralized lottery game based on the popular worldwide Jackpot game, where players have to guess 7 numbers that will be randomly drawn in the future, and if someone succeed, then he will win the jackpot cumulative prize, or the pool will be split evenly if there will be more tickets that matched all 7 numbers. How it works Lottery is based on time. Users have: 60 minutes to buy lottery tickets After this time pass, lottery will draw random numbers and buying tickets will no longer be possible untill the game will reset. And after the numbers are drawn, users have: 20 minutes to check what numbers were drawn by the lottery. And after this time will pass, game will reset, delete all the data like sent tickets, drawn numbers, etc., and new game will begin, so users can buy new tickets and try to guess numbers for next lottery. (this is for testing purposes) Game rules Prize pool is cumulative and it's locked in smart contract until at least one ticket will match all 7 randomly selected numbers, and if that happen, prize pool will start cumulating again for next lottery. Anyone can buy and send ticket to the lottery with 7 selected numbers. Distribution of tickets revenue: 90% to cumulative prize pool 10% to protocol pool claimable only by admin Admin can fund contract with his own tokens which will be stored in "adminPool" variable, and he will be eligible to withdraw this funds later on. Winners are checked after every lottery, and rewards are claimable at any time. Users can buy as many tickets as they want. <div