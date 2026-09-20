---
slug: "payhere-sri-lanka-integration-testing"
url: "https://devpost.com/software/payhere-sri-lanka-integration-testing"
title: "PayHere Sri Lanka - Integration Testing"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 164
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/web_dom"
---

# PayHere Sri Lanka - Integration Testing

> Easy integration testing for your existing PayHere Integrations.

[Devpost](https://devpost.com/software/payhere-sri-lanka-integration-testing) · hackathon [[The Postman API Hack]]

## Facets

  <sub>weak: simulation_digital_twin</sub>
**domain** [[finance_payments]]
**substrate** [[web_dom]]

**stack** postman

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Running a Subscription Payment Callback Simulation Important settings in one Postman Environment Inspiration PayHere Payment Services are being integrated by many businesses around Sri Lanka. Even though PayHere hosts its own documentation regarding its services, sometimes those details are not enough to complete the service integration. What it does A set of tools and requests that allow you to test your integrations, learn how to integrate with PayHere REST Services and quickly build HTML components. For example, it is very difficult to test Subscription Cancellation flows. Without knowing exactly what parameters you receive in a Payment Callback (Server-to-server HTTP POST request), you can't determine how you will have to process a subscription cancellation. Are grace periods involved? And what are the statuses I will receive? Resolving such ambiguities and providing an easy way to test and build your PayHere Subscription integration is what this project accomplishes! How we built it Everything was built in Postman, except the few email components written in PHP. <div