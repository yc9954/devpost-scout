---
slug: "customer-service-bot"
url: "https://devpost.com/software/customer-service-bot"
title: "Customer Service Messenger Bot"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 219
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Customer Service Messenger Bot

> Promote customers' services through chatbots.

[Devpost](https://devpost.com/software/customer-service-bot) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets


**stack** glitch, javascript, messenger, node.js, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration I (Ouissal Moumou) had an internship experience where I automated sending product data in batches using the Facebook Marketing API, and I was impressed by how the API is doing a good linking job. Since I was working with the marketing team (despite being in the engineering team), I had access to the social media accounts of the company, and I noticed how the manual customer service was inefficient. It is just recently that I learned about wit.ai from this competition, and where I gathered all these ideas to make a Messenger bot that uses the Facebook Marketing API to suggest products and answer customers' inquiries. I also suggested the idea to my brother, and he was super excited to turn this idea into a project. What it does The customer service bot is a messenger chatbot that answers customers' questions using that data available in the Facebook catalog of the company. How we built it To build the messenger chatbot, we created a new Wit.ai application to handle the NLP part of the project. Then we created a NodeJS application and host it on Glitch. This app serves as a bridge between the messenger app, Wit.ai, and the Facebook catalog. This app also contains the functions that return responses depending on the intent detected by Wit.ai. <div