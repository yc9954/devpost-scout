---
slug: "ecobolt"
url: "https://devpost.com/software/ecobolt"
title: "Ecobolt"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 541
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/security_privacy"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Ecobolt

> A comprehensive IoT monitoring system for agricultural environments

[Devpost](https://devpost.com/software/ecobolt) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[agriculture_food]] [[security_privacy]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** bolt.new, esp32, npksensor, salesforce, twilio

## How they structured the write-up

- 🌱 inspiration
- ⚙️ what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for ecobolt
- 🏁 challenge compliance

## Body

AI insight of the field Analytics of fileld data Appliance control Threshold setting Device detail Email Alert Whatsapp Alert SMS Alert Weather information 🌱 Inspiration Farming today still relies heavily on manual observation and guesswork. Small-scale farmers often lack access to real-time data and intelligent tools, making it hard to respond quickly to changing environmental conditions. We wanted to bridge this digital gap by building a smart, AI-powered farming assistant that’s affordable, scalable, and farmer-friendly. ⚙️ What it does EcoBolt is an agricultural IoT monitoring system that: Captures real-time environmental data (temperature, humidity, light, soil conditions, nutrients) Visualizes live and historical data through an interactive dashboard Sends alerts via SMS/email when parameters breach critical thresholds Offers AI-powered recommendations using IBM WatsonX Controls appliances (pumps, lights, etc.) remotely via Bolt IoT 🛠️ How we built it Frontend: React 18, TypeScript, Tailwind CSS, Chart.js Backend: Supabase (PostgreSQL, Realtime, Auth), Edge Functions Hardware: ESP32 microcontroller with soil, light, and weather sensors AI Layer: IBM WatsonX for generating contextual farming suggestions Notifications: Salesforce email/SMS integration with Twilio Other APIs: OpenWeatherMap for weather, Bolt Cloud for appliance control 🚧 Challenges we ran into Real-time synchronization between ESP32 and Supabase Managing consistent device authentication and secure data flow Fine-tuning WatsonX prompts to produce localized and actionable advice Formatting email/SMS alerts reliably via Salesforce for all devices Handling fallback when internet/cloud services were unavailable 🏆 Accomplishments that we're proud of Fully functional production-grade dashboard with real-time updates Successfully integrated WatsonX for smart, AI-based recommendations Built a modular device management system with multi-device support Enabled remote appliance control with status feedback using Bolt Cloud Created a scalable, end-to-end system deployable on real farms 📚 What we learned Practical use of Supabase’s real-time capabilities and Row Level Security Efficient IoT data handling with ESP32 and multiple sensors Best practices in AI prompt engineering for actionable results Importance of weather-awareness and fallback systems in farming Real-world usability factors for rural, low-connectivity areas 🚀 What's next for EcoBolt Launching a mobile app for farmers with offline support Training local AI models for low-connectivity, edge-based insights Incorporating computer vision for pest/disease detection Expanding to hydroponic and polyhouse environments Partnering with agricultural institutions for real-world pilots 🏁 Challenge Compliance Deploy Challenge: EcoBolt has been successfully deployed as a full-stack application using Netlify . The project demonstrates smooth integration between frontend, backend, and real-time hardware communication — all hosted seamlessly on Netlify. The live deployment ensures reliable access and responsive performance across devices. 🔗 Live Site Startup Challenge: EcoBolt leverages Supabase for authentication, real-time database updates, row-level security, and serverless Edge Functions. The architecture is designed to scale with ease — from managing multiple devices per farm to handling high-frequency sensor data. This setup positions EcoBolt to scale to millions of users and IoT events with minimal overhead. Inspirational Story: EcoBolt was born from a personal motivation to empower farmers in rural areas with accessible technology. As someone who has seen the challenges faced in traditional agriculture, I wanted to create a tool that could bring AI and IoT directly to the fields. Built entirely using Bolt.new's prompt-based workflow , this project reflects overcoming both technical and resource limitations, proving that with the right tools and vision, innovation can be both meaningful and scalable. <div