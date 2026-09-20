---
slug: "kharonpay-mini"
url: "https://devpost.com/software/kharonpay-mini"
title: "KharonPay mini"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 319
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# KharonPay mini

> Next gen offramp system via whatsapp chat

[Devpost](https://devpost.com/software/kharonpay-mini) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**domain** [[education]] [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[web_dom]]

**stack** actix, api, cairo, postgresql, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kharonpay mini

## Body

Kharon pay mini banner kharon pay mini logo Inspiration The literacy rate of many Africans is a big contributor to this. Many can read, yes, but most have this view that web3 and blockchain products are for geeks and computer guys. They are not super enthusiastic about trying out or learning how to use web3 products; and this is large number of people. Now we created Kharon pay mini to meet these people where they are, they can send crypto to their bank via WhatsApp in meagre 22 to 60 seconds. All it takes is just 4 - 5 short messages sent to the bot. What it does Sends crypto to bank account in seconds with minimal interactions and no wallet signing. How we built it We got WhatsApp API and used webhooks for back and forth messaging, then API calls to aggregator and servers to transaction processing. Indexer catches the event and triggers API on aggregators which triggers disbursement and webhooks return transaction responses. Challenges we ran into Setting up WhatsApp API on Meta was terrible, and we ended up using Twilio which was easier. Accomplishments that we're proud of To be able to leverage AA on Starknet via Cartridge controller to achieve offramp on Whatsapp is a feat we are proud of. What we learned WhatsApp is more programmable than we think, and since web3 needs adoption (talk about onboarding the billions), bringing this service to apps billions of people use daily is a great strategy to take Web3 to the masses. What's next for KharonPay mini Kharon pay mini already have web version, kharon pay, which is also at MVP. Once we secure liquidity to facilitate payments/disbursement we can roll out beta in a few days. We are also integrating paymaster soon, with Kharon pay merchant service where users can scan QR Code or get payment url from merchants and then directly send them payments. <div