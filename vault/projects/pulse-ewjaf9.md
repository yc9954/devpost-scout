---
slug: "pulse-ewjaf9"
url: "https://devpost.com/software/pulse-ewjaf9"
title: "Pulse"
hackathon: "OpenAI Build Week"
organization: "OpenAI"
winner: true
words: 473
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/transcript_audio"
---

# Pulse

> An AI teammate that listens during cardiac arrest and holds the state the team leader is juggling: rhythm, shocks, drug timings, hands-off time. Deterministic engine, no LLM in the clinical loop.

[Devpost](https://devpost.com/software/pulse-ewjaf9) · hackathon [[OpenAI Build Week]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
  <sub>weak: voice_speech</sub>
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[transcript_audio]]

**stack** codex, fastapi, gpt-5.5, gpt-5.6, groq, next.js, openai, playwright, pydantic, pytest, python, react, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Inspiration I'm a cardiologist. During a cardiac arrest, the team leader is tracking rhythm, shock count, drug timings, how long compressions have been paused and which cycle we're on — all at once, in their head, while people are shouting. The tools we have record what happened. None of them understand what's happening. I wanted the thing that doesn't get tired and doesn't lose count. What it does Pulse listens to the room during a cardiac arrest and maintains clinical state. Spoken phrases become evidence. Evidence becomes clinical events. A deterministic state machine advances from those events, and the dashboard shows the team leader what's true right now and what's due next: CPR clock and cycle number, started by the words "CPR started" Rhythm and pathway — say "rhythm is VF" and it moves to the shockable branch itself Shock count, and a hands-off timer that starts climbing after every shock and keeps climbing until compressions come back Medication timeline with ACLS timing, so it surfaces "Also due: consider amiodarone" after the third shock before anyone asks A full audit trail; every accepted event can be undone It handles the way people actually speak, including the code-switched Egyptian Arabic of a real Cairo resus room, where a doctor says "الريذم VF" rather than any textbook phrase. How we built it Built with Codex across GPT-5.5 and GPT-5.6 sessions. I wrote a constitution first — AGENT.md — fixing the boundaries the agent was never allowed to cross: the AI does not own clinical state, spoken evidence is gated before it can act, and every accepted event must be auditable. Then Codex implemented one vertical slice at a time, each with tests: the state machines, the evidence and fusion layer, multilingual normalization, the confirmation policy, the audio pipeline. The architectural decision I care most about: there is no language model in the clinical loop. The LLM helps read messy speech. It never decides what happened. Clinical state is advanced by deterministic code, which is why the behaviour is reproducible and testable. Stack: FastAPI + Pydantic backend, Next.js + TypeScript frontend, pluggable speech recognition, everything runnable offline with a deterministic fake ASR so anyone can evaluate it without credentials. Challenges we ran into Real speech isn't scripted speech. The first phrase matcher worked on the phrases I wrote and failed on the phrases I say. Fixed by testing against replays of real recorded clinician speech instead of my own test strings. Silence hallucinated. Empty audio segments were producing confident transcripts that tried to mutate clinical state. That's the most dangerous class of bug in this app, and it now fails closed. Echo duplicates inflated the shock count. One shout of "shock delivered" heard twice became two shocks. There's now a deduplication window per event type — 15 seconds for shocks, 10 for CPR and rhythm. <div