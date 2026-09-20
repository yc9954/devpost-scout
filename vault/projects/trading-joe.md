---
slug: "trading-joe"
url: "https://devpost.com/software/trading-joe"
title: "Shtocks"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 619
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
---

# Shtocks

> AI powered automated tools to buy and sell stocks based on rumours and news.

[Devpost](https://devpost.com/software/trading-joe) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]

**stack** alpaca, apexcharts, javascript, postman, twitter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for shtocks

## Body

Inspiration While the world is currently grappling with the devastating health and emotional effects of the Covid-19 pandemic, it is widely feared and speculated that the pandemic's economic after effects will also be dire and long lasting. In the same way that technology helped people to overcome the quarantines and lockdowns, I think it can help with the economic tsunami that is on the way. Governments are printing money at a frightening pace, which will probably lead to high inflation rates. The best way for people to deal with this problem is owning assets, and the easiest and cheapest to buy are stocks in companies, which will not only derive monetary growth for those who own it, but will also help drive the economic recovery for everyone. What it does This application hopes to democratise stocks and provide a useful toolbox which will help developers: buy and sell stocks with eases and without fees in a clever way - by getting ideas on what to buy and when to sell (buy the rumour, sell the news) and add AI based automation - for optimization, speed, and well - we're not stock brokers, we have a day job - do it all for you How I built it Ever since I saw the Alpaca™ API, I've wanted to use it and this was a great opportunity. I used it to set up the FREE buying and selling of stocks , as well as getting useful information like: Current stock information Market Opening and Closing times Technical data which I then processed using postman visualizer to create candlestick charts In order to get suggestions on what stocks to buy/sell, I used the Twitter™ API and ran that information through the IBM Watson™ API for sentiment analysis in order to get a buy or sell recommendation. I curated a number of twitter accounts which are considered speculative future looking - the "rumours". Those are monitored using Postman™ monitors and when they have a very positive sentiment about a stock, it's time to buy. I then curated a number of popular news outlets, and when those publish information - with very strong sentiment (positive OR negative) it's time to sell. Challenges I ran into Authentication against the various Twitter™ APIs was confusing and took a long time to debug. There are several versions of the API, each has different permissions, and there are two possible authentication protocols - not fun. The Postman™ console really helped here, by letting me see the HTTP details. It was also the first time I used the Postman™ monitors, so that took some time to understand. Accomplishments that I'm proud of I'm proud of the resulting tools which I think other people will be able to fork and build even more useful applications. I also hope that besides the fun in this, others will derive financial benefit and help the economy recover. What I learned I have been using APIs for many years, but I gained additional knowledge and experience in how to build good and useful APIs, as well as mistakes to avoid, from using the various APIs in this project. I have used Postman™ before, but it was fun to learn about the other amazing capabilities of Postman and how those parts can work together to build super versatile autonomous workflows. What's next for Shtocks Shtocks will always be open and public, and I hope others will join in building this further, either by adding additional functionality to the workspace or by forking it and taking it to other creative directions. I plan to add additional tools to make the buying and selling options more accessible as well as making the AI part more advanced. <div