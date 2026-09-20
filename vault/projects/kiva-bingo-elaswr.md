---
slug: "kiva-bingo-elaswr"
url: "https://devpost.com/software/kiva-bingo-elaswr"
title: "Kiva Bingo"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 519
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# Kiva Bingo

> Kiva Bingo gamifies lending to all 76 countries, 15 sectors, and 163 activities Kiva.org facilitates crowdfunded microloans for.

[Devpost](https://devpost.com/software/kiva-bingo-elaswr) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]

**stack** graphql, javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for kiva bingo

## Body

Kiva Bingo! All categories lent to. No Bingo yet: still more categories to lend to with link to next recommended loan Inspiration Kiva.org crowdfunds microloans to low-income communities. I signed up for Kiva as a lender nearly 10 years ago. I did not have much money, but I wanted to see the power of $25. I made a loan and when it was repaid, I made another loan. With each loan, I learned a little bit about another country and the people from it. One of my motivations was to lend to every country, sector, and activity Kiva facilitates loans for. Finding loans in countries, sectors, and activities I had not yet lent to involved opening tens of tabs every time I was ready to relend the repaid loans. I saw that Kiva had an API and the capabilities to make relending faster and easier. What it does Kiva Bingo gamifies lending. It finds loans in the countries, sectors, and activities categories you have not yet lent to. When you have lent to all the countries, sectors, and activities Kiva is currently funding, you hit Kiva Bingo! How I built it Entirely in Postman! First, I created an API definition in Postman. I did a GraphQL introspection query on Kiva's API, converted to GraphQL SDL, and imported the SDL. Then, I created a Postman collection for my project. I wrote the queries and used Postman's test scripts to store relevant request response values as Postman environment variables. The Postman Collection Runner enabled me to run each API request sequentially. The test script for each query ran after the request to fetch and store relevant information in the Postman environment variables. I used the test expections to indicate when a person hit Kiva Bingo. If you have lent to all available loan categories, all tests pass. If there is a category you have not yet lent to, the final test will fail and provide a URL to a loan category you still need to complete. Challenges I ran into Kiva recently replaced its original public REST API with a GraphQL API. Unfortunately, their new GraphQL API does not yet have all of the functionality of its original API. Kiva does not yet support third-party app authentication on its new GraphQL API (but it is coming), so users must extract an OAuth 2.0 Bearer token from Kiva.org using browser developer tools for now. Also, there are some features defined in the public GraphQL documentation that require undocumented features to use, so they cannot actually used yet. Accomplishments that I am proud of Learning how to import a GraphQL API into Postman Learning to use Postman scripts to control flow and Postman environment variables from scripts to pass data between requests in a workflow Hopefully inspiring more people to become lenders on Kiva and to spread opportunity to countries they may not know much about What I learned See "Accomplishments that I am proud of" :) What's next for Kiva Bingo When Kiva offers third-party app authorization, I can turn this into something more accessible to all levels of technical skill. <div