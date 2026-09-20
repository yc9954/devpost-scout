---
slug: "azure-cognitive-services-apis-and-microsoft-bot-framework"
url: "https://devpost.com/software/azure-cognitive-services-apis-and-microsoft-bot-framework"
title: "Azure Cognitive Services APIs and Microsoft Bot Framework"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 243
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Azure Cognitive Services APIs and Microsoft Bot Framework

> The Azure Cognitive Services are essentials to develop a AI chatbot system based on Questions & Answers pairs. Using REST API we present with this collection how to create, train and use the API

[Devpost](https://devpost.com/software/azure-cognitive-services-apis-and-microsoft-bot-framework) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for azure cognitive services apis and microsoft bot framework

## Body

Inspiration The Azure Cognitive Services are essentials to develop a AI chatbot system based on Questions & Answers pairs. We used QNA Maker in various use cases in the past, as part of the the Microsoft Bot Framework , which was quite straightforward (C# libraries are ready for that and part of the Virtual Assistant templates ). Recently we faced a use case, where we developed our own bot based on different frameworks and NLU, but we wanted to still use the QNA Maker services, so we developed our own REST API client for that. Based on that, we present here our Postman collection that should help any chatbot developer to get to know this powerful QNA service from Microsoft, train it, query it, update and so on.. What it does The collection helps you to perform a useful selection to query QNA knowledge base, update and train it, test it (ask a question) and more. How we built it Based on the documentation Challenges we ran into There's a new version of QNA Maker services, a managed service, which has more features. We extended the API collection to use both versions Accomplishments that we're proud of Using the API directly with Microsoft Cognitive Services without using any library or previous code What's next for Azure Cognitive Services APIs and Microsoft Bot Framework We want to extend it to update/query the synonyms database for the questions/answers, and to add more test functions <div