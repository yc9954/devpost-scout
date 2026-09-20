---
slug: "adapt-ujvn5e"
url: "https://devpost.com/software/adapt-ujvn5e"
title: "ADapt"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 588
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ADapt

> One ad. Every market.AI-localized in seconds.

[Devpost](https://devpost.com/software/adapt-ujvn5e) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[measured_ablation]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]]
  <sub>weak: voice_speech</sub>
**domain** [[developer_tools]]
  <sub>weak: immigration_refugee</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** elasticsearch, fastapi, ffmpeg, graphite, greylock, jwt, model-context-protocol-(mcp), next.js, numpy, openai-gpt-5, openai-whisper, perplexity-sonar-api, pil, poke

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adapt

## Body

Gallery Video Editor Frontend Inspiration Every brand wants personalized ads, but creating unique creatives for every audience segment is expensive and slow. We watched marketing teams manually re-edit the same video dozens of times, tweaking pacing, color, and captions for different demographics. We thought: what if AI could understand both the video and the audience, and automatically generate targeted variants from a single, manually developed ad? What it does ADapt is an AI-powered video ad localization platform. Upload one master video and a CSV of audience profiles, and it: Analyzes your video by extracting scenes, transcribing audio, and generating per-second action descriptions Clusters your audience into meaningful segments using embeddings, visualized on an interactive 3D map Researches each segment with real-time market insights via Perplexity Sonar Generates targeted variants with segment-specific speed adjustments, color grading, text overlays, vertical reframing, and more, all driven by a constraint-aware AI planner The result: multiple production-ready ad variants from a single upload, each tailored to a specific audience. How we built it Backend : FastAPI with a multi-agent architecture. An Orchestrator routes requests, a Transform Planner uses GPT with a constraint-checking review loop, a Market Research Agent queries Perplexity Sonar, and a Group Ads Generator coordinates the full pipeline. Video Processing : FFmpeg handles speed changes (bounded at ±6%), 7 color grading presets, text overlays with impact-scored phrase placement, film grain, backdrop blur, and vertical reframing. Audience Intelligence : Elasticsearch embeddings for clustering with a heuristic fallback, projected into 3D via SVD for interactive visualization. Frontend : Next.js 16, React 19, Tailwind CSS 4, and TypeScript. Features a campaign dashboard, 3-step upload modal, timeline scrubber, 3D embeddings map, and variant gallery. MCP Server : Exposes video editing tools via the Model Context Protocol so external AI agents can use our platform programmatically. Challenges we ran into Getting the LLM to reliably choose the right video transforms. We solved this with a multi-round planner/reviewer loop that enforces explicit constraints over up to 3 revision rounds. Deciding where to place text overlays required building an impact scoring algorithm that considers keywords, punctuation, position in the video, and audio vs. visual source. Cross-platform font handling with FFmpeg's drawtext filter behaves differently across OS, so we built a fallback chain with PIL-based rendering. Making audience clustering work without Elasticsearch by building a heuristic vectorization fallback from raw profile data. Accomplishments that we're proud of Full end-to-end automation: from a raw video and a CSV to multiple targeted ad variants with zero manual editing. A constraint system that produces thoughtful, context-aware edit decisions (moody grades for urban professionals, bright grades for teen audiences). An interactive 3D audience visualization that makes segment groupings immediately intuitive. MCP integration that makes ADapt composable with any AI agent workflow. What we learned Structured constraint loops beat elaborate prompting for reliable LLM output. Small bounded transforms (like ±6% speed) compound into meaningful personalization without jarring artifacts. Deterministic randomization (MD5-based stable rolls) is critical for debugging pipelines with many moving parts. Robust fallbacks (heuristic clustering, font rendering, hardware acceleration detection) aren't just safety nets, they make the product actually usable across environments. What's next for ADapt Generative transforms : connecting stubbed-out background replacement, object erasure, and text replacement to cloud GPUs. A/B testing integration : feeding variant performance data back so ADapt learns which transforms work best per segment. Multi-language voice synthesis : re-voicing ads in different languages while preserving tone and cadence. Production scale : moving to a production database, adding job queues for parallel processing, and deploying on GPU infrastructure. <div