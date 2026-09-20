---
slug: "boom-6kr2bj"
url: "https://devpost.com/software/boom-6kr2bj"
title: "Boom!"
hackathon: "United Hacks V5"
organization: "Hack United"
winner: true
words: 549
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Boom!

> See what makes your stream Boom! and what makes it bust. Boom! allows inexperienced streamers discover what engages the audience, improving the accessiblity of streaming as a career.

[Devpost](https://devpost.com/software/boom-6kr2bj) · hackathon [[United Hacks V5]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**substrate** [[geospatial]] [[web_dom]]

**stack** fastapi, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for boom!

## Body

Home page Loading screen Average excitement Excitement over time Detailed breakdown Boom! Inspiration The world of content creation is ever growing, but for new streamers, breaking through feels like an impossible challenge. I realized the most important factor that separates newer creators with more experienced ones is not fancy equipment, but an consistently engaging personality. Thus, to succeed in streaming, creators need to know what parts of their stream their audience love and which parts they find themselves bored. Creators might find themselves scrubbing through countless hours of their stream, trying to find the most "hype" moments to learn from. However, traditionally, this process is tedious, inefficient, and a major roadblock to growth, and also what prevents countless childhood fantasies from coming to fruition. I was inspired to improve the accessibility of streaming as a career. I wanted to empower creators by replacing guesswork with data-driven insights. My goal was to build a tool that does the heavy lifting, allowing creators to focus on what they do best: creating. What it does Boom! is an AI-powered web application that analyzes Twitch VODs to find the most exciting moments. A user simply provides a link to a Twitch VOD and sets an analysis interval. Boom! then processes the entire stream and presents a rich, interactive dashboard with: Average Excitement Score: A single, easy-to-understand score from 0-100 representing the stream's overall hype level. Visual Hype Graph: An interactive, beautifully styled line chart that maps the excitement score over time, allowing creators to instantly spot the peaks and valleys of audience engagement. Detailed Breakdown Table: A timestamped log for each interval of the stream, featuring the specific excitement score, an AI-generated "vibe" of the chat (e.g., "Hyped," "Funny," "Focused"), and a 1-2 sentence summary of what the chat was talking about. How we built it Frontend Framework: React. This is a single-page application (SPA) built in React for quick and responsive UI. Backend Framework: FastAPI, Python. FastAPI efficiently communicates with the frontend. AI/LLM Services: Google Gemini 2.5 Flash-Lite Preview 06-17. This model balances speed with consistency and accuracy. Twitch Chat Logs: chat-downloader, twitch-python. Accessing the Twitch API with Python. Challenges we ran into LLM Issues: Choosing the correct Gemini model for Boom! required hours of trial and error. For example, while the 2.5 Pro model is incredibly smart and powerful, its latency is more than ten times that of the 2.5 Flash-Lite Preview model I finally decided on. Getting Twitch Chat Logs: While the Twitch API does not provide any tools for accessing the chat logs of VODs, the chat-downloader python library does. However the Twitch API still had to be used in order to get details about the streamer and stream (name, description). Accomplishments that we're proud of Building a full-stack application from scratch over one day Integrating Google GenAI and accessing the Twitch API Creating a unique aesthetic and animated UI for not just the website but the Boom! brand What we learned Full stack development The newest LLM model is not always the best for every scenario. What's next for Boom! Allow user accounts: Create an average excitement score over time graph, allowing creators to track their progress in becoming more engaging with their audience Expanding to Youtube, Kick, and other streaming platforms to reach a wider audience <div