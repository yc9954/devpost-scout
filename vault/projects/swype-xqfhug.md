---
slug: "swype-xqfhug"
url: "https://devpost.com/software/swype-xqfhug"
title: "Swype AI"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 589
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Swype AI

> Swype is an online application, transforming how people with motor-neurodegenerative diseases use their computer - from traditional keyboards and mice to gestures and voice commands.

[Devpost](https://devpost.com/software/swype-xqfhug) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[civic_government]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[video_visual]]

**stack** mediapipe, opencv, pyautogui, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for swype

## Body

Transforming Computer Interaction Inspiration Growing up with a close relative who navigated motor disabilities, I witnessed firsthand the critical need for accessible technology. Watching them struggle with tasks that many of us take for granted, like using a computer or navigating the internet, inspired me to explore how technology could be harnessed to improve accessibility and empower individuals facing similar challenges. This personal experience, combined with my passion for innovation, has driven me to create solutions that make a tangible impact on the lives of others. This belief is the foundation of my work with Swype, an application designed to empower individuals with neurodegenerative motor disabilities by enabling them to control their computers using natural hand movements and voice commands. What it does Swype allows individuals to transition from traditional input devices like keyboards and mice to seamless hand gestures and voice commands, offering a more accessible and efficient solution for those with motor diseases such as arthritis, Parkinson's, and more. By integrating advanced technologies, Swype makes digital interaction more intuitive, inclusive, and empowering for individuals with motor disabilities. How we built it Swype was developed using Python, leveraging key modules like MediaPipe for real-time hand tracking, OpenCV for image processing, and PyAutoGUI for controlling the computer interface. The system translates hand gestures into corresponding movements and actions, enabling users to control their computers without the need for traditional input devices. Challenges we ran into One of the major challenges we faced was reducing the latency between user input and the system's response, which initially led to erratic cursor movements and decreased efficiency. To tackle this, we integrated a Kalman filter into our system, a mathematical tool commonly used in signal processing to predict and smooth data points. By applying the Kalman filter, we were able to filter out noise from the hand tracking data and generate more precise cursor movements. We further enhanced this by adjusting the motion parameters, including the low-pass filter and dynamic scaling factors, to optimize the system's responsiveness and accuracy. Additionally, we fine-tuned the frame rate to ensure the system could process inputs in real-time, which is critical for providing a smooth and intuitive user experience. These technical refinements allowed us to achieve a balanced system that operates with high speed, efficiency, and reliability, significantly improving the user interaction experience for individuals with motor disabilities. Accomplishments that we're proud of Swype has been developed with Buildspace Season 5, and has passed through all challenges provided. Additionally, we're excited to be working with the Virginia Assistive Technology Department, who has agreed to let us test our product with some of their constituents to gain valuable information and usage results. What we learned Through our development process, we learned the importance of adaptability and inclusivity in assistive technology. Initially focused on motor disabilities, we recognized the potential for Swype to serve a broader audience, including individuals with neurodegenerative diseases and children with learning disabilities. This has driven us to expand Swype’s capabilities to cater to a wider range of users. What's next for Swype We are preparing to relaunch our beta version in September, with plans to release a full 1.0 version by November. We have been invited to present Swype at the 2024 Myositis Association International Annual Patient Conference in Baltimore, Maryland, where we will showcase our product to experts in the field. Additionally, we are honored to share our research with the American Chronic Pain Association in their quarterly publication, The Chronicle, further raising awareness and gathering valuable feedback for Swype’s continued development. <div