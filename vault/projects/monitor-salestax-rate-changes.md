---
slug: "monitor-salestax-rate-changes"
url: "https://devpost.com/software/monitor-salestax-rate-changes"
title: "Monitor SalesTax Rate Changes"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 205
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Monitor SalesTax Rate Changes

> What if you can get directly notified when your beloved government updates the sales tax rates so you can just pass down to your customers without having to consult your CPA? Putting sexy in sales tax

[Devpost](https://devpost.com/software/monitor-salestax-rate-changes) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for monitor salestax rate changes

## Body

Inspiration After an invoice bump one month, the customer wanted to know when the tax rate changed. What it does Notify tax rate changes. How we built it Postman collection and a scheduled monitor Challenges we ran into Not being able to persist collectionVariables across monitor-runs using pm.collectionVariables.set() api is hindering the implementation of a monitor. I like the fact that collectionVariables act like a mini key-value db and using it to persist values across different runs helps to compare previous state with current state while running in the desktop app, and this opens up a lot of possibilities to implement solutions that otherwise would have taken a full-blown app to accomplish something so simple and straightforward. I am aware that modifying collections is possible in monitor-runs via postman API. However, that approach calls for extra code as opposed to just using pm.collectionVariables.set() api. If pm.collectionVariables.set() can work across all types of runs, transparently, then it would be epic. If anyone read this far and know a better way to implement a monitor for the above use case, please holler at me. I would love to learn. Thanks, Mahi Accomplishments that we're proud of What we learned What's next for Monitor SalesTax Rate Changes <div