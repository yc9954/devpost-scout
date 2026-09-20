---
slug: "icu-2egdxy"
url: "https://devpost.com/software/icu-2egdxy"
title: "ICU"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 969
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "user/patient_family"
  - "substrate/video_visual"
---

# ICU

> Extra eyes for those who need them the most. With hand gestures or voice commands, ICU's servo-powered camera rotates, analyzes the environment, and describes surroundings for the visually impaired.

[Devpost](https://devpost.com/software/icu-2egdxy) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[elder_child_care]]
**user** [[patient_family]]
**substrate** [[video_visual]]

**stack** ambition, arduino, c++, elliott, esp-32, gemini, gpt, iphone13-promax, mediapipe, openai, opencv, pen, python, redbull

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for icu

## Body

Inspiration Katie's grandfather has been battling diabetic retinopathy (vision loss due to diabetes) for the past 5 years. He's been struggling more and more with everyday tasks like finding his medication, identifying what's on the dinner table, or checking if he left the stove on. He's constantly asking how new tech can help him stay independent of his caregivers -- why not make it a reality? #fathersday Her grandfather expressed that existing solutions for visually impaired people remain too focused on text-to-speech instead of environmental awareness. This isn't very helpful. This capability gap forces many to choose between constant dependence on others or navigating with incomplete information about their surroundings. ICU addresses this challenge directly by combining voice commands with gesture controls to provide real-time environmental context without requiring technical expertise. It's not just her grandfather who needs this; vision impairment affects approximately 2.2 billion people worldwide. What it does ICU acts as an intelligent pair of eyes, allowing users to request specific insights about their surroundings using natural voice or hand commands. The system dynamically adjusts a camera based on voice input or the direction a user points toward, streaming visuals to advanced AI models (Gemini and local Mediapipe landmark extraction) to analyze the environment and give precise, contextual feedback. It also speaks back to the user as if it's a human assistant, making it more natural to use. This approach enables visually impaired individuals, like elderly users with age-related vision decline, to independently identify objects, verify safety conditions, and maintain awareness of their surroundings. Extending beyond just convenience, ICU's functions preserve dignity, reduce dependence, and enabled continued participation in daily activities that most take for granted. How we built it We integrated a voice agent interface for two-way natural conversations and commands. Cameras are strategically placed: one dynamically moves based on voice instructions interpreted by OpenAI Whisper, and another is fixed on the user, extracting hand landmarks using Mediapipe. Our local ML model runs efficiently on laptops, processing video streams sent from phones. Data and signals are exchanged seamlessly via WebSockets between microservices that manage analysis, logic, and user interactions. AI-driven inference is handled by Gemini, which receives visual streams to deliver insights. Challenges we ran into Managing real-time streaming with low latency was initially tough, especially maintaining smooth WebSocket communication between multiple devices and services. The ML pipeline was another challenge. We had Mediapipe running for hand tracking and Gemini for visual analysis, and we had to make them work harmoniously. The most surprising challenge came with the hand tracking. Translating a pointing gesture into actual camera movement directions required accurate inverse kinematics to translate hand landmarks into meaningful directional data. We spent hours fine-tuning our inverse kinematics algorithms because the initial versions would misinterpret slight hand tremors (common in elderly users) as intentional movements. We also wanted to make this project different from other visually-impaired assistance projects, which are quite common but often not very practical. It was initially a struggle to ideate beyond basic screen readers or OCR tools. We knew we wanted something that could actually describe what's happening in a room, and that required solving a completely different set of technical problems that few hackathon projects attempt to tackle. Accomplishments that we're proud of Successfully integrating multiple complex components (real-time voice commands, dynamic camera movements, and ML-driven analysis) into a cohesive, user-friendly solution was incredibly rewarding. We also achieved near-real-time responsiveness, ensuring the technology could provide practical assistance without noticeable lag. The moment our first end-to-end test worked was super rewarding, and we immediately sent progress videos to Katie's grandfather, whose excitement seeing the prototype validated our approach. We're now excited for Katie's grandfather to test the system in person next month. What we learned We learned valuable lessons in real-time data streaming, model integration, and handling asynchronous tasks efficiently. Working with WebSockets taught us how to maintain persistent connections across devices while minimizing latency, which is critical for a responsive assistive technology. We discovered that implementing buffer management and proper error handling significantly improved reliability when network conditions fluctuated. The challenge of coordinating multiple ML models forced us to develop a more sophisticated understanding of resource allocation and parallel processing workflows. Our team strengthened our skills in integrating cloud-based AI models with local ML processing, finding the right balance between offloading complex inference tasks to more powerful cloud services while keeping latency-sensitive operations like gesture tracking running locally. Finally, we gained practical experience in designing intuitive user interactions for individuals with visual impairments. We learned that responsiveness and consistent feedback were even more crucial than technical sophistication. What's next for ICU Looking ahead, we plan to miniaturize and optimize the system for portability, aiming to run entirely on mobile devices or compact wearables. We're specifically exploring the Raspberry Pi Zero 2 W paired with a lightweight camera module that could reduce the current setup's footprint by 70% while maintaining core functionality. Enhanced ML models for better accuracy and expanded environmental context are also on our roadmap, particularly focusing on improved object recognition in low-light conditions, a common challenge identified during our testing. We're developing a more comprehensive ontology of household objects with specialized detection for medication bottles, appliance states, and potential hazards. Next month, we'll conduct our first extended user test when Katie's grandfather tries the system in his home. We are looking for his feedback regarding voice command natural language processing and the sensitivity of gesture controls. We're also exploring integration with smart home systems to enable ICU to not just identify but interact with the environment (e.g., "turn off the stove" after detecting it was left on). Ultimately, we envision ICU becoming an essential tool for those needing intuitive, accessible, and immediate assistance, with a particular focus on creating affordable deployment options for individuals with limited financial resources. <div