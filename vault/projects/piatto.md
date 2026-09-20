---
slug: "piatto"
url: "https://devpost.com/software/piatto"
title: "Piatto"
hackathon: "Cloud Run Hackathon"
organization: "Google"
winner: true
words: 828
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Piatto

> Meet Piatto - the AI chef that designs recipes just for you and cooks along, step by step.

[Devpost](https://devpost.com/software/piatto) · hackathon [[Cloud Run Hackathon]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[agriculture_food]] [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ci/cd, docker, fastapi, gemini-2.5-flash, github-actions, google-agent-development-kit-(adk), google-artifact-registry, google-cloud, google-cloud-cdn, google-cloud-run, google-cloud-sql, google-secret-manager, javascript, jwt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for piatto

## Body

Inspiration Cooking should be an act of creativity, but for many of us, it starts with chaos. That feeling of staring into a full fridge with no idea what to make is all too familiar. We wanted to build a culinary co-pilot that could instantly turn your random ingredients into a delicious recipe and then guide you, step-by-step, through the cooking process. We envisioned a tool that handles the mess - managing timers and answering questions - so you can focus on the fun of creating. The Google Cloud Run Hackathon was the perfect start to bring this vision to life. What it does Piatto is your AI-powered kitchen assistant that transforms culinary chaos into creative calm. Simply tell Piatto what ingredients you have (by text or just by snapping a photo!), and it springs into action: 🍅 Generates a personalized recipe tailored to your wishes and what's in your kitchen 🥄 Provides interactive, step-by-step guidance with automated timers that keep you on track 🗣️ Answers your cooking questions hands-free via voice. Need a substitute for cilantro? Just ask! ✅ Acts as your all-in-one cooking hub , making the entire process from idea to dish seamless and enjoyable How we built it Piatto is powered by a sophisticated multi-agent AI system built with the Google Agent Development Kit (ADK) and the Gemini models. This allows different AI agents to specialize in tasks like analyzing images, creating recipes, and providing interactive instructions. The entire application runs on a modern, serverless architecture on Google Cloud: Backend: A high-performance FastAPI application running as a container on Google Cloud Run Data Storage: We used a dual-database strategy. A secure and managed Cloud SQL instance stores all our structured data (like user profiles and recipes), while Cloud Storage handles all our blob data, such as user-uploaded ingredient images Frontend: A speedy and responsive user interface built with React and Vite Infrastructure: We used Google Cloud CDN to deliver our app globally with lightning speed and GitHub Actions for a fully automated CI/CD pipeline Challenges we ran into As a team, we were brand new to cloud services, so diving into Google Cloud Platform felt like jumping into the deep end! Our biggest challenge was navigating the entire ecosystem from scratch. We spent countless hours learning how to: Configure Secure Networking: Setting up a VPC and getting Cloud Run to communicate securely with our Cloud SQL database was a major hurdle. Understanding service accounts and permissions felt like learning a new language Managing Credentials: Figuring out the right way to handle secrets and API keys using Secret Manager instead of hardcoding them was a critical learning curve The "Serverless" Mindset: Shifting our thinking to a stateless, event-driven architecture with Cloud Run took time. Our first few deployments failed in ways we didn't expect, forcing us to rethink how we built our application Accomplishments that we're proud of From Cloud Novices to Builders: We are incredibly proud of building a production-grade, secure, and scalable cloud infrastructure with zero prior experience. Getting all the GCP services to work together harmoniously was a huge win for us! 🎉 Fully Serverless & Scalable: Piatto can scale from zero to infinity automatically thanks to Cloud Run. It’s cost-efficient and ready for a global audience right out of the gate Seamless Multi-Modal Experience: We successfully integrated both text and image-based ingredient input, making the app incredibly intuitive and easy to use End-to-End DevOps Automation: We built a CI/CD pipeline with GitHub Actions that automatically deploys our app. This allowed us to iterate quickly and focus on building features, not on manual deployment chores What we learned Google Cloud is Incredibly Powerful (Once You Get It): That initial steep learning curve was tough, but once the concepts clicked, we felt empowered. Tools like Cloud Run are a superpower for developers, abstracting away the complexity of infrastructure management Security First is Non-Negotiable: Our initial struggles taught us the immense importance of building securely from the start. Properly using VPCs and Secret Manager is not just a best practice; it's essential Structured AI is Reliable AI: Forcing our AI agents to output structured, validated data using Pydantic schemas was a game-changer. It turned unpredictable LLM responses into reliable, application-ready data What's next for Piatto 📱 A Dedicated Mobile App: We want to bring Piatto to your fingertips with native iOS and Android apps for an even smoother on-the-go cooking experience 🧠 Personalized Culinary Profiles: Piatto will learn your tastes! It will track your favorite cuisines and dietary preferences to suggest recipes you’re guaranteed to love 📅 Advanced Meal Planning: Moving beyond single recipes to help you plan your entire week, generating shopping lists and reducing food waste 🤝 Recipe Sharing and Community: Create and share your culinary masterpieces with friends, and see what they're cooking up with Piatto 🤖 Smart Kitchen Integration: We dream of a future where Piatto can preheat your smart oven or set timers on your smart display automatically <div