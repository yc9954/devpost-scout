---
slug: "juris-gene"
url: "https://devpost.com/software/juris-gene"
title: "Juris-Gene"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 721
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Juris-Gene

> JurisGenie turns legal documents into executable contract state machines with AI extraction, human verification, deterministic execution, and blockchain-backed verification.

[Devpost](https://devpost.com/software/juris-gene) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]]
**user** [[legal_professional]] [[small_business]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** google-gemini-api, lucide-react, monaco-editor, natural-language-processing, next.js, pinecone, radix-ui, react, react-flow, recharts, regexlib, sqlite, tailwind-css, typescript

## How they structured the write-up

- inspiration
- real-world applicability: solves a highly costly b2b problem (contract disputes) with an infrastructure-level solution along with security layer on chain..
- what it does
- 🚀 key features
- how we built it
- key technical challenge
- 🏆 what we're proud of
- what's next

## Body

Overview and Architecture Diagram AI Annotation part for extracting key details of complex contracts (Only things that actually matters). Compliance part for finding what is actually wrong,dangerous in your contracts ex risky clause like payment receipt not given State machine for Showing how the contract evolves over time like active-breached-convicted Knowledge graph shows how everything is connected Blockchain part put necessary details like force majeure implemented after signing in Final Blockchain part makes the contract tamper proof under your case name Cryptographic security layer preventing duplication, and unauthorized modifications done via the third party. Difference shows what are the key details modified, updated and deleted over time like difference of contracts after multiple hearings JurisGenie — AI Contract Intelligence Platform Inspiration Real-World Applicability: Solves a highly costly B2B problem (contract disputes) with an infrastructure-level solution along with security layer on chain.. Contracts today are static PDFs — hard to read, harder to understand A single contract review can take 4–6 hours of manual effort Hidden liabilities and ambiguous clauses often go unnoticed Contract disputes cost businesses over $150 billion globally every year In India, 3 crore+ legal cases are pending — many caused by unclear agreements JurisGenie solves this. Upload any contract. Get structured, verifiable intelligence in minutes. Built entirely solo — product concept, architecture, frontend, backend, AI pipeline, blockchain integration, and security layer. Designed and shipped as a real product, not a demo. What It Does 🚀 Key Features AI Clause Extraction — Automatically identifies parties, obligations, amounts, penalties, and deadlines from any contract https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/annotate Risk & Compliance Analysis — Detects missing obligations, ambiguous clauses, and legal risks with clear explanations https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/compliance Interactive Knowledge Graph — Visualizes relationships between parties, payments, and obligations https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/graph Contract Diff — Compares versions and highlights added, removed, or modified clauses https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/diff State-Based Simulation — Shows how a contract evolves (Active → Breached → Terminated) based on real-world events https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/state-machine Blockchain Verification — Anchors contracts on Ethereum for tamper-proof, immutable proof https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-38/blockchain Execution & Audit Trail — Record events (e.g., delayed payment) and track contract actions transparently https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/execution Security Simulation — Tests contract robustness against tampering and unauthorized actions https://jurisgenie-pro-6ijp.onrender.com/pro/contracts/jg-demo-138/simulate Solves biggest flaw hallucination and unpredictability . How We Built It Frontend — Next.js, React, Tailwind CSS, React Flow (knowledge graph), Monaco Editor Backend — Node.js, Express.js, reverse proxy monorepo architecture AI layer — Google Gemini Pro for clause extraction, semantic reasoning, and hybrid retrieval Search — Pinecone vector search + BM25 keyword retrieval for fast, accurate contract querying Storage — SQLite for persistence, contract hashes for integrity verification Blockchain — Ethereum Sepolia testnet for immutable execution anchoring Production-Grade Observability JurisGenie is built with full real-time monitoring: AI Pipeline Latency: 345 ms Deterministic Engine Execution: 12 ms Blockchain Anchor Time: 8.9 seconds All paths are deterministic and continuously monitored https://jurisgenie-pro-6ijp.onrender.com/pro/system/metrics This level of observability ensures reliability for enterprise use cases in banking, insurance, and legal tech. Key Technical Challenge 🌍 Real User Impact A small business owner I worked with faced a payment dispute over a ₹2,00,000 agreement What seemed simple turned into multiple lawyer visits and hours spent understanding complex documents There was constant uncertainty about what actually went wrong When we ran the same document through JurisGenie, it instantly highlighted the issue — a repayment claim with no supporting proof What took weeks of confusion was understood in minutes This revealed the real problem: not access to law, but clarity of contracts 🏆 What We're Proud Of Built a complete 8-stage pipeline — from document ingestion to blockchain verification — fully working end-to-end, solo Designed a deterministic State Machine where the same contract and same event always produce the exact same outcome Created a compliance system that explains why a rule fails, not just that it fails Developed a Determinism Score that detects ambiguity and quantifies contract risk before it becomes a dispute Built full production-grade observability with real-time monitoring (AI Pipeline: 345ms, Engine: 12ms, Blockchain Anchor: 8.9s) Evolved the product from a simple Quick Analysis + AI Chat mode into a complete 8-layer legal infrastructure after deeply understanding real-world contract pain points. Demo photos below https://drive.google.com/drive/folders/1K9vtnHtHRmizO6XOPJG6Tmf7ENn0EjKb What's Next Smart contract execution hooks generated directly from legal clauses Wallet-based digital signatures (MetaMask integration) Real-time AI-assisted contract negotiation rooms Mobile interface for on-the-go contract review look for funds if got accepted and validated <div