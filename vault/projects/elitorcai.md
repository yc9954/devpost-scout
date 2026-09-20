---
slug: "elitorcai"
url: "https://devpost.com/software/elitorcai"
title: "ElitOrcAI"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 712
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ElitOrcAI

> AI-powered clinical decision support that chains vector search, medical imaging, and expert reasoning to provide instant diagnostic assistance for healthcare professionals.

[Devpost](https://devpost.com/software/elitorcai) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
  <sub>weak: multi_agent, realtime_stream, vision_ocr</sub>
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: medical_record</sub>

**stack** cohere, mastra, tidb, typescript

## Body

Home Page Chat Page Conversation Screen What Inspired Me The healthcare industry processes overwhelming amounts of complex data daily - from medical images to patient histories to research literature. I was inspired by the potential to create an AI agent that could instantly connect similar clinical cases, analyze medical scans, and provide structured diagnostic guidance, essentially giving every healthcare professional access to a "digital medical consultant" powered by collective medical knowledge. What I Learned Multi-Agent Orchestration : Building complex workflows that chain multiple AI tools together seamlessly Vector Database Integration : Implementing semantic similarity search for medical cases using TiDB Serverless with Cohere embeddings Medical AI Ethics : The importance of providing AI assistance while emphasizing professional medical consultation Mastra Framework : Leveraging modern agent frameworks for building production-ready AI applications How I Built It The architecture follows a 4-step agentic workflow : Medical Image Analysis → Roboflow AI model analyzes uploaded MRI/X-ray scans for abnormalities Vector Similarity Search → TiDB Serverless finds similar historical cases using semantic embeddings Clinical Reasoning → Groq LLM (Llama 3.3 70B) synthesizes findings into structured diagnoses Knowledge Ingestion → New cases are automatically stored with vector embeddings for future similarity matching Technical Stack Frontend : Next.js with TypeScript, Tailwind CSS, and react-markdown for clinical formatting Agent Framework : Mastra 0.12.3 with LibSQL memory and tool orchestration Vector Database : TiDB Serverless with cosine similarity search AI Models : Groq LLM for reasoning, Cohere for embeddings, Roboflow for medical imaging Features : Voice input with speech-to-text, file upload, session management TiDB Integration -- Clinical cases table with vector embeddings CREATE TABLE clinical_cases ( id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), description TEXT, patient_demographics TEXT, diagnosis TEXT, treatment TEXT, embedding_vector VECTOR(1024), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, VECTOR INDEX idx_embedding_vector (embedding_vector) ); // Semantic similarity search implementation const results = await connection.execute( `SELECT id, title, description, patient_demographics, VEC_COSINE_DISTANCE(embedding_vector, ?) as distance FROM clinical_cases ORDER BY distance ASC LIMIT ?`, [JSON.stringify(embedding.embeddings[0]), limit] ); Challenges I Faced 1. Image Data Flow Initially struggled with passing base64 image data through the agent workflow. The LLM was calling tools with placeholder text instead of actual image data. Solution : Explicitly instructed the agent to use exact imageDataUri values from the request context, not placeholder text. 2. Tool Orchestration Ensuring the agent calls all required tools in the correct sequence for comprehensive analysis. Solution : Implemented mandatory workflow instructions that force execution of all three analysis tools for every medical image: Roboflow analysis (first) TiDB similarity search (second) Medical image analysis (third) 3. Clinical Output Quality Balancing AI assistance with medical ethics and providing structured, professional output. Solution : Created standardized clinical assessment format with: Primary diagnosis with confidence levels Differential diagnoses (top 3 alternatives) Recommended workup and treatment Clinical considerations and red flags Professional consultation disclaimers 4. Vector Search Optimization Fine-tuning TiDB vector search with appropriate embedding models and similarity thresholds. Solution : Used Cohere's embed-english-v3.0 model with cosine similarity and optimized query embedding generation for medical terminology. Real-World Impact ElitorcAI demonstrates how multi-step AI agents can augment healthcare decision-making by: Reducing diagnostic time through instant case similarity matching Providing structured clinical assessments with confidence levels Supporting medical education with historical case analysis Enabling voice-driven queries for busy healthcare professionals Democratizing medical expertise by making advanced diagnostic tools accessible Technical Innovation The application showcases the power of agentic AI workflows - moving beyond simple Q&A to complex, multi-step reasoning that mirrors how medical professionals actually work: Analyze images → AI-powered scan interpretation Review similar cases → Vector database similarity search Synthesize findings → LLM-based clinical reasoning Document conclusions → Structured medical reporting Multi-Modal Capabilities Text Input : Natural language clinical queries Voice Input : Speech-to-text for hands-free operation Image Upload : MRI, X-ray, CT scan analysis File Attachments : Medical documents and reports Markdown Output : Professional clinical formatting Future Vision This foundation could scale to support: Specialized medical domains (cardiology, oncology, neurology) Hospital EMR integration for real-time patient data access Emergency medicine support with rapid diagnostic assistance Medical education platforms with case-based learning Telemedicine enhancement for remote diagnostic support Research applications for pattern recognition across patient populations ElitorcAI represents the future of AI-assisted healthcare - where intelligent agents work alongside medical professionals to provide faster, more accurate, and more accessible diagnostic support. <div