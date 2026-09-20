---
slug: "croppers"
url: "https://devpost.com/software/croppers"
title: "Cropt"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 666
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# Cropt

> Cropt: AI-powered crop disease detector that works completely offline. Snap a photo or describe symptoms for instant plant health insights for farmers.

[Devpost](https://devpost.com/software/croppers) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[agriculture_food]] [[climate_energy]] [[education]] [[health_clinical]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** 11elevenlabs, auth0, expo.io, gemma, mlange, react, react-native, supabase, tailwind, twilio, typescript, vite, whatsapp, zertic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cropt

## Body

Cropt: Field intelligence. Community protection. Inspiration The inspiration for Cropt stems from a devastating reality in Southeast Asia: a crop disease that decimated 2.5 million acres, leading to an 80% yield loss. Information travels slower than the disease itself, leaving farmers like Amara—one of 500 million smallholder farmers globally—utterly helpless. These farmers often face the "triple barrier": low connectivity, low literacy, and limited education. When a crop shows signs of distress, they are forced to wait for hotlines or post blurry photos to crowded WhatsApp groups, often receiving advice too late to save their livelihood. We realized that for the next Amara, the solution couldn’t depend on the cloud or a stable signal; it had to be as immediate as the threat itself. What it does Cropt is an offline, audio-first crop disease prevention application designed specifically for low-connectivity environments. Using an "audio-as-interface" philosophy, farmers simply point their camera at a suspicious plant. Our on-device AI instantly analyzes the image to provide a diagnosis and specific treatment steps via voice. To foster community resilience, a single tap allows farmers to broadcast alerts to nearby neighbors or send automated WhatsApp messages to community groups. When internet access is available, the app utilizes a sophisticated conversational agent capable of switching between 70+ languages, while every scan contributes to a real-time global dashboard that provides agricultural organizations with unprecedented grassroots outbreak data. How we built it The core of Cropt is built on breakthrough on-device AI integration. We leveraged Zetic’s NPU technology to run heavy analysis models locally on low-cost mobile phones without requiring internet or cloud processing. To make the app truly accessible, we designed a minimalist, audio-centric UI that bypasses literacy barriers. For the conversational layer, we integrated ElevenLabs to provide high quality, localized speech synthesis in over 70 languages. The backend infrastructure is designed to queue data locally and sync with a central dashboard only when connectivity is restored, ensuring no data point is lost. Challenges we ran into Technically, we faced the significant hurdle of integrating compressed AI models that were originally incompatible with mobile environments. Optimizing these models to maintain high accuracy while running on limited hardware required rigorous engineering. Additionally, ensuring accurate speech recognition and audio playback in "noisy" field environments, like wind, machinery, and nature, presented a unique design challenge. We also had to build a robust offline-first synchronization system that could handle intermittent signals without draining the user’s battery or storage. Accomplishments that we're proud of We are incredibly proud of creating a tool that serves as essential climate infrastructure. We successfully moved advanced agricultural science out of the lab and directly into the hands of those who need it most. By enabling instant, offline diagnosis, we have created a system that can help prevent a portion of the $220 billion in annual crop losses. Bridging the gap between cutting-edge NPU technology and the daily needs of a smallholder farmer is a feat of both engineering and empathy that we stand by. What we learned This project taught us that high-tech doesn’t have to mean high-barrier. We learned that for global impact, the user interface must adapt to the user’s environment, not the other way around. Audio-first design isn’t just a feature; for millions of people, it is the only viable way to interact with technology. We also gained deep insights into the power of localized data; seeing how a single offline scan can eventually inform a nationwide agricultural response changed our perspective on data crowdsourcing. What's next for Cropt Our goal is to scale Cropt to support millions of farmers who currently lack these resources. We are looking to expand our model library to include more regional-specific crops and pests. We also plan to deepen our partnerships with international agricultural organizations to turn our real-time dashboard into a standard early-warning system for global food security. Cropt won’t stop until every farmer has the power to protect their harvest and their community, regardless of their signal strength or literacy level. <div