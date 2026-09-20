---
slug: "polkadot-point-of-sale-terminal"
url: "https://devpost.com/software/polkadot-point-of-sale-terminal"
title: "Polkadot Point of Sale Terminal"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 391
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/general_public"
  - "user/government_staff"
  - "substrate/financial_record"
---

# Polkadot Point of Sale Terminal

> Accept Polkadot and Nodle payments at your retail location, print receipts, reports

[Devpost](https://devpost.com/software/polkadot-point-of-sale-terminal) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[transportation]]
**user** [[general_public]] [[government_staff]]
**substrate** [[financial_record]]

**stack** android, java, subquery

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for polkadot point of sale terminal

## Body

User interface for entering amount and confirming transaction Currently working on supporting Sunmi V2 and Wiseasy Point of Sale Menus for configuring the Point of Sale Application Inspiration Retailer looking for ways to drive traffic to their physical stores and increase sales can accept Nodle Cash as payment method, Nodle Point of Sale (POS) app enables businesses to accept Nodle Cash payments at their locations using a mobile phones and android terminals, all they need to do is advertise on social media and using store signs that they accept Nodle Cash as payment, this will drive traffic to the stores and increase sales. Nodle Cash is mined by the consumers using their mobile phones and is easly available. What it does Retailers define a Nodle/Fiat conversion rate and sets a Nodle Wallet using Nodle Cash App or Nova wallet. During a transaction the clerk enters the amount to pay and the application calculates the amount in Nodles and displays a QRcode. The customers proceed to pay using their nodle mobile wallet, and the application detects when the payment is received and prints receipts and reports, it can be used on on mobile phones or Point of Sale terminals. How we built it Native Android application that uses Subquery Network to access the Nodle blockchain, Subquery.network provides the API to the balance indexer and transaction history for the specified retailer's wallet. During a transaction the Nodle POS creates a websocket to onfinality.io and registers state_subscribeStorage to detect balance updates. The retailer uses a non-custodial wallet application (Nodle Cash Wallet or Nova Wallet) to create their Nodle public keys, and registers the public keys at the Nodle POS application. Since Nodle is not currently trading, the retailer sets a fixed conversion rate in the application which is used to calculate the amount to pay. Future versions will use the exchange rate for Nodle. Challenges we ran into Learning about Subquery and completing the application in time for the competition. Accomplishments that we're proud of Learning about Subquery.network and creating a balance and transaction history indexer. What we learned The speed and efficiency of Subquery Network to fetch useful data from Polkadot blockchains What's next for Polkadot Point of Sale Terminal Extend to other point of sale terminals and increase language support and features. Incorporate other Substrate-based chains and Develop an IOS version. <div