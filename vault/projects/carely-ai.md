---
slug: "carely-ai"
url: "https://devpost.com/software/carely-ai"
title: "Carely AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 608
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Carely AI

> A dual-agent WhatsApp CRM that automates customer support and delivers real-time business intelligence for African SMEs — powered by smart RAG and Groq.

[Devpost](https://devpost.com/software/carely-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[housing_homeless]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** chart.js, chromadb, flask, groq, html5, llama-3.1-8b-instant, llama-3.3-70b, mongodb, pypdf, python, whatsapp-webhook-api

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i faced
- what i learned
- what's next

## Body

Inspiration Africa has a unique business landscape. Walk into any market in Nairobi, Lagos, or Accra and you'll find small business owners glued to their phones — not because they want to be, but because WhatsApp is their storefront. Over 90% of SMEs on the continent use it as their primary sales channel, which means the business owner personally handles every customer inquiry, every pricing question, and every complaint. All day. Every day. I built Carely AI because I saw how unsustainable this is. These business owners don't need enterprise software built for Fortune 500 companies — they need something affordable, WhatsApp-native, and intelligent enough to run without a technical team behind it. What It Does Carely AI is a dual-agent CRM platform that plugs into WhatsApp and does two things simultaneously: Agent 1 — Customer Support (RAG Engine) The business owner uploads their PDFs — price lists, FAQs, product catalogues. Carely converts these into vector embeddings stored in ChromaDB. When a customer sends a message, the agent performs a semantic search and responds instantly using the business's own knowledge — 24/7, with no human required. Agent 2 — Business Intelligence Engine Every incoming message is analysed in real time. It receives a sentiment score (−1.0 to 1.0) and is automatically categorised into buckets like Pricing Inquiries , Complaints , or Technical Support . The agent also runs Knowledge Gap Discovery — scanning unanswered queries, cross-referencing them with the existing document base, and recommending exactly which new FAQ documents the business should create. How I Built It Layer Technology Backend Python / Flask AI Inference Groq LPU (ultra-fast) Support Agent Model Llama 3.3-70B-Versatile Analytics Agent Model Llama 3.1-8B-Instant (128K context) Vector Database ChromaDB Primary Database MongoDB PDF Processing PyPDF WhatsApp Integration Webhook API Frontend & Dashboard HTML5, CSS3, Chart.js The architecture is modular — the customer-facing agent, business-facing agent, database layer, and API routes are all fully separated, making the system easy to extend and maintain. Challenges I Faced 1. Balancing Speed vs. Accuracy The customer support agent needed to be accurate, while the analytics agent needed to be fast enough to classify messages in real time without blocking the UI. I solved this by routing each task to the right model — Llama 70B for deep reasoning, Llama 8B-Instant for rapid classification. 2. Background Re-categorisation When a business owner approves a new AI-suggested category, the system needs to scan all historical messages and re-categorise them retroactively. Running this on the main thread would freeze the UI, so I implemented a background threading approach to handle it asynchronously. 3. Context Window Management Managing conversation history for multi-turn WhatsApp dialogues without exceeding token limits required careful context window trimming in the history manager — keeping enough history for coherent replies without bloating each API call. 4. RAG Accuracy on Varied Document Formats Business owners upload PDFs of varying quality — scanned menus, handwritten price lists, formatted brochures. Getting consistent, accurate text extraction and chunking across all these formats required significant tuning of the document processor. What I Learned How to architect a multi-agent AI system where two LLMs work in parallel on the same data stream The power of RAG for grounding LLM responses in real business context How to use ChromaDB for semantic search at the application level The importance of designing for the actual user — a small business owner in Africa who has no time for complex tools What's Next Native WhatsApp Business API integration for full production deployment Voice message transcription and support in Swahili and other local languages A mobile-friendly dashboard optimised for low-bandwidth connections Multi-tenant SaaS architecture to onboard multiple businesses ``` <div