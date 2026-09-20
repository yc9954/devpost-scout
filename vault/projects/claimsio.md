---
slug: "claimsio"
url: "https://devpost.com/software/claimsio"
title: "Claimsio"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 340
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/structured_db"
---

# Claimsio

> Transforms debt collection into a compliant, automated process that works (and is 97% cheaper and 40% more effective, thanks agents 🙌) Stack: Elevenlabs, Loveable, Vercel, n8n, Twilio, Stripe, Go, TS

[Devpost](https://devpost.com/software/claimsio) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]]
**substrate** [[structured_db]]

**stack** elevenlabs, go, javascript, lovable, n8n, stripe, supabase, ts, twilio

## How they structured the write-up

- team introduction
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for claimsio

## Body

Check performance of your AI collection Check and pay for your debt Add a new debtor to collect Talk with an Agent using text messages or audio Team introduction We are friends who love to build together and are planning to continue developing this project after the Hackathon. We work at a neo bank, with one of us serving as the technical Head of Product in Portugal and the other handling a combination of Backend, DevOps, and compliance responsibilities in Poland. Inspiration Working daily on building a neo bank in Portugal, we experienced firsthand how manual and difficult it is to scale the debt collection process. This challenge ignited an idea that we discussed with several customers, ultimately deciding to develop it during the hackathon. What it does We automate the debt collection process through calls and text messages, with plans to expand to additional channels and automated court filing in the future. During the hackathon, we developed a simple journey that tracks debt from initial recording through the resolution/negotiation process to final payment via Stripe. How we built it Debtor panel: Lovable (admin.claimsio.com) Debt collection panel: Lovable (pay.claimsio.com) Database: Supabase Workflows/back-end: n8n and Go + JavaScript scripts to handle incoming calls Hosting: Vercel (admin.claimsio.com, pay.claimsio.com, claimsio.com) Communications: Twilio Payments: Stripe Voice synthesis: ElevenLabs LLMs: Claude 3.5 Sonnet and OpenAI GPT-4 Challenges we ran into While we found a potential solution for outbound calls with ElevenLabs, time constraints prevented us from implementing it fully. Accomplishments that we're proud of We successfully created a fully automated debt resolution process MVP! This will provide an excellent foundation for future customer presentations. What we learned We gained valuable experience with multi-agent systems, Langchain integration within n8n, and the capabilities of ElevenLabs API for outbound communications. What's next for Claimsio The project was built to be scaled after the hackathon. Our focus now shifts from building to customer acquisition. We plan to explore opportunities with various market players, including debt collection agencies, utility companies, and B2B enterprises. Demo recorded in the loom: https://www.loom.com/share/31897c281b284b47a56b020e8693c3ed?sid=a0f13492-bc54-4edd-9ff6-64ff23d03f19 <div