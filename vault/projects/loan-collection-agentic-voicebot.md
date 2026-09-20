---
slug: "loan-collection-agentic-voicebot"
url: "https://devpost.com/software/loan-collection-agentic-voicebot"
title: "Loan Collection Agentic VoiceBot"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 292
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Loan Collection Agentic VoiceBot

> An agentic voicebot for helping banks and organizations by providing with call based automations.

[Devpost](https://devpost.com/software/loan-collection-agentic-voicebot) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** fastapi, groq, langchain, python, twilio, vapi.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for loan collection agentic voicebot

## Body

Inspiration Loan collection is still heavily manual, expensive, and inefficient. Financial institutions rely on agents making repetitive calls, which is slow and hard to scale. We wanted to explore whether an AI voice agent could automate these interactions while still keeping conversations natural and responsive. What it does Loan Collection Agentic VoiceBot is an AI-powered voice agent that automatically calls customers with overdue loan payments. It can understand the customer’s response in real time, hold short conversations, send payment links via SMS if they agree to pay, and log the outcome to a database. How we built it We built the backend using FastAPI (Python) with an agent-based architecture. Groq LLM handles intent detection and response generation. Vapi.ai manages real-time voice calls and speech streaming. Twilio sends SMS payment links. SQLite stores customer data and call outcomes. A React + Vite frontend dashboard allows users to add customers, trigger calls, and upload audio recordings for testing. Challenges we ran into Managing low-latency real-time voice conversations Handling unpredictable user responses during calls Coordinating multiple APIs (Vapi, Groq, Twilio) through webhooks Testing voice pipelines locally with tools like ngrok Accomplishments that we're proud of Built a fully working AI voice agent capable of real-time calls Designed a modular multi-agent architecture for dialogue, sentiment, and actions Integrated voice AI, LLM reasoning, and SMS automation into a single system What we learned We learned how complex real-time voice AI systems are compared to chatbots, the importance of prompt design for intent detection, and how modular agent architectures make AI systems easier to extend. What's next for Loan Collection Agentic VoiceBot Next, we plan to add payment gateway integration , multilingual support , improved conversational intelligence, and an analytics dashboard for lenders to track recovery performance. <div