---
slug: "budgetbot-vqfn1c"
url: "https://devpost.com/software/budgetbot-vqfn1c"
title: "BudgetBOT"
hackathon: "Hack to the Future"
organization: "Finastra"
winner: true
words: 318
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
---

# BudgetBOT

> Pay Smart, Not Hard - Our solution uses a combination of FFDC APIs and our new trained Machine Learning models to help marketplace consumers find things that are affordable specifically for them.

[Devpost](https://devpost.com/software/budgetbot-vqfn1c) · hackathon [[Hack to the Future]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** api, asp.net, c#, fusion, html5, javascript, machine-learning

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for budgetbot

## Body

BudgetBOT Use Case (UI) BudgetBOT Use Case (Response) Inspiration When people start looking for a home, they either start at a home marketplace such as Zillow, Realtor.com, etc. or a lender. Between the amount homes cost, and the amount someone can get approved for with a loan, it is difficult for shoppers to know exactly how much home they can afford. What it does To help with this problem, we created BudgetBOT. BudgetBOT is a service designed to bridge the gap between lender and marketplace and create a consistent and seamless experience for consumers. By creating this partnership between lenders and marketplaces, we are able to provide marketplaces with a way to cater their results to a consumer’s finances, and in return, drive more loan opportunities back to the lender that provided the data. How we built it BudgetBOT works by analyzing a user’s bank accounts using several FFDC Malauzai APIs. It looks at account balance as well as historical account transactions to create trends for that user. Once the data is analyzed, BudgetBOT performs calculations to come up with 3 levels of affordability based on the consumer’s spending – Affordable, Semi-affordable, and Unaffordable. Beyond this, it also feeds the user’s spending and demographic information into 10 different machine learning models trained from US Government Consumer Spending survey results to come up with areas where the user’s budget is higher than people with similar demographic information. After all these calculations, the three affordability levels as well as categories where the user can improve their budget are sent back to the marketplace to be used in their search results. By being able to tailor search results, the marketplace can help users determine which results are affordable to them. What's next for BudgetBOT This service is an open platform API so the possibilities for marketplace use is endless - Auto Dealerships, Boat Dealerships, Realty Groups, Property Management Groups, etc.. <div