---
slug: "stratl"
url: "https://devpost.com/software/stratl"
title: "Stratl"
hackathon: "Hack to the Future"
organization: "Finastra"
winner: true
words: 786
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/researcher"
---

# Stratl

> The lego of finance for designing investment strategies

[Devpost](https://devpost.com/software/stratl) · hackathon [[Hack to the Future]]

## Facets

**domain** [[finance_payments]]
**user** [[researcher]]

**stack** angular.js, gcp, java, mongodb, spring

## How they structured the write-up

- story
- first steps
- stratl - your strategy l ab
- our vision: a stratl community

## Body

Decision diagram Story In our team, we've been trading in investment banks, hedge funds and large commodity trading houses for years. The process that consists of programming, running simulations and analysing the results is time consuming, especially in a fast paced capital markets environment where testing a trading strategy, and weighting its associated risks, justifies, or at least supports all major trading decisions. Within a trading team, each one has their own trading ideas that they would like to test very quickly to be able to take the best trading decisions. The strategy design is very often a team effort. Backtesting is the first important step for the valuation of the potential risk and returns. First steps A few years ago, our co-founder, Marc, used to automate every single process that could (and should) be automated. He created good old excel files that let his teammates backtest their ideas very easily by importing market data, creating signals (e.g moving averages), and defining entry and exit levels for their positions. The UX, as you can imagine, was made as simple as possible: dropdown menus, automatic recalculation, visualization of results… The result of this tedious process answered 90% of his colleagues' needs. Building and testing almost similar strategies, with only slight modifications, over and over again, is currently the norm in trading companies. The STRATL idea simply hatched out of good old frustration at workl! :) It was time to try and suggest to all traders out there something new, initiated by the STRATL team, and eventually built and maintained by a larger community, for the community. STRATL - Your Strategy L ab STRATL helps traders design systematic trading strategies, without having to write a single line of code. The process is fun, with no frustration and produces fast results STRATL lets you create investment and trading strategies like a Lego , with pre-coded calculation modules. The design has two essential diagrams: an analysis diagram , where every node consists of a quantitative model, taking signals (or series e.g. prices) as inputs and producing signal outputs. a decision diagram , where every state corresponds to a target portfolio position. The transition between states is based on the value of the signals of the analysis diagram. With these two diagrams, the user can structure a large number of strategies . STRATL is built with Angular 8 on the front end, served by Java Spring and Mongodb on the back-end. The UX lets the user build strategies in a flexible and intuitive manner, backtest them and "debug" them efficiently. Backtests are produced on "minute" candles. The UX experience is also adapted for touch screens, for any passionate trader to use STRATL at their workplace, or from the comfort of their bed. Money never sleeps ;). The technological challenge is two-fold: bringing "fun" into a very serious sector , but mostly taking the frustration out of a trader's mind . To this end, the platform has to be very transparent . The trader has to understand quicklly why a strategy is performing well or not. optimized performance . The process is non-blocking. STRATL lets you design multi-asset strategies. Models can be very sophisticated. Our vision: a STRATL community In investment banking, trading houses or hedge funds, there are typically: quantitative analysts who develop quantitative models. These quantitative analysts can be either "quants" or "structurers". They need to convince traders of the sound logic of their models. In other words, they have to pitch and sell their model to the trading desk. Simliraly, STRATL is a quant marketplace where quants will be able to create models and sell them to the trading community. ITs who work hard on the IT infrastructure to serve the relevant data. Commodity houses are slowly shifting to cloud based solutions. STRATL lets you pay only for the service you need. Traders, asset and hedge fund managers who use signals to take investment or trading decisions. They also look for best execution. STRATL lets you participate in the performance of the most successful managers with a copy trading option. Every desk has a specific function and the full structure as it stands is hardly flexible or scalable. Today, starting a quantitative hedge fund with $100mio AUMs or less hardly covers the fixed costs. Historical data, IT infrastructure, Research and Development are all necessary to be and stay competitive. STRATL helps every trader to build their own trading environment. They can allocate resources efficiently. We are a team of financial and startup professionals with a lot to give and learn and we are thrilled to see our team of advisors, passionate technologists and traders, expanding. We started our B2B Go-to-market recently with the first exciting feedbacks from traders. <div