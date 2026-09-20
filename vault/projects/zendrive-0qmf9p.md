---
slug: "zendrive-0qmf9p"
url: "https://devpost.com/software/zendrive-0qmf9p"
title: "ZenDrive"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 621
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ZenDrive

> IoT and Google Maps Integrated Cognitive Fatigue Detection Using EMG Signals and Computer Vision.

[Devpost](https://devpost.com/software/zendrive-0qmf9p) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** arduino, artificial-intelligence, camera-module, cloudflare-for-hosting, exg-sensor, exg-sensor.-software-&-development:-computer-vision, fast-api, fastapi-for-backend, google-maps, javascript, machine-learning, mongodb, mongodb-for-database, opencv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zendrive

## Body

Inspiration As we look around us, day by day traffic accidents due to 'Driver Fatigue' is rising, statistics show that every year, about 20-30% of traffic accidents are caused by fatigue driving, 5% to 15% of accidents result in death. Traditional fatigue detection methods, like self-reporting and alertness tests, are often inaccurate and impractical in real time. Our solution made it possible by integrating Google Maps API and an Arduino based module that tracks for changes in driver’s bio-signal via EXG sensors. What it does Google Maps-Integrated Journey Tracking: The system uses Google Maps API to plot and monitor the entire driving route in real time, highlighting accident-prone zones as well as when the driver may feel fatigued based on the sleep data recorded and fed into our ML model. Pre-Drive Risk Assessment via Maps: Before starting a journey, the driver enters their sleep hours into the app or records it via in-app sleep recorder. This system powered by Google Maps data, estimates using our machine learning model, how long the driver can safely drive, considering real-time traffic density, terrain difficulty, and road history. Real-Time Driver Monitoring: Hardware like Raspberry Pi and Arduino operate in the background, tracking eye blinks, and yawns. The alerts are sent when these values exceed the threshold, Escalation via Geo-Fencing: If alerts are ignored, the system uses the driver’s GPS location from Google Maps to escalate the alert, notifying emergency contacts and local authorities near the current route. =>The Outcome: A Google Maps-powered neuro-alert system that prevents fatigue-related accidents by visualizing risk zones, integrating real-time drowsiness data, and guiding drivers safely through intelligent route planning. How we built it We integrated a range of hardware and software components to create a seamless, intelligent monitoring solution. On the hardware side we used a Raspberry Pi with a camera module to detect eye blinks, yawns, and head movements through computer vision techniques powered by OpenCV and TensorFlow, while an Arduino connected to an EXG sensor continuously monitored muscle contraction patterns (scalable to be added in the steering wheel to know if the driver loses grip for a prolonged and dangerous amount of time i.e. is feeling fatigue) to detect signs of fatigue. For the software backbone, we leveraged Scikit-Learn for drowsiness classification models and FastAPI to build a lightweight backend that efficiently connects all components. The mobile app, developed using React and JavaScript, provides users with a dynamic interface that integrates Google Maps for real-time journey tracking and displays alerts over the live route. We used MongoDB for user and trip data storage. Challenges we ran into The main problem we faced was with our EXG Pill. Due to lack of soldering in out chipset. The connection was not as secure as intended. This resulted in a lot more noise than intended. Another aspect of the problem came with our off-brand Arduino UNO clone, the main board connected to EMG sensors. This hardware refused to be connected most of the time and showed many issues regarding pushes the sketches to the architecture. We solved these problems with a mix of trail and error and research on the internet. Issue related to the arduino board came down a lot by installing drivers from its original manufacturer. Accomplishments that we're proud of One accomplishment we're particularly proud of is integrating real-time drowsiness detection with Google Maps by using the EXG muscle sensor and Arduino. The system analyzes muscle grip variability to detect fatigue, and when thresholds are crossed, it triggers dynamic alerts directly on the live Google Maps interface. These alerts mark the driver’s current location, highlight accident-prone zones ahead, and suggest nearby safe-stop areas, enabling context-aware navigation focused on driver safety. What we learned What's next for ZenDrive <div