---
slug: "iris-ovx582"
url: "https://devpost.com/software/iris-ovx582"
title: "Iris"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 533
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "substrate/video_visual"
---

# Iris

> provides real-time reality checking to combat hallucinations, AI chat support, and easy access to medical information for seamless digital assistance 24/7.

[Devpost](https://devpost.com/software/iris-ovx582) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[health_clinical]] [[mental_health]]
**substrate** [[video_visual]]

**stack** coffee, dart, flutter, git, llama, meta, nebius, qwen, tears

## How they structured the write-up

- inspiration
- features
- development process
- accomplishments
- lessons learned
- future plans

## Body

Landing page Home page Reality checker Chatbot Panic button for emergency contact alerts Resources Inspiration Iris was inspired by the need to provide immediate, accessible support for individuals experiencing reality distortion or hallucinations. The goal was to create a companion app that could help users distinguish between real and perceived experiences while offering immediate support and resources. Features 🎥 Reality Check Uses real-time camera feed and AI to help users verify their perceptions. Point the camera to check reality through AI-powered visual analysis. 💬 Support Chat AI-powered conversational interface for immediate emotional support. Real-time messaging with empathetic responses. 🏥 Medical Information Educational resources on mental health. Emergency contact access for crisis situations. 🚨 Emergency Alert System Add and manage emergency contacts. One-tap panic button to send immediate alerts. Automated SMS alerts via Twilio. Built using express and twilio to be pinged. Development Process How It Was Built Developed using Flutter for cross-platform compatibility. Integrated camera functionality using the camera package. Implemented AI analysis using Nebius AI's Qwen-VL model for visual processing. Used GetX for state management and dependency injection. Implemented Meta’s Llama model for support chat assistance. Designed a polished UI using Material Design with custom theming. Challenges Faced Switching from React Native to Flutter : React Native dependencies clashed, leading to a complete framework switch. Had to learn Dart from scratch as native development was unfamiliar. Camera Integration : Handling different device orientations and camera sensors. Converting YUV420 format into processable images. Optimizing frame processing to prevent performance issues. AI Integration : Managing API rate limits for real-time analysis. Balancing response time with accuracy. Handling API failures gracefully. UX Design : Ensuring accessibility during distressful moments. Maintaining app stability and responsiveness. Managing permissions and device capabilities across platforms. Model Integration : TensorFlow and TensorFlow Lite were outdated and incompatible. Finding an alternative solution took extensive research and time. Lost a week trying to make TensorFlow work, finishing the project in the last 5 hours. Accomplishments Last minute completion : finishing the project in the last 5 hours. Real-time Visual Analysis : Successfully implemented frame-by-frame AI-based analysis. Empathetic Chat Interface : Designed an engaging and supportive conversational experience. Cross-Platform Compatibility : Stable functionality on both iOS and Android. Performance Optimization : Achieved smooth camera preview and real-time processing. User-Centric Design : Ensured accessibility during moments of distress. First-Time Flutter Development : Completed the project within a tight deadline despite a framework switch. Lessons Learned Flutter! Tensorflow has not been updated for native or flutter yet :( Advanced Flutter camera integration . AI model implementation for both visual and text processing . Real-time image processing techniques . Effective state management using GetX. Considerations for cross-platform development . Importance of accessibility in mental health applications . Future Plans Enhanced Features Voice interaction for hands-free operation. Customizable reality check parameters . Integration with wearable devices for continuous monitoring. Community Features Optional trusted contact connections . Integration with local support services . Anonymous community support groups for shared experiences. Technical Improvements Advanced image processing capabilities . Multi-language support . Improved battery optimization . Enhanced security features . Clinical Integration Partnerships with mental health providers . Telehealth service integration. Symptom tracking and reporting features for medical professionals. <div