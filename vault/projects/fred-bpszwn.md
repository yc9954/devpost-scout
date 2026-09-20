---
slug: "fred-bpszwn"
url: "https://devpost.com/software/fred-bpszwn"
title: "FRED"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 801
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# FRED

> FRED is a satellite-powered emergency response tool that allows users in remote areas to send GPS coordinates, images, and voice data to responders, ensuring help can be dispatched from anywhere.

[Devpost](https://devpost.com/software/fred-bpszwn) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[disaster_emergency]]
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** cellular, firebase, ios, llama, python, raspberry-pi, satellite, skylo, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for fred

## Body

SOS Data Flow FRED First Responder Dashboard Inspiration The need for faster and more reliable emergency communication in remote areas inspired the creation of FRED (Fire & Rescue Emergency Dispatch). Whether due to natural disasters, accidents in isolated locations, or a lack of cellular network coverage, emergencies in remote areas often result in delayed response times and first-responders rarely getting the full picture of the emergency at hand. We wanted to bridge this gap by leveraging cutting-edge satellite communication technology to create a reliable, individualized, and automated emergency dispatch system. Our goal was to create a tool that could enhance the quality of information transmitted between users and emergency responders, ensuring swift, better informed rescue operations on a case-by-case basis. What it does FRED is an innovative emergency response system designed for remote areas with limited or no cellular coverage. Using satellite capabilities, an agentic system, and a basic chain of thought FRED allows users to call for help from virtually any location. What sets FRED apart is its ability to transmit critical data to emergency responders, including GPS coordinates, detailed captions of the images taken at the site of the emergency, and voice recordings of the situation. Once this information is collected, the system processes it to help responders assess the situation quickly. FRED streamlines emergency communication in situations where every second matters, offering precise, real-time data that can save lives. How we built it FRED is composed of three main components: a mobile application, a transmitter, and a backend data processing system. 1. Mobile Application: The mobile app is designed to be lightweight and user-friendly. It collects critical data from the user, including their GPS location, images of the scene, and voice recordings. 2. Transmitter: The app sends this data to the transmitter, which consists of a Raspberry Pi integrated with Skylo’s Satellite/Cellular combo board. The Raspberry Pi performs some local data processing, such as image transcription, to optimize the data size before sending it to the backend. This minimizes the amount of data transmitted via satellite, allowing for faster communication. 3. Backend: The backend receives the data, performs further processing using a multi-agent system, and routes it to the appropriate emergency responders. The backend system is designed to handle multiple inputs and prioritize critical situations, ensuring responders get the information they need without delay. 4. Frontend: We built a simple front-end to display the dispatch notifications as well as the source of the SOS message on a live-map feed. Challenges we ran into One major challenge was managing image data transmission via satellite. Initially, we underestimated the limitations on data size, which led to our satellite server rejecting the images. Since transmitting images was essential to our product, we needed a quick and efficient solution. To overcome this, we implemented a lightweight machine learning model on the Raspberry Pi that transcribes the images into text descriptions. This drastically reduced the data size while still conveying critical visual information to emergency responders. This solution enabled us to meet satellite data constraints and ensure the smooth transmission of essential data. Accomplishments that we’re proud of We are proud of how our team successfully integrated several complex components—mobile application, hardware, and AI powered backend—into a functional product. Seeing the workflow from data collection to emergency dispatch in action was a gratifying moment for all of us. Each part of the project could stand alone, showcasing the rapid pace and scalability of our development process. Most importantly, we are proud to have built a tool that has the potential to save lives in real-world emergency scenarios, fulfilling our goal of using technology to make a positive impact. What we learned Throughout the development of FRED, we gained valuable experience working with the Raspberry Pi and integrating hardware with the power of Large Language Models to build advanced IOT system. We also learned about the importance of optimizing data transmission in systems with hardware and bandwidth constraints, especially in critical applications like emergency services. Moreover, this project highlighted the power of building modular systems that function independently, akin to a microservice architecture. This approach allowed us to test each component separately and ensure that the system as a whole worked seamlessly. What’s next for FRED Looking ahead, we plan to refine the image transmission process and improve the accuracy and efficiency of our data processing. Our immediate goal is to ensure that image data is captioned with more technical details and that transmission is seamless and reliable, overcoming the constraints we faced during development. In the long term, we aim to connect FRED directly to local emergency departments, allowing us to test the system in real-world scenarios. By establishing communication channels between FRED and official emergency dispatch systems, we can ensure that our product delivers its intended value—saving lives in critical situations. <div