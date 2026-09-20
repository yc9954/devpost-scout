---
slug: "briefo"
url: "https://devpost.com/software/briefo"
title: "Briefo"
hackathon: "Perplexity Hackathon"
organization: "Perplexity"
winner: true
words: 420
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# Briefo

> Briefo is social media for people who want to stay informed, not distracted. AI-powered summaries and financial insights, and public or private chats. No noise, a social platform with real info.

[Devpost](https://devpost.com/software/briefo) · hackathon [[Perplexity Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** apis, bolt, css, eas, expo.io, github, react-native, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what's next for briefo

## Body

Notifications page for news suggestions, unread chat messages, new friend requests, and friend-request acceptances into a single feed. Deep Research categories to choose from for a company report Ask about various news articles, companies, or anything you want! Perplexity knows your favorite news categories and companies. Profile page, displays name, username, bio, favorite categories and companies, and comments. Can change everything in settings in top right. Article summary, you can like/dislike, share with friends, and use the comment section. Chat with friends or the personalized Perplexity AI Assistant Scroll through an infinite newsfeed with various categories to choose from by clicking the top right. Inspiration Briefo was inspired by Perplexity’s clean, AI-powered news summaries and Reddit’s upvote-driven comment system. Today’s news platforms are either filled with noise or only surface the biggest headlines, usually with dozens of identical articles. Briefo offers a smarter alternative: one feed, no clutter, no bias. What it does Briefo delivers a daily AI-curated feed of real, non-duplicative news stories from trusted sources. It categorizes each story, summarizes it with Sonar, and enables social discussion via comments, likes, and shares. Users can also research companies, tag friends, and even generate deep analysis reports, all from one app. How I built it I used Bolt to scaffold a React Native + Expo frontend, built the app in TypeScript, and set up the backend with Supabase, handling auth, database storage, and edge functions. Those edge functions call the Perplexity API (along with Alpaca and Alpha Vantage) securely to power news summaries, chat, and deep research. Challenges I ran into The biggest challenges were designing system prompts that generated consistent, useful output and implementing API calls securely across different app flows, especially when juggling multiple models and search configurations. Accomplishments that I’m proud of I’m proud of how many distinct ways I integrated the Perplexity API into the app, from daily headlines and summaries to deep company research and contextual chatbot replies. The deep research component, with customizable criteria and detailed output, is a standout. What I learned I learned how to push Perplexity beyond simple prompts, using tools like ‘search_domain_filter’, ‘search_context_size’, and ‘search_recency_filter’ to get highly relevant, controlled results. Each use case benefits from tailored prompting and model choice. What's next for Briefo Next up: I want to deepen the financial features (more context, deeper stock analysis), enhance the social layer with groups and trending topics, and add a payment system so I can sustainably scale API usage. There’s still a lot of potential left to build. <div