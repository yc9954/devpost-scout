---
slug: "xrpower"
url: "https://devpost.com/software/xrpower"
title: "XRPower"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 550
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# XRPower

> Stake your XRP. Predict outcomes. Win the pot. XRPower turns your opinions into on-chain rewards through decentralized prediction markets on the XRP Ledger.

[Devpost](https://devpost.com/software/xrpower) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** node.js, react, ripple, web3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for xrpower

## Body

Inspiration I’ve always been interested in how communities form collective predictions around events like elections, crypto prices, and sports, and how those opinions could be turned into a rewards system. Most prediction markets today either rely on centralized systems with no transparency or complex, gas-heavy smart contract platforms that are hard for new users to interact with. I wanted to explore whether I could build a lightweight, fast, and easy-to-use prediction platform using the XRP Ledger. XRPL’s fast transaction speeds, low fees, and built-in tools for escrow and payments made it a great match for this type of application. I imagined a world where anyone could say "I think this will happen", back it with XRP, and be rewarded for being right, without needing a centralized betting app or login form. What it does XRPower is a prediction-based rewards platform built on the XRP Ledger. It lets users vote on the outcome of real-world events by sending a small amount of XRP to one of two wallet addresses, one representing “Yes” and one representing “No.” Each vote is an actual payment transaction on the XRP Ledger. The system tracks the total XRP sent to each outcome in real time. How I built it I used React and TailwindCSS to build the frontend, and Node.js with Express for the backend. I used the xrpl.js SDK to generate XRP testnet wallets, monitor transactions, and send reward payouts. Challenges I ran into One of the main challenges was transaction detection. The XRP Ledger confirms transactions quickly, but building a real-time listener that filters the right transactions from the stream and handles edge cases like double voting or late submissions required careful validation. Another challenge was payout logic, making sure rewards were distributed fairly based on who voted and preventing any double payouts. Since I was using testnet wallets and a backend-based admin trigger, I also had to ensure that key management and transaction signing were handled safely and efficiently. Time management was another big factor. Accomplishments that I am proud of I’m proud that I was able to design and build a fully functioning prediction and reward platform in such a short amount of time. XRPower supports real-time vote tracking, uses actual XRP testnet transactions, and includes a working payout system that sends testnet XRP to the correct voters. The flow is smooth, intuitive, and easy for new users to interact with. It also opens up possibilities for new types of experiments and lightweight applications in event prediction and staking models, all built without needing complex smart contracts or third-party infrastructure. What I learned I learned a lot about the XRPL developer ecosystem, including how to work with xrpl.js, how XRP handles transactions, and how to manage payment-based workflows. I also gained hands-on experience with building real-time systems that respond to on-chain activity. I also deepened my understanding of how to scope and ship a working MVP under extreme time pressure as a solo builder. What's next for XRPower If the project gains traction, I’d like to deploy a version on the XRP mainnet with more robust transaction management and lower risk thresholds for new users. XRPower is still in its early stages, but I believe it has potential to become a fun and rewarding tool for event forecasting and community-powered insight. <div