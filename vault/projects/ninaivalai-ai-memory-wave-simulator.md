---
slug: "ninaivalai-ai-memory-wave-simulator"
url: "https://devpost.com/software/ninaivalai-ai-memory-wave-simulator"
title: "Ninaivalai - AI Memory Wave Simulator"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 371
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Ninaivalai - AI Memory Wave Simulator

> Upload your photos, videos & voice notes — Amazon Nova AI rebuilds them into a narrated memory experience with timeline, story, emotions & cinematic replay.

[Devpost](https://devpost.com/software/ninaivalai-ai-memory-wave-simulator) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: retrieval_grounding</sub>
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** amazon, amazon-route-53, amazon-web-services, bedrock, express.js, javascript, node.js, nova, python, react, vite

## Body

Drag and drop or browse to upload files. Home Page-Ninaivalai home screen showcasing all AI-powered feature. Analyzing-Amazon Nova AI analyzing your memories in real time using Nova Pro Vision + Nova Lite. Timeline-Smart chronological timeline built from your memories with time labels and thumbnails. Upload Page-Upload your photos, videos, voice notes or documents. AI auto-fills the date from filename. Emotions-Sentiment analysis showing primary emotion and scores across Joy, Love, Nostalgia, Excitement and Calm. Story-AI-generated 3-paragraph emotional narrative based on your uploaded memories. Chat-Conversational memory assistant — ask anything about your memories and Nova answers. Gaps-AI reconstructs what likely happened between your captured memories using timeline inference. Highlights-Top 3 most significant memory moments ranked with gold, silver and bronze badges. Replay Playing-Cinematic slideshow playing each photo and video with timeline captions and progress bar Replay Start-Full cinematic recap player showing all memories in sequence with AI narration script. Memories fade over time. We wanted to build an app that preserves cherished moments forever using AI — turning scattered photos and videos into a living, narrated experience. Upload photos, videos, voice notes or documents — Amazon Nova analyzes them and generates a smart timeline, emotional story, sentiment chart, top highlights, gap reconstruction, memory chat assistant, semantic search, and a full cinematic replay with narration. React + Vite frontend, Node.js + Express backend, Amazon Nova Pro (vision) + Nova Lite (text) via AWS Bedrock Converse API, Amazon S3 for file storage. Nova Pro analyzes actual image pixels, Nova Lite runs 7 AI steps in parallel in under 30 seconds. Getting Nova Pro to analyze real image pixels correctly, fixing strict user/assistant message alternation in Nova's Converse API, preventing AI hallucination (inventing fake names), and running the full pipeline in parallel without timeouts. Full multimodal pipeline where photos are analyzed by Nova Pro Vision and Nova Lite generates 9 AI features simultaneously. The cinematic replay plays every photo and video in sequence with AI narration. How to use AWS Bedrock Converse API, chain Nova Pro + Nova Lite together for a real multimodal pipeline, and handle multi-turn conversation history correctly with Amazon Nova. Add Nova Sonic for real-time voice narration, build a mobile app, and enable shared family memory albums with collaborative AI storytelling. <div