---
slug: "d-u-see-your-vietnamese-tones"
url: "https://devpost.com/software/d-u-see-your-vietnamese-tones"
title: "Dấu - See your Vietnamese tones"
hackathon: "OpenAI Build Week"
organization: "OpenAI"
winner: true
words: 557
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/transcript_audio"
---

# Dấu - See your Vietnamese tones

> Dấu makes Vietnamese tones visible. Record a word, compare your pitch with validated contours, see the meaning your tone created, and get the exact physical fix.

[Devpost](https://devpost.com/software/d-u-see-your-vietnamese-tones) · hackathon [[OpenAI Build Week]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[structural_withholding]] [[voice_speech]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[transcript_audio]]
  <sub>weak: video_visual</sub>

**stack** chatgpt, codex, gpt-4o-transcribe, gpt-5.6-sol, gpt-image-2, gpt-realtime-2.1, gpt-realtime-2.1-mini

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for dấu - see your vietnamese tones

## Body

Tone Shapes overlays your pitch on a validated reference, then gives an immediate verdict and physical correction. Dialogue Practice shows which word changed, what it meant, and links you back to the matching tone lesson. Six Vietnamese tone contours measured in speaker-relative semitones across one normalized syllable. Four connected scenes turn isolated tone practice into useful, contextual Vietnamese conversation. Inspiration My family speaks Vietnamese. I say a word, they laugh, and I rarely know why. The reason is usually tone. ma , mà , má , mả , mã , and mạ can mean ghost, but, mother, grave, code, or rice seedling. Most apps give learners a red X without showing what their voice actually did. I wanted Dấu to show the pitch curve, explain the accidental meaning, and give one physical correction. What it does Dấu is an open-source Vietnamese tone practice lab. Tone Shapes lets learners hear a validated reference, watch its contour, record one syllable, and see both pitch curves overlaid. Cô Dấu then explains how to move the voice differently. Dialogue Practice applies those skills across four connected scenes with 26 turns and 13 learner replies. Dấu highlights changed words and links them back to their tone lessons. The core experience works without an API key: grading runs locally, while validated audio, artwork, and practice fixtures are bundled with the app. How I built it My central rule was: DSP judges the tone. The LLM coaches the learner. A browser Web Worker extracts pitch with YIN and compares it with accent-conditioned templates using constrained Dynamic Time Warping, acoustic features, energy, and voicing evidence. OpenAI models handle the tasks they are better suited for: coaching, Vietnamese transcription, reference speech, and meaning artwork. FastAPI keeps every model call server-side, behind BotID, quotas, concurrency limits, and a kill switch. Generated reference recordings must pass lexical, signal, and contour validation before they can become ground truth. 36 of 38 reference targets have passed; the two failures are withheld rather than shipped. Challenges I ran into Vietnamese ASR often recovers the intended word instead of exposing the tone that was physically spoken. In one native-speaker test, transcription normalized mả to mã , while DSP separated the contours using pitch and voicing evidence. My first server-based grader was also too slow after a cold start. Moving grading into a browser Worker removed the network round trip. Finally, two Southern reference targets still fail my validation gates. I withheld them and kept grading at the acoustic-family level rather than weakening the standard. Accomplishments that I'm proud of A complete no-key practice experience Four dialogue scenes and 52 validated recordings Immediate browser-based pitch feedback 91.7% held-out acoustic-family accuracy on the current reference corpus Honest abstention when the signal does not support a verdict About $12 in total OpenAI build spend What I learned A language model and deterministic signal processing make a better teacher together than either does alone. Pitch grading should be measurable and inspectable; explanation and drill selection are where the LLM adds the most value. I also learned that "please record again" is better than a confident wrong answer. What's next for Dấu - See your Vietnamese tones Complete the Southern reference corpus, unlock six-tone grading when the evaluation gates pass, improve Cô Dấu's word-level dialogue timing, and build a live conversation mode. Live: dau.huynhrobert.com License: MIT <div