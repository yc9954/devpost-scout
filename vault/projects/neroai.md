---
slug: "neroai"
url: "https://devpost.com/software/neroai"
title: "NeroFashion"
hackathon: "GKE Turns 10 Hackathon"
organization: "Google"
winner: true
words: 676
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# NeroFashion

> Bringing online shopping closer to reality with AI.

[Devpost](https://devpost.com/software/neroai) · hackathon [[GKE Turns 10 Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[retail_commerce]]
**substrate** [[video_visual]]

**stack** fastapi, gemini, google-genai, nanobanana, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nerofashion

## Body

Products Product Detail AI Image Remix AI Image Remix - Image Ready Fashion Assistant AI AI Image Description - Accessibility Smart Product Recommender Smart Product Recommender - Result Inspiration The biggest barrier in online shopping is not price, it’s the lack of proximity to the product . Customers can’t touch, try, or feel items before purchasing, which creates insecurity, frustration, and high return rates. Our inspiration came from this challenge: how can we make e-commerce more personal, inclusive, and fun? What it does We built a new AI microservice for the online boutique application that runs on Google Kubernetes Engine (GKE) . Without changing the core system, we added a layer of intelligence that helps customers feel closer to the products. ✨ Key features: Image mixing - Users can see themselves wearing the product before buying. Smart descriptions + Accessibility - AI generates detailed product/person descriptions. With text-to-speech , blind users can describe interests via audio and receive personalized recommendations. Fashion tips and compliments - Makes the experience more human and engaging. Intent-based search - The user can say: “I want sunglasses for summer” . The AI extracts intent, finds the product in the catalog with price/metadata, and shows it applied to the user. How we built it Stack : Google Gen AI API (Nano Banana + LLMs) FastAPI for the API Docker for containerization GKE for orchestration and scalability Designed as a plug-and-play microservice , so intelligence could be added seamlessly to the boutique application. Handled multimodal inputs: text, image, and audio in the same pipeline. Challenges we ran into We faced the challenge of integrating a new service into the boutique app while preserving its original architecture, ensuring that the microservice could extend the system without breaking it. Deploying and orchestrating AI workloads on GKE required careful design to guarantee scalability and modularity. Another challenge was managing multimodal data, handling text, images, and audio together in a consistent pipeline. Finally, maintaining low latency was essential so that the AI experience would feel immediate and interactive for end users. Accomplishments that we're proud of We are proud of having built and deployed a fully functional AI service on GKE in a short time frame, proving how fast innovation can be scaled with the right architecture. Delivering features that are both innovative and accessible was an achievement that truly motivated us, as we opened new possibilities for blind and visually impaired users. Beyond the technical milestones, we are proud of how our team worked: engaged, collaborative, and deeply focused on solving a real and relevant problem. This spirit of integration and shared purpose allowed us to move quickly, overcome blockers, and deliver a solution that went beyond expectations. What we learned We learned how powerful GKE can be for rapidly prototyping and scaling AI services, giving us the confidence to build modular microservices that integrate smoothly into existing systems. We also learned how accessibility should not be an afterthought: by designing inclusive features such as text-to-speech, we extended the impact of our solution to a broader audience. Finally, we learned that creativity matters, by mixing image generation, product compliments, and fashion tips, we turned a purely technical solution into a human-centered experience that people can relate to. What's next for NeroFashion Our next step is to deepen our knowledge and usage of GKE, exploring its full potential for scaling AI services in production scenarios. We also want to test recommendation models on a larger and more complex catalog, since during this hackathon we felt limited by the number of product samples available. Another key area is accessibility: we plan to continue improving inclusive features so that online shopping becomes truly universal. Finally, we see a clear application of MCP (Model Context Protocol) and deep agents in this project. Our goal is to convert the nanobananaservice API we built into an MCP server, enabling deep agents to consume our service seamlessly. Unfortunately, we didn’t have enough time to implement this during the hackathon, but it is one of the directions we’re most excited to explore next. <div