---
slug: "nutricare-agents"
url: "https://devpost.com/software/nutricare-agents"
title: "NutriCare Agents[Disqualified–Submitted to another hack]"
hackathon: "PANDA Hacks 2025"
organization: "PANDA Organization"
winner: true
words: 1001
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# NutriCare Agents[Disqualified–Submitted to another hack]

> Smart nutrition for all – multi-agent AI transforming public health

[Devpost](https://devpost.com/software/nutricare-agents) · hackathon [[PANDA Hacks 2025]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[agriculture_food]] [[developer_tools]] [[mental_health]]
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** apifirebase-realtime-database, cloud, cloud-storage, colabgemini-api-(google-genai), fastapi, firebase-(authentication, firebase-cloud-functions, firebase-hosting, firebase-hosting), google, google-analytics, google-bigquery, google-cloud, google-cloud-platform-(gcp)

## How they structured the write-up

- about the project

## Body

Artchitecture Agentic Assitant HomePage Recommendations Login News Chat Interface SignUp Project Story: NutriCare Agents About the Project NutriCare Agents is an innovative, multi-agent, AI-powered nutrition advisory system designed to address the specific dietary needs and health challenges of the Vietnamese population. The project was conceived as part of the GDGOC Hackathon Vietnam 2025, with the goal of revolutionizing personalized nutrition guidance through the use of cutting-edge AI technologies such as Graph Neural Networks (GNN), Gemini APIs, and a multi-agent system architecture. The inspiration for this project stemmed from the pressing need to tackle nutrition-related health issues in Vietnam. With rising rates of non-communicable diseases like cardiovascular disease, type 2 diabetes, and digestive disorders, coupled with limited access to professional nutritional counseling, it became clear that a more accessible, personalized solution was needed. Many existing solutions did not take into account the unique cultural, regional, and socioeconomic factors that influence the dietary habits of the Vietnamese people. Inspiration The core inspiration for NutriCare Agents was to bridge the gap between scientific nutritional knowledge and culturally relevant, personalized advice. We wanted to create a system that goes beyond generic recommendations, offering tailored meal suggestions based on individual health conditions, dietary preferences, and budget constraints. Moreover, we aimed to make this system accessible to everyone, including those who face financial and physical barriers to professional nutrition services. The ultimate goal is to improve public health and quality of life through personalized, evidence-based nutrition advice. What We Learned Throughout the development of NutriCare Agents, we learned a great deal about AI orchestration, multi-modal systems, and the integration of advanced technologies in real-world applications. Key takeaways include: AI Integration : The challenge of orchestrating multiple AI agents in a way that allows them to work seamlessly together was both technically challenging and intellectually rewarding. We learned to fine-tune various AI models for specific tasks (e.g., meal recommendations, nutritional analysis) while ensuring they could communicate with one another efficiently. Graph Neural Networks (GNN) : Working with GNNs to personalize meal recommendations based on a user’s health data and preferences was a complex but fascinating learning experience. We were able to use GNNs to analyze large datasets of Vietnamese dishes and ingredients, identifying patterns that allowed us to make tailored recommendations. Cultural Sensitivity : We realized the importance of incorporating local cultural knowledge into the system. It was essential to understand Vietnamese culinary traditions, regional variations, and specific health concerns when designing the system’s recommendations. Multi-Modal Design : Building a system that supports voice commands, text-based input/output, and eventually image and video processing pushed us to think about how users interact with AI in various forms. Designing an intuitive and accessible user experience was crucial for the success of the platform. How We Built the Project We built NutriCare Agents by integrating several powerful technologies and APIs, leveraging both Google’s AI stack and open-source frameworks. The architecture of the system includes: Frontend : The user interface was developed using Next.js and React, with Tailwind CSS for styling, ensuring a responsive, modern design. Firebase Authentication was integrated for user account management. Backend : Firebase Cloud Functions were used for the serverless backend, which allows us to scale the platform without worrying about infrastructure management. Firebase Realtime Database was employed to store user data and preferences, while Google Cloud Storage handled large media files such as images. AI and Machine Learning : The heart of the system is the multi-agent AI framework built using LangChain and Google GenAI SDK. Each agent serves a specific function, such as grounding recommendations in nutritional science or applying logical inference. Graph Neural Networks were employed for personalized meal recommendations based on a large dataset of Vietnamese dishes. Voice Interfaces : Google Speech-to-Text and Text-to-Speech APIs were integrated to provide voice commands and guidance to users. This feature is especially useful for users with disabilities or those who prefer voice interactions. Maps Integration : We incorporated Google Maps JavaScript API and Places API to recommend nearby restaurants and food vendors offering dishes that match user preferences. Challenges Faced While building NutriCare Agents was an incredibly rewarding experience, there were several challenges along the way: Data Scarcity : Gathering a comprehensive dataset of Vietnamese dishes and ingredients with nutritional information was a significant challenge. We had to scrape data from various sources and manually clean it to ensure accuracy. Cultural Sensitivity : Ensuring that the recommendations aligned with the cultural and dietary preferences of the Vietnamese population required extensive research. It was important to avoid generic recommendations and instead reflect the diversity of regional cuisines and local food habits. Multi-Agent Coordination : Orchestrating multiple AI agents, each with its own specialized task, was a complex technical challenge. Ensuring that the agents worked together cohesively required careful design and testing. Scalability : As the platform evolved, we had to ensure that it could scale efficiently to handle large amounts of user data and provide fast, real-time responses. We optimized the system for performance, particularly the recommendation engine, which needed to generate personalized suggestions in a timely manner. User Privacy : Since NutriCare Agents handles sensitive health data, we had to implement robust data privacy mechanisms. This included local data processing and user-controlled data management, which posed additional challenges in terms of system architecture. 👨‍💻 Team Members Nguyễn Lâm Phú Quý – AI Engineer, Backend Specialist Huỳnh Trung Kiệt – Full-Stack Developer, UI/UX Designer Đào Sỹ Duy Minh – AI Researcher, System Architect Phan Bá Thanh – Data Engineer, Infrastructure Lead Conclusion The journey of building NutriCare Agents has been an incredibly fulfilling learning experience. Not only did we have the opportunity to work with cutting-edge AI technologies, but we also had the chance to make a tangible impact on improving health outcomes in Vietnam. By addressing the specific nutritional needs and challenges of the Vietnamese population, NutriCare Agents is helping to democratize access to personalized nutrition guidance. We look forward to continuing to enhance the platform and expand its reach to more users in the future. <div