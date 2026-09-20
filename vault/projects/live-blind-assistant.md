---
slug: "live-blind-assistant"
url: "https://devpost.com/software/live-blind-assistant"
title: "Live Blind Assistant"
hackathon: "Forest Hacks"
organization: "ForestHackathons"
winner: true
words: 493
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/video_visual"
---

# Live Blind Assistant

> AI-powered real-time assistant that helps blind individuals navigate their surroundings safely through visual and object descriptions.

[Devpost](https://devpost.com/software/live-blind-assistant) · hackathon [[Forest Hacks]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[video_visual]]

**stack** imagerecognition, opencv, pyttsx3, speechrecognition, textrecognition

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for live blind assistant

## Body

Inspiration The inspiration for our Live Assistant for Blind People came from the need to improve accessibility for individuals with visual impairments. We wanted to create a tool that could provide real-time assistance in navigating their surroundings, identifying objects, and offering descriptions of their environment. Our goal was to empower blind users with greater independence and confidence in their daily lives through the use of cutting-edge AI and computer vision technologies. What it does The Live Assistant for Blind People is an AI-powered app that helps visually impaired individuals by capturing images from their surroundings and providing detailed audio descriptions. Using speech recognition, the app allows users to issue voice commands to describe objects, environments, or even read text from books. Additionally, a live mode captures images at intervals to warn the user of any potential hazards or provide assistance while on the move. How I built it We built the app using Python and integrated the Google Gemini API for generating descriptive text from images. We also utilized OpenCV for capturing images through the camera and Pyttsx3 for converting text to speech. The app’s interface is built using Tkinter to make it simple and user-friendly, and we incorporated the OpenWeather API to offer additional information like weather updates. The real-time processing capabilities of Gemini API allowed us to create a seamless and efficient experience for the users. Challenges I ran into One of the main challenges we faced was optimizing the accuracy of image descriptions while keeping response times low. Capturing relevant details about objects and ensuring the descriptions were concise yet informative took a lot of fine-tuning. Additionally, developing a voice command system that could reliably recognize and respond to user input was challenging, especially when dealing with noisy environments or different accents. Accomplishments that I'm proud of We’re incredibly proud of creating an application that truly makes a difference in the lives of blind individuals. Successfully integrating speech recognition and AI-powered descriptions was a huge milestone. The app's ability to detect potential hazards and offer real-time assistance is a feature we are especially proud of, as it addresses a critical need for user safety. What I learned During the development process, we learned a lot about the importance of accessibility in software design. We deepened our understanding of AI model integration and learned how to balance performance and accuracy in real-time systems. Additionally, working with user feedback from the blind community gave us valuable insights into designing solutions that prioritize user needs and experience. What's next for Live Blind Assistant In the future, we plan to enhance the live mode to include object tracking and more sophisticated hazard detection. We are also exploring ways to improve the accuracy of text recognition for reading printed materials and expand the language support for users worldwide. Ultimately, our goal is to make this app a staple tool for visually impaired individuals, helping them navigate and engage with their environment confidently and independently. <div