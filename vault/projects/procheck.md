---
slug: "procheck"
url: "https://devpost.com/software/procheck"
title: "Procheck"
hackathon: "AI Accelerate: Unlocking New Frontiers"
organization: "Google"
winner: true
words: 854
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Procheck

> Evidence-based medical protocols, instantly

[Devpost](https://devpost.com/software/procheck) · hackathon [[AI Accelerate- Unlocking New Frontiers]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[legal_justice]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** elastic, fastapi, firestore, gemini, react

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges
- impact
- beyond healthcare
- performance metrics
- dataset summary
- conditions covered in the dataset
- acknowledgments

## Body

Home screen chat interface follow up questions & step thread follow up answer followup answer sources ProCheck: AI-Powered Medical Protocol Assistant Inspiration Imagine a doctor in an emergency room searching for "fever from bug bites" — but the official protocol is titled "Malaria Treatment Guidelines." Traditional keyword search fails, wasting precious minutes. This gap between how doctors think and how protocols are stored inspired ProCheck — an AI-driven system that understands medical intent, not just keywords. Using Elasticsearch's hybrid search and Google Gemini AI, it makes clinical knowledge instantly accessible through natural language. What We Built ProCheck is a semantic medical protocol search and checklist generator that helps healthcare professionals find and apply the right information in seconds. Core Technologies Elasticsearch (Hybrid Search) – Combines BM25 keyword matching with vector similarity using Reciprocal Rank Fusion (RRF): RRF Score = ∑(r∈R) 1/(k + rank_r(d)) Ensures documents relevant by meaning or keyword both rise to the top. Google Gemini AI – Generates embeddings, expands queries with medical terminology, and powers conversational answers with citations. FastAPI – Async Python backend handling search orchestration. React + TypeScript – Real-time, type-safe frontend with streaming AI chat. Firebase – Authentication and user data management (saved protocols, chat history). How It Works Query Expansion : Gemini enhances queries with medical terms. Semantic + Keyword Search : BM25 and vector search run in parallel. RRF Fusion : Combines results for optimal precision and recall. Conversational Layer : Users can ask follow-ups or generate checklists — every response includes verified citations. How We Built It Architecture A modern three-tier setup: React frontend → FastAPI backend → Elasticsearch, Gemini AI, Firebase Development Journey Week 1 : Setup core stack and fixed Elasticsearch's new client issues. Week 2 : Implemented hybrid search with Gemini embeddings. Added caching (LRU + Firestore) cutting query latency from 3–5s to under 500ms. Week 3 : Built conversational AI with context summarization to stay within token limits. Week 4 : Optimized UI with react-window for smooth scrolling and optimistic updates for instant feedback. Week 5 : Added document upload with chunked async embedding for large PDFs. Key Learnings Hybrid Search Requires Tuning : BM25 excels for exact terms, vector search for conceptual ones. Proper RRF weighting was crucial. Cache Everything Expensive : Embedding generation added 150ms per query — caching cut latency and API costs by 80%. Balance Context in Chat : Keeping the last three messages plus summaries maintained quality without exceeding limits. Speed Beats Features : Healthcare users prioritized instant, reliable search over UI flair. Challenges Index Mapping Errors : Missing dense_vector field forced zero-downtime reindexing. Chat Race Conditions : Fixed with optimistic UI updates and reconciliation. Auth Failures : Solved by adding Firebase token interceptors to API requests. Rate Limits : Mitigated Gemini's constraints with exponential backoff and jitter. Impact In testing with healthcare professionals, ProCheck cut protocol lookup time from 3–5 minutes to under 10 seconds , improving first-try accuracy from 60% to 85% . Citations boosted trust — users could verify every claim instantly. Where It Helps Most Emergency Medicine : Fast retrieval during critical care. Medical Education : Interactive learning via chat. Research & Telemedicine : Cross-comparison of guidelines and patient-specific checklists. Beyond Healthcare The same hybrid-search architecture can power: Legal research Engineering documentation Scientific literature Regulatory compliance Any domain needing concept-based retrieval benefits from this approach. Performance Metrics Metric Value Search latency 450 ms (cached) Cache hit rate 85% Indexed protocols 130+ Concurrent users 5+ Uptime 99.8% Handles 100+ chat turns smoothly Dataset Summary Total protocols : 134 (infectious, chronic, emergency, pediatric) Sources : WHO, CDC, NHS, MoHFW, AHA, Mayo Clinic Schema : Key Data Type Description (Implied) disease string The specific disease or condition covered (e.g., "Malaria", "COVID-19"). region string The geographical region or country the protocol applies to. year number The publication or effective year of the protocol. organization string The issuing authority (e.g., "WHO", "Ministry of Health"). title string The official title of the protocol or guideline. section string A specific section within the larger protocol (e.g., "Diagnosis", "Treatment"). body string The main content or text of the protocol section. source_url string A URL link to the original source document. last_reviewed string The date the record was last checked or updated. Conditions Covered in the Dataset The dataset encompasses 134 protocol records and over 35 unique diseases/groups , organized into the following categories: Category Conditions Vector-Borne Infectious Malaria, Dengue, Zika, Chikungunya, Yellow Fever Respiratory Infectious COVID-19, Influenza, Tuberculosis, Pneumonia, Measles, Meningitis, Bronchitis Gastrointestinal/Infectious Gastroenteritis, Hepatitis, Sepsis, Urinary Tract Infection Chronic Diseases Diabetes, Hypertension, Asthma, COPD, Obesity, Hypothyroidism Cardiovascular/Emergencies Heart Attack, Stroke, Cardiac Arrest, Angina, Atrial Fibrillation Pediatric Conditions Fever, Dehydration, Asthma, Ear Infection, Food Allergy (children) Other Infectious/General Choking, Burns, Poisoning, Severe Bleeding, Anaphylaxis, Concussion, Seizure Preventive Vaccination Schedule This organization aims for clarity and minimum redundancy across the records. All URLs verified (Oct 2025), no duplicates or private data. Acknowledgments Thanks to Elasticsearch , Google Cloud Gemini , Firebase , shadcn/ui , and the open-source community for enabling this project. ProCheck is open-source under the MIT License — built to make medical knowledge faster, safer, and universally accessible. <div