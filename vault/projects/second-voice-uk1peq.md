---
slug: "second-voice-uk1peq"
url: "https://devpost.com/software/second-voice-uk1peq"
title: "Second Voice"
hackathon: "OpenAI Build Week"
organization: "OpenAI"
winner: true
words: 375
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/transcript_audio"
---

# Second Voice

> A zero-training AI communication aid that turns unclear speech from people with dysarthria into clear, confirmable sentences using GPT-5.6, then speaks them aloud.

[Devpost](https://devpost.com/software/second-voice-uk1peq) · hackathon [[OpenAI Build Week]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[transcript_audio]]

**stack** api, codex, gpt-5.6, openai, speech-to-text, text-to-speech

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for second voice

## Body

Inspiration Dysarthria affects speech clarity for a huge range of people. Most ALS patients eventually develop it, along with over half of children with cerebral palsy and a large share of stroke and Parkinson's patients. Existing tools like Voiceitt ask users to record 50+ phrases before they even work. We wanted something that works from the first sentence, with zero training, and that never puts words in someone's mouth without their okay first. What it does Second Voice listens to unclear or partial speech, then combines the transcript with the user's personal phrasebook and the current situational context to reconstruct what they most likely meant. GPT-5.6 proposes 2-3 candidate sentences ranked by confidence. The user picks (or edits) one with a single low-effort action, a confirm-before-speak step, and only then does the app speak it aloud via text-to-speech. Nothing is said on the user's behalf without that explicit confirmation. How we built it Second Voice was built with Codex from the first line of code. The reconstruction step (transcript, phrasebook, and context in; ranked candidate sentences out) runs on GPT-5.6, which is the core reasoning engine of the app rather than a bolt-on. Speech capture uses transcription, and output uses TTS, but the sentence-level understanding and disambiguation is GPT-5.6's job. Challenges we ran into Getting reconstruction to feel fast enough for real conversation while still giving the user a meaningful moment to confirm or correct was the hardest balance. Ambiguous or very fragmented input (common with more severe dysarthria) also required tuning how much weight to give the phrasebook versus the raw transcript. Accomplishments we're proud of Second Voice needs zero enrollment or training recordings before it's usable, a real contrast to training-heavy tools like Voiceitt. The confirm-before-speak loop also gives users control and dignity: the app never speaks for them without a clear go-ahead. What we learned Small UX decisions, like how many candidate sentences to show, or how much friction the confirm step adds, matter enormously for a tool meant to be used by someone with limited motor control, often mid-conversation. What's next for Second Voice We'd like to explore lower-latency realtime transcription and letting GPT-5.6 proactively suggest new phrasebook entries based on recurring context, without changing the core zero-training, confirm-before-speak experience. <div