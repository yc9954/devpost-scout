---
slug: "procuro"
url: "https://devpost.com/software/procuro"
title: "Procuro"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 408
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Procuro

> Procuro is a procurement automation system that streamlines vendor negotiations, price comparisons, and shipment tracking in real time with automated calling, sourcing, and integrations.

[Devpost](https://devpost.com/software/procuro) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[retail_commerce]] [[supply_logistics]]
**substrate** [[document_pdf]] [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** databases, demo, elevenlabs, elevenlabs-(for-voice-agents), excel-(for-automation-of-generating-sheets/csv), lovable, ngrok, node.js, perplexity, perplexity-api-(for-search-mechanic-+-report-generation), sms), supabase, twilio, twilio-(for-phone-calls

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for procuro

## Body

Main Procuro Dashboard New Order Search + Order Agent Page (with contact list), with Procuro negotiating for you New Order Agent generated Purchase Order receipt Shipping Status Agent Page (with overview, contact features, status bar) Routine Ordering Automation Agent page Routine Ordering calendar view Inspiration Our inspiration came from watching our families in manufacturing struggle with legacy systems, juggling endless Excel sheets and paper records. We saw hours lost on manual phone calls just to track shipments and confirm orders. This inefficiency sparked our desire to create an automated solution that parallelizes calling, saves time, and increases revenue. We envisioned a system that lets people focus on what really matters—growing their business, building better products, and creating time to spend with their families. What it does Procuro tackles the inefficiencies in procurement by automating routine tasks like restocking, price negotiations to best the best prices for new orders, automatically generating purchase order documents, and shipment tracking. It streamlines vendor interactions using automated calling powered by Twilio and ElevenLabs, coupled with intelligent price comparisons via Perplexity AI. Real-time updates and dynamic dashboards keep you informed without the hassle of manual follow-ups. How we built it We built Procuro by integrating our existing vendor database with modern communication APIs like Twilio and ElevenLabs. For parts sourcing and price comparison, we harnessed Perplexity AI. Other tools we used: Lovable, Github, NGrok, NextJS. Challenges we ran into Initially, we embarked on an ASL-to-speech translator project and encountered significant hurdles in training a deep learning model from scratch. By 2am, we recognized the need to pivot, channeling our efforts into building the procurement agent instead. We faced tight deadlines and technical roadblocks, but our team powered through by working around the clock for 8 hours straight. Accomplishments that we're proud of We embraced our initial setbacks and pivoted quickly, demonstrating resilience and creative problem-solving. What we learned We learned firsthand how to build AI voice agents and connect multiple modalities—from ASL video integration to natural language processing. Working as a team, we divided tasks efficiently, gaining invaluable insights into rapid development and collaboration. Exploring cutting-edge tools like Fal, Lovable, and ElevenLabs. What's next for Procuro Next, we're focusing on building a robust MVP for real-world customers and collecting their feedback for iterative improvements. We're excited to integrate high-quality shipment datasets and expand our ERP system integrations for seamless operations. Our roadmap includes refining our vendor search algorithms and enhancing our negotiation features. <div