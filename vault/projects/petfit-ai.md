---
slug: "petfit-ai"
url: "https://devpost.com/software/petfit-ai"
title: "PetFit Ai"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 1243
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PetFit Ai

> Compassion Meets AI, Accessible Pet Care for All.

[Devpost](https://devpost.com/software/petfit-ai) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[health_clinical]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** cloudrun, css, django, gcp, google-adk, html, javascript, kafka, orm, python, sql, tidb

## How they structured the write-up

- 🧠 inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- 🚀 what’s next for petfit ai

## Body

🧠 Inspiration The idea for PetFit AI comes from a very personal experience. I have a cat named Chai , and when he was just two months old, he broke his leg one night while playing. I didn’t realize how serious it was, and with no vet available that late at night, I felt helpless and panicked. That moment made me realize how crucial it is for pet owners to have timely guidance and reliable support. Pets can’t tell us what’s wrong, and even small delays in care can change everything. PetFit AI was born to bridge that gap — combining real-time vitals, AI-driven insights, and always-available guidance so no pet parent ever feels that same helplessness. It’s about turning uncertainty into action and love into smarter care. What it does PetFit is a comprehensive AI-powered health monitoring and management system for pets, designed to provide pet owners with actionable insights and real-time health data. It integrates data from a smart pet collar with a sophisticated multi-agent AI system to provide a seamless, interactive experience. The core of PetFit is its ability to analyze pet data, including vitals, audio, and images, to identify potential health issues, suggest remedies, and provide detailed information, all in real time. The web application features dynamic charts and a conversational agent that acts as a single point of contact for all pet-related queries. This ensures pet owners can proactively manage their pet's well-being with a robust, data-driven solution. How we built it We built PetFit on a scalable and robust architecture, with TiDB at the center of our data management strategy. The project's data flow begins with a Kafka Streaming pipeline, which ingests raw pet data from a smart collar. The data is then efficiently sunk into a TiDB table using SQL Sink Integration . To maintain a clean and relevant dataset, we configured TiDB's TTL (Time-to-Live) feature to automatically delete old data. The backend of our web application is powered by the Django Framework , which connects directly to TiDB for ORM management using the django_tidb library. For our multi-agent system, we utilized the Google Agent Development Kit (ADK), which orchestrates the flow between specialized agents. The main petfit_agent acts as a central hub, routing user requests to the appropriate sub-agent. Agent and Tool Breakdown The architecture is centered around the petfit_agent , which acts as the main orchestrator, directing user requests to the appropriate specialized agents. Here's a breakdown of the key agents and the tools they utilize: symptom_remedy_agent : This is a complex agent that manages the entire symptom identification and remediation workflow. It orchestrates a series of sub-agents: rephraser_agent : Rephrases the user's initial symptom description for a richer query. recommender_agent : Uses the get_top_matches tool to perform a hybrid text search (combining full-text search and semantic search ) to find the most relevant matches. finalizer_agent : Interacts with the user to narrow down the recommended symptoms by asking a series of crafted questions. summarizer_agent : Summarizes the matched information in a detailed, easy-to-understand format. symptom_remedy_agent : This agent is dedicated to analyzing audio files uploaded by the user. identify_sound_meaning : Uses a Open Source Google model Yamnet to generate audio embeddings, which are then used for a vector search in the database. get_info_dog_behaviour : Performs a hybrid search and reranks results using Jina AI to provide in-depth information about pet behavior. pet_vitals_info_agent : Provides real-time information about a pet's vital signs. query_information_database : This tool uses the TiDB Chat2Query API to translate natural language questions into database queries, allowing the agent to fetch and present real-time vital data. pet_skin_disease_detection_agent : Specialized in analyzing images of a pet's skin. identify_skin_disease : Performs a semantic search on a pet image table in TiDB to identify potential skin diseases. search_agent : Conducts external research (e.g., Google Search) to provide detailed information on the detected disease. report_generation_agent : Generates reports summarizing a pet's health data and history. pet_python_code_execution : Runs Python scripts to analyze, visualize, and format data into comprehensive reports. TiDB — central role (what we used & why it matters) Vector Search: We store embeddings (audio/image/text) as vectors in TiDB and search for semantic matching (audio→condition, image→disease, text→symptoms). This enabled fast and accurate nearest-neighbor retrieval across modalities. Chat2Query API: The pet_vitals_info_agent uses TiDB’s Chat2Query API to convert natural-language questions into SQL and fetch live vitals from the database — enabling true “ask-your-data” capabilities. TTL (Time-to-Live): We configured TTL on high-frequency telemetry tables so rows older than 15 days are automatically removed — keeping storage and query performance clean without manual ETL. Kafka sink: Kafka ingestion is handled via SQL Sink integration, so collar HTTP producers feed Kafka, which then reliably sinks into TiDB for persistence and real-time analytics. This enabled real-time dashboards and downstream processing. Core components & stacks Database / Storage: TiDB (vector tables, time-series tables, TTL). Streaming: Kafka producers at collar → Kafka cluster → SQL sink → TiDB. Web backend: Django + django-tidb for ORM + REST endpoints (image/audio uploads, chat). Multi-agent system: Google ADK (Agent Development Kit) Embeddings & Ranking: Jina AI for text/image embeddings & reranking; YamNet for audio embeddings. LLM: Gemini 2.0 Flash (agent reasoning, summarization, question generation). Deployment: Docker containers hosted on GCP Cloud Run. Challenges we ran into One of the main challenges was integrating the disparate components of the multi-agent system. We had to ensure a seamless flow between the orchestrator agent and its specialized sub-agents, each with its own specific tools and data requirements. We also faced hurdles in optimizing search performance, particularly for the hybrid text search, to ensure our response times were fast enough for a good user experience. Furthermore, managing the streaming data from Kafka and ensuring it was efficiently ingested into TiDB without data loss required careful configuration of the SQL Sink. Accomplishments that we're proud of We are incredibly proud of building a fully functional, end-to-end system that demonstrates a practical and innovative use of multi-agent AI and a distributed database. The seamless integration of TiDB with various components, from Kafka for data ingestion to our custom agents for complex queries, is a major accomplishment. We are particularly proud of implementing a hybrid text search that combines both Full-Text and Semantic Search , a powerful feature made possible by TiDB's versatility. The real-time dashboard charts, powered by Kafka and TiDB's live data, are also a key achievement that showcases the system's dynamic capabilities. What we learned We gained a deeper understanding of building scalable, real-time applications using a distributed database. We learned how to leverage TiDB's unique features, such as its HTAP (Hybrid Transactional/Analytical Processing) capabilities and its support for multiple data types, including JSON and Vector Search. We also learned how to effectively manage complex AI workflows using a multi-agent architecture and how to handle data streaming from IoT devices into a structured database. 🚀 What’s Next for PetFit AI PetFit AI is just getting started. Our vision is to make pet care smarter, more accessible, and more compassionate for every owner. In the coming months, we aim to: Expand Collar Integrations — support for more smart collars and wearable devices. Deeper Health Analytics — advanced trend detection and early warning systems. Personalized Care Plans — AI-driven diet, exercise, and wellness recommendations. Community Support — connect pet parents to share experiences, tips, and care stories. Our journey is fueled by the belief that pets deserve the very best — and we’re building the tools to make that possible. <div