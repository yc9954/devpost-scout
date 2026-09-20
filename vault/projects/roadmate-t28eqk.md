---
slug: "roadmate-t28eqk"
url: "https://devpost.com/software/roadmate-t28eqk"
title: "RoadMate"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 1026
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/government_staff"
  - "substrate/video_visual"
---

# RoadMate

> Intelligent driving companion that keeps you alert and safe by monitoring drowsiness, engaging you in personalized conversations, and automatically notifying loved ones when you're on the road

[Devpost](https://devpost.com/software/roadmate-t28eqk) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[security_privacy]] [[transportation]]
**user** [[frontline_worker]] [[government_staff]]
**substrate** [[video_visual]]

**stack** clerk, elevenlabs, fastapi, gemini, lovable, next.js, posthog, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Speak to Road Mate, a conversational AI agent Customizable topics and contacts list Personal accident from sleep deprivation #2 Personal accident from sleep deprivation #1 Facial and Road Analysis for Context Generating RoadMate Architect Inspiration Every year, drowsy driving causes over 100,000 crashes globally, claiming 10,000-30,000 lives - a silent epidemic that strikes without warning. In the age of long commutes and late-night drives, we're all vulnerable to those dangerous moments when our eyes get heavy and our focus drifts. Despite modern vehicles having dozens of sensors and safety features, they can't meaningfully engage with the driver or understand the subtle signs of fatigue that precede an accident. Our inspiration came from a personal experience: A friend of ours dozed off and totaled his car a couple of weeks ago, fortunately he was unscathed. We realized that existing solutions - like basic alarm systems or periodic alerts - are not enough to address the core problem. Drivers need an intelligent companion that can actively monitor, engage, and intervene before fatigue becomes fatal. Road Mate AI transforms your smartphone into an intelligent co-pilot that combines computer vision, conversational AI, and real-time monitoring to create a comprehensive safety system. By engaging drivers in natural conversation about their interests, monitoring facial cues for signs of drowsiness, and maintaining a connection with loved ones, we're not just building another safety app - we're reimagining the relationship between drivers and their vehicles. What it does Road Mate AI is an intelligent driving safety platform that prevents accidents from drowsy driving and keeps you connected to loved ones. Our intelligent model features 4 main components: Real-time drowsiness detection using dual-camera streams to analyze facial cues, instantly detecting signs of fatigue, and road conditions for enhanced driver safety monitoring and accident prevention. An AI conversation companion powered by ElevenLabs that adapts its conversation based on your alertness level - from casual chat about your interests to urgent wake-up calls Automated emergency contact system that sends location updates and alerts to designated contacts A personalization dashboard where users can customize their safety preferences, favorite conversation topics, and emergency contacts How we built it Our tech stack combines modern tools for a robust, scalable solution: Frontend: The UI is built with Next.js 13+ and TypeScript, paired with Tailwind CSS for a sleek, responsive design Authentication is built with Clerk for quick and secure implementation Real-time video processing using browser's Media API for dual camera streams ShadCN UI components for consistent, accessible interface elements We used lovable as a starting base template prompting it to create our interface and it designed a clean and modern look for our application. Backend: FastAPI powers our real-time video analysis server Gemini Vision AI for frame-by-frame analysis of both driver and road conditions Python's deque data structure maintains efficient context history PostHog for comprehensive LLM observability and performance tracking AI Processing: ElevenLabs Voice AI for natural conversation and alerts Prompts for specialized detection: Driver monitoring: Alertness levels, eye patterns, head position Road conditions: Hazards, lane position, traffic patterns Context-aware response system that adapts to driver state Mobile Development: Initially built in React Native for native performance Pivoted to mobile-optimized Next.js web app Responsive design works across all devices Progressive Web App capabilities for offline use Challenges we ran into Voice AI Integration Adapting ElevenLabs conversational widget for React Native environment Creating seamless voice interactions that wouldn't distract drivers Implementing context-aware responses based on real-time analysis Managing different states of conversation based on alertness levels User Experience Design Designing an interface that's safe to interact with while driving Finding the right balance between alerts and conversations Creating clear, non-distracting visual feedback for safety status Ensuring the app remains reliable in areas with poor connectivity Technical Integration Adding custom tool calls to ElevenLabs bot for emergency contacts Managing state between video analysis and voice interaction Implementing efficient error handling across multiple APIs Ensuring cross-platform compatibility for different mobile devices Accomplishments that we're proud of Created a fully functional driver safety system in 36 hours that processes both driver and road conditions in real-time Successfully integrated voice AI that can maintain engaging conversations while monitoring driver safety Built a scalable architecture that can handle multiple video streams with minimal latency Achieved seamless integration between video analysis and conversational AI Developed an intuitive interface that doesn't distract drivers while providing critical safety information Implemented robust emergency protocols that can alert contacts in critical situations What we learned Advanced video processing techniques for handling multiple streams Real-time data synchronization between visual analysis and voice interactions The complexities of building AI systems that need to make safety-critical decisions The importance of user experience in safety applications Integration patterns for multiple AI services (Gemini Vision, ElevenLabs) How to optimize performance when dealing with multiple API rate limits The challenges of building applications that need to work reliably in various driving conditions What's next for RoadMate Enhanced Safety Features Integration with car entertainment systems Advanced prediction models for early drowsiness detection Multi-language support for international drivers Customizable alert thresholds based on driving patterns Expanded AI Capabilities Personalized conversation models based on driver preferences Enhanced road hazard detection Integration with traffic and weather APIs Behavioral pattern analysis for personalized safety recommendations Platform Growth Mobile app release for both iOS and Android Partnership with ride-sharing companies Integration with major navigation platforms Fleet management features for transportation companies Community Features Anonymous sharing of safety insights Driver safety scoring and recommendations Community-driven conversation topics Integration with family safety apps Team Members Anwar: Led the development of the dual-stream analysis system, implementing real-time processing of driver and road conditions. Architected the context generation pipeline using Gemini Vision AI and engineered the analysis dashboard. Managed deployment infrastructure and CI/CD pipelines across our stack. Integrated Posthog for monitoring. Russell: Spearheaded the development of our mobile-optimized web application using Next.js and Tailwind CSS. Integrated Clerk authentication system and established secure user management. Contributed to core system architecture decisions and implementation strategies. William: Engineered the ElevenLabs conversational AI integration, developing custom prompts and context-aware responses for driver interaction. Implemented the mobile interface components and developed the API layer for real-time context integration with the voice agent. <div