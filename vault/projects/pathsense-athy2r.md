---
slug: "pathsense-athy2r"
url: "https://devpost.com/software/pathsense-athy2r"
title: "PathSense"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 982
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# PathSense

> Empowering Vision Through Voice. Revolutionizing indoor mobility with real-time, adaptive AI-enabled guidance for seamless navigation in complex spaces.

[Devpost](https://devpost.com/software/pathsense-athy2r) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** auth0, cohere, convex, detectron2, dpt, git, gpt-4, groq, javascript, json, jwt, kubernetes, mappedin, ngrok

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pathsense

## Body

route generated after a voiceflow convo Inspiration Our journey with PathSense began with a deeply personal connection. Several of us have visually impaired family members, and we've witnessed firsthand the challenges they face navigating indoor spaces. We realized that while outdoor navigation has seen remarkable advancements, indoor environments remained a complex puzzle for the visually impaired. This gap in assistive technology sparked our imagination. We saw an opportunity to harness the power of AI, computer vision, and indoor mapping to create a solution that could profoundly impact lives. We envisioned a tool that would act as a constant companion, providing real-time guidance and environmental awareness in complex indoor settings, ultimately enhancing independence and mobility for visually impaired individuals. What it does PathSense, our voice-centric indoor navigation assistant, is designed to be a game-changer for visually impaired individuals. At its heart, our system aims to enhance mobility and independence by providing accessible, spoken navigation guidance in indoor spaces. Our solution offers the following key features: Voice-Controlled Interaction: Hands-free operation through intuitive voice commands. Real-Time Object Detection: Continuous scanning and identification of objects and obstacles. Scene Description: Verbal descriptions of the surrounding environment to build mental maps. Precise Indoor Routing: Turn-by-turn navigation within buildings using indoor mapping technology. Contextual Information: Relevant details about nearby points of interest. Adaptive Guidance: Real-time updates based on user movement and environmental changes. What sets PathSense apart is its adaptive nature. Our system continuously updates its guidance based on the user's movement and any changes in the environment, ensuring real-time accuracy. This dynamic approach allows for a more natural and responsive navigation experience, adapting to the user's pace and preferences as they move through complex indoor spaces. How we built it In building PathSense, we embraced the challenge of integrating multiple cutting-edge technologies. Our solution is built on the following technological framework: Voice Interaction: Voiceflow Manages conversation flow Interprets user intents Generates appropriate responses Computer Vision Pipeline: Object Detection: Detectron Depth Estimation: DPT (Dense Prediction Transformer) Scene Analysis: GPT-4 Vision (mini) Data Management: Convex database Stores CV data and mapping information in JSON format Semantic Search: Cohere's Rerank API Performs semantic search on CV tags and mapping data Indoor Mapping: MappedIn SDK Provides floor plan information Generates routes Speech Processing: Speech-to-Text: Groq model (based on OpenAI's Whisper) Text-to-Speech: Unreal Engine Video Input: Multiple TAPO cameras Stream 1080p video of the environment over Wi-Fi To tie it all together, we leveraged Cohere's Rerank API for semantic search, allowing us to find the most relevant information based on user queries. For speech processing, we chose a Groq model based on OpenAI's Whisper for transcription, and Unreal Engine for speech synthesis, prioritizing low latency for real-time interaction. The result is a seamless, responsive system that processes visual information, understands user requests, and provides spoken guidance in real-time. Challenges we ran into Our journey in developing PathSense was not without its hurdles. One of our biggest challenges was integrating the various complex components of our system. Combining the computer vision pipeline, Voiceflow agent, and MappedIn SDK into a cohesive, real-time system required careful planning and countless hours of debugging. We often found ourselves navigating uncharted territory, pushing the boundaries of what these technologies could do when working in concert. Another significant challenge was balancing the diverse skills and experience levels within our team. While our diversity brought valuable perspectives, it also required us to be intentional about task allocation and communication. We had to step out of our comfort zones, often learning new technologies on the fly. This steep learning curve, coupled with the pressure of working on parallel streams while ensuring all components meshed seamlessly, tested our problem-solving skills and teamwork to the limit. Accomplishments that we're proud of Looking back at our journey, we're filled with a sense of pride and accomplishment. Perhaps our greatest achievement is creating an application with genuine, life-changing potential. Knowing that PathSense could significantly improve the lives of visually impaired individuals, including our own family members, gives our work profound meaning. We're also incredibly proud of the technical feat we've accomplished. Successfully integrating numerous complex technologies - from AI and computer vision to voice processing - into a functional system within a short timeframe was no small task. Our ability to move from concept to a working prototype that demonstrates the real-world potential of AI-driven indoor navigation assistance is a testament to our team's creativity, technical skill, and determination. What we learned Our work on PathSense has been an incredible learning experience. We've gained invaluable insights into the power of interdisciplinary collaboration, seeing firsthand how diverse skills and perspectives can come together to tackle complex problems. The process taught us the importance of rapid prototyping and iterative development, especially in a high-pressure environment like a hackathon. Perhaps most importantly, we've learned the critical importance of user-centric design in developing assistive technology. Keeping the needs and experiences of visually impaired individuals at the forefront of our design and development process not only guided our technical decisions but also gave us a deeper appreciation for the impact technology can have on people's lives. What's next for PathSense As we look to the future of PathSense, we're brimming with ideas for enhancements and expansions. We're eager to partner with more venues to increase our coverage of mapped indoor spaces, making PathSense useful in a wider range of locations. We also plan to refine our object recognition capabilities, implement personalized user profiles, and explore integration with wearable devices for an even more seamless experience. In the long term, we envision PathSense evolving into a comprehensive indoor navigation ecosystem. This includes developing community features for crowd-sourced updates, integrating augmented reality capabilities to assist sighted companions, and collaborating with smart building systems for ultra-precise indoor positioning. With each step forward, our goal remains constant: to continually improve PathSense's ability to provide independence and confidence to visually impaired individuals navigating indoor spaces. <div