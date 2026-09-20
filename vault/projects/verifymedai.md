---
slug: "verifymedai"
url: "https://devpost.com/software/verifymedai"
title: "VerifyMedAI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 650
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/structured_db"
---

# VerifyMedAI

> Killing Ghost Networks with AI.

[Devpost](https://devpost.com/software/verifymedai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[legal_professional]] [[patient_family]]
**substrate** [[structured_db]]

**stack** code, difflib, forms, git, google, pandas, python, streamlit, twilio, vs

## How they structured the write-up

- verifymedai: killing ghost networks with ai 🛡️
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for verifymedai

## Body

VerifyMedAI: Killing Ghost Networks with AI 🛡️ Inspiration We’ve all been there urgently needing a doctor, finding one in our insurance directory, and calling... only to hear "This number is out of service" or "Dr. Smith retired three years ago." These are "Ghost Networks." Studies show that up to 52% of provider directory data is inaccurate . This isn't just annoying; it delays care for patients and costs insurers millions in fines. We realized that the current solution manual call centers calling doctors one by one is too slow and expensive. We wanted to build a Self-Healing Database that fixes itself autonomously. What it does VerifyMedAI is an autonomous "Human-in-the-Loop" verification agent that cleans healthcare data in real-time. Ingests Data: It scans payer databases and cross-references them against a trusted "Source of Truth" (NPI Registry). Detects Anomalies: Using fuzzy logic, it identifies discrepancies in addresses, phone numbers, or names (e.g., "123 Main St" vs "123 Main Street"). Initiates Protocols: If a high-confidence mismatch is found, it automatically triggers a secure SMS verification loop to the provider. Heals the Data: The provider receives a text with a one-click verification link. Their response validates the data instantly, turning "Red" records into "Green" verified records on the dashboard. How we built it We built the entire architecture using a modern Python stack: Python (Pandas & Difflib): The core logic engine that handles data ingestion and performs "Fuzzy Matching" to calculate confidence scores for every record. Twilio API: The communication gateway. We used Twilio's programmable SMS to send real-time, secure verification links to providers' personal devices. Streamlit: We built a professional "Command Center" dashboard that visualizes the AI's decision-making process, showing live logs, confidence scores, and verification statuses in a dark-mode UI. Google Forms (Mock Database): For the demo, we integrated a pre-filled form to simulate the provider portal, allowing for a seamless user experience. Challenges we ran into The "Ghost" UI: We struggled with Streamlit's theming engine—at one point, our dashboard text went invisible (white-on-white) due to system dark mode conflicts. We had to write custom CSS injection and force a config-level theme override to create a professional "Bloomberg Terminal" look. API Security: We accidentally exposed our API keys during the initial Git push! We learned the hard way about git filter-branch and .gitignore best practices to scrub our history and secure our credentials. Latency Simulation: Making the demo feel "real" was tricky. Real-time data processing is too fast for a stage demo, so we had to engineer realistic delay loops to give the judges time to see the "Sending SMS..." status before the phone actually buzzed. Accomplishments that we're proud of The "Pocket Buzz" Moment: Successfully bridging the gap between code and the physical world. Seeing the dashboard turn red and immediately feeling the phone vibrate in our pocket was a huge win. Zero-Friction UX: We proved that you don't need a complex app to verify data. A simple SMS link has the highest conversion rate for busy doctors. The UI Polish: We went from a basic script to a fully interactive, professional-grade dashboard that looks like enterprise software. What we learned Human-in-the-Loop is Key: AI is great at detecting errors, but you still need a human (the doctor) for the final source of truth. The best agents assist humans, they don't replace them. Fuzzy Logic Nuance: "Exact Match" doesn't work in the real world. Handling typos like "Suite 100" vs "Ste 100" required fine-tuning our similarity thresholds (we settled on 80% confidence for alerts). What's next for VerifyMedAI Voice AI Agents: Integrating Twilio Voice to actually call the doctor's office and speak with the receptionist using conversational AI if they don't reply to the text. WhatsApp Integration: Expanding channels to WhatsApp for international markets. RPA Write-Back: authenticating the Google Form webhook to automatically write the corrected address back into the SQL database, closing the loop entirely without human admin intervention. <div