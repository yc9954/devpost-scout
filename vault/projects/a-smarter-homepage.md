---
slug: "a-smarter-homepage"
url: "https://devpost.com/software/a-smarter-homepage"
title: "TailorTab"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 552
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
---

# TailorTab

> TailorTab transforms your new tab page into a personal dashboard. Type what you want to see; from World Cup scores to current stock market updates, it appears instantly, updating itself every day.

[Devpost](https://devpost.com/software/a-smarter-homepage) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
  <sub>weak: supply_logistics</sub>
**user** [[developer]]
  <sub>weak: structured_db, web_dom</sub>

**stack** claude, claude-code, cloudflare, coinbase-api, css, espn, github, github.-cloud-services:-cloudflare-workers.-database:-supabase.-apis:-openai, google-news-api, google-news-rss, html, json, json.-platforms:-chrome-extension-manifest-v3, openai-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tailortab

## Body

The "Custom Widget" Page The "Choose Profile" Page Example of a Preset Profile: The "Finance Bro" Page The "Settings" Page novus proof of installation novus dashboard Inspiration Over the last few weeks, important events have been abundant: the World Cup, the NBA finals, the Iranian war, stock market swings, and much more. Like many others, I found myself constantly searching for updates in each event, which was repetitive and time-consuming. So, I created TailorTab: a personalized, live-updating dashboard that generates information widgets from natural language prompts. What it does TailorTab replaces the current Chrome Tab with a custom, AI-powered dashboard to receive any information upon opening a new tab. It does this by generating widgets from natural language. For example, type "show me Steelers news, AAPL and TSLA prices, and the weather in Pittsburgh" and TailorTab parses the intent into separate widgets and lays them out. It features in-built data sources, such as weather and finance APIs, but also features an API-sourcing agent to find and call public APIs on demand to satisfy requests without the user submitting any API keys. How we built it For the frontend, I used React 18 + TypeScript + Vite. In the AI layer, a Cloudflare Workers + Hono backend holds the OpenAI key (gpt-4o-mini) server-side. The data is fetched client-side to comply with Chrome's terms of service. Challenges we ran into Initial user interviews showed some users were unsure what kind of information they should display, so I added the different profile feature, which allows the user to choose different pre-set widget dashboards based on different interests, to give a guide on the extension's capabilities. Additionally, initially, all API requests went through the backend, which was in violation of Google Chrome Developer guidelines, so I changed the API call to the client-side. Finally, another challenge was to account for all query types, from single queries with a single request to single queries with multiple requests. These multi-intent prompts required a different number of widgets, so user testing was necessary to account for all query types. Accomplishments that we're proud of An accomplishment I am proud of is developing an agent that sources live APIs at runtime, not just a fixed set of integrations. This gives the user up-to-date news and also the ability to integrate virtually any information or news into their dashboard. I am also proud that I was able to ship this product as it is available on the Google Chrome store, and I look forward to sharing my work with thousands of potential users. What we learned I learned more about full-stack engineering and the requirements to ship a product end-to-end, especially regarding permissions and system requirements. I also learned more about how to structure the backend such that the product is ready to ship: with special consideration to rate limits, caching, and data collection. What's next for TailorTab The next steps to TailorTab is connect the extension to the user's Google account so they have the ability to sync their Google Calendar, Gmail, and other Google products. Additionally, advertising the product on social media such as TikTok and Reddit would increase the user base and help with user feedback to further enhance the app. In the long run, I also hope to monetize through advertisements or develop a premium model. <div