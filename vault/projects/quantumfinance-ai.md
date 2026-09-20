---
slug: "quantumfinance-ai"
url: "https://devpost.com/software/quantumfinance-ai"
title: "QuantumFinance AI"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 989
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/developer"
  - "substrate/geospatial"
---

# QuantumFinance AI

> Your AI copilot for the stock market. Get instant analysis, news summaries, and trading strategies to make smarter, faster decisions.

[Devpost](https://devpost.com/software/quantumfinance-ai) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[disaster_emergency]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** hp-ai-studio, mlflow, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quantumfinance ai

## Body

Inspiration The world of finance is flooded with data, but the tools to make sense of it all are often too complex or expensive for the average person. I wanted to change that. My goal was to build a single, easy to use platform that uses AI to break down complex market information into clear, actionable insights. I built QuantumFinance AI to give every investor a real strategic advantage. What it does QuantumFinance AI is a complete financial analysis platform powered by Large Language Model AI. Here's are the features: Main Dashboard: Shows you the hot topics driving a stock sector, which companies are gaining momentum, and the overall market mood. AI Stock Research: Gives you a full picture of any stock by creating a single story from many web sources and modeling its future projections. LLM Powered Stock Strategy: Creates trading strategies based on a stock's history. You can get ideas for intraday, weekly, or monthly timeframes. Synthesized News: Keeps you ahead with quick summaries of important news for any company or theme you're watching. Market Sentiment Analysis: Helps you understand the feeling of the market and what's driving it for specific stocks. Automated Risk Identification: Lays out the key risks for a company or sector so you can make safer decisions. Stock Assist: This is your personal finance expert. You can ask it specific questions like, "Summarize Apple's latest earnings report," and get a straight answer, fast. How we built it I built QuantumFinance AI with a local first, security focused approach. That's why I chose HP AI Studio to be the foundation of my work. Backend and Development: The entire backend, built with Python and FastAPI, was developed inside HP AI Studio's containerized environment. This gave me a stable and ready to use workspace with NVIDIA's libraries already set up, which saved a huge amount of time. Deployment and Version Control: I used MLflow inside HP AI Studio for local deployment and to keep track of my models. This made it easy to test new ideas and roll back to an older version if something didn't work. For the live version, the application is containerized, so it's ready for cloud deployment. AI and Models: I used Perplexity Large Language Model API for the momentum dashboard, stock assist, news summary , sentiment analysis, and risk features. This allow me to incorporate A.I with web searching for latest data My Stock Research feature uses Perplexity Deep Research Model pipeline to generate a comprehensive report on requested company using the most up to date information. The Stock Strategy feature uses an Perplexity Deep Reasoning Model with historical market data from AlphaAdvantage API to come up with trading signals. How HP AI Studio Helped Solving a Real World Problem: I used HP AI Studio to build a serious FinTech application from the ground up, showing how it can handle a complex, real world project. A Better Technical Workflow: My process was made much easier by HP AI Studio. I used its containers for stable development and MLflow to manage all my AI models, all while using the power of NVIDIA GPUs. Key Features I Used: Local First Security: Building the tool locally was essential for handling financial data safely and privately. Efficiency and Repeatable Results: The built in tools made my development cycle faster and meant I could easily reproduce my results. NVIDIA GPU Power: Having direct access to GPU acceleration was critical for training my models and making the platform fast. Challenges we ran into My main challenge was not training models, but orchestrating a suite of powerful external APIs to work together seamlessly. Getting a specialized model like Perplexity to provide precise, reliable financial insights requires more than a simple query; it demands meticulous prompt engineering . Crafting and refining the perfect prompts to get structured, accurate data for each feature was a huge task. This is where HP AI Studio became indispensable. I ran my entire FastAPI backend within its stable, containerized environment. This allowed me to rapidly test and debug countless API calls and data pipelines without ever worrying about system conflicts. As I iterated through hundreds of prompt variations, especially for the nuanced sentiment and risk analysis features, keeping track of what worked was critical. HP AI Studio's built-in MLflow integration was a lifesaver. It allowed me to log each prompt version and its resulting output, creating a clear, versioned history that made the entire process manageable and prevented me from losing progress. Without this structured environment, managing the complexity would have been overwhelming. Accomplishments that we're proud of My proudest accomplishment is the sophisticated architecture of QuantumFinance AI, which I was able to design and build as a solo developer entirely within HP AI Studio . The platform acts as a central hub, intelligently routing user requests to the correct specialized AI model and then synthesizing the responses into a simple, clear format. Building this complex system was only possible because of the streamlined and organized workflow the studio provided. What we learned This project taught me a lot about applying AI in the real world of finance. I learned how important a good development environment like HP AI Studio is for keeping a complex project on track. I also got great hands on experience fine tuning language models for finance and building a solid RAG pipeline. Most importantly, I learned that building a tool that people will actually find useful means focusing on the user from start to finish. What's next for QuantumFinance AI I believe QuantumFinance AI is just getting started. Here's what I have planned next: More Data: I plan to add support for international markets, cryptocurrencies, and other alternative data sources. Smarter AI: I will keep improving the models and plan on exploring NVIDIA's NeMo framework to build custom language models for even better financial insights. Mobile App: I will be developing native apps for both iOS and Android. <div