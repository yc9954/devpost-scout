---
slug: "reclaim-ai"
url: "https://devpost.com/software/reclaim-ai"
title: "FairVal"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 697
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# FairVal

> Your post-purchase autopilot that automatically tracks online price changes and writes emails to give you refunds, returns, and savings.

[Devpost](https://devpost.com/software/reclaim-ai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** claude, react, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fairval

## Body

Inspiration We were inspired by the issue of returns, which is so commonplace for everyday life and for consumers. However, this is an issue that most people don't think about at all. We think that this is the biggest and most accessible opportunity that we can tackle at Cal Hacks to be able to create a real tangible benefit for consumers, especially during an unprecedented cost of living crisis. We also were hoping to explore new use cases for AI tools and public data collection, for example from Bright Data, which could enhance everyday lives in a B2C application interface. What it does FairVal is a consumer facing tool designed to help people save money after their purchase. Currently, customers are allowed to get a rebate on product they've already bought if the price has dropped prior to the return window. However, most people don't know this or completely forget about it. Our tool allows you to scan in your receipts and begin to automatically track the price online for any changes. Once there are any price drops and potential savings, FairVal will notify you and generate a request-for-rebate email for you to send to customer support! How we built it We built our product using TypeScript for a web app, using Next.js and Tailwind CSS for styling. For intelligent data extraction, we integrate Anthropic's Claude AI SDK (claude-3-5-haiku and claude-sonnet models) to perform receipt OCR, return policy analysis, and fallback price scraping when structured data is unavailable. The website is deployed on Vercel, allowing us to schedule daily cron jobs. Web scraping is powered by Bright Data's Scraping Browser via Puppeteer Core, connecting to Bright Data's proxy network for reliable, anti-bot-detection browser automation. This enables real-time price monitoring across major retailers (Amazon, Walmart, Target, etc.) using retailer-specific DOM selectors. Backend services run on Supabase for PostgreSQL database management, authentication, and real-time subscriptions. Form validation is handled by Zod with React Hook Form, while TanStack Query manages server state and caching. The application employs Vercel Analytics for performance monitoring and uses Axios for HTTP requests to external APIs, including Bright Data's dataset triggers for structured product data collection. Challenges we ran into One of the challenges we faced was integrating the Bright Data Web Scraper agent within our website and trying to get the scraper working for as many websites as can for price checking. Accomplishments that we're proud of We haven't used many AI tools before, especially with data collection and integrating a website with the Claude API. We're proud that we were able to create a working product in such a short period of time, and learn how to integrate other tools as well. What we learned One thing we've realised is to keep what you're building simple, especially during a first iteration and especially with such a time crunch. When we were building our product, there was such a temptation to add a whole myriad of new features and integrations to other platforms. However, we learned that for the best reason it is usually to focus a few core features and to execute the product building as best as we can. What's next for FairVal We are beginning to recruit potential alpha users for our platform. Most people we've talked to about this idea will be interested in using it, which is very exciting! We are also planning to add a feature where we could forward receipts, digital receipts, or buy emails or run website emails which could automatically process it and begin tracking instead of having to manually copy or scan receipts. We weren't able to add it to the Cal Hacks iteration because of a lack of time, and the fact that we wanted to focus on getting the core features working. We will also be starting the process to integrate this tool directly within Email platforms such as Gmail instead of having it as a separate website. We were hoping to add this feature in within the hackathon product stage. However, this requires us to integrate within the Google OAuth platform, which has a hard time limit of 4-6 weeks to be approved, which couldn't be fit into Cal Hacks. <div