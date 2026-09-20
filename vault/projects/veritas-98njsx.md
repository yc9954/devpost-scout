---
slug: "veritas-98njsx"
url: "https://devpost.com/software/veritas-98njsx"
title: "Veritas"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 661
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Veritas

> Veritas is a Chrome extension that fact-checks YouTube videos in real time. It extracts claims and checks them against sources like Wikipedia, news, and government data, showing results instantly.

[Devpost](https://devpost.com/software/veritas-98njsx) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]] [[labor_employment]] [[media_journalism]] [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[transcript_audio]] [[web_dom]]

**stack** agentverse, chrome, extensions, fastapi, fetch.ai, gemma, javascript, pydantic, python, sqlite, uagents, websockets, wikipedia

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- built with

## Body

Veritas - Truth in Every Claim Veritas — Real-Time Video Fact Checker Inspiration Misinformation spreads fastest through video — a podcast host drops a wrong statistic, a news anchor misattributes a quote, a documentary overstates a figure — and most viewers have no practical way to verify claims in real time. We wanted to build something that sits alongside the video as you watch, automatically catching factual claims and surfacing verdicts backed by real evidence. The goal: make fact-checking as effortless as turning on subtitles. We were also drawn to using autonomous agents for the retrieval and reasoning layer. Fetch.ai's uAgent framework gave us a natural way to isolate the fact-checking pipeline as a self-contained, cacheable agent that could eventually be discoverable and composable with other agents on Agentverse. What It Does Veritas is a minimalistic Chrome extension that fact-checks YouTube videos in real time. Live caption streaming — The extension watches YouTube's closed captions and streams them to a FastAPI backend over WebSocket. Claim extraction — Gemma receives the transcript along with video metadata (title, channel, date, description) and extracts standalone, check-worthy factual claims. Retrieval-augmented fact-checking — Each claim is sent to a Fetch.ai uAgent that first checks a semantic vector cache (Gemini embeddings + cosine similarity), and on a miss gathers evidence from Wikipedia and Google Fact Check Tools, then asks Gemma for a verdict ( true , false , misleading , or needs_context ) with confidence, rationale, and citations. Overlay UI — A dark, modern, expandable panel on the YouTube page shows live verdicts as color-coded cards with clickable timestamps and source links. Ask Veritas — A built-in chat lets users ask free-form questions about the video using recent transcript context. How We Built It Chrome Extension (Manifest V3, vanilla JS) — A content script observes YouTube caption DOM mutations and streams finalized cues to the backend. A background service worker manages WebSocket connections. The overlay UI is injected directly into the page. FastAPI Backend — WebSocket endpoints ingest captions. A per-session orchestrator buffers transcript, extracts claims via Gemma, and dispatches them to the fact-check agent with rate-limit backoff. Fetch.ai uAgent — Registered on Agentverse with automated mailbox provisioning. Handles the full RAG pipeline: embed → cache lookup → evidence retrieval → LLM verdict → cache write-back. The backend communicates with it directly via RulesBasedResolver . Semantic Cache — SQLite with Gemini embeddings and cosine similarity (threshold 0.85), so paraphrased claims like "330 meters tall" and "stands at 330m" hit the same cache entry. LLM — Google Gemma 3 27B IT for claim extraction and verdict judgment. Prompts are tuned to use video metadata for pronoun resolution, cite sources by name, and always commit to a verdict. Challenges We Faced Agentverse mailbox vs. sync messaging — The uAgents SDK's send_sync_message doesn't work through the Agentverse mailbox (which is async). We had to use RulesBasedResolver to route directly to the agent's local endpoint. YouTube caption observation — YouTube reveals captions word-by-word, so we implemented an idle-timeout finalizer to emit each cue exactly once. LLM prompt engineering — Getting Gemma to consistently output valid JSON, avoid hallucinated citations, cite sources by human-readable name, and commit to verdicts required multiple prompt iterations. What We Learned Autonomous agents are powerful for encapsulating retrieval + reasoning, but the gap between "registered on Agentverse" and "reliably receiving sync messages" has real rough edges in the current SDK. Semantic caching with embeddings is remarkably effective — paraphrased claims hit the cache at a high rate, cutting redundant API and LLM calls. Video metadata as LLM context massively improves claim extraction. Without it, the model can't resolve "he" or "this policy" to anything meaningful. Built With Frontend : Chrome Extension (Manifest V3), vanilla JavaScript, custom CSS Backend : Python, FastAPI, Uvicorn, Pydantic AI/ML : Google Gemma 3 27B IT, Gemini Embeddings Agents : Fetch.ai uAgents SDK, Agentverse Evidence : Wikipedia REST API, Google Fact Check Tools API Data : SQLite (vector cache with cosine similarity) <div