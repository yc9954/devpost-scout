---
slug: "hippo-predict"
url: "https://devpost.com/software/hippo-predict"
title: "Hippo Predict"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 880
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Hippo Predict

> PancakeSwap-Prediction clone with improved decentralization and game mechanics to incentivize game play and user adoption

[Devpost](https://devpost.com/software/hippo-predict) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]]
**substrate** [[financial_record]] [[structured_db]]

**stack** solidity

## How they structured the write-up

- chainlink hackathon fall 2021
- a - decentralization:
- b - sharing with community:
- c - community decisions

## Body

To be concept design for the game page Hippo Prediction Chainlink Hackathon Fall 2021 Hippo Prediction is a enhanced clone of PancakeSwap-Prediction game with changes in game protocol to increase decentralization and to incentivize game play and user adoption. We enhanced 3 critical aspects of the game A - Decentralization B - Community Sharing C - Community Decisions We targeted to change the centralized implementation of the original protocol by removing any privileged user access to stop or cancel the game and we allowed anyone to start the rounds. We believe in the power of community so we decided to share the earnings with players and game keepers by implementing our own raffle system. And lastly unlike the original protocol we allow players to choose which price pair to predict by voting on ChainLink price feed oracles. The problems and how we addressed them A - Decentralization: The original protocol has centralized methods that could be used against the will of the players. Here are some problems we targeted and fixed: Centralization problems and our fixes : Pancakeswap Hippo Prediction The original protocol is dependent on the admin/operator’s execution. We have removed the modifiers of privileged methods that could and allowed game keepers to start the rounds. We are giving raffle tickets to incentivize the continuous execution of the game. Anyone can now start the rounds and earn raffle tickets in exchange. The original protocol the execution of a round depends on the privileged accounts, they can make an insider bet; then when they understand they are going to lose they can simply pause or don’t execute the round so the round will be cancelled and they get their bet back. In our system we don't have a privilege method to pause the game and anyone can start a new round and finalize the previous round. The original system depends on the latest price feed from the oracle to execute. If the round is not executed in a timely manner the round is cancelled. Similar to the insider abuse, if an attacker has a bet and foresees an odds against him, they can attack the protocol or the operator to prevent the round being executed and get their bet back. Our system can complete a round even after a year; by using the on chain data of Chainlink price feeds, if somehow our rounds are not executed in time, they are not paused and any member can execute the completion of an older round. The smart contract simply goes back and finds the latest answer of the oracle before that round’s ending time. B - Sharing with Community: In order to make the game more community based; we wanted to share the betting commissions with the community. This sharing happens with two different systems: -Raffle System: Whenever a user makes a bet a portion of the amount goes into the raffle contract and the user gets tickets for the Raffle round. The raffles are drawn randomly by using Chainlink VRF and all the collected commissions are distributed to the winners. Every player has a chance of winning proportional to the number of tickets they collected. In order to encourage users to keep playing the game for multiple rounds instead of a single large bet on a single round; we designed a logarithmic distributing algorithm to decrease the amount of tickets given as the bet amount increases. An example of ticket distribution depending on the multipliers is as follows: 0.01 matic : 1 ticket 0.1 matic : 7 tickets 1 matic : 11 tickets 10 matic : 16 tickets 100 matic : 22 tickets -Reference System: As a community based system, we want to grow our community with their references. Therefore we give back the commission fees to referrers and referees. Every user that used a reference code will simply get back a portion of their commissions when they claim a winning round. Every user can use only one reference code. Every user that referred others; will get a portion of those users' betting commissions when they claim their winning round. Every user can refer unlimited users and get a part of their commission. C - Community Decisions The original protocol was limited to bet on a predefined price BNB/USD pair that could not be altered by the community. Thanks to more than 60 Chainlink price feed Oracles on Polygon updating every 27 seconds, we implemented a voting system to let our community decide on the target token pair. Whenever the voting round ends, the most voted Chainlink oracle takes up the place and starts feeding the new rounds’ price. Tech Stack Thanks to the sponsors of Chainlink Hackathon, we were able to implement our strategy. Technology Description Polygon Thanks to the fast transactions and low gas cost, the game runs smoothly and with less burden to the users Chainlink PriceFeeds Getting data from 60+ Chainlink Pricefeed Oracles. The target oracle is chosen by the community Chainlink VRF Getting random from Chainlink VRF Oracle for the Raffle System Moralis Thanks to syncing our contract events to the Moralis Database; we were able to get and calculate the data required for frontend. Especially on leaderboard, raffle and voting statistics and data. Contracts Deployed: HippoPrediction Raffle Reference RandomNumberConsumer Frontend Repo # HippoPrediction <div