---
slug: "iot-tbd"
url: "https://devpost.com/software/iot-tbd"
title: "Strong Incentive"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 802
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/financial_record"
---

# Strong Incentive

> Incentivize people to host and maintain IOT devices. This hackathon project was inspired by real need my non-profit (https://frankyants.org) currently faces. I'm sure it'd help others too!

[Devpost](https://devpost.com/software/iot-tbd) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: realtime_stream</sub>
**substrate** [[financial_record]]

**stack** chainlink, chainlink-keepers, google-cloud, javascript, purpleair, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for strong incentive

## Body

Chainlink UpPeep performing upkeeps on the deployed Strong Incentive contract Two real-time Yerevan air quality widgets on Frankyants.org PurpleAir air quality sensor Inspiration The inspiration came from the problem I face since earlier this year. I need reliable people to host and maintain outdoor air quality sensors. This is for my non-profit project. It aims to bring attention to the air quality problem in Yerevan, the capital of Armenia. More details can be found at Frankyants.org . The most reliable hosts so far have been my relatives. However, for the project to help cover the city with enough sensors, I need more hosts than just my relatives. I feel I will be able to find enough hosts if there is a reliable reward system for people hosting and maintaining the sensors. The hosting requires providing electricity and internet. The maintenance requires replacing the internal fan and filter when they wear out. What it does The goal is to automatically and reliably reward the hosts for each IoT device they host and maintain. I use the PurpleAir air quality sensor in this hackathon project to demonstrate the use case based on my experience. I believe many similar use cases are possible and would be popular. How I built it To demonstrate how it could work I developed an external adapter and 2 smart contracts. The external adapter connects to sensors and gathers parameters via the API. These parameters help understand if the sensor has been offline and for how long, confirm that it is placed outside, confirm that it does not need maintenance etc. Based on the data the external adapter responds with the proportion of the reward payout earned for the sensor, e.g. 100 meaning 100% of the payout. The first smart contract ( APIConsumer.sol ) checks if the host is to be paid for the hosted sensors. To do that it makes requests to the external adapter via ChainlinkClient based HTTP Get (for now). The adapter is hosted on Google Cloud for the demo purposes. I've already started a discussion on discord with a Chainlink node operator about hosting the adapter. The second smart contract ( Trigger.sol ) is a Chainlink Keeper compatible contract that triggers the first at the specified update interval. I set the interval to 1 minute for test and demo purposes. The interval should be increased in production. To manage the Keeper contract I registered the Chainlink UpKeep Strong Incentive Chainlink Demo . As long as the UpKeep and corresponding APIConsumer are funded, the upkeep is performed every minute and the transactions can be seen on Etherscan . Challenges I ran into This was my first solidity code, first blockchain work, and so on. You can imagine. Pretty much everything blockchain related seemed like a challenge. The teaching materials and my software development and architecture experience helped me grasp things relatively quickly and build something working. Big thanks to Patrick and others who helped produce the documentation, examples, and videos. Otherwise, I would be just an observer. Accomplishments that I'm proud of At first implementing my idea on Chainlink and blockchain seemed overwhelming, because the tools and processes I am used to are not applicable or available there. I learned new ways of doing things, e.g. using Keepers instead of Cron. In the end I made everything necessary to prove my concept using Chainlink and blockchain and learned a lot along the way. I feel proud and super pumped to continue to the next stage of my project. What I learned Before the hackathon I knew some general theory about blockchains and some concepts about specific blockchain projects like Chainlink. The hackathon helped me start practicing and in the process learn much more about Ethereum blockchain, oracles, smart contracts, side-chains, tokens, wallets, blockchain transactions, state, and so on. What's next for Strong Incentive I need to figure out what is necessary to make Strong Incentive work in real life. It must be cost effective, reliable, and gather enough interest to cover the development costs. I believe there are others who have a need similar to mine and not necessarily with air sensors, but with all kinds of sensors and IoT devices. I will try to find those people and get their feedback. In the meantime, I would like to continue building my solution to learn more about smart contracts, oracles, and blockchains in general. I plan to partner with a node-operator to make my external-adapter available on Chainlink. I would like to experiment with Open Zeppelin and other libraries that help make smart contracts reliable and secure. I am glad that the Chainlink development community is supportive. I am sure I will have plenty of questions along the way. At some point soon, I hope to organize an experienced team to bring Strong Incentive to fruition. <div