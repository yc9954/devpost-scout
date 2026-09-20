---
slug: "x-dropbot"
url: "https://devpost.com/software/x-dropbot"
title: "X DropBot"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 335
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# X DropBot

> Spice up your Twitter tips with Chain Signatures on NEAR—secure, seamless, and decentralized. A new era of crypto tipping! 🌶️⚡

[Devpost](https://devpost.com/software/x-dropbot) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** chain-signatures, near, next, rust, web3auth

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for x dropbot

## Body

X DropBot Inspiration Tipping on Twitter is a great way to show appreciation, but existing solutions are limited to traditional payment systems. We wanted to create a decentralized way for users to send Bitcoin tips seamlessly through Twitter using on-chain signatures. What it does X DropBot allows users to send Bitcoin tips to other Twitter users via a simple tweet. By leveraging chain signatures, users can securely authorize transactions without leaving Twitter. The bot processes the request, verifies the signature, and executes the transfer on-chain. How we built it Integrated Twitter’s API to detect tip commands and user mentions. Used a NEAR-based wallet system and Web3Auth for chain signatures and authentication. Built a backend service that listens for tip requests, verifies signatures, and processes Bitcoin transactions. Implemented a linkdrop mechanism to allow recipients to claim their Bitcoin even if they don’t have a wallet set up yet. Deployed on Vercel with a serverless architecture to ensure scalability and efficiency. Challenges we ran into Ensuring secure and gas-efficient on-chain transactions. Managing Twitter API rate limits while maintaining real-time responses. Implementing a seamless user experience for both senders and recipients, especially those unfamiliar with blockchain. Handling cross-chain transactions between NEAR and Bitcoin. Preventing the bot from sending links to users while maintaining a smooth claiming process. Accomplishments that we're proud of Successfully implemented a working prototype of the bot that executes Bitcoin tips via chain signatures. Developed a frictionless onboarding process for non-crypto users. Optimized transaction verification and processing to reduce delays. What we learned Advanced handling of Twitter’s API for real-time interactions. Efficient ways to bridge NEAR-based authentication with Bitcoin transactions. The importance of UX in making blockchain tools accessible to mainstream users. How to implement and utilize chain signatures on NEAR Protocol for secure, verifiable, and decentralized transaction authorization. What's next for X DropBot Expanding support for additional cryptocurrencies like Ethereum and Dogecoin. Introducing a reward mechanism to incentivize usage. Implementing analytics to track tipping trends. Enhancing security features and reducing transaction costs further. <div