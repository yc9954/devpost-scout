---
slug: "fizz-buzz"
url: "https://devpost.com/software/fizz-buzz"
title: "Fizz Buzz"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 640
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Fizz Buzz

> Roommate Confrontation Simulator

[Devpost](https://devpost.com/software/fizz-buzz) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
  <sub>weak: finance_payments</sub>
**substrate** [[transcript_audio]] [[video_visual]]
  <sub>weak: financial_record, web_dom</sub>

**stack** css, deepgram, gemini, html, javascript

## Body

home roommate confrontation Inspiration Every roommate situation eventually produces the moment — the exploded Coke in the freezer, the dishes that have been "soaking" for four days, the 2am speaker session on a Tuesday. We've all rehearsed that conversation in the shower a hundred times, then fumbled it in real life because confrontation is hard. We wanted to build something that lets you practice the hard conversation before it costs you the security deposit — or the friendship. What it does FizzBuzz is a roommate confrontation simulator framed as an RPG boss battle. You describe your grievance (e.g., "the exploding Coke incident"), optionally upload a photo of your roommate, then knock on an animated door and enter combat. You speak your grievances into the mic; your roommate — powered by Gemini AI and voiced by Deepgram — fires back with weaponized deflections, wild excuses, and gas-lighting masterstrokes. Health bars drain on both sides. You win by landing calm, specific, boundary-setting statements. Lose your cool and you take recoil damage. When the dust settles, a fight card shows your stats: STT confidence scores, boundary clarity rating, best spoken line, and personalized coaching notes on how to have the real conversation. How we built it Frontend: Vanilla JS + Vite, single-page with three screens (prep → battle → fight card), styled in a pop-art comic aesthetic Backend: Node.js + Express serving both the API and Vite in middleware mode LLM: Google Gemini generates scenario-aware roommate dialogue — compact JSON with an attack name, one-liner, and comeback Speech-to-Text: Deepgram nova-3 over WebSocket with real-time interim results, confidence scores, and endpointing detection; Web Speech API fallback Text-to-Speech: Deepgram Aura with six voice personalities that shift speed and tone based on roommate emotional state; browser speechSynthesis fallback Image processing: Gemini Vision API for the optional "forehead mode" portrait distortion Video generation: Pika API wired for seven mood-based avatar loops (idle, defensive, gaslighting, etc.) Challenges we ran into Wiring real-time bidirectional voice into a battle loop was the hardest part. Deepgram's WebSocket STT fires interim results continuously — deciding when the player is actually done speaking required tuning silence endpointing (550ms) while keeping the game from feeling laggy. We also had to synchronize TTS playback with health bar animations and sentiment meter updates without a framework managing state for us. Gemini prompt tuning was trickier than expected. Getting responses that were both funny and compact enough to be voiced in under 10 seconds took several iterations of the system prompt. The roommate has to feel unhinged but coherent. Accomplishments that we're proud of The voice loop actually works and feels alive. Hearing Deepgram voice a Gemini-generated deflection like "The Carbonation Innocence Plea" while a health bar drops is genuinely funny — which is the whole point. We're also proud of the boundary scoring system: it rewards calm, specific asks and penalizes escalation, so the game subtly teaches real conflict-resolution behavior while you're just trying to win a boss fight. What we learned Deepgram's real-time STT is remarkably fast — the latency from end-of-speech to transcription showing up is low enough to feel conversational. We learned to lean on confidence scores and interim results rather than waiting for final transcripts to keep the loop snappy. We also learned that fallback chains matter enormously in a hackathon demo: having hand-crafted excuse banks and browser speech synthesis meant the demo never fully died even when API limits hit. What's next for Fizz Buzz Pika video loops: the avatar animation pipeline is fully wired — we just need the API key configured to swap in live mood-reactive video clips Typed fallback: players who can't use a mic should still be able to fight Scenario library: pre-loaded classic roommate crimes (dishes, noise, thermostat wars, the labeled food situation) Multiplayer mode: two players, each convinced the other is the unreasonable one <div