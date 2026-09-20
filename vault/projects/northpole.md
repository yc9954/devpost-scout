---
slug: "northpole"
url: "https://devpost.com/software/northpole"
title: "Northpole"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 732
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Northpole

> A binary options platform for European electricity markets

[Devpost](https://devpost.com/software/northpole) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, chainlink, ipfs, linkpool, moralis, nordpool, python, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for northpole

## Body

Technology architecture overview of the platform Northpole logo Inspiration The rising electricity prices of the past year have not gone unnoticed by anyone, and with the ongoing inflationary pressures and geopolitical instabilities most analysts expect prices to remain elevated for some time ahead. Moreover, structural deficits of natural gas inventories and stable base power also give rise to very high price volatility during peak loads, which can squeeze corporations and retail customers alike. Some of my co-workers like to play a game where they take bets on the closing price of the Nordic electricity system futures for each month and the winner gets a free lunch paid for by the loser. I figured that this would make for an interesting and useful decentralized financial product which would allow retail customers to easily hedge their exposure to electricity prices in a trustless way, while also giving institutional parties a transparent way to sell parametric insurance/binary options on the underlying physical energy price. What it does Northpole is a decentralized platform which allows for the exchange and settlement of binary options on the physical energy markets in Sweden and Finland (and the Nordic System price). Institutional investors or a general insurance provider can create and list contracts on the average physical energy price in a specified electricity price area during a given date. Prospective buyers can browse and purchase contracts, which moves the underlying smart contract to an active state. Once the duration of the contract is over, one of the parties query a Chainlink oracle which provides the average spot price during the time period, and the escrowed funds are automatically paid out to the winner. How we built it The Northpole smart contracts are deployed on the Polygon Mumbai PoS testnet and are arbitrated by a Chainlink node which retrieves the average spot price for the price area and time period in question. This is done using a custom external adapter for the Nord Pool power market built with python and deployed as a lambda function. The front end is built using react and javascript, using Moralis to handle databases and users. IPFS is used to host the contract image resources. Challenges we ran into This was my first time working with solidity events, Moralis and front ends in general, which required some effort to get started. Thankfully, Moralis regularly provides code along projects where you learn to build web3 versions of popular web2 websites step-by-step. I learned the basics of web3 front end development by experimenting with the web3uikit resources and forking their Airbnb repo, which provided the front end base for my project. I also ran into a few limitations with solidity optimization and contract size, which limited the scope of the project. Accomplishments that we're proud of I'm really happy to have finally learned full stack development for building web3 applications, and I feel privileged to be in a position where I was able to create a hybrid smart contract powered application addressing (and hopefully improving) the predictability of electricity costs for retail customers. What we learned I drastically improved my solidity skills and become more proficient in full stack web3 development in general. What's next for Northpole The current state of the platform is only a minimal proof-of-concept. There are many improvements to be made to the protocol, and also several features I had neither the time nor developer resources to implement. Among them are custom energy contract sizing in MWh, the possibility to aggregate a larger amount of contracts to be settled through a single oracle call through a keeper network (this would be necessary to make the costs palatable for insurance providers) and providing historical market data to help users assess contract terms. For a production version, you would also change the duration of the contracts to be settled over months or quarters, currently the default duration is one day for testing. It would also be desirable to diversify the data sources and nodes. The largest impediment to widespread adoption of such a platform is that the majority of potential users do not use web3 protocols today, and would only start doing so after the negative outcomes that the platform aims to alleviate occur. Thus, a logical improvement would be to integrate purchase and settlement with legacy payment rails through cross chain communications in order to facilitate pricing and escrow of the contracts in fiat. <div