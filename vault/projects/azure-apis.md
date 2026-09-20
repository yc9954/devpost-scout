---
slug: "azure-apis"
url: "https://devpost.com/software/azure-apis"
title: "Azure APIs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 154
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
---

# Azure APIs

> Azure APIs for App Services, Resource Groups and CosmosDB

[Devpost](https://devpost.com/software/azure-apis) · hackathon [[The Postman API Hack]]

## Facets


**stack** javascript, postman

## How they structured the write-up

- inspiration
- what it does
- what's next for azure apis

## Body

Inspiration I needed to add some automated tests to check data in Cosmos so I started to add the CosmosDB REST API into my test runs. I then needed to update values in Cosmos and restart the App Service, so i integrated the Azure REST API for App Services. What it does The collection uses the Azure and CosmosDB REST APIs to give an easy way to perform many handy functions in Azure via Postman. The Authentication requests are handled at a collection level via pre-request scripts, so once you have entered the required keys everything just works. Token Expiry is also integrated handled by these scripts. Some requests also visualise the responses giving an alternative way to view the data. What's next for Azure APIs Currently the collection only contains a fraction of the Azure APIs available, so it would be good to grow the collection as more use cases come up. <div