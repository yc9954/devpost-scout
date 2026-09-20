---
slug: "coco-mail-agent"
url: "https://devpost.com/software/coco-mail-agent"
title: "CoCo - Mail agent"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 727
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/web_dom"
---

# CoCo - Mail agent

> Transform Email, Amplify Productivity

[Devpost](https://devpost.com/software/coco-mail-agent) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[web_dom]]

**stack** python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coco - mail agent

## Body

This is the dashboard of coco - Mail Agent. There is a side panel for three easy setup. After setup your CoCo agent is ready to use . This It is the result of the read mail which gave by this agent this perfectly classified spam or safe mail. Inspiration Every day, millions of people struggle with email overload. The average person receives 121 emails per day, yet spends significant time: Sorting through spam and irrelevant emails Writing routine, repetitive email responses Managing and organizing thousands of emails Composing professional emails from scratch I realized that email management could be revolutionized with AI . Instead of spending hours on routine email tasks, users should focus on what matters. This inspired us to create CoCo - an intelligent assistant that handles the tedious parts of email management. What it does Core Features 1. Smart Email Reading & Analysis Read emails from Gmail inbox (last 1-10 emails) Spam Detection: AI-powered spam classification with Groq LLM Email preview with sender, subject, and content Statistics dashboard (Total, Spam, Safe emails) How it works: Fetches emails via IMAP Extracts email body (handles HTML/plain text) Sends to Groq AI for spam analysis Returns [SPAM] or [SAFE] with reasoning 2. AI Email Composition Generate professional emails on ANY topic Create emails for: meetings, requests, thank yous, proposals, etc. One-click email generation. How it works: User describes email purpose Groq AI generates professional content User can edit before sending 3. Smart Email Sending Send emails with automatic address extraction Direct Gmail SMTP integration Success/error feedback How it works: Parses recipient email (handles all formats) Sends via Gmail SMTP (secure) How we built it Building CoCo required a carefully selected technology stack that balanced ease of development, performance, and accessibility. At the core, we used Python 3.x as our primary programming language due to its extensive libraries and rapid development capabilities. For email access, we leveraged imaplib (the built-in IMAP protocol library) to read emails from Gmail inboxes and smtplib for secure email sending via Gmail's SMTP servers. These low-level libraries gave us complete control over email operations while ensuring security through SSL/TLS encryption. The email parsing and manipulation was handled by Python's native email module, which allowed us to construct and decode complex email messages with proper MIME formatting. The most critical component of CoCo is its AI brain , powered by Groq's Mixtral-8x7b language model via the Groq API. We chose Groq over other AI providers (like OpenAI) for three compelling reasons: first, it offers unlimited free API calls for reasonable usage, eliminating cost barriers; second, its Mixtral model delivers lightning-fast inference speeds (sub-second responses) compared to traditional LLMs; and third, it provides a 32K context window perfect for analyzing long emails. The Groq API integration allows us to send email content to the AI for spam detection, reply generation, and email composition in real-time. Challenges we ran into 1. Email Address Extraction Bug (MAJOR) Challenge: Emails from Gmail IMAP come formatted as: "Name email@domain.com " Sending emails directly to this format caused delivery failures Error: Address not found - message wasn't delivered 2. HTML Email Content Parsing 📧 Challenge: Emails with HTML content returned tags: Hello Displaying raw HTML was unprofessional LLM received broken content 3. Streamlit State Management Streamlit reruns entire script on every interaction Session state wasn't persistent Lost data between interactions Accomplishments that we're proud of 1. 100% Email Delivery Success We solved the email address extraction problem completely. All replies now deliver successfully to actual senders, not test addresses. 2. Lightning-Fast AI Processing Using Groq API, we achieved: Spam detection in <1 second per email Email composition in 2-3 seconds 10x faster than traditional LLMs 5. Fully Functional AI Agent Built a complete email agent with: AI-powered analysis Intelligent composition Context-aware replies Batch processing What we learned 1. Email Protocol Mastery Deep understanding of IMAP protocol SMTP email sending mechanics Email encoding and parsing challenges Gmail security requirements 2. AI/LLM Integration How to effectively prompt LLMs API optimization and rate limiting Model selection for different tasks Cost vs. performance tradeoffs ** 3. Project Management** Phased development approach Feature prioritization Testing and validation Documentation importance What's next for CoCo - Mail agent 1. Multi-Language Support Support for 20+ languages Automatic language detection Reply in different language 2. Mobile App Native iOS app Native Android app Offline functionality Push notifications <div