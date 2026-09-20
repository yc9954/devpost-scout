---
slug: "vibesb2b"
url: "https://devpost.com/software/vibesb2b"
title: "vibesB2B"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 742
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# vibesB2B

> Vibe check the Zoom - 10x revenue

[Devpost](https://devpost.com/software/vibesb2b) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
  <sub>weak: realtime_stream</sub>
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[transcript_audio]] [[video_visual]]

**stack** attio, electron, flask, gemini-api, keras-tf, mastra, mediapipe, ngrok, node.js, opencv, python, recall.ai, slack, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

our techstack vibesB2B Inspiration Most people walk away from meetings, presentations, or pitches with only a vague sense of how they did. Were they engaging? Did they confuse their audience? Did they hold attention, or lose it? That’s why we built vibesB2B , a pitch reflection and coaching agent that synchronizes transcripts with emotion analysis to show not just what you said, but how it landed. By matching timestamps from transcription with audience emotion signals, the app highlights key moments: what was said, how the room reacted, and where things went well or could improve. It then provides structured feedback so presenters can refine their delivery and learn from every session. This ties directly into the Curator’s Cause track , since stronger communication leads to better education, clearer teamwork, and more effective collaboration, outcomes that ripple outward and make groups more capable together. It also aligns with the Ergo sponsor track , because vibesB2B is more than analytics, it is a productivity agent built on Mastra that turns raw meeting data into actionable coaching insights . By automatically linking words, reactions, and feedback, it helps people work smarter, present better, and ultimately make every meeting more impactful. What it does vibesB2B acts like a personal meeting coach . From the user’s perspective, it works like this: You open the lightweight Electron desktop app , which automatically detects and records your meetings. Once the meeting ends, vibesB2B processes the recording and transcript. It generates a timeline showing what you said, when you said it, and how your audience reacted. You receive personalized coaching notes , explaining: Key moments where you engaged your audience, Spots where people seemed confused or disengaged, and Concrete suggestions for how to improve your delivery next time. The results are delivered back into the tools you already use such as Slack, Docs, and Attio CRM through the Mastra agent framework , so the feedback is seamlessly integrated into your workflow. In short, you walk away from every meeting not with guesswork, but with actionable insight into how your message landed and how you can grow as a communicator. How we built it Behind the scenes, vibesB2B is powered by a multi-layer AI pipeline orchestrated with Mastra: Capture Layer → The Electron app uses the Recall.ai Desktop SDK to detect meetings, record audio and video, and upload them when the session ends. Transcription Layer → Speech is transcribed with AssemblyAI , providing accurate word-level timestamps for alignment. Vision and Emotion Analysis → Recorded video frames are decoded with OpenCV, analyzed with MediaPipe Face Mesh to extract 468 landmarks, and passed through a ResNet50 and LSTM model trained on AffectNet and Aff-Wild2 to classify emotions. Custom brow-furrow metrics capture confusion beyond standard FER models. Synchronization Layer → Transcript text and emotion outputs are merged by timestamp, creating a unified timeline of what was said and how people reacted. LLM Coaching Layer → Gemini consumes this timeline to generate structured feedback, phrased in a supportive, coaching-oriented style that users can act on. Orchestration Layer → The Mastra agent framework ties everything together, routing results into Slack, Docs, and Attio CRM. This makes vibesB2B feel less like an isolated tool and more like a true productivity agent embedded in pre-existing workflows. All processing happens after a meeting ends, so a 30 to 60 minute meeting can be fully analyzed and summarized within a few minutes. Challenges we ran into Social and business challenge: Feedback can feel like judgment. We had to design outputs to feel supportive and constructive, like coaching, not criticism. Emotion detection gap: Standard FER models do not include “confusion” or “engagement.” We solved this by mapping combinations of basic emotions and adding brow furrow geometry as a custom confusion metric. Integration pain: Electron, Mastra, Recall, AssemblyAI, Flask, and SQLite all spoke slightly different “languages.” We spent hours debugging mismatches in formats, timing, and async communication. Transcription limits: Recall.ai’s live video stream often dropped to around 2 fps or became corrupted. After many experiments, we pivoted to analyzing recorded meetings, which turned out to be a better fit for reflection and coaching anyway. Accomplishments that we're proud of Delivered a sophisticated multi-modal AI pipeline that combines computer vision, temporal modeling, LLM summarization, and workflow orchestration. Built a synchronized transcript + emotion timeline , turning abstract metrics into practical coaching feedback. Pivoted fast when live transcription broke, reframing the product toward post-meeting reflection, making it both more stable and more valuable. <div