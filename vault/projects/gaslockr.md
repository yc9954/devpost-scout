---
slug: "gaslockr"
url: "https://devpost.com/software/gaslockr"
title: "PricePal"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 820
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# PricePal

> PricePal serves as the first GasFi protocol. It leverages ZK coprocessor and Amazon Forecast to create correct priced derivatives, and automatically hedge volatile gas prices by Chainlink Automation.

[Devpost](https://devpost.com/software/gaslockr) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** amazon-forecast, chainlink-automation, javascript, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of & what we learned
- what's next for pricepal

## Body

PricePal - hedging high and volatile gas prices Subscription Future GasInsure Current issues How works Inspiration We were inspired by three current on-chain issues to build PricePal. Reliability : More people than ever are using services relying on blockchains. Organizations (including DAOs) need to be able to operate through turbulent times. Services need to provide guarantees for availability through SLAs (Service Level Agreements) in order for users to trust and adopt these services e.g. AWS provides SLAs for each of its services often more than 99.99%. In the past base gas fees on Polygon have spiked to $200 for a simple token transfer. This makes blockchains even L2's unusable at times. Hence they are not currently something users and organizations can rely on all of the time. Onboarding : Users must already have tokens in their wallet to cover gas fees. This creates a chicken-and-egg problem where the user needs funds before they can do anything on-chain, presenting an unnecessary barrier to the onboarding process. Existing solutions like faucets are difficult to use and often don't provide enough to even cover the fees of a single transaction. UX : Every time a user wants to submit a transaction, they have to manually approve transactions and think about what gas price to specify. This doesn't need to be the user's concern and it often confuses new web3 users. What it does PricePal services as the first trustless GasFi protocol. It uses ZK coprocessor to read historical gas prices, and rely on Amazon forecast , a time-series forecasting service based on machine learning (ML), to provide verifiable correctly priced GasFi derivatives. The financial models in PricePal update in real-time. PricePal is interoperable with other protocols and can be used as foundational on-chain infrastructure to build protocols and services that will solve the reliability , onboarding and UX problems we face today. It also provides automatic execution by Chainlink Automation service, which monitors on-chain and credibly compensates users for losses. It provides an efficient way to hedge against the risk of rising gas prices, allowing users and organizations to rely on blockchains. Services that operate on-chain will finally be able to provide SLAs (Service Level Agreements) to their users, building trust and acting as a catalyst for web3 adoption. With our trustless financial derivatives product, other wallets or services can build on reliable infrastructure for hedging gas fees. With account abstraction (ERC-4337), paymasters provide a way for someone else to pay your gas fees so that the user don't need any tokens in their wallet to start interacting on chain. For example, they can pay a monthly subscription fee to a paymaster in fiat to be able to submit up to 100 transactions in a month. Or a service could offer to pay for your first 5 transactions using their service. With account abstraction, users can create a session key just like logging into a game where they pre-approve particular transactions. Wallets can leverage this to automatically submit transactions on the user's behalf without them having to manually approve them and specify a gas price. Together with account abstraction, PricePal allows wallets to provide a seamless user experience where the user is not even aware that gas prices exist. We built GasInsure, an insurance service as a demonstration of how PricePal can be used as financial infrastructure to build amazing services. It is an insurance service that aims to provide users with protection against gas price fluctuations. Through a simple web GUI users can purchase insurance specifying how long they would like the protection for and pay a small premium to be protected against the tail risk of gas price fluctuations. The GasInsure will monitor real-time gas price and compensates users when reach set. How we built it In the smart contract, we record the logic of pricing model and uses the interface of on-chain service Axiom as the ZK coprocessor to read historical gas prices. Then we still need scripts to seed the Amazon forecast service to get predicted gas price real time. For the priced derivatives, e.g. GasInsure, we record all the insurance contracts on-chain. We uses the Chainlink Automation functions in smart contract, and the Keepers help monitor on-chain and credibly executes. Challenges we ran into We have no experience with both Amazon Forecast and Chainlink Automation, so we managed to figure these amazing services. Accomplishments that we're proud of & What we learned We successfully make our ideas presented as the product, and we gained a lot knowledge from both technical and product points of view. Also, we have deepened our understanding of blockchain and various technologies including Chainlink and Amazon services. What's next for PricePal The hackathon is a start for us, we will continue to explore services from Chainlink and other platforms to make PricePal better. Also, we will try to extend our ideas and seek to corporation, aims for improving the ecosystem of crypto world. <div