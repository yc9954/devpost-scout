---
slug: "transatron"
url: "https://devpost.com/software/transatron"
title: "Transatron"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 425
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Transatron

> Tron transaction processor with cheaper fees and no TRX required, 1 step integration with any wallet.

[Devpost](https://devpost.com/software/transatron) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**substrate** [[financial_record]] [[web_dom]]

**stack** java, postgresql, spring, swing, tron, trongrid

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for transatron

## Body

Inspiration Tron is very popular blockchain for OTC market. Nowadays, first crypto token that user obtains out of cash is USDT in Tron. Newbies in Tron typically don't have TRX and have no idea where to find TRX for their transactions. They either call their more crypto-advanced friends and ask for some TRX, or have to register accounts on CEX and buy TRX there. What it does Transatron processes transaction without TRX and charges users in USDT. It is capable of processing individual transaction and batches of transactions scheduled for future (up to 48 hours). How we built it Initially, we wanted to build a telegram bot that users can claim some energy with, so that they can have their transactions processed without burning TRX. But after many attempts, we found that there are many bots on the market, and users still struggle to deal with them. So we build Transatron in a way that it can be integrated seamlessly in a wallet (by replacing tron node address) and cover users' transaction with resources the way that user even don't understand it's there. Challenges we ran into Tron energy model V2 is a big step forward, it took quite a while to understand how it works in details. It also took quite a while to make a viable business model, so that energy delegation becomes profitable comparing to more simplified (commodity style) Tron energy markets that already exist with variety of suppliers. Speaking about technical challenges, there was a security of the energy provider wallets, we end up using Active Permission and separate keys to let Transatron Server operate securely with energy/bandwidth provider accounts. When building a batch mode, it was challenging to understand the limits of how far into the future can we delay transaction execution. Practically we found that 48 hours is safe with Tron consensus engine. Accomplishments that we're proud of From the business prospective, we are proud that we've end up with a profitable and viable business model for Transatron. From the technical side, we are proud of a Transatron Proxy node interface, that allows for simplistic integration of the service with existing wallets and solution providers. Simply changing node API URL does the job. What we learned First of all, that most obvious idea doesn't seems to be the most viable. You have to seek for users and do a basic customer development at least. What's next for Transatron Transatron needs a better infrastructure, code review and go to market strategy. Few experiments are in progress bringing optimistic results. <div