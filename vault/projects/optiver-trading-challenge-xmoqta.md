---
slug: "optiver-trading-challenge-xmoqta"
url: "https://devpost.com/software/optiver-trading-challenge-xmoqta"
title: "Money Making Market Maker #team-14"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 531
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/regulation_legal_text"
---

# Money Making Market Maker #team-14

> Bulding a bot for the Optiver Market Making Challenge.

[Devpost](https://devpost.com/software/optiver-trading-challenge-xmoqta) · hackathon [[HackZurich 2021]]

## Facets

  <sub>weak: finance_payments</sub>
**substrate** [[regulation_legal_text]]

**stack** python

## Body

Due to Covid-19 and the resulting recession we all got interested in the world of trading and the stock market. General Approach For our solution, we submitted an approach focusing on influencing the market in means of liquidity of green stocks and at the same time exploiting small discrepancies in prices for personal profit. Mainly, we employ the Quoting Strategy, thereby minimizing risks and making the market to make money. To achieve this, we estimate a fair price for the ETF we want to trade. This value Theo (abbrev. Theoretical value) consists of a bid and ask representing what we consider the current fair ask and bid price. In our case, Theo is the mean of all bids, and separately of all asks of stocks in the C2 GREEN ENERGY ETF . To generate profit based on this estimated price tag, we now place new limit orders, in a given range around Theo , trying to generate profit by buying below Theo.bid and selling above Theo.ask . To minimise the exposure of the market, we hedge each investment as fast as possible using IOC's in the stocks, which the ETF is based on. Algorithm Our algorithm iterates over a set of function calls in roughly that order: Before opening any new trades, we try to hedge any open investments. We get the current highest bid and lowest ask from the price book for our stocks of interest in order to calculate Theo . Given Theo . If anyone sells below Theo.ask , we consider this a sell below value and if anyone buys above Theo.bid , we consider this a buy above value. In such cases, we act immediately using IOC's trying to acquire those positions for personal profits. Otherwise, we try to be the best bidder and asker with a margin of profits using limit orders. Before a trade is executed we make sure that all market regulations are met. Note: We always delete existing limit orders before executing above mentioned IOC's and update them afterwards so no conflicts occur. We hedge while limit orders are possibly active in order to keep them alive as long as possible before canceling them. Complying to Regulations We always calculate a minimum volume of lots to be traded at once while still complying to all market restrictions. Rule 1 : Differences to the capacity are considered. Rule 2 : We have a hard-coded check to not exceed 800 orders per instrument. Rule 3 : We apply a Ring-Buffer of size 25 containing the time stamps of the most recent orders. Rule 4 : We calculate the maximum possible volume of a trade after which the new positions still comply to the risk rule. Credit Factor In order to prevent being stuck at the edges of the maximum positions per instrument and possibly missing out on good investments, we decrease the profit margin over time to make it more attractive to potential traders. When they accept our offers, it moves us away from the limit of maximal positions yielding in opportunities in any new directions. We use a square-root based factor which introduces a lean towards profit, i.e. preferring safety over own liquidity. <div