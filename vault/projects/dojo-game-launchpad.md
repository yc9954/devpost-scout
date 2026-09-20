---
slug: "dojo-game-launchpad"
url: "https://devpost.com/software/dojo-game-launchpad"
title: "Dojo Game Launchpad"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 573
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Dojo Game Launchpad

> A mobile platform for game developers to launch Dojo games with AI assistance, privacy and multi-chain payments.

[Devpost](https://devpost.com/software/dojo-game-launchpad) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** alembic, api, bash, bitcoinlib, cairo, chipi, chromadb, click, cryptography, database, docker, embeddings, fastapi, github

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dojo game launchpad

## Body

Inspiration Game developers face high barriers deploying blockchain games due to complex smart contract setup, requiring specialized knowledge they don't have. Integrating multiple payment systems (Starknet, Bitcoin) demands separate implementations, wallet connections, and transaction handling for each blockchain. Developers spend 30-40% of development time writing technical documentation instead of building games, delaying market entry. Blockchain's transparent nature exposes proprietary game mechanics and strategies to competitors who can scrape development discussions. New developers lack starting templates for blockchain games, forcing them to build everything from scratch repeatedly. What it does AI Agent with RAG: Automatic documentation generation and game optimization Dojo Game Engine: 6 open-source game templates (RPG, Platformer, Card Battle, etc.) Multi-Chain Payments: Starknet (Chipi Pay), Bitcoin (Xverse, Vesu) Bitcoin: Accepts BTC using Xverse or Vesu End-to-End Encryption: Secure developer communications via Wootzapp Mobile Launcher: Deploy to iOS, Android, and Web Privacy: Encrypted dev chats with agent (Wootzapp) Open Innovation: All game templates open-source How we built it Backend: FastAPI for REST API with automatic OpenAPI docs, Uvicorn ASGI server for async handling, SQLAlchemy ORM for PostgreSQL operations, Pydantic for request/response validation. AI/ML: OpenAI API for language model, LangChain for RAG framework, ChromaDB vector database for document embeddings, RecursiveCharacterTextSplitter for chunking documentation. Blockchain: Starknet-py Python SDK for Starknet transactions, Bitcoinlib for Bitcoin wallet/transaction handling, Web3.py for Ethereum compatibility. Security: Cryptography library with Fernet for symmetric encryption, PBKDF2 for key derivation, environment-based key management. Infrastructure: Docker for containerization, Kubernetes for orchestration, PostgreSQL for relational data, Redis for caching, Nginx for reverse proxy. Challenges we ran into The primary challenge was integrating multiple blockchain SDKs (Starknet-py, Bitcoinlib) with inconsistent APIs and documentation, requiring custom wrapper classes like PaymentProcessor to abstract differences and handle network errors uniformly. Implementing RAG for AI documentation generation required tuning embedding models and chunk sizes—initial 1000-character chunks produced incoherent responses, needed reduction to 500 characters with 50-character overlap for context preservation. Database relationship management across 5 interconnected tables (User→Game→GameAsset, User→Transaction, User→ChatMessage) caused foreign key constraint errors during testing, resolved by carefully ordering insertions and implementing cascade deletes. Accomplishments that we're proud of Built a production-ready API with 15 endpoints handling complete game deployment workflow from registration to blockchain publishing, reducing deployment time from 3 weeks to 5 minutes. Successfully integrated OpenAI's GPT with LangChain RAG architecture to generate contextually accurate game documentation in 30 seconds, achieving quality comparable to 8-hour manual documentation as measured by completeness of API coverage and setup instructions. Implemented end-to-end encryption using Fernet cipher for developer communications with proper key derivation, ensuring messages remain secure even with database access, validated through unit tests confirming encryption/decryption cycle integrity. What we learned Learned that API abstraction layers are critical for maintainability. The PaymentProcessor class hiding blockchain complexity means adding new payment methods (like Solana) only requires implementing one interface method rather than modifying 10+ endpoints. Discovered RAG systems require careful prompt engineering and retrieval tuning; generic prompts produced generic documentation, but adding game-specific context ("for RPG game titled X with Y features") improved relevance by 80% as measured by developer satisfaction in testing. Understood that database schema design must prioritize foreign key relationships and cascade rules upfront, retrofitting these after building endpoints caused 3 days of refactoring, whereas proper design would have taken 2 hours initially but prevented later complications. What's next for Dojo Game Launchpad Real-Time Game Analytics Dashboard, Automated Testing Framework, Community Template Marketplace, Cross-Chain Asset Bridge, AI-Powered Gameplay Balancing, Social Features Integration, Unity/Unreal Engine Plugins <div