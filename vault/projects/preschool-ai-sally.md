---
slug: "preschool-ai-sally"
url: "https://devpost.com/software/preschool-ai-sally"
title: "Sally, An Educational Preschool AI"
hackathon: "Amazon Sumerian AR/VR Challenge"
organization: "Amazon"
winner: true
words: 950
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
---

# Sally, An Educational Preschool AI

> A educational experience for preschoolers built with AWS Sumerian

[Devpost](https://devpost.com/software/preschool-ai-sally) · hackathon [[Amazon Sumerian AR-VR Challenge]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[runtime_tool_creation]] [[vision_ocr]] [[voice_speech]]
**substrate** [[video_visual]]

**stack** amazon-web-services, javascript, lambda, lex, polly, python, rekognition, sumerian

## How they structured the write-up

- inspiration
- what it does
- how i did it & challenges i faced
- instructions
- accomplishments that i'm proud of
- future development

## Body

Start screen Intro First question Second question Sally. A Preschool Level Educational AI. Inspiration I wanted to attempt to create a new experience of perhaps what the future of educational programming might be for preschoolers. So I drew on the examples of past popular and widely regarded television programs for preschoolers. Learned what made them successful, and with Amazon Sumerian and other AWS services, attempt to innovate upon those key concepts. Here are the 3 programs I used as a benchmark. Sesame Street One of the longest educational programs that is still running today in the United States was an experiment to transform educational television. They combined entertainment and education it is arguably the first successful educational programming to be created. Main takeaway, fun! The app must be fun but also educational. Blue's Clues Created by child behavioral experts, they added the concept of eliciting participation from viewers. This changed how programs are created today, and most modern programs have one form or another of this concept in their scripts. Main takeaway, interactivity! The app must be interactive and encourage participation. Dora the Explorer Created during a time when the population of Spanish speaking children were increasing in the United States, they introduced a host that added Spanish into the program. This made the show more approachable. Main takeaway, accessibility! If I can incorporate different languages to the app, it can make it more accessible to more children. What it does Sally is a 3D Amazon Sumerian host that will take on the role of an instructor/friend for a child. The child can then interact with it as if it is a real person. Meaning understanding a child's answer and reacting accordingly. To make Sally more like a real person, I gave her a voice (polly) , ears (webrtc, web speech, aws lex) , and eyes (webrtc, aws lambda, aws rekognition) . Through different inputs 3D animations are done in real time. Entities that are interacted with are personified because the audience is at a preschool age. For more accessibility, the project can be experienced in multiple languages (aws lambda, aws translate) . How I did it & challenges I faced 3D I used Amazon Sumerian to provide the host that will take on the persona of Sally as well as the 3D engine. I needed to make it entertaining, so I wanted to have fun animations like stretching and squashing of things (Like in cartoons). One big problem is I am not a 3D artist, so I did it the best way I knew how, with math. To scale, move and rotate the meshes in the scene to look naturally I needed more control over the transform component. So I created a script with some extra math functions for lerping and updating the transforms over time. Speeches AWS Lex was used to get the context of speeches from the user. I also did not want to use a button or any input to figure out when a user is speaking. So I used webrtc to detect microphone inputs which can trigger webspeech api to start listening if it is not already. Web speech will then transcribe the speech to text, and only then its sent to Lex. The end result is as if Sally now had ears! The Host Sumerian has host that can be animated through gesture marks in speeches. These can be generated out of play, but I needed it to be more dynamic due to the variety of answers the user may give. I had experience experimenting with this in the past, but there required a couple of improvements to my script. And with that I rewrote my custom speech extension script so speeches included some dynamically generated SSML. Image Recognition For this I used webrtc to draw the camera feed onto a canvas. The canvas is captured and sent to a serverless lambda function which calls AWS Rekognition for it's labels. The labels are passed back into the app logic and used to generate speech responses. Languages Everything in the app is actually in English. Whenever a translation is needed, the text is sent to a serverless lambda function which uses AWS Translate. For example if the user chooses French. Speeches are translated into French before speaking. Similarly user inputs are first translated back into English before it is handled. Instructions Please use the latest Chrome browser and at a minimum have a microphone. For the best experience, use headphones and a camera. Start the scene, then you can select a language or just press start and begin. No other inputs other than your voice is needed! Your voice input is displayed on the bottom, as well as Sally's current sentence. Tips are available on the upper right hand corner of the screen if you need it. Enjoy! Accomplishments that I'm proud of The project is all done with scripting. Some cool custom sumerian components that can be reused in future projects. Integrating Asian languages into the project was harder than I expected. Finding out it actually worked... Future development Add VR for the scene. If I had a chance to get the proper equipment I would like to add VR capabilities to the app. I felt like since I cannot properly test out VR it may take away from the current form of the project. Use AWS comprehend for NLP. Lex is great for finding context but I ran into several limitations while developing this project. Adding more languages, this can be done immediately but may not work as intended because I lacked the time to test them. Working to find more issues, which I am sure there are still a lot of. <div