---
slug: "true-insights"
url: "https://devpost.com/software/true-insights"
title: "True Insights"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 544
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# True Insights

> Analyze texts and discover meaningful insights from qualitative data by extracting sentiments and keywords from natural language texts in your monday.com boards.

[Devpost](https://devpost.com/software/true-insights) · hackathon [[monday apps challenge]]

## Facets

**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** aws-lambda, css, dynamodb, html, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for true insights

## Body

Metrics Sentiment Word Cloud Keywords and sentiments Relations Inspiration Businesses have huge amounts of qualitative data coming directly from customers, such as customer tickets, product reviews, survey responses or feedback forms. Analyzing this data is time consuming and requires a lot of work. Our main concern is helping companies understand what their users say about the product or brand. We use advanced Natural Language Processing algorithms to automatically analyze all this data and then show clear charts and visualizations to help you discover new insights and make smart data-driven decisions. What it does It turns qualitative data (plain texts from users) into charts and metrics. Our Monday app provides three features: 1) True Insights Board Widget: A Board View that extracts meaningful insights from texts in a board and presents it using beautiful charts. 2) True Insights Widget: A Widget that extracts insights from any amount of boards and presents. 3) Listen to Twitter Integration: An integration that periodically collects tweets matching your query. When there's a new tweet that matches your query, it creates a new item in a board. You can use either the True Insights Dashboard Widget and Board View with the data you already have on Monday. And you can also optionally use our Listen to Twitter Integration to extend your social listening strategy. This can help you discover insights to: Understand what users like/dislike: Looking at salient keywords and your customers' attitude (sentiment) toward them. You can also easily see what specifically your users care about and what they use your product for. Craft better messaging for your campaigns: Use your customers' own words in your marketing campaigns. Learn what words they use to describe your product. How we built it We built this project using Node.js in the backend and plain JavaScript in the frontend. Our backend is fully serverless, as it leverages AWS Lambda and DynamoDB. Challenges we ran into Initially we tried to store the insights from our natural language processing API in Monday boards, so that the more dedicated users could dig deep down into the data. However, we discovered that this exhausted Monday's rate limits both by performing too many actions and by creating too many items. Additionally, we had plenty of work integrating Twitter into the authorization flow for our Listen to Twitter Integration. Implementing the charts for the widget and board view was relatively simple, but figuring out how to filter the data to extract the most meaningful insights took us a few weeks. Accomplishments that we're proud of We were able to create the widget and corresponding backend that can process thousands of texts in seconds. What we learned We learned how to develop Monday apps We also learned to work with graphql and how to periodically gather tweets from Twitter. What's next for True Insights Besides improving the overall quality of the insights and adding new charts, we saw a lot of potential in customer-specific models. Using our API, we could develop an integration that, when a new Item is created, processes the text and automatically assigns it a category chosen by the user like "sales" or "user experience". This integration would automatically assign a tag to, say, incoming trouble tickets, thus saving a lot of time and effort. <div