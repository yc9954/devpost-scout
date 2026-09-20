---
slug: "tabib"
url: "https://devpost.com/software/tabib"
title: "Tabib"
hackathon: "MongoDB AI Hackathon: Code for a Cause"
organization: "MongoDB"
winner: true
words: 327
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "user/clinician"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Tabib

> This is an app for first aid, basically a chat that helps alleviate concerns about health situation and detect if situation needs medical care or not.

[Devpost](https://devpost.com/software/tabib) · hackathon [[MongoDB AI Hackathon- Code for a Cause]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]]
  <sub>weak: disaster_emergency</sub>
**user** [[clinician]]
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-web-services, langchain, mongodb, node.js, python, typescript

## Body

Inspiration Healthcare can be intimidating and confusing, especially when dealing with emergencies or uncertain symptoms. Inspired by the need for a quick, accessible first-aid tool that can evaluate situations and provide immediate guidance, we created Tabib —a chat-based AI assistant to bridge the gap between immediate first-aid advice and professional medical help. What it does Tabib acts as an AI-powered first responder in a chat format, analyzing conversations to assess the severity of a user's symptoms. It provides initial advice, and if the symptoms appear critical, it routes users to the nearest available doctors. Tabib outputs a JSON file at each interaction, responding to the user's request, along a "is_severe" flag which returns True if LLM senses that the situation requires medical attention. How we built it Generative AI & LLMs : We leveraged generative AI models to interpret user conversations, using AWS Bedrock for embeddings, as well as Groq's llama 3.2 90b vision, since all bedrock's llms were unavailable on the us-west-1 region. Database & Search : MongoDB Atlas stores and retrieves user data efficiently, with vector search allowing for fast, relevant information recall. Routing System : Using geographic information, Tabib connects users to nearby doctors if a severe condition is detected. Challenges we ran into Accuracy of Diagnosis : Ensuring the AI could accurately distinguish between mild and severe symptoms was challenging. Accomplishments that we're proud of Successfully deploying an app that provides immediate health guidance while maintaining accuracy. Integrating a real-time vector search in MongoDB Atlas for high-performance data retrieval. Designing a JSON-based output that allows a dynamic user-AI interaction What we learned We gained valuable insights into embedding techniques and integrating vector databases with real-time applications. Working with healthcare data reinforced our understanding of privacy and security protocols. What's next for Tabib Enhanced Routing : Expanding the doctor network and adding support for telehealth consultations. Improved Symptom Detection : Integrating additional health conditions to improve the range of symptoms Tabib can assess. <div