---
slug: "stock-alert-islw3f"
url: "https://devpost.com/software/stock-alert-islw3f"
title: "Crypto Trader Alert"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 220
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/structured_db"
---

# Crypto Trader Alert

> Most important parameters for a trade are entry point, target and stoploss. The collection we created is a slack alerter once target of stoploss is hit, so that the user can proceed closing the trade

[Devpost](https://devpost.com/software/stock-alert-islw3f) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[structured_db]]

**stack** coingecko, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for stock alert

## Body

Inspiration Being a trader, we rely the most on stock alert. As part of fundamental analysis, we first arrive at an entry point (Buy of tock is done), target (Profit is taken out) and a stoploss (Minimise loss). As we cannot monitor the market every second, we would be wanting an automated alerter to get an alert when any of these are hit. What it does The current alerter is built for Crypto currency. We have used api exposed by CoinGecko to get the stock quote. We can give list of currencies and their corresponding targets and stop losses as parameters in a csv file. The collection posts to slack a message if either of these are hit How we built it We used postman collections to put all out requests. CoinGecko free APIs are used to fetch quotes. Slack Apis are used to post message in slack Accomplishments that we're proud of The main aim of our hack was to learn how to use Postman collection. That was accomplished with this. Also, being a trader, I would love to have a realtime alert for stocks. With the tests in this postman collection, we could achieve that What's next for Stock Alert Build a realtime poller so that this can be used for the purpose it was built for <div