---
slug: "yapdraw"
url: "https://devpost.com/software/yapdraw"
title: "YapDraw"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 503
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# YapDraw

> Think out loud, and see your ideas form in real time.

[Devpost](https://devpost.com/software/yapdraw) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**user** [[developer]]
**substrate** [[geospatial]] [[transcript_audio]]

**stack** dagre, deepgram, excalidraw, next.js, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for yapdraw

## Body

landing library generate your diagram Inspiration Every diagramming tool makes you work for it. Drag nodes, connect arrows, fight the layout engine. But when engineers explain a system to each other, they just talk. The other person gets it in thirty seconds. We wanted to capture that. Stop forcing people to translate their thoughts into drag-and-drop actions. Just let them talk, and have the diagram appear. What it does YapDraw is Wispr Flow for Excalidraw. Describe a system, workflow, or process out loud. It generates a clean, structured, fully editable Excalidraw diagram in seconds. What makes it more than a one-shot generator: Handles how people actually talk. Corrections, filler words, backtracking. The diagram reflects your intent, not your literal words. Truly incremental. Say "add a Redis cache" and only that changes. Say "remove the message queue" and only that disappears. Everything else stays exactly where it is. Full version history. Every AI change is snapshotted. Cmd+Z reverts the last generation without touching anything you edited manually. Three modes. Freeform (anything), System Architecture (layered service graphs with protocol labels), and Process Flowchart (decision trees, approval flows, research pipelines). How we built it The core pipeline: voice → Deepgram transcript → LLM → structured graph JSON → Dagre layout → Excalidraw canvas. Next.js for the full stack Deepgram for real-time voice transcription with silence detection Dagre for automatic graph layout from the LLM's logical graph Excalidraw as the canvas, rendering laid-out elements and allowing free manual editing Challenges we ran into Excalidraw is unforgiving with programmatic input. Its arrow elements require a precise native format. Using its own conversion utility on pre-positioned Dagre arrows produced a "Linear element is not normalized" crash on any user drag. We bypassed the converter entirely and constructed native elements manually, including generating sibling bound text elements for arrow labels (which Excalidraw requires as separate elements rather than inline properties). Incremental updates are a stateless problem. The LLM has no memory. On minor edits, it would sometimes drop existing nodes entirely. We built a safety merge that detects accidental drops and restores them, while an explicit remove field in the graph schema lets the LLM signal intentional deletions without triggering the safety restore. Accomplishments that we're proud of Building a 15-node architecture diagram incrementally across multiple voice turns and having it hold together perfectly Getting natural speech, mid-sentence corrections and all, to produce clean diagrams consistently Shipping an interaction model that genuinely feels new: think out loud, the diagram keeps up What we learned LLMs follow examples far more reliably than instructions. Every meaningful quality improvement came from better few-shot examples in the prompt, not more rules. Perceived latency matters as much as real latency. Removing the loading skeleton and replacing it with a single pulsing dot made the app feel noticeably faster without changing the actual response time. What's next for YapDraw Real-time collaboration PNG/SVG export and shareable links More diagram modes: org charts, mind maps, ER diagrams Mobile app (voice input is a natural fit for phone) <div