---
slug: "zero-kare-lizf08"
url: "https://devpost.com/software/zero-kare-lizf08"
title: "Zero Kare"
hackathon: "MongoDB AI Hackathon: Code for a Cause"
organization: "MongoDB"
winner: true
words: 742
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Zero Kare

> Maternal Health Analytics with AI & SDOH Integration

[Devpost](https://devpost.com/software/zero-kare-lizf08) · hackathon [[MongoDB AI Hackathon- Code for a Cause]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[health_clinical]] [[housing_homeless]] [[transportation]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[medical_record]] [[structured_db]] [[video_visual]]

**stack** javascript

## How they structured the write-up

- inspiration
- 🌟 what it does
- 🛠️ how we built it
- ⚡ challenges we faced
- 🎉 accomplishments we're proud of
- 🔍 what’s next
- 🚀 why zero kare stands out
- 🌐 how it works
- 📂 project structure
- 🛠️ tech stack

## Body

🚀 Zero Kare: Maternal Health Analytics with AI & SDOH Integration Inspiration Maternal healthcare remains a global challenge, especially in underserved communities. Zero Kare was inspired by the need to leverage AI and Social Determinants of Health (SDOH) to improve maternal healthcare outcomes. 🌟 What it Does Zero Kare is a comprehensive maternal health analytics platform that empowers healthcare providers and policymakers through AI-driven insights and interactive visualizations. Key Features: AI-Powered Risk Assessment: Utilizes Google Gemini for analyzing images and videos to assess risks like preeclampsia, diabetes, and more. SDOH Analysis: Maps social determinants like food security, housing stability, and healthcare access to health outcomes. Predictive Insights: Predicts intervention outcomes and tracks trends in risk factors over time. Interactive Dashboard: Provides real-time visualizations of demographic and regional disparities. 🛠️ How We Built It Frontend React.js : For creating a modern, responsive user interface. Recharts : For interactive data visualizations. shadcn/ui : Provides consistent, accessible UI components. GSAP: for smooth animations Backend Node.js + Express.js : API handling and data processing. MongoDB : Stores patient records, videos, and analysis results. AI & Machine Learning Google Gemini API : Multimodal analysis of images and videos for maternal health insights. Google Cloud Vision API : Detects SDOH factors in visuals. Security Zero-Knowledge Proofs (ZKPs) : Secure and verifiable access to patient medical records without exposing sensitive information. Data Encryption : Protects patient data in transit and at rest. ⚡ Challenges We Faced AI Integration : Combining insights from Google Gemini and SDOH data required careful preprocessing and interpretation. Data Privacy : Implementing Zero-Knowledge Proofs added complexity to ensure data security. Video File Handling : Processing and analyzing large video files posed technical challenges. 🎉 Accomplishments We're Proud Of Successfully Integrated Multimodal AI : Leveraged Google Gemini for actionable maternal health insights. Privacy by Design : Implemented ZKPs to ensure secure, verifiable data access. Scalable Interface : Created a user-friendly, intuitive platform for healthcare stakeholders. Mobile App Development : Built a companion app for increased accessibility. 🔍 What’s Next Expanded Data Sources : Integrate additional datasets for more comprehensive SDOH analysis. Healthcare Partnerships : Collaborate with hospitals and NGOs to pilot Zero Kare in real-world settings. Enhanced Predictive Models : Use federated learning to improve accuracy while ensuring data privacy. 🚀 Why Zero Kare Stands Out Alignment with Hackathon Goals: Social Good : Tackles maternal health disparities by integrating SDOH data and AI insights. Innovation : Combines Google Gemini's multimodal AI with real-time Google Search grounding and secure data practices. Impact : Designed to address healthcare challenges in underserved communities. 🌐 How it Works Initial Analysis Google Gemini analyzes images and videos for maternal health insights and SDOH factors. Grounding with Google Search Insights are sent to Google Search for real-time retrieval of the latest medical knowledge. Enhanced Risk Assessment Combines initial analysis with grounded information to produce a comprehensive risk profile. Analytics Dashboard Displays: Risk Trends : Tracks risk levels over time. Demographics : Highlights disparities in outcomes by age, location, etc. SDOH Clustering : Groups patients with similar challenges for targeted intervention. Regional Mapping : Identifies high-risk geographic areas. Photorealistic 3D Maps Interactive 3D map navigation with altitude control Real-time environmental data visualization Dynamic 3D markers for points of interest Draggable UI components for customizable workspace Responsive dashboard with live updates Gamification Environmental Data Display: Shows real-time environmental data (temperature, wind speed, air quality) fetched from APIs. Hotspot Analysis: Allows users to find and analyze environmental hotspots on a 3D map. Score and Sustainability Rating: Tracks the user's score and provides a sustainability rating based on their progress. Confetti Celebration: Celebrates successful hotspot analysis with a confetti effect. Camera Controls: Offers smooth camera controls to explore the 3D map, including fly-to and fly-around functionalities. Dynamic Hotspots: Generates hotspots dynamically based on the map's center location. Environmental Tips: Periodically displays interesting facts about environmental sustainability. Wind Simulation: Simulates wind conditions, updating the wind speed and direction periodically. 📂 Project Structure ZeroKare/ ├── frontend/ │ ├── src/ │ │ ├── components/ │ │ ├── pages/ │ │ ├── utils/ │ │ └── App.jsx │ └── package.json ├── backend/ │ ├── routes/ │ ├── models/ │ ├── controllers/ │ ├── server.js │ └── package.json ├── data/ │ ├── datasets/ │ └── analysis_results/ ├── README.md └── .env 🛠️ Tech Stack Component Technology Frontend React, Tailwind CSS Visualizations Recharts Backend Node.js, Express.js Database MongoDB AI & ML Google Gemini API, Google Cloud Vision API Security Zero-Knowledge Proofs, snarkjs <div