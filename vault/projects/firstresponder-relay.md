---
slug: "firstresponder-relay"
url: "https://devpost.com/software/firstresponder-relay"
title: "FirstResponder-Relay"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 394
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "substrate/transcript_audio"
---

# FirstResponder-Relay

> When 911 lines flood during a wildfire, FirstResponder Relay triages overflow calls in 13+ languages, locates callers inside active fire zones, and translates dispatcher guidance both ways real time.

[Devpost](https://devpost.com/software/firstresponder-relay) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: human_in_the_loop</sub>
**domain** [[disaster_emergency]] [[health_clinical]]
  <sub>weak: developer_tools</sub>
  <sub>weak: general_public</sub>
**substrate** [[transcript_audio]]
  <sub>weak: geospatial</sub>

**stack** anthropic-claude-sonnet-4.6, arize-ax, deepgram-aura-2, deepgram-nova-3, fastapi, mapbox, mapbox-gl-js, next.js, ngrok, openinference, python, react, redis, redis-cloud

## Body

Caller View Dispatcher View During the 2018 Camp Fire, Paradise's 911 system received 999 emergency calls in 30 minutes. Today, roughly 25% of San Francisco Bay Area residents speak a language other than English at home, and dispatchers can only fluently communicate with a handful of them. When a disaster collides with that language gap, lives are lost in the seconds it takes to find a translator. FirstResponder Relay is a multilingual AI dispatcher that absorbs overflow when human dispatchers are saturated. Callers connect from any phone with a QR code, speak in any language (we tested 13, including English, Spanish, Hindi, Punjabi, French, Japanese, German, and Mandarin), and the system: Transcribes their voice in real time with Deepgram nova-3 multilingual streaming Uses Claude Sonnet 4.6 to classify urgency (URGENT / GUIDANCE / INFO), extract the address, and detect the spoken language Geocodes the address with Mapbox and uses Shapely point-in-polygon checks to determine whether the caller is INSIDE one of three active wildfire perimeters (Twin Peaks SF, Oakland Hills, Mount Hamilton SJ) Speaks back a calming response in the caller's own language within ~2 seconds Streams the structured triage to a dispatcher dashboard that ranks calls by urgency, shows the caller pinned on a live Mapbox map relative to the fire polygons, and lets the dispatcher type or speak an English response that is translated and delivered back to the caller's phone as voice The system is explicitly positioned as decision support for overflow capacity, not a replacement for human 911 dispatchers. Every triage classification is presented as a recommendation with the caller's full transcript and an English summary alongside, so the human dispatcher always has the final call. We ran a 30-case evaluation suite spanning English, Spanish, French, Hindi, and adversarial transcription noise. Results: 90% urgency-level accuracy, 100% language detection accuracy, 100% address extraction accuracy. All Claude reasoning traces stream to Arize AX for production observability. The hardest single problem was the translation bridge. Most "multilingual" demos do speech-to-text in one language. We close the human-in-the-loop: dispatcher speaks English on a laptop, Claude translates to the caller's detected language, the caller's phone speaks it back via browser TTS (English uses higher-quality Deepgram Aura-2). The caller can keep talking; the dispatcher can keep responding. Two humans, one shared conversation, separated by language and saved by latency under three seconds end to end. <div