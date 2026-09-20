---
slug: "random-as-a-service-raas"
url: "https://devpost.com/software/random-as-a-service-raas"
title: "Random As A Service (RAAS)"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Random As A Service (RAAS)

> Random As A Service (RAAS) powered by chainlink. RAAS provides chainlink verifiable Random Function as a simple REST api.

[Devpost](https://devpost.com/software/random-as-a-service-raas) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** alchemyapi, automation, chainlink, connect-any-api, deta, fastapi, javascript, polygon, python, quasar, solidity, vrfv2, vuejs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for random as a service (raas)

## Body

Inspiration This project was greatly influenced by the session on Using Chainlink services in your web2 applications by Richard. One of the effective route to web3 adoption is abstraction. Abstraction allows web2 developers and users to interact with web3 with minimal friction. This project therefore aims to abstract the chainlink services and the blockchain component. RAAS allows web2 developers and users to interact with the blockchain without a crypto wallet or having to hold crypto. What it does RAAS provides chainlink VRF v2 as a simple REST api. How I built it This project comprises of four parts, the smart contract, the api, the demoapi to receive webhooks and the User Interface for verification. The User Interface is independent, only reads data from the blockchain rather than the api. Using the api, a user is able to request for random numbers from chainlink. The api interfaces with the smart contract which then interacts with chainlink services. The user receives a webhook with the generated random numbers. All the generated random numbers are displayed on the verification dapp. Challenges I ran into The main challenge was the project architecture. Abstracting multiple chainlink services in a single REST API was challenging. Accomplishments that I'm proud of During the hackathon, I learned alot. Read alot of chainlink documentation. I am very proud that using the resources available, I have been able to start working on RAAS and complete the project. What I learned Every process of creating the project was a learning oppotunity. I learned more on solidity, considering I knew some basic Vyper. Verification of solidity contracts, working with events. And the most important lesson, fulfillRandomWords should never revert. What's next for Random As A Service (RAAS) RAAS can be offered as a paid service to lotteries, casinos and any use case which requires a verifiable randomness generator. <div