---
slug: "newsswipe"
url: "https://devpost.com/software/newsswipe"
title: "NewsSwipe"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 408
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
---

# NewsSwipe

> Swipe Right on News, Left on the Clutter.

[Devpost](https://devpost.com/software/newsswipe) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**domain** [[retail_commerce]]

**stack** amazon-dynamodb, amazon-ec2, docker, flask, gpt, gravitee.io, ios, python, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- exploring api management with gravitee.io
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for newsswipe

## Body

Launch the App Inspiration In today’s fast-paced world, staying informed shouldn't be a hassle. Traditional news platforms are often riddled with obstacles Cookie Consent Pop-ups, Incessant newsletter sign-ups Intrusive ads These distractions chip away at your time and patience. Imagine a news experience where the top stories are not only easily accessible but also presented in a concise, engaging format that respects your time and enhances your understanding. That's the vision we're striving for—a streamlined news service that delivers quality over quantity. What it does NewsSwipe : Get straight to the point with top news stories, trimmed down to just the essentials and enjoy a smooth, scroll-through experience like TikTok, without any annoying ads or headlines getting in your way. We curate and condense news from a variety of sources, employing advanced scrapers and the summarization prowess of GPT to ensure you're informed, not overwhelmed. How we built it Swift for iOS development Gravitee.io as the API gatekeeper Amazon EC2 instances running Docker containers for our application server Brains of the operation—GPT-3.5 Turbo via OpenAI, orchestrated with Flask and CRON jobs for scheduled tasks, which scrapes top articles provided by Google News API Amazon DynamoDB keeps our data structured and accessible. Exploring API Management with Gravitee.io HTTPS endpoints secured with API Keys Entrypoints GET: news/get_top_news POST: news/create POST: news/viewed Endpoint Amazon EC2 instance running flask server. Shows the 3 entrypoints configured on Gravitee API Management platform Challenges we ran into Tackling the steep learning curve of iOS app development for the first time. Navigating the intricacies of publishing our app for beta testing through TestFlight. Accomplishments that we're proud of Successfully launching our first version of the app. Implementing robust security measures for our endpoints with API keys and HTTPS through Gravitee.io. What we learned iOS app creation and the intricacies of Swift. Server management and API security. Content curation and summarization techniques using AI. What's next for NewsSwipe We're not stopping here. Our roadmap includes: Integrating Ads for monetization in way which is not intruisive (separate list item, occurring once between 10-15 articles). Personalization features allowing users to select and follow their favorite topics. Sharing capabilities with deep links to articles to foster app engagement and broaden our user base. A bookmarking option for readers to save articles for later, ensuring they never miss a story that matters to them. Notifications - for keeping up with the latest. Checkout the APP here on Appetize: App Link <div