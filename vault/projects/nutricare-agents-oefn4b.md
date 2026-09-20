---
slug: "nutricare-agents-oefn4b"
url: "https://devpost.com/software/nutricare-agents-oefn4b"
title: "NutriCare Agents"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 583
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# NutriCare Agents

> NutriCare Agents: Revolutionizing nutrition with AI-driven, personalized meal recommendations tailored to your health, tastes, and lifestyle — for a healthier, smarter tomorrow!

[Devpost](https://devpost.com/software/nutricare-agents-oefn4b) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[voice_speech]]
  <sub>weak: realtime_stream, vision_ocr</sub>
**domain** [[agriculture_food]]
  <sub>weak: accessibility, developer_tools</sub>
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** api, firebase, gemini, google, google-cloud, javascript, maps, next.js, openai, places, react, tailwind

## Body

Logo Inspiration The core inspiration for NutriCare Agents was to bridge the gap between scientific nutritional knowledge and culturally relevant, personalized advice. We wanted to build a system that goes beyond generic recommendations, offering tailored meal suggestions based on individual health conditions, dietary preferences, and budget constraints. Our vision was to make personalized nutrition guidance accessible to everyone , including people who face financial or physical barriers to traditional nutrition services. Ultimately, NutriCare Agents aims to improve public health and quality of life through evidence-based, culturally aware nutrition intelligence . What We Learned Throughout the development of NutriCare Agents, we gained valuable insights into AI orchestration, multi-modal systems , and the challenges of integrating advanced technologies into real-world applications. AI Integration Orchestrating multiple AI agents and enabling them to collaborate seamlessly was both challenging and rewarding. We learned to fine-tune AI models for specialized tasks — such as meal recommendation or nutrition analysis — and design a communication layer that keeps them synchronized. Graph Neural Networks (GNN) We explored GNNs to personalize meal recommendations using user health data and preferences. By modeling relationships between Vietnamese dishes, ingredients, and dietary constraints, GNNs helped us uncover meaningful patterns that power our recommendation engine. Cultural Sensitivity Nutrition is deeply cultural. We realized the importance of integrating Vietnamese culinary traditions, regional differences, and local health concerns into the logic of our recommendations. This ensured our system remained relevant and trusted by real users. Multi-Modal Design Supporting text, voice, and potentially image/video inputs pushed us to think more broadly about AI–human interaction. Creating an intuitive, accessible experience—especially for users with disabilities—was a major design priority. How We Built the Project NutriCare Agents was built by integrating a powerful stack of Google AI technologies and open-source frameworks. The system architecture includes: Frontend Built with Next.js + React Styled with Tailwind CSS for a modern, responsive UI Firebase Authentication for secure user management Backend Firebase Cloud Functions for a scalable, serverless backend Firebase Realtime Database for storing user data and preferences Google Cloud Storage for managing large media files (e.g., images) AI & Machine Learning Multi-agent framework built using LangChain + Google GenAI SDK Specialized agents for: Nutritional grounding Logical inference Meal recommendation Graph Neural Networks (GNNs) used to model Vietnamese dishes and personalize suggestions Voice Interfaces Google Speech-to-Text and Text-to-Speech APIs Enables hands-free operation and accessibility support Maps Integration Google Maps JavaScript API Places API to recommend nearby restaurants that match the user’s dietary profile Challenges Faced Data Scarcity Reliable nutritional data for Vietnamese cuisine is limited. We scraped multiple sources and manually cleaned data to ensure completeness and accuracy. Cultural Sensitivity We avoided generic recommendations by studying regional cuisines, portion norms, and local dietary habits—ensuring the system felt authentically Vietnamese. Multi-Agent Coordination Designing agents that specialize but still cooperate fluidly was a significant architectural challenge. Scalability The recommendation engine needed to deliver real-time, personalized results at scale. This required heavy optimization and efficient backend design. User Privacy Handling sensitive health data required strong privacy protections, including: Local processing where possible User-controlled data management Secure Cloud Function isolation Conclusion Building NutriCare Agents has been a deeply meaningful and technically enriching journey. We combined cutting-edge AI technologies with culturally grounded nutritional knowledge to create a system capable of improving public health in Vietnam. By personalizing nutrition advice and making it accessible to all, NutriCare Agents contributes to democratizing healthcare through AI. We are excited to continue improving the platform and expanding its impact to more users in the future. <div