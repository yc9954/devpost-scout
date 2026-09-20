---
slug: "edumentor-ai-1snvq8"
url: "https://devpost.com/software/edumentor-ai-1snvq8"
title: "EduMentor AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 593
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# EduMentor AI

> An AI educator here to change the game

[Devpost](https://devpost.com/software/edumentor-ai-1snvq8) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** amazon-web-services, aws-fargate, aws-sdk-automation:-n8n-databases:-postgresql, languages:-typescript, python, sql-frameworks:-next.js-(react), tailwind-css-ai-model:-amazon-nova-cloud-platforms:-aws-amplify, vercel-containerization:-docker-tools-&-sdks:-vercel-ai-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for edumentor ai

## Body

the welcome/dashboard page the chat area a working chat page Inspiration The vision for EduMentor AI Tutor was born from a simple observation: the "one-size-fits-all" approach to traditional education often leaves students behind. As a BSc Information Technology student, I saw a unique opportunity to bridge this gap using the Amazon Nova model. My goal was to create a mentor that doesn't just provide answers, but understands a student's specific learning pace and style, essentially democratizing private tutoring through scalable AI. What it does EduMentor AI Tutor is a personalized, AI-driven educational platform designed to act as a 24/7 private tutor for students. Unlike standard chatbots that simply provide answers, EduMentor utilizes Amazon Nova to employ Socratic teaching methods, guiding students through complex concepts by asking probing questions and providing incremental hints. How we built it The architecture was designed to be modular and scalable, focusing on a modern web stack: Frontend: Developed using Next.js to provide a fast, responsive interface for students. AI Orchestration: Integrated Amazon Nova via the AWS SDK. I used Vercel for initial prototyping due to its excellent streaming support. Containerization: To ensure consistency between my local environment and the cloud, I used Docker. This allowed me to package the application logic and dependencies into a single image. Deployment: I utilized AWS Amplify to host the application, taking advantage of its CI/CD pipelines to automate updates whenever I pushed code to my repository. Challenges we ran into Cold Starts & Latency: Initially, the AI responses felt sluggish. I had to optimize my Docker images to be as lightweight as possible to reduce deployment times and improve execution speed. Token Management: Managing the cost and context window of the Amazon Nova model required strict logic to ensure the "tutor" didn't lose track of the conversation during long study sessions. Environment Parity: I faced several "it works on my machine" moments when deploying to AWS. This was the primary reason I pivoted to a Docker-first workflow, which resolved the dependency conflicts between my local OS and the AWS Lambda/Fargate environments. Accomplishments that we're proud of Seamless Amazon Nova Integration: Successfully implementing a low-latency streaming architecture using Vercel and AWS, ensuring that the AI’s "thought process" feels instantaneous to the student. Robust Containerization: Transitioning to a Docker-first workflow, which reduced our deployment errors by nearly 90% and ensured perfect environment parity. User-Centric Design: Creating an interface that prioritizes focus and minimizes cognitive load, a core principle we applied from our studies in Human-Computer Interaction (HCI). What we learned This project was a masterclass in modern DevSecOps and Full-Stack AI development. We learned: Advanced Prompt Engineering: How to "guardrail" an LLM to prevent it from simply doing a student's homework, forcing it instead to facilitate active recall. Cloud Architecture Optimization: The nuances of deploying containerized applications on AWS Amplify and managing the trade-offs between serverless execution and persistent containers. Data Science Fundamentals: Implementing sales forecasting models and ticket classification systems during the project helped us understand how to structure the underlying data for the AI's "knowledge base." What's next for EduMentor AI The journey for EduMentor is just beginning. Our roadmap includes: Multimodal Capabilities: Integrating image recognition so students can snap a photo of a handwritten math problem or a biology diagram for instant explanation. Collaborative Study Rooms: Developing a feature where multiple students can interact with the same AI tutor in a shared virtual space. Deeper Blockchain Integration: Exploring the Sui blockchain to create a decentralized system for "Proof of Learning" credentials, allowing students to own their academic progress data securely. <div