---
slug: "watcher-nstuq1"
url: "https://devpost.com/software/watcher-nstuq1"
title: "Watcher"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 490
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# Watcher

> Watcher turns ordinary security cameras into an AI guard that spots danger the moment it happens and calls for help on its own.

[Devpost](https://devpost.com/software/watcher-nstuq1) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[provenance_signing]] [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**substrate** [[video_visual]]

**stack** bland.ai, computer-vision, gpt-4, nextjs, openai, react, resend, supabase, tailwindcss, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next

## Body

Inspiration Most security cameras are only useful after something has already gone wrong. Someone has to scrub through hours of footage to find the moment that mattered, and by then the chance to actually help has passed. We wanted cameras that watch with you, notice trouble the second it starts, and raise the alarm without waiting for a human to be staring at the right screen. What it does Watcher is an AI video surveillance platform that detects dangerous events in real time and alerts security on its own. It analyzes live camera streams or uploaded footage, flags things like medical emergencies, violence, and suspicious activity, and then fires a full alert pipeline: a spoken alert, an email with the clip and context, an in app inbox entry, and an optional AI voice call that reports the incident and can answer follow up questions. Every event is logged to an audit history, so there is a clear record for review and evidence. How we built it The dashboard is a Next.js and TypeScript app with Supabase handling auth and storage. Operators see a grid of camera feeds with an event feed tied to each camera's playback time, so clicking an event jumps the video straight to the moment it happened. Frames are sampled from the live stream or an upload and sent to OpenAI's vision model, which decides whether something dangerous is happening and writes a short description of what it sees. When an event fires we fan out to email through Resend, spoken alerts, and the inbox, and the operator can press Call Security to place an AI voice call through Bland that already knows the event type, location, timestamp, and a description of the person involved. Challenges we ran into Deciding what counts as a real incident without drowning operators in false alarms took a lot of tuning. Keeping the event feed in sync with each camera's playback time, so the right events light up at the right second, was fiddly. And wiring a live voice agent that already knows the context of the incident, instead of starting from a blank slate, took some careful plumbing. Accomplishments that we are proud of A camera feed can go from a normal scene to a detected incident, a ringing alert, and a voice agent reporting it to security in a matter of seconds, with no one watching the screen. Seeing that whole loop fire on its own for the first time was the moment it felt real. What we learned We learned a lot about treating video as a stream of decisions rather than just footage, about designing alerts that people will actually trust and act on, and about keeping an audit trail that holds up when it matters. What's next More camera integrations, smarter on device filtering to cut bandwidth, and richer incident reports that bundle the clip, the description, and the response into a single shareable record. <div