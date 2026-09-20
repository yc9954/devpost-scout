---
slug: "insight-vyfj5z"
url: "https://devpost.com/software/insight-vyfj5z"
title: "InSight"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1091
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# InSight

> Insight uses Meta Ray-Bans to record your every interaction, creating an AI clone of yourself that completely understands your virtual and physical relationships to streamline your work.

[Devpost](https://devpost.com/software/insight-vyfj5z) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** dlib, ffmpeg, mcp, opencv, pillow, postgress, pyannote, pyav, python, pytorch, smithery, typescript, whisper, wordware

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for insight

## Body

Inspiration As our digital lives become increasingly automated, our digital relationship data has become a less genuine reflection of ourselves. True personal human context, how we speak, connect, and interact in person, is missing from the automations that are being increasingly used. We built InSight to bridge that gap. We believe the future of AI isn’t replacing people, but reflecting them authentically. We capture both digital and physical interactions to create an real, intelligent extension of who you are. What it does InSight is your personal memory engine, a virtual clone that captures everything you see, say, and do. Using Meta Ray-Ban glasses and a custom audio-visual pipeline, it records real-world interactions, recognizes who you’re talking to, and labels every conversation with names and timestamps. Imagine being able to search your life like a Google Doc, where every moment is instantly accessible. What makes InSight stand out is how it connects your real and digital worlds. It syncs with tools like Slack, turning in-person chats and reminders into actionable insights right inside your workspace. Support for WhatsApp and Discord is on the way, allowing InSight to organize and understand your conversations across every platform you use. InSight is not just a memory tool. It’s an active collaborator that reminds you of commitments, drafts follow-ups, and schedules meetings based on your conversations. Whether you’re a student balancing projects or a professional managing a busy schedule, InSight keeps your ideas and actions seamlessly connected so you never lose track of what matters most. How we built it We built InSight as a collection of microservices, starting with a multi-stage ML pipeline for processing interactions. Due to there not being an SDK to work with Meta Ray Bans glasses, we made our own way to livestream video from the glasses to our pipeline. By livestreaming through the glasses on Instagram, we could open Instagram Live on our computers and see what the glasses were seeing. From this, we used FFMPEG to take a constant screen capture of the video. Interaction Processing Pipeline: In the background, we run a Voice Activity Detection model, which helps us figure out when the user starts having a conversation with someone. Once speech is detected, the interaction is automatically segmented and beamed to our audio and visual pipelines. Audio Pipeline: Our audio processing leverages two state-of-the-art models working in tandem. Faster Whisper performs high-accuracy speech-to-text transcription with precise timestamps, while pyannote.audio handles speaker diarization, identifying when different speakers take turns in the conversation. This generates initial transcripts labeled with generic speaker IDs ("Speaker 1", "Speaker 2") and exact timing information, which becomes crucial for downstream processing. Video Pipeline: The video pipeline employs dlib's ResNet-based face recognition with one-shot learning capabilities, meaning it can identify people from just a single reference photo. As frames are processed, we detect all visible faces, extract 128-dimensional face encodings, and match them against our database using euclidean distance metrics. The system tracks confidence scores and timestamps for when each person appears, building a comprehensive registry of everyone in the interaction. Aggregation & Speaker Matching: The magic happens when we fuse audio and video data together. Using OpenCV's optical flow analysis, we track lip movements by monitoring facial landmarks around the mouth region. For each audio segment, we calculate movement magnitude across all detected faces to determine who was actually speaking. By correlating lip movement intensity with speaker timestamps, we replace the generic speaker labels with actual names from our face recognition database. This synchronized data, transcripts with accurate speaker attribution, timestamps, and confidence scores, is then stored in our PostgreSQL database, making every interaction queryable through our MCP server interface. MCP Server. To make our interaction data accessible to Poke, we built a Model Context Protocol (MCP) server that acts as a natural language interface to our PostgreSQL database. The MCP server exposes two core tools that any MCP-compatible AI assistant can invoke: list_people (returns everyone you've ever talked to) and list_interactions_with_person (retrieves full conversation transcripts with a specific person). This architecture transforms InSight from a passive database into an active AI memory system. Instead of writing custom API endpoints or forcing users to learn query syntax, we leverage MCP to let AI assistants query your interaction history through conversational prompts. For example, you can simply ask "What did I discuss with Sarah last week?" and the AI agent automatically calls list_interactions_with_person with the appropriate parameters, retrieves the relevant transcripts, and synthesizes a natural answer. Challenges we ran into No Official SDK for Ray-Ban Meta Glasses Meta doesn't provide a developer SDK for the Ray-Ban Meta glasses' video feed. We worked around this by livestreaming through Instagram Live and using FFmpeg to capture the screen. This required detecting and cropping the feed region, handling buffering and latency, and managing connection drops—all while dealing with uncontrollable video quality and potential Instagram UI changes. Integrating with Poke Agent's Black-Box Architecture Getting the Poke agent to query our interaction data was difficult. With limited visibility into its internal processing, we treated it as a black box and iterated through trial-and-error. We experimented with tool descriptions, input schemas, and response formats until we found patterns that triggered correct behavior. Voice Capture in High-Noise Environments Real-world conversations happen in noisy places - coffee shops, streets, restaurants. Our VAD system had to distinguish actual conversations from background noise without false positives or missed interactions. We experimented with energy thresholds and frequency filtering to find the right balance. Audio quality from the Ray-Ban glasses also varies by positioning and acoustics. After multiple iterations and using multiple models, we achieved consistent performance in high-noise environments. Accomplishments that we're proud of Initially, all we were looking to do was to be able to bring the real world’s data to your technology. We are extremely proud that we were able to accomplish this through the Meta RayBan glasses, but beyond that, we were even able to make numerous integrations that take advantage of this vast dataset. In short we’re proud that we were not only able to create the data layer, but also the applications on top of that layer. What's next for InSight The number of users for wearable vision glasses is bound to grow exponentially throughout the next few years, so InSight is particularly built for the future. Similarly, the need for personalization and the need for context have been growing and are going to continue growing this decade. We see InSight as becoming the base layer for thousands of apps that are going to be built on top of us. <div