---
slug: "cognito-uf3rs1"
url: "https://devpost.com/software/cognito-uf3rs1"
title: "Cognito"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 452
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Cognito

> Ask any question about your users

[Devpost](https://devpost.com/software/cognito-uf3rs1) · hackathon [[TreeHacks 2023]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** fastapi, gcp, javascript, openai, python, react, vercel

## How they structured the write-up

- inspiration
- a few example use cases
- what it does
- how we built it
- what we learned
- what's next for cognito

## Body

chat interface to query and work with data dashboard to display extracted data Inspiration Companies lack insight into their users, audiences, and marketing funnel. This is an issue I've run into on many separate occasions. Specifically, while doing cold marketing outbound, need better insight onto key variables of successful outreach while writing a blog, I have no idea who reads it while triaging inbound, which users do I prioritize Given a list of user emails, Cognito scrapes the internet finding public information about users and the companies they work at. With this corpus of unstructured data, Cognito allows you to extract any relevant piece of information across users. An unordered collection of text and images becomes structured data relevant to you. A Few Example Use Cases Startups going to market need to identify where their power users are and their defining attributes. We allow them to ask questions about their users, helping them define their niche and better focus outbound marketing. SaaS platforms such as Modal have trouble with abuse. They want to ensure people joining are not going to abuse it. We provide more data points to make better judgments such as taking into account how senior of a developer a user is and the types of companies they used to work at. VCs such as YC have emails from a bunch of prospective founders and highly talented individuals. Cognito would allow them to ask key questions such as what companies are people flocking to work at and who are the highest potential people in my network. Content creators such as authors on Substack looking to monetize their work have a much more compelling case when coming to advertisers with a good grasp on who their audience is. What it does Given a list of user emails, we crawl the web, gather a corpus of relevant text data, and allow companies/creators/influencers/marketers to ask any question about their users/audience. We store these data points and allow for advanced querying in natural language. video demo How we built it we orchestrated 3 ML models across 7 different tasks in 30 hours search results person info extraction custom field generation from scraped data company website details extraction facial recognition for age and gender NoSQL query generation from natural language crunchbase company summary extraction email extraction This culminated in a full-stack web app with batch processing via async pubsub messaging. Deployed on GCP using Cloud Run, Cloud Functions, Cloud Storage, PubSub, Programmable Search, and Cloud Build. What we learned how to be really creative about scraping batch processing paradigms prompt engineering techniques What's next for Cognito predictive modeling and classification using scraped data points scrape more data more advanced queries proactive alerts video demo <div