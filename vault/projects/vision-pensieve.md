---
slug: "vision-pensieve"
url: "https://devpost.com/software/vision-pensieve"
title: "Vision Pensieve"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 760
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Vision Pensieve

> Find any image by describing it. A local-first, semantic search and asset manager powered by single-pass vision AI.

[Devpost](https://devpost.com/software/vision-pensieve) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[media_journalism]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** agents, css, fastapi, fastembed, gemini, groq, lancedb, next.js, ollama, openai, pydantic, python, react, rust

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for vision pensieve

## Body

Inspiration My photo library had thousands of images and no way to find anything. Filenames are IMG_4032.jpg . Folders are by date. Tags never get added because tagging is boring. Meanwhile every "smart" photo search product wants to upload my entire camera roll to someone else's servers. So: what if the search index lived on my machine, and the cloud model only ever saw each photo once? What it does Vision Pensieve is a local-first desktop app that searches photo libraries in plain language. You describe what you want - "a dog on a beach", "the receipt with the blue logo", "screenshots of error messages" and it finds the matching images. Index a folder. Each image is analyzed once by a vision model into a structured description, detected objects, and any visible text (OCR). Search instantly. Descriptions are embedded and stored locally in LanceDB and SQLite. Every search after that is local semantic similarity - no image ever goes back to the model. Refine in natural language. Narrow results with follow-up filters instead of rebuilding a query. Organize safely. Ask it to sort photos into folders and it generates a dry-run preview of every file operation first. Nothing moves on disk until you click approve. How I built it Backend: Python + FastAPI, with the OpenAI Agents SDK driving the vision, refinement, and organizer agents. Storage: LanceDB for vectors, SQLite for metadata. Both embedded - no server, no Docker, no daemon to babysit. Embeddings: FastEmbed, running locally on CPU. Frontend: Next.js 16 + React 19, shipped as a native desktop app via Tauri 2. Secrets: API keys live in the OS keychain, never in a config file in the repo. The architecture is deliberately one-directional: images flow in to the model exactly once, and from then on every feature - search, refinement, organization - runs against local text and vectors. Challenges I ran into Picking a vector store that doesn't need infrastructure. The first design used a server-based vector DB. That's fine for a web service and completely wrong for a desktop app - asking a user to run Docker before they can search their own photos is a non-starter. Migrating to embedded LanceDB removed the entire class of problem. Embedding identity. Change the embedding model and every stored vector silently becomes garbage - queries still return results, just wrong ones. I had to make the embedding model part of the index's identity so a mismatch is detected loudly instead of degrading quietly. Background indexing was a trap. An early version auto-indexed folders on a timer. It burned tokens on images nobody asked about, ran while the user wasn't looking, and made cost unpredictable. I ripped it out entirely. Indexing is now explicit and per-folder: the user points at a folder and pays for exactly that. Reading API keys from the keychain. The desktop shell often attaches to an already-running backend rather than spawning it, so passing secrets down from the shell process didn't reliably work. The Python process reads the OS keychain directly instead. Cost discipline as a design constraint. Never call a model on a keystroke. Never call a model where a regex will do. One vision call per image, ever - that rule shaped more of the architecture than any framework choice did. Accomplishments that I'm proud of Search cost is decoupled from library size. Indexing 1,000 photos costs around $0.15–$0.30 in vision API calls, once. After that, searching returns results in sub-50ms over local LanceDB vectors with zero API calls - persistently stored locally. Even if the database is manually deleted, your photos remain completely untouched; the worst-case scenario is simply re-indexing, while normal day-to-day operation guarantees zero API overhead for search. Also: destructive operations are preview-first by default. The organizer shows you the full plan before a single file moves. What I learned Local-first isn't only a privacy stance - it's a performance and cost stance. Once the expensive work is done once and cached locally, the app gets faster and cheaper the longer you use it, which is the opposite of how most AI products behave. And "remove the feature" is often the right answer. Auto-indexing looked smart and was actively harmful; deleting it made the product both cheaper and easier to reason about. What's next for Vision Pensieve A fully local vision model option, so images never leave the machine at all. Face and person grouping, computed locally. Duplicate and near-duplicate detection using the vectors already in the index. Archive-wide questions - asking about the whole library rather than searching within it. <div