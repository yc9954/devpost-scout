---
slug: "pigeon-umg3xe"
url: "https://devpost.com/software/pigeon-umg3xe"
title: "Pigeon"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 562
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# Pigeon

> Pigeon maps city infrastructure issues in 3D using phone calls, helping rideshare, delivery, and city services avoid disruptions through AI-powered alerts and real-time coordination.

[Devpost](https://devpost.com/software/pigeon-umg3xe) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[civic_government]] [[labor_employment]] [[transportation]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[transcript_audio]]

**stack** css, flask, gemini, google-maps, javascript, python, react, sql, supabase, typescript, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for data pigeon

## Body

Inspiration Every day, citizens spot potholes, blocked sidewalks, and broken signals—but those reports get buried in outdated 311 systems and disconnected city workflows. Meanwhile, departments operate in silos, unaware of overlapping construction plans. The result? Delays, duplicated work, and unsafe streets. We built Pigeon to change that. Our system captures public complaints in real time through an AI agent and dynamically maps any complaints automatically—cutting friction between insight and action. But that’s only part of the problem. The real-world impact goes far beyond city hall. In fact, Waymo recalled over 1,000 of its autonomous vehicles after they collided with things like low level construction barriers—despite having advanced perception systems. The issue wasn’t just sensors. It was a lack of reliable, forward-looking infrastructure data. That’s where Pigeon comes in. Whether it’s AVs, rideshare, or last-mile delivery, mobility operators rely on accurate, up-to-date road conditions to make real-time decisions. When cities fail to communicate lane closures or planned disruptions, it’s gig workers and passengers who pay the price. We bridge that gap—providing structured, city-verified data to both public agencies and private mobility platforms—so everyone can move smarter, safer, and more efficiently. What It Does Data Pigeon is an AI-powered infrastructure intelligence dashboard for cities. It: 📞 Automatically transcribes and analyzes 311 calls using Whisper + Gemini to extract hazards and suggested locations. 🗺️ Pinpoints reports on a 3D map using NLP + interactive confirmation links sent to callers. 🧩 Identifies overlapping infrastructure projects across departments, preventing costly delays and redundancies. 🔁 Pushes real-time updates to mobility companies (e.g., Uber, Google Maps, DoorDash) via API so they can reroute drivers based on live street conditions. 💬 Includes a built-in chatbot trained on city alerts, enabling teams to ask natural language questions like: "What road closures overlap with planned events this weekend?" 💸 Features budget and asset tracking to help cities see not just what's being built, but how well it’s being managed. How We Built It Frontend: React + Tailwind + 3D GlobeKit + Google Maps 3D APIs for immersive city visualization. Backend: Flask + Supabase for data storage and authentication. AI/NLP: Used OpenAI Whisper for transcription of incoming calls. Gemini Pro to summarize, extract addresses, and classify complaint types. Mobility Sync: Exposed clean GeoJSON endpoints to allow Google Maps & delivery platforms to ingest our alerts. Challenges We Ran Into Gemini’s rate limits & inconsistent output required adaptive prompt tuning. Geolocation from raw audio was tricky; users don’t always mention cross-streets clearly. We solved this with fallback mapping links. Ensuring 3D map accuracy for reports with partial or noisy location data. Accomplishments We’re Proud Of Seeing our tool map a citizen's vague voicemail onto a precise city block fully automatically felt like magic. Successfully showing two conflicting infrastructure projects on the same road segment and flagging it in real time. Creating a bridge between city planning and the delivery economy's needs. What We Learned Human problems need human-first interfaces. By simplifying city workflows, we empower both officials and citizens. The best civic tech isn’t just for governments it includes Uber drivers, delivery couriers, and commuters. What’s Next for Data Pigeon Pilot our system with a real city department (we’ve already received interest!). Build native integrations with Google Maps and Uber APIs. Expand multilingual support for 311 calls across diverse communities. Add predictive insights: e.g., "Which neighborhoods will see the most disruption next month?" <div