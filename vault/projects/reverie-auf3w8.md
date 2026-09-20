---
slug: "reverie-auf3w8"
url: "https://devpost.com/software/reverie-auf3w8"
title: "Reverie"
hackathon: "FigBuild 2026"
organization: "Figma"
winner: true
words: 1172
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Reverie

> Every dream, a revelation.

[Devpost](https://devpost.com/software/reverie-auf3w8) · hackathon [[FigBuild 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[health_clinical]] [[mental_health]] [[scientific_research]] [[security_privacy]]
**user** [[researcher]]
**substrate** [[geospatial]] [[video_visual]]

**stack** claude, figma

## How they structured the write-up

- the spark
- what we built
- how we built it
- the hardest parts
- what we learned

## Body

Reverie - Every dream, a revelation. Reverie App EyeMask VR Experience (using Figma Make) Reverie: Every dream, a revelation. The Spark It started with a feeling most of us know but never talk about: waking up with the certainty that something important just happened — and watching it dissolve before you can reach for it. We spend roughly 26 years of our lives asleep . During REM sleep, the brain enters its most honest state — no social performance, no logical constraints, no ego editing what gets through. Neuroscientists like Matthew Walker have shown that REM is when the brain processes emotional memory, strips the stress from difficult experiences, and makes the loose associative connections that produce creative breakthroughs. The periodic table, the structure of the double helix, the opening chapter of Frankenstein — all of them came from dreams. And yet we have built an entire industry around optimizing sleep — tracking heart rate, sleep stages, breathing patterns — while completely ignoring what actually happens inside it. We've optimized the container and ignored the contents entirely. The question that started Reverie was simple: what are you losing every morning? What We Built Reverie is a dream recording and self-discovery platform consisting of a smart sleep mask and a companion mobile app. The mask captures physiological proxies for REM sleep — infrared eye tracking, EEG dry electrodes, HRV, and skin conductance — and uses Targeted Memory Reactivation (TMR) to gently influence dream content through audio and haptic cues during REM cycles. The app turns that data into something meaningful: a personal library of your subconscious, organized like a record collection. Each night becomes a CD. Each month becomes an album. Over time, patterns emerge — emotional themes, recurring imagery, the things your waking mind has been quietly avoiding. We designed for three use cases, each building on the last: Curiosity — for users like Emily, an undergrad who keeps waking up with the feeling that something important just slipped away. No agenda required. Just: what did I dream? Creative breakthroughs — for users like Ryan, a filmmaker stuck on an opening sequence for three months. He sets an intention before sleep. In the morning, Reverie surfaces a fragment: the sky was the floor of an aquarium — light filtering down through salt water, something vast moving slowly overhead. He films it the next week. Self-discovery — for users like Priya, who has been in therapy for a year struggling to articulate her relationship with her parents. After six weeks of recordings, Reverie's pattern map shows that 80% of her high-anxiety dreams cluster on Sunday nights — the night before her weekly call home. Her subconscious already knew. Reverie gave her the evidence. How We Built It We approached Reverie as a full product design exercise — from neuroscience grounding to interaction design to hardware concept. The science first. We grounded every design decision in peer-reviewed research. REM emotional processing (Walker, Berkeley). Threat simulation theory (Revonsuo). Memory consolidation and weak associative connections (Barrett, Harvard). Targeted Memory Reactivation as the mechanism for dream influence. We were careful about what we could and couldn't claim: patterns over time are a real signal; single-night interpretation is not. That constraint shaped the entire product — the most defensible and meaningful screen in the app is the monthly album view, not the nightly recap. The design system. We built a visual language that needed to feel both intimate and rigorous — like a journal that takes itself seriously. Three typographic voices only: a serif italic for emotional content, small-caps sans-serif for identity and labels, tracked Helvetica Neue for all metadata. An emotion color system — $\text{Anxiety} = \textcolor{#7B5EA7}{\blacksquare}$, $\text{Joy} = \textcolor{#C9A84C}{\blacksquare}$, $\text{Calm} = \textcolor{#5A9E7C}{\blacksquare}$ — that runs consistently from the CD visuals to the filter chips to the insight lines. A warm neutral background ( #f5f2ee ) instead of white, so nothing feels clinical. The CD metaphor. Dreams needed a container that felt personal and collectible, not like health data. A vinyl record library was the answer: each night a CD, each month an album cover generated from the emotional palette of that month's dreams. The metaphor does real functional work — ring density encodes vividness, an arc around the center hole indicates a lucid dream, color encodes dominant emotion. You can read a CD at a glance before you tap into it. The onboarding. The hardest design problem was the privacy screen. We're asking users to wear a recording device on their face while they sleep — the most intimate ask any app has ever made. We designed the privacy and consent screen to come before mask pairing, not after. Users choose their recording level (full, emotions only, minimal) before they give us anything. The copy leads with the thing that matters most: "Your dreams belong to you. Always." The Hardest Parts What we can't promise. Dreams are not a direct window into the psyche. A single night tells you almost nothing. Patterns over 6-8 weeks tell you something real. Resisting the temptation to over-interpret — and designing an app that communicates appropriate epistemic humility without feeling cold — was a constant tension. The insight line "Anxiety has surfaced 6 times this month — often near familiar places" is carefully worded. It describes a pattern without diagnosing a cause. That line took longer to write than almost any other part of the app. The edge cases that keep us honest. The breakup dream, logged and surfaced in a monthly pattern while someone's new partner is holding their phone. The trauma resurfacing — the app accurately detecting a recurring nightmare cluster and surfacing it as an insight at exactly the wrong moment, with no support infrastructure around it. The user who becomes so invested in their dream data that they start making real decisions from single data points. These aren't hypotheticals. They're inevitable at scale. We don't have complete answers — but naming them explicitly is what separates a concept from a product someone would actually trust. The first night problem. Everything that makes Reverie meaningful requires longitudinal data. The app is at its best after 6 weeks. But a user's first morning — when they wake up excited after wearing the mask for the first time — is the most vulnerable moment in the entire user journey. We designed for it specifically: a first-night screen that doesn't pretend to have insights yet, but makes the user feel the shape of what's coming. What We Learned The most important insight came from the neuroscience, not the design: the brain during REM sleep is not replaying your day. It's editing it. Stripping the emotional charge from difficult memories, forging connections between things that don't obviously belong together, rehearsing social threats in a safe environment. It is, in the most literal sense, doing exactly what we spend our waking hours paying therapists and coaches and journaling practices to help us do. We already have the tool. We just haven't been watching. Reverie is the infrastructure for finally paying attention. <div