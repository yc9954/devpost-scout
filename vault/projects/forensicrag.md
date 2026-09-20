---
slug: "forensicrag"
url: "https://devpost.com/software/forensicrag"
title: "ForensicRAG"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 287
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/legal_justice"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# ForensicRAG

> A production-grade hybrid RAG system and Heretic-LLM that combines vector search, BM25 retrieval, and cross-encoder reranking to analyze 25,000+ legal documents with high precision on Colab's T4 GPU.

[Devpost](https://devpost.com/software/forensicrag) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[legal_justice]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** bge-embeddings, cross-encoders, faiss, flask, google-colab, llama-cpp-python, llamaindex, mistral-nemo-12b, ngrok, python, rank-bm25

## How they structured the write-up

- inspiration
- what i built
- challenges & solutions
- impact & results

## Body

About the Project Inspiration I set out to accelerate the analysis of 25,303 legal documents released by the Jeffrey Epstein House Oversight Committee—a dataset that typically requires months of manual sifting. I saw a unique opportunity to combine a Retrieval-Augmented Generation (RAG) system with a Large Language Model (LLM) to democratize access to these records, providing users with immediate, fact-based insights. What I Built I engineered a Hybrid RAG System specifically optimized for limited GPU resources without sacrificing precision. The Architecture Search Mechanism: A hybrid approach combining Vector search ( FAISS ) and Keyword search ( BM25 ). Precision: Implemented Cross-encoder reranking ( ms-marco-MiniLM ) to refine search results. Inference: Deployed an Abliterated Mistral-Nemo-12B LLM for uncensored, objective responses. Infrastructure: A Flask backend using ngrok for public access, managed by a thread-safe FIFO queue. Technical Optimization To balance accuracy and speed, the system utilizes a weighted scoring function to merge retrieval methods: $$Score_{final} = \alpha \cdot Score_{vector} + (1 - \alpha) \cdot Score_{keyword}$$ This setup allowed me to offload embeddings to the CPU and run the 90MB reranker alongside the 12B model on a single T4 GPU. Challenges & Solutions Challenge Impact Solution Resource Limits Risk of OOM & Kernel crashes on Colab Free Tier. Optimized CPU offloading and memory management. Model Stability Loops & hallucinations in abliterated models. Extensive parameter tuning (Temperature, Top_K, Repeat Penalty). Concurrency Handling simultaneous user requests. Implemented a robust thread-safe FIFO queue. Impact & Results The tool successfully bridged the gap between raw legal data and public curiosity: Reliability: Successfully handled 234 unique users and 372 queries during a 10-hour stress test. Uptime: Achieved zero crashes under heavy load. Demand: Validated by 20+ comments and continuous engagement during the live period. <div