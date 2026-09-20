---
slug: "sherlock-n4fikj"
url: "https://devpost.com/software/sherlock-n4fikj"
title: "Sherlock"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 645
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Sherlock

> Connecting the dots for investigative minds.

[Devpost](https://devpost.com/software/sherlock-n4fikj) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: graph_reasoning</sub>
**domain** [[developer_tools]] [[media_journalism]]
  <sub>weak: legal_justice</sub>
  <sub>weak: developer</sub>
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** python, react, vite

## Body

Sherlock Sherlock Web App Inspiration Investigative journalism is one of the most powerful tools for transparency, but it’s also one of the hardest jobs in the world. Reporters juggle huge amounts of unstructured data, struggle with limited resources, and, in many cases, risk their own safety to uncover the truth. The reality? Journalists today are drowning in information —leaked documents, financial records, interviews, and news reports pile up fast. Only 25% of newsrooms have dedicated investigative teams , meaning most journalists are forced to dig through mountains of data alone. The profession is getting more dangerous—2024 saw a record high of 124 journalists killed worldwide. The world desperately needs better tools to help reporters find connections faster, stay organized, and focus on the real work—telling the story. That’s why we built Sherlock. Core Functionality Sherlock is an AI-powered investigative assistant that connects the dots for journalists. Instead of dumping a long list of search results, Sherlock maps information into an interactive, evolving graph, showing how people, events, and documents are connected. Key Features: Graph-Based Story Mapping : A dynamic, AI-generated knowledge tree that visually organizes leads based on specificity and relevance, helping journalists spot hidden connections instantly. AI-Powered Lead Discovery : Sherlock suggests the next steps in an investigation, flagging missing data and recommending what to collect next. Hybrid Data Analysis (Public + Private) : Unlike traditional AI tools that just search the web, Sherlock lets journalists upload private information documents and combines them with public sources for deeper insight. Conversational Data Input : Journalists can chat with Sherlock to add proprietary data—upload files, type notes, and refine leads in real-time. Clean, Intuitive UI : A beautiful, interactive graph-first interface that integrates everything—no more flipping between spreadsheets, notes, and PDFs. How We Built It Sherlock is built on a multi-layered AI system combining LLMs, retrieval-augmented generation (RAG), and knowledge graph structures. Frontend: React + TailwindCSS + Vite Backend: FastAPI for lightweight, fast processing SMTP WebSockets + Twilio for email and phone communication & alerts OpenAI API for reasoning & text-based intelligence Perplexity API for retrieving high-quality, real-time public data Voyage AI, Unstructured, and Weaviate for RAG-based lead expansion Challenges We Faced In the backend, connecting Sherlock to multiple APIs, handling different file formats, and making sure everything talked to each other seamlessly was a massive task. Every new integration introduced new failure points and debugging nightmares. Some APIs also have strict rate limits, which meant we had to get creative with caching, batching requests, and optimizing queries to avoid bottlenecks. For the frontend, there was a steep learning curve in customizing React Flow for real-time graph updates and smooth interactions. In addition, settling on a type system that balanced developer sanity and runtime safety took way longer than expected. Accomplishments That We're Proud Of We started actually hacking around Saturday at noon, and in just over a day, we pulled off a fully functional AI-powered investigative tool with a complex backend, real-time graph UI, and multi-source data integration—a huge feat given the scope. Sherlock dramatically speeds up investigations, cutting hours of manual research into minutes by automatically organizing and expanding leads. Beyond just functionality, we’re proud of how usable and intuitive the final product feels—Sherlock was built with journalists in mind, prioritizing clarity, speed, and seamless interaction over complexity. What's Next for Sherlock? More data sources for better lead expansion – Expanding integrations with news APIs, court records, and financial databases. Integrating more forms of proprietary data – Allowing users to upload data in other forms (text files, audio files, videos) would make the UI even more intuitive and accessible. Community-driven features – Creating a collaborative investigation mode, where teams can track and link findings together. Sherlock isn’t just an AI tool—it’s a revolutionary assistant that empowers investigative journalists to work faster, safer, and smarter. We're excited to see how it can change journalism. <div