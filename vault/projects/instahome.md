---
slug: "instahome"
url: "https://devpost.com/software/instahome"
title: "Realindex"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 854
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Realindex

> Realindex is a synthetic asset protocol that brings off-chain real estate data on the blockchain and allows users to invest in the real estate of global cities and neighbourhoods.

[Devpost](https://devpost.com/software/instahome) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]
**substrate** [[financial_record]] [[geospatial]]

**stack** amazon-cloudfront-cdn, amazon-dynamodb, amazon-ec2, amazon-lambda, amazon-ses, amazon-web-services, chainlink, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for realindex

## Body

user dashboard Inspiration • Investing in real estate is a time-consuming, operationally constrained process that is only available to those with the financial ability to put down a large deposit. • Many crypto holders want to invest in real estate without going through TradFi routes. Attempts have been made to solve this problem, however, many of these solutions e.g. tokenized real estate suffer from scalability issues and regulatory constraints. • Ultimately, with Realindex we wanted to enable investing in real estate in a decentralised way and without the need to leave the crypto world. What it does Realindex enables index based investing for real estate of global cities, using a synthetic asset protocol on the blockchain that bridges on-chain tokens with off-chain real estate data. Each token is tied to a price feed of a specific city that is representative of the average price of that city. Every single real estate transaction that happened in a given city is tracked using government published data, then the price of each token is updated to represent the average price of this market region. Users can then swap USDC for this token and in this way they buy exposure to real estate which is diversified (the entire market Vs one property in one location), without discounts to the net asset value (NAV), and without ongoing management fees. In addition, we provide analytics for off-chain real estate transactional data, so that users can make informed decisions when transacting on-chain. How we built it Each token represents a certain region in the world, pegged to the region’s average house price. Our first token for the hackathon represents London. We used Chainlink to bring off-chain house price data on the blockchain. Our swap contract then integrates with Chainlink GBP/USD price feed to provide real-time currency conversion and allow users to swap USDC for tokens of each region. The front end was built with Next.js and we have a backend using AWS Lambda and AWS DynamoDB to handle waitlist registrations. Challenges we ran into • We started the hackathon with no experience in solidity and learning from scratch in such a short period of time was a challenge. • Working with chainlink also presented challenges due to insufficient documentation and a lack of publicly documented available nodes on the testnet. • Moreover, we had to make changes due to differing testnet and mainnet implementations of the chainlink token interface and difficulty in obtaining official testnet USDC. • At last, integrating web3 functionality to our app was also challenging as we would often face significant precision loss during calculations. Accomplishments that we're proud of • Despite a steep learning curve and starting the hackathon late, we managed to develop and release a stand-alone product quickly. • We were able to deploy both our web app and smart contracts on the mainnet in less than a month of work, something we thought was impossible before we started due to our lack of experience and knowledge. • We are also proud for working on a project that we consider it to be net a positive for the world. What we learned We learned new technical skills; how to design, write, test and deploy smart contracts in solidity. We also learned a lot about Polygon, Chainlink and also further expanded our knowledge on various AWS solutions. We also developed our team-work abilities. At last, we got a deep understanding of users; we built this product after talking to 50 users, understood the problems they have when investing in real estate, and their problems when they are trying to diversify their crypto to alternative assets. We learned that for the vast majority of them it’s important to be able to buy real estate without the need to convert to fiat, while one third of users mentioned they would prefer to be able to do this in a decentralised way. This last group is now our target user. What's next for Realindex • We got 400+ people in the waitlist over the past 4 weeks and our plan over the subsequent 4 weeks is to convert 100 of those people to paying users. • Over the next 3 months, we plan to develop the lending protocol. First, this will enable counter-parties in the contract at the sell-side (Realindex is currently the only counterparty). The lending protocol will also enable people to short the market and for the first time everyone will be able to bet against the real estate market as well as hedge their exposure against real estate price drops. At last, the lending protocol will enable landlords to access liquidity on the blockchain. • We will also integrate with AMMs. AMM liquidity pools will represent a group of users lending crypto assets in order to keep a specific city/market liquid. These lenders will receive fees in return and traders are providers with a liquid market. • Next, by end of the November we aim to add New York, and New Delhi to the cities users can invest in and ultimately our vision is to do this for every city and neighbourhood in the world. <div