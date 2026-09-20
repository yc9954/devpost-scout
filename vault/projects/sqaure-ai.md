---
slug: "sqaure-ai"
url: "https://devpost.com/software/sqaure-ai"
title: "Square AI"
hackathon: "Square Developer Hackathon 2023 "
organization: "Square"
winner: true
words: 319
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# Square AI

> Square AI empowers business owners with an advanced tool that use sales data to generate customers psychographic analysis, create new campaigns and product catalogs.

[Devpost](https://devpost.com/software/sqaure-ai) · hackathon [[Square Developer Hackathon 2023]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[retail_commerce]]
**substrate** [[video_visual]]

**stack** chart.js, chatgpt, python, react, speech-to-text, stablediffusion, text-to-speech, typescript

## How they structured the write-up

- what it does
- how we built it
- key features

## Body

Popular Product Analysis Generating a new product Store Customers Store Catalog Store Subscriptions Analysis What it does Square AI empowers business owners with an advanced tool that harnesses the power of sales data to generate comprehensive psychographic analysis of their customers and create new campaigns and product catalogs accordingly. By leveraging this tool, businesses gain valuable insights into popular sales items with its associated customers’ demographics, preferences, interests, lifestyle and trends. Meanwhile, businesses can easily craft personalized marketing campaigns and tailor product catalogs to meet the preferences of their customer segments with one button-click. With this innovative solution, businesses can drive growth, enhance customer satisfaction, and thrive in today's competitive marketplace. How we built it Square APIs used: Catalog Orders Customer Subscription Other APIs: Image generation: Stable Diffusion v2-2-2 Large Language Model: ChatGPT 3.5-turbo Text to Speech: Google Cloud Text-to-Speech Speech to Text: Web Speech API Technologies: React, Typescript, Flask, Python Key Features Popular Product Analysis Count and sort products by numbers sold For each product find the most popular age bucket Run psychoanalysis on the top three popular product's most popular age bucket "Generate a new product" button to create a new product idea taking into account what your top three selling products are, the psychoanalysis on the age bucket demographics your products are popular with. Store Catalog "Generate a new product" button to create a new product idea inspired by your store catalog Store Customers Graphs your customers by age buckets Runs psychoanalysis for all the age buckets Store Subscriptions Analysis Aggregate your subscriptions with numbers sold For each of them, count all the customers to figure out the most popular age bucket. For the top subscription, for its customers we generate a demographic psychographic analysis on the top 3 customer age buckets. At any point in the chat you can ask Square AI questions and it will know the context of the conversation so far. <div