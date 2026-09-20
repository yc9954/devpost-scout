---
slug: "yinbox"
url: "https://devpost.com/software/yinbox"
title: "Yinbox"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 427
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
---

# Yinbox

> Yinbox is the first fully integrated messenger app with end-to-end encryption and spam prevention on NEAR protocol.

[Devpost](https://devpost.com/software/yinbox) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]]
**domain** [[finance_payments]]
  <sub>weak: video_visual</sub>

**stack** assemblyscript, mongodb, near, nextjs, react, typescript, vercel

## How they structured the write-up

- inspiration
- features
- technical process flow
- what's next for yinbox
- screenshots

## Body

Yinbox - Integrated Instant Messenger on NEAR Inspiration There is no easy way to reach someone you've come across on the blockchain unless you know them personally or their Discord handle. Whether it's coming across a wallet address on the blockchain, or the owner of an NFT you find on a marketplace that you'd like to talk to. We wanted to bridge that gap, and give people the ability to make connections with anyone on the blockchain. Secured. Integrated. Spam free. Yinbox is the first fully integrated messenger app with end-to-end encryption and spam prevention on NEAR protocol. Start a conversation with anyone on NEAR with nothing but their wallet account name, link any NFTs on the network, engage in a rich and intuitive messaging experience. Just connect your wallet and you're good to go, no signups required. Features End-to-End Encryption Your messages are secured so only you and the person you're communicating with can read them. No one else in between can see your conversation, not even us at Yinbox. Fee Based Spam Prevention To prevent spams, Yinbox charges a one time fee of 0.5 NEAR when beginning a new conversation with anyone. On-Chain and Off-Chain Symbiosis Security, Speed and Convenience NFT Integration Link any NFTs on NEAR protocol via special chat commands. More exciting features coming soon Send and receive payments, see real-time asset prices, trade NFTs - all within the conversation. Technical Process Flow Wallet Sign-In Users first connect their wallet using a wallet provider like My NEAR Wallet, then signs a message to Yinbox Authentication API, which verifies the authenticity and returns a generated JWT token for subsequent Yinbox API calls. End-To-End Encryption When starting a conversation with anyone, a session key is generated. This session key is unique for each conversation between two people, and is used to encrypt and decrypt messages on the browser. Fee Based Spam Protection For new conversation, Yinbox Smart Contract receives an unlock fee and stores the conversation unlock record on the blockchain. The unlock fee is configurable to maintain a balance between spam prevention and usage feasibility. Message Transmission All messages are encrypted on users browser using the conversation session key before they are sent across the network. They remain encrypted even on Yinbox and is only decrypted on the recipient browser. What's next for Yinbox Exciting chat features: Send and receive payments View real-time asset price Trade NFTs Group messaging Roadmap: Q4 2022: Planning and prototyping Alpha build on NEAR Testnet Q1 2023: Technical foundation and production readiness Soft launch on NEAR Mainnet Screenshots <div