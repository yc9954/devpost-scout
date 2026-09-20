---
slug: "linkwallet-jo1p8n"
url: "https://devpost.com/software/linkwallet-jo1p8n"
title: "LinkWallet"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 363
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/financial_record"
---

# LinkWallet

> Account Abstraction wallet with off-chain gas fee subscription by Chainlink & Stripe paymaster.

[Devpost](https://devpost.com/software/linkwallet-jo1p8n) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[financial_record]]

**stack** accountabstraction, chainlink, polygon, quicknode, stripe

## How they structured the write-up

- linkwallet
- user benefits
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linkwallet

## Body

top how-it-works stripe LinkWallet Account Abstraction Wallet with Off-chain Gas Fee Subscription by Chainlink User Benefits Users can pay the gas fee with an off-chain subscription It enables users to skip "bridge token from the other chain" or "send token from the central exchange," which is the first obstacle for users to start using a blockchain-based app It brings excellent onboarding, especially for the new user What it does User can pay the gas fee by credit card with a stripe subscription After the user subscription, a webhook is called from Stripe, and the webhook sends a tx to request Chainlink Chainlink gets the payment status from the off-chain stripe API, then stores it in the on-chain paymaster contract Paymaster contract verifies the payment status with the user address, then pays the gas fee for paid users when sending tx. How we built it Chainlink and Account Abstraction is the primary implementation of the hackathon Payment status is integrated securely with Chainlink Verification is implemented in an Account Abstraction way which brings better flexibility than the average meta transaction Chainlink Integration This is to integrate stripe payment status into the Account Abstraction Paymaster The Main reference of the integration (Contract)[ https://github.com/taijusanagi/chainlink-aa-paymaster-wallet/blob/main/packages/contracts/contracts/ChainlinkStripePaymaster.sol#L68 ] (Backend)[ https://github.com/taijusanagi/chainlink-aa-paymaster-wallet/blob/main/packages/app/src/pages/api/stripe/checkout-callback-to-request-chainlink.ts#L13 ] Polygon Integration ChainlinkStripePaymaster https://mumbai.polygonscan.com/address/0xbb0447c7194fb0e99213ad140d0dff4c82fbb9ca#code EntryPoint https://mumbai.polygonscan.com/address/0xf317c52db727f9d8a3ac04304cb34a297bffef9a#code WalletFactory https://mumbai.polygonscan.com/address/0x5352d8704b9a251d46aa4674e3215fc6d7baa80a#code Quicknode Using Quicknode RPC for better performance Used in deploy script and Account Abstraction Bundler https://github.com/taijusanagi/chainlink-aa-paymaster-wallet/blob/main/package.json#L22 https://github.com/taijusanagi/chainlink-aa-paymaster-wallet/blob/main/packages/contracts/network.json#L9 Challenges we ran into This is my first to build an Account Abstraction paymaster, and significantly less documentation is available for this implementation. I had to debug so many times to complete the whole process. Accomplishments that we're proud of Now I can use paymaster for any Account Abstraction tx. This is good progress. I believe this is the first implementation of integrating Account Abstraction and Chainlink. There should be excellent business opportunities too. Automated chainlink integration, and it works very well What we learned How to use Chainlink and Account Abstraction What's next for LinkWallet Run own bunder This off-chain payment method can be used in cross-chain payment too. This enables user not to need to bridge and swap to use the dApp. Users can pay the fee in any chain. <div