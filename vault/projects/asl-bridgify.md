---
slug: "asl-bridgify"
url: "https://devpost.com/software/asl-bridgify"
title: "ASL Bridgify"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 388
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# ASL Bridgify

> Our innovative platform for learning American Sign Language (ASL) aims to redefine education through real-time feedback, personalized learning paths, and comprehensive AI-driven modules.

[Devpost](https://devpost.com/software/asl-bridgify) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** faiss, flask, intel, intelai, ipex, langchain, lstms, mongodb, nextjs, openai, poseestimation, python, rag, randomforests

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomphishments we are proud of

## Body

Seaching Feature AI Chatbot Quiz AI word-to-text AI sign-to-letter Inspiration We created ASL Bridgify to address the need for an interactive real time pose-estimation based learning model for ASL. In a post-pandemic world, we foresee that working from home and more remote experiences signals the need to communicate with individuals with hearing disabilities. It is a feature that is missing from various video conferencing, learning, and entertainment - based platforms. Shockingly, Duolingo the number 1 language learning platform does not teach ASL. What it does ASLBridgify is an educational platform that specifically focuses on the learning of ASL. We provide comprehensive modules that help you learn languages in scientifically proven ways. We provide easy to follow UI and personalized AI assistance in your learning journey. We realize that the future of AI comes in more than chatbot form, so our AI models are integrated within video to track hand-movement using Media pipe and TensorFlow. How we built it We created an educational platform by leveraging many technologies. Our frontend uses Next.js, Tailwind and Supabase. Our backend used Python libraries such as PyTorch, TensorFlow, and Keras to train our LLMs with the use of Intel Developer Cloud GPU and CPU to expedite the training. We connected the Frontend with the Backend with Flask. Moreover, we combined our trained models with Google Search API OpenAI API for Retrival-Augemented-Generation (RAG) Challenges we ran into The biggest challenge was time. The time it took to train one Large Language Model, even when using Intel Developer Cloud GPU capabilities was immense. It was a roadblock because we couldn't test any other code on one computer until the LLM was done training. Initially we tried to preprocess both words and sentences using hand pose to map ASL and using encoder decoder architecture, but we were not able to complete this because of the time constraint. ASL sentences is something we want to incorporate in the future. Accomphishments we are proud of We successfully trained preliminary large language models using PyTorch GPUs on the Intel Cloud from scratch. We're thrilled to integrate this accomplishment into our frontend. Through implementing three AI tools—each using different methods such as calling an API and building with IPEX—we've gained valuable insights into AI. Our excitement grows as we introduce our one-of-a-kind educational platform for ASL to the world. <div