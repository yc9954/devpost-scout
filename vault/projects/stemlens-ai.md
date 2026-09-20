---
slug: "stemlens-ai"
url: "https://devpost.com/software/stemlens-ai"
title: "STEMLENS-AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 565
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# STEMLENS-AI

> Turn any real-world object into a STEM lesson

[Devpost](https://devpost.com/software/stemlens-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[climate_energy]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** firebase, next.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i faced
- what i learned
- future improvements
- impact

## Body

STEMLens AI Inspiration As a student, I have often noticed that many learners struggle to connect STEM concepts to the world around them. Subjects like Physics, Mathematics, Engineering, and Technology are usually taught through textbooks and theoretical examples, making it difficult for students to see how these concepts apply in their daily lives. I was inspired by the idea that learning could become more engaging if students could simply point their camera at an object and instantly discover the STEM principles behind it. Whether it's a bicycle, a bridge, a solar panel, or even a water bottle, every object around us can become a learning opportunity. This inspired me to build STEMLens AI. What It Does STEMLens AI is an AI-powered educational platform that transforms everyday objects into interactive STEM lessons. A user uploads or captures an image of an object, and the application uses computer vision and artificial intelligence to: Identify the object Extract relevant STEM concepts Generate personalized explanations Create interactive quizzes Provide real-world applications of the concepts For example, if a student uploads an image of a bicycle, STEMLens AI can explain concepts such as momentum, friction, energy transfer, gear systems, and mechanical advantage while also generating assessment questions to reinforce learning. How I Built It I built STEMLens AI as a full-stack web application using modern web technologies. Frontend Next.js TypeScript Tailwind CSS Shadcn/UI Backend Next.js API Routes Artificial Intelligence Google Gemini API Gemini Vision for image recognition and analysis Database & Authentication Firebase Firestore Firebase Authentication The workflow is straightforward: A user uploads an image. Gemini Vision analyzes the image and identifies the object. AI generates STEM concepts related to the object. The platform creates detailed educational explanations. A quiz is generated automatically to test understanding. User progress and learning history are stored for future reference. Challenges I Faced One of the biggest challenges was designing a system that could accurately connect a wide variety of real-world objects to meaningful STEM concepts. Simply identifying an object was not enough; the platform needed to explain why that object was relevant from a scientific, mathematical, or engineering perspective. Another challenge was generating structured AI responses that could be consistently displayed in the application. To solve this, I engineered prompts that forced the AI to return organized JSON data, making it easier to generate lessons and quizzes dynamically. Ensuring a responsive and intuitive user experience across different devices was also important. I spent time refining layouts and interfaces to make the platform accessible on both mobile and desktop devices. What I Learned Through this project, I gained deeper experience in: AI-powered application development Computer vision integration Prompt engineering Full-stack web development Responsive UI/UX design Firebase authentication and database management I also learned the importance of designing technology around real educational challenges rather than simply building AI features for their own sake. Future Improvements In the future, I would like to expand STEMLens AI by adding: Interactive STEM simulations Voice-based learning assistance Multiple language support Teacher dashboards Personalized learning paths Offline functionality for low-connectivity environments Augmented Reality (AR) STEM experiences Impact STEMLens AI makes STEM education more practical, engaging, and accessible by helping students learn directly from the world around them. Instead of memorizing concepts from textbooks, learners can discover science, technology, engineering, and mathematics through everyday experiences. My goal is to make STEM learning more interactive, inclusive, and enjoyable for students everywhere. <div