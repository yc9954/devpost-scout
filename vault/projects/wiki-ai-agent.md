---
slug: "wiki-ai-agent"
url: "https://devpost.com/software/wiki-ai-agent"
title: "AI-powered Wikipedia Agent"
hackathon: "Build Your Own AI Chat Bot"
organization: "OmVi"
winner: true
words: 508
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "domain/scientific_research"
  - "substrate/web_dom"
---

# AI-powered Wikipedia Agent

> A chatbot application that integrates Google's Gemini API with MediaWiki API (Wikipedia) to provide comprehensive, transparent and explainable AI responses with chain-of-thought reasoning capability.

[Devpost](https://devpost.com/software/wiki-ai-agent) · hackathon [[Build Your Own AI Chat Bot]]

## Facets

**domain** [[media_journalism]] [[scientific_research]]
**substrate** [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** flask, gemini, javascript, lucidreact, mediawiki, pythonanywhere, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wiki ai agent

## Body

Screenshot showing the functionality of our chatbot. Inspiration We were inspired by the need for AI systems that don’t just provide answers but also remain transparent about the information they are providing. Many AI chatbots generate responses without citing sources or detailing their reasoning, leading to concerns about misinformation. By combining Wikipedia’s factual data with Gemini AI’s reasoning abilities, we built a system that delivers both accuracy and explainability—giving users confidence in AI-driven knowledge. What it does Wiki AI Agent: Searches Wikipedia for relevant information using the MediaWiki API Provides context from Wikipedia to the Gemini AI Generates responses with chain-of-thought reasoning Allows users to toggle the reasoning process on or off Offers a clean, user-friendly interface built with React, Tailwind CSS, and shadcn/ui Stores API keys securely in localStorage for ease of use This approach ensures responses are both informative and explainable, making AI more trustworthy and transparent. How we built it We used the following technologies to bring Wiki AI Agent to life: Frontend: React, TypeScript, Tailwind CSS, shadcn/ui State Management & Data Fetching: TanStack Query (React Query) API Integrations: MediaWiki API – for retrieving Wikipedia content Google Gemini API – for AI-generated responses with reasoning Utilities & Libraries: Lucide React (icons), UUID (message tracking), html-entities (Wikipedia content processing) Storage: LocalStorage for securely saving the Gemini API key The application follows a structured process: A user submits a query The system searches Wikipedia via the MediaWiki API If relevant content is found, it’s passed to Gemini AI for reasoning-based response generation The AI generates an answer with step-by-step explanations The response is displayed to the user with an option to toggle reasoning visibility Challenges we ran into Optimizing UI/UX for seamless interaction – Making the reasoning toggle intuitive while keeping the interface clean took some iteration. Ensuring secure API key management – We had to find a balance between user convenience and security while storing API keys. Accomplishments that we're proud of Successfully integrating real-world knowledge from Wikipedia with AI reasoning Building a transparent AI system where users can see how the AI thinks Creating a smooth, modern UI that makes interacting with AI more enjoyable Overcoming API integration challenges Developing a scalable solution that can evolve with more data sources and AI improvements What we learned The importance of AI explainability – Users trust AI more when they see its reasoning API integration best practices – Handling multiple APIs with different response structures efficiently Balancing UI simplicity with functionality – Keeping things user-friendly while adding advanced features Generating chain-of-thought reasoning: Gemini AI generates a response with chain-of-thought reasoning What's next for WIKI AI Agent Expanding beyond Wikipedia – Integrating more trusted knowledge sources (e.g., research papers, news APIs) Improving AI reasoning & customization – Allowing users to tweak the AI’s reasoning style Enhancing the UI – Adding voice input, better response formatting, and interactive elements We believe that AI should be both powerful and explainable, and Wiki AI Agent is just the beginning of this vision! Access our chatbot using the following link https://aashif000.github.io/Wiki_AI_Agent/ <div