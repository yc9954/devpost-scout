---
slug: "moodify-iwq8ug"
url: "https://devpost.com/software/moodify-iwq8ug"
title: "Moodify"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 637
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/mental_health"
---

# Moodify

> Meet Moodify - your emotional companion UI and cli version

[Devpost](https://devpost.com/software/moodify-iwq8ug) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[mental_health]]
  <sub>weak: web_dom</sub>

**stack** css, deepface, emoroberta, flask, gemini-api, html, javascript, opencv, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for moodify

## Body

Inspiration Moodify was inspired by the need for an accessible tool to help individuals understand and manage their emotions. In an era where mental health is becoming increasingly important, I wanted to create a platform that empowers people to recognize their emotional states and receive personalized guidance in real-time. The idea emerged from my curiosity about how technology, especially AI, can play a role in emotional well-being. What it does Moodify is an AI-powered emotion recognition platform that helps users understand their emotional state through webcam and text input. Using computer vision and natural language processing, it analyzes facial expressions and text to detect emotions like joy, sadness, anger, and more. The platform then provides personalized responses and recommendations tailored to the detected emotions, helping users navigate their feelings and improve their emotional well-being. UI Version (Web Interface) Emotion Detection : The system uses webcam input to detect emotions through facial expressions in real time. The webcam feed is processed using OpenCV and Haar cascades for emotion recognition. Personalized Responses : Once the emotion is detected, the system generates tailored, AI-driven responses to provide emotional insights. Real-Time Interaction : The system allows for seamless, real-time interaction with users, providing an accessible interface to monitor and respond to emotional states. CLI Version Text Input : The CLI version allows users to input text for emotion analysis. It processes the text using EmoRoBERTa, a transformer-based model, to detect emotions like happiness, sadness, etc. Emotion Analysis : After analyzing the input, the CLI version returns the detected emotion and generates a personalized response based on the analysis. Command-Line Interaction : The CLI provides a simple way to run the platform via terminal, offering flexibility and ease of use for those who prefer a text-based interface. How I built it I used OpenCV for face detection and DeepFace for emotion recognition to analyze the user's facial expressions in real-time. For text-based emotion analysis, EmoRoBERTa, a transformer-based model, was integrated to detect emotions from written input. Both systems feed their results into a unified interface that provides personalized responses and emotional insights. All of this is wrapped in a streamlined user interface, ensuring a seamless user experience. CLI Version The CLI version leverages the same emotion detection models (EmoRoBERTa for text and OpenCV/DeepFace for webcam), but the interface is command-line based. It offers a flexible, script-based method for emotion analysis, allowing users to test the system without relying on a graphical user interface. Challenges I ran into Integration of Two Systems : Combining webcam-based emotion detection with text-based emotion recognition into a single user-friendly platform was a complex task. Real-Time Performance : Achieving accurate and fast emotion detection, especially with both text and webcam input, required fine-tuning the system to ensure it provided quick responses without lag. Personalization : Delivering relevant, personalized responses based on detected emotions required careful design of the recommendation engine to make sure the advice resonated with the user's emotional state. Accomplishments that I am proud of Successfully integrated two distinct emotion-detection systems (webcam and text) into a cohesive experience. Developed a responsive interface that allows users to receive real-time emotional insights. Achieved a functional prototype capable of detecting and responding to emotions accurately. Released a CLI Version that provides text-based emotion analysis and offers users an alternative method of interacting with the platform. What I learned Throughout the development process, I gained valuable experience in integrating multiple machine learning models and optimizing them for real-time use. I also learned about the challenges of creating personalized, emotion-driven responses and how important user experience is when designing applications aimed at mental well-being. What's next for Moodify I plan to integrate voice recognition features to improve the user experience. The goal is to offer users a comprehensive emotional health tool that they can turn to anytime they need support. <div