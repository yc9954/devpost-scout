---
slug: "fundmy-space"
url: "https://devpost.com/software/fundmy-space"
title: "FundMy.space"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 305
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
---

# FundMy.space

> Connecting everyone in the world with Blockchain by allowing Creators to be supported with Cryptocurrency and other assets on the Stellar Network

[Devpost](https://devpost.com/software/fundmy-space) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[finance_payments]]

**stack** bootstrap, django, python, stellar

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fundmy.space

## Body

Front Page Dashboard User page Claiming a Balance Inspiration The inspiration behind FundMy.space comes from the unavailability of accepting funds / donations from platforms such as BuyMeACoffee, Kofi, Patreon, GitHub Sponsors due to either PayPal or Stripe being unavailable in the country I reside. The other reason is that Banks in my country are really slow and processing fees are really high. What it does FundMy.space doesn't use PayPal or stripe instead it uses the Blockchain more specifically the Stellar Network to allow the exchange of Assets. With Blockchain there are no limits on who can and who cannot accept funds. Anyone with a valid Stellar Account can! Stellar has support for more than 8000 Assets. How I built it FundMy.space is built using Django a Python Framework. It communicates via Horizon Stellar's API Endpoints to execute operations and query records. It uses Sponsoring Reserves to help with the account creation for a particular user and uses Fee Bumps and Claimable Balances to ease out the process for claiming all kinds of Assets and Stable Coins. For the frontend I used the bootstrap framework to build a simple design. Challenges I ran into The Challenges I ran into were the errors I got while writing my code. Some of those were my fault some of those could happen by an error from the User, so trying to predict what the user can do wrong is and writing an exception along with an error alert is a bit hard. Accomplishments that I'm proud of I'm proud that I managed to build such a complex project in 36 hours. What I learned I learned more about the Stellar Blockchain, building and deploying Django Projects and how to manage my time well. What's next for FundMy.space Support for other cryptocurrencies and an improved design and Error handling. <div