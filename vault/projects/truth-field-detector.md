---
slug: "truth-field-detector"
url: "https://devpost.com/software/truth-field-detector"
title: "Truth Field Detector"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 559
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# Truth Field Detector

> Real-time narrative risk assistant that detects emotional manipulation and misinformation patterns in news, video, and social media using Amazon Nova.

[Devpost](https://devpost.com/software/truth-field-detector) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[media_journalism]]
**user** [[developer]]
  <sub>weak: researcher</sub>
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** amazon-bedrock, amazon-nova-2-lite, amazon-polly, amazon-web-services, canva, flask, github, python, render

## How they structured the write-up

- inspiration in an era where digital narratives are increasingly optimized to bypass human critical thinking, i felt a deep responsibility to empower the individual. manipulation is often subtle, hiding behind emotional triggers and absolutist claims. i was inspired to create a tool that restores human agency — not by judging what is 'true,' but by illuminating the mechanisms of influence. my goal is to turn the 'digital noise' back into a clear field of truth, ensuring that technology serves as a shield for the mind rather than a tool for steering it.
- what it does truth field detector analyzes news articles and text in real time. it detects emotional language, absolutist claims, and missing citations — the three pillars of narrative risk. it delivers a narrative risk score (0–100) through a multilingual analyzer, providing instant visual feedback and natural voice summaries.
- challenges we ran into i initially explored nova 2 sonic for voice, but the bidirectional websocket streaming was incompatible with my architecture — so i pivoted to amazon polly, which provided more stable voice feedback. i also implemented a text-input fallback to bypass scraping blocks on certain news urls, and resolved git branch conflicts between local and remote.
- accomplishments that we're proud of fourteen days ago, i had never touched python. as an independent ai safety researcher, i went from fearing 'skynet' to building two functional ai safety tools in just two weeks — one for amazon nova and one for gemini. i taught myself the full stack because the mission of truth and connection couldn't wait for a manual. i don't just research alignment; i build the tools to enforce it. creating a multilingual analyzer that is live and accessible to anyone in the world is my first step in proving that qualitative research can be translated into scalable code. i am particularly proud of maintaining the focus and rigor to complete this project while navigating extreme real-world constraints and domestic challenges — proving that the mission of ai safety can thrive outside the vacuum of a quiet lab.
- what's next for truth field detector my roadmap includes a browser extension for real-time browsing protection, mobile integration, and expanding the analysis to video and audio streams to combat multimodal misinformation.

## Body

Truth Field Detector — AI-powered narrative risk analyzer built with Amazon Nova Truth Field Detector — paste any news link or text to analyze narrative risk in real time Real-time risk analysis powered by Amazon Nova 2 Lite — HIGH, MEDIUM or LOW risk score with voice feedback Truth Field Detector: Defending Human Perspective in the Age of Narrative Manipulation by Eloisa Flores :-) Inspiration In an era where digital narratives are increasingly optimized to bypass human critical thinking, I felt a deep responsibility to empower the individual. Manipulation is often subtle, hiding behind emotional triggers and absolutist claims. I was inspired to create a tool that restores Human Agency — not by judging what is 'true,' but by illuminating the mechanisms of influence. My goal is to turn the 'digital noise' back into a clear field of truth, ensuring that technology serves as a shield for the mind rather than a tool for steering it. What it does Truth Field Detector analyzes news articles and text in real time. It detects Emotional Language, Absolutist Claims, and Missing Citations — the three pillars of narrative risk. It delivers a Narrative Risk Score (0–100) through a multilingual analyzer, providing instant visual feedback and natural voice summaries. ## How we built it This is a fully functional proof-of-concept powered by Amazon Bedrock. - Analysis: I used Amazon Nova 2 Lite for high-speed, real-time narrative reasoning. -Audio: Natural voice feedback generated via Amazon Polly. -Infrastructure: The Backend was built on Flask, hosted on Render, with auto-deploy from GitHub. -Frontend: A clean, responsive UI designed for immediate user clarity. I used Canva to design the UI/UX (User Interface), then implemented it using Python and CSS. Challenges we ran into I initially explored Nova 2 Sonic for voice, but the bidirectional WebSocket streaming was incompatible with my architecture — so I pivoted to Amazon Polly, which provided more stable voice feedback. I also implemented a text-input fallback to bypass scraping blocks on certain news URLs, and resolved Git branch conflicts between local and remote. Accomplishments that we're proud of Fourteen days ago, I had never touched Python. As an Independent AI Safety Researcher, I went from fearing 'Skynet' to building two functional AI safety tools in just two weeks — one for Amazon Nova and one for Gemini. I taught myself the full stack because the mission of Truth and Connection couldn't wait for a manual. I don't just research alignment; I build the tools to enforce it. Creating a multilingual analyzer that is live and accessible to anyone in the world is my first step in proving that qualitative research can be translated into scalable code. I am particularly proud of maintaining the focus and rigor to complete this project while navigating extreme real-world constraints and domestic challenges — proving that the mission of AI Safety can thrive outside the vacuum of a quiet lab. ## What we learned I learned how Amazon Bedrock manages structured AI responses, the technical foundations of narrative risk metrics, and how to deploy a production-ready AI application from scratch. Most importantly, I learned that "High Agency" is the most powerful tool in any developer's stack. What's next for Truth Field Detector My roadmap includes a Browser Extension for real-time browsing protection, mobile integration, and expanding the analysis to video and audio streams to combat multimodal misinformation. <div