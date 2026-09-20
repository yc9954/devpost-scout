---
slug: "defa-by-invoicemate"
url: "https://devpost.com/software/defa-by-invoicemate"
title: "DeFa by InvoiceMate"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 422
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# DeFa by InvoiceMate

> DeFa brings real-world, risk-assessed yield to StarkNet, a decentralized lending protocol where investors earn stable returns backed by real economic activity, not volatile crypto markets.

[Devpost](https://devpost.com/software/defa-by-invoicemate) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: revocation_withdrawal</sub>
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** and-user-information)-thirdweb-sdk-(smart-contract-interaction-and-wallet-integration)-blockchain-/-web3-layer-primary-network:-starknet-(phase-one)-smart-contracts:-vault-/-pool-contract:-manages-deposits, and-withdrawals-lp-token-contract:-issues-dlp-tokens-representing-investor-stakes-and-yields-stablecoin-contracts-(usdc-&-usdt):-enable-deposits, apy-logic, assets, blockchain, cairo, contract, contracts, css, defi, express.js, financing, invoice, kyi-scores

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for defa by invoicemate

## Body

Invest page Pools page Dashboard page Inspiration DeFi today is mostly speculative. It doesn’t create real, lasting value for the world. At the same time, small and medium-sized enterprises (SMEs) in emerging markets struggle to access affordable financing, with invoice factoring often slow, costly, or unavailable. We built DeFa by InvoiceMate to bridge these two worlds, connecting crypto liquidity with verified, revenue-generating real-world assets. The goal is to create a protocol that delivers stable, yield-backed returns for lenders while giving businesses faster, cheaper access to working capital. What it does DeFa by InvoiceMate is an AI-native DeFi lending protocol that unlocks real-world yield through tokenized invoice financing. For businesses: DeFa provides instant liquidity by factoring verified invoices on-chain. For lenders: It offers access to stable, real-world yield instead of volatile, speculative returns. The system uses on-chain smart contracts to manage pools and liquidity distribution, while real-world invoice data and KYI (Know Your Invoice) scores are stored securely off-chain. DeFa’s architecture ensures transparent, auditable, and data-driven financing flows between lenders and verified businesses. How we built it DeFa is built with a hybrid architecture: Data Layer (ICP): Stores borrower details, invoices, and KYI scores. DeFa Smart Contracts (Arbitrum, Stellar, and now Starknet): Manage liquidity pools and yield distribution for different lenders. Backend: Handles invoice verification, KYI scoring, and fiat-on/off-ramp processing. Frontend (React + Wallet Integration): Allows lenders to connect using Argent X or Braavos wallets and invest in invoice pools on Starknet Testnet. The Starknet integration focuses on smart contract deployment for yield pools, wallet integration, and test transactions to simulate real-world lending behavior. Challenges we ran into Adapting DeFa’s multi-chain design to Starknet’s Cairo-based architecture. Managing interoperability between off-chain data (invoices, KYI scores) and on-chain logic. Handling liquidity pool mechanics with time-locked investments for fair yield calculation. Ensuring a smooth wallet experience across Argent X and Braavos. Balancing privacy and transparency while keeping key repositories private for security reasons. Accomplishments that we're proud of Processed over $500M in tokenized invoices and $70M in real-world financing through our existing deployments. Onboarded 310K+ users in the testnet phase, validating strong community interest. Secured a $20M credit facility to support liquidity growth and real-world adoption. Successfully implemented the first version of DeFa’s Starknet integration. What we learned There’s strong demand for stable, real-world yield products in DeFi — users want simplicity, clarity, and trust. Clear communication around how risks and returns work is key to engagement. Hybrid systems that combine off-chain verification and on-chain transparency can scale effectively. What's next for DeFa by InvoiceMate <div