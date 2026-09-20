---
slug: "finbay-cskr1h"
url: "https://devpost.com/software/finbay-cskr1h"
title: "FinBay"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 572
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "user/general_public"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# FinBay

> A credit card advisor for beginners to develop healthy financial habits.

[Devpost](https://devpost.com/software/finbay-cskr1h) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[education]] [[finance_payments]] [[retail_commerce]]
**user** [[educator_student]] [[general_public]] [[small_business]]
**substrate** [[financial_record]] [[structured_db]]

**stack** arima, finance, firebase, flutter, gcp, lambda, machine-learning, plaid, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for finbay

## Body

Adding a financial institution Show the best cashback cards based on vendor The rewards for certain categories, for all available cards Select a credit card based on our model that forecasts future purchases on past transactional data The benefits from choosing one card over the other A list of the user's cards Inspiration A good financial posture is critical in today’s daily life, and that begins with credit cards. How does one choose a credit card for themselves, if all the information they receive is vendor-biased? If it is recommended that you maintain many credit cards for credit building, using which one, and where, where will benefit the user the most? How does a university student with no credit history, make a decision about what card to use? As the only application that offers our functionalities, we present a seamless application that is integrated securely using Plaid, delivering educational value and optimal financial recommendations, completely free of any bank bias. What it does With FinBay, here are some of our key features: Forecast end-of-week, end-of-month, end-of-year expenditures based on frequent categories (Groceries, Restaurants, Travel) and overall trends Recommend the most optimal credit card for the current purchase based on expected expenses, maximizing all rewards and incentives Allow the user to securely authenticate themselves to a variety of leading banks, to manage their financial portfolio Aggregate and display the interest rates/other benefits tied to each credit card in an interactive dashboard Our recommendation and forecasting features are agnostic to financial institutions How we built it Mobile App We developed the mobile App in Flutter, written in Dart, with an emphasis on an interactive and easy-to-use design. The mobile app is connected to our backend applications through firebase and cloud functions. Backend Our backend is developed with TypeScript and centered around the Plaid API to securely retrieve and store card, transaction, merchant, and other dashboard information. Algorithms We used the ARIMA model with Python, to forecast the expected value of future transactions based on a history of previous transactions aggregated at a category level. We then use this information to determine the benefits from each card, standardizing all benefits to a monetary level. Based on the expected benefits, we recommend a card to the user. Google Cloud We used firestore as our no-sql database implementation to store all retrieved transactions, and other aggregated information for the dashboard with firebase for authentication. With an asynchronous server-less pipeline, all our backend functions and ]algorithms are hosted on cloud functions, triggered incrementally with event triggers. For example: the cloud function which holds our forecasting algorithm is directly triggered when an update or a new user with transactions has been created. Languages: Dart, TypeScript, Python Challenges we ran into Integration with firestore, such as writing to firestore from a cloud function Setting up the asynchronous triggers, such as triggering the ML algorithm when a transaction is added or created What's next for FinBay Next, we would like to further work on the app to expand our card and stores selection, and improve the recommendation algorithm before making this available to the public. Also we want to explore further ways to import transactional data from other vendors (some people may not be comfortable solely relying on Plaid) and supporting more financial products to better educate everyone. Research and Statistics An average person owns 3.1 cards ( https://www.valuepenguin.com/credit-cards/statistics/usage-and-ownership ) $893 billion credit card debt in US ( https://www.fool.com/the-ascent/research/credit-card-debt-statistics ) <div