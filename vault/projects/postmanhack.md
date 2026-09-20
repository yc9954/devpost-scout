---
slug: "postmanhack"
url: "https://devpost.com/software/postmanhack"
title: "Hashalytic"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 458
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/retail_commerce"
---

# Hashalytic

> Use hashdata to understand the trend of the product.

[Devpost](https://devpost.com/software/postmanhack) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[retail_commerce]]

**stack** airtable, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hashalytic

## Body

Testscript to get the hashtag count Response from Instagram Post record to Airtable Result on Airtable Inspiration Because of current pandemic situation, online shopping becomes more important and popular nowadays. However, not everyone especially the traditional owners keen to convert their physical business to an online way. I think the major reason is they do not familiar the relationship between Internet and products marketing. Social media is a powerful tool to do the trend analysis. There should have a tool that provide easy and clear interface for the owner to understand how their product is trending. So that they can set up a corresponding strategy to sell their products and reach the end user easier. What it does It is a tool that can get the count of a specific hashtag on social media. After that, it can display the count number on a table with the product name. So that the user can look at the table to understand which products is trending or is more popular. The table will also show the stock number so the user can know which product they should buy more from the supplier and have an enough stock. How we built it We create a collection in Postman. The collection includes API that retrieve the hashtag count and post the data to Airtable. First, using an API link to get the hashtag count from Instagram. Then, get the count value from the json response in the test script. Set this value to global variable. Reference to the Airtable REST API documentation to create link in the collection. So that user can create, update and delete data in the Airtable. Challenges we ran into The hardest part in this project is to get the authentication token from the social media. Almost all the social media accounts need you create an app to get the token. Some of them like twitter will need to approve the app before we can start on it. Also, we do not have an online shop to test our idea. For example, our initial idea is to do an integration with Shopify. Yet, it needs an account and the free trial only valid in a short period of time. Accomplishments that we're proud of We successfully get the hashtag count from Instagram without using authentication token. Then update the Airtable successfully. What we learned We learnt how to use different social media API and also gain a lot of knowledge in different social media API because of the research. Learnt how to collaborate in Postman is also another significant skill that we learnt. What's next for Hashalytic The next step will be do a proper integration in Shopify. Also, make the collection supports more social media site. <div