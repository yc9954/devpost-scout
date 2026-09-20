---
slug: "da-derpy-derby"
url: "https://devpost.com/software/da-derpy-derby"
title: "Da Derpy Derby"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 594
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# Da Derpy Derby

> Kart-themed arcade game controlled by scripts placed on IPFS, CIDs stored on-chain, and executed in an external adapter publishing messages on an MQTT broker.

[Devpost](https://devpost.com/software/da-derpy-derby) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** brownie, cpp, filecoin, ipfs, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for da derpy derby

## Body

Kart GIF Kart Scoring GIF DaDerpyDerby Flow chard Inspiration My wife and I have an empty bedroom, and she let me convert it into a workshop. A dream of mine has been to house some Chainlink nodes in its unused closet, and make a few extra bucks. This made me think, could I also utilize the room itself? Thus, the idea of hosting remote arcades in families' unused spare-bedrooms was born. Players from around the world could stake funds and compete against one another for the spoils. I see a future where Chainlink oracles are a conduit, not just for pulling, but for pushing data to control complex behaviors within an IoT network. My goal with this hackathon has been to experiment with the tech required for implementing a secure, autonomous, remote, physical arcade game. What it does This project showcases a potential backend for a remote arcade. It takes in submissions, queues them up, executes them, grabs their score, and, lastly, checks if this score is the new high score. Here's a more delineated walkthrough: When a user submits an IPFS content id (CID) number to this smart contract, it places it in a queue to be processed this CID should point to a valid script JSON file. ( example ) A Keepers Upkeep is registered to monitor the contract for submissions The Upkeep also manages other states of the queue When the queue is not empty, these CIDs are sent to an external adapter for processing via sendChainlinkRequestTo() The external adapter connects to, and publishes data on, a secure, pre-defined MQTT Broker A free HiveMQ private broker was used for this project After the ChainlinkFulfillment returns, another Chainlink request is sent to collect the submission's score The score pulled is then checked against the high score The process repeats with the next submission in the queue After 24-hours, the high score leader would be awarded that day's pool of cash, and then the score is reset How we built it Smart Contract: Written in solidity, Brownie was used for compiling, deployment, and scripting External Adapter: Written in python, Pipenv and Pytest was used for management and testing IoT devices: Written in C++, PlatformIO was used for dependency management, compiling, testing, deployment, and serial monitoring Challenges we ran into My wife and I had a son (Nick) born on 4/21/22, the day before the hackathon started. I did not have time to build a GUI for this project, and considered not submitting. However, I was able to finish a bit more than I expected, and decided I wanted to share where I'm at with the project. Also, my Linux machine running my Chainlink node kept crashing. Still trying to figure that one out. Accomplishments that we're proud of The Keepers Upkeep successfully monitoring the smart contract's states for execution was something I did not think I would even start, much less finish, much less actually work. Storing data on IPFS and pulling it down for execution opens endless possibilitiesx for this project. What we learned IPFS storage on web3.storage, and utilizing CIDs to retrieve data Keepers-compatibility Solidity iterable-mappings (used to create the queue) and events What's next for Da Derpy Derby A GUI is needed for easily creating scripts, pushing them to IPFS, and submitting them to the contract for processing. A way to watch a stream of the field executing submissions would also be nice Collecting, holding, and awarding users' funds for playing/winning Utilizing a DAO to ensure fair play has occurred and enable control to adjust something that was unfair <div