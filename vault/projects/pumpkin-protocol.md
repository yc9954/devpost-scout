---
slug: "pumpkin-protocol"
url: "https://devpost.com/software/pumpkin-protocol"
title: "Pumpkin Index"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 321
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/web_dom"
---

# Pumpkin Index

> Create custom index tokens, set your strategy and rebalance the underlying assets to achieve optimal returns. Follow top creators or build your own. Join us today!

[Devpost](https://devpost.com/software/pumpkin-protocol) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** hardhat, javascript, nextjs, remix, solidity

## How they structured the write-up

- what is an index token?
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pumpkin index

## Body

Screenshot of the create token page. Users can set the name of the index token, the symbol, and the percentages of each underlying asset Testing the 1% per year fee that a creator can claim on hardhat using a fork of the Fantom Mainnet. Issuing new tokens, underlying assets can be seen being transferred to the index contract Testing the rebalance function. Underlying tokens are swapped on Spookyswap for a specified amount, and the ratio of each asset changes. Early sketch of the Pumpkin Protocol. 🎃Pumpkin Index 🎃 What is an index token? ❓ An index token is like a basket that holds many different types of cryptocurrencies at once, allowing investors to invest in several cryptocurrencies through one token. Inspiration 👻 Fantom network currently does not have any Index Tokens. 🧟 We took inspiration from TokenSets / Set Protocol and recreated it without any fees. What it does 🎃 Lets users create & manage their own index tokens 🧙 Redeem index tokens for underlying assets 🧛‍♂️ Creators can collect a custom streaming fee from 0 to 1% per year 🍬 Others can buy these tokens on a decentralized exchange 🔪 Adjust/rebalance each portion of underlying tokens in an index token How we built it 🕯️ Wrote the solidity smart contract from the ground up ✨ Integrated SpookySwap for token rebalancing 🧪 Tested by forking Fantom Mainnet using Hardhat Challenges we ran into 🧮 Algorithms to transfer a streaming fee from all token holders to the creator 📐 Mathematics for how much to calculate % of underlying tokens Accomplishments that we're proud of 🔮 Calculated necessary values to execute trades ⚰️ Successfully Rebasing tokens 👽 Integrating the Smart Contracts & Website together (a lot of trial and error) What we learned 🧠 Learning more about solidity math 🌃 Learning about the Fantom Ecosystem What's next for Pumpkin Index 🍂Gas optimization 🐺 Security Improvements 🧑 UX Improvements Try it yourself! Walkthrough <div