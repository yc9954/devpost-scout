---
slug: "warp-yield"
url: "https://devpost.com/software/warp-yield"
title: "WARP YIELD"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 253
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# WARP YIELD

> A protocol to allow users to capture the highest yields on AAVE between blockchains

[Devpost](https://devpost.com/software/warp-yield) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets


**stack** aave, brownie, ccip, chainlink, javascript, next, python, solidity, uniswapv3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i proud of
- what l earned
- what's next for warp yield

## Body

Inspiration ChainLink now is offering a solution to move assets and messages between chains (CCIP). That could provide a solution for thousands of users to secure the highest returns from AAVE. What it does Concentrate the capital of all users in a vault that moves between blockchains to receive the highest interest rates for their USDC, and saving thousands of users gas. How I built it Two main contracts plus two additional auxiliary contracts written in Solidity. The entire deployment process has been carried out using Brownie Python. Challenges I ran into For me, the biggest challenge was how to manage when a CCIP message arrives on a blockchain and has to send another CCIP message to a different blockchain automatically. This meant that the contract receiving the first message had to be able, on its own, to purchase the necessary fees on Uniswap to send the message to the next blockchain. Accomplishments that I proud of This protocol will be able to save users thousands in gas fees, and it also saves you from having to constantly monitor AAVE yields to move your capital from one blockchain to another. The protocol does it for you. What l earned I have learned a lot, especially about how services with ChainLink, Uniswap V3, and AAVE work in depth. What's next for WARP YIELD The next planned feature for Warp Yield is to allow users to deposit their aWRP tokens, which they receive after making a deposit, as collateral to borrow against other assets. <div