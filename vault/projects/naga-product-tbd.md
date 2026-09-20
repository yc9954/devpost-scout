---
slug: "naga-product-tbd"
url: "https://devpost.com/software/naga-product-tbd"
title: "SLP Manager"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 615
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/general_public"
---

# SLP Manager

> The SLP liquidity pool that can help every Axie manager to send SLP to scholar to their scholar. Scholars can easily check and claim their SLP credit by themself without 15 days waiting time period.

[Devpost](https://devpost.com/software/naga-product-tbd) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]] [[labor_employment]]
**user** [[general_public]]

**stack** api, chainlink-custom-api, chainlink-keeper, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for slp manager

## Body

Inspiration We run Axie scholarship program one of the most famous NFT game right now. We have more than 50 members in our guild and the problem is when we have to claim SLP token and pay to our scholar. If you are Axie Manager you have to claim token by yourself every 15 days and pay to scholar for everyone who play for your guild. Why can't we just let scholar claim token by themself? There is no feature like that in Axie right now so we decide to create it by ourself. What it does We would like to introduce SLP Manager, the smart contract that can let scholar claim SLP token by them self without asking their manager which waste their time. They can earn their return in realtime without waiting for 15 days period like before. They can use Metamask Wallet to connect our DApp, check balance and claim their token. This is risk free, save a ton of time and less human error. guildMaster have to collateralize SLP token for their scholarship and account SLP token for each member in the guild. guildMaster can freely change percentShare and member in every way they want in less process. In scholar side, all we need is Ronin Wallet Address to get data from Axie Infinity Game and Metamask Wallet to receive their wage. How we built it We use APIConsumer contract to receive and feed all needed data to Blockchain from and account the claimable SLP that our scholar should get and automate API call by using Chainlink keeper to call updateBalance function everyday. Challenges we ran into How to create incentive for our team to succeed this hackathon. This is very hard to hack together especially during the Covid pandemic. It hard to work by just talk on internet so we decide to have a have camping together in hotel for 3 days and that is turn out to be the most wonderful hacekathon camp I ever had. We got the first API Consumer for our ever and that is amazing even it hard to find API that actually work from Axie Infinity but we got it. We face many error that we don't understand but with good help from people in discord that can help us overcome it. Accomplishments that we're proud of We got the product that can solve our pain and that is so satisfied. The SLP manager is ready to use with a bit of decoration we believe it will reduce a lot of work that we have to manage. We got the solidity contract that work on testnet, we got web3 frontend to interact with and we have experience for using Chainlink product like Chainlink Keeper and any API. And even we didn't use it right now but we proud to tell you that we already have Chainlink node and we will modify and use it in the future. What we learned We learn a lot from this hackathon. We create our ever first contarct that can call external API and that's so cool. One of my team finish the web3 frontend even he never write it before. What's next for SLP Manager We will use it for real production in very soon. We will test our product with only our guild and keep improve so other guild can join this tool then when we confidence with our product we will start to contact Mavis Hub for scale this product to official feature of Axie Infity. This will help a lot of work from every Axie manager and create to utility of SLP single pool on their farm for using as collateralize and earning fee. <div