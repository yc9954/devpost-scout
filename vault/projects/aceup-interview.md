---
slug: "aceup-interview"
url: "https://devpost.com/software/aceup-interview"
title: "AceUp-interview"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 489
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# AceUp-interview

> AI-powered system interview platform with automated grading, real-time proctoring, and interactive AI interviews that help companies evaluate engineers quickly and consistently.

[Devpost](https://devpost.com/software/aceup-interview) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[transcript_audio]]

**stack** elvenlab, github, javascript, json, next, python, react, supabase

## How they structured the write-up

- inspiration
- what aceup does
- how we built it
- challenges
- accomplishments
- what we learned
- what’s next for aceup

## Body

AceUp — Project Description Inspiration AceUp was created from a simple observation: companies need engineers who can design scalable systems, yet evaluating these skills is slow, inconsistent, and expensive. Traditional system design interviews require senior engineers, long review cycles, and subjective scoring. We wanted to change that. As students passionate about software architecture, we set out to build a platform that makes system design assessment consistent, scalable, and accessible for any engineering team. What AceUp Does AceUp provides a fully automated system design interview experience—from real-time interaction to final evaluation. At its core is an AI interview agent that behaves like an experienced engineer. It receives continuous updates from the candidate’s design canvas and asks relevant follow-up questions about architecture choices, trade-offs, and reasoning. A lightweight proctoring layer monitors the candidate’s webcam to ensure integrity during the session. After the interview, the candidate’s diagram and full conversation are analyzed by an LLM across five key dimensions: Scalability Reliability Availability Communication clarity Trade-off reasoning Every candidate receives a fair, standardized assessment—and companies get structured, actionable scoring. How We Built It AceUp is powered by Next.js, React, Typescript, and Supabase across the frontend and backend. The design canvas outputs the candidate’s system diagram as structured JSON. A streaming pipeline continuously sends diagram updates to the AI agent, enabling real-time contextual interviewing. Proctoring captures periodic webcam frames and performs computer vision checks for anomalies such as multiple faces, device usage, or unusual distractions. After the interview, the transcript, diagram, and metadata are processed by an LLM guided by a custom evaluation rubric. The grading output is transformed into clear insights so teams can understand the candidate’s strengths and weaknesses. Challenges Building the communication layer that connects the live canvas stream to the AI agent was one of the toughest parts. Real-time synchronization and context injection required fast and reliable data handling. Optimizing the proctoring system was another challenge—processing webcam frames frequently without affecting the user experience demanded careful performance tuning. Accomplishments Implementing real-time context awareness for the AI agent—the moment it reacts to diagram changes is incredibly powerful. Developing a stable and accurate proctoring module that detects irregularities while minimizing false positives. Watching the full pipeline work end-to-end, from interview start to automated grading, proved that AceUp can truly replace manual system design interviews. What We Learned We gained deep knowledge about building multi-modal AI systems that combine computer vision, real-time streaming, conversational AI, and LLM evaluation. We also learned how small refinements in evaluation rubrics can dramatically improve grading consistency. Technically, we strengthened our expertise in streaming architecture, prompt engineering, and orchestrating multiple AI components simultaneously. What’s Next for AceUp We plan to expand AceUp into a complete automated interview platform. Upcoming features include: AI-led coding interviews AI-led behavioral interviews Practice mode so candidates can improve through feedback Advanced dashboards for teams to track performance and compare candidates AceUp aims to become the backbone of reliable, scalable, AI-powered technical interviewing. <div