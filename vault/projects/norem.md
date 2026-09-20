---
slug: "norem"
url: "https://devpost.com/software/norem"
title: "Norem"
hackathon: "Junction 2017"
winner: true
words: 611
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
---

# Norem

> Bringing power of online banking to SMEs

[Devpost](https://devpost.com/software/norem) · hackathon [[Junction 2017]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** expo.io, react-native, sketch

## How they structured the write-up

- inspiration
- for whom
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for norem

## Body

Inspiration As regular customers we are already using dozens of various solutions for online banking. However, all the small and medium enterprises are customers, too. SMEs do need simple native ways of retrieving information on their accounts, they need tools to manage invoices and, most importantly, set up expectations for the nearest future. Whether you are a succeeding company or not, you need the simplest way of accessing your account information possible. What can be simpler than the very same banking service you already use? This is exactly the idea of Norem – use the power of PSD2 and establish a native and simple environment for managing SMEs banking data. For whom The key target audience of Norem is SMEs, which include any kind of startups, development studios or even freelancers trying to get the expectations of their current economy challenges. The target audience is also a key difference. While, the market is overwhelmed with 'personal saving plans', implementations for companies lack ideas, creativity and usability. Thus, SMEs is an excellent audience, since this area is open for disruption What it does At this stage Norem is able to find all the recurrent payments and sum those up, allowing the company to see regular spendings. Also, you can find all the invoices and manage those via the application. Norem sets up the flow of the revenue and, if you are not succeeding at covering all the costs, it will try to help you with managing invoices or transfer money from other accounts How we built it The project is built with Expo, which means that at this moment it is a native application for both Android and iOS, with support of the most variations (hi, iPhone X). React Native uses regular fetch requests to access Nordea's API. However, since the API is still in progress, some data was modified in order to meet real life situations. It does not affect the logic at all, but simply works with more relevant data. The actual API implementation including all the get and post requests for accounts and payments can be found in the application in the forth tab. The rest of the application, uses sample mockData file, which perfectly mimics the structure of the Nordea's API responses Challenges we ran into The biggest challenge is the state of the API – it is hard to retrieve different from default data and modify it. However, all the key aspects, such as account-instance are implemented, which means that at most of the situations the similar behaviour can be anticipated. Accomplishments that we're proud of Design of the application and the landing page Really nice and clean set up of React Native: logic separation and use of simple independent modules as well as totally independent API section Opportunity to work with real Fintech product A chance to affect life of companies all over the world What we learned How to design and code the application at the same time at immersive speed API requests for Fintech services Brainstorm and validation What's next for Norem At the moment most of the functionality is just a basic setup, which works as a proof of feasibility of concept. However, we would like to bring more complex logic and the predicative analysis of the revenue flow with more options to explore (set up limits for different accounts, split the accounts, connect cards and manage cards subscriptions). Additionally, some parts of the application depend on mock data, but since all of the functionalities that were expected to be used in the application are currently in the progress or planned for the nearest future it is just a matter of time <div