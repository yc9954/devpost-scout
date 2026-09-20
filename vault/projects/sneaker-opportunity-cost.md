---
slug: "sneaker-opportunity-cost"
url: "https://devpost.com/software/sneaker-opportunity-cost"
title: "Sneaker Opportunity Cost"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 532
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/structured_db"
---

# Sneaker Opportunity Cost

> Find out how much money you could've made/lost had you not bought your last pair of sneakers. This api enables you to quickly compare your sneaker collection with stocks and crypto.

[Devpost](https://devpost.com/software/sneaker-opportunity-cost) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[transportation]]
**substrate** [[structured_db]]

**stack** airtable, amazon-web-services, api, asyncairtable, awscli, axios, javascript, lambda, marketstack, node.js, nomics, openapi, postman, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sneaker opportunity cost

## Body

Inspiration The inspiration behind this project all began with The Sneaker Database API. A little over a year ago when looking to develop an app in the sneaker industry I realized there wasn't a readily available database that contained sneaker product data. So I developed one. When entering this hackathon I wanted to find a creative way to use the API I built for The Sneaker Database. Since sneakers are used as an investment vehicle in my community I thought it would be cool to compare the value of a sneaker over a given time period with stocks and crypto currencies. Why? Because... Who doesn't love crypto? I wanted to find a fun way to show people in my community that it is possible to build wealth with just a few dollars. What it does It takes a sneaker SKU or list of SKUs and finds their retail value and release date. Using this info, it looks up a static or user supplied list of stocks/crypto currencies and finds their price based upon the sneaker release date(s). Then it calculcates how much money you could've made had you invested in the specified stocks/crypto currencies instead of purchasing the sneakers. I also have an endpoint that reads from Airtable for those people who aren't interested in sneakers or keep their sneaker collection in Airtable. How we built it Technologies used: Node.js AWS (API Gateway, S3, Lambda) Terraform Airtable OpenAPI 3.0 Data Sources: The Sneaker Databse API Nomics API Market Stack API Challenges we ran into The biggest challenge I ran into was creating the closet feature on The Sneaker Database. It was my first time using firebase for authentication and it required more thought/updates to the user journey than I originally expected. Accomplishments that we're proud of I'm proud that I was able come up with a cool idea and develop it. Technology wise, I'm proud that I was able to find a use case for working with Airtable and that I've obtained a better understanding of Postman. I am also super excited about getting a working prototype complete for the closet feature that calculates the portfolio value and opportunity cost of your entire sneaker collection. What we learned I got exposure to Airtable's API and learned it is built using callbacks instead promises. This hackathon helped me to learn the following about Postman: variables (environment and global) enivronments workspaces using pre-request scripts to set variable values in the body of a request create APIs using OpenAPI documentation genrate collections from schemas mock server creation I learned that Firebase is a great tool for enabling auth within an application quickly. I was able to integrate social sign in within my application within minutes. What's next for Sneaker Opportunity Cost Next, I want to build a web application to display the opportunity cost. Once the web application is built, I want to create a prediction model for sneaker valuations. With this model, people can compare their opportunity cost prior to buying sneakers. Ultimately, I want to expand this to more than just sneakers. I want to expand it to everyday expenses, where we can help people identify the opportunity cost of non-essential expenses. <div