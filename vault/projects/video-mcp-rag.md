---
slug: "video-mcp-rag"
url: "https://devpost.com/software/video-mcp-rag"
title: "Video-MCP-RAG"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 762
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Video-MCP-RAG

> Ask anything. Find any moment. Understand every video.

[Devpost](https://devpost.com/software/video-mcp-rag) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[labor_employment]]
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** amazon-bedrock, amazon-nova-lite, amazon-nova-pro, amazon-titan-multimodal-embeddings, aws-transcribe, fastapi, fastmcp, ffmpeg, gunicorn, moviepy, pixeltable, pyav, pydantic, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for video-mcp-rag

## Body

Ask anything. Find any moment. Understand every video. Inspiration Video is one of the richest formats for storing knowledge, yet it remains almost entirely unsearchable. Lectures, product demos, meeting recordings, and training videos represent enormous institutional value — but the only way to find anything inside them is to watch them in full. We wanted to change that. The question that drove us was simple: what if you could talk to a video the same way you talk to a colleague who watched it for you? What it does Video-MCP-RAG lets users upload any video and interact with it through natural language. Once a video is processed, users can: Ask factual questions — "What did the speaker say about the budget?" and receive a grounded answer drawn directly from the transcript and scene captions Find specific moments — "Show me when the product is demonstrated" and receive a trimmed clip of exactly that scene Search by image — upload a reference image and find the most visually similar moment in the video Extract by time — "Give me the first 30 seconds" returns that clip immediately How we built it The system runs as two services connected via the Model Context Protocol (MCP): MCP Tool Server (FastMCP) owns all video intelligence — frame extraction, audio transcription via AWS Transcribe, batched scene captioning with Nova Pro, and similarity search powered by Amazon Titan Multimodal Embeddings. It exposes four typed tools: get_video_clip_from_query , get_video_clip_from_image , get_video_clip_by_time , and ask_question_about_video . FastAPI Server hosts the NovaAgent, which runs a four-stage pipeline on every user message: routing (Nova Lite classifies intent), tool selection (Nova Pro picks the right tool via structured JSON output), tool execution (MCP call), and response generation (Nova Pro wraps the result in natural language). The key architectural decision was using Amazon Titan Multimodal Embeddings V1 for every modality — text, images, and video frames all live in a single unified vector space. This eliminated the need for separate CLIP and text-embedding models and made cross-modal search work naturally. All structured LLM outputs are Pydantic-validated using Bedrock's forced tool-use mode, so there is no string parsing anywhere in the agent pipeline. Pixeltable serves as both the vector store and the conversation memory backend. Challenges we ran into Unified embedding space — early versions used separate models for image and text embeddings, which made cross-modal retrieval unreliable. Switching everything to Titan Multimodal Embeddings solved this cleanly. MCP health checking — the FastMCP server returns HTTP 406 to plain GET requests (it expects SSE headers), which broke our startup health check. We had to detect 406 as a valid "server is up" signal rather than treating it as a failure. Gunicorn worker count — the default formula (2 × CPU + 1) spawned too many workers on constrained cloud environments, exhausting available memory. We added an explicit worker cap for deployment. Video processing latency — per-frame Nova Pro captioning was too slow and expensive. Batching consecutive frames (5 per API call) reduced both latency and cost by roughly 3x while producing better captions because the model has temporal context. Accomplishments that we're proud of A fully working multimodal RAG pipeline that searches across transcript chunks and scene captions in a single unified vector space Structured JSON output at every LLM step with zero string parsing — every routing, tool-selection, and generation call is Pydantic-validated A clean two-service architecture using MCP that keeps video intelligence fully decoupled from the agent layer Full observability with Opik tracing every LLM call end-to-end What we learned Amazon Titan Multimodal Embeddings is a genuinely powerful simplification for multimodal systems — one model, one vector space, no glue code MCP is an elegant pattern for separating tool logic from agent logic, and FastMCP makes it very fast to build production-ready tool servers Nova Lite is surprisingly capable for binary routing decisions and adds almost no latency — the two-model routing pattern (Lite for routing, Pro for reasoning) is a pattern we will reuse Batching multimodal inputs to Nova Pro significantly reduces both cost and latency without sacrificing quality What's next for Video-MCP-RAG Multi-video search — query across an entire library of videos at once Automatic chapter generation — use Nova Pro to segment and label videos into named chapters automatically Speaker diarization — identify and label individual speakers in the transcript so users can search by speaker name S3 integration — connect directly to existing video libraries in S3 without manual upload Nova Act integration — use Nova Act to automate video upload and processing workflows across web-based video platforms <div