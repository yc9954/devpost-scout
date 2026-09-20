---
slug: "learnscape-tubm4g"
url: "https://devpost.com/software/learnscape-tubm4g"
title: "Learnscape"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 767
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Learnscape

> Discover the STEM behind real-world objects using AI-powered visual learning. Learnscape is a real-time AI learning companion that turns everyday objects into interactive educational experiences.

[Devpost](https://devpost.com/software/learnscape-tubm4g) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** firebase, firebasestudio, geminiapi, genkit, google-cloud, htmlcanvas, next.js, node.js, typescript, vision, webcameraapi

## How they structured the write-up

- 🌱inspiration
- 🤖 what it does
- 🛠️how we built it
- 🔄 system pipeline
- 🔧 challenges we ran into
- 🎯 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for learnscape

## Body

Landing Page How It Works Features Agent Architecture Examples Solution Problem AI Learning Pipeline Use Case Architecture 🌍Learnscape 🌱Inspiration Learning scientific concepts often feels abstract and disconnected from the real world. Students read about physics, chemistry, and mathematics in textbooks but often struggle to visualize how these ideas appear in everyday life. We asked a simple question: What if the world around us could become an interactive classroom? With the rise of multimodal AI capable of understanding images, text, and context, we saw an opportunity to connect real-world observation with conceptual learning . Learnscape transforms everyday environments into a live learning landscape , where simply pointing a camera at an object can unlock the science behind it. 🤖 What it does Learnscape is a real-time AI learning companion that converts real-world objects into interactive STEM learning experiences. Using the device camera, the system detects objects in the environment and generates relevant scientific concepts related to them. Learners can explore explanations, visualizations, and even ask questions through voice interaction. For example: Point your camera at a glass → Learn about refraction of light Detect a fan → Explore rotational motion and energy Look at a bottle → Understand fluid dynamics and pressure The interface overlays explanations and concept visualizations directly on the camera view, helping learners connect physical objects with scientific principles . With voice interaction , users can also ask questions such as: “Why does this happen?” “How is this used in real life?” "Give some follow up examples for this topics?" "What are the other use cases for this concept?" This turns Learnscape into a conversational AI tutor that interacts with the physical world. 🛠️How we built it Learnscape combines multimodal AI, real-time camera input, and interactive visual overlays . Frontend Next.js for the web application Web Camera API for real-time environment capture HTML Canvas overlays for visual concept diagrams Interactive UI for topic exploration Backend Node.js services for AI orchestration Genkit framework for managing AI workflows AI Models Gemini API for multimodal reasoning Vision understanding for object detection Natural language generation for explanations Conversational interaction for voice queries Infrastructure Firebase / Google Cloud for deployment and backend services 🔄 System Pipeline Learnscape operates through a real-time AI pipeline: Capture camera frame Detect object using multimodal AI Generate relevant STEM topics User selects a concept AI generates explanation Canvas overlays visualize the concept User can ask follow-up questions via voice This architecture enables continuous interaction between the user, the environment, and the AI system. 🔧 Challenges we ran into One major challenge was optimizing AI API usage . Initially, the system triggered object detection multiple times during the learning flow, which quickly exhausted the Gemini API quota. We redesigned the pipeline to cache detected objects and reuse them across the session , reducing redundant inference calls. Another challenge was designing clear and meaningful visual overlays that enhance learning without cluttering the interface. Building intuitive canvas-based diagrams required careful experimentation with UI layout and interaction. We also had to balance AI response latency with real-time interaction , ensuring explanations and visualizations appear quickly enough to maintain a smooth user experience. 🎯 Accomplishments that we're proud of We successfully built a working multimodal AI learning system that connects real-world objects with scientific understanding. Key accomplishments include: Building a multimodal AI pipeline connecting camera input with educational explanations Integrating multiple AI agents for vision understanding, topic generation, explanation, and visualization Creating dynamic concept diagrams using HTML Canvas overlays Designing an interactive UI that keeps the camera feed central to the learning experience Enabling real-time generation of STEM explanations based on objects in the environment The result is a prototype that demonstrates how AI can transform everyday surroundings into learning opportunities. 📚 What we learned Through building Learnscape, we explored how multimodal AI can function as an educational interface rather than just a chatbot . We learned how to: Design systems where AI interacts with the physical world Combine vision understanding with generative reasoning Optimize AI pipelines to reduce redundant inference Build interfaces where learning emerges naturally from observation This project showed us how AI can help bridge the gap between theoretical knowledge and real-world experience . 🔮 What's next for Learnscape We see Learnscape evolving into a fully interactive AI learning platform. Future improvements include: More advanced physics and chemistry simulations Adaptive learning paths personalized to the user Expanded STEM concept coverage Saving & Downloading scenes and conversations Our long-term vision is to create a system where any environment can become an interactive classroom , enabling learners to explore and understand the science behind the world around them. <div