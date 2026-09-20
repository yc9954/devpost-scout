---
slug: "money-money-stocks-bot"
url: "https://devpost.com/software/money-money-stocks-bot"
title: "MoneyMoneyStocksBot"
hackathon: "XHacks 2021"
organization: "XHacks Organization"
winner: true
words: 452
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# MoneyMoneyStocksBot

> Enjoy easy-to-access stock data through discord.

[Devpost](https://devpost.com/software/money-money-stocks-bot) · hackathon [[XHacks 2021]]

## Facets

**mechanism** [[realtime_stream]]

**stack** alphavantage, discord.py, flask, git, github, matplotlib, python, repl.it

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for moneymoneystocksbot

## Body

MoneyMoneyStocksBot Help command Some example stocks IBM Stock Example Shopify Stock Inspiration A couple of months ago when we were first getting into stocks, we found that we missed out on many opportunities whenever we didn’t check on stock updates and trends, especially that of GME and AMC, some of the biggest booms in the stock market in recent memory. This is because to obtain this type of information, you would typically have to manually search for it. We wanted a convenient way to show your favourite stocks through a simple channel that we regularly use , and since we consistently use Discord in order to chat with friends, which has become common-place especially with the pandemic and not being able to go outside, we connected our passion for the two, and MoneyMoneyStocksBot was created. What it does MoneyMoneyStocksBot connects people with up-to-date stock prices, charts and updates, straight onto Discord servers, all through a single, simple command . That way we can do what we need to do straight from Discord, which countless amounts of people use on a daily basis. The bot obtains real-time stock data through the AlphaVintage API, and displays it through an easy to understand and concise graph for you to view in order to make smart, informed stock market decisions. How we built it We used: Discord.py, a Discord API for developing the discord bot commands and general upkeep of the bot AlphaVantage, an HTTP API to access accurate historic and current stock data MatPlotLib, a python library for making easy-to-understand graphs of the different stocks Flask and UptimeRobot for keeping the bot running 24/7 Challenges we ran into This is the first time that any of us worked with this API, so finding a way to efficiently parse through the large quantities of data that we received from the API and extracting the specific information gave us a bit of trouble, and it took us a bit of time to properly find a method of doing this. We ran into some difficulties in terms of plotting the information into useful graphs when we first used the MatPlotLib library, which we resolved by choosing the settings that would make the graph most user-friendly. What's next for MoneyMoneyStocksBot New updates to MoneyMoneyStocksBot we hope to add in the future: Wider range for stock data (1 day, 7 days, 1 month, 6 months, and so on) A command to display cryptocurrency data A 'recommended' command that allows users to see which stocks have been on a positive trend lately The ability to select certain stocks to add to your user profile, and the bot gives you alerts to any major changes in the price of those stocks <div