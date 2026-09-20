---
slug: "fakey-ai"
url: "https://devpost.com/software/fakey-ai"
title: "Proofy.AI"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 976
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/media_journalism"
  - "user/general_public"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Proofy.AI

> An explainable, Gemini-powered verification platform built to restore trust in digital media.

[Devpost](https://devpost.com/software/fakey-ai) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[media_journalism]]
**user** [[general_public]] [[researcher]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** ai, aistudio, antigravity, apis, clsx, confidence, css, custom, framer, functions, gemini, google, google/genai, invocation

## How they structured the write-up

- project story
- mobile app
- browser extension – on-screen verification
- web platform – advanced verification & analysis
- how we built it
- challenges faced
- accomplishments
- what we learned
- what’s next

## Body

Landing Page - 1 Landing page (Dashboard) - 2 Check Many feature - 3 Loading page - 4 AI Text Checker feature - 5 AI Text Checker feature Result - 6 Landing Page (uploading ) - 7 Video Deepfake AI detection result - 8 Video AI result (cont) - 9 Source finder feature - 10 Source finder image upload - 11 Source finder image result - 12 Proofy.AI Project Story Inspiration Proofy.AI began from a real incident at home. My mother almost invested money after watching a video that appeared to show India’s Finance Minister, Nirmala Sitharaman, promoting an investment scheme. The video looked authentic, the voice was convincing, and there were no obvious red flags. Only later did we discover that the video had been generated using AI. When we tried to verify the video, we realized that most available detection tools were designed for researchers or large organizations. They were either too technical or inaccessible for everyday users. There was no simple way for someone without technical background to verify content before trusting it. Proofy.AI was built to bridge this gap and give regular users an easy, reliable way to verify digital content before falling victim to scams or misinformation. What It Does Proofy.AI allows users to verify whether digital content such as videos, images, audio, or text is authentic or AI-generated through simple and accessible interfaces. Mobile App The mobile application is designed for real-world usage, especially when users are already watching or reading content. Instant Screen Analysis Users do not need to open the app manually. Pressing the Volume Up and Volume Down buttons together triggers a secure system overlay that captures whatever is currently visible on the screen and sends it for analysis. The system was tested to ensure reliable interpretation of partial screenshots, UI overlays, and compressed screen captures, which are common during real-world usage. Video Verification Videos are analyzed frame by frame rather than as a single compressed file. The system checks for: Frame-level inconsistencies Unnatural facial movements Motion interpolation artifacts Lip-sync mismatches Temporal glitches common in AI-generated videos By evaluating how visual inconsistencies evolve across frames, the system can detect subtle manipulations that may not be visible in individual frames. Voice and Text Detection Users can paste text or record short audio clips for verification. Voice analysis focuses on rhythm, pacing, pauses, and unnatural consistency often found in synthetic speech. Text analysis checks for repetitive phrasing, overly uniform structure, and patterns commonly seen in AI-generated or scam-related content. Source Finder Images are traced to determine whether they have been reused, edited, or presented out of context. The system focuses on identifying semantic similarities rather than exact duplicates to catch modified or cropped versions. Browser Extension – On-Screen Verification The browser extension enables users to verify content directly on the webpage they are viewing. Analyzes visible videos, images, and text in real time Works across news sites, social media platforms, and embedded media Does not require downloads, uploads, or switching tabs Special care was taken to ensure accurate interpretation of dynamic webpages, overlays, captions, and partially visible media. Web Platform – Advanced Verification & Analysis The web platform is intended for deeper inspection and detailed review, especially for users who want to understand why content was flagged. Multi-File Verification Users can upload and analyze multiple files simultaneously, including videos, images, audio files, and text documents. Each file is processed independently, with results displayed together to allow easy comparison across formats. Frame-Level Video Analysis Uploaded videos are broken down into individual frames and analyzed for: Facial distortions or unnatural expressions Lighting and shadow mismatches Motion and lip-sync inconsistencies Visual artifacts produced by generative models Instead of providing only a final verdict, the platform highlights exact timestamps where anomalies occur. Audio Verification & Voice Clone Detection Audio files can be uploaded or recorded directly for verification. The system checks for: Synthetic or generated speech Voice cloning indicators Replayed or manipulated audio segments Analysis focuses on micro-variations in human speech, such as breath patterns, timing irregularities, and unnatural smoothness. AI Text & Fact Consistency Checks Written content is evaluated to determine whether it was likely generated by AI based on: Repetitive sentence structures Overly consistent phrasing Limited linguistic variation The system also checks the logical consistency of the content itself by identifying: Internal contradictions Unsupported or unverifiable claims Fabricated or hallucinated facts Language patterns commonly used in scams Original Source Finder Images are traced across the web to identify: Where they first appeared Whether they have been reused or edited If they are being presented in a misleading context Detailed Analysis & Export After verification, users receive a structured breakdown explaining: What was analyzed What issues were detected Why certain sections were flagged Confidence indicators with supporting evidence The analysis can be exported as a file for documentation or sharing. How We Built It Proofy.AI was developed as a multi-platform system where the mobile app, browser extension, and web platform share the same detection logic while being optimized for their specific environments. Challenges Faced One major challenge was implementing the volume-button trigger on Android, which required careful handling of system permissions and background execution. Another challenge was maintaining detection accuracy while keeping the system fast and accessible for non-technical users. Accomplishments First place at a national-level hackathon held at IIT Delhi Awarded a ₹50,000 cash prize Built a complete ecosystem including a mobile app, web platform, and browser extension Implemented instant on-screen verification Designed with real users and real-world trust issues in mind What We Learned We learned that for public-facing AI systems, explainability and usability matter as much as technical accuracy. People are more likely to trust and use a system when they understand its decisions. What’s Next We plan to expand Proofy.AI for journalistic, investigative, and institutional use cases, where transparent verification, timestamp-level evidence, and clear explanations are essential. <div