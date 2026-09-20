---
slug: "this-bank"
url: "https://devpost.com/software/this-bank"
title: "This.bank"
hackathon: "Junction 2017"
winner: true
words: 347
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# This.bank

> Your programmable bank account

[Devpost](https://devpost.com/software/this-bank) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[structured_db]]

**stack** es6, java, javascript, postgresql, redux, spring

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for this.bank

## Body

Inspiration As a people who use bank accounts on a daily basis, we always wanted to automate things we do every day such as regular payments, bills and money management. There is always a pattern, but for each person these patterns are individual. At Junction 2017 we were trying to make financial life much easier by automating financial scenarios. What it does This.Bank provides an interface to control your money through the code. We let you write code that interacts with transactions in real-time. For example, if you are saving money on vacation, you can write some code that rounds up each card transaction you make to the nearest 5 euro, and adds that to your savings account. Also, you can write code that automatically loads, parses and pays your bills. You can use the all features of JS engine(with the addition of our own library), details on the transaction, all info about your bank account to bring your idea to life. How we built it To build our product we’ve used Nordea Open API with ReactJS on the front-end part and Spring on the back-end, Postgres as a database. We fetch user's bank transactions through Open API and we run JS code created by a user when a new transaction is detected. Challenges we ran into We had challenges with Bank API and encountered some pitfalls with runtime execution of user-generated JS-code inside Java virtual machine. Accomplishments that we're proud of We are managed to build the complex application which depends on many individually independent components. We accomplish at bringing them together to a working MVP in the small amount of time. What we learned We've learned more about React integration with Spring backend and deploying to a remote server. Also, we’ve managed to work in the loud environment with a lot of people and work as a -T-eam. What's next for This.bank We are going to work on connecting other banks to our service, extend the number of supported API methods and simplify UI/UX to make our product accessible to people without developer background. <div