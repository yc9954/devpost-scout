---
slug: "fusion-creditsense"
url: "https://devpost.com/software/fusion-creditsense"
title: "Fusion CreditSense"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 733
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Fusion CreditSense

> With Fusion CreditSense, we leveraged OpenBanking+FFDC APIs and machine learning to create creditworthiness and micro-loan prediction models based on a user's transaction history.

[Devpost](https://devpost.com/software/fusion-creditsense) · hackathon [[Hack to the Future 2020]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]]

**stack** angular.js, docker, ffdc, flask, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for fusion creditsense

## Body

Fusion CreditSense Inspiration With the world amidst a pandemic and a looming credit crisis, we took advantage of the opportunity to participate in the hackathon where we can leverage the tools, technology, and resources to create something that we can implement and make a real-world change. In particular, we focused on building financially inclusive technology for people who have difficulty gaining credit due to the traditional credit scoring system. What It Does We created a platform that allows a user to gain creditworthiness and financial credibility using alternative financial records that are not typically used in traditional credit scoring models: banking transactions. Our application seamlessly allows a user to connect his banking details and almost instantly returns a credit score and a microloan offer. How We Built It Our FFDC-Branded Angular/Material User Interface is powered by our custom Edge Service, which integrates the handling of both the machine learning and the FFDC + OpenBanking APIs. The OpenBanking APIs return the transaction records, which are fed into two separate machine learning models through a Flask application. Both machine learning models take into account various features and mathematical aggregations derived from the transaction data--and one model assigns the credit score, while the other one predicts a microloan amount. Next, we do another API call to FFDC to register the customer into our system, and begin the process of moving forward with the loan. The user interface was built using Finastra Design System and is perfectly integrable with any Finastra branding products. The user experience is consistent, accessible, and easy to use. Challenges We Ran Into We faced unexpected issues when integrating the Loans FFDC APIs due to lack of unsecured loan products available in Fusion Essence. During the course of the project, we found that these same loan APIs had now been marked as unavailable for use in the Sandbox. Additionally, the OpenBanking APIs that we integrated were still in the development phase, meaning that we had a limited number of APIs to call. We also had to map account numers and sort codes to account references for the OB APIs. In terms of the data, the OpenBanking data that we had access to was limited. Thus, we came up with our own method of generating fake data, but this could mean that the data was inherently biased, leading to potential biases in the ML models. With the integration of multiple systems in the project (Open Banking APIs + FFDC Fusion Essense APIs), we found that some data mapping was necessary. Accomplishments We're Proud of We built a microservice leveraging cutting edge technologies through a beautifully working infrastructure. With 2 ML + AI models, multiple APIs, we developed a packaged solution that can be white labelled or sold as a standalone Finastra solution. 2 Finastra Core systems communicate through FFDC as the backbone of innovation, and the APIs we utilized allow integration into those legacy core systems for existing financial institutions to enable adoption for existing players in the space. FFDC APIs we used: Customer Onboarding : Personal Customers > Search personal customers Customer Onboarding : Personal Customers > Create personal customers Loans : Loan Enquiry > Retrieve the list of loans for a given customer Loans : Loan Creation > Create basic loan OpenBanking APIs we used: OpenBanking : Get Banks > Get all financial institutions that support OpenBanking on the Finastra platform OpenBanking : Get Accounts > for this enrolled customer get all Bank Accounts that have consent to share data via OpenBanking OpenBanking : Get Transactions > For the selected account, get all transaction data. What We Learned With the integration of multiple core systems, we learned pretty quickly that "nothing good ever comes easy"! Expectedly, we ran into multiple issues while putting together the whole infrastructure and getting everything to flow smoothly. While doing background research about this project, we also learned about the problems of the traditional credit system and its factors in order to apply the shortfalls of this system to our Proof-of-Concept solution. What's Next for Fusion CreditSense We could not get some parts of the Loans APIs fully working in time, but this could be a planned future integration. Because we have a mix of standalone APIs as well as a packaged UI service available in the cloud, this means that we have 2 routes for commercialisation. It could be offered as a standalone Finastra solution. <div