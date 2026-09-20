---
slug: "novareel"
url: "https://devpost.com/software/novareel"
title: "NovaReel"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1182
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "user/small_business"
  - "substrate/video_visual"
---

# NovaReel

> Turn product photos into high-converting videos.

[Devpost](https://devpost.com/software/novareel) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[labor_employment]]
**user** [[small_business]]
  <sub>weak: government_staff</sub>
**substrate** [[video_visual]]

**stack** amazon-nova-models, amazon-polly, amazon-sqs-ready-architecture, bedrock, clerk-authentication, edge-tts, eslint, ffmpeg, javascript, pexels-api, playwright, postcss, pytest, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for novareel

## Body

Video Studio Video Translation Option Social Media Integration live status updates. Option to Configure your brand identity. Logo, fonts, colors Admin page for Overall health for the current rollout month. asynchronous processing Pricing Option Account management Inspiration NovaReel came from a real problem I experienced as an Amazon seller from 2019 to 2021. I saw firsthand how much product videos can improve conversion, but I also learned how difficult they are for small sellers to produce consistently. Most sellers do not have a creative team, an editor, a copywriter, or the budget to keep making new video content for every launch, listing refresh, or campaign. That creates a frustrating gap: sellers already have product photos, but turning those photos into high-converting marketing videos is still too slow, too expensive, and too manual. We built NovaReel to close that gap and give small businesses access to a fast, AI-powered video marketing workflow without draining their already thin profit margins. What it does NovaReel turns product photos and a short product description into a complete marketing video in minutes. A user uploads product images, selects preferences like style, language, voice, captions, and aspect ratio, and NovaReel generates a polished 30 to 60 second video with voice narration, subtitles, transitions, music, and downloadable output. It goes beyond simple slideshow generation. NovaReel analyzes the uploaded images, writes a six-scene script, matches visuals to each scene, generates missing contextual visuals when the user does not have enough assets, and renders the final video automatically. It also supports storyboard review before rendering, multilingual translation, A/B video variants, AI-generated publishing metadata, and direct YouTube publishing. How we built it We built NovaReel as a full-stack application with a Next.js frontend, a FastAPI backend, and an async worker for video generation jobs. The rendering pipeline is powered by ffmpeg , which handles scene assembly, motion effects, subtitles, transitions, audio synchronization, and final export. Instead of treating video generation as a single prompt, we designed NovaReel as an agentic workflow. The system first understands the uploaded assets, then plans and executes the full generation pipeline step by step. That architecture gave us much better control over output quality, timing, and fallbacks. We used multiple Amazon Nova models, with each model solving a specific part of the problem: Amazon Nova Pro ( amazon.nova-pro-v1:0 ) powers the orchestration and reasoning layer. It acts as the agentic controller for the pipeline, deciding what to do next, invoking tools in sequence, reviewing script quality, planning scene media, deciding when AI-generated visuals are needed, and finalizing the workflow. Amazon Nova Lite ( amazon.nova-lite-v1:0 ) is the main multimodal workhorse. We use it for understanding uploaded product images, extracting product descriptions and focal regions, generating the six-scene script, supporting media planning and B-roll reasoning, translating scripts into other languages, and generating publishing metadata. Amazon Nova 2 Multimodal Embeddings ( amazon.nova-2-multimodal-embeddings-v1:0 ) handles semantic image matching. We use it to match each script line with the most relevant uploaded product image so the storyboard feels coherent instead of randomly assembled. Amazon Nova Canvas ( amazon.nova-canvas-v1:0 ) is used for AI image generation. When a seller only has a few product photos, Nova Canvas creates new campaign-style or contextual visuals so the final video has more variety and feels more premium. Amazon Nova Sonic ( amazon.nova-sonic-v1:0 ) is our intended Nova-native voice layer. In the current implementation, it is configured in the architecture, but narration still falls back to EdgeTTS and Polly while streaming support is being completed. Around these Nova models, we built the rest of the workflow: storyboard review and approval, multilingual output, variant generation for testing, metadata generation, brand customization, and publishing support. Challenges we ran into One of the biggest challenges was reliability when users upload only a small number of product images. In real seller workflows, users often have only two to four usable product photos, which is not enough to create a visually rich video on its own. We had to build logic that decides when to reuse product shots, when to use contextual media, and when to generate new AI imagery to avoid repetitive output. Another major challenge was synchronization. Audio length, scene timing, transitions, subtitle timing, and final video duration all have to line up cleanly. We ran into mismatches between generated narration and rendered scenes, so we added duration reconciliation and padding logic to keep the final video aligned with the audio. We also had to design strong fallbacks throughout the system. If a media source, voice provider, or generation step failed, the pipeline still needed to complete in a way that felt usable and polished. Accomplishments that we're proud of We are proud that NovaReel is not just a concept, but a working end-to-end product workflow. Users can upload product images, generate videos, review storyboards, translate outputs, create variants, and prepare content for publishing from a single interface. That makes the product feel practical for real sellers, not just impressive in a demo. We are also proud of the way we used Amazon Nova models together. Rather than using a single model for everything, we designed a system where orchestration, multimodal understanding, semantic matching, and AI image generation each have a clear role. That made the output much more reliable and gave us a stronger real-world workflow. Most importantly, we are proud that NovaReel directly addresses a real business pain point. It helps small sellers create high-quality marketing videos without needing an agency, a video editor, or a large content budget. What we learned We learned that solving this problem is not just about generating a video. The real challenge is reducing creative friction across the whole workflow. Sellers do not only need editing help; they need help with scripting, asset gaps, timing, localization, testing, and publishing. That pushed us to think beyond "AI video generation" and build a broader AI marketing workflow. We also learned that multimodal AI becomes much more powerful when it is orchestrated well. Image understanding, script generation, embeddings, AI image generation, and rendering each solve a different part of the problem, but the real value comes from connecting them into a dependable system. Finally, we learned that for real product use cases, reliability matters just as much as raw model capability. Guardrails, fallbacks, and synchronization logic were just as important as the AI itself. What's next for NovaReel The next step for NovaReel is turning it from a strong hackathon project into a seller-ready platform. We want to expand direct publishing beyond YouTube to channels like TikTok and Instagram, improve brand controls for more consistent creative output, and deepen analytics so sellers can understand which video variants perform best. We also want to add stronger marketplace integrations, faster batch generation for multiple products, and more advanced campaign workflows for commerce teams. On the AI side, we want to complete deeper voice integration and continue improving how NovaReel handles limited product assets while still producing visually strong videos. Our long-term vision is simple: give every seller, especially small businesses, an AI-powered video marketing studio that helps them compete without needing a full creative team. <div