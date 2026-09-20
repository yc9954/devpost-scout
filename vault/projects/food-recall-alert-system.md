---
slug: "food-recall-alert-system"
url: "https://devpost.com/software/food-recall-alert-system"
title: "Food Recall Alert System"
hackathon: "Azure AI Developer Hackathon"
organization: "Microsoft"
winner: true
words: 533
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/video_visual"
---

# Food Recall Alert System

> The Recall Alert System is designed to integrates data from openFDA and enhances it with Azure AI services to deliver accurate and relevant recall alerts.

[Devpost](https://devpost.com/software/food-recall-alert-system) · hackathon [[Azure AI Developer Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
**user** [[general_public]]
**substrate** [[video_visual]]

**stack** ai, azure, cognitive, nextjs, openai, python, react, storage, table, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for food recall alert system

## Body

Inspiration Food safety is a critical concern, and consumers often struggle to access timely recall information. I wanted to create an intuitive, AI-enhanced system that provides real-time alerts about food recalls, ensuring public health and consumer safety. By leveraging Azure AI, openAI and openFDA data, I aimed to bridge the gap between recall announcements and consumer awareness. What it does The Food Recall Alert System is a web application that: Displays the latest nationwide food recalls. Allows users to search for recalls based on ZIP code, product name, or brand name. Provides enriched recall data with AI-generated summaries, sentiment analysis, and key insights. Sends real-time notifications via email or SMS for subscribed users. Features an admin panel for managing recall data and interactions. How we built it This is a Proof of Concept (PoC) with an emphasis on minimizing cloud costs while ensuring efficiency and trying to leverage hybrid cloud platform Frontend: Developed using React.js with Tailwind CSS for a responsive user experience. Backend: Python-based API hosted on Azure Functions. Data Source: Retrieves recall data from the openFDA API in JSON format. AI Enrichment: Uses Azure AI services for sentiment analysis, key phrase extraction, and entity recognition. Search & Indexing: Implemented with Azure Cognitive Search for fast recall retrieval. Gen AI Summary: Uses GPT-4o to generate consumer-friendly recall summaries. Data Storage: Stores recall summary data in Azure Table Storage for fast retrieval. This will be moved to Cosmos. Hosting: Deployed using Vercel NextJS template. Challenges we ran into Handling Large Data Sets: Efficiently processing and indexing high volumes of recall data. Data Quality: The raw data from openFDA required significant data cleansing before it could be processed effectively by Azure AI. This introduced challenges in structuring and formatting data for accurate entity recognition and sentiment analysis. AI Token Optimization: Reducing token consumption while ensuring meaningful summaries. Real-time Updates: Ensuring recall alerts remain current as new data becomes available. Scalability: Designing the system to handle high traffic loads with Azure's autoscaling capabilities. Accomplishments that we're proud of Successfully integrated AI-powered enrichment, improving recall accessibility. Implemented a fast and scalable search system using Azure Cognitive Search. Designed a user-friendly, responsive UI for better consumer experience. Built a real-time information about recall to inform users of recalls based on their preferences. What we learned Leveraging AI for Data Enrichment: Effectively using Azure AI services to enhance recall data. Optimizing API Consumption: Strategies for minimizing API costs while processing large data sets and batch processing of openAI APIs Improving Search Performance: Techniques for implementing fast and efficient search capabilities. Data Preprocessing for AI: The necessity of data normalization, cleaning, and restructuring to ensure accurate AI processing. What's next for Food Recall Alert System In Progress: Implement email subscriptions to send weekly recall notifications to subscribers. Future Enhancements: Expand Recall Sources – Include drug and medical device recalls alongside food recalls. Mobile App Development – Launch a mobile-friendly version with push notifications. Machine Learning Insights – Implement image-based search, allowing users to identify if a product has been recalled by scanning it. Partnerships – Collaborate with grocery stores and consumer safety organizations to expand reach. Multilingual Support – Enable recall alerts in multiple languages for broader accessibility. <div