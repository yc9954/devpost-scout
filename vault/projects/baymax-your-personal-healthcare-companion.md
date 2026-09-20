---
slug: "baymax-your-personal-healthcare-companion"
url: "https://devpost.com/software/baymax-your-personal-healthcare-companion"
title: "Baymax, Your Personal Healthcare Companion"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1133
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Baymax, Your Personal Healthcare Companion

> Our AI-powered robot arm is a personalized solution to restore physically impaired and elderly individuals’ ability to interact with their environment.

[Devpost](https://devpost.com/software/baymax-your-personal-healthcare-companion) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[video_visual]]

**stack** dynamixel-sdk, google-mediapipe, matplotlib, mediapipe, numpy, openai, openai-gpt4-api, openai-whisper, opencv, pyaudio, python, vlc, vlc-sdks:-dynamixel-sdk-apis:-openai-gpt-4-model-calls

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for baymax

## Body

Inspiration 40 million people in the world are blind, including 20% of all people aged 85 or older. Half a million people suffer paralyzing spinal cord injuries every year. 8.5 million people are affected by Parkinson’s disease, with the vast majority of these being senior citizens. The pervasive difficulty for these individuals to interact with objects in their environment, including identifying or physically taking the medications vital to their health, is unacceptable given the capabilities of today’s technology. First, we asked ourselves the question, what if there was a vision-powered robotic appliance that could serve as a helping hand to the physically impaired? Then we began brainstorming: Could a language AI model make the interface between these individual’s desired actions and their robot helper’s operations even more seamless? We ended up creating Baymax—a robot arm that understands everyday speech to generate its own instructions for meeting exactly what its loved one wants. Much more than its brilliant design, Baymax is intelligent, accurate, and eternally diligent. We know that if Baymax was implemented first in high-priority nursing homes, then later in household bedsides and on wheelchairs, it would create a lasting improvement in the quality of life for millions. Baymax currently helps its patients take their medicine, but it is easily extensible to do much more—assisting these same groups of people with tasks like eating, dressing, or doing their household chores. What it does Baymax listens to a user’s requests on which medicine to pick up, then picks up the appropriate pill and feeds it to the user. Note that this could be generalized to any object, ranging from food, to clothes, to common household trinkets, to more. Baymax responds accurately to conversational, even meandering, natural language requests for which medicine to take—making it perfect for older members of society who may not want to memorize specific commands. It interprets these requests to generate its own pseudocode, later translated to robot arm instructions, for following the tasks outlined by its loved one. Subsequently, Baymax delivers the medicine to the user by employing a powerful computer vision model to identify and locate a user’s mouth and make real-time adjustments. How we built it The robot arm by Reazon Labs, a 3D-printed arm with 8 servos as pivot points, is the heart of our project. We wrote custom inverse kinematics software from scratch to control these 8 degrees of freedom and navigate the end-effector to a point in three dimensional space, along with building our own animation methods for the arm to follow a given path. Our animation methods interpolate the arm’s movements through keyframes, or defined positions, similar to how film editors dictate animations. This allowed us to facilitate smooth, yet precise, motion which is safe for the end user. We built a pipeline to take in speech input from the user and process their request. We wanted users to speak with the robot in natural language, so we used OpenAI’s Whisper system to convert the user commands to text, then used OpenAI’s GPT-4 API to figure out which medicine(s) they were requesting assistance with. We focused on computer vision to recognize the user’s face and mouth. We used OpenCV to get the webcam live stream and used 3 different Convolutional Neural Networks for facial detection, masking, and feature recognition. We extracted coordinates from the model output to extrapolate facial landmarks and identify the location of the center of the mouth, simultaneously detecting if the user’s mouth is open or closed. When we put everything together, our result was a functional system where a user can request medicines or pills, and the arm will pick up the appropriate medicines one by one, feeding them to the user while making real time adjustments as it approaches the user’s mouth. Challenges we ran into We quickly learned that working with hardware introduced a lot of room for complications. The robot arm we used was a prototype, entirely 3D-printed yet equipped with high-torque motors, and parts were subject to wear and tear very quickly, which sacrificed the accuracy of its movements. To solve this, we implemented torque and current limiting software and wrote Python code to smoothen movements and preserve the integrity of instruction. Controlling the arm was another challenge because it has 8 motors that need to be manipulated finely enough in tandem to reach a specific point in 3D space. We had to not only learn how to work with the robot arm SDK and libraries but also comprehend the math and intuition behind its movement. We did this by utilizing forward kinematics and restricted the servo motors’ degrees of freedom to simplify the math. Realizing it would be tricky to write all the movement code from scratch, we created an animation library for the arm in which we captured certain arm positions as keyframes and then interpolated between them to create fluid motion. Another critical issue was the high latency between the video stream and robot arm’s movement, and we spent much time optimizing our computer vision pipeline to create a near instantaneous experience for our users. Accomplishments that we're proud of As first-time Hackathon participants, we are incredibly proud of the incredible progress we were able to make in a very short amount of time, proving to ourselves that with hard work, passion, and a clear vision, anything is possible. Our team did a fantastic job embracing the challenge of using technology unfamiliar to us, and stepped out of our comfort zones to bring our idea to life. Whether it was building the computer vision model, or learning how to interface the robot arm’s movements with voice controls, we ended up building a robust prototype which far surpassed our initial expectations. One of our greatest successes was coordinating our work so that each function could be pieced together and emerge as a functional robot. Let’s not overlook the success of not eating our hi-chews we were using for testing! What we learned We developed our skills in frameworks we were initially unfamiliar with such as how to apply Machine Learning algorithms in a real-time context. We also learned how to successfully interface software with hardware - crafting complex functions which we could see work in 3-dimensional space. Through developing this project, we also realized just how much social impact a robot arm can have for disabled or elderly populations. What's next for Baymax Envision a world where Baymax, a vigilant companion, eases medication management for those with mobility challenges. First, Baymax can be implemented in nursing homes, then can become a part of households and mobility aids. Baymax is a helping hand, restoring independence to a large disadvantaged group. This innovation marks an improvement in increasing quality of life​ for millions of older people, and is truly a human-centric solution in robotic form. <div