---
slug: "gridsense-ri49gk"
url: "https://devpost.com/software/gridsense-ri49gk"
title: "Gridsense-A Community Powered Neighborhood Outage Prediction"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 1437
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Gridsense-A Community Powered Neighborhood Outage Prediction

> 30–60 minutes before the power goes out, your neighborhood already knows. GridSense listens.

[Devpost](https://devpost.com/software/gridsense-ri49gk) · hackathon [[Build with MeDo Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[sensor_fusion]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** css3-animations, deep-translator, groq-api-(llama-3.3-70b), html5-canvas-(aurora-effect), javascript-(vanilla), langdetect, leaflet.js, localstorage, medo-ai-app-builder, open-meteo-weather-api, openrouter, web-speech-api-(voice-input)

## How they structured the write-up

- the morning this became real
- what it does
- how i built it with medo
- what i learned
- challenges
- cities in the neighborhood database as per this version
- how i structured conversations with medo to build gridsense
- the most impressive feature medo helped me create
- the bigger picture

## Body

The Morning This Became Real It was 4am. My database exam was at 9. I woke up to no power ,my laptop dead, phone at 8%, room completely dark. The transformer outside had been humming differently for two days. A neighbor mentioned a crew van at the junction. Lights had flickered twice that week. Every signal was there. Nobody had built the tool to connect them. * I am a second-year CS student in Mukono, Uganda. My mother owns a stationery and printing business. I have watched her lose entire days of revenue to outages that arrived without a single second of warning. And the irony around this problem is that it affects each and every corner of the economy, down to healthcare(expired reagents due to random outages),education, social ,productivity, every single business that fundamentally relies on electricity to run * Uganda loses 1.15% of annual GDP to unannounced power outages. That is not a statistic. That is 1.5 billion people across Africa, South Asia, Southeast Asia, and the Middle East facing the same problem every single week. This is GridSense. What It Does GridSense is a neighborhood-scale early warning system. A user reports what they notice — a transformer hum, flickering lights, a utility crew van, a photo of sparking equipment, a voice note. GridSense synthesizes those signals with live weather data and the memory of every past report from that neighborhood, and returns a calibrated outage probability, a plain-English explanation of the reasoning, and a personalized five-step action checklist — all within seconds. The goal is not to predict every outage. The goal is to give people 30 to 60 minutes of warning often enough that it changes how communities experience a problem that has been quietly taking from them for years. How I Built It with MeDo GridSense was built entirely using MeDo's AI-powered app builder across 20+ iterative prompts , each one adding a layer of intelligence and polish. The journey went like this: Foundation — I started with a skeleton prompt describing the core concept: neighborhood outage prediction from community signals. MeDo generated the initial structure instantly. The Brain — I wired in a hybrid AI system: a deterministic simulation engine that processes keyword signals and city baselines for instant responses, combined with live Groq Llama 3.3 inference for when real AI reasoning is needed. Both paths return the same structured JSON schema — probability, confidence, explanation, countdown, and a five-step checklist. The Interface — Through successive MeDo prompts, the UI evolved into something cinematic: an aurora cursor effect built with lerp interpolation, a probability ring with four distinct states (SAFE → ELEVATED → WARNING → CRITICAL), a live regional hex grid showing neighborhood risk levels, and a luminous 7-day heatmap with glow animations. Intelligence layers added prompt by prompt: Input validation rejecting gibberish, spam, and past-tense reports Multilingual support via deep-translator preprocessing Voice input via Web Speech API Live Leaflet map with real GPS positioning Outcome confirmation loop for community learning Free-form international location onboarding — any village or megacity on Earth What I Learned Building GridSense on MeDo taught me that the real skill in AI-assisted development is knowing what to ask and in what order . MeDo handles the implementation. The developer's job becomes architecture, judgment, and iteration. I also learned that a well-structured system prompt is worth more than a fine-tuned model when time and compute are limited. The GridSense simulation engine — which runs without any external API — produces calibrated, realistic predictions because the logic was designed carefully, not because it uses expensive infrastructure. Challenges Onboarding navigation bug — Early builds had the three-question onboarding not routing correctly to the main interface after completion. Resolved through a targeted MeDo prompt specifying the exact navigation flow and state management behavior. Groq API reliability — Free tier rate limits meant the live AI toggle needed graceful fallback to the deterministic engine when the API was unavailable. The hybrid architecture made this seamless for the user. Map accuracy — Getting the Leaflet map to correctly show the user's actual GPS position versus a simulated neighborhood required carefully separating the real location dot from the regional risk visualization. Power cuts during development — I am building this in Mukono, Uganda. The irony of building an outage warning system while experiencing outages is not lost on me. Every session was a reminder of exactly why this matters. Cities in the Neighborhood Database as per this Version Mukono/Uganda · Lagos/Nigeria · Karachi/Pakistan · Johannesburg/South Africa Manila/Philippines · Beirut/Lebanon · Chennai/India · San Francisco/USA How I Structured Conversations with MeDo to Build GridSense I did not start with a full specification. I started with a problem. My first conversation with MeDo was simple . I described what power outages feel like in my community and asked whether it was possible to build something that could warn people before they happen. MeDo did not just answer the question. It helped me think through what the product actually needed to be. That conversation shaped the entire architecture before a single line of code was written. From there I worked in layers. I would describe one piece of the system in plain language e.g the probability engine, the neighborhood map, the weather integration and MeDo would build it, explain what it built, and flag what needed to connect next. When something did not work the way I imagined, I described the gap in the next message and MeDo revised. The multi-turn structure meant I was never starting over. Every conversation built on the last one. The most important thing I learned was to be specific about outcomes, not instructions. Instead of telling MeDo how to build something, I told it what I needed the user to experience and let MeDo figure out how to get there. That shift made the conversations faster and the output significantly better. I used MeDo's visual editor to review and adjust layout decisions, and switched to direct conversation when I needed logic changes or new features added. The two modes complemented each other well. By the end, the codebase was far more complete and coherent than anything I could have produced alone in the same timeframe. The Most Impressive Feature MeDo Helped Me Create The most impressive feature is the weather-fused dual-brain probability engine and the reason it impresses me is not the complexity but the fact that it works exactly the way I imagined it, which I did not think was possible when I first described it. I told MeDo I wanted the app to not just react to what was currently happening but to reason about what was about to happen. I wanted live weather conditions and a short-term forecast — rain, wind, cloud cover across the next six hours to feed directly into the outage probability calculation. I wanted the brain to weigh those forward-looking signals alongside community reports and produce a single honest risk score. MeDo built that. It built the MeDo Weather plugin integration that fetches both current conditions and a 6-hour block forecast on every prediction call. It built the weighting logic that treats forecast signals as forward-looking risk factors. It built the fallback architecture so that if the live AI brain fails for any reason, a local simulation engine takes over silently and the user never sees a broken state. What makes it impressive to me is not the individual pieces but it is that the whole thing reasons about the near future, not just the present. A platform that can say "heavy rain is forecast to intensify in your city in the next two hours and your neighbours are already reporting flickering lights" is a fundamentally different tool from one that reacts after the outage starts. MeDo helped me build the version I actually wanted, not a simpler substitute. The Bigger Picture In the grand scheme, GridSense becomes more powerful with every report. One user reporting a flicker gives a probability. Two users reporting the same flicker — two streets apart — raises it. A third user confirming the outage occurred teaches the system what those signals actually mean on that specific block. The community becomes the sensor network. The data commons becomes the competitive moat. And the communities most affected by power instability become the authors of the AI that protects them. This is version one. The roadmap includes SMS access for feature phone users, utility company data partnerships, IoT breaker panel nodes, and eventually a real-world community-sourced power infrastructure dataset for the developing world. Data that does not currently exist. Data that only GridSense can build. Everyone deserves a warning. <div