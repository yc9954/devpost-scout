---
slug: "sherlostholmes"
url: "https://devpost.com/software/sherlostholmes"
title: "SherLostHolmes"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 534
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# SherLostHolmes

> A gamified lost-and-found system for Concordia Uni where AI detectives match your lost items, interrogate you to prove ownership, and unlock smart lockers for secure pickup. Never lose hope again! 🔍

[Devpost](https://devpost.com/software/sherlostholmes) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[finance_payments]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** cloudinary, langchain, mongodb, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned

## Body

Home Page for authentication New Registeration page Sign in page Home Page after signing in Filing a lost item Evidence Page where you try to find your lost item by describing it and seeing if there is a match in the database If an item has not been collected for over 6 months, you can try your luck to win one by pulling the slot machine! The dashboard after logging in as an admin. SherLostHolmes — The Detective for Your Lost Items Inspiration We've all been there. Our friend, let's call them "The Forgetful One," had a legendary talent for losing things — keys in the library, a phone in the Hall Building, a jacket somewhere between lectures. Every time, the process was the same: awkward visits to lost-and-found offices, vague descriptions, and the dreaded "we'll call you if something turns up." We thought: what if reclaiming your lost items felt less like bureaucracy and more like solving a mystery? That's when SherLostHolmes was born — a gamified, AI-powered lost-and-found system that turns the frustrating experience of losing something into an engaging detective adventure. What It Does SherLostHolmes reimagines lost-and-found with: AI Detective Matching : Using LangChain and vector embeddings, our system semantically matches your lost item description against found items — even if you describe your "blue water bottle" and someone submitted a "navy hydration container" Blind Lineup : Matched items appear as anonymous "suspects" with blurred images and mysterious personas, preventing false claims Interrogation Room : An AI persona "guards" each item, asking ownership-verification questions. Only true owners know the secret details! Fraud Detection : A random decoy item is hidden in every lineup — selecting it instantly flags fraudulent claims Smart Lockers : ESP32-powered lockers with servo locks allow 24/7 secure pickup with one-time passwords Lucky Find : A slot machine mini-game where you can win unclaimed items that have been sitting for 6+ months How We Built It Backend: FastAPI (Python) for high-performance async APIs MongoDB Atlas for flexible document storage LangChain + OpenRouter for AI orchestration Custom vector embeddings for semantic search Cloudinary for image processing (including automatic blurring!) Frontend: Next.js 14 with TypeScript Tailwind CSS for that vintage detective aesthetic Clerk for authentication Framer Motion for smooth animations Hardware: XIAO ESP32-S3 microcontroller Servo motor for physical lock mechanism CardKB I2C keyboard for code entry RESTful API integration for real-time locker state Challenges We Faced Anti-Hallucination in Interrogation : Getting the AI to ask verification questions without accidentally revealing the answers was tricky. We implemented strict prompt engineering with forbidden phrases and validation layers. Fraud Detection Balance : Adding decoy items to the lineup required careful tuning — too obvious and it's useless, too similar and real owners get confused. We settled on cross-category decoys. Real-Time Sync : Keeping locker state synchronized between the ESP32 hardware and our backend required careful polling and password refresh mechanisms. What We Learned LangChain Agents are powerful but need guardrails — structured workflows beat free-form agent behavior for reliability Gamification transforms UX — adding detective theming made users want to verify their identity Hardware + Software integration is incredibly rewarding when it clicks Built with energy drinks and determination at ConuHacks X <div