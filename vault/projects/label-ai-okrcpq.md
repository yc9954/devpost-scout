---
slug: "label-ai-okrcpq"
url: "https://devpost.com/software/label-ai-okrcpq"
title: "Label Ai"
hackathon: "Hacktivism II"
organization: "Politechs"
winner: true
words: 353
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Label Ai

> Label AI – Your food, decoded in 3 seconds

[Devpost](https://devpost.com/software/label-ai-okrcpq) · hackathon [[Hacktivism II]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[scientific_research]]
**substrate** [[genomic_bio]] [[geospatial]] [[video_visual]]

**stack** ai, googleai, health, innovation, javascript, react, tesseract

## How they structured the write-up

- 🌟 inspiration
- 🛠️ how we built it
- 📚 what we learned
- 🚧 challenges we faced
- 🔬 math behind it
- 🏆 outcome

## Body

📖 Project Story – Label AI 🌟 Inspiration Every day, millions of people struggle to understand complex food labels filled with jargon, hidden additives, and confusing nutrition facts. As someone passionate about health tech and AI, I wanted to create a tool that empowers people to make smarter, healthier food choices instantly. That’s where Label AI was born — a fusion of computer vision, NLP, and AI that decodes food in just 3 seconds. 🛠️ How We Built It Frontend : Built with React 18 + Context API for smooth state management. Vision Processing : Custom pipeline with Google Cloud Vision API + Tesseract.js for OCR. AI/ML : Powered by Gemini 2.0 Flash for semantic understanding of ingredients. Backend : Secure APIs with encryption to protect user health data. Deployment : Deployed on Vercel for fast, scalable hosting. 📚 What We Learned Fine-tuning OCR pipelines to deal with low-quality packaging images . Leveraging AI + NLP to go beyond text extraction and truly understand health risks & allergens . Balancing real-time speed (< 1s) with accuracy (~97%). The importance of user-first design in health apps — clear insights matter more than raw data. 🚧 Challenges We Faced Noisy Data : Food labels have inconsistent layouts, fonts, and languages. Allergen Detection : Ingredients like “milk solids” vs. “lactose” required semantic AI mapping. Optimization : Achieving sub-second performance while running OCR + AI analysis together. User Trust : Designing a privacy-first architecture (end-to-end encryption, zero-knowledge). 🔬 Math Behind It We modeled health scoring as a weighted sum of nutritional components: $$ HealthScore = \sum_{i=1}^n w_i \cdot x_i $$ Where: ( x_i ) = nutritional value (sugar, fat, protein, etc.) ( w_i ) = weight based on user’s dietary profile (e.g., diabetic, allergic). This formula allows personalized scoring for each user in real time. 🏆 Outcome Built in a hackathon and recognized for real-world impact . Helps users with diabetes, allergies, or dietary restrictions make informed food decisions. Reinforces the idea that AI can truly enhance everyday life . ✨ Label AI isn’t just a project it’s a step toward a healthier, more informed future. <div