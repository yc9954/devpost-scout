---
slug: "payment-vouchers"
url: "https://devpost.com/software/payment-vouchers"
title: "Payment Vouchers"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 209
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/web_dom"
---

# Payment Vouchers

> Allow user to lock some amount of NEAR in smart contract as Payment Voucher and use it later to make a payment. Another user (who scan QR-code or have secret URL) can get payment from this Voucher.

[Devpost](https://devpost.com/software/payment-vouchers) · hackathon [[Hack to the Future 4]]

## Facets

**domain** [[finance_payments]]
**substrate** [[web_dom]]

**stack** near, rust, vuejs

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for payment vouchers

## Body

Inspiration I couldn't find blockchain solution for delayed payments on NEAR blockchain and decided to develop it. What it does You can create Payment Voucher with locked tokens on our smart-contract. Show this voucher (QR-code or send secret URL) to another user and he will be able to get this tokens. To start using: Login using your NEAR wallet. Generate payment Vouchers (lock your funds). Send link or show QR-code to make a payment. Challenges we ran into Main challenge: How to store Vouchers (private info that allow to take payment from voucher) in blockchain that is public. Solution: Public key for each voucher stored in blockchain and private key exists in browser local storage. To generate secret url and make transfer funds we using both keys. Accomplishments that we're proud of Owner can set expiration date for each voucher (optional). Ability to get just part of locked amount. Rest funds will be returned to the Voucher owner. Low Gas and no commission for payments. What we learned How to use NEAR Blockchain. How to work with private/public keys. How to transfer funds. How to write tests. What's next for Payment Vouchers Ability to generate multiple vouchers in few clicks. Print page for selected vouchers. Launch on MainNet. <div