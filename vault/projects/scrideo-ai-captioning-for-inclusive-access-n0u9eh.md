---
slug: "scrideo-ai-captioning-for-inclusive-access-n0u9eh"
url: "https://devpost.com/software/scrideo-ai-captioning-for-inclusive-access-n0u9eh"
title: "Scrideo – AI Captioning for Inclusive Access"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 454
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Scrideo – AI Captioning for Inclusive Access

> AI powered tool that makes videos accessible to 466M deaf and hard-of-hearing people worldwide. Upload any video or YouTube link, get professionally captioned content in minutes. No skills required.

[Devpost](https://devpost.com/software/scrideo-ai-captioning-for-inclusive-access-n0u9eh) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** css3, ffmpeg, flask, html5, jwt, numpy, openai, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scrideo – ai captioning for inclusive access

## Body

Inspiration Online video content is more accessible than ever before. It connects people across the world, educates millions, and powers digital communication. Yet for many, this access remains incomplete. Over 466 million deaf and hard of hearing individuals worldwide still face barriers when consuming online video content. While platforms have introduced auto captioning, tools like YouTube’s captions are often inaccurate and unreliable. Professional subtitling services cost $10 to $30 per minute, making them inaccessible for most creators. In earlier days, television channels like DD News often included Indian Sign Language (ISL) interpretation, making content more inclusive. Today, such accessibility features are rare in mainstream digital media. That saddened me. And it motivated me to build Scrideo. What it does Scrideo – AI Captioning for Inclusive Access is a web-based AI platform that automatically generates and permanently embeds professional subtitles into videos. Users can upload: Video files (MP4, MOV, AVI, MKV, WEBM) A YouTube URL Scrideo then: Generates highly accurate, timestamp synced captions (95%+ accuracy on clear audio) Allows customization of 50+ subtitle styles (font, color, outline, shadow, position) Permanently burns subtitles into the video (no external .srt files required) Provides a ready to download, shareable final video How we built it AI & Transcription: OpenAI Whisper (large-v2) for state of the art speech recognition Automatic language detection Intelligent subtitle line breaking using NLP heuristics Backend & Processing: Flask for server side architecture FFmpeg for audio extraction and subtitle embedding ASS (Advanced SubStation Alpha) for professional grade subtitle styling yt-dlp for YouTube downloading JWT Authentication for secure user sessions Asynchronous job queue for non blocking video processing Frontend: TailwindCSS for responsive and modern UI Real time subtitle preview without reprocessing Fully mobile responsive design Deployment: Hosted on Hugging Face Spaces Production ready using Gunicorn Auto cleanup system to manage temporary storage Challenges we ran into YouTube Download Timeouts: Long videos exceeded request time limits. Implemented background processing with status polling. Temporary Storage Constraints: Hosting resets storage on restart. Designed an in-memory job tracker with automated cleanup routines. Accomplishments that we're proud of Live working demo accessible to anyone 95%+ transcription accuracy 30 seconds processing per minute of video 50+ customizable subtitle styles Fully responsive across devices Secure authentication system with user history Deployed successfully on free tier infrastructure What we learned Deep understanding of transformer-based speech recognition (Whisper architecture) Advanced FFmpeg filter graph manipulation Professional broadcast subtitle standards (ASS format) Memory optimization and model deployment strategies Secure authentication using JWT Building scalable async processing system What's next for Scrideo – AI Captioning for Inclusive Access Speaker diarization (identify who is speaking) Cloud storage integrations (Google Drive / Dropbox) Analytics dashboard for usage insights Integration of Indian Sign Language (ISL) overlay support in future versions <div