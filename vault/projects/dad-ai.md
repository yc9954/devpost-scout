---
slug: "dad-ai"
url: "https://devpost.com/software/dad-ai"
title: "Dad AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 381
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# Dad AI

> AI assistant that helps you fix your household items like a dad

[Devpost](https://devpost.com/software/dad-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools</sub>
**substrate** [[video_visual]]

**stack** amazon-dynamodb, amazon-nova, amazon-nova-multimodal-models, amazon-nova-sonic, amazon-web-services, aws-amplify, aws-cloudformation, aws-cognito, aws-lambda, aws-sam, aws-sdk, javascript, next.js-14, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i am proud of
- what we learned
- what's next for dad ai

## Body

Inspiration I wanted to explore how voice-first AI and visual understanding could work together in a single, practical assistant. Most AI tools treat voice, vision, and persistence as separate experiences. DadAi was inspired by the idea of a dependable assistant that can listen, see, reason, and retain context—closer to how a human assistant supports real-world needs. What it does DadAi is a full-stack multimodal AI application that enables real-time voice conversations, intelligent image analysis, and secure cloud-based data storage. I can speak to the assistant using natural voice, upload images for analysis, and have results automatically stored and associated with my account. How we built it I built DadAi using a serverless AWS architecture. The backend uses AWS Lambda (via SAM) with Python to handle image analysis and voice interactions. Amazon Nova Sonic powers real-time voice conversations, while Amazon Nova multimodal models handle image understanding. Images and analysis results are stored in S3, user data is managed in DynamoDB, and authentication is handled with Cognito. The frontend is a Next.js application using TypeScript, Tailwind CSS, and shadcn/ui, with AWS Amplify connecting the frontend to backend services. Challenges we ran into One of the main challenges was working with bidirectional audio streaming for real-time voice interaction. Handling simultaneous audio input and output requires careful coordination to maintain low latency and avoid interruptions or feedback loops. Managing streaming state, buffering, and synchronization between the browser, backend services, and the voice model added complexity, especially while ensuring a natural, conversational experience with consistent performance. Accomplishments that I am proud of I’m proud of delivering a fully working multimodal AI assistant that combines voice, vision, and cloud persistence in a cohesive experience. Successfully integrating real-time voice AI with image analysis and scalable AWS infrastructure demonstrated that Amazon Nova can be used in production-style applications. What we learned I learned how to design and deploy real-time, multimodal AI systems using Amazon Nova and AWS serverless services. I gained practical experience with voice streaming, multimodal reasoning, infrastructure-as-code, and building secure, scalable full-stack AI applications. What's next for Dad AI Next, I plan to add conversation history persistence, user preference management, and more advanced agent behaviors. I also want to improve contextual memory across sessions and explore additional real-world integrations to make DadAi more proactive and personalized. <div