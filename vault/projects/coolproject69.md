---
slug: "coolproject69"
url: "https://devpost.com/software/coolproject69"
title: "VisionScout"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 929
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/educator_student"
---

# VisionScout

> VisionScout: a bridge between what you see and want. AI glasses auto-generate listings with condition reports, and an AI gives you Spotify-level recommendations for homes and cars that fit your vibe.

[Devpost](https://devpost.com/software/coolproject69) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[housing_homeless]] [[transportation]]
**user** [[educator_student]]

**stack** beautiful-soup, flask, hardware, langgraph, python, react.js, restapis, selenium, tailwindcss, typescript, yolo, zillow

## How they structured the write-up

- 🚀 inspiration
- 💡 what it does
- 🧠 tech stack & architecture
- ⚙️ challenges we ran into
- 🏆 accomplishments we’re proud of
- 📚 what we learned
- 🔮 what’s next for visionscout

## Body

Landing Page Listing Page AI Chatbot Page About Page - Light Mode Smart Glasses VisionScout 👓 "See Smarter. Decide Faster." 🚀 Inspiration Every car or property listing you see online is written by someone trying to describe what they saw — and every buyer is left trying to imagine what’s real. We thought: Why are listings still manually written in 2025? What if your glasses could do the listing for you — detecting condition, estimating confidence, and automatically generating a full summary? And what if you could then talk to an AI assistant that understood your preferences and taste — giving you Spotify-level recommendations for homes or cars that fit your vibe, budget, and lifestyle? That’s how VisionScout was born: a bridge between what your eyes see and what your heart wants — where visual data meets personalized discovery. 💡 What it does VisionScout is a unified AI system that turns short videos from smart glasses into rich, structured listings and also provides you personalized AI recommendations that perfectly matches your preferences. 🏠 Property Mode Detects: Wall damage, appliances, flooring and room dimensions Generates a condition confidence score and automatically builds a structured listing. 🚗 Car Mode Detects: Dents, scratches, tire wear, windshield damage, the make and model Applies lighting and angle normalization to keep results consistent. 🧭 User Experience Once data is in the system: 🔍 Users can search, toggle, and sort between Car and Property listings. 💬 They can describe their dream car or home (“a 2-bedroom apartment with bright lighting in Frisco” / “a red SUV under 30k”) — and VisionScout’s agentic AI matches real listings using a weighted similarity algorithm. 📊 Each result comes with an AI-derived condition score , benchmarked against comparable market data (Zillow + cars.com). The result: a personalized, intelligent experience that automates trust. 🧠 Tech Stack & Architecture Our build combined full-stack web development, AI reasoning, and data automation — all working together seamlessly. Frontend: Built with React.js , TypeScript , and Tailwind CSS , the interface is fully responsive across mobile and desktop. The sleek chat UI and listings grid were designed for clarity, interactivity, and quick data visualization. Backend: We designed and implemented RESTful APIs in Python , using Flask to bridge the AI agent backend with the frontend in real time. The server handles request parsing, AI query dispatching, and structured data delivery. AI & Data Layer: The agent was built using LangGraph , integrating Gemini 2.5 Pro for natural-language reasoning and intent understanding. Real-estate listings were fetched dynamically using the Zillow API , while car data was scraped with Selenium and BeautifulSoup4 from Cars.com. A custom merge-score algorithm ranked results by trust, value, and relevance to ensure the most reliable listings surfaced first. Hardware: We designed a smart glasses using Python and Flask , for defects for cars and walls and vehicle make, integrating Gemini 2.5 pro for automated debugging. A sleek and clean design is incorporated to extract objects effectively. Together, these components formed a cohesive agentic system that connects intelligent reasoning with live, data-driven discovery. ⚙️ Challenges we ran into This project tested everything — from teamwork to hardware to data engineering. First Hackathon for Most of Us: Three of our team members were completely new to hackathons. Navigating the 24-hour sprint, juggling roles, merging code, and learning to prioritize under pressure was a huge challenge — but also our biggest teacher. Hardware Hurdles: The smart glasses provided at HackUTD were brand new and came with sensor and antenna issues. We had to manually recalibrate the antennas to keep all sensors functional. The SDK itself was partially broken — several bugs required us to modify the libraries directly, and documentation was sparse since the hardware was so new. The default online API for the glasses was extremely slow, so we trained our own AI detection model locally to ensure smooth inference. Backend & Data Struggles: We didn’t receive certain sponsor API keys, so data integration was tricky. We improvised — pulling data from the Zillow API for real-estate listings and scraping cars.com for vehicle data to populate our recommendation system. The entire pipeline had to be built from scratch — from cleaning that data to syncing it with our detection outputs. Despite all that, we delivered a fully functional end-to-end system . 🏆 Accomplishments we’re proud of Building a real, working demo that goes from vision → AI detection → automated listing → AI recommendations. Designing a clean, production-ready frontend with toggles, filters, and a conversational AI. Training our own computer vision model to bypass SDK/API limitations. Creating an AI condition scoring system that generalizes across both vehicles and properties. Developing a recommendation engine that feels personal, natural, and explainable. 📚 What we learned How to coordinate a project from zero under extreme time constraints. The power of data normalization for consistent AI scoring. How to blend agentic AI, computer vision, and user-centric design to solve real-world problems. That hardware, software, and communication all need to work in sync — just like a team. 🔮 What’s next for VisionScout 🤝 Partner APIs for auto dealers (Toyota, Carvana) and real-estate firms (CBRE, Zillow). 📱 Native mobile app for real-time scanning and listing uploads. 🧩 Smarter AI models trained on user preferences for even better personalization. 🏗️ Expansion into insurance inspections, rental evaluations, and condition auditing. 🌍 Long-term: making VisionScout the AI layer that understands the condition, value, and potential of everything you see. 👓 VisionScout – Automating Trust in Vision Because what your eyes see — and what your heart wants — should work together. <div