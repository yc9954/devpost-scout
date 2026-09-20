---
slug: "furcavision-ai-powered-furcation-detection"
url: "https://devpost.com/software/furcavision-ai-powered-furcation-detection"
title: "FurcaVision - AI Powered Furcation Detection"
hackathon: "MEGA Hackathon 2025"
organization: "MegaHackathonLeague"
winner: true
words: 403
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# FurcaVision - AI Powered Furcation Detection

> Our AI-powered web app detects furcation defects and bone loss in dental X-rays, providing fast, accurate, and accessible analysis to support early diagnosis and better patient care.

[Devpost](https://devpost.com/software/furcavision-ai-powered-furcation-detection) · hackathon [[MEGA Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** chakra-ui-backend:-node.js, express.js, fastapi, javascript, javascript-frontend:-react, node.js, python, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for furcavision – ai-powered furcation detection

## Body

Home Page Detection Page Inspiration Early detection of furcation defects is crucial in preventing advanced periodontal disease and tooth loss. However, identifying these defects in dental X-rays is time-consuming and requires expert analysis. We aimed to create an AI-powered solution that automates this process, making diagnostics faster and more accessible for dental professionals. What It Does FurcaVision automatically analyzes dental X-rays to detect furcation defects and bone loss. It: Classifies images as "With Furcation" or "Without Furcation" using deep learning. Extracts individual teeth for focused analysis. Marks both furcation defect areas and bone loss regions for better visualization. How We Built It AI Model We developed a multi-model deep learning system: Teeth Extraction Model: Built on YOLOv8 , it segments and extracts individual teeth from X-rays for precise analysis. Furcation Marker Model: Uses U-Net with MobileNetV2 as the backbone to detect and highlight furcation defect areas. Bone Loss Marker Model: Also based on U-Net with MobileNetV2 , it identifies and marks bone loss regions in the X-rays. Classification Model: A fine-tuned DenseNet201 classifies X-rays into "With Furcation" or "Without Furcation." Tech Stack Frontend: React with Chakra UI for a smooth and responsive user experience. Backend: Node.js and Express, integrating TensorFlow for real-time predictions. Deployment: Hosted on a web platform for easy accessibility without installation. Challenges We Ran Into Data Limitations: Finding and preprocessing a well-labeled dataset for furcation defects and bone loss was challenging. Model Optimization: Balancing accuracy while ensuring real-time performance required extensive tuning. Integration Issues: Coordinating multiple deep learning models to work seamlessly in a web-based system. Accomplishments That We're Proud Of Successfully developed a multi-model AI system for furcation detection and bone loss analysis. Integrated deep learning models into a fully functional web application. Created a user-friendly interface that simplifies dental diagnostics for professionals. What We Learned Implementing multiple AI models requires careful coordination and optimization. Medical imaging analysis demands high-quality datasets and robust preprocessing. Efficient model deployment is crucial for a smooth user experience in web-based AI applications. What's Next for FurcaVision – AI-Powered Furcation Detection Enhanced Accuracy: Further refining models with larger, high-quality datasets. Additional Dental Diagnostics: Expanding beyond furcation defects to detect other periodontal issues. User Feedback & Testing: Collaborating with dental professionals to improve usability. Mobile Compatibility: Extending support for mobile devices for greater accessibility. FurcaVision aims to revolutionize dental diagnostics by enabling early, accurate, and efficient detection of furcation defects and bone loss. 🚀 <div