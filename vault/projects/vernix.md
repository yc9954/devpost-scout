---
slug: "vernix"
url: "https://devpost.com/software/vernix"
title: "Blabber Coach"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 646
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "substrate/sensor_telemetry"
---

# Blabber Coach

> Full-voice mock interview coach. Upload a resume, choose a domain and difficulty, speak your answers BlabberCoach listens, pushes back, then tells you exactly what to fix.

[Devpost](https://devpost.com/software/vernix) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[labor_employment]]
**substrate** [[sensor_telemetry]]

**stack** amazon-web-services, javascript, next.js, node.js, nova, react, tailwindcss, typescript

## How they structured the write-up

- building blabbercoach: a voice-first ai interview coach

## Body

Building BlabberCoach: A Voice-First AI Interview Coach Inspiration BlabberCoach started from a pattern I kept noticing while helping friends prepare for interviews. Many candidates are technically strong but still struggle during live interviews. The issue usually isn’t knowledge — it’s delivery under pressure : pacing, filler words, confidence, and clarity. Most interview preparation tools are text-first . They help candidates write answers, but they don’t train the part that often determines interview outcomes: spoken communication . So I decided to build BlabberCoach , a voice-first interview simulator that lets candidates practice interviews the way they actually happen — through real-time conversation. System Design BlabberCoach is built as a multi-agent AI pipeline that simulates a realistic technical interview. The system consists of several coordinated stages. Resume Parsing and Profile Extraction The system begins by analyzing the candidate’s resume to extract relevant signals such as: skills technologies experience level target roles This enables the interview to be personalized to the candidate's background rather than relying on generic questions. Intelligent Question Generation Questions are generated dynamically based on: role or domain candidate experience level selected difficulty This allows the system to produce context-aware technical questions and adaptive follow-ups . Live Voice Interview The core feature is a real-time bidirectional voice interview . During the interview the system: transcribes the candidate’s speech maintains conversation context generates follow-up questions adapts the conversation flow The goal is to create an experience closer to a real technical interview rather than a chatbot interaction . Post-Interview Evaluation After the session ends, BlabberCoach generates a structured feedback report including: quote-linked feedback communication analysis answer rewrites actionable improvement suggestions This helps candidates clearly understand how to improve before their next interview . What I Learned One of the biggest lessons from building BlabberCoach was that AI reliability matters as much as model capability . To make the system reliable in production-like workflows, several safeguards were necessary: strict schema validation for model outputs prompt contracts to maintain predictable responses graceful fallbacks when validation fails Without these guardrails, even powerful models can create fragile systems. Another important realization was how much UX sequencing influences perceived performance . For example: performing interview setup while precomputing question plans providing progressive analysis feedback visualizing results with clear scoring rubrics These improvements significantly increased user trust and responsiveness. Challenges Building a real-time AI interview system introduced several technical challenges. Real-Time Voice Orchestration Maintaining natural conversation required coordinating: speech recognition language model responses voice synthesis while keeping latency low enough for fluid conversational turn-taking . Infrastructure Constraints The system needed to work within serverless environments and WebSocket-based communication , which required: managing session state handling real-time message streams implementing environment-based fallbacks Evaluation Quality Another difficult challenge was converting qualitative speech signals into useful metrics without introducing noise. The scoring system had to balance measurable signals with contextual understanding. Some signals are intentionally explicit. Scoring Signals Filler Word Rate $$ \text{Filler Rate} = \frac{\text{filler_count}}{\text{total_words}} \times 100 $$ This measures the percentage of filler words such as um , uh , or like . Words Per Minute $$ \text{WPM} = \frac{\text{word_count}}{\text{duration_seconds}/60} $$ This evaluates speaking pace to determine whether a candidate is speaking too quickly or too slowly. Overall Interview Score $$ \text{Overall Score} = 0.40C + 0.25Q + 0.20V + 0.15D $$ Where: (C) = Content quality (Q) = Communication clarity (V) = Vocabulary and articulation (D) = Delivery and confidence These signals help make scoring transparent and explainable rather than a black-box evaluation. Final Thoughts BlabberCoach was built to address a simple but overlooked problem: technical preparation rarely trains verbal performance . By combining voice interaction, AI evaluation, and explainable feedback , the goal is to make interview preparation closer to the real experience candidates face . Building the project reinforced an important lesson: effective AI products depend not only on model capability, but on reliable system design around the model . <div