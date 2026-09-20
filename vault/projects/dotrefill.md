---
slug: "dotrefill"
url: "https://devpost.com/software/dotrefill"
title: "DotRefill"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 346
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/financial_record"
---

# DotRefill

> DotRefill as a mobile app lets you shop global gift cards, mobile top-ups, and digital services directly with your Polkadot wallet. Powered by Bitrefill’s global catalog and Nova Wallet integration.

[Devpost](https://devpost.com/software/dotrefill) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[financial_record]]

**stack** figma, flutter, polkadot, visual-studio, westend

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dotrefill

## Body

Search amongst vouchers Select amount See how much DOT it would cost Confirm transaction in Nova Wallet Get confirmation Inspiration We are convinced, that Polkadot's main issue currently is the low level of usability and spend-ability of your assets. What it does DotRefill is a front layer for the popular Bitrefill, which is an e-commerce platform that lets you use cryptocurrencies, like Bitcoin and Ethereum, to purchase gift cards, eSIMs, and mobile phone top-ups. How we built it We planed the most convenient workflow with considering the end goal: the usability of DOT for real-life scenarios, like spending for utilities. Like a World of Warcraft subscription :) The planned flow is: 1) User opens app → searches f.e "Netflix" 2) App queries Bitrefill catalog → shows Netflix gift card 3) User taps → chooses $25 card 4) App fetches price → displays equivalent DOT amount 5) App launches Nova Wallet with transaction details (amount, recipient address) 6) User approves payment → wallet sends DOT 7) App listens or polls Bitrefill for invoice confirmation. 8) App displays confirmation screen with order receipt. Challenges we ran into We were dedicated to use React Native+Expo, but when we discovered, that the Reown / WalletConnect support for Polkadot is non-existing for React Native. So we switched to Flutter. Accomplishments that we're proud of We were able to set up the flow including (6). And it works with proper stability. What we learned Most of all, we learned how to Flutter in a beginner level, was interesting. Also, we get familiar with Polkadot devnet (Westend) and how to set up a proper unsigned transaction - and how to ask a signature for it in NovaWallet. What's next for DotRefill Instead of sending the purchased vouchers to the user's email, display them directly in the app Implement other wallets possibly Spending custom amount: you want to buy fuel voucher for 100 USD, and the fuel voucher provider offers only 50, 20 and 10 USD vouchers - DotRefill calculates it for you as 1x 50, 2x 20 and 1x 10 USD vouchers <div