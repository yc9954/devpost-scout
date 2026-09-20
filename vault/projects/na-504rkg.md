---
slug: "na-504rkg"
url: "https://devpost.com/software/na-504rkg"
title: "Beacon"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 1064
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# Beacon

> A real-time, cross-domain Customer Happiness Index that detects, tracks, and helps act on customer sentiment for T-Mobile.

[Devpost](https://devpost.com/software/na-504rkg) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[health_clinical]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[transcript_audio]]

**stack** downdetector, figma, flask, forumscout, llama, mongodb, next.js, ngrok, tailwindcss, twilio

## How they structured the write-up

- 🧠 inspiration
- 🎯 what it does
- 🔍 main features
- 🏗️ how we built it
- 🧩 technical challenges
- 🎉 accomplishments and highlights
- 📚 what we learned
- 🔭 what’s next
- 🧾 acknowledgments

## Body

Login Page Central Dashboard Call Center Agent Dashboard Social Campaigns Dashboard Tech Stack 🐶 Beacon Meet Telly, your friendly companion turning customer data into delight. A real-time, multimodal Customer Happiness Index built to detect, understand, and improve how people feel about T-Mobile. 🧠 Inspiration Welcome to Beacon! When thinking about what truly defines the customer experience—and how to transform satisfaction into delight —we focused on three pillars: Detect customer experience in real time. Address feedback in a meaningful, actionable way. Tailor campaigns, offers, and engagement based on what genuinely works for customers. After calling T-Mobile ourselves, we imagined a world where every customer interaction leaves behind a digital heartbeat as a mix of text, voice, and network data. Beacon listens to those signals, learns from them, and empowers teams to act faster, smarter, and with empathy. 🎯 What It Does Beacon is a unified platform that visualizes and improves the customer journey in real time. It detects live sentiment from social media, customer calls, network telemetry, and then connects those signals to personalized recommendations, automated triage, and actionable insights. Telly the Dog (our mascot 🐶) embodies loyalty, alertness, and connection. When customers “bark,” Telly guides teams toward better outcomes. 🔍 Main Features 📡 Real-Time Happiness Index Aggregates sentiment, feedback, and network data to produce a live 0–100 “Happiness Score” by region, service, and location. 🗺️ Interactive Map Dashboard Built with Next.js and TailwindCSS , it visualizes national customer sentiment and emerging issues. 📞 Call Domain: Twilio + Flask Pipeline Twilio captures live customer calls and streams them to a Flask server via ngrok . The Flask server uses Presidio , a lightweight open-source NLP model by Microsoft, to detect and remove all personally identifiable information (PII). Cleaned transcripts are analyzed for sentiment and issue classification using an LLaMA model hosted on the Groq API . Processed data (including issue type, anonymized text, and sentiment) is stored in MongoDB for real-time dashboards. 💬 Social Domain: ForumScout + Downdetector Collects posts from ForumScout API and outage trends from Downdetector . Each post is processed via a LLaMA model for sentiment and emotion detection, creating structured insights. 🐾 Call Agent Dashboard Provides T-Mobile service agents with a real-time, branded view of customer issues while keeping all PII anonymized. Live, PII-Scrubbed Transcriptions: Calls captured via Twilio and scrubbed in our Flask backend are streamed in real time to the front end. Sentiment & Issue Tracking: Displays current sentiment and identified issues as the conversation progresses. Recommended Actions: Suggests resolution paths and relevant resources based on the issue and sentiment. Proactive Awareness: Issues appear immediately on the dashboard, so agents are informed before the customer reaches the queue. 📰 PR & Campaign Dashboard Social media triage organizes posts by priority for rapid review. AI Campaign Generator suggests micro-campaigns based on topic, objective, and location. Supports T-Mobile Tuesday offerings , allowing teams to specify the number of offers and the amount spent per user. 🔐 Auth0 Integration Provides secure, role-based access for employees and partners while protecting sensitive data. 🏗️ How We Built It Architecture Overview Beacon integrates real-time customer feedback, social sentiment, and PR insights into one intelligent system powered by Telly 🐶 , our loyal Un-carrier companion. Backend Flow Twilio → Flask via ngrok tunnel: Calls are transcribed and then streamed to the backend. PII Scrubbing: All PII is removed before any analysis. LLaMA Processing: Anonymized transcripts and social posts are classified for sentiment and issue type. ForumScout & Downdetector: Social posts and service issues are collected and correlated with sentiment trends. MongoDB Atlas: All structured data is stored securely for dashboards. Frontend Flow Built with Next.js and TailwindCSS for a clean, reactive interface. Displays live happiness scores, call logs, social sentiment trends, and PR campaign suggestions. Agents and PR teams can view emerging issues, recommended actions, and campaign planning all in one place. Tech Stack Summary Backend: Flask, Twilio, ngrok, LLaMA, ForumScout API, Downdetector API, MongoDB Atlas Frontend: Next.js, TailwindCSS, Auth0 🧩 Technical Challenges 1. Cross-Domain Data Fusion Synchronizing live call sentiment, forum posts, and outage data required maintaining consistent timestamps and metadata across domains. 2. Real-Time Performance Dashboards update automatically from MongoDB without needing WebSockets or polling, keeping the interface lightweight and fast. 3. Privacy-First NLP Presidio ensures no sensitive data reaches AI models, protecting customers while allowing actionable insights. 4. Sentiment Context Awareness Capturing tone accurately in voice and text was challenging; the LLaMA pipeline interprets context for more reliable sentiment scoring. 🎉 Accomplishments and Highlights ✅ Built a cross-domain customer happiness system in under 24 hours ✅ Real-time visualization of national sentiment from social media and call data ✅ Fully anonymized NLP pipeline using Microsoft Presidio ✅ Integrated Twilio, Groq, ForumScout, Downdetector, and Auth0 in a single platform ✅ Created Telly 🐶 , a mascot representing loyalty, alertness, and customer connection ✅ Aligned with T-Mobile’s Un-carrier values: Love Our Customers. One Team, Together. Dream Big and Deliver. 📚 What We Learned Multi-Source Data Integration: Combining call transcripts, social media posts, and outage data in real time taught us how to structure a system that ingests heterogeneous data efficiently. Data Display & Dashboard Design: Turning diverse signals into actionable insights required careful design choices to ensure the front end communicated trends, sentiment, and issues clearly without overwhelming users. Real-Time Sentiment & Issue Tracking: Processing sentiment and issue classification on live data streams highlighted the importance of latency optimization and structured storage in MongoDB . Cross-Domain Insights: Merging ForumScout social data with Downdetector outage trends showed us how correlations between platforms can reveal emerging problems early. Front-End Responsiveness: Using Next.js + TailwindCSS , we built dashboards that updated dynamically as new data arrived, keeping the experience smooth and intuitive. Hackathon Collaboration: Coordinating backend, ML, and design efforts under a tight timeline reinforced the importance of clear data pipelines, modular architecture, and rapid iteration. 🔭 What’s Next Predictive Churn Alerts: Forecast negative sentiment to prevent escalation. Agent Copilot: Provide live, anonymized context so customers don’t repeat issues. Telly Mobile App: Real-time sentiment and issue insights on mobile. Dynamic Campaign Optimization: Adjust campaigns based on live happiness metrics. Explainable Sentiment: Show why specific emotions or issues are detected. 🧾 Acknowledgments T-Mobile HackUTD 2025 Team Twilio , Flask , ngrok , ForumScout , Downdetector , Auth0 , MongoDB , and Presidio And of course, Telly 🐶 , for reminding us that great customer care always starts with listening. <div