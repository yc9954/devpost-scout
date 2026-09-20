---
slug: "nexaflow"
url: "https://devpost.com/software/nexaflow"
title: "NexaFlow"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 393
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# NexaFlow

> Real-time weather + navigation assistant, built for everyday trave

[Devpost](https://devpost.com/software/nexaflow) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: sensor_fusion, voice_speech</sub>
**substrate** [[geospatial]]

**stack** etc, javascript, kiro, nextjs, tailwindcss, typescript, weatherapi

## Body

Inspiration Traveling often comes with uncertainty — “Will it rain on my trip?” “How long will it take to get there?” “Should I leave earlier?” I wanted to create a simple but powerful assistant that combines real-time weather forecasting with navigation, so people can travel smarter and safer. What it does The app has two main features: Chat Assistant – Users can ask questions like “Weather in Nigeria ?” and get both text and spoken responses. Map & Navigation – Users can turn on GPS to detect their current location, set a destination, and see a live Map with real-time distance, ETA, and voice updates every 30 minutes until arrival. It helps travelers make better decisions by combining weather awareness with navigation guidance. How I built it Kiro AI was used to generate much of the base code through structured prompts and specs. Weather Assistant was implemented using Kiro’s spec-to-code approach, with support for both text and voice input/output. Navigation System was integrated using Maps API for live location, routes, ETA, and distance. Voice feedback was added with text-to-speech so users receive spoken updates during trips. The app is modular, with a separate Chat section and a Map section, keeping the user experience clean. Challenges i ran into Getting real-time navigation updates without breaking performance. Handling voice input/output smoothly on mobile devices. Structuring prompts for Kiro so it generated working, production-ready code instead of partial snippets. Ensuring the UI stayed simple while still supporting advanced features like live maps and voice updates. Accomplishments that I'm proud of Successfully combined weather + navigation + voice into one app. Built a clean, working interface with separate sections for chat and maps. Leveraged Kiro to speed up development while still keeping control over customization. Implemented real-time ETA and distance calculations with spoken reminders every 30 minutes. What I learned How to structure clear Kiro prompts/specs to generate reliable code. The power of combining APIs (weather + maps) with voice features to improve user experience. How to balance simplicity and functionality in app design. That even complex ideas can be broken down into small, buildable specs when working with AI-driven tools. What's next for NexaFlow Add offline mode so maps and forecasts work without internet. Support multi-stop trips for better travel planning. Improve personalization based on user habits. Extend alerts and navigation to wearables like smartwatches. <div