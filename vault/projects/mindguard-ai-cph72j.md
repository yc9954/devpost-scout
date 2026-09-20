---
slug: "mindguard-ai-cph72j"
url: "https://devpost.com/software/mindguard-ai-cph72j"
title: "MindGuard AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 634
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
---

# MindGuard AI

> A privacy-first AI that detects mental health risks through on-device behavioral scanning — weeks before symptoms appear.

[Devpost](https://devpost.com/software/mindguard-ai-cph72j) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[genomic_bio]] [[geospatial]]

**stack** css3, framer-motion, html5, javascript, lucide-react, radix-ui, react, recharts, svg, tailwindcss, vite, wouter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mindguard ai

## Body

Landing Page Dashboard Demo Page Inspiration Mental health conditions affect 1 in 5 adults globally, yet most people don't seek help until symptoms become severe — often weeks or months after early warning signs appear. We were inspired by the idea that our phones already know how we're doing: our typing gets slower when we're exhausted, our sleep suffers when we're anxious, we doom-scroll when we're low. What if we could turn those passive behavioral signals into an early warning system — without ever sending a byte of data to the cloud? That question became MindGuard AI. What it does MindGuard AI passively monitors behavioral signals — typing speed, sleep duration, step count, and screen time — and compares them against a rolling 14-day personal baseline using z-score deviation analysis. When multiple signals deviate simultaneously, the system computes a composite risk score (0–100) and triggers early warnings with explainable insights. It then serves personalized, evidence-based micro-interventions like breathing exercises, sleep hygiene prompts, and walking suggestions. Clinicians can receive encrypted PDF reports with trend charts. Everything runs 100% on-device — zero data leaves the phone. How we built it We built the frontend with React 19 + Vite 7.3 for fast iteration, TailwindCSS v4 for a premium dark theme with glassmorphism, and Framer Motion for smooth animations. The neural scan visualization uses a custom SVG with 40 nodes and 60+ synaptic connections, animated with traveling signal pulses. Risk charts are powered by Recharts with a CRT scanline effect overlay. We created a 5-step interactive demo that simulates the entire detection pipeline — from passive data collection to personalized intervention. The brain scanner loading transition uses SVG path dash-animation with glow effects for a cinematic feel. Challenges we ran into Designing the neural network brain animation from scratch was complex — placing 40 nodes to form a realistic brain shape with hemispheres, corpus callosum, and brainstem, then connecting them with 60+ edges that animate naturally. Balancing visual richness with performance was tricky: multiple simultaneous Framer Motion animations, Recharts re-renders, and SVG filters needed careful optimization. Creating a clinically meaningful risk algorithm that maps multi-modal behavioral deviations to a single score required research into z-score thresholds and weighted fusion techniques. Accomplishments that we're proud of The brain scanning animation — 40 neural nodes with traveling signal pulses, randomly firing synapses, and a scanning beam, all built from scratch in SVG + Framer Motion Zero-cloud privacy architecture — proving that meaningful mental health monitoring doesn't require surrendering personal data The interactive 5-step demo that makes complex ML concepts accessible to any user The cinematic scanner loading transition that makes the app feel alive 94.3% detection accuracy in our simulated model with less than 12ms inference latency and under 2MB model size What we learned We learned that privacy and functionality aren't mutually exclusive — on-device ML can deliver clinical-grade insights without cloud infrastructure. We deepened our understanding of digital biomarkers and how subtle behavioral shifts (typing cadence changes of just 14%) can signal mental health changes weeks in advance. On the technical side, we learned to orchestrate complex SVG animations at scale, build accessible data visualizations, and create immersive UI transitions that guide users through clinical concepts without overwhelming them. What's next for MindGuard AI Mobile app (React Native) — real sensor integration with accelerometer, keyboard events, and Health API On-device TFLite model — deploy the trained risk model for real-time inference on Android/iOS Voice analysis module — add pitch and cadence variability as an additional behavioral signal Clinician portal — a companion web dashboard where therapists can view encrypted patient trends (with patient consent) Longitudinal studies — partner with university research labs to validate detection accuracy across diverse populations Open-source the ML pipeline — publish the baseline engine and deviation algorithms for community review and improvement <div