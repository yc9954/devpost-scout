---
slug: "newspulse-ai"
url: "https://devpost.com/software/newspulse-ai"
title: "NewsPulse AI"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 570
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# NewsPulse AI

> Track Key Business Events Impacting Your Investments

[Devpost](https://devpost.com/software/newspulse-ai) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** databricks, dbrx, duckduckgo, langchain, openai, pandas, python, streamlit, yahoo-finance

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for newspulse ai

## Body

sentiment analysis sentiment vs stock price chat over news articles architecture GIF gif demo Inspiration It is quite difficult to keep track of what's going on in the today's world. With tech layoffs, product recalls and major reorgs, both corporate and retail investors risk their capital if they don't monitor their portfolios closely. Hundreds of news articles are published daily, potentially containing crucial information about a company. Reading all of them is time-consuming, especially if our portfolio contains many stocks. With that in mind, I decided to build an app that provides insights through up-to-date news analytics. What it does The app is designed to monitor the latest news articles and analyze sentiment around various business events, such as layoffs, M&As, reorgs, disputes, etc. Such events may have significant impact on stock performance, and therefore are crucial for the investors. The app has three main features: Sentiment Analysis (by day and topic & aggregated) Stock Price vs Sentiment (time series that allows to analyze impact of news sentiment on stock performance) Chatbot (Q&A with vector search index and sources) The process of acquiring the data is as follows: DuckDuckGo API is used to fetch the recent news articles about the selected company. ScrapeGraphAI and GPT 3.5-Turbo is used to scrape article content from URLs. DBRX Instruct and LangChain is used to extract sentiment from articles. RAG: the articles are split into chunks, embedded & loaded to vector store. YahooQuery is used to load stock price history data. The idea is that the Databricks jobs are scheduled to run every day or even multiple times per day to enrich the database and vector store with the newest articles. How we built it I built the project using Python and multiple libraries like Streamlit for front-end, LangChain for LLM Ops, ScrapeGraphAI for web scraoing and pandas and spark for data processing. There are three Python notebooks in Databricks: Scrape, Clean & Load Articles.ipynb Extract & Analyze Sentiment.ipynb RAG.ipynb The additional files for the front-end can be found in GitHub Repo. Challenges we ran into The main challenge I ran into is AWS costs associated with developing an app. Because of that I could not load enough data and was constrained by time to develop in Databricks notebooks. The second challenge is that during the trial period, it is not possible to deploy model endpoint. That is why the chat feature was not fully deployed using Databricks. For the demo, I used embedchain locally to demonstrate the desired functionality. Accomplishments that we're proud of I'm proud that I was able to build the data pipeline that includes multiple API calls and LLM chains. On top of that I'm happy that I was able to use my Python skills to build the front end of the app. What we learned I've learned about the existence of DBRX model and vector stores in Databricks. Additionally, I learned about the RAG process and experimented with different options to split the content. This allowed me to learn how different approaches impact the LLM response quality. What's next for NewsPulse AI There are a few features that can be added to the app: New user sign up process (create account, select watchlist) More sophisticated analysis of stock vs sentiment correlation The chatbot that uses Databricks endpoint NOTE: The demo app is not connected to the Databricks due to the ending trial account and to avoid AWS costs. <div