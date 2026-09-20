---
slug: "synapse-ai-powered-cognitive-retraining-platform"
url: "https://devpost.com/software/synapse-ai-powered-cognitive-retraining-platform"
title: "Synapse - AI Powered Cognitive Retraining Platform"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 715
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/general_public"
  - "user/researcher"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# Synapse - AI Powered Cognitive Retraining Platform

> Synapse is a revolutionary AI-driven cognitive training platform specifically designed for children with ADHD, autism spectrum disorder, and learning disabilities.

[Devpost](https://devpost.com/software/synapse-ai-powered-cognitive-retraining-platform) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[general_public]] [[researcher]]
**substrate** [[regulation_legal_text]] [[structured_db]]

**stack** deepface, esp32, fastapi, ipfs-(interplanetary-file-system), javascript-/-typescript, kaggle, langchain, langgraph, nextjs, node.js, openai-whisper-v3, pyannote.audio, python, python-lsl-(lab-streaming-layer)

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for synapse – ai powered cognitive retraining platform

## Body

system architecture part 1 system architecture part 2 Synapse: Comprehensive AI-Powered Cognitive Retraining Platform for Children with Disabilities Watch Video Demo Inspiration Access to professional cognitive therapy for children with ADHD, autism spectrum disorder, and learning disabilities is severely limited, especially in underserved and rural areas. Families often lack affordable, accessible, and personalized support tools to help their children develop memory, focus, problem-solving, and emotional regulation skills. Inspired by this critical gap, Synapse aims to leverage artificial intelligence, neurotechnology, and gamification to create an adaptive, home-based cognitive retraining platform that empowers children, supports parents, and facilitates therapist collaboration. What it Does Synapse delivers personalized cognitive training through daily gamified sessions that adaptively evolve based on real-time monitoring of the child’s brain activity, emotional state, and engagement. The platform combines: EEG-enabled neurofeedback to objectively measure attention and cognitive load. AI-driven adaptive exercise engine targeting memory, focus, problem-solving, and behavioral skills. Multi-modal emotion and speech recognition to assess engagement and tailor interactions. Personalized rewards and comics based on the child’s preferences and progress. Parental dashboards with WhatsApp report delivery for convenient progress tracking and guidance. Therapist portals offering rich longitudinal and multi-modal clinical insights for remote professional oversight. Secure decentralized data storage ensuring privacy and ownership. How We Built It Utilized ESP32-based EEG devices streaming brain signals via Python LSL protocols. Integrated SARVAM AI for multilingual speech-to-text and text-to-speech abilities. Implemented DeepFace for facial emotion analysis and OpenAI Whisper-v3 for speech emotion recognition . Developed a columnar database infrastructure to support fast, scalable real-time analytics. Built adaptive game modules focusing on critical cognitive domains. Automated report generation stored on IPFS and pushed via Twilio WhatsApp API . Leveraged pyannote speaker diarization to analyze conversational dynamics during sessions. Designed accessible, multi-language, and gamified user experiences. Challenges We Ran Into Ensuring accuracy and reliability of EEG data within affordable consumer-grade hardware constraints. Seamless integration of multiple AI models (speech, emotion, EEG) to form cohesive, real-time actionable insights. Handling large multi-modal data streams with low latency using a scalable database and streaming architecture. Designing an adaptive exercise engine that personalizes difficulty without overwhelming or boring children. Maintaining privacy and security while supporting decentralized data storage and peer-to-peer sharing. Developing interfaces and voice interactions accessible to children with diverse cognitive and sensory needs. Educating families and therapists to effectively leverage complex data-driven feedback. Balancing high tech with intuitive, warm, and supportive user experience. Accomplishments We're Proud Of Creation of a truly adaptive, neurofeedback-enabled gamified cognitive training system personalized in real time. Integration of real-time facial and speech emotion recognition alongside EEG data for richer engagement analytics. Deployment of secure, decentralized data storage via IPFS coupled with instant WhatsApp report delivery for unparalleled parental access. Development of multi-stakeholder collaboration tools linking children, families, and therapists around shared data and care goals. Designing personalized AI-generated kids’ comics that incorporate hobbies, learning progress, and emotional states. Building a multi-language, accessibility-first platform adaptable to diverse cultural and linguistic contexts. What We Learned Real-time multimodal monitoring significantly improves personalization and engagement. Low-cost EEG devices can provide clinically meaningful insights when combined with robust AI. Seamless and direct parent communication is critical for retention and motivation. Therapist involvement enriches outcomes and validates home-based interventions. Gamification boosts adherence, but must be carefully balanced with therapeutic objectives. Accessibility and cultural sensitivity are non-negotiable in building inclusive digital health tools. Cross-disciplinary collaboration between AI specialists, neuroscientists, clinicians, and educators is vital. Successfully implementing decentralized storage requires thoughtful user education and backup policies. What's Next for Synapse – AI Powered Cognitive Retraining Platform Further refining the adaptive algorithms using longitudinal clinical data and deep learning. Expanding multilingual support to include more Indian and global languages. Introducing teletherapy integration for video-based therapist interactions within the platform. Enhancing the personalized comics engine with interactive, story-driven gamified tasks. Improving offline usability and data synchronization to expand access in low-connectivity areas. Deploying edge AI solutions for real-time local processing on devices. Launching a large-scale clinical validation study with partner institutions. Offering an SDK/API to enable integration with other health tech ecosystems. Synapse connects minds, builds futures, and transforms cognitive care—one child at a time. Tags AI Cognitive Training, ADHD, Autism, Learning Disabilities, Neurofeedback, Gamification, Adaptive Learning, EEG, Speech Emotion Recognition, Pediatric Therapy, Parent Support, Therapist Dashboard, Decentralized Data, Accessibility, Multilingual, Personalized Comics, Digital Therapeutics <div