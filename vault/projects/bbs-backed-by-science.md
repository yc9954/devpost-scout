---
slug: "bbs-backed-by-science"
url: "https://devpost.com/software/bbs-backed-by-science"
title: "BBS: Backed by Science"
hackathon: "Perplexity Hackathon"
organization: "Perplexity"
winner: true
words: 423
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/media_journalism"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
---

# BBS: Backed by Science

> Scientific verification for social media videos. Get AI-powered fact checks and evidence-based analysis powered by Perplexity.

[Devpost](https://devpost.com/software/bbs-backed-by-science) · hackathon [[Perplexity Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[media_journalism]]
  <sub>weak: scientific_research</sub>
**substrate** [[financial_record]] [[transcript_audio]]
  <sub>weak: genomic_bio</sub>

**stack** firebase, node.js, perplexity, swift, swiftui, typescript

## Body

Report view: List of claims Report view: Summary References for the summary Home page with the list of the reports Inspiration As a fitness enthusiast, I found myself constantly questioning the validity of health and wellness claims in YouTube and TikTok videos. From protein requirements to meal timing, I noticed many creators making contrasting statements about what's "scientifically proven." While Perplexity helped me verify these claims individually, I wanted a more efficient way to fact-check video content directly. This led to the creation of BBS - a tool that brings scientific verification to video content consumption. What it does BBS analyzes video content from YouTube and TikTok, extracting key claims and statements. Using Perplexity's Sonar API, it verifies these claims against scientific sources, providing users with evidence-based analysis and citations. The app integrates seamlessly with iOS share sheets, allowing users to fact-check videos with a single tap. How I built it Frontend : Developed an iOS app using SwiftUI for a clean, intuitive interface Backend : Implemented a robust system for video processing and analysis API Integration : Perplexity's Sonar API for scientific verification and research Multiple transcription services for redundancy (YouTube and TikTok) Performance Optimization : Implemented caching for transcriptions and reports Built a system to handle viral content efficiently Optimized API usage to manage costs while maintaining performance Challenges I ran into Video Transcription : Finding reliable APIs for YouTube and TikTok video transcription was challenging. I solved this by implementing multiple solutions for redundancy. Cost Management : To handle viral content efficiently while managing API costs, I implemented a smart caching system. This ensures that only the first user needs to wait for a full analysis, while subsequent users get instant results. API Integration : Learning to work with Perplexity's Sonar API and implementing structured output for LLMs required significant experimentation and iteration. Accomplishments that I'm proud of Created a seamless user experience for video content verification Successfully integrated multiple transcription services for reliability Built an efficient caching system that balances performance and cost Developed a robust scientific verification engine using Perplexity's Sonar API Created a solution that addresses a real need in content consumption What I learned How to effectively use structured output with LLMs Best practices for integrating and optimizing Perplexity's APIs Techniques for efficient caching and cost management The importance of redundancy in critical services What's next for BBS: Backed by Science Enhance the app's robustness and reliability Prepare for App Store submission Expand verification capabilities to more video platforms Optimize the scientific verification engine further <div