---
slug: "naterida-microbots"
url: "https://devpost.com/software/naterida-microbots"
title: "NATERIDA microbots"
hackathon: "FusionHacks 2"
organization: "FusionHacks"
winner: true
words: 1134
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NATERIDA microbots

> NATERIDA — The AI-powered exploration robot that thinks, adapts, and protects while gathering smart data across farms, forests, space, and disaster zones — no risks, just intelligence.

[Devpost](https://devpost.com/software/naterida-microbots) · hackathon [[FusionHacks 2]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[agriculture_food]] [[climate_energy]] [[disaster_emergency]] [[education]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]] [[researcher]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** css, deepseek-api-(llm), esp32, espasyncwebserver, espwebserver, html, javascript-frameworks/libraries:-arduino-ide, kalman-filter-library, languages:-c++, matplotlib, numpy, opencv, pandas, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for naterida microbots

## Body

Naterida version 1 completed. facing troubles to correct code asynctcp did not work hence we switched to webserver view through naterida's camera 1st prototype problems to read sensor values live curve sketcher kalman filter for obstacle avoidance object detection using realtime naterida camera stop sign 91% confidence rate Heatmap generator we got approx of 98% accuracy within 10 epoch in classification model with 2 classes naterida cv trying to work locally computer vision detection Inspiration I built my first Arduino project—a blinking light—in grade 10, and it left a lasting impression on me. Since then, I’ve pursued my passion for robotics. Coming from Nepal, a country rich in natural beauty but lacking technological support, I’ve always dreamed of using robotics and AI to create real impact. That vision led me to build Naterida, my exploration bot designed to contribute to the betterment of my country and its people. What it does NATERIDA isn’t just any robot—it's like a mini Mars rover, but designed for Earth. The name stands for Navigation Transfer Intelligent Data Allocation Bot. It’s basically a multi-functional smart robot, loaded with sensors, AI capabilities, and a compact but powerful structure. The whole idea is to send it into any environment—whether it’s a forest, disaster site, remote village, or a traffic zone—and let it adapt using computer vision and sensors. The first thing it solves is environmental monitoring. With sensors like DHT11 for temp/humidity, MQ2 for gas/smoke, and light sensors, it can collect real-time environmental data.Also by using resnet 18 architecture we have designed a CNN to detect and identify different diseases in plants, with the help of computer vision and camera attached to naterida it can detect diseases and inform the locals or forest rangers about the spread of disease in plants, improving the sustainability. This data could be helpful for organizations or researchers who are working on pollution or climate change. Then there’s the exploration part—imagine sending humans to a risky zone, like an unstable cave or an area with toxic gas. Why risk a life when a robot can go there first? NATERIDA is built to take on those dangerous explorations with proper data collection and feedback systems. Then comes surveillance and monitoring. It uses computer vision to do stuff like number plate recognition or traffic flow analysis. In emergency cases like an accident, the robot can automatically deploy to the scene and help the victim or notify authorities. There’s also a concept for using it in wildlife reserves to prevent poaching—it’s silent, smart, and can capture activity using live video. Another idea is to fuse it with LLMs like ChatGPT or a local language model. That would give it a brain and a mouth—a chatbot with legs! It could become an assistant, a teacher, a guide, or even a friend. And since robotics is moving toward miniaturization, I believe in the future we could deploy a disaster response micro version of NATERIDA—able to crawl through collapsed buildings, scan for life, or detect gas leaks. How we built it The heart of NATERIDA is the ESP32, a powerful and Wi-Fi-capable microcontroller. We wired up sensors like DHT11, MQ2, LDR, MPU6050, HC-SR04, and GPS (NEO-6M) to it. For mobility, we used TT motors connected through an L298N motor driver. The brain part (vision + AI) runs on a PC or local server where we stream data from the robot to a web interface coded in HTML/CSS/JS. The dashboard shows sensor data live, lets us control the robot, change motor speeds, and even trigger alerts or messages. For computer vision, we started with OpenCV in Python and plan to upgrade to models like YOLO or MediaPipe for object detection. We also used TinyGPS++ for real-time location tracking. Power comes from a rechargeable Li-ion pack that powers both the ESP and the motors. Challenges we ran into There were a bunch of challenges. The biggest was sensor noise, especially from the MPU6050. It gave messy pitch and yaw values, which we cleaned up using a Kalman filter. Another issue was processing power—ESP32 couldn’t handle heavy vision tasks or AI locally. So we had to split the work between the bot and a server. Also, sometimes the ESP32 would crash when multiple tasks ran together, so we had to introduce watchdog timers and optimize the sensor polling rate. Since country like nepal is very unfamaliar with topics like robotics we really had to scavange various shops and stores for the equipments and parts. With a budget as less as 60$ we really had to face the true definition of optimization and adjustment. We also faced motor overheating, especially when testing long hours. L298N got too hot, so we added heat sinks and spaced out the circuit better. And yeah, Wi-Fi drops were a pain—especially in outdoor tests. So we had to code reconnect loops and error handling to make it more stable. Accomplishments that we're proud of The first win was making a fully functional robot with real-time sensor updates and web control—all on a tight budget (less than $60). We’re also proud of how modular the system is: you can remove or add sensors anytime, and the robot adapts. Another proud moment was integrating an LLM for control—that gave the bot a kind of “soul”. The fact that a high school student from Nepal could build something so versatile, so powerful—that too with limited access to tech—is something I’ll always be proud of. What we learned We learned that hardware is messy. Code is one thing, but real-world signals, motors, and sensors don’t act how you expect. We learned how to clean data, optimize performance, and debug under pressure. I personally understood how AI can transform dumb robots into adaptive, conversational systems. We also saw the power of open-source and how many global tools can be brought together for something local. Most importantly, we learned that impact doesn’t require money—it needs intention and engineering. What's next for NATERIDA microbots We’re enhancing NATERIDA by integrating local LLMs like DeepSeek and Mistral, making it smarter and more autonomous. Our next step is adding NVIDIA Jetson Nano—or even scaling to CUDA-powered platforms like NVIDIA COSMOS—for real-time ML processing, object detection, and advanced autonomy onboard. A swarm version is under development to enable multiple bots to collaboratively explore large-scale environments such as farms and disaster zones. We’re also working on a medical variant equipped with vitals sensors for rescue missions and remote healthcare. Beyond robotics, we’ve already built a ResNet-18 model for plant disease detection and a weather forecasting system—currently left unintegrated due to the ESP32’s AI limitations, but planned for deployment once we transition to stronger compute platforms. Finally, we aim to open-source the NATERIDA framework and release an AI-robotics API, empowering young innovators worldwide to build, scale, and adapt robotics for their own communities. <div