---
slug: "climabyte"
url: "https://devpost.com/software/climabyte"
title: "ClimaByte"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 642
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ClimaByte

> ClimaByte is your pocket AI coach that watches what you buy, eat, and travel, then gives you one tiny habit change per day that actually moves the needle on your carbon footprint.

[Devpost](https://devpost.com/software/climabyte) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[climate_energy]] [[disaster_emergency]] [[education]] [[retail_commerce]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]

**stack** anthropic-claude-api, api, artificial-intelligence, carbon-footprint, claude-sonnet-4.6, climatiq-api, computer-vision, data, large-language-models, pillow, plotly, python, streamlit, sustainability

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for climabyte

## Body

Inspiration As a student in Quebec I see climate change happening right in front of me, winters that don’t feel as cold anymore, wildfire smoke in the summer, and all the news about Canada’s emissions. I really wanted to do something, but every carbon app I tried just made me feel guilty and gave me the same boring advice like “eat less meat.” I thought, what if an AI could actually look at my real receipts and shopping and give me one tiny, doable change that actually makes a difference? That’s how ClimaByte was born, to turn guilt into fun, real action I can track. What it does ClimaByte is your personal AI climate coach that lives in your pocket. You snap a photo of any receipt or just type what you bought, Grok Vision reads it instantly, it calculates the real carbon impact using official data, and then your AI coach gives you one encouraging daily challenge plus a prediction of how much you’ll save this month. There’s a clean dashboard with your streaks, savings charts, and even shareable impact cards. The goal is simple: help normal people save 150–250 kg of CO₂ every month without feeling overwhelmed. How we built it I built the whole thing from zero in just six days using completely free tools. The app is written in Python and Streamlit because it let me create a clean, professional interface super fast that works on phones too. The heart of ClimaByte is Anthropic’s Claude API, I used Claude Sonnet 4.6 for computer vision to read receipt photos and also to power the friendly AI coach that writes natural, encouraging messages. For accurate carbon numbers I connected the Climatiq API. The charts and impact visuals come from Plotly, I used Pillow to handle the uploaded images, and everything is deployed instantly on Streamlit Cloud Challenges we ran into Claude Vision sometimes gave messy results on real receipts so I added a quick manual fallback so the app never breaks during a demo. Streamlit session state resets on refresh so I had to save the cart in a simple way that survives. Getting the coach to sound supportive instead of preachy took a lot of prompt tweaking. And with only seven days total I had to stay laser-focused on the core flow instead of adding extra stuff like blockchain. Accomplishments that we're proud of This was my first time using Claude Vision in a real project and it actually worked great. I managed to combine computer vision, a smart LLM coach, and predictive impact charts into one smooth experience in under a week. The live demo feels magical, judges can upload their own receipt and see real numbers in seconds. And I turned a heavy topic like climate into something that actually feels fun and addictive. What we learned Claude API is surprisingly fast and really good at giving clean structured output, even for vision stuff. Real carbon data from Climatiq is way more trustworthy than making up numbers. People actually respond ten times better when you give them one small action instead of big lifestyle changes. Streamlit plus cloud deployment is honestly a hackathon cheat code, no server headaches at all. And always build a backup plan for AI features because it saved me multiple times. What's next for ClimaByte I want to add simple login so history is saved across sessions, turn it into a real mobile app with camera access, bring in location data for local sustainable swaps, and maybe team up with Quebec universities for campus leaderboards and actual carbon offset donations. Eventually I’d love to open-source it so other students can improve the emission factors for Canadian products. ClimaByte started as a hackathon weekend project, but I really believe it can help thousands of people turn their daily habits into real climate wins. <div