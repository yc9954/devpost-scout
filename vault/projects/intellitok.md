---
slug: "intellitok"
url: "https://devpost.com/software/intellitok"
title: "IntelliTok"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 542
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
---

# IntelliTok

> Revolutionize TikTok sales with IntelliTok. An AI-driven CRM that listens, learns, and helps you close. Smart insights, automated tasks, happier clients.

[Devpost](https://devpost.com/software/intellitok) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[transcript_audio]]

**stack** css, google-cloud, openai, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for intellitok

## Body

IntelliTok: Smart Sales Assistant for TikTok Inspiration In learning more about the TikTok Sales workflow, we discovered that representatives juggle multiple clients, spend a significant amount of time completing tedious routine tasks, and struggle to provide real-time, data-driven insights. The fragmented nature of client information, time-consuming meeting preparations, and lack of intelligent support in decision-making were clear pain points. Inspired by the need to streamline workflows and enhance productivity, the TikTok Smart Sales Assistant integrates advanced automation and intuitive design to transform the sales experience. What it does IntelliTok is an AI-powered smart sales assistant designed to streamline TikTok's end-to-end sales process. Key features include: Intelligent CRM Dashboard : Centralizes client information with AI-generated insights and real-time sentiment analysis. Smart Meeting Assistant : Conducts real-time transcription, analysis, and AI-powered suggestions during sales calls. Provides automatic call summarization, highlights action items, and conducts sentiment analysis. Email Integration & Analysis : Provides automatic email summarization, intelligent response suggestions, and sentiment analysis. Performance Analytics : Delivers customizable dashboards with predictive analytics for sales forecasting from multiple perspectives. Client Information Assistant : Enables natural language queries for accessing client data and automated research compilation. Prepare efficiently for sales calls with the chat assistant. How we built it We developed IntelliTok using a robust tech stack: Frontend : Streamlit for the web application, Plotly for data visualization Backend : Python with FastAPI for high-performance APIs AI & ML : OpenAI's GPT-3.5 and GPT-4 models, Google Cloud Speech-to-Text API, and custom-trained models Authentication : Google OAuth Integration : Google Calendar and Gmail APIs Challenges we ran into Real-time Processing : Implementing low-latency transcription and analysis for live meetings. Incorporating streaming input for both microphone and speaker for real-time transcription. Integrating APIs : Implementing the ChatGPT Assistant API was challenging due to insufficient documentation, making it difficult to troubleshoot issues. Additionally, integration with Google REST APIs was difficult due to the complex authentication processes and handling of scopes and responses. Accomplishments that we're proud of Developed a fully integrated, AI-powered sales assistant tailored for TikTok's unique ecosystem. Implemented real-time transcription and analysis capabilities for live sales meetings. Created an intuitive, user-friendly interface that encapsulates complex AI-driven insights. Successfully integrated multiple APIs and services into a cohesive, powerful platform. What we learned We gained valuable experience in working with complex APIs from OpenAI and Google. This process taught us how to effectively interpret API documentation, handle authentication protocols, and manage API requests and responses efficiently. We discovered the importance of fine-tuning API interactions to suit our specific needs. Utilizing Streamlit for our front-end development was a valuable learning experience. We found that it allowed for rapid prototyping and iteration. Its Python-based approach seamlessly integrated with our back-end logic. What's next for IntelliTok Platform Integration : Deeper integration with TikTok's sales platform for real-time campaign insights, particularly for the business insights page. An intelligent BI system should be visible depending on the representative's role in the team. AI Enhancements : Continuous improvement of AI models for more accurate and context-aware suggestions. Expanded Ecosystem : Developing integrations with other popular sales and marketing tools. IntelliTok is poised to transform how sales operations are conducted in the dynamic world of social media platforms, setting a new standard for intelligent, AI-driven sales assistance. <div