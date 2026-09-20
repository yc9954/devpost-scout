---
slug: "talent-mkt"
url: "https://devpost.com/software/talent-mkt"
title: "Talent Mkt"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 382
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Talent Mkt

> A dApp that allows clients to hire potential tech freelancers. Freelancers would request for a review from the client after finishing a job. Client approves for payout to be made to the customer.

[Devpost](https://devpost.com/software/talent-mkt) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**user** [[small_business]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** flow, next, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for talent mkt

## Body

Page for Freelancers to access their works and see job history Page for Client to view their transactions and histories Login Landing page Inspiration One should be able to hire brilliant talents on a transparent, yet hassle free process. Clients and freelancers can see all the records of their transactions and their status respectively What it does Freelancers showcase their service and clients get to hire them. Numbers of projects completed and amounts received from clients would be used as metrics for determining outstanding freelancers. Freelancers would request for a review from the client after finishing a job. Client hits the approve button for payout to be made to the customer. The system pays the freelancer after a certain grace period in the case of delay from the client to approve the job. Conversely, the system refunds the client’s pending fee after a given grace period has elapsed to complete the job. Hence, the freelancer performance rating drops. Clients and freelancers can see all the records of their transactions and their status respectively. How we built it The project was built with Nextjs and and deployed on the Flow blockchain. We used FCL for the frontend interaction. Challenges we ran into Seeing Flow is relatively new, we observed some level of irregularities on the error messages when updating and redeploying smart contract. For context, one would have successfully redeployed one's smart contract, but the message that follows after on the terminal would give the impression as if the deployment did not go through, thus kept one wondering what one did wrong. Accomplishments that we're proud of Getting hang of using Resources and storage on Flow What we learned Having dived into Flow and Cadence for the first time, we were able to appreciate why Flow stands out from EVM blockchain. We learnt how to use the playground to write and interact with the smart contract using different accounts We tinkered with some of the Flow ecosystem tools like dev wallet , FCL , Flow CLI , write scripts and transactions , understood the differences among Flow chains(emulator, testnet and mainnet) and when to use them. What's next for Talent Mkt Talent Mkt is far from perfect. We plan to continue developing to the MVP stage. Consequently, deploy to the main net! <div