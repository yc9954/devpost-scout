---
slug: "argus-w6i0pv"
url: "https://devpost.com/software/argus-w6i0pv"
title: "Argus"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 495
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "substrate/video_visual"
---

# Argus

> Argus combines AI, computer vision, and real-time streaming to deliver intelligent, low-latency surveillance with instant threat detection, reporting, and search across all your video networks.

[Devpost](https://devpost.com/software/argus-w6i0pv) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]] [[labor_employment]] [[security_privacy]]
**substrate** [[video_visual]]

**stack** claude, elasticsearch, gemini, groq, letta, mux, nextjs, rtmp, supabase

## How they structured the write-up

- 👀 what does argus do?
- 🧑‍💻 how we built it
- ⚔️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 🤯 what we learned
- 👁️👁️👁️ what's next for argus

## Body

Landing Page Dashboard AI Analysis & CV Video Asset view Elasticsearch with Argus Chat with Argus - Interface with your data Automated Incident Report Generation Event Analysis & Job Stats The name itself Argus comes from Argus or Argos Panoptes, a many-eyed giant in Greek mythology who's known for his perpetual vigilance, he served the goddess Hera as a watchman. Felt fitting and was a cool thing to build around! 👀 What does Argus do? Argus is the multi-tool for all your enterprise surveillance needs. 🛰️ Surveillance Input Pipeline: MUX Realtime Live streaming & VOD asset generation using RTMP streaming Supabase Edge Functions sync the MUX data stream Gemini 2.5 Pro Vision Analysis for Event & Anomaly detection off generated VOD assets Roboflow 3.0 Object Detection Computer Vision for generating bounding boxes and tracking entities within streams 🧩 Event Pipeline: Gemini & Roboflow jobs sync with MUX VOD assets creating a event timeline within the viewer & detection display Elasticsearch accessses the Supabase DB through real-time sync and populates the index to allow for semantic searching of events/anomalies Stats are populated based off of Supabase through realtime & the Elasticsearch knowledge base 💬 Interface Pipeline: The AI Chat page accesses all of the available data and allows for direct interaction through various models ( Letta Stateful Agent , Kimi K2 Instruct through Groq , Claude 4.5 Sonnet , Claude 4.5 Haiku ) Through the Chat interactions, you are able to generate Incident Reports of events & anomalies which are editable through a Tiptap Rich Markdown editor 🧑‍💻 How we built it By coding :) 🤓 ⚔️ Challenges we ran into Since Argus has so many services, you need to be running at least 4 terminals to host it locally : ngrok server to point MUX webhooks Next.js application Node worker running the workflow services & agents (Gemini, Roboflow, Elasticsearch) Containerized Docker Supabase instance with supabase edge functions Alongside the terminal suffering, we had to deal with merge conflict misery a few times.... 😭 🏆 Accomplishments that we're proud of All in all, Argus is the most fleshed out hackathon project we've made so far, it was really satisfying putting it all together and seeing it all work! As someone who's worked in Government IT & Cybersecurity (Carson), it was really cool to create something that has genuine real-world use cases and with some more overall polish could even be shipped as a full tool integrated into security workflows! 🤯 What we learned We learnt a lot about many of the tools provided by CalHacks' sponsors! We had a lot of fun tinkering around with each interface and understanding the capabilities, very cool tools and we are looking forward to spending more time working with them in the future! 👁️👁️👁️ What's next for Argus Hardware integration (into security cameras for example) Enterprise level security Entity tracking across video streams (did Person A walk from Camera 1 to Camera 3?) More automated workflows & agentic pipelines <div