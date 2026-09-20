---
slug: "navi-7sp5mz"
url: "https://devpost.com/software/navi-7sp5mz"
title: "Navi"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 489
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Navi

> Navigate smarter: a co-pilot for your browser Navi streamlines your browsing experience with immediate assistance, voice navigation, and website recommendations based on predicted user intent.

[Devpost](https://devpost.com/software/navi-7sp5mz) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]]
**domain** [[accessibility]]
**substrate** [[video_visual]] [[web_dom]]

**stack** context, elevenlabs, gemini, groq, javascript, mistral, next.js, openai, perplexity, scrapybara, typescript, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for navi

## Body

Inspiration Given the substantial lack of accessibility resources and compliance in modern website UI—over 96% of websites fail to meet accessibility requirements—we wanted to develop an AI-driven copilot agent, Navi, for human browsing, in addition to creating an easier web infrastructure for AI models to interact with. 🌐🤖 What it does In short, Navi makes web browsing easier for human users, with accessible voice navigation 🎤, intuitive browsing with user intent prediction 🔮, instant feedback to questions 📝, and personalized further reading suggestions 📚. In terms of serving AI models, Navi extracts web pages more efficiently compared to traditional VLMs. ⚡ How we built it To integrate visual context, we captured screenshots of the user's navigation, which were then processed by visual language models (VLMs) to inform Navi's AI. This enabled Navi to understand and interpret website layouts in real time 🖼️. Simultaneously, we harnessed Context, a robust context fetching engine, to analyze user interactions, predicting browsing intent and tailoring recommendations. In the background, Scrapybara autonomously suggests related websites 🌐, while Groq converts audio commands into prompts for OpenAI's 4-o LLM, ensuring rapid and accurate responses ⚙️. Additionally, we leveraged Mistral for fast, simplified website renderings that highlight key information, making navigation even easier for the user 🏃‍♂️. Challenges we ran into Balancing rapid AI responses with efficient web page extraction was just one layer of our challenge 🏔️. A deeper complexity arose from integrating multiple AI components into a unified, accessible system. Each component—whether it was the Context engine, VLMs, or voice processing with Groq—had its own processing speeds, data formats, and dependencies. Merging these disparate systems required careful orchestration to ensure they communicated seamlessly in real time ⏱️. We designed robust interfaces and error-handling protocols to bridge differences in performance and data structure ⚖️. This meant synchronizing outputs from slow VLMs with faster processing modules, ensuring that delays in one area wouldn’t disrupt the overall user experience. Accomplishments that we're proud of We're proud to have built Navi as a truly integrated, AI-driven copilot that enhances web accessibility and usability 🌟. Navi not only improves browsing efficiency through context-aware predictions and voice navigation but also serves as a high-performance data extractor for AI models. This project sets a new benchmark for creating accessible digital experiences and bridging the gap between human and AI interaction 🌉. What we learned Throughout this project, we gained invaluable insights into prompt orchestration, context fetching, and the nuances of designing for accessibility. We learned how critical it is to balance technical sophistication with user-centric design, ensuring that advanced features translate into real-world usability for diverse audiences 🎓💡. What's next for Navi Looking ahead, we plan to expand Navi's compatibility with more websites and enhance its voice and intent recognition capabilities 🔧. Our next steps include optimizing the system for even faster and more accurate responses ⏩, refining personalized recommendations, and exploring additional accessibility features to further empower users with disabilities ♿. <div