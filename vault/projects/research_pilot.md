---
slug: "research_pilot"
url: "https://devpost.com/software/research_pilot"
title: "Research_Pilot"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 951
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/legal_justice"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Research_Pilot

> "Turn hours of research into minutes — voice-in, insight-out. A multi-agent AI system using every Amazon Nova model to autonomously research, synthesize, and deliver structured reports."

[Devpost](https://devpost.com/software/research_pilot) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]] [[legal_justice]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[web_dom]]
  <sub>weak: regulation_legal_text, video_visual</sub>

**stack** amazon-nova-2-lite, amazon-nova-2-pro, amazon-nova-2-sonic, amazon-nova-act, amazon-nova-multimodal-embeddings, arxiv-api, asyncio, aws-bedrock, beautifulsoup4, faiss, pydantic, pypdf2, python, streamlit

## Body

Inspiration Every student and researcher knows the pain: you have a complex question, you open twelve browser tabs, spend three hours reading, and still end up with a messy document and no clear synthesis. As second-year CSE students at CVR Global University, we live this problem every week — literature reviews, research assignments, project surveys. We wanted to build something that treats research as a pipeline problem, not a manual task. When we discovered Amazon Nova Act could actually browse the web autonomously, and that Nova 2 Pro had extended thinking for deep reasoning, we realized we had everything needed to automate the entire research workflow end to end. What it does ResearchPilot is a multi-agent AI research automation system that turns a spoken or typed question into a fully cited, structured research report in under 5 minutes. You speak your research question → Nova 2 Sonic transcribes it → the Orchestrator Agent (Nova 2 Pro) decomposes it into sub-tasks → Nova Act autonomously browses Google Scholar, arXiv, Wikipedia, and Google News → Nova 2 Pro reads and analyzes every source including PDFs and charts using multimodal capabilities → Nova Multimodal Embeddings semantically reranks all sources by relevance using FAISS → Nova 2 Pro with extended thinking detects contradictions across sources → the Synthesis Agent produces a 7-section structured report with citations and confidence scores → Nova 2 Sonic reads the executive summary back to you. The output includes a confidence score, automatic human-escalation flag when confidence is low, and the report is exported in Markdown, HTML, and JSON. How we built it We orchestrated five Amazon Nova models into a single coherent pipeline via AWS Bedrock: Nova 2 Pro — Central orchestrator, multimodal document analysis, contradiction detection with 8,000-token extended thinking budget, and final report synthesis Nova 2 Lite — Research planning and structured JSON output (fast and cost-efficient for non-reasoning tasks) Nova 2 Sonic — Voice input (speech-to-text) and voice report delivery (text-to-speech) Nova Act — Browser automation agent that navigates Google Scholar, arXiv, Wikipedia, and news sites using natural language instructions Nova Multimodal Embeddings — Semantic similarity search with FAISS to rerank gathered sources and filter noise before synthesis The backend is pure Python with a ThreadPoolExecutor for parallel agent execution. The frontend is a Streamlit dashboard. Every Nova component has a fallback — the system is fully runnable even without a Nova Act API key using arXiv and Wikipedia REST APIs. Challenges we ran into The hardest challenge was getting the synthesis quality right. Early versions averaged across sources rather than reasoning about them — Nova 2 Pro's extended thinking mode was the breakthrough that enabled genuine contradiction detection instead of bland summarization. Parallel agent coordination was tricky — we had to carefully manage dependencies so the synthesis agent only triggered after all parallel research agents completed, without blocking unnecessarily. We also struggled with Nova Act's structured output parsing across different sites — Google Scholar, arXiv, and news sites all return wildly different DOM structures. We solved this by having Nova Act return natural language descriptions that Nova 2 Lite then converted to structured JSON, rather than relying on strict schema parsing. Finally, managing the context window for synthesis across 8-10 sources required careful chunking and relevance filtering — that's where the Nova Embeddings reranking pipeline proved essential. Accomplishments that we're proud of We're most proud of the contradiction detection feature. No existing research tool actively surfaces disagreements between sources — most just summarize. Using Nova 2 Pro's extended thinking to identify that Toyota claims 2027 production readiness while BloombergNEF estimates 2030+, and explaining why that gap exists, felt like genuine AI reasoning rather than pattern matching. We're also proud of using all five major Amazon Nova models in a single pipeline where each one has a justified, distinct role — not just for the sake of it, but because each model genuinely does what it's best at. Building a production-quality system with confidence scoring, human escalation, parallel execution, fallback architecture, multi-format output, and a Streamlit dashboard in hackathon time as second-year undergraduates is something we're genuinely proud of. What we learned Nova Act's natural language paradigm is transformative. Writing agent.act("Search for X and press Enter") is more maintainable than any CSS selector or scraping approach. It handles JavaScript rendering, pop-ups, and dynamic content automatically. Extended thinking is worth the token cost for synthesis tasks. The quality jump on contradiction detection was immediately noticeable — standard completion glosses over disagreements, extended thinking surfaces them. Nova 2 Lite is underrated. For structured JSON output and planning tasks that don't need deep reasoning, its speed and cost profile make it the right choice. Using Nova 2 Pro for everything would be slower and more expensive. Multimodal embeddings unlock cross-modal semantic search — you can rank an image from a PDF against a text query in the same vector space. That's simply not possible with text-only embeddings. Building agentic systems taught us that reliability > capability — a simpler agent that always produces output beats a sophisticated one that occasionally fails silently. What's next for Research_Pilot Domain-specific modes — medical literature (PubMed), legal research (case law), financial analysis (SEC filings), each with tailored source lists and confidence calibration Zotero and Mendeley integration for one-click citation export into existing research workflows Browser extension that lets you trigger ResearchPilot from any web page you're reading Collaborative research sessions — multiple researchers querying the same ResearchPilot instance and seeing each other's findings in real time University pilot program — we're exploring deploying ResearchPilot at CVR Global University's library system as a student research assistant Real-time streaming reports — instead of waiting for the full pipeline, surface findings as each source is analyzed <div