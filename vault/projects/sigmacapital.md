---
slug: "sigmacapital"
url: "https://devpost.com/software/sigmacapital"
title: "SigmaCapital"
hackathon: "Hack the Northeast"
winner: true
words: 401
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
---

# SigmaCapital

> A revolutionary new approach to stock investing through data driven recommendations. SigmaCapital seeks to empower you to make informed financial decisions using the power of data analytics.

[Devpost](https://devpost.com/software/sigmacapital) · hackathon [[Hack the Northeast]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]

**stack** alpha-vantage, initial-state, python

## How they structured the write-up

- sigmacapital
- table of contents
- introduction
- technologies
- requirements
- status
- acknowledgements
- challenges

## Body

SigmaCapital A revolutionary new approach to stock investing through data driven recommendations. SigmaCapital seeks to empower you to make informed financial decisions using the power of data analytics. Table of Contents Introduction Technologies Requirements Status Acknowledgements Challenges Introduction Investing into the stock market has always beeen a daunting task. For first time buyers, there are many pitfalls to avoid. Which stocks should I invest in? What current market trends do I need to be aware of? When should I sell my shares? These are common concerns that can arise when dipping your toes into the stock market. SigmaCapital was conceived as a response to these challenges and seeks to simplify the convoluted world of finance and stock market investing. We use advanced data analytics in order to generate real time predictions about the near future value of a stock, giving you the insights you need in order to make informed decisions on the stock market and maximise your returns. Technologies The app runs on a Python backend, which samples 5 year historical data from the Alpha Vantage API. This data is fed into a set of models that generate predictions, which are then combined with information from other economic indicators in order to produce a final recommendation of "Buy", "Sell" or "Hold". This recommendation is then streamed to a Initial State Front End. Requirements Python 3.7 is the main requirement. As such, you will also need to pip install the latest versions of alpha-vantage, ISStreamer and pmdarima (which fetches statsmodels, which is also required). Status As of 7th June 2020, the project status is still active. For future improvements, we want to add more sophisticated models and indicators to our repertoire so that we can further optimise the accuracy of predictions. We also want to add support for indices such as the S&P500 and FTSE100 and generate sector specific predictions. We are also exploring plans to integrate our product into banking accounts, so we can generate personalised predictions for our customers. Our vision is to create a comprehensive platform that encompasses stocks, bonds, ETFs, foreign exchange and cryptocurrencies. This is just the beginning. Acknowledgements We used the Alpha Vantage API in order to get the latest, up-to-date stock data. Furthermore, parts of the project were adapted from here . Challenges Our models were more conservative than expected due to the drastic effect of the COVID-19 pandemic on the stock market <div