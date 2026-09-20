---
slug: "tpmarket-prediction-market-on-tron"
url: "https://devpost.com/software/tpmarket-prediction-market-on-tron"
title: "tpMarket - Prediction Market on Tron"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 574
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# tpMarket - Prediction Market on Tron

> tpMarket is a prediction market where users can be both market makers and takers. It supports 3 markets on testnet (TRX, BTC and JST) and 9 on mainnet (TRX, BTC, JST, ETH, SUN, NFT, BTT, USDT, USDC).

[Devpost](https://devpost.com/software/tpmarket-prediction-market-on-tron) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**substrate** [[web_dom]]

**stack** react, solidity, tron, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tpmarket - prediction market on tron

## Body

Inspiration After seeing multiple accounts on twitter engaging in making bets against each others, most famously the Algod vs Do Kwon bet regarding Luna and UST https://www.theblock.co/post/137687/terraform-labs-do-kwon-bets-1-million-on-lunas-future-price , we saw that a prediction market for over/under bets is necessary and sought after in the crypto space. With oracles and smart contracts it's possible to remove the escrow, and automate the whole process from the creation of a bet to the payout of a bet. What it does As a user you can create a market or buy a side of market that someone else has created. Two example scenarios are: You are bullish BTC and is certain that it will be above $30k on January 1st 2023. You are bearish a stablecoin and think that it will depeg. We take example 1 from above and show how a bet can go from creation to payout on tpMarket. First, you'll need to choose some parameters: Strike Price: $30 000 (the price BTC needs to hit for you to win) Expiry: 2023-01-01 (the end date) Position Size: 1000 TRX (what should the payout be?) Over Odds: 5.00 which is the same as 20% (your side) Under Odds: 1.25 which is the same as 80% (the opponent's side) NOTE : Over Odds + Under Odds = 100% always because we take 0 fees. Under Price = Position Size / Under Odds = 1000 / 1.25 = 800 TRX Someone buys it for 800 TRX which means that you'll receive 800TRX, making the input for your bet: Your stake = Position Size - List Price = 1000 - 800 TRX = 200 TRX And your opponents stake is of course 800 TRX. This table explains what will happen on January 1st: BTC Price Winner Payout $BTC is above $30000 -> You 200 TRX * 5.00 = 1000TRX $BTC is below $30000 -> Not You 800 TRX * 1.25 = 1000TRX So to summarize, if you win you'll get 1000TRX and your stake is only 200 TRX, which makes sense since 200 * 5.00 = 1000 and your odds was 5.00! When 2023 is here and if BTC is above $30k then you just go to the page that's showing active positions and click exercise, and you'll receive the payout. How we built it There are two major smart contracts, Exchange.sol which handles how markets gets transferred between users and PredictionMarket.sol which handles the creation and payouts of markets. The frontend is built with Typescript and React. Challenges we ran into The WinkLink pricefeeds are stale on testnet (not updated since october), which is a shame since they would be useful when testing. That made it a little harder for us. Accomplishments that we're proud of The fact that it's now really simple to go from the creation of a market all the way to the payout. Also the fact that you as a user can be both a maker and a taker. What we learned That everything that needs for a market to be created is a maker, and when everyone can be a maker then you'll hopefully get tons of markets. What's next for tpMarket - Prediction Market on Tron Keep working on the UI and the general UX of the website Optimize the contracts to consume less energy. Get support for more markets, and they don't have to be for cryptocurrencies. Make it possible to have whatever token you want as collateral for a position <div