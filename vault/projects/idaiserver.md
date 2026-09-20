---
slug: "idaiserver"
url: "https://devpost.com/software/idaiserver"
title: "Idaiserver / API contract testing"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 192
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# Idaiserver / API contract testing

> API for contract testing. Automate tests against an implemented API, based on a Postman collection.The server provides APIs to execute tests and generate Cucmber reports.

[Devpost](https://devpost.com/software/idaiserver) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[web_dom]]

**stack** cucumber, gcp, java, kubernetes, openapi, spring

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for idaiserver

## Body

Inspiration Inspiration was coming from the need to test an implemented API against its contract. That test should be automated as much as possible. Idaiserver is the solution for that. What it does The test automation is based on a Postman collection. You can use your Postman collection as a contract. You define request and response data by sending requests to a mock server. You save the data including the response data as example data in your test collection. And Idaiserver runs tests against a defined API validating data based on your defined example data. You will get a nice Cucumber report and a Gherkin feature file with the test results. How we built it It is built on Java Spring Boot with API First. It is deployed to GCP with Kubernetes. Challenges we ran into Only time. Accomplishments that we're proud of Nothing special besides the cool idea of this project. What we learned How to get a full version ready in a very limited timeframe. What's next for Idaiserver There are still some features that can be added. Like adding several URLs for testing.. Or uploading several Postman collections. <div