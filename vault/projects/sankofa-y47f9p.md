---
slug: "sankofa-y47f9p"
url: "https://devpost.com/software/sankofa-y47f9p"
title: "Sankofa"
hackathon: "Gemini Live Agent Challenge"
organization: "Google"
winner: true
words: 1247
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/video_visual"
---

# Sankofa

> Transforming fragmented family history into living, breathing, multimodal stories.

[Devpost](https://devpost.com/software/sankofa-y47f9p) · hackathon [[Gemini Live Agent Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[media_journalism]]
**user** [[researcher]]
**substrate** [[genomic_bio]] [[video_visual]]

**stack** docker, gemini, google-adk, next.js, react, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- built with
- third-party integrations
- try it

## Body

Inspiration For over 200 million people in the African, Caribbean, and South Asian diasporas, the answer to "where are you from?" carries a weight most people never have to think about. Heritage isn't a percentage on a DNA test. It's a story. And for millions, that story has been lost, scattered across colonial archives, oral traditions, and academic papers most people will never read. Existing ancestry tools give data: country names, ethnicity percentages, migration paths. But heritage is inherently multimodal. It lives in the sound of a language, the landscape of a homeland, the texture of traditional craft, and the rhythm of oral storytelling. No single modality can capture it. Sankofa is named after the Akan word meaning "go back and get it." It's a multimodal AI griot, a storyteller in the West African tradition, that transforms sparse family history into an immersive heritage narrative you don't just read. You experience it. What It Does A user provides a few seeds: a family surname, a country or region, a time period, and optionally any fragments they know. From those seeds, Sankofa generates a flowing, multi-act heritage narrative with: Griot-inspired narration in a warm, oral storytelling voice grounded in historical fact AI-generated watercolor imagery of landscapes, people, and cultural artifacts, placed by the model at emotionally resonant moments via Gemini's native interleaved output Trust indicators where every segment is tagged as Historical, Cultural, or Reconstructed, so users always know what's documented fact versus imaginative reconstruction Audio narration via Gemini TTS for each text segment, with a persistent narration bar featuring track list, seek, and auto-advance Ambient soundscapes with per-act background audio (wind, fire, nature, market, drums) that crossfade between acts, selected contextually by the arc planner Follow-up exploration where users can ask Sankofa to go deeper into any aspect, with answers streaming in segment-by-segment via SSE Live voice conversation where users talk to the Griot in real-time via the Gemini Live API, with full context from the narrative already generated. Full-duplex audio with barge-in support. The Cinematic Opening Generating a full multimodal narrative takes time. Instead of showing a loading spinner, Sankofa opens with a ~90-second cinematic griot monologue ("Come. Sit with me...") synchronized to 12 on-screen text beats, with fire ambient audio and floating gold particles. The entire backend pipeline runs concurrently. If the narrative finishes before the monologue, the app waits. When the monologue ends and the story isn't ready yet, rotating heritage fun facts and arc chapter teasers keep the user engaged. When generation completes: "Your story is ready. Come, let us begin." Latency becomes ritual. How We Built It ADK Agent Orchestration The narrative pipeline is orchestrated by a Google ADK agent ( sankofa_heritage_narrator ) with 9 tool functions. The agent decides tool order at runtime and self-corrects: after planning a narrative arc, it calls validate_narrative_arc and re-plans if the validation fails. After generating segments, it can call enrich_segment to upgrade RECONSTRUCTED passages with real historical detail. A notify_user tool surfaces "thinking aloud" status messages to the frontend in real-time. A second ADK agent ( sankofa_heritage_live_narrator ) powers the Live Griot voice conversation with a filtered, conversation-only tool set. Four Gemini Models, Four Jobs Model Role Gemini 2.5 Flash Arc planning + ADK agent orchestration Gemini 2.5 Flash Image Interleaved text + watercolor image generation (core narrative engine) Gemini 2.5 Pro Preview TTS Audio narration in a warm storytelling voice Gemini 2.0 Flash Live Real-time bidirectional voice conversation Interleaved Streaming Architecture Text, images, and audio stream to the frontend via SSE. Each text segment is emitted, then its TTS generates in the background via asyncio.create_task . Audio for segment N arrives while segment N+1's text is being displayed. Text segments are split into 2-3 sentence chunks and generated concurrently with asyncio.gather for 3-4x speedup. Cinematic Frontend Built with Next.js 16, React 19, Tailwind CSS v4, and Motion. Features include word-by-word text reveal animations, cinematic blur-to-sharp image transitions with sepia-to-color reveals, act transition dividers with the Sankofa bird and gold particles, audio-synced reading highlights that progress through text using actual audio duration, a vertical scroll progress bar with act markers, and two Live Griot UI modes (glassmorphism dock over the narrative, or ambient full-screen with Ken Burns zoom). Cultural Knowledge Base A curated knowledge base provides decade-by-decade historical data for regions across West Africa (Ghana, Nigeria, Senegambia, Dahomey, Sierra Leone), the Caribbean (Jamaica, Haiti, Trinidad), and South Asia (Punjab, Bengal). The agent assesses context quality and adapts: rich knowledge base data lets the narrative lean on verified history; sparse data triggers additional grounding via research tools. Any region worldwide receives generic coverage via Gemini's knowledge. Challenges We Ran Into TTS latency was the hardest engineering problem. Generating audio for a full narrative sequentially took 30-60 seconds of dead time. Sentence-level chunking, concurrent generation, and interleaved SSE streaming brought it down to 4-5 seconds per segment, making the experience feel live rather than something you wait for. Balancing trust and immersion. Labeling content as "reconstructed" felt like it might break the storytelling flow. In practice, it does the opposite. When users see the system is honest about what it knows versus what it imagines, they lean in harder. Trust classification became a feature, not a compromise. Making the cinematic opening feel intentional, not indulgent. The ~90-second griot monologue had to justify its length by doing real emotional work: introducing the Sankofa concept, explaining the griot tradition, and building anticipation. If it felt like filler, the whole experience would suffer. Synchronizing 12 text beats to the voiceover audio required precise timestamp calibration. Accomplishments We're Proud Of Five modalities woven into a single coherent experience: text, images, voice narration, ambient audio, and live conversation An ADK agent that validates its own output and self-corrects, not just a prompt chain with tools bolted on A cinematic loading experience that converts generation latency into the emotional high point of the product Trust indicators that make AI-generated heritage narratives transparent without breaking immersion Audio-synced reading highlights that make the narration bar feel like a real audiobook player What We Learned Interleaved multimodal output demands holistic design. You can't treat text, images, and audio as separate tracks. The pipeline has to be choreographed as one experience. Agentic self-correction (arc validation, segment enrichment) produces notably richer output than a hardcoded pipeline. Latency is a design material. The cinematic intro was born from a constraint: multimodal generation is slow. The best solution to a technical limitation was a creative one. Live voice transforms the experience. Being able to talk to the narrator after reading the story crosses a threshold from content generation to something closer to presence. Built With AI Models: Gemini 2.5 Flash, Gemini 2.5 Flash Image, Gemini 2.5 Pro Preview TTS, Gemini 2.0 Flash Live Agent Framework: Google Agent Development Kit (ADK), two agents (narrative + live voice) Backend: Python 3.12, FastAPI, SSE via sse-starlette Frontend: Next.js 16, React 19, Tailwind CSS v4, Motion (motion/react) Google Cloud Services: Cloud Run (backend + frontend), Firestore (session persistence), GenAI SDK Deployment: Automated via deploy.sh, Docker Compose, deploy_windows.ps1 Voice Input: Web Speech API (browser-native) Live Voice: Gemini Live API (full-duplex) Third-Party Integrations motion/react (MIT license): Animation library for React, used for cinematic transitions sse-starlette (BSD license): Server-Sent Events for FastAPI Next.js (MIT license): React framework Tailwind CSS (MIT license): Utility-first CSS framework All third-party dependencies are open source with permissive licenses. Try It Code: https://github.com/Jeremiah-Sakuda/Sankofa Category: Creative Storyteller Blog Post: Building Sankofa: How I Used Gemini to Turn Family History into Immersive Oral Storytelling <div