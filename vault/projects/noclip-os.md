---
slug: "noclip-os"
url: "https://devpost.com/software/noclip-os"
title: "Agora"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 898
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/transportation"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Agora

> A Greek-style AI dojo for public speaking: weave cue words into a live oration while AI scores your tempo, fillers, eye contact, poise, and meaning

[Devpost](https://devpost.com/software/noclip-os) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[transportation]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[sensor_telemetry]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** css3, express.js, face-api.js, gpt-oss, groq, html5, javascript, mediarecorder, node.js, web-speech-api, webrtc, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for agora

## Body

Inspiration Scroll for ten seconds and you'll hit one: a street interview. Someone with a microphone stops a stranger, asks a simple question, and films the answer. When the answer is sharp, it's magnetic. When it isn't — when someone freezes, rambles, or fills the silence with "um, like, you know" — that clip gets shared too, and thousands of strangers quietly decide that person isn't very smart. That's what bothered us: looking dumb has never been easier. A camera can appear at any moment, and social media has turned every unscripted sentence into something that can be replayed and judged. Yet the one skill that saves you — oration, thinking clearly out loud under pressure — is almost never taught. We spend years learning to write essays and zero minutes learning to hold a thought together when a mic is in our face. We didn't want to be the person in that clip, so we built Agora — named after the agora of ancient Athens, where ordinary citizens had to stand and persuade a crowd with no script. What it does Agora is an AI oratory trainer that puts you on the spot on purpose. A round goes like this: The agora picks your topic. Leave the theme blank and the AI hands you a subject — a title plus a one-line "charge" — on a 10-second countdown to gather your thoughts. Cue words rise in tempo. As you speak, evocative words appear one at a time at a pace you set, each with a small beat beneath it (its job: "open by naming the fear," "the turn — admit a doubt"). You weave them into one coherent argument as they come. It watches and listens. Your webcam feeds a face tracker that estimates eye contact and poise; your mic is transcribed to measure words-per-minute vs. your target tempo and count filler words — the exact habits that sink a street-interview answer. A rhetoric judge scores the meaning. At the end an AI master-of-rhetoric reads your transcript against the cue words and their beats, returning a critique, a per-cue scorecard (✓/✕ — did you use each word to hit its beat?), and a single composite orator's score. It shows you perfect. Finally it writes the model speech that would have aced meaning, so you can hear the version to aim for. How we built it Frontend: vanilla HTML/CSS/JS — no framework, no build step — with a marble-and-bronze "Greek orator" theme and a fluted-column stele where each cue word is "carved." Backend: a small Node + Express server that proxies Groq so the API key never touches the browser, with four endpoints: /api/topic, /api/cues, /api/transcribe, /api/feedback. Topic, cues, and judging: Groq's openai/gpt-oss-120b, prompted to return strict JSON — topics with a charge, cue+beat pairs ordered as a rising rhetorical arc, and a verdict with the meaning score, per-cue hits, and the model speech. Speech recognition: a hybrid pipeline — the browser's Web Speech API gives a live preview while MediaRecorder captures the audio and sends it to Groq Whisper (whisper-large-v3-turbo) at the end for the authoritative transcript used in scoring. Face tracking: face-api.js (TinyFaceDetector + 68-point landmarks); we estimate head yaw and face-centering for eye contact, and track face-box jitter for poise. Challenges we ran into The browser's speech API was sabotaging the whole idea. Web Speech is Chrome-only, drops out mid-session, and — worst of all — silently deletes "um" and "uh" before you ever see them, which broke our entire filler-word mechanic. We fixed it by recording the audio and transcribing with Groq Whisper, prompt-biased to keep disfluencies, so the fillers survive and it works in any browser. Estimating eye contact without a heavy gaze model — we derived a "looking at you" heuristic from 2D landmarks (head yaw + how centered the face is) instead. Live vs. batch: Whisper is batch, not streaming, so we kept a live preview for feel and reserved the accurate transcript for the verdict. Reliable structured JSON from the model for topics, cue+beat lists, and a multi-part verdict — solved with strict prompts, fence-stripping, and local fallbacks so the app never hard-fails. A classic last-mile bug: a new screen blanked the whole page because it wasn't registered in our screen router — it hid every screen and then crashed on the missing one. One line to fix, and we hardened the router so it can't recur. Accomplishments that we're proud of A complete loop that runs end-to-end in the browser: it picks a topic, paces you with cue words, captures camera and mic, transcribes you accurately across browsers, and returns delivery metrics plus an AI judgment of your meaning — and then shows the model speech to aim for. It also degrades gracefully: with no API key it still runs on local fallbacks, so it never just breaks in a demo. What we learned How to prompt models into reliable structured JSON, the browser media stack (getUserMedia, MediaRecorder, the Web Speech API), the real tradeoffs between streaming and batch speech recognition, and how to turn something fuzzy like "good delivery" into a concrete, explainable scoring rubric. What's next for Agora Use Whisper's word-level timestamps to score pauses and "ease"; feed the cue-hit ratio directly into the score so missed beats cost points; add a leaderboard and saved history to track improvement; and ship one-click deploy with multi-language support. <div