---
slug: "emusify"
url: "https://devpost.com/software/emusify"
title: "Emusify"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 835
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Emusify

> Emusify is a real-time mood-based music recommendation system that runs in the background and plays music according to a user's mood.

[Devpost](https://devpost.com/software/emusify) · hackathon [[Funathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** deep-learning, keras, machine-learning, opencv, python

## How they structured the write-up

- 💡 inspiration
- ⚙️ what it does?
- 🔧 how i built it?
- challenges i ran into 🙁
- accomplishments that i am proud of 😇
- what i learned 🤔
- what's next for emusify 📲

## Body

Working Emotion classifier Data Training Recommendation of song Recommendation of song Emotion recommendation according to dominant emotion Emusify Emusify is a real-time mood-based music recommendation system that runs in the background and plays music according to a user's mood. 💡 Inspiration During this modern age, music platforms have revolutionized the way we access and enjoy music, making vast collections easily available at our fingertips. These platforms constantly strive to enhance music organization and search capabilities, effectively tackling the problem of choice and simplifying the process of discovering new music. The rising popularity of recommendation systems further aids individuals in finding the right music for every occasion. Nevertheless, there remains a gap in terms of personalization and recommendations that truly cater to emotions. Music holds a profound influence over human beings, often utilized for relaxation, mood regulation, stress relief, and even as a therapeutic tool for various ailments. Thus, recommendation systems aim to assist people in selecting music suited to their specific life situations and maintaining their mental and physical well-being. ⚙️ What it does? This system will operate persistently in the background, continuously analyzing and forecasting the user's mood within a designated time frame. It will select and play a song based on the user's mood. For instance, if the user is feeling calm or neutral, a soothing or meditative song will be chosen. The script will continue to run in the background, monitoring any changes in emotions every 5-6 minutes, and selecting a new song accordingly. 🔧 How I built it? Technology Stack ● OpenCV ● Machine Learning ● Deep Neural Network Emusify is a real-time mood-based music recommendation system using machine learning and keras dataset. This project has three main parts: ❖ Data Collection ❖ Data Training ❖ Data Testing This project utilizes Mediapipe, which retrieves various key points called landmarks. Within the Mediapipe framework, Holistic is a pipeline that combines optimized components for face, hands, and pose tracking. This enables the model to simultaneously detect hand and body poses, as well as facial landmarks. To gather data, the data collection script must be executed for each emotion. In this project, approximately 1000 images were collected for six specific emotions, in addition to the keras emotion dataset. After collecting the data, it needs to be loaded and sent for training the dense neural network. In the testing script, the model and labels are loaded. Subsequently, the predicted emotion can be displayed on the screen based on the user's facial expression. Next, we move on to predicting songs based on the user's emotions. To achieve this, a local directory for songs needs to be created. Within the song folder, folders corresponding to each emotion must be added. Each of these emotion folders should contain 5-6 songs related to that specific emotion. Images Dataset When the user appears in front of the webcam, we will monitor their emotions for approximately 15-20 seconds. During this time, we will analyze their facial expressions to determine their emotional state. We will maintain an array to track the occurrence of specific emotions, and the counter for the dominant emotion will increase. Based on the dominant emotion, a corresponding song will be played. For instance, if the user displays signs of sadness for an extended period, a cheerful song will be played to uplift their mood. After the initial song is played, the script will continue running in the background and analyze the user's emotions for approximately 5-6 minutes. Following this analysis, another song will be selected based on the most prevalent emotion. Challenges I ran into 🙁 I encountered difficulties while collecting data, as capturing 990 images portraying a specific emotion proved to be a rather demanding task. Interestingly enough, during the process, there were instances where a sad emotion unexpectedly transformed into a happy one, resulting in some amusing moments. Accomplishments that I am proud of 😇 I take pride in my achievement of successfully developing an effective recommendation system within a relatively limited timeframe. Additionally, we have the opportunity to enhance the code to capture the emotions of multiple individuals and provide collaborative song recommendations based on their combined emotions. What I learned 🤔 I learned a lot about new modules and packages of python like MediaPipe Selfie Segmentation for removal of a human face from the background and also the Keras library. What's next for Emusify 📲 This particular project is specifically designed for individuals positioned in front of a computer's webcam, situated at a distance of 1 meter. However, if the distance exceeds this threshold, the accuracy of predictions diminishes, particularly when it comes to accurately capturing neutral and sad emotions. Consequently, the predictions tend to be incorrect. To enhance this situation, a number of measures can be taken. Firstly, acquiring a high-definition camera would be beneficial. Additionally, it is crucial to establish a comprehensive training dataset consisting of approximately 6000-10000 diverse images showcasing individuals expressing various emotions. Moreover, experimenting with different models for both training and testing the data can also prove advantageous. <div