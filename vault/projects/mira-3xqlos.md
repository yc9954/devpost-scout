---
slug: "mira-3xqlos"
url: "https://devpost.com/software/mira-3xqlos"
title: "Mira Mira on Da Wall"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 726
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Mira Mira on Da Wall

> MIRA is an AI powered smart mirror that helps you decide what to wear and what to buy. "Mira Mira On The Wall..."

[Devpost](https://devpost.com/software/mira-3xqlos) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[vision_ocr]]
**domain** [[retail_commerce]]
**substrate** [[financial_record]] [[video_visual]]

**stack** 11labs-api, cloud-deployment-services, elevenlabs, embedded, firecrawl, google-oauth, google-shopping-apis, heygen, javascript, mcp-server, mediapipe, node.js, openai-api, perplexity-sonar

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mira

## Body

Mira helps you shop and try on clothes in real-time Mira gives you personalized recs based on your data & scraped data diagram Inspiration “Mirror, mirror on the wall… who’s the best dressed of them all?” We realized that we already ask our mirrors questions every day. Does this look good? Is this too formal? Is this giving the right vibe? The mirror never answers. That gap inspired MIRA. We believed that if smart TVs and smart homes are becoming standard, smart mirrors are next. Instead of building another shopping app, we wanted to transform something you already use daily into something interactive. MIRA was born from the idea that your mirror could be your stylist, your honest friend, and your fashion guide all at once. What it does MIRA is an AI powered smart mirror that helps you decide what to wear and what to buy. You stand in front of it and see clothes visually layered onto your reflection. You can get real time styling feedback, personalized recommendations based on your shopping history, emails, and calendar, and direct links to purchase items. At the center is Mira, an expressive assistant with personality who talks to you, gives feedback, and makes the experience feel natural and conversational instead of transactional. How we built it We combined hardware, computer vision, and multiple AI systems into one integrated experience. On the hardware side, we assembled a two way mirror with a vertically mounted monitor behind it and an embedded webcam for real time capture. On the software side: Frontend built with React and a mirror optimized interface Gesture detection using MediaPipe Real time 2D clothing visualization over live video OpenAI powered agent for reasoning and styling ElevenLabs for voice synthesis Google OAuth for secure email scraping MCP server with Poke integration for shopping data Search integrations using tools like Perplexity Sonar and Serp APIs Mobile onboarding app deployed on Vercel We engineered a custom real time animated assistant by dynamically blending emotional states to create a more expressive presence. Challenges we ran into One major challenge was clothing visualization. We initially explored full 3D garment meshing and rendering, but it proved too complex for our timeframe. We pivoted to a 2D overlay system that delivered strong user value while remaining feasible. Another challenge was scraping reliability. Extracting useful signals from emails and calendars—without hallucinating or misinterpreting context—required tightening our pipelines and improving streaming for accuracy and consistency. On the fashion side, the sheer volume of public images made precision critical. We had to give our OpenAI agent very clear instructions on exactly which items to identify, and build structured labels for each category to power accurate, personalized recommendations. Creating emotional presence was also difficult. We needed the assistant to feel expressive and empathetic, not robotic. Accomplishments that we're proud of Successfully assembling the physical smart mirror hardware Getting real time clothing visualization working Integrating voice input and output seamlessly Building an expressive animated assistant that enables lip sync Creating an end to end scraping and recommendation pipeline and feed it to our magic pipe for users to interact with. We are especially proud that the experience feels natural. It does not feel like using an app. It feels like interacting with your reflection. What we learned We learned the importance of prioritization. Not every technically impressive feature belongs in an MVP. We learned that empathy in AI comes from more than intelligence. Voice, timing, and visual expression matter just as much as reasoning. We also learned how complex it is to integrate multiple APIs and systems into one seamless experience. Real time interaction requires careful coordination across hardware, frontend, backend, and AI layers. What's next for Mira Explore full 3D garment rendering and body meshing Improve scraping accuracy and personalization depth (potentially gathering information from diverse sources, such as social media) Develop a more advanced multi agent reasoning system Expand the onboarding phone app for users to manage all information input and output of the smart mirror Refine the mirror specific user interface and gestures and have a personalized interface /avatar for each user who remembers their exact personality type and preferences. Deploy and test with real users in household settings Our long term vision is simple. Smart mirrors will become common in homes. When that happens, MIRA will already be there, ready to style you. <div