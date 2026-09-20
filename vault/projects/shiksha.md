---
slug: "shiksha"
url: "https://devpost.com/software/shiksha"
title: "Shiksha"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 328
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Shiksha

> Keeping an ear on class, so you don’t have to!

[Devpost](https://devpost.com/software/shiksha) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[transcript_audio]] [[video_visual]]

**stack** deepface, opencv, python, streamlit, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shiksha

## Body

UI Processing of video Emotion Metrics on the lecture Engagement Percentage Inspiration In the rapidly evolving educational landscape, teachers face unprecedented challenges in maintaining student engagement, adhering to curriculum, and providing personalized learning experiences. Shiksha was born from a vision to leverage cutting-edge AI technologies to support educators by providing real-time, actionable insights into classroom dynamics. The inspiration came from recognizing the limitations of traditional classroom monitoring: Difficulty in simultaneously tracking student engagement Challenges in maintaining curriculum adherence Limited real-time feedback mechanisms Lack of data-driven insights for teaching improvement What it does Shiksha is an intelligent classroom monitoring system that: Analyzes real-time classroom video feeds Transcribes and evaluates teacher's speech Tracks student engagement and emotional responses Provides instant, actionable feedback to educators Monitors curriculum coverage and teaching effectiveness Key Features: Facial recognition and emotion detection Speech-to-text transcription Engagement scoring Curriculum adherence tracking Interactive dashboard for real-time insights How we built it We developed Shiksha using a sophisticated technological stack: Architecture: Design Pattern: Factory and Service patterns for modular design Dependency Injection for flexible component management Technical Stack: Speech Analysis: OpenAI Whisper Natural Language Processing: Hugging Face Transformers Computer Vision: OpenCV for video processing DeepFace for facial recognition Frontend: Streamlit Data Visualization: Plotly Programming Language: Python Key Components: Speech Analyzer (Whisper-based) Vision Analyzer (DeepFace and OpenCV) Engagement Analyzer (Transformer-based) Metrics Collection and Processing Real-time Dashboard Challenges we ran into Complex Integration: Combining multiple AI technologies with different inference mechanisms Real-time Performance: Ensuring low-latency processing of video and audio streams Accomplishments that we're proud of Created a modular, extensible AI system for educational monitoring Successfully integrated multiple cutting-edge AI technologies What we learned Challenges of real-time AI inference Nuances of emotion and engagement detection Balancing technical complexity with user experience Ethical considerations in AI-powered educational tools What's next for Shiksha Future Development Roadmap: Enhanced Machine Learning Models Personalized Teaching Recommendations Multi-language Support Integration with Learning Management Systems Advanced Privacy Controls Predictive Analytics for Student Performance Mobile and Tablet Support <div