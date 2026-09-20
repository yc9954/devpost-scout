---
slug: "senya"
url: "https://devpost.com/software/senya"
title: "Senya"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 849
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Senya

> Making music something you can feel, see, and sign.

[Devpost](https://devpost.com/software/senya) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** claude, lifeprint, numpy, opencv, pika, pillow, python, torch, whispr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for senya

## Body

Inspiration On February 12, 2023, the Super Bowl Halftime Show featuring Rihanna delivered a record 113 million viewers. But it wasn't her performance that captured the attention of most — it was her ASL interpreter. Justine Miles made the performance accessible to the Deaf and hard-of-hearing community, and in doing so went viral, exposing millions of hearing viewers to the expressiveness of American Sign Language for the first time. That moment crystallized something for us: ASL interpretation of music shouldn't be a once-a-year spectacle reserved for the biggest stages. Every song, for every person, should be able to sign. Senya was born from the idea that the gap between a song and its ASL performance could be closed by software, making music a shared experience rather than a divided one. What it does Senya transforms any song into a synchronized ASL music video. You give it lyrics (or just an audio file) and the original song, and it returns a complete video of a signer performing the lyrics in American Sign Language, timed to the music, with karaoke-style captions burned in. Under the hood it transcribes the lyrics with timestamps, translates English into ASL gloss, fetches real ASL signing clips for each sign, stretches them to match the song's pacing, stitches them into one continuous performance, overlays the original music, and adds synced captions, producing a shareable video that makes any track accessible and engaging for the Deaf and hard-of-hearing community. How we built it Senya is a seven-stage Python pipeline. Stage 1 uses OpenAI Whisper (or a text parser) to turn lyrics into timed words. Stage 2 uses Anthropic's Claude (claude-sonnet-4-6) to translate English into ASL gloss, since ASL has its own grammar and word order rather than a one-to-one mapping from English. Stage 3 resolves each gloss token to a real signing clip by fetching GIFs on demand from Lifeprint (Dr. Bill Vicars' ASL University), converting them to MP4 with Pillow and OpenCV while preserving each frame's native timing, and caching the resulting CDN URLs so no sign is ever fetched twice. Stages 4 through 7 run entirely on Pika's REST API: generate_reference_video takes the stitched clips and overlays them onto the Pika avatar to give a realistic concert-feel, edit_speed adjusts clip timing at the phrase level, edit_concat stitches clips together (batched to respect the 24-clip limit), edit_audio_mix overlays the original song, and add_captions burns in synced karaoke lyrics. The final output is a single Pika CDN URL. Challenges we ran into The biggest challenge was getting Pika to sign accurately at all. Our first approach was to fine-tune a model on MLASL, a dictionary of English words mapped to ASL videos that is widely used in research. That quickly proved unworkable: Pika is closed source, so we had no access to the model weights and no way to fine-tune. We pivoted to Pika's generate-reference-video tool, using Lifeprint's videos as the reference. Because Lifeprint features a consistent signer against a consistent background, Pika was able to reproduce the signs accurately and place that signing within a concert-style environment, which was exactly the result we were after. From there, the focus shifted to stitching the generated clips into one continuous performance. We made strong progress getting portions of the song working, and refined our approach to timing and tempo to keep the signing synchronized to the music across the track. Accomplishments that we're proud of We're proud that Senya uses real ASL rather than synthetic avatars or approximations that the Deaf community has long criticized. We built an on-demand architecture that requires no multi-gigabyte dataset download: each sign is fetched the first time it's needed and cached forever after, so the system gets faster the more you use it. And we got an end-to-end pipeline working across two AI APIs and a video editing API, turning a raw song into a captioned, music-synced ASL performance with a single command. What we learned We learned that ASL is a full language with its own grammar, not a signed transcription of English — which is why the gloss translation step matters so much and why naive word-for-word mapping fails. We got hands-on with the realities of programmatic video editing: frame timing, aspect ratios, concat limits, and audio mixing each carry constraints that shape the whole architecture. And we learned that accessibility engineering is full of trade-offs between sign authenticity and coverage, musical timing and sign readability, where the right answer is usually a thoughtful fallback rather than a perfect solution. What's next for Senya Next we want to move from stitched real-sign clips toward smoother transitions between signs, since signing is continuous rather than a sequence of discrete words. We'd like to expand sign coverage beyond Lifeprint by integrating additional datasets (like How2Sign) to shrink the fingerspelling fallback rate. We're also interested in capturing ASL's non-manual markers, which are facial expression and body movement carry grammatical and emotional meaning that static clip-stitching loses. Longer term: real-time signing for live performances, support for sign languages beyond ASL, and a community feedback loop so Deaf signers can help improve translation quality. <div