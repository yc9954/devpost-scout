---
slug: "x-defi"
url: "https://devpost.com/software/x-defi"
title: "IPPS"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 786
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
---

# IPPS

> A blockchain-based payment gateway system to enable centralized financial institutions to participate in DeFi movement by tokenizing fiat assets.

[Devpost](https://devpost.com/software/x-defi) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]] [[immigration_refugee]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** alchemyapi, chai, chainlink, hardhat, mocha, nextjs, polygon, solidity, typescript

## How they structured the write-up

- inspiration/context
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for ipps

## Body

IPPS (Inter Planetary Payment System) Bank View - Staker Info IPPS (Inter Planetary Payment System) Bank - Apply For Enlistment IPPS (Inter Planetary Payment System) Staker View - All Banks IPPS (Inter Planetary Payment System) Staker View - Individual Bank IPPS (Inter Planetary Payment System) End User Mobile App IPPS (Inter Planetary Payment System) Staker View - My Earnings IPPS (Inter Planetary Payment System) Technical Architecture of Smart Contract Inspiration/Context From the early 2000’s, payment gateways such as Visa and Mastercard have dominated cashless money transfers through their centralized monopolistic network - which in many ways have given them a price-setting capability. IPPS aims to provide a breakthrough in this market by leveraging blockchain network as ground truth and thus remove friction and intermediaries within the fiat money transfer systems. What it does IPPS (Inter Planetary Payment System) is a blockchain-based payment gateway system to enable centralized banks or any financial institutions to participate in DeFi movement by tokenizing fiat assets. Core System Components: Banks: Banks provide us with users fiat balance in their respective accounts. These assets are then tokenized by minting XX tokens in 1:1 ratio according to their fiat balance. Stakers: Stakers stake in favor of these banks, validating and lowering risks for users in case banks opt-out from providing fiat balance to our users against XX token. They are rewarded with a portion of transaction fees and governance tokens Users: The users of our platform who can make payments, transfer balance in XX tokens (representing their fiat balance) - Should we charge users/ banks for using our service? Merchants: The business organizations registered within a bank - who pays (subscription fee/ percentage amount - per transaction?) a certain amount when receiving XX tokens from users as payments. (Should we/banks charge them cash-out fees when redeeming XX tokens to fiat?) How we built it Technologies Languages: Solidity, TypeScript Libraries: OpenZeppelin, Typechain, Wagmi React Hooks Frameworks/Development Environments: Hardhat, Mocha, Chai, NextJS Oracle: Chainlink Storage: Web3.Storage Infra: Quicknode, Alchemy Chain: Polygon Mumbai Others: NFC Card Technical Architecture View on Figma UI/UX Design Resources (Figma) UI Bank View UI Stacker View UI Mobile View User Journey/Process Flows Bank & User Onboarding A bank requests to join X platform specifying a limit (which can’t be exceeded for this bank unless changed) Stakers verify and stakes in stablecoin Banks get limits for the amount which is staked for that particular bank Banks provide us with user wallet addresses and initial fiat balance (amount which they internally decide to allow for each user - may vary from user to user based on their use or balance) X mints XX tokens to users wallet in 1:1 ratio to its balance (provided by the bank). Additionally, the wallets are whitelisted in the protocol so that the tokens are non-transferrable to any other address Merchant Onboarding Merchant wallet addresses are provided by the banks Whenever a token is transferred from other wallets (from users), a small fee is charged - which could be the main source of revenue of IPPS Merchants can redeem these tokens from banks Staker Onboarding Stakers view limit requests by the banks in X platform Additional details of banks are uploaded in Filecoin Stakers stake an amount in favor of the bank to provide them limit for that particular amount Stakers receive transaction fee shares proportional to their staking amount (Whenever users make payments using XX tokens) Additional Note on Staking A Bank can stake in favor of itself too - As onboarding stakers is not our goal. The goal is to minimize the risk for users in case the banks decline to provide fiats against XX tokens. In such circumstances the DAO can reimburse platform users with staked assets (most likely stablecoins). Challenges we ran into Faced challenges while setting up Quicknode on custom contracts, although we used it to set up Chainlink clients. Accomplishments that we're proud of The overall product thinking, UI and UX deep dive, and in-depth technical architectures based on ecosystem. Additionally, we also implemented quite a few test cases & wrote tests with mock contracts & different edge case scenarios. What's next for IPPS We have quite a few things on our roadmap, including: DAO Contract development and deployment: Stakers get privileges as DAO members with the governance token distributed respectively to their staking amount. They can perform certain actions, protocol management, etc. with these governance tokens, received along with transaction fee shares Chainlink ZK Proof: Leveraging Chainlink ZK Proof for interbank comms, like age verification for user eligibility Chainlink VRF: Implementing Chainlink VRF if we want to pick random stakers via reward/incentivizing programs Chainlink Automation: Integrating Chainlink Automation to execute smart contracts via cron job in terms of periodic transactions. <div