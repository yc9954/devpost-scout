---
slug: "expir3"
url: "https://devpost.com/software/expir3"
title: "Expir3"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 320
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Expir3

> Create on chain will or beneficiary. Schedule an automatic payout to accounts of your choice as your will or as a fall back.

[Devpost](https://devpost.com/software/expir3) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**substrate** [[financial_record]]
  <sub>weak: video_visual</sub>

**stack** chainlink, chainlinkautomation, hardhat, javascript, nextjs, polygon, quicknode, rainbowkit, solidity, tailwind, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for expir3

## Body

Dashboard Screenshot Expir3 Logo NFT Received example Inspiration Many users lose funds because they lose their keys, wallets or pass away with no way to recover funds What it does Expir3 Dapp lets you setup a deadman's lock to set beneficiaries to your assets. If you don't check in Chainlink Automation will execute the transaction sending the assets to the set wallets How we built it Technologies This project is built with the following open source libraries, frameworks and languages. User choice of framework used, available in plain js or typescript. Tech Description ------ ------ React Frontend Environment ------ Next JS React Framework ------ ------ CSS Framework ------ Tailwind A utility-first CSS framework ------ ------ Ethereum Development Environment ------ Hardhat Ethereum development environment for professionals ------ ------ Included Libraries ------ WAGMI A set of React Hooks for Web3 RainbowKit RainbowKit is a React library that makes it easy to add wallet connection to your dapp. ChainlinkAutomation Automatic Execution service for your smart contracts QuickNode The RPC provider used to deploy and connect our contract to the front end DAPP Challenges we ran into Getting the Chainlink automation to function. There was no logging system to see where things went wrong and spent much time trying to trace the issue ourselves. (Turn out to be an onlyOwner issue) General bugs and quality of life fixes are always a challenge Accomplishments that we're proud of We got it work! Figuring issues we were having with Chainlink Automation. Finding a creating way to handle scaling solution if the Dapp got popular. What we learned How to work with Chainlink Automation and it's limitations. Finding clever ways to handle the beneficiary system and token system What's next for Expir3 Drop down options for existing tokens in wallet (Pull wallet assets) Give a grace period before execution Send a reminder to email/calendar when check in date is coming up Looking deploying user's own contracts <div