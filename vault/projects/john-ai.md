---
slug: "john-ai"
url: "https://devpost.com/software/john-ai"
title: "Dealwise"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 424
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Dealwise

> Tired of wasting hours calling businesses for quotes and negotiating? Dealwise: the AI negotiator that automatically calls every vendor, haggles in real-time, and hands you the best price.

[Devpost](https://devpost.com/software/john-ai) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]] [[video_visual]]

**stack** boundaryml, browseruse, elevenlabs, lovable, python, react, supabase, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for dealwise

## Body

Browser agent finding local businesses Actual real-time call with local business to get a price quote Quotes from calls to 10 local businesses Browser agent output (step 1) Input fields for Dealwise Dealwise: The AI Price Negotiator That Calls So You Don’t Have To Inspiration We just moved to San Francisco two weeks ago and bought a secondhand couch on Facebook Marketplace… and spent days calling businesses for quotes to deep clean it. We even had one company quote us a price on the phone, then when they came tried to upsell us. From couch cleaning to car purchases, we realized the modern world still runs on phone calls —and nobody has time to spend hours on the phone with local businesses trying to get the best price. What It Does Dealwise is your AI-powered haggling sidekick . Enter a service (e.g., “plumber”, "carpet cleaning") and your zip code, and we: Scrape & call every nearby business. Get quotes populating quotes one by one from different businesses Deliver a battle-ready price list —so you can book from the lowest quote business. How We Built It Twilio for connecting the calls to a virtual number Elevenlabs for voice agent and voice prompts Lovable for UI Supabase for database BoundaryML for prompt engineering BrowserUse for the browser agent Challenges We Ran Into IVR : “Press 1 to verify, blocked most car dealership calls. Dual-tone multi-frequency signaling (DTMF) is our next step to tackle. We quickly pivot to calling home services. How to make it sound more human? : Early tests failed—vendors hung up. (attached photo) Breakthrough : Adding accents in the voice, every vendor thinks they are talking to a human after the change. Ethical Haggling : Balancing assertiveness without training AI to be rude Accomplishments We’re Proud Of Stealth Mode Success : Vendors had no clue they were talking to AI. Real-life cases : We successfully secured a few quotes from the vendor and booked appointments. Humanizing Tech : Proved “imperfect” AI voices outperform sterile perfection. What We Learned Flaws Build Trust : A slight stammer or accent makes AI feel human . IVR : Most businesses hide behind phone trees— cracking this is critical . What’s Next for Dealwise IVR : Crack DTMF so the agent can bypass the verification on the spot. Negotiation GPT v2 : Industry-tailored prompts. Scale to Warp Speed : Parallel call queues to deliver quotes in seconds. Price War Mode : Auto-negotiate by pitting vendors against each other ( “Company X offered $500—beat it or lose me” ). <div