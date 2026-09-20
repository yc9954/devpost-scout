---
slug: "crm-pcg2xb"
url: "https://devpost.com/software/crm-pcg2xb"
title: "CRM"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 451
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# CRM

> AI That Handles Your Support End-to-End

[Devpost](https://devpost.com/software/crm-pcg2xb) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]] [[web_dom]]

**stack** 2.5, gemini, gmail-imap, gmail-smtp, imaplib, meta, openpyxl, outlook-imap, python, requests, smtplib, sqlite, whatsapp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crm

## Body

Snippit Inspiration Traditional CRM systems are heavily dependent on manual effort — someone has to read emails, create tickets, assign them, follow up, and track deadlines. This leads to delays, human errors, and inefficiencies, especially in high-volume B2B environments. We were inspired by a simple question: “What if a CRM could think and act on its own?” With the rise of AI agents and large language models, we saw an opportunity to build a system that doesn't just assist humans — but operates autonomously, handling the entire incident lifecycle from start to finish. What it does The Agentic AI CRM is an autonomous system that: Reads incoming emails from Gmail and Outlook Uses AI to classify issues (IT, Billing, HR, etc.) and set priority Automatically creates and assigns tickets to the right team Tracks SLA deadlines and escalates delays Sends real-time notifications via WhatsApp and Email Maintains structured records in a database and Excel dashboard How we built it Core Stack: Python — Core logic and orchestration IMAP (imaplib) — Email ingestion Google Gemini 2.5 Flash — AI classification and structured output SQLite — Ticket storage (ACID-compliant) openpyxl — Excel reporting SMTP — Email notifications Meta WhatsApp API — Real-time alerts cPanel Cron Jobs — Scheduled execution every 5 minutes Architecture Flow: Fetch unread emails via IMAP Send email content to AI for structured JSON extraction Parse response and validate data Create ticket in database Assign agent based on category Send notifications (Email + WhatsApp) Monitor SLA and trigger escalations Challenges we ran into AI Output Reliability: Ensuring the AI always returns valid JSON required building a fallback parser and rule-based classifier. Authentication Issues: Setting up secure IMAP access with Gmail/Outlook App Passwords was tricky. Email Parsing Complexity: Handling different email formats (HTML, MIME, attachments) required robust parsing logic. WhatsApp API Limitations: Meta API setup and token expiration added friction during integration. Shared Hosting Constraints: No persistent backend processes meant we had to design a cron-based execution model. Accomplishments that we're proud of Built a fully autonomous CRM workflow — no manual ticket creation Achieved end-to-end automation from email to resolution tracking Designed a zero-cost architecture using open-source tools Successfully integrated AI + automation + real-time communication Created a system that is scalable, modular, and production-ready What we learned How to integrate LLMs for structured decision-making Designing resilient systems with fallback mechanisms Building automation within real-world constraints (shared hosting) Importance of idempotency and error handling in cron jobs Bridging the gap between AI outputs and traditional systems (databases, workflows) What's next for CRM Client Portal Dashboard Real-time ticket tracking for customers AI-Powered Knowledge Base Suggest solutions based on past incidents Local LLM Deployment For privacy-focused organizations (no external API calls) <div