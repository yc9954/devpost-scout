---
slug: "chainpay-automatic-payroll"
url: "https://devpost.com/software/chainpay-automatic-payroll"
title: "ChainPay - Automatic Payroll"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 175
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# ChainPay - Automatic Payroll

> Decentralized payroll system using Solidity smart contracts and Chainlink Automation. Employers deposit funds, add employees, and salaries are paid automatically with zero manual intervention.

[Devpost](https://devpost.com/software/chainpay-automatic-payroll) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** alchemyapi, chainlink, etherscan, foundry, solidity, visual-studio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges that i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for chainpay - automatic payroll

## Body

Inspiration Traditional payroll systems are expensive, centralized, and require manual intervention. I saw an opportunity to leverage blockchain for an automated solution that eliminates intermediaries and guarantees on-time payments. What it does ChainPay is a decentralized payroll manager on Ethereum. Employers deposit funds, register employees with custom salaries and payment frequencies, and Chainlink Automation handles the rest, automatically processing payments when due with zero manual intervention. How I built it Smart Contracts: Solidity ^0.8.19 with OpenZeppelin security libraries Automation: Chainlink Keepers via checkUpkeep() and performUpkeep() Development: Foundry framework Deployment: Verified on Ethereum Sepolia testnet Challenges that I ran into Gas optimization for batch payment processing Chainlink Automation configuration with proper gas limits Accomplishments that I'm proud of Fully functional automated payroll system deployed on Sepolia Robust security using OpenZeppelin standards Scalable design handling hundreds of employees What I learned Chainlink Automation architecture and keeper networks Real-world blockchain application design for scalability What's next for ChainPay - Automatic Payroll Multi-token support (USDC, etc.) for price stability Employee self-service web portal Multi-chain deployment for lower costs <div