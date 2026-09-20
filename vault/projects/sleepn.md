---
slug: "sleepn"
url: "https://devpost.com/software/sleepn"
title: "Sleepn"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 394
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/mental_health"
  - "substrate/sensor_telemetry"
---

# Sleepn

> Sleepn is a web3 game that pays you to sleep better.

[Devpost](https://devpost.com/software/sleepn) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[mental_health]]
**substrate** [[sensor_telemetry]]

**stack** blender, chainlink, figma, fitbit, hardhat, polygon, react, solidity, superfluid

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sleepn

## Body

How Sleepn Works Bedroom NFTs Inspiration Would you like to be smarter? Happier? More productive? Healthier? Of course you do. You can improve all these things by sleeping better. However, our modern society sucks at sleeping and it's been getting worse year after year. What it does Sleepn is a web3 game that rewards you $SLEEP every minute you sleep. You earn more for the time you are in REM & deep sleep cycles. The goal is to improve your sleep and mental health. We do this by incentivizing better presleep decisions like being more active during the day, having a consistent sleep schedule, shutting down social media before bed, meditating during the day, etc. All of these decisions lead to improved sleep. To play the game, you must have a wearable that tracks your sleep quality. The first one we integrate with is Fitbit. Oura Ring & Apple Watch are next. Then you must mint a Bedroom NFT, which is your game piece. Each bedroom can be upgraded with additional NFTs such as better pillows, sheets, mattresses, etc. These NFTs have various traits that allow you to earn more $SLEEP. How we built it All of the Sleepn smart contracts are deployed to Polygon. We use Superfluid to stream $SLEEP token to the user per minute of sleep. Gnosis Safe is used as Sleepn's treasury. The game itself is a mobile app built with React Native. We're using WalletConnect for the web3 wallet option. We started a $SLEEP liquidity pool using Uniswap's V3 contracts. We're using FitBit's API to get sleep data from a user's wearable. Challenges we ran into The biggest challenge was the game theory behind it all. How do you make a game fun & rewarding while also having the desired impact? This will be an experiment in progress. Accomplishments that we're proud of We created some cool 3D isometric bedroom NFTs that are really neat. They can be personalized with all sorts of upgrades. And to our knowledge, we are the first project to ever stream tokens to someone based on the minutes slept in each sleep cycle. That's pretty freaking awesome. What we learned Don't drag around in hackathons. Get to work ASAP and ship a product. What's next for Sleepn This project will continue. We plan on turning this into a gamified health & wellness app. <div