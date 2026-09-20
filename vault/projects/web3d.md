---
slug: "web3d"
url: "https://devpost.com/software/web3d"
title: "Web3D"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 233
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "substrate/geospatial"
---

# Web3D

> Let's build a decentralized 3D Google Maps thanks to zero-knowledge proof!

[Devpost](https://devpost.com/software/web3d) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[structural_withholding]]
**substrate** [[geospatial]]

**stack** alchemyapi, hardhat, metamask, polygon, privy, solidity, three.js, zokrates

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for web3d

## Body

Inspiration One of our team members was working on a mapping application when they discovered how bad the 3D mapping services were. The data was not detailed enough to make an immersive experience and most places did not appear in 3D on Google Maps or Open Street Map. What it does Our service allows network participants to add scans of the physical world to build a collaborative 3D map. A native token aligns the interest of the network participants and the map-based applications that will consume the data. For this hackathon, we focused on building a zero-knowledge proof system to verify that different layers of data are corresponding with each other without putting all of them on-chain. How we built it Privy for access controlled data storage Open street map for low-resolution data (building cuboid) three.js for decoding data Zokrates for zk proofs Polygon for verifier contracts Alchemy RPC Challenges we ran into Not enough time to wire everything up after getting individual components running Decoding/Manipulating 3D data with three.js was harder than expected Proof verifying with local Zokrates library but not on-chain What we learned First time working with zkProofs, super cool stuff First time working with 3D data, super hard First time working with Privy, great access controlled data storage What's next for Web3D The project will continue to be developed under another name. Join the waiting list here: https://www.theextraapp.com/ <div