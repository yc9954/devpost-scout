---
slug: "emergencyact"
url: "https://devpost.com/software/emergencyact"
title: "EmergencyAct"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 961
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/transportation"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# EmergencyAct

> Creating an aware and safer world by identifying emergencies which can improve mobility, public spaces, open areas, school buildings and more.

[Devpost](https://devpost.com/software/emergencyact) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[disaster_emergency]] [[education]] [[elder_child_care]] [[transportation]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** aiohttp, base64, collections, cv2, datetime, fastapi, gridfs, joblib, json, mongodb, numpy, openai, os, pandas

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for emergencyact
- note
- sources

## Body

GIF Inspiration Public transport is essential for millions of people around the world, but safety concerns remain prevalent. Sudden stops, starts, or turns can cause passengers to lose balance, especially if they are standing or moving around the vehicle. This issue is more significant in crowded buses where holding onto support bars might not be an option. According to recent studies, approximately 47% of bus accidents result in injuries (Kyle F., 2023). Older adults are particularly susceptible to falls on buses due to balance issues, vision impairments, and slower reaction times. This demographic is at a heightened risk, as falls are the leading cause of fatal and nonfatal injuries among older adults, according to the Centers for Disease Control and Prevention. Current Solutions on the Market While several fall detection devices exist, like the Medical Guardian MGMini Lite and the MobileHelp Micro, most are designed to be worn as pendants or wristbands (Habas et al., 2024). These devices focus on individual users rather than addressing the environmental and situational challenges in public spaces. ] Another solution, the Lunderg Chair Alarm System, uses wireless bed and chair sensor pads to alert caregivers before a fall happens. While effective in home settings, it falls short in complex environments like buses, where factors such as sudden stops and variable space require more adaptive solutions. We are built differently What it does Our Solution: EmergencyAct EmergencyAct is a real-time, video-based fall detection system designed specifically for public transport. Unlike traditional wearable devices, our solution leverages advanced camera systems integrated with machine learning algorithms to detect potential falls or sudden passenger movements, offering broader coverage and higher accuracy. How we built it Tools Used 📌 Computer Vision: OpenCV 📌 Natural Language Processing: GPT-3.5 Turbo, prompt classification 📌 Generative AI: GPT-4-o, base64 image encoding 📌 Data Visualization: Plotly 📌 Model Vision YOLOv8mpose, ultralytics, pytorch 📌 Machine Learning Random Forest (97% test set accuracy), MLP (97% test set accuracy) 📌 Libraries streamlit, CV2, ultralytics, numpy, base64, os, requests, openai, collections, datetime, torch, pickle, sklearn, joblib, pandas, numpy, fastapi, shutil, pymongo, urllib, aiohttp, json, PIL, gridfs, BASE64. Challenges we ran into We could not access external compute power. We could not divide computer power between computers because of internet restrictions.. Hosting our own API to make internal request in between services. Integrating the computer vision algorithm with the genai methods on the Streamlit platform. During the hackathon we managed to somehow tackle the issues by keeping our implementation internal, at least while using FIU’s internet connection. As for the integration of various services we managed to have a running MVP for our demo. Accomplishments We're Proud Of 🔍 Computer Vision Tools ✅ Object Detection: Identifies multiple individuals in a given area. 🔄 Pose Estimation: Detects if a person is in a potentially dangerous position. 🔒 Privacy Preservation: Ensures privacy by using tags without storing biometric data. 🧭 Pose Coordinate Tracking: Uses LLMs to track individual movements. 💡 Accident Prevention Recommendations: Suggests measures to improve safety. 🤖 Generative AI Tools 🕒 Timestamp Detection: Utilizes Vision AI to detect the time of a fall. 📍 Relative Position Analysis: Determines the accident location relative to the individual. 🔍 Cause Analysis: Analyzes potential causes based on timestamps. 📞 Emergency Call Prompting: Crafts messages to alert emergency services using text-to-speech. 📊 Dashboard Summary: Displays a summary of accidents and emergencies. What we learned Team Learning and Growth Collaboration: Building the project required a diverse set of skills such as computer vision, machine learning, data visualization, and real-time integrations. We learned how to better coordinate among team members with varied expertise, focusing everyone's strengths and knowledge for a better logisitic. Computer Vision: We gained hands-on experience with computer vision models like YOLOv8mPose. This project pushed us to go beyond object detection, which are critical for fall detection in complex environments. Generative AI and NLP Integration: Integrating natural language processing models into computer vision workflows was a new territory for us. Combining vision-based fall detection with text-based cause analysis gave us a new understanding of hybrid AI systems and how generative AI can enhance context understanding. Human-Centric Design: Public safety in transport is a sensitive issue. Through this project, we learned to approach safety-critical applications with a human-centered mindset, ensuring our solution is both effective and respectful of user privacy. Adapting in Real-Time: The dynamic nature of a hackathon forced us to rapidly adapt to unforeseen issues, such as limited internet access and integrating various components within tight deadlines. We became more adept at troubleshooting, quick decision-making, and agile development, ensuring that we still met our key objectives. These learnings not only enhanced our technical capabilities but also deepened our understanding of real-world applications of AI in public safety scenarios. Us What's next for EmergencyAct Next, we plan to enhance EmergencyAct by integrating it with real-time emergency response systems and piloting it on public buses to validate its effectiveness in real-world conditions. We will focus on improving privacy-preserving techniques, such as Federated Learning, and expanding multi-language support to make the solution accessible to diverse communities. Additionally, we aim to build a centralized dashboard for transport authorities, enabling them to monitor safety trends and generate reports. Note Our streamlit web page is limited due to internet connection restrictions inside the university, so not all features are available. Sources ChatPose: Chatting about 3D Human Pose. (2024). In arXiv:2311.18836v2 [cs.CV] 23 Apr 2024 [Journal-article]. https://arxiv.org/pdf/2311.18836 Kyle F. ,Bus Accident Statistics – 2023 Edition. (12/27/2023). https://www.truckinfo.net/research/bus-accident-statistics National Aging and Disability Transportation Center’s. (n.d), Falls prevention awareness in public transportation. https://www.usaging.org/files/N4A_Falls_wTips.pdf Habas, C., Uhler, K., & Ms, C. P. (2024, September 23). 4 Best fall detection Devices: a complete guide in 2024. https://www.helpguide.org/handbook/medical-alert-systems/best-fall-detection-devices Lunderg. (2024, September 29). Chair Alarm System - Wireless chair sensor pad & pager | Lunderg. https://lunderg.com/chair-alarm/ <div