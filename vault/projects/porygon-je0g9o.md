---
slug: "porygon-je0g9o"
url: "https://devpost.com/software/porygon-je0g9o"
title: "Porysays"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 512
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# Porysays

> Build, backtest and automate trading strategies without programming or burning your wallet.

[Devpost](https://devpost.com/software/porygon-je0g9o) · hackathon [[MongoDB World Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]

**stack** mongodb, mongoose, node.js, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- about the team
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for porysays

## Body

Stock details view Create strategy Backtest results Orders view Inspiration The inspiration behind Porysays comes from our own personal experiences with learning how to trade. We found the process to be very convoluted and the tools available to be too bloated for a beginner starting out. Analysing charts and determining when to place orders is overwhelming and a lot of the rules could be applied programmatically. We created Porysays as a playground for learning how to create trading strategies, test using historical data and automate without burning our wallets. Our vision is to level the playing field and make trading more accessible to everyone. What it does Users can create trading strategies using technical indicators. Backtest using historical data to see how accurate a strategy would have predicted actual results. Paper trade to practice buying and selling stocks without risking real money (trading automation in development). How we built it Database uses MongoDB Atlas for storing user data, strategies, indicators and backtest results and Mongoose for schema management. Frontend is built in React. Backend is built in Node using Hapi with the following endpoints available: [POST] Create a new user [GET] account [GET] orders [DELETE] orders [POST] an orders [GET] positions [GET] stocks [GET] stock chart [GET] indicators [GET] strategies [PUT] Update strategies [DELETE] strategies [POST] Execute backtest strategy [GET] backtest results The magic The "Porysays engine" responsible for backtesting and risk analytics is written in Python and communicates with the node backend using GRPC. Hosting Frontend is hosted on Netlify and Backend is hosted on AWS. About the team Samantha and Luannie are both colleagues working in two sister startups in Melbourne, Australia. Outside of work, you can find the dynamic duo and partner in crimes dabbling in new technologies and hustling on side projects together under the alias Shooting Unicorns . Challenges we ran into From a front end perspective, building a dynamic form where the fields are determined by indicator input parameters and rules was quite challenging. However, the biggest challenges are actually non-technical, where we had to learn how to evaluate the results produced by each technical indicator and how to create buy and sell signals. We also put thought into the designs of Porysays with consideration around onboarding and how we could make it intuitive for new traders to use. Accomplishments that we're proud of We've been hacking on Porysays full time over the weekend and every night for the hackathon! We're extremely proud of the amount of work delivered in such a short amount of time and we can't wait to continue developing this idea post hackathon. What we learned A lot about trading, Python, and MongoDB change streams although we didn't get to use change streams yet. What's next for Porysays Continue optimising our engine to eliminate backtesting biases and overfitting of data to produce more accurate results. Add more technical indicators Automate paper trading using results from strategies. Use MongoDB change streams for real time orders and notifications! beef out risk management [edit]: changed Porygon to Porysays. Built with love by Shooting Unicorns <div