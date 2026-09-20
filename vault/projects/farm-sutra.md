---
slug: "farm-sutra"
url: "https://devpost.com/software/farm-sutra"
title: "Farm Sutra"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 951
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Farm Sutra

> "AI-powered farming assistant for rural India — multilingual, 2G-ready, and built on Amazon Nova."

[Devpost](https://devpost.com/software/farm-sutra) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[civic_government]] [[education]] [[finance_payments]] [[health_clinical]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-web-services, amplify, apigateway, asyncstorage, bedrock, expo.io, lambda, novapro, openmeteo, react-native, typescript, vercel

## How they structured the write-up

- 💡 inspiration
- 🛠️ how we built it
- 📚 what we learned
- 🚧 challenges we faced
- 🔮 what's next for farm sutra

## Body

🌾 Farm Sutra — AI-Powered Farming Assistant for Rural India 💡 Inspiration India has over 140 million farmers , yet most of them make critical decisions — when to sell, what disease is attacking their crop, whether to take a loan — based on word of mouth or outdated information. The breaking point for us was a simple observation: a farmer in rural Haryana loses 30–40% of his crop yield every season not because he lacks hard work, but because he lacks access — access to timely market prices, access to expert crop diagnosis, access to fair credit. Existing agri-apps are built for smartphone-savvy users in English. They ignore the reality that most Indian farmers: Speak Hindi, Punjabi, Tamil, or Haryanvi — not English Are on 2G networks with limited data Have no formal credit history , making banks turn them away We asked ourselves: What if AI could sit in every farmer's pocket — speaking his language, understanding his crop, helping him sell at the right price? That question became Farm Sutra . 🛠️ How We Built It Farm Sutra is a full-stack mobile + cloud application built on the AWS ecosystem, powered at its core by Amazon Nova Pro via Amazon Bedrock. Architecture Overview React Native (Expo) App │ ├── AWS Amplify (API Gateway + Auth layer) │ │ │ └── AWS Lambda (Node.js) │ │ │ └── Amazon Bedrock │ │ │ └── Amazon Nova Pro v1 │ ├── Open-Meteo API (Live GPS Weather) └── AsyncStorage (Offline chat persistence) Feature Breakdown 🤖 Farm Sutra AI (ChatBot) The AI chatbot uses Amazon Nova Pro via Bedrock for all responses. Every query is augmented with a language instruction so Nova replies strictly in the farmer's chosen language — Hindi, Punjabi, Tamil, Haryanvi, or English. Crop Scanner — the most technically complex feature — sends both a base64-encoded image and a fully translated prompt to Nova's multimodal endpoint. The prompt itself is written in the farmer's language, structured to extract disease name, treatment plan, urgency, and confidence level. $$\text{Crop Health Score} = f(\text{Image} {\text{base64}}, \text{Prompt} {\text{lang}}, \text{Nova Pro Multimodal})$$ 🛒 Mandi (Market) A real-time marketplace where farmers list their crops and buyers post demand. Built with AsyncStorage for persistence and includes live GPS-based weather context at the top of the screen. 🌦️ AgriWeather Uses Open-Meteo's free GPS API to pull 7-day live forecasts. The AI layer converts raw WMO weather codes into actionable farming advice — "High humidity for 2 days — fungal infection risk for your wheat" . 🏦 Credit Score A proprietary farmer credit scoring system that rewards positive farming behaviors — scanning crops, checking weather, selling in the Mandi. This creates a verifiable activity log for farmers who have zero formal credit history. $$\text{Credit Score} = \text{Base Score} + \sum_{i=1}^{n} \text{ActivityPoints}_i$$ Where each activity (crop scan, weather check, market listing) contributes weighted points to build a farmer's financial credibility over time. 🌍 Multilingual Engine Every single string in the app — UI labels, AI prompts, error messages, weather alerts, pest warnings — is translated into 5 languages : Language Region English Default Hindi (हिन्दी) North India Punjabi (ਪੰਜਾਬੀ) Punjab Haryanvi (हरियाणवी) Haryana Tamil (தமிழ்) South India 📚 What We Learned Prompt engineering is everything for multilingual AI. Simply asking Nova to "reply in Hindi" wasn't enough — we had to write the entire system prompt in the target language to get culturally accurate, dialect-appropriate responses. The Haryanvi dialect prompt took multiple iterations. Multimodal inputs require careful image compression. Sending full-resolution images to Bedrock on a 2G network was impractical. We settled on quality: 0.5 in Expo ImagePicker — enough for accurate disease diagnosis while staying 2G-friendly. Offline UX is a feature, not an afterthought. For rural farmers, connectivity is unreliable. Building graceful offline handling — persistent chat history, informative banners, queue messaging — required as much thought as the AI integration itself. Credit scoring for the unbanked is a design challenge. Traditional credit models require financial history. We learned to think differently — behavior as credit — rewarding consistent, verifiable farming activities instead. 🚧 Challenges We Faced 1. Haryanvi Dialect Haryanvi is not a standard language with NLP support. Getting Amazon Nova to respond in authentic Haryanvi farmer dialect — with words like "सै", "कोन्या", "आपणा" — required hand-crafting every prompt and testing with native speakers. No existing dataset or library helped here. 2. 2G Network Optimization Most agri-apps assume 4G. We had to rethink every API call: Image compression before Bedrock upload AsyncStorage chat persistence to avoid re-fetching Open-Meteo chosen specifically for its lightweight JSON response 3. Multimodal Prompt Translation Writing the crop scan diagnostic prompt in 5 languages — with the exact same structured output format (emojis as anchors: 🌿, 🔍, 🦠, 💊, ⏰) — so that parsing remains consistent regardless of language was a significant challenge. 4. Credit Score Without Financial Data Building a meaningful credit scoring system for farmers who have zero bank history meant inventing new signals. We used in-app behavioral data as a proxy for creditworthiness — a concept we're proud of and believe has real-world applicability. 🔮 What's Next for Farm Sutra Amazon Nova 2 Sonic integration — Replace mock voice input with real multilingual speech-to-speech using Nova 2 Sonic, enabling truly voice-first interaction for low-literacy farmers Nova 2 Omni — Video-based crop scanning, where farmers can record a 10-second video of their field for richer disease detection Bank API integration — Connect the Credit Score tab directly to Kisan Credit Card loan applications Government scheme push— Partner with state agriculture departments to deliver PM-KISAN and soil health scheme notifications directly to farmers "Farm Sutra is not just an app. It's a voice for the farmer who never had one." <div