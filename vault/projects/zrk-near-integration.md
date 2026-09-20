---
slug: "zrk-near-integration"
url: "https://devpost.com/software/zrk-near-integration"
title: "NEAR integration - ZRK.UA"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 427
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# NEAR integration - ZRK.UA

> zrk.ua is one of most popular handmade platforms in Ukraine last years. We happy to introduce NEAR Blockchain payments integration in our portal!

[Devpost](https://devpost.com/software/zrk-near-integration) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** laravel, near, near-api-js, node.js, php, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for zrk near integration

## Body

Shop settings - add NEAR Wallet address Cart order - NEAR payment selected Cart order - make payment Orders list - order marked as "paid" Web2 integration - Visualisation Inspiration zrk.ua is one of most popular handmade platforms in Ukraine where anyone can create handmade store and sell unique handmade stuff. We develop this platform 7 years ago using Laravel and support it all this years. Main issue for us all this time was direct payments between craft-mans and customers - how user can pay directly to craft-man and avoid huge fees. What it does For this hackathon I added new payment option for our stores and solve our pain: now any craft-mans can set NEAR wallet address to enable direct crypto-currency payments. When someone create new order for this store and chose NEAR Wallet as payment option, we calculate payment amount and use NEAR blockchain for this payment. To control payments and update database I create separate open-source solution with smart-contract (used for payments and temporary data storage of new transactions) and server-side script that connect to this smart-contract and synchronise new orders list with server database. How we built it I updated zrk.ua platform: add new payments method, update cart and orders processing, add payment status in database and user interface. Main issue was - how to make sure that payment was success, user pay correct amount and update our database based on blockchain transaction. To solve this issues I created separate open-source project that process our payments and update database. I configure server-side script that connect to smart-contract and regularly check if we have new payments (used smart-contract storage). When new payment detected - server update database records and cleanup smart-contract storage. Now store owner (craft-man) can see that payment was made for new orders, can accept it and clarify details with customer. For testing use our demo website: demo.zrk.ua . "Try it out" links section include the link to store with enabled NEAR Wallet payment method. I provided login credentials in "Please explain why you chose the above track" section. All notifications on this website disabled to avoid sending spam to real users. Challenges we ran into How to synchronise blockchain payments with database. How to integrate blockchain payments in zrk.ua. How to make simple interface for our customers. Accomplishments that we're proud of Fast and simple solution. Ability to use open-source part for any web2 integration. Extend NEAR ecosystem and invite new users. What's next for ZRK NEAR integration Test and launch on mainnet. Add USDT and USDC tokens for payment. <div