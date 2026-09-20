---
slug: "pcosense"
url: "https://devpost.com/software/pcosense"
title: "PCOSense"
hackathon: "LaunchHacks IV"
organization: "LaunchHacks"
winner: true
words: 436
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "user/clinician"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# PCOSense

> Transforming PCOS Care with AI-Driven Insights .

[Devpost](https://devpost.com/software/pcosense) · hackathon [[LaunchHacks IV]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[agriculture_food]] [[health_clinical]]
**user** [[clinician]]
**substrate** [[code_repository]] [[video_visual]]

**stack** fastapi, firebase, flutter, mongodb, neo4j, ollama

## How they structured the write-up

- 🧠 inspiration
- 💡 what it does
- 🛠️ how we built it
- 🧗 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for pcosense

## Body

🧠 Inspiration Polycystic Ovary Syndrome (PCOS) affects 1 in 5 women in India and remains widely misunderstood. We wanted to build a tool that not only helps manage the symptoms but empowers women with AI-driven insights , personalized care, and a sense of support. Our goal was to create an app that bridges the gap between complex medical data and everyday self-care, especially in a society where such conversations are often silenced. 💡 What it does PCOSense is a smart health companion for women with PCOS that provides: AI-powered cycle prediction and symptom tracking . AI-based food scanner that assesses both cooked and packaged food for PCOS-friendliness using a knowledge graph . Yoga and mindfulness sessions with real-time AI pose matching . Backend intelligence using Neo4j , MongoDB , ChromaDB , and LLM inference for personalized care suggestions. 🛠️ How we built it We used a Flutter frontend and integrated it with: Firebase Authentication for user management. FastAPI backend with Python for inference, data handling, and REST APIs. MongoDB Atlas to store user images, logs, and nutritional records. Neo4j to model dietary relationships and support recommendation queries. ChromaDB to store vector embeddings and perform semantic search on food descriptions and user queries. Google ML Kit and custom ML models for pose detection, OCR, and food analysis. Gemini API and Ollama for large language model (LLM)-based inference. AI tools like ScraperAPI and Hugging Face for structured web scraping and language tasks. 🧗 Challenges we ran into Getting high-quality, structured food data was a major hurdle — we had to scrape data across multiple websites and consolidate inconsistent nutrition and ingredient formats . Designing a knowledge graph and embedding system that supports contextual food recommendations . 🏆 Accomplishments that we're proud of Successfully integrated cooked food and packed food analysis using AI. Created a custom recommendation engine with Neo4j and ChromaDB vector search. Developed a complete end-to-end mobile app with backend and AI workflows . Created a solution that can genuinely improve lives through personalization and empathy . 📚 What we learned How to integrate multiple AI pipelines (food OCR, pose detection, vector search, recommendation) into a mobile workflow. Hands-on experience with Neo4j , ChromaDB , Google ML Kit , Gemini API , and Ollama for inference. Importance of user-centric design when solving sensitive healthcare problems. How to work under pressure as a cross-functional team in a real hackathon environment . 🔮 What's next for PCOSense Enhance the recommendation engine using reinforcement learning and ChromaDB semantic expansions. Incorporate telemedicine APIs for easy doctor consultations. Integrate with wearables for real-time data from fitness trackers. GitHub Repository : https://github.com/Jothika1526/PCOSense <div