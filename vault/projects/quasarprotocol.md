---
slug: "quasarprotocol"
url: "https://devpost.com/software/quasarprotocol"
title: "QuasarProtocol"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 524
team_size: 6
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
---

# QuasarProtocol

> QuasarProtocol is a platform that creates leveraged tokens in a fully decentralized manner, made possible by MangoMarkets

[Devpost](https://devpost.com/software/quasarprotocol) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[civic_government]]

**stack** anchor, mangomarkets, pyth, react, rust, serum, solana

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quasarprotocol

## Body

Inspiration Centralized exchanges with perpetual futures contract markets such as FTX and Binance are using their markets to issue leveraged tokens, and more and more users are using them. We thought this was one of the missing DeFi blocks in the Solana ecosystem, and since MangoMarkets has already implemented decentralized perpetual futures contracts, we thought we could implement it quickly. What it does Quasar Leveraged Tokens Quasar Leveraged Tokens(QLTs) are normal SPL tokens that can give you leveraged exposure to cryptocurrency markets, without the inconvenience and worry of managing a leveraged position. Unlike existing leveraged tokens managed by centralized exchanges such as FTX and Binance, QLTs are issued in a fully decentralized manner, using MangoMarkets, which implements a decentralized perpetual futures contract. The leveraged token will automatically reinvest or sell its position for target leverage in Mango perpetual market. If your position makes money, it will reinvest your position, or if your position loses money, it will sell your position. This task will run periodically. Mint QLT When users deposit their collateral assets and create new QLTs, the Quasar program automatically deposits the collateral assets in the MangoMarkets and creates a new perpetual futures contract to match the target leverage. Redeem QLT Conversely, when users redeem QLT tokens, the Quasar program sells perpetual futures contracts held in MangoMarkets and withdraws collateral assets as much as the users redeem. Rebalance QLT When the price of the underlying asset of QLTs changes, the leverage also changes. To adjust this, the Rebalance Program is executed in QuasarProtocol at regular intervals or whenever a specific leverage value is exceeded to set the target leverage. How we built it We made a plan, did the necessary studies, and then made a product. That's it. All done in 3 weeks. Challenges we ran into MangoMarkets integration The QLT token is very closely linked to the MangoMarkets program. We first had to fully analyze and understand all the program codes in MangoMarkets, and that was our first challenge. Position and risk management Whenever each QLT token is issued or burned, perpetual futures contracts must be bought or sold on MangoMarkets according to the target leverage. At this time, optimization work was done on which account to manage each contract and how to trade. Governance and reward system Efforts were made to become a self-sustaining platform such as QLT token launch function through QSR token voting, profit distribution through QSR token staking, and liquidity supply through LP token staking. Accomplishments that we're proud of We have created a fully decentralized leveraged token platform. We are proud to have created everything from CPI to MangoMarkets program, price linkage using Pyth Oracle, and a user-friendly web interface in less than a month. What we learned Since MangoMarkets uses Serum DEX internally and Serum is the center of the Solana DeFi ecosystem, by analyzing the MangoMarkets code, we were able to learn the overall development of DeFi service in the Solana ecosystem. What's next for QuasarProtocol Our mission is to develop DeFi blocks that are still missing in the Solana blockchain one by one. Among them, we chose leveraged tokens as a starting point. <div