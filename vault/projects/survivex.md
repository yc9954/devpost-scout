---
slug: "survivex"
url: "https://devpost.com/software/survivex"
title: "SurviveX"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 966
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SurviveX

> Your hands-free conversational survival assistant. Powered by on device LLM inference, offering step-by-step instructions to keep you smarter and safer anytime, anywhere.

[Devpost](https://devpost.com/software/survivex) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[disaster_emergency]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** executetorch, finetuning, github, llama, mixedreality, nvidia-brev, python, pytorch, swift, torchtune, vision, visionos, visionpro, vscode

## How they structured the write-up

- the problem 💭
- our solution ⚙️
- how we built it
- fine-tuning our model
- what's next for survivex
- challenges we ran into
- what we learned
- accomplishments that we're proud of

## Body

welcome to SurviveX! once we did a little bit of digging.. what are we trying to solve? our way of being part of the solution SurviveX Link to demo The Problem 💭 30% of people who get lost in the wilderness never find their way back. Imagine yourself lost and alone in the middle of nowhere, no internet access to call for help or look up survival knowledge and time is running out . Whether it's a hiker with a broken leg, a soldier in combat, a responder during a natural disaster, or someone lost at sea, the lack of internet connectivity and immediate expert guidance can mean the difference between life or death . Our Solution ⚙️ SurviveX is an offline embedded AI assistant that combines Edge AI on a hands free device like the Apple Vision Pro along with health monitoring and voice guidance to provide real-time survival assistance . Our assistant provides step-by-step guidance , offering stressed users fast responses and ample opportunity for clarification throughout the process. Tracking vital signs through Terra's API , using them to augment our responses. Our machine learning model is designed to run on a hands free device like the Apple Vision Pro enabling survivors, first responders and soldiers to communicate via speech so your hands can focus on what matters : survival . Fine tuning our model to provide a user specific solution governed by environment indicative of the stress of the situation. Whether you need to treat an injury, start a fire with flint, fix up your broken car on the side of the highway, or aimlessly wonder and be navigated by the stars. SurviveX acts as your personal survival expert, adapting its guidance based on your speech and environmental conditions. How we built it We used ExecuTorch for on device inference for our Edge AI solution. The model we decided on was Meta's Llama-3.2-1B-Instruct since it was small and the most practical for on device inference. To fine tune our model we used torchtune - a PyTorch library for fine tuning our Llama Model on an instance of Nvidia's H-100 using Brev.dev. We used SwiftUI for the interface on the Vision Pro and linked in binaries from ExecuTorch for implementing the on device Llama model. We used data from Terra API to simulate tracking of heartbeats and vitals which our model used to adjust its tone and focus. Fine-tuning our Model Our Llama3.2-1B-Instruct model claimed to be fine tuned but we were a little worried when our model started generating bogus output when asked how to start a fire. We realized we needed to fine tune with 1000s of lines of code of particular scenarios our users may be in. We fine-tuned using LORA and then our custom dataset using tunetorch. We prepared them into a specific prompt/completion format using GPT-4: { "from": "human", "value": "How do I start a fire without matches? Can you please in small and concise steps explain to me how can I go about this task?" }, { "from": "assistant", "value": "1. Okay. Let us start by gathering dry tinder, such as leaves, grass, or bark. Let me know once you have got it." } Fine tuning our Llama3.2-1B model gave us much more promising results. Moving up to 3B tokens, caused our computer to crash which made us use Nvidia's Brev to fine tune with its H100 GPU. What's next for SurviveX Using iPhone's/Vision pro's external cameras' & sensors' ability to extract video input to provide personalized feedback based off our user's point of view. Higher GPU power would possibly enable us to use a larger model on device to extend beyond the Llama3.2-1B. Challenges we ran into Programming for the Vision Pro had limited resources and none of us had done it before. All of our team members wear glasses so they couldn't actually use the Vision Pro without switching off into contacts 😦 ExecuteTorch was only able to be run on an Intel Processor so generation of .pte files could only be done on one device. We had to stick to a smaller model such as Llama's 1B tokens because Llama3.2 with 3B slowed down on device inference. Fine tuning our model also increased the size which ran fine on MacOS and iOS but led to certain memory limits on the Vision Pro. Linking ExecuTorch and Swift within the Apple Ecosystem proved to be harder than we expected. The lack of Macbooks with an Apple Silicon chip in our team meant less hands on Swift. What we learned You don't need an internet connection to generate a response from an ML model! There are a lot of different survival scenarios that the wilderness can lead you to. Striking a good balance between speech-to-text and touch when developing for a hands free environment. With half of the team spending their time in the terminal we learned how useful linux commands can be. Accomplishments that we're proud of We have never worked with on device inference or Edge AI before so it was really fulfilling to get ExecuTorch working, and generating our pte files. Fine tuning our model on our local machines proved difficult and we pivoted with Nvidia's new platform, Brev, which helped us fine tune the Llama model with higher context windows. Once we had fine tuned the model, we were able to change context length depending on the device and its capabilities. Changing the context length parameter increased the quality of the model on both the iPhone as well as the Apple Vision Pro. None of us had really built for a hands free environment like the Vision Pro before so being able to leverage Swift knowledge and connect our on device AI inference along with speech to text was a huge learning experience. <div