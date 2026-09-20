---
slug: "r3kon-gpt"
url: "https://devpost.com/software/r3kon-gpt"
title: "R3KON GPT"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 425
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/security_privacy"
---

# R3KON GPT

> An offline first Cybersecurity AI assistant

[Devpost](https://devpost.com/software/r3kon-gpt) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**domain** [[education]] [[security_privacy]]

**stack** artificial-intelligence, machine-learning, python, qwen, tkinter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for r3kon gpt

## Body

Inspiration In many parts of Africa, internet access is expensive, unstable, or completely unavailable , but cybersecurity risks are still growing. I wanted to build an AI tool that doesn’t depend on constant connectivity, doesn’t expose user data to the cloud, and can provide real, practical guidance offline. That was the spark behind R3KON GPT: an AI designed for areas where cybersecurity support is needed most, but connectivity is weakest. What it does R3KON GPT is a cybersecurity-focused offline AI assistant designed for low-connectivity regions. It can: Give cybersecurity tips and safe-practice guidance Help detect suspicious behavior and give threat-awareness advice Function fully without Wi-Fi or stable internet Run as a standalone Windows .exe so anyone can use it instantly Offer general AI responses while prioritizing digital safety It’s built for users who need protection, not data drain. How I built it Python for core logic An offline-capable model packaged directly into the app Multiple cybersecurity-focused prompt layers and logic modules A Windows build system that bundles everything into one .exe Local processing so users don’t need cloud access or API keys The large file size comes from embedding all required AI and security components directly inside the executable — making it fully functional offline. Challenges I ran into Managing the huge file size caused by offline AI models Packaging everything into a single .exe without dependency errors Ensuring the app runs on multiple Windows setups without missing DLLs Designing the AI to be helpful, safe, and security-aware offline Sharing the release safely through Google Drive without exposing personal files Accomplishments that I'm proud of Creating an AI tool that works fully offline, something rare for cybersecurity assistants Building and shipping a functional 1.3GB AI executable at 19 Designing a system that can help users in areas with no Wi-Fi Adding another major product under Aethar Tech Proving that African-first AI tools can be powerful and independent What I learned Offline AI is powerful, but packaging it is challenging Cybersecurity tools need careful design and clear, safe guidance Building for low-connectivity environments requires a different mindset Managing large builds and dependencies is its own skill Releasing software safely matters as much as building it What's next for R3KON GPT A lighter version with modular downloads Stronger offline security features (local threat scanning, phishing detection) A cleaner UI and more stable packaging Mobile and web versions Integration with Nyx Browser for secure browsing + AI support Partnerships and pilots in schools, cyber clubs, and rural areas Turning R3KON GPT into a complete offline cybersecurity toolkit <div