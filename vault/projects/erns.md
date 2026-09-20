---
slug: "erns"
url: "https://devpost.com/software/erns"
title: "Erns"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 868
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Erns

> An institutional-grade earnings intelligence terminal that levels the playing field for retail investors through real-time data, AI sentiment analysis, and quantitative modeling.

[Devpost](https://devpost.com/software/erns) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[government_staff]] [[researcher]]
  <sub>weak: legal_professional</sub>
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** beautifulsoup4, clerk-(authentication), fastapi, feedparser, framer-motion, lxml, mongodb, mongoose, next.js, numpy, pandas, python, react, sec-edgar-api

## How they structured the write-up

- the problem
- the solution: what is erns?
- how it works (technical architecture)
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for erns
- 🛑 important notes for judges to test the app

## Body

Logo Erns The Problem Earnings season is one of the most volatile and opportunity-rich periods in the stock market. However, the playing field is entirely uneven. Institutional investors and hedge funds have access to expensive, lightning-fast terminal software that instantly parses SEC filings, aggregates analyst estimates, and models expected price moves. On the other hand, retail traders and independent analysts are stuck refreshing Yahoo Finance, digging through dense 10-Q PDFs on the SEC website, and manually searching for historical EPS beats or misses. Building a cohesive picture of a company's earnings performance takes hours of manual research, and by the time a retail trader figures out the sentiment of an earnings report, the market has already moved without them. The Solution: What is Erns? To level the playing field, I built Erns (originally called Tyche). Erns is a professional-grade earnings intelligence platform designed to give everyday investors institutional-level insights. It transforms how users interact with earnings data by combining real-time web scraping, AI-powered sentiment analysis on SEC filings, and advanced quantitative metrics into a single, sleek terminal interface. With Erns, users can instantly see which companies beat or missed expectations, screen upcoming earnings by market cap and date, track real-time price reactions, and even read AI-generated summaries of lengthy financial documents. How it works (Technical Architecture) Erns is built as a highly decoupled full-stack application. The Frontend Network: The user interface is a Next.js (App Router) application that I built to resemble a high-end trading desk or Bloomberg Terminal. It uses Tailwind CSS, Shadcn UI, and Framer Motion for a dark, data-dense, yet incredibly responsive aesthetic. I used Clerk to handle secure user authentication, MongoDB to store user profiles and watchlist preferences, and integrated Nodemailer to seamlessly send automated email notifications to users. The Backend Engine: The heavy lifting happens on a proprietary Python FastAPI backend. The API layer is massive and handles complex data aggregation. I wrote custom scraper scripts using BeautifulSoup and feedparser to continuously pull live data from sources like Yahoo Finance, Nasdaq, and the SEC EDGAR database. To ensure the terminal remains fast, the backend uses SQLAlchemy and a local SQLite database to aggressively cache the scraped JSON payloads, earnings calendars, and financial metrics. The backend also handles quantitative math, such as calculating the options market's Expected Move based on implied volatility. A simplified version of this calculation looks like this: $$ \text{Expected Move} \approx \text{Stock Price} \times \text{Implied Volatility} \times \sqrt{\frac{\text{Days to Expiration}}{365}} $$ Challenges I ran into Building a financial data platform from scratch was incredibly difficult. First, financial data is notoriously dirty. Synchronizing and normalizing data from completely different streams required writing robust fallback logic. A ticker might be listed differently on Nasdaq versus the SEC database, so mapping everything precisely was a nightmare. Second, performance under load was a major issue. Processing massive JSON payloads from the SEC and running sentiment analysis on dense 10-K filings requires heavy computation. I had to completely re-architect my backend caching mechanisms so that the FastAPI routes could return data to the frontend in milliseconds rather than timing out. Finally, managing complex frontend state for interactive charts and real-time news feeds without causing the browser to stutter required extremely careful optimization of React hooks. Accomplishments that I'm proud of I am most proud of the UI/UX design. Financial data is inherently boring and overwhelming to look at, but I managed to build a terminal that feels premium, fast, and exciting to use. I am also incredibly proud of the backend architecture. Pulling real-time market data without paying thousands of dollars for enterprise API keys meant I had to creatively engineer my own scrapers, and making them run reliably is a huge personal win. What I learned This project pushed my skills as a full-stack developer further than anything I have built before. I learned how to properly architect a scalable API using FastAPI, manage database connection pooling, and build animation-rich UIs with Next.js. I also learned a tremendous amount about market mechanics and how institutional data pipelines actually work behind the scenes. What's next for Erns I plan to add real-time WebSocket integrations so the terminal updates live without needing a page refresh. I also want to expand the AI integration to include voice or text-based querying (e.g., asking the terminal "How did Apple's margins look this quarter?"). 🛑 Important Notes for Judges to Test the App You can visit the live application at tychefinancials.com (which will be migrating to ernsfinancials.com in the future). Waking up the Backend: Because the backend is currently hosted on a free tier, it goes to sleep when idle and does not run 24/7. Please open api.tychefinancials.com in a new browser tab first! Opening the API link will wake up the server so the terminal functions properly. Stripe Billing is in Test Mode: The Stripe integration is actively in development. This means no actual payments are required. You can click through and test out all the premium features and subscription tiers completely for free! Open Source Note: The provided GitHub repository only contains the frontend code. I have kept the backend proprietary to protect the custom APIs, scraping logic, and AI analysis models used to gather the data. <div