---
slug: "findx-4dvnf5"
url: "https://devpost.com/software/findx-4dvnf5"
title: "FindX"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 247
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# FindX

> FindX is an AI-powered lost and found platform that uses Google Gemini AI to automatically analyze photos of lost or found items, generate descriptions, and intelligently match them with their owners.

[Devpost](https://devpost.com/software/findx-4dvnf5) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** chart.js, cloud-firestore, dart, firebase-authentication, firebase-cloud-messaging, firebase-storage, flutter, geocoding-api, google-gemini-ai, google-maps-sdk, google-places, next.js, python, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next for findx

## Body

Location HeatMap Home Screen Push Notification Ai Matching Ai Analysis Autoposting on social media Inspiration Every year, millions of items worth over $30 billion go unreturned worldwide. Traditional lost and found systems are fragmented, manual, and disconnected. We wanted to leverage AI to transform this frustrating experience into an intelligent, automated solution. What it does FindX is an AI-powered lost and found platform that: Uses Google Gemini AI to automatically analyze photos of lost/found items Generates detailed descriptions and categories from images Intelligently matches lost items with found items using AI similarity scoring Shows a real-time location heatmap using Google Maps Enables instant chat between finders and owners Sends push notifications when items are reported nearby Auto-generates Instagram posts to spread the word Provides police integration with AI-generated FIR drafts How we built it Frontend: Flutter for cross-platform mobile app AI: Google Gemini 1.5 Flash for image analysis and matching Backend: Firebase (Auth, Firestore, Storage, Cloud Messaging) Maps: Google Maps SDK, Places API, Geocoding API Dashboard: Next.js with Chart.js for analytics Challenges we faced Optimizing Gemini prompts for accurate item identification Implementing real-time AI matching with confidence scores Handling Firestore security rules for chat functionality Balancing feature richness with app performance What we learned Deep integration of Google Gemini AI for multimodal analysis Building real-time systems with Firebase Importance of thoughtful UX for community-driven platforms What's next for FindX Integration with more social platforms Partnerships with universities, airports, and transit systems Advanced AI matching using embeddings <div