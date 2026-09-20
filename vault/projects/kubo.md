---
slug: "kubo"
url: "https://devpost.com/software/kubo"
title: "KUBO"
hackathon: "Red Hat and Intel AI Hackathon"
organization: "Red Hat"
winner: true
words: 735
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# KUBO

> Versatile AI companion - Empowering lifelike assistance

[Devpost](https://devpost.com/software/kubo) · hackathon [[Red Hat and Intel AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** langchain, llamacpp, node.js, openvino, python, react.js, three.js, whispercpp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for kubo

## Body

Custom trained int8 openvino YOLO model MeloTTS with openvino WhisperASR with OPENVINO llamacpp running with AMX instructions OVMS serving Inspiration Recently, I struggled with my PC’s Wi-Fi, going through days of trial and error—searching forums, downloading drivers, and engaging in long chats with support agents who could only offer standard troubleshooting tips. Finally, I stumbled upon a manual PDF specific to my motherboard model, revealing a unique driver that wasn’t mentioned anywhere else. This sparked an idea: What if AI could be trained to recognize unique product models and offer tailored guidance, and better, if it could emulate the effortless way humans identify and solve problems? Meet KUBO, a customizable AI companion that could adapt to any role from personalized study buddy to customer support agent , bringing specific, model-based expertise into a user-friendly intelligent support. Through real-time video, KUBO enables users to interact naturally—showing, talking, and guiding—providing the feeling of in-person assistance from anywhere. What it does This is trained as a customer support agent. User Interaction : Conversational Real-Time Assistance Offers dynamic, interactive support with video-based consultations, creating a seamless and engaging experience for users across various scenarios, from learning to troubleshooting. Object Recognition & Contextual Understanding Identifies objects or situations visually, interprets their context, and delivers accurate and personalized responses, eliminating the need for extensive input from users. User Management & Secure Interaction Supports user authentication and profiles, enabling tailored interactions while maintaining security and privacy. Personalized Recommendations Analyzes user behavior and preferences to suggest relevant options, whether it’s learning resources, tasks, or decision-making aids. Administrative and Management Features : Customizable AI Allows administrators to configure the AI avatar’s personality as well as AI model configuration. Knowledge Database Management Facilitates the creation and maintenance of a centralized knowledge base, covering manuals, documents, multimedia files, user guides, or other resources that the AI can draw upon for context-aware responses. Dashboard & Performance Analytics Provides detailed insights into interactions, success rates, feedback, and usage patterns to continuously refine the experience and optimize outcomes for users. How we built it Frontend Development : Utilized React for dynamic and responsive user interface and Three.js to manipulate a realistic, interactive avatar that enhances the virtual in-store experience. Backend Infrastructure : Built a robust backend server with Node.js and Express to handle requests, manage sessions, and serve data to the frontend. Integrated MongoDB for data and vector storage, allowing efficient retrieval of information. AI and Model Integration : Leveraged Red Hat OpenShift AI’s OpenVINO Model Server (OVMS) with LLM capabilities (using Llama Index and LangChain) to handle natural language understanding, content generation, and advanced conversational flows. Deployed a containerized model mesh setup that includes specialized models: Speech-to-Text , Text-to-Speech, Object Recognition, Lip-Sync Model Developed inference code in Python to enable real-time processing across all AI models within the model mesh setup. Data Retrieval and Contextual Understanding : Retrieval-Augmented Generation (RAG) to access the company’s knowledge base and contextual data, ensuring responses are accurate and relevant. Resources used Silero VAD for precise voice activity detection run on web browser with onnx runtime Lip sync was trained with rhubarb library Whisper.cpp with OpenVINO support for voice understanding capabilities Binary vector embeddings with the all-MiniLM-L6-v2 model for remembering conversations MeloTTS for speech- OpenVINO, YOLO model with INT 8 for optimization Challenges we ran into Integration of Diverse opensource AI Models Ensuring seamless collaboration between different AI models with distinct functionalities was complex and required extensive optimization. Performance Bottlenecks Initial reliance on external models caused delays in response times. To address this, a custom model was trained, significantly improving speed and efficiency. Advanced Morph Targets and Animation Development Creating lifelike animations and precise morph targets for avatars was a technical challenge, requiring a deep understanding of animation techniques and iterative refinement to achieve natural, responsive behavior. Camera Integration and Object Recognition Integrating real-time camera input and training AI to accurately recognize objects and link them to relevant data for efficient, context-aware responses. What's next for KUBO Emotion and Sentiment Analysis : Incorporate sentiment analysis to detect user frustration or confusion, adapting responses for improved user experience. Design own Avatar : Allow users to create fully customizable avatars, choose personality traits and a variety of voice profiles and accents. Multilingual Interaction : Add support for multilingual voice processing to cater to a global audience Enhanced Facial Expressions and Realistic Animations : Improve KUBO’s facial animations and micro-expressions for more lifelike, engaging interactions <div