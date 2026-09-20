---
slug: "cuecard"
url: "https://devpost.com/software/cuecard"
title: "Snipper"
hackathon: "Build your Flutter Butler with Serverpod"
organization: "serverpod"
winner: true
words: 496
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# Snipper

> Transforming raw, long-form comedy footage into high-engagement social media content by leveraging the multimodal reasoning of Gemini 3 Flash.

[Devpost](https://devpost.com/software/cuecard) · hackathon [[Build your Flutter Butler with Serverpod]]

## Facets

**mechanism** [[structural_withholding]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** cloudrun, cloudsql, gcs, genimi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snipper

## Body

Snipper Inspiration Comedians need social media to survive. But editing standup sets into viral clips? That's a nightmare. It's tedious, technical, and eats up hours. Most comedians know they have killer moments buried in their footage. The problem is finding them. You're stuck scrubbing through timelines, guessing at timing, fighting with editing software. We built Snipper to handle all of that. Think of it as your personal content butler. It understands comedy timing, picks up on audience laughter, spots viral moments, then edits everything for you automatically. What it does Snipper is your automated editing assistant. Here's how it works. You upload raw standup footage, and Snipper: Analyzes the performance using Gemini 3.0 Flash Preview . It finds the distinct bits by picking up on setup/punchline structure and audience reactions. Scores each moment. You get a "Viral Potential" rating plus an explanation of why it works. Transforms your horizontal stage footage into vertical clips. Smart reframing keeps you centered in the shot. Generates karaoke-style captions that pop on the punchlines. Delivers social-ready clips. It even reminds you when to post so you stay consistent. How we built it We went full-stack Dart to keep everything type-safe: Frontend : Flutter for desktop and web. Clean, focused editor experience. Backend : Serverpod 3 handling all the RPCs, background jobs, and sessions. AI : Google Gemini 3.0 Flash Preview. We trained it to actually understand comedy structure, not just transcribe words. Infrastructure : Running on Google Cloud Run with Cloud SQL and PostgreSQL 16. Media : FFmpeg doing the heavy lifting for clipping, reframing, and burning in captions. Challenges we ran into Getting Cloud Run to talk to Cloud SQL reliably. Establishing stable database connectivity required careful configuration and extensive debugging. Coordinating asynchronous media pipelines. Orchestrating analysis, clipping, captioning, and export jobs while keeping progress visible and recoverable required careful iteration. Making it feel fast when it's not. Video processing is slow. Period. We had to build progress indicators and state updates so the app doesn't feel frozen while FFmpeg and AI do their thing. Accomplishments that we're proud of Snipper feels like a real production tool, not a one-off demo. It provides a persistent video library, clear job status tracking, and reliable exports. The system consistently turns long standup sets into polished, vertical clips with dynamic captions that are ready to post. What we learned Modularity matters when you're building AI workflows. Serverpod 3's separation of endpoints, jobs, and data models meant we could change the pipeline without breaking everything. Strong types across the backend and Flutter killed so many bugs before they happened. Made the whole async mess way easier to think about. What's next for Snipper We want to give creators more creative control: Caption styles that match your brand Auto-generated hashtags tuned for each platform AI thumbnails that capture your vibe Visual filters so you can style the same clip differently for different audiences Eventually Snipper goes from clipping butler to full creative partner. <div