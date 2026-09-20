---
slug: "galicea-ai"
url: "https://devpost.com/software/galicea-ai"
title: "Galicea AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 631
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Galicea AI

> An AI-powered astronomy chatbot that makes astrophysics accessible to students worldwide, using RAG technology, real-time celestial data, and a conversational interface.

[Devpost](https://devpost.com/software/galicea-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** ollama, python, pytorch

## How they structured the write-up

- inspiration
- what galicea does
- what i learned
- how i built it
- challenges
- accomplishments that we're proud of
- what we learned
- what's next for galicea ai

## Body

Inspiration In 2025, I was sitting in my room in Senegal, asking myself: how can I become the person I want to be, and how can I help my community? I love astronomy deeply, but I struggled to find accessible resources that could help me truly understand it. So I asked myself: why not build something that helps me — and everyone facing the same problem? That moment gave birth to Galicea . The name itself is personal: I created it by combining Alice (one of my closest friends) and Galaxie — Alice + Galaxie = Galicea . What Galicea Does Galicea is an AI-powered astronomy assistant that can: Greet users and remember their name and location Calculate distances between the user and celestial objects Describe planets and define astronomical terms Identify which artificial satellites are currently visible from the user's location in real time Correct errors in user questions Honestly say when it doesn't know something — it never invents answers What I Learned Building Galicea taught me Retrieval-Augmented Generation (RAG) using LangChain, vector storage with ChromaDB, and real-time astronomical calculations using Astropy and the Gaia DR3 database . Star distances are calculated using the parallax formula: $$d = \frac{1}{\pi}$$ where $d$ is the distance in parsecs and $\pi$ is the parallax in arcseconds. How I Built It Before writing a single line of code, I opened my notebook and wrote down everything I wanted Galicea to be and do. Then I organized my schedule, chose my tools, and started building step by step. Tech stack: Python — core language LangChain — RAG pipeline ChromaDB — vector database (14,000+ indexed chunks from scientific PDFs) Groq API + LLaMA 3.3 — language generation HuggingFace Embeddings — semantic search Astropy + Geopy — real-time celestial calculations Streamlit — web interface Challenges The journey was far from easy. I faced package conflicts, mysterious errors, and wrong code lines that took hours to debug. At one point, my computer ran out of storage completely — I could no longer run or even open my program. It was devastating. I stopped coding for months. I was desperate. But I came back. I solved the storage problem by migrating from a local model (Ollama/Mistral) to the Groq API , moving computation to the cloud. My laptop stopped overheating. Galicea came back to life. I built this entirely alone, with no mentor, no formal training — just documentation, trial and error, and a deep desire to build something meaningful for my community. Accomplishments that we're proud of Built a fully functional AI astronomy assistant from scratch, alone, at 17 years old in Senegal with no formal training Indexed 14,000+ chunks from scientific PDFs to create Galicea's knowledge base Integrated real-time celestial calculations using Astropy and the Gaia DR3 database Selected as Finalist in the AI Futures Challenge 2026 by Northeastern University London, awarded a £1,000 scholarship Successfully migrated from a local LLM to cloud-based Groq API, solving overheating and storage issues What we learned How to build a RAG pipeline from scratch using LangChain and ChromaDB How to work with real astronomical data from the Gaia DR3 database How to secure API keys and manage environment variables properly How to structure a complex Python project independently That persistence matters more than perfection — I stopped for months and came back stronger What's next for Galicea AI Adding real-time tracking of artificial satellites using TLE data from CelesTrak and the Skyfield library Expanding the knowledge base with more scientific papers and multilingual support for French and Wolof speakers Deploying Galicea online so students across Africa can access it freely Adding a feature to generate personalized astronomy learning paths based on the user's level and interests Submitting Galicea to more competitions and research programs to grow its impact <div