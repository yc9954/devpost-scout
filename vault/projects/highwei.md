---
slug: "highwei"
url: "https://devpost.com/software/highwei"
title: "HighWei"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 273
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/mental_health"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# HighWei

> Tollbooth smart contract. Chainlink node scrapes/filters/aggregates MTA toll fees with Adapter.js. Chainlink pricefeeds convert gas to tolls. Chainlink Keepers/Ultrasonics sense when to close servo.

[Devpost](https://devpost.com/software/highwei) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[mental_health]]
**substrate** [[financial_record]] [[web_dom]]

**stack** chainlink, filecoin, ipfs, javascript, polygon, python, raspberry-pi, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for highwei

## Body

Inspiration Automation solution to tollbooth issues [human error, ticket vending machine failure, depressing job]. Creates fair pricefeed aggreation using Adapter.js with Chainlink API request with MTA website fee data being webscraped using Puppeteer. What it does Tollbooth smart contract with ultrasonic sensors and servo motors. Chainlink node scrapes,filters,scales and aggregates MTA toll fee data with Adapter.js. Chainlink pricefeeds remove need for ERC20 payments. Chainlink Keepers used to close gate [servo] 15 seconds after opened. Ultrasonic sensor sends closeServoGate() Tx with web3.py when distance under 30cm AND gate open. How we built it In Solidity, Javascript, Python and HTML. Raspberry Pi 4 GPIO pins handle electronics communication. Challenges we ran into Deciding what language to use for the ultrasonic sensor. Javascript Node.js packages were not working so I ended up using Python with web3.py. Accomplishments that we're proud of The responsive demo with the ultrasonic sensor and Chainlink Keepers being a backup sensor. Being able to use an IPFS Storage CID inside a Solidity smart contract to point at Javascript logic using an Adapter.js Chainlink request to update toll price states on chain for a custom contract was cool too. What we learned That ultrasonic sensors can be used effectively to automate smart contract transactions. IPFS CID Adapter.js request saves gas in the contract compared to the raw Javascript code inside the contract. On top of that, you can have long Javascript code and not have to worry as much about the Spurious Dragon Solidity contract file size limitation (24.576 KB https://soliditydeveloper.com/max-contract-size ) What's next for HighWei To inspire more robotics projects with smart contracts. Possibly partner with groups interested in the project. <div