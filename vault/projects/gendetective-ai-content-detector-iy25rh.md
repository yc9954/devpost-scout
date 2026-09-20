---
slug: "gendetective-ai-content-detector-iy25rh"
url: "https://devpost.com/software/gendetective-ai-content-detector-iy25rh"
title: "GenDetective: AI Content Detector"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 394
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# GenDetective: AI Content Detector

> GenDetective is a multi-modal AI content detector that uses statistical and stylometric analysis as well as LLM reasoning to identify AI-generated images, videos, and text.

[Devpost](https://devpost.com/software/gendetective-ai-content-detector-iy25rh) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[civic_government]] [[media_journalism]]
**user** [[researcher]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** css, fastapi, geminiapi, git, github, html, javascript, opencv, python, scikit-learn, scipy, transformers

## How they structured the write-up

- inspiration
- what it does
- the goal is to make ai detection transparent, explainable, and accessible .
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gendetective: ai content detector

## Body

System Architecture Extension Frontend Image output example Web Dashboard Extension Inspiration The rapid growth of generative AI tools has made it increasingly difficult to distinguish between human-created and AI-generated digital content. Images, videos, and text produced by modern AI models are now widely shared online without disclosure, raising concerns about misinformation, academic integrity, fake news, and digital trust. This project was inspired by a simple real-world question: “Is the content I am seeing real or AI-generated?” To address this, we built GenDetective , a multimodal AI-content detection system available as both a Chrome browser extension and a web dashboard . What it does GenDetective analyzes images, videos, and text and estimates whether they are AI-generated or human-created . The system provides: Classification (AI-generated, likely AI, likely real, real, inconclusive) Confidence score Human-readable explanation Forensic indicators used in the decision Users can: Upload media through the browser extension Use the dashboard interface Submit text for analysis The goal is to make AI detection transparent, explainable, and accessible . How we built it GenDetective consists of three main components: Browser Extension HTML CSS JavaScript Dashboard Interface Image upload and detection Video upload and detection Text analysis Visualization of detection results FastAPI Backend Technologies used: FastAPI NumPy OpenCV Transformers (CLIP) Gemini API scikit-learn The system uses an ensemble detection approach combining heuristics, ML models, embeddings, and LLM reasoning . Challenges we ran into Avoiding false positives in compressed media Detecting high-quality AI-generated videos Handling large video uploads efficiently Combining heuristic detection with LLM reasoning Maintaining performance inside a browser extension Limited API usage constraints Accomplishments that we're proud of Built a working multimodal AI detection system Created a Chrome extension connected to a backend Built a dashboard interface for detection Implemented image, video, and text detection pipelines Designed an explainable AI detection workflow Integrated CLIP + Gemini + ML models What we learned AI-generated content differs from human content in subtle statistical patterns rather than obvious visual artifacts . No single feature can reliably detect AI content Detection works best by combining multiple weak signals Video detection requires temporal analysis Browser extensions require performance optimization What's next for GenDetective: AI Content Detector Expand benchmarking datasets Improve deepfake video detection accuracy Add frame-level voting detection Improve motion realism modeling Strengthen text detection robustness Deploy backend to cloud infrastructure Publish the browser extension Optimize dashboard UX and performance <div