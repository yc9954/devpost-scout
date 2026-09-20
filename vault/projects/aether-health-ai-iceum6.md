---
slug: "aether-health-ai-iceum6"
url: "https://devpost.com/software/aether-health-ai-iceum6"
title: "Aether Health AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 844
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Aether Health AI

> Trusted healthcare AI, grounded in science and nature.

[Devpost](https://devpost.com/software/aether-health-ai-iceum6) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[civic_government]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** css3, framer, gemini, html5, javascript, kaggle, mapbox, mongodb, node.js, rag, react, typescript, who-dataset

## How they structured the write-up

- inspiration
- what it does
- how we built it
- built with
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aether health ai

## Body

Inspiration The inspiration for Aether Health stemmed from a critical flaw in modern digital healthcare: it often creates more anxiety than it cures. We noticed that when people Google their symptoms, they fall into the trap of "cyberchondria," misinterpreting mild issues as fatal diseases due to uncurated search results. Furthermore, we saw systemic issues across the globe: dangerous medication errors caused by illegible doctor handwriting, the alarming rise of counterfeit medicines in developing nations, and language barriers that isolate patients. We wanted to build a platform that didn't feel clinical, sterile, or anxiety-inducing. We drew inspiration from the Five Elements of Nature (Fire, Water, Air, Earth, and Space) to create a calming, holistic, and culturally inclusive framework. Our goal was to harmonize advanced AI with empathetic design, replacing panic with verified, accessible support. What it does Aether Health is a unified healthcare companion that maps specific medical challenges to the five elements: 🔥 Fire (VitalScan): An empathetic symptom checker that uses sentiment analysis to detect user panic and adjusts its tone to be calming. It provides probability-based assessments using RAG grounded in WHO guidelines. 💧 Water (HydroGuard): A community-driven map and citizen science tool for tracking local water safety and reporting contamination to local officials. 🌬️ Air (ClearScript): An AI prescription reader that deciphers notoriously messy doctor handwriting, autocorrects drug names, and sets automated medication reminders. 🌍 Earth (TrueMeds): A visual counterfeit defense system that analyzes medicine packaging and physical pill characteristics to verify authenticity against a "Golden Dataset." 🌌 Space (LifeLoop): The holistic intelligence layer that translates complex medical jargon into local dialects and aggregates all health data for a personalized overview. How we built it We built Aether Health with a focus on seamless user experience and robust, responsible AI. Frontend: We used React 18 with Vite and TypeScript for a highly responsive interface. To achieve our "calming" aesthetic, we utilized Tailwind CSS with a Glassmorphism UI and Framer Motion for smooth, organic animations. Backend & Data: The backend runs on Node.js, utilizing MongoDB/Firebase for secure, privacy-first data storage of user profiles and contamination reports. AI Engine: The core of the platform is powered by the Google Gemini API (1.5/2.5 Pro & Flash). We utilized Gemini's text capabilities for empathetic chat and real-time translation. We built a Retrieval-Augmented Generation (RAG) pipeline to ground symptom analysis strictly in verified World Health Organization (WHO) datasets. We heavily leveraged Gemini's multimodal Vision API to perform advanced OCR on messy prescriptions and visual classification for counterfeit pill detection. Built With Languages: TypeScript, JavaScript, HTML5, CSS3 Frontend Frameworks & Libraries: React 18, Vite, Tailwind CSS, Framer Motion Backend Runtime: Node.js Databases & Cloud Storage: MongoDB, Firebase AI & Machine Learning: Google Gemini API (Gemini 1.5/2.5 Pro & Flash, Gemini Vision for multimodal tasks), Retrieval-Augmented Generation (RAG) APIs & Integrations: Google Maps API / Mapbox (for HydroGuard mapping) Tools: Git, GitHub, npm/yarn Challenges we ran into Preventing AI Hallucinations: Using LLMs for medical advice is inherently risky. We had to overcome the challenge of the AI "guessing" diagnoses. We solved this by implementing a strict RAG architecture that restricts the AI to only generating responses based on verified WHO clinical guidelines. Decoding Doctor Handwriting: Traditional OCR completely fails on cursive, messy medical scripts. We had to meticulously prompt and tune the Gemini Vision API to not only read the text but contextually understand pharmacological terms to autocorrect misspelled drug names. Balancing Tone and Accuracy: It was challenging to make the AI sound empathetic and calming without downplaying potentially serious symptoms. We had to refine our sentiment analysis prompts to ensure the AI acts as a supportive guide while hardcoding it to escalate critical symptoms (like chest pain) to human emergency services. Accomplishments that we're proud of Element Tick-Mark Traceability: We are incredibly proud of our Explainable AI (XAI) feature. Whenever the AI provides an assessment, it visually cites the exact WHO data source that led to that conclusion, building immense user trust. The Zero-Panic UI: Successfully breaking away from the traditional, stressful "medical app" aesthetic and creating an interface that actually lowers a user's heart rate through design. Multimodal Integration: Seamlessly blending text processing, sentiment analysis, and advanced image recognition (for both prescriptions and counterfeit detection) into a single, cohesive user journey. What we learned Building Aether Health taught us the profound difference between "accurate AI" and "empathetic AI." We learned that how health information is delivered is just as important as the information itself. Technically, we gained deep expertise in implementing RAG pipelines for specialized, high-stakes domains and pushing the boundaries of what multimodal LLMs can achieve in complex optical character recognition tasks. What's next for Aether Health AI Our vision for the future is expansive: Expanding Earth (TrueMeds): Partnering with global pharmaceutical companies to expand our "Golden Dataset" of verified medicine imagery. Government API Integration: Connecting HydroGuard directly into municipal water safety databases to automate the ticket generation process for contamination reports. Wearable Sync: Integrating smartwatch data (heart rate, sleep) into Space (LifeLoop) to give the AI even more context before it provides lifestyle recommendations. <div