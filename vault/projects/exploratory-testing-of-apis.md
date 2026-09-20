---
slug: "exploratory-testing-of-apis"
url: "https://devpost.com/software/exploratory-testing-of-apis"
title: "Exploratory Testing of APIs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 235
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/web_dom"
---

# Exploratory Testing of APIs

> explore and validate your API responses without developer bias on the tests.

[Devpost](https://devpost.com/software/exploratory-testing-of-apis) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for exploratory testing of apis

## Body

test mock server endpoint with random input Inspiration As developers we are used to test and code what we know and expect from our implementation. This normally leaves a door open to users or attackers that do not follow the expected logic of the API to exploit problems. There are not a lot of tools out there that help make our APIs more robust It is simple to create requests to our API that we know they work using postman. What it does This project is a collection that allows you to define different parameters as an environment (base url, endpoints, schema...) It will iterate through all of them creating random inputs for your endpoints and schemas and make sure there are no server or unexpected error responses. How we built it We use the Test scripts inside a collection. To start the project a mock server was created to mock the expected results. Challenges we ran into The requirement of having a request that actually does not do anything. This would be better as a module from the postman runner itself. Accomplishments that we're proud of Validate whatever API is defined in the configuration What we learned A bit more of the tooling available in the workspace like the mock servers. What's next for Exploratory Testing of APIs Add more replacement placeholders, not only validate rest JSON APIs but also others (xml, ...). <div