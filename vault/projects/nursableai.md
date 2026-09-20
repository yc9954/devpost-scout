---
slug: "nursableai"
url: "https://devpost.com/software/nursableai"
title: "NursableAI"
hackathon: "Predictive AI In Healthcare with FHIR®"
organization: "Darena Solutions"
winner: true
words: 718
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# NursableAI

> NursableAI is an AI-powered triage robot that uses face recognition, autonomous navigation, and real-time decisions to streamline patient intake, reduce wait times, and integrate with healthcare syste

[Devpost](https://devpost.com/software/nursableai) · hackathon [[Predictive AI In Healthcare with FHIR-]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]]
**user** [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** arduino, cpp, gpus, javascript, ollama, python, pytorch, ros2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nursableai
- updates v1.1

## Body

v1.1 Robot Finished Inspiration The inspiration behind NursableAI came from the need to streamline the triage process in healthcare environments. As healthcare systems face growing demand and overwhelmed medical staff, an AI-powered solution could reduce wait times and ensure more accurate patient assessments. The goal was to create a robot that could autonomously identify patients, assess their condition, and securely transmit the data to healthcare providers, all while improving the patient experience. What it does NursableAI is a triage robot that uses face recognition to identify patients, depth cameras and image segmentation for autonomous navigation, and AI-powered triage via Ollama. It gathers patient information by asking real-time questions, generating medical summaries, and creating FHIR-compliant documents for encounters, conditions, and diagnostic reports. These reports are then posted to MeldRx for seamless integration with existing healthcare systems. How we built it We built NursableAI using a combination of hardware and software technologies: Hardware: The robot uses depth cameras and sensors for navigation, while the face recognition system helps identify patients. We integrated this with motors and controllers for autonomous movement. Software: We leveraged Ollama for the AI-driven triage and used YOLO for real-time image segmentation. We also ensured the system generates structured FHIR documents, following industry standards for healthcare data exchange. Integration: The system integrates directly with MeldRx to upload triage data and ensures real-time availability to healthcare providers. Videos for the robot building process for this competition: How to Build a medical Robot Part1 How to Build a medical Robot Part2 Challenges we ran into Autonomous Navigation: Ensuring precise and safe navigation in busy environments was one of the main challenges. We had to fine-tune the robot’s ability to recognize and navigate around obstacles without human intervention. Real-Time Data Processing: Generating accurate FHIR-compliant documents in real-time required handling complex data processing while maintaining performance. Face Recognition Accuracy: Ensuring that face recognition worked reliably in varying lighting conditions and with diverse patient demographics was a challenge. Accomplishments that we're proud of Seamless Integration: The robot’s integration with MeldRx has been smooth, providing real-time access to triage data for healthcare providers. Autonomous Navigation: Successfully implementing the robot’s ability to navigate autonomously in dynamic environments without collisions. AI-Powered Triage: The conversational AI powered by Ollama is performing well, offering accurate and personalized assessments that improve the triage process. What we learned Iterative Development: We learned that building an autonomous system requires continuous refinement and testing. Small adjustments to the AI and navigation systems can have a big impact on performance. Data Interoperability: Integrating healthcare data systems (like FHIR and MeldRx) requires understanding both the technical aspects and regulatory requirements of data security and privacy. User Experience: We discovered how critical user experience is, especially when dealing with patients who may be anxious or in distress. Creating a smooth, empathetic interaction is as important as the technical functionality. What's next for NursableAI Enhanced Diagnostics: We plan to expand the AI’s capabilities to include diagnostic support, such as analyzing medical images or test results. Expanded Deployment: NursableAI’s deployment will extend beyond clinics and hospitals to other healthcare settings, like telemedicine, home care, and emergency services. Updates v1.1 NursableAI v1.1 Update What’s New in v1.1? With this update, NursableAI has taken a major step forward in both physical design and intelligence, making it more capable and user-friendly in real-world healthcare environments. Full Robot Body & Mobility 🦾 Custom-built robot body designed for better stability and patient interaction. Improved mobility system allowing smoother navigation in hospitals and clinics. Enhanced ergonomics for better approachability and accessibility in medical spaces. Vision System Enhancements 👀 Upgraded depth camera system for more accurate patient detection and navigation. Better image segmentation to recognize obstacles and identify patients in crowded areas. Face recognition improvements for faster and more reliable patient identification. AI Conversation & Triage Upgrades 🗣️ More natural and engaging conversations with enhanced language processing. Improved question adaptation to adjust based on patient responses. Emotion and tone recognition to better assess patient distress levels. Impact of v1.1 More human-like interaction improves patient trust and comfort. Greater accuracy in triage reduces errors in patient assessment. Better real-world adaptability for hospitals and clinics. This update brings NursableAI closer to being a fully functional AI-powered medical assistant, bridging the gap between robotics, AI, and real-world patient care. More upgrades are on the way! <div