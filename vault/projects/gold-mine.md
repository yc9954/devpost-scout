---
slug: "gold-mine"
url: "https://devpost.com/software/gold-mine"
title: "Gold Mine"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 404
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/scientific_research"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Gold Mine

> Crawling the web and financial data to accurately predict company performance

[Devpost](https://devpost.com/software/gold-mine) · hackathon [[HackUTD X]]

## Facets

**domain** [[scientific_research]]
**substrate** [[structured_db]] [[web_dom]]

**stack** chakraui, fastapi, google-cloud, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gold mine

## Body

Home Page w/ Eleven Labs Agent Narrating Daily Forecast Financial Algorithm Visual Processing Company Score Page Category Score Page Company Score Page Trader View Company Score Page Trader View Company Score Page Trader View Note: If you just want to see a demo of the project, skip to the 1 minute point in the video Inspiration We were inspired by Goldman Sachs' prompt to explore various alternative data sources such as sentiment from social media and openly available stock data. Additionally, we all really wanted to explore the field of generative AI and thought that this challenge was the perfect place to do so. What it does Gold Mine crawls the web for social media sentiment as well as earnings reports of various companies to give investment advice on a stock by stock basis. Gold Mine crawls reddit, youtube, twitter, and the news for sentiment scores. It also scrapes companies 10-Q and 10-K forms from the sec's website. It combines these into a Base Stock Score which is then adjusted for macroeconomic conditions through our Macro Indicators section of the Stats Engine. All of this data is displayed on a dashboard so users can make informed investment decisions. How we built it We built it using FastAPI for the backend, MongoDB atlas as a database, which was hosted on Google Cloud. The frontend was made using ChakraUI and web scraping was done through various social media API's as well as web crawling through get requests. Challenges we ran into It was difficult finding free high quality data sources, so we had to spend extra time wrangling with those. Twitter recently made their api a lot more strict, as well as yfinance and earnings reports requiring paid access. Accomplishments that we're proud of We're proud of finding a way to scrape earnings reports for free as well as finding workarounds for the other api issues through caching in the mongodb database. What we learned We learned how to web scrape as well as cache api query results to avoid rate limits. We also read about stock valuation prediction papers, such as lazy prices, which expanded our financial knowledge. What's next for Gold Mine Next, we'd like to look at more research papers and see how we can incorporate those findings into our investor dashboard as well. We would also like to make a backtesting framework to more accurately showcase the effectiveness of each strategy <div