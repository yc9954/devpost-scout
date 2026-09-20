---
slug: "hallmark"
url: "https://devpost.com/software/hallmark"
title: "Hallmark"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 652
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/agriculture_food"
  - "domain/immigration_refugee"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Hallmark

> Governed AI creative: generate ad campaigns that can prove where they came from.

[Devpost](https://devpost.com/software/hallmark) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[agriculture_food]] [[immigration_refugee]] [[supply_logistics]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[regulation_legal_text]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** backblaze-b2, boto3, deepseek, docker, elevenlabs, eu-ai-act, fastapi, featherless-ai, ffmpeg, flux, genblaze, generative-ai, javascript, nvidia-nim

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next

## Body

Inspiration EU AI Act Article 50 became applicable on 2 August 2026 — the day we started building. It requires AI-generated image, audio and video to be marked in a machine-readable format and detectable as AI-generated. Every AI creative tool we looked at hands you a file and, at best, a prompt history. Neither survives a compliance review. Meanwhile Genblaze already emits a canonical, SHA-256-bound manifest that can be embedded directly into an MP4 or PNG, and Backblaze B2 has Object Lock. Those two things are almost exactly what the regulation asks for — nobody had connected them. That gap is Hallmark. What it does You write a one-line brief and a brand kit (tone, visual rules, banned claims, required disclosure). Hallmark then: Plans the campaign into structured scenes with an LLM. Generates keyframes per scene and per format. Judges its own output — a vision model scores brand adherence, a text model checks copy for banned claims. Failures are retried with the critique fed back into the prompt , and each attempt is linked by parent_run_id , so the reasoning trail is part of the provenance. Discloses — burns the required AI-disclosure onto the creative. Composes an MP4 ad from the approved stills with ElevenLabs voiceover. Attests — embeds the manifest inside each delivered file and writes an immutable copy to B2 under Object Lock. Verifies — anyone can drop a file into the public /verify page and read its full lineage offline. No lookup, no need to trust our website. Exports the Article 50 disclosure register as CSV. How we built it FastAPI + React in one Docker container, with all Genblaze usage deliberately confined to a single pipelines.py so the orchestration boundary is inspectable. B2 is the system of record — run records live in the bucket as JSON, so the Library and Register survive restarts with no database at all . The judge loop is Genblaze's AgentLoop with a CallableEvaluator ; the planner is a custom SyncProvider that wraps chat(base_url=…) so the LLM call becomes a real manifest'd Step rather than an untracked side call. Challenges we ran into The free NVIDIA NIM catalog is much smaller than the docs suggest. We probed it directly: only flux.1-dev was reachable. Cosmos video, Riva TTS, Fugatto, SDXL and SD3.5 all returned 404, and flux.1-schnell hung indefinitely. So there is no video model in this stack — the ad is composed from generated stills with ffmpeg instead. Honest, fast, and every frame is still provenance-covered. Genblaze rejects presigned URLs in manifests (they decay before the manifest does). On a private bucket that means durable URLs aren't browser-loadable, so the app mints short-lived signed URLs at read time. This turned out to be the better architecture. ObjectStorageSink never forwards allowed_roots to AssetTransfer , so file:// assets can only be read from temp roots. All provider scratch moved under TMPDIR . FFmpegTransform declares only VIDEO/AUDIO modalities , so the image disclosure overlay uses Pillow while the video path stays a real pipeline step. zoompan silently defaults to 1280x720 , which broke the Ken Burns crop until we pinned s= . Hugging Face Spaces now requires PRO for Docker Spaces , so we moved the deploy to Render. Accomplishments we're proud of The verify portal. Drop a file in and it reads its own provenance out of the bytes — no database lookup, no trust in our server. And the governance is real, not decorative: the copy judge caught a genuine borderline claim during testing and rejected it. What we learned Provenance is only worth anything if it is a side effect of the normal workflow. The moment it becomes a separate step someone has to remember, it stops happening. What's next Ed25519 manifest signing (Genblaze trust mode 2) to prove who generated an asset, not just that it is unmodified; C2PA interop; and B2 Event Notifications to trigger verification automatically on upload. <div