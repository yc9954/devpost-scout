---
slug: "citadelle-cortex"
url: "https://devpost.com/software/citadelle-cortex"
title: "Citadelle Cortex"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 516
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Citadelle Cortex

> An autonomous AI swarm powered by Amazon Nova Act that navigates legal & financial databases (SEC, Oyez, CourtListener) to synthesize exportable Master Dossiers.

[Devpost](https://devpost.com/software/citadelle-cortex) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]] [[legal_justice]] [[mental_health]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** amazon-bedrock, amazon-nova, boto3, express.js, node.js, python, react, tailwind.css, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for citadelle cortex

## Body

The Citadelle Cortex landing page. Users type or speak their legal research goal to deploy the autonomous AI swarm. Live Bedrock stream. Three Nova Act browser agents execute parallel workflows while users monitor their real-time thought processes. The synthesized analysis. Nova 2 Lite digests the cross-referenced intelligence to generate a cohesive, trial-ready legal narrative. Sources featuring Semantic Relevance Scores calculated by Nova Embeddings, and the Nova 2 Sonic Voice Orb for interactive audio briefings. The final exportable Master Dossier (PDF/DOCX). Gives litigators a formatted, court-ready document with cited sources and AI synthesis. Inspiration Litigators and trial attorneys spend countless billable hours manually searching siloed databases (court records vs. SEC financial filings) using rigid keyword searches to build their arguments. We realized that true legal intelligence for the courtroom requires semantic cross-referencing to find hidden connections. The goal was to build a system where a single voice prompt deploys a swarm of autonomous agents to do 10 hours of trial preparation and case research in minutes. What it does Citadelle Cortex deploys three simultaneous browser agents (using Nova Act) to independently navigate SEC EDGAR, Oyez, and CourtListener. It extracts the relevant documents, uses Amazon Nova Multimodal Embeddings to calculate a semantic relevance score across the different sources, and uses Nova 2 Lite to synthesize a "Master Dossier." Finally, users can interact with the dossier via a voice-activated orb powered by Nova 2 Sonic. How we built it We built a highly concurrent hybrid architecture. The frontend is React/Tailwind. The orchestrator backend is Node.js/Express communicating via WebSockets. When a user issues a command, Node.js spawns three independent Python child processes running nova-act and boto3. We used Nova Embeddings for the semantic scoring math, Nova 2 Lite for the final text synthesis, and Nova 2 Sonic for the real-time interactive audio. Challenges we ran into Orchestrating a swarm of Python browser agents from a Node.js WebSocket server without blocking the event loop was highly complex. Additionally, transitioning from traditional keyword matching to vector-based semantic relevance scoring required a deep dive into how AI understands conceptual relationships across different industries (e.g., matching financial SEC jargon with Supreme Court legal precedents). Accomplishments that we're proud of I successfully coordinated four distinct Amazon Nova services (Act, Lite, Sonic, and Embeddings) into a single, seamless application. But more importantly, in an industry narrative that claims "SaaS is dead," I proved that SaaS is simply evolving and showcased the shift from passive software (where humans do the clicking) to "Agentic SaaS"—an active, autonomous workforce that executes complex, multi-platform workflows on behalf of the user. What we learned I learned that the true power of AI in law isn't just text generation; it's orchestration. Combining Nova Act's visual browser automation with Nova Embeddings' mathematical semantic matching creates a level of autonomous research that traditional keyword search engines simply cannot compete with. What's next for Citadelle Cortex Expanding the swarm to navigate state-level appellate courts and integrating an "Adversarial AI" mode. This feature will deploy the swarm to intentionally find precedents that contradict the user's case, helping litigators anticipate arguments and prepare for opposing counsel. <div