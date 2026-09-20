---
slug: "proofstack-ai-trust-verification-engine"
url: "https://devpost.com/software/proofstack-ai-trust-verification-engine"
title: "ProofStack: AI Trust & Verification Engine"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 698
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# ProofStack: AI Trust & Verification Engine

> ProofStack verifies AI-generated security answers by breaking them into claims, checking each claim against your source files, scoring trust, and producing an audit-ready report with evidence lineage.

[Devpost](https://devpost.com/software/proofstack-ai-trust-verification-engine) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** and, claim-verification, deterministic, local-json-persistence, next.js-15, node.js, openai-api, react-19, trust-scoring, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for proofstack: ai trust & verification engine

## Body

Inspiration I built ProofStack: AI Trust & Verification Engine because I kept running into one uncomfortable truth: in cybersecurity, AI can sound confident even when it is wrong, and confident mistakes are expensive. The turning point for me was simple. Every AI tool could generate an answer, but very few could answer the follow-up question that actually matters in security: “How do I know this is true?” I wanted to build something that does not ask teams to trust AI blindly. I wanted to build a system that earns trust with evidence. That is where ProofStack started: not as a chatbot, but as a verification layer between AI output and real-world decisions. What it does ProofStack takes an AI-generated security answer and turns it into an auditable artifact. In practical terms, it does this: Ingests source files (PDF, TXT, MD) Generates a draft answer Breaks the draft into atomic, verifiable claims Retrieves evidence for each claim Assigns verdicts: Supported / Weak / Unsupported Computes a deterministic trust score (0-100) Produces a verified, safer answer with evidence references Exports a trust report for review and handoff So instead of one long paragraph that “sounds right,” users get a structured report that clearly shows what is proven, what is uncertain, and what should not be shared yet. How I built it I built ProofStack with Next.js 15, React 19, and TypeScript , with API routes orchestrating the full verification workflow. The core verification pipeline is: Sources -> Chunking -> Draft -> Claim Extraction -> Retrieval -> Verification -> Scoring -> Redline -> Report Key design constraints I chose intentionally Domain focus: Cyber/Security (depth over breadth) Claim cap: 12 (readability + latency control) Evidence retrieval: top-3 snippets per claim (signal over noise) Trust score: deterministic and explainable (no opaque scoring) Decision output: HOLD or SAFE TO SHARE Exportable report: markdown artifact for judge/reviewer workflows I also built a Challenge Demo Mode that intentionally injects one false claim, so the system can visibly prove that it catches unsupported output. Challenges I ran into 1) Preventing polished but unverifiable output LLMs can produce fluent answers that feel correct but lack evidence. I addressed this with structured extraction, strict validation, and fallback logic. 2) Balancing rigor and speed A deep verification pipeline can become slow and noisy. I constrained claims and retrieval scope to keep decisions fast and reviewable. 3) Making trust explainable, not abstract A single score is not enough for high-stakes work. I added score explainability and per-claim contribution visibility so users can inspect why the score is what it is. 4) Building for first-time users and judges The product had to be understandable by non-security audiences too. I simplified the UI and kept the mental model clear: claim, evidence, verdict, decision. Accomplishments that I'm proud of Built an end-to-end verification product solo, not just a prompt wrapper Shipped claim-level verification with confidence and explanations Implemented evidence lineage from [E#] references back to source snippets Added deterministic trust scoring with explainable logic Introduced challenge mode for reliable demo contrast Delivered a polished, judge-friendly report artifact flow Most importantly, I built a product that changes AI from “convincing text” to “defensible output.” What I learned This project taught me that in AI systems, trust must be engineered , not implied. I learned that: Structure beats verbosity in high-stakes workflows Explainability increases adoption more than flashy features Constraints make demos and products more reliable Good security UX is about reducing ambiguity under pressure Building this solo also strengthened my product judgment: when time is limited, choose features that improve decision quality, not just novelty. What's next for ProofStack: AI Trust & Verification Engine Near term PDF export and richer report formatting Persistent multi-session history Better support for larger source sets Mid term Multi-domain verification presets Compliance-oriented mappings (SOC 2 / ISO / NIST contexts) Team review workflows around trust reports Long term My vision is for ProofStack to become an AI trust layer that sits between generation and action: Before any AI recommendation is shared externally or acted upon internally, it should be verified, scored, and traceable. That is the standard I am building toward: AI output that is review-ready, auditable, and defensible. <div