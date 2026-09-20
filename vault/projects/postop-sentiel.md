---
slug: "postop-sentiel"
url: "https://devpost.com/software/postop-sentiel"
title: "PostOp Sentiel"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 579
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# PostOp Sentiel

> PostOp Sentinel: AI-powered recovery monitoring that catches complications before they become emergencies.

[Devpost](https://devpost.com/software/postop-sentiel) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]] [[security_privacy]]
**user** [[patient_family]]
**substrate** [[medical_record]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** amazon-rds-relational-database-service, amazon-web-services, fastapi, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for postop sentinel

## Body

Patient chat screen PostOp Sentinel AI-powered post-surgery monitoring that detects complications early and protects patients recovering at home. Inspiration Post-operative recovery is one of the most vulnerable phases of patient care. Every year, over 310 million surgeries are performed globally, yet studies show up to 25% of patients experience complications. Many of these issues—such as infection, fever, or abnormal bleeding—emerge only after discharge when continuous clinical monitoring is no longer available. Furthermore, the World Health Organization highlights a critical global shortage of healthcare workers. We were inspired to bridge this gap by building PostOp Sentinel , an intelligent "digital guardian" that extends hospital-level oversight into the home, ensuring symptoms are caught before they escalate into emergencies. What it does PostOp Sentinel is an AI-powered recovery assistant that performs automated conversational check-ins with patients. Voice-Based Reporting: Patients can report symptoms hands-free, which is vital for those with limited mobility or pain. Multimodal Analysis: The system analyzes text descriptions and photos of surgical wounds to identify redness, swelling, or discharge. Early Detection & Escalation: Using advanced reasoning, it identifies high-risk patterns and triggers intelligent alerts for healthcare providers. Accessible Interaction: By turning clinical forms into natural conversations, it improves patient compliance and data accuracy. How we built it The platform is designed for real-time interaction and high-speed reasoning: The AI Core (Amazon Nova): Amazon Nova 2 Sonic: Powers the speech-to-speech conversational engine, allowing for low-latency, natural voice dialogue. Amazon Nova 2 Lite: Handles multimodal reasoning, processing wound images and text descriptions to identify clinical risk signals. Backend: Built with FastAPI to manage patient scheduling and model orchestration. Real-Time Streaming: We utilized Server-Sent Events (SSE) to ensure the AI's responses feel fluid and instantaneous. Frontend: A clean, accessible web interface (React) designed for patients who may be fatigued or recovering. Challenges we ran into The Frequency Balance: We struggled to find the "sweet spot" for check-ins—frequent enough to catch complications, but not so often that they became a nuisance to a recovering patient. Accomplishments that we're proud of Successful Multimodal Integration: We are proud of how seamlessly the system switches between analyzing a patient's voice and evaluating a physical image of a surgical site. Accessible Design: Creating a tool that feels supportive and "human" rather than clinical, making it easier for elderly or high-pain patients to use. Leveraging Nova: Successfully implementing the Amazon Nova portfolio to create a sophisticated, agentic AI that feels like a proactive member of a care team. What we learned Voice is the UI of Healthcare: We learned that for recovering patients, typing is a barrier. Voice interaction isn't just a "feature"; it's an accessibility requirement. The Power of Multimodal Insights: Text-only data misses the "visual truth" of a wound. Multimodal AI provides a much richer clinical picture. Agentic Efficiency: We discovered how autonomous monitoring agents can significantly reduce the manual workload for overstretched nursing staffs. What's next for PostOp Sentinel EHR Integration: Connecting directly with hospital Electronic Health Records to provide surgeons with a seamless dashboard of patient progress. Wearable Sync: Integrating data from smartwatches (heart rate, SpO2, and sleep patterns) to add objective biometric data to the AI's risk assessment. Predictive Risk Scoring: Developing models to predict which patients are at the highest risk of readmission before they even leave the hospital. Personalized Care Plans: Tailoring the AI's personality and check-in frequency based on the specific type of surgery performed. References: Global Surgery Statistics (The Lancet) Postoperative Complications (BMJ Open) WHO Health Workforce Fact Sheet <div