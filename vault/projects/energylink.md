---
slug: "energylink"
url: "https://devpost.com/software/energylink"
title: "EnergyLink"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 538
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/climate_energy"
---

# EnergyLink

> EnergyLink is a blockchain energy saving IoT platform that leverages power grid demand data and controls residential smart thermostats through Chainlink External Adapters and Keepers Network

[Devpost](https://devpost.com/software/energylink) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[civic_government]] [[climate_energy]]
  <sub>weak: structured_db</sub>

**stack** chainlink, firebase, gcp, nest, next.js, react, solidity

## Body

EnergyLink Frontend System Diagram Git Repo: https://github.com/firwar/ChainlinkWinter2021 EnergyLink is a blockchain energy saving IoT platform that leverages power grid demand data and controls residential smart thermostats all through Chainlink External Adapters. We created a campaign through smart contracts for power companies to deposit a fund that gets distributed to users after a set duration if they save a certain threshold of energy. The contract uses Google Nest APIs with External Adapters to read and control Nest Thermostats, US Department of energy EIA Data with External Adapter, Google Weather Oracle, and the Keeper's Network. Live Dapp Demo: (Kovan) https://chainlink-winter2021.vercel.app/ Overview With the global environment deteriorating everyday, it has become more and more important to conserve our natural resources and reduce pollution to the environment through the saving of energy. To promote and motivate the general public to conserve energy we use blockchain to gamify and provide transparency in a reward based IoT platform. This platform leverages government energy data via Chainlink to optimize energy savings. Solution In EnergyLink, this smart contract is deployed by a power company or government body for its customers, for example this could be the Los Angeles Department of Water and Power. Customers that have a smart thermostat (i.e. Google Nest) can join this contract, giving control of their thermostat, and transparently earn rewards. The overall flow is the following: Power company or department of energy deploys and funds EnergyLink contract Customer joins smart contract and provides their Google Nest information via Oauth and their location region Firebase database stores Nest thermostat authentication information Smart contract is periodically called by Chainlink Keeper Upon keeper call, contract queries US Department of Energy data through Chainlink Oracle to get current energy usage in the customer’s location region If energy usage is above a threshold, command is sent via custom Google Nest Chainlink EA to control user’s Nest to reduce thermostat settings User’s Nest is periodically checked via Google Nest Chainlink EA, if they are within temperature setting limits the user’s reward increases User can track their statistics / rewards and how their saving compare against others User can request payout after their reward passes a certain threshold What Inspired Us We wanted to build something that had an impact on the environment in combination with leveraging the transparency and decentralization of the blockchain to interact with real world physical devices and entities. How We Built Our Project [Smart Contracts] - Used Hardhat + Solidity to develop on Kovan through Alchemy [Front End] - React with Next JS and ethers, Vercel for deployment [Backend / Other] - Chainlink EA Adapter with Google Nest API for Google Nest device control and information, Chainlink Oracle with US Energy Information Administration (EIA) for energy grid data, Chainlink Keepers to periodically check Nest and energy grid data, Firebase to store Google Nest Credentials What we learned Overall increased knowledge of solidity programming / deployment and how to setup Chainlink EA Adapters to control real world physical devices and Chainlink Keepers to periodically call contracts Challenges We Faced Overall it was a great experience putting together this project. The biggest challenge was getting all of the connected blocks to interact with each other smoothly since there are so many different moving parts. <div