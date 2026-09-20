---
slug: "m-4f2iwy"
url: "https://devpost.com/software/m-4f2iwy"
title: "Edamame"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 682
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/housing_homeless"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Edamame

> AI Clones for Organizational Memory

[Devpost](https://devpost.com/software/m-4f2iwy) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[housing_homeless]]
  <sub>weak: labor_employment</sub>
  <sub>weak: developer</sub>
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[transcript_audio]]

**stack** css, google, gpt-5.3, mem0, next.js, notion, octokit, react, slack, supabase, tailwind, tts, typescript, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for me

## Body

Chatting with My AI Digital Twin Chatting with Co-worker's Digital Twin Onboarding workflow for engineers Off-boarding workflow for James Liu Management insights generation process Management predictions on team stances Edamame - AI Clones for Organizational Memory Inspiration Organizations lose institutional knowledge every day. When someone leaves, years of context walk out the door. When someone joins, they spend weeks piecing together tribal knowledge scattered across Slack, Drive, email, and a dozen other tools. We wanted to build a system that creates digital twin clones of every person in your organization, so their knowledge is always accessible — even when they're not. We see Edamame becoming a simpler database for companies, where the AI clones and knowledge bases can simplify finding information like the reasoning behind past product decisions and the context that normally lives only in people’s heads. Instead of searching across fragmented tools or tracking down the right person, you can simply ask, and the system returns the exact answer with the full context behind it. What it does Edamame creates AI clones of every employee by ingesting their Slack messages, Google Drive docs, Gmail threads, GitHub commits, Notion pages, and Jira tickets. Each clone becomes a queryable digital twin that answers questions grounded in real data with source citations. Clones learn continuously -- every new message, conversation, and document gets absorbed in real-time. It has 4 main features: Clone Chat : Talk to anyone's digital twin in text or voice. Each clone has a distinct personality modeled after its person. A live memory panel shows facts being extracted and stored as you talk. Management Insights : Ask a strategic question and Edamame polls every clone simultaneously, generates per-person stances with confidence scores and evidence, then aggregates into themes. An animated agent network shows the multi-clone query in real-time. Onboarding Briefs : Auto-generates "here's what you need to know" docs for new hires by querying relevant clones for key people, recent decisions, and open risks. Offboarding Handoff Packs : When someone leaves, their clone preserves their knowledge -- ownership areas, unresolved work, key links, and suggested new owners. Additional features: Full voice I/O using Whisper transcription and TTS synthesis Real-time Slack webhook -- clones learn new messages as they're sent Semantic memory search across all data sources Real OAuth integrations with Slack, Google Drive, Gmail, GitHub, and Notion How we built it Frontend: Next.js 16 with React 19 and TypeScript, paired with Tailwind CSS for a Cursor-inspired dark theme. Agent network visualization uses animated SVG particles on bezier curves. Clone Memory: Supabase with pgvector. Unified memories table with type discriminators and source tags. IVFFlat indexing for sub-50ms semantic search. Clone Intelligence: GPT-5.3 with personality-aware system prompts. text-embedding-3-small for embeddings. Continual learning extracts facts from every conversation. Voice: Whisper for transcription, TTS for synthesis. Full spoken conversation with any clone. Integrations: Real OAuth to Slack, Google Drive, Gmail, GitHub, Notion. Live data sync with token refresh. Challenges we ran into Making clones sound like distinct people, not generic chatbots Supabase connection limits when querying all clones simultaneously for CEO insights Embedding dimension bug at 3am (3072-d instead of 1536-d -- slower AND less accurate) Silent OAuth token expiry causing clones to "forget" GDrive knowledge mid-demo Accomplishments that we're proud of Built fully functional AI clones with real integrations, voice I/O, and continual learning in 12 hours Every clone response is grounded with source citations -- no hallucination Continual learning works live: send a Slack message, ask the clone seconds later, get a cited answer All integrations use real OAuth, not mocked data Code from every abandoned pivot shipped in the final product What we learned Personality modeling matters as much as retrieval quality for making clones feel real Real-time webhook learning is what makes a clone feel "alive" vs. static RAG Scope management is one of the hardest hackathon skills What's next for Me Enterprise Deployment: Multi-tenant isolation, SSO/SAML, role-based clone access control Smarter Clones: Temporal reasoning, cross-clone knowledge graphs, clone-to-clone consultation More Integrations: Calendar, meeting transcripts, Linear, Figma, etc. Our futuristic vision: notion-like database for company knowledge, but better :) <div