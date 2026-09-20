---
slug: "signbridge-tjcnv5"
url: "https://devpost.com/software/signbridge-tjcnv5"
title: "SignBridge"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 372
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
---

# SignBridge

> "Sign Bridge is an AI-powered real-time Indian Sign Language detector that makes STEM education accessible for deaf students using Computer Vision."

[Devpost](https://devpost.com/software/signbridge-tjcnv5) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
  <sub>weak: geospatial</sub>

**stack** mediapipe, opencv, python, pyttsx3, scikit-learn, streamlit

## Body

"Yes" gesture "Stop" gesture "Good" gesture "What" gesture Inspiration Over 63 million people in India who are deaf or have a hearing problem. Deaf students have a tough time, in classrooms every day because the education system is not made for them. We thought about this a lot. Asked ourselves. What if we could use artificial intelligence to help deaf people communicate. This idea turned into Sign Bridge. What We Built Sign Bridge is a Sign Language detection system that uses artificial intelligence. It can detect hand gestures. Convert them into text right away. You just need a webcam to use it no equipment required. Sign Bridge helps people communicate through sign language. How We Built It Data Collection Captured ISL gestures via webcam using OpenCV. 200 samples per sign stored as hand landmark data. Landmark Extraction Used MediaPipe to extract 21 landmarks per hand. Each hand gives 63 values for x, y, z coordinates. Both hands combined give ( 21 \times 3 \times 2 = 126 ) features per frame. Model Training Static signs → Random Forest classifier Motion signs → CNN + LSTM sequential model processing ( T = 30 ) frames per gesture The full feature vector per frame: F=[x1,y1,z1,…,x21,y21,z21]×2=126 features F = [x_1, y_1, z_1, \dots, x_{21}, y_{21}, z_{21}] \times 2 = 126 \text{ features} F=[x1​,y1​,z1​,…,x21​,y21​,z21​]×2=126 features Deployment Real-time Streamlit web app with live webcam feed accessible from any browser. Tech Stack Python | TensorFlow | MediaPipe | OpenCV | Scikit-learn | Streamlit What We Learned How to Get Hand Landmarks. Make Them Consistent, with MediaPipe Difference Between Static Gestures and Motion Gestures How LSTM Understands Patterns in Time for Gesture Data Building and Deploying a Real-Time AI Web App Challenges We Faced Similar looking signs confused the model at Lighting conditions also affected how well the model detected hands The model had to work in real-time so it had to balance being fast and accurate Collecting data was a slow process. We had to gather 200 samples, for each sign Impact Sign Bridge — because every student deserves to be heard, even in silence. Sign Bridge makes ISL recognition accessible through any browser, breaking communication barriers in STEM classrooms for millions of deaf students across India. <div