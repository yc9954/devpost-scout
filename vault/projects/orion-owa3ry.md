---
slug: "orion-owa3ry"
url: "https://devpost.com/software/orion-owa3ry"
title: "Orion"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 771
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Orion

> The onboarding buddy that's been a part of the team from day 1 to help you build as quickly as possible.

[Devpost](https://devpost.com/software/orion-owa3ry) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** bash, chromadb, css, flask, javascript, npm, postgresql, python, react, scikit-learn, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for orion

## Body

GIF Orion Logo Inspiration Onboarding is a universal pain. Whether you’re an intern or a staff engineer, navigating the codebase is only half the battle: the rest lives in scattered Slack threads, README drift, terminal one-offs, CI logs, and PR history. Context is fragmented, and the first weeks are spent searching instead of shipping. Orion was created to simplify this chaos, serving as a guide to new engineers to get up to speed and stay up-to-date on the project as it evolves. What it does Think of Orion as the teammate who’s been here since day one: it understands the code, the discussions around it, and the PRs that shaped it. Ask a question and Orion answers concisely with references to the particular Slack messages, PRs, docs, and commands it drew from. Beyond summarizing, Orion writes and maintains living documentation. It observes real workflows, turning them into resources engineers can later reference and keeping them up-to-date as the project evolves. Beyond current project status, Orion reveals the story: the choices and trade-offs that led here, guiding what you do next. Additionally, Orion stays live, polling GitHub and Slack every second to ingest new PRs, reviews, merges, and messages as they land. It then incrementally updates Postgres/Chroma so answers and the Reference Timeline are always current. How we built it Vector embeddings -- We used a combination of dense vector embeddings (model: nomic-embed-text) and sparse vector embeddings (TF-IDF) to capture text similarity in different ways. Python + Langchain chunk PRs, Slack threads, docs, and CLI logs so we can then create and store our dense embeddings in ChromaDB, along with metadata like timestamps; we then create the corresponding sparse embeddings with TF-IDF. Data gathering -- Python ingestors call GitHub and Slack APIs, normalize payloads (PRs, diffs, comments, threads), and extract clean text + metadata. The system processes local documentation in the form of PDFs and other existing resources. Additionally, we have a bash script to capture key terminal commands and store those as documentation. The process is dynamic - through polling from the Github and Slack clients along with event driven triggers for PDFs and terminal capture, Orion stays up to date. PostgreSQL Backend storage -- PostgreSQL database holds source artifacts, metadata (owners, timestamps, URLs), and timelines; this database allows the contents of the webpages to be fully dynamic and updated automatically every time Orion gets new data. LLM inference with context -- Once data is gathered and embedded, a user query can be answered by getting the top-k similar documents (based on both dense and sparse embeddings) and providing that as context to an LLM so it can give an informed response. This is standard Retrieval Augmented Generation, but the twist is that the context is dynamic rather than manual. The intelligence of Orion grows with team discussions and project development, making Orion just like another team member. React UI -- React + JS/CSS front end: chat interface to query the LLM and a Reference Timeline that visualizes the exact Slack/PR/doc/CLI sources used with timestamps. Challenges we ran into Scope vs. depth (36 hrs) -- It was hard to balance creating a project that works end-to-end while not getting lost in nitty-gritty. We trimmed scope and tried to iterate fast RAG reliability & hallucinations -- We noticed that early answers drifted from context, and especially when generating docs we faced the common issue of large amounts of context leading to decreased accuracy. To deal with this, we tightened ingestion and data curating to keep outputs grounded. Frontend from scratch -- None of us are experienced in Front-End, so building a clean, futuristic UI took time Latency & model choice -- We tested multiple LLM APIs/local models including Llama3, Gemini, and GPT5; we found that Gemini worked best for us, but creating snappy user response while maintaining high quality LLM responses was a big tradeoff for us. Accomplishments that we're proud of End-to-end in 36 hours -- Built a working RAG pipeline (GitHub + Slack + docs + CLI) with Flask API, ChromaDB vector storage, Postgres to support dynamic webpages, and a React UI Live, cited answers -- Built Orion to return concise guidance with receipts—Slack threads, PRs, docs, and commands—so users are given direct references to guide them on where to dive deeper into project information Futuristic UI -- We designed a clean, futuristic UI that simplifies how users interact with Orion, taking it from beyond just being a chatbot to being a unique visual, learning workspace Always up to date -- Implemented near-real-time polling of GitHub/Slack and incremental re-indexing to keep LLM context fresh What's next for Orion YC. <div