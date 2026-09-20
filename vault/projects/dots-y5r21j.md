---
slug: "dots-y5r21j"
url: "https://devpost.com/software/dots-y5r21j"
title: "Dots"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 525
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Dots

> Dots transforms floor plans into ADA-compliant tactile maps, providing architects and businesses with a scalable way to ensure universal accessibility through navigation.

[Devpost](https://devpost.com/software/dots-y5r21j) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[accessibility]] [[developer_tools]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** elevenlabs, fastapi, fetch.ai, gemini, python, sqlite, swift, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dots

## Body

Full Customer pipeline (How this comes in life once the business is ADA compliant) GIF Example 3D model Inspiration We started this project from a simple but high‑impact question: why are floor plans everywhere, yet blind and low‑vision users often get zero usable orientation from them? In most venues (stadiums, malls, campuses), wayfinding depends on visual signage, and even when accessibility exists, it’s rarely something you can hold, feel, and use immediately. We wanted a way where you can take a floorplan and output a tactile-friendly map that can be printed or embossed—then make it even more useful by attaching a QR code so anyone can scan and ask questions about the layout (text or voice). What it does Dots turns a floorplan into an accessibility-first navigation experience: Generates a tactile-style map image (high-contrast black-on-white, patterns + symbols, no numeric legends) from a floorplan. Produces an ADA-style compliance summary/report from the extracted layout when available. Creates a map-specific QR link so anyone can scan and ask: Text Q&A: “Where is the entrance?”, “Where are the stairs?”, “How many exits?” Voice Q&A: same questions via a conversational voice agent. Keeps Q&A isolated per map using a unique map_id, so different venues/maps never mix context. How we built it Python + FastAPI backend to handle uploads, map creation, and serving /m/{map_id} chat + /m/{map_id}/voice. Gemini (google-genai) for tactile map generation and for producing a compact “map context” used to ground Q&A. Fetch.ai ASI:One for fast text-based Q&A using the per-map context as the system prompt. ElevenLabs Conversational AI for voice sessions using short-lived server-minted tokens and per-map prompt overrides. SQLite to store per-map context and per-user chat history keyed by map_id + session_id. Challenges we ran into Latency from chaining model calls; we redesigned the pipeline so “broadcast Q&A” can skip regeneration when a tactile image already exists. Model variability when interpreting tactile-style images; we added robust fallbacks so the system remains usable even when context extraction is imperfect. Deployment + URL correctness: making QR links work required careful handling of public base URLs, local vs server environments, and persistent storage. Accomplishments that we're proud of A true end-to-end accessibility pipeline: floorplan → tactile output → QR → Q&A (text + voice). Per-map isolation via map_id, so multiple tactile maps can be broadcast simultaneously without cross-contamination. A practical voice setup that’s secure by design (ElevenLabs keys never leave the server; clients only get short-lived tokens). What we learned Great accessibility UX comes from grounded context and simple interaction loops (scan → ask → orient). Voice agents are mostly a product problem: token minting, mic permissions, and low-latency responses matter as much as the model. For reliability, every AI step needs observable debugging and safe fallbacks. What's next for Dots Improve map understanding with structured layouts (doors/walls/POIs) so Q&A can answer with higher precision and fewer vision-only guesses. Add optional heading-aware guidance (compass calibration) to answer “turn left/right” relative to the user’s orientation. Support venue-scale maps (multi-level, zones, stairs/elevators) and better tactile print formats (PDF templates + QR embedding). Production hardening: background jobs, caching, and a clean “create map → share QR” workflow for events and facilities. <div