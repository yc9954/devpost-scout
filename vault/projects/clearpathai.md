---
slug: "clearpathai"
url: "https://devpost.com/software/clearpathai"
title: "Expungo"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 621
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Expungo

> Making expungement simple and accessible for all.

[Devpost](https://devpost.com/software/clearpathai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[housing_homeless]] [[legal_justice]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[financial_record]] [[regulation_legal_text]] [[structured_db]] [[web_dom]]

**stack** chromadb, fastapi, google-gemini-api, httpx, lang-chain, live-kit-sdk, next.js, open-ai-gpt-4-api, pydantic, python, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for expungo

## Body

Inspiration Our inspiration behind our idea was to make expungement (the process of dismissing an old conviction) easier for people to access. It can be incredibly hard to find information, know what you need, and successfully go through the long official process. Our website asks the user a few simple questions and looks at their court documents to determine if they are eligible for expungement. If they aren't, it suggests next steps for the user to become eligible. If they are, it fills out the forms for them, simple as that. What it does Expungo is an AI-powered platform that simplifies and automates the criminal record expungement process by analyzing uploaded documents to determine eligibility. Users simply upload their court or RAP sheet and review their case directly with Expungo’s live voice agent for personalized, step-by-step guidance. All data is processed entirely in memory — ensuring that sensitive user information remains secure and confidential. How we built it • Frontend: Developed with Next.js 15, TypeScript, and Tailwind CSS for a fast, accessible interface. The design includes a guided multi-step form and responsive layout for both desktop and mobile users. • Backend: Powered by FastAPI with asynchronous endpoints for high-performance handling of PDF uploads, RAG queries, and voice session tokens. Each microservice communicates via HTTPX and uses Pydantic for validation. • Document Intelligence: Implemented Google Gemini (via google-genai) for advanced PDF parsing -- It extracts structured legal data—case numbers, conviction codes, and court details—from scanned RAP sheets. • Legal Reasoning (RAG System): Built with LangChain and ChromaDB , which stores vector embeddings of expungement laws from all 50 states. We use GPT-4 for natural-language reasoning over retrieved statutes to generate personalized eligibility results. • Voice Agent: Created with LiveKit Agents SDK, integrating WebRTC, Silero VAD, and real-time conversation management. This enables users to speak with Expungo’s AI assistant for hands-free legal guidance. • Privacy & Security: All data is processed in-memory only—nothing is stored in external databases. Environment variables manage all API keys, and JWT authentication secures LiveKit sessions. Challenges we ran into • Integrating state-specific expungement laws was difficult. Each state’s statutes, eligibility criteria, and form formats are very different. Making sure our model pulled accurate and recent information from government sources required careful validation. • We had to be precise when extracting legal and government data, and found that even small extraction errors affected eligibility outcomes. • We ran into quite a few technical challenges regarding latency and reliability when we were combining voice input, document OCR, and NLP pipelines. Accomplishments that we're proud of • Successfully built a voice-enabled AI legal assistant that is able to guide users through expungement eligibility checks and generate completed court forms. • Designed a memory system that values privacy, where user data is stored locally in memory instead of databases or external APIs for confidentiality and control. • Integrated multi-state legal logic and document parsing that scales to various expungement statutes. What we learned • This was our first time developing a fully voice-driven agent, and we learned how to manage conversational state, speech-to-text accuracy, and intent recognition. • We gained experience in combining LLM based reasoning with structured legal rules. • We learned a lot about user trust and ethical AI design, especially when working with personal and legal data. What's next for Expungo • Expanding to support additional government and legal services like housing forms, voter registration, and professional licensing reinstatement. • Transitioning from third party LLM APIs to fully self-hosted or open source models for further data privacy. • Partnering with legal aid nonprofits and public defenders to test Expungo in real expungement clinics. • Continuing to refine our voice interface and eligibility logic for more inclusive, multilingual support. <div