---
slug: "lingling-ai"
url: "https://devpost.com/software/lingling-ai"
title: "LingLing.ai"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 462
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# LingLing.ai

> AI music tutor that analyzes your playing with a vision and audio model, offers advice, answers questions generates personal songs and sheet music to practice the key areas you need to improve.

[Devpost](https://devpost.com/software/lingling-ai) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** beatovenai, cors, flask, librosa, magicloop, musci21, openai, plotly, streamlit

## How they structured the write-up

- inspiration
- what it does
- architecture

## Body

Inspiration We all know the famous saying: "You must practice 40 hours a day to master your instrument." But in reality, time is precious and limited. A staggering 45% of music students quit within their first two years, often due to lack of consistent guidance and feedback. What if you could maximize the effectiveness of every practice minute with AI-powered guidance? That's where MusicTeacher AI comes in. What it does LingLing.AI reimagines music education with an empathetic AI-powered system. It leverages advanced technologies to enhance the practice experience, providing intelligent, performance-aware assistance to both students and teachers. Performance videos are analyzed in real-time on a single platform and evaluated based on multiple criteria. Critical details such as rhythm accuracy, pitch, posture, emotional expression, and technical execution are collected from the performances. These details are leveraged to recommend specific practice strategies and generate custom exercises. Architecture We developed LingLing.AI using a comprehensive tech stack: Frontend: Streamlit for the user interface and visualization Plotly for interactive spider charts and data visualization Custom CSS for styling built with codebuff Backend: Flask for the server-side API Flask-CORS for cross-origin resource sharing OpenAI API for chat interactions and feedback Nebius.ai API and mediapipe for video performance analysis custom model for audio performance analysis Beatoven.ai for music generation and sheet music making Codebuff for optimisations, code densing and removing repetitions and ineficiencies Challenges we ran into Creating a robust dataset of musical performances across skill levels Developing accurate real-time audio analysis algorithms Integrating multiple AI models for comprehensive performance assessment Balancing technical feedback with encouraging, motivational guidance Suffered a catastrophic loss with github and lost alot of functionality while tweaking for the video but everything is still in the reflog Accomplishments that we're proud of Successfully using a computer vision model for instrument-specific posture analysis Developed a comprehensive performance evaluation system Created an adaptive song generation algorithm that matches student skill level Technical Complexity Implemented multiple AI models for audio and video analysis Created a sophisticated music generation system Developed real-time performance analysis capabilities Design and User Experience Our design focuses on student engagement and learning: Clean, intuitive UI suitable for all age groups Comprehensive progress tracking and visualization Immediate feedback during practice sessions Interactive sheet music display Impact Makes quality music education accessible to everyone Supports teachers with detailed student progress analytics Bonus Points Open-sourced our performance analysis model on HuggingFace Published a dataset of annotated music performances What we learned How to combine multiple AI technologies for comprehensive music analysis The importance of balance between technical and artistic feedback Methods for generating personalized practice materials What's next for LingLing.AI Expand instrument support beyond current offerings Develop more sophisticated music generation capabilities Partner with music schools for real-world testing Add support for ensemble practice and analysis <div