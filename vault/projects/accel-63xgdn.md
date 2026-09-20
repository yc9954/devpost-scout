---
slug: "accel-63xgdn"
url: "https://devpost.com/software/accel-63xgdn"
title: "Accel"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 566
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Accel

> Your empathetic chemistry tutor 🧪

[Devpost](https://devpost.com/software/accel-63xgdn) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-bedrock, flask, hume, intel-ai, langchain, next.js, react.js, tailwind

## How they structured the write-up

- about the project
- technologies
- contact

## Body

Accel - Won $3,100 Your empathetic chemistry tutor GitHub » Alex Talreja · Cindy Yang · David Mazur · Selina Sun About The Project Traditional study methods and automated tutoring systems often focus solely on providing answers. This approach neglects the emotional and cognitive processes that are crucial for effective learning. Students are left feeling overwhelmed, anxious, and disconnected from the material. Accel is designed to address these challenges by offering a unique blend of advanced AI technology and emotional intelligence. Here's how Accel transforms the study experience: Concept Breakdown : Accel deconstructs complex chemistry topics into easy-to-understand segments, ensuring that students grasp foundational concepts thoroughly. Emotional Intelligence : Using cutting-edge vocal emotion recognition technology, Accel detects frustration, confusion, or boredom, tailoring its responses to match the student’s emotional state, offering encouragement and hints instead of immediate answers. Adaptive Learning : With Quiz Mode, students receive feedback on their progress, highlighting their strengths and areas for improvement, fostering a sense of accomplishment. Built With Technologies Technical jargon time 🙂‍↕️ Intel AI To build the core capabilities of Accel, we used both Intel Gaudi and the Intel AI PC. Intel Gaudi allowed us to distill a model ("selinas/Accel3") by fine-tuning with synthetic data we generated from Llama 70B model to 3B, allowing us to successfully run our app on the Intel AI PC. The prospect of distributing AI apps with local compute to deliver a cleaner and more secure user experience was very exciting, and we also enjoyed thinking about the distributed systems implications of NPUs. Amazon Bedrock To further enhance the capabilities of Accel, we utilized Amazon Bedrock to integrate Retrieval-Augmented Generation (RAG) and AI agents. This integration allows the chatbot to provide more accurate, contextually relevant, and detailed responses, ensuring a comprehensive learning experience for students. When a student asks a question, the RAG mechanism first retrieves relevant information from a vast database of chemistry resources. It then uses this retrieved information to generate detailed and accurate responses. This ensures that the answers are not only contextually relevant but also backed by reliable sources. Additionally, we utilized agents to service the chat and quiz features of Accel. Accel dynamically routes queries to the appropriate agent, which work in coordination to deliver a seamless and multi-faceted tutoring experience. When a student queries, the relevant agent is activated to provide a specialized response. Hume EVI The goal of Accel is to not only provides accurate academic support but also understands and responds to the emotional states of students, fostering a more supportive and effective learning environment. Hume's EVI model was utilized for real-time speech to text (and emotion) conversion. The model begins listening when the user clicks the microphone input button, updating the input bar with what the model has heard so far. When the user turns their microphone off, this text is automatically sent as a message to Accel, along with the top 5 emotions picked up by EVI. Accel uses these cues to generate an appropriate response using our fine-tuned LLM. Additionally, the users' current mood gauge is displayed on the frontend for a deeper awareness of their own study tendencies. Contact Alex Talreja (LLM agents, Amazon Bedrock, RAG) - vta3nc@virginia.edu Cindy Yang (frontend, design, systems integration) - cwyang@umich.edu David Mazur (model distillation, model integration into web app) - dsmazur@umich.edu Selina Sun (synthetic data generation, scalable data for training, distribution through HuggingFace) - selinas@umich.edu <div