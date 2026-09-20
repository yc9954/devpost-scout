---
slug: "heartstart"
url: "https://devpost.com/software/heartstart"
title: "HeartStart"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1607
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# HeartStart

> Emergency Detection. Autonomous Robot CPR.

[Devpost](https://devpost.com/software/heartstart) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[disaster_emergency]] [[health_clinical]]
**user** [[frontline_worker]] [[legal_professional]] [[patient_family]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** arduino, c, cad, css, html, javascript, opencv, python, ros2, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- the sensing system
- the vision system
- the user interface
- the cpr mechanism
- challenges we ran into
- single-camera depth perception
- system integration
- hardware
- accomplishments that we're proud of
- what we learned
- what's next for heartstart
- multi-room navigation
- continuous patient tracking
- enhanced medical capabilities
- integration with emergency systems

## Body

Inspiration Every year, more than 350,000 people in the US experience cardiac arrest outside of a hospital setting. The difference between life and death often comes down to those critical minutes before emergency services arrive—minutes where CPR must be performed continuously, consistently, and correctly. But bystanders freeze, panic, or simply don't know how to administer CPR properly. First responders face impossible response times. And even trained individuals grow fatigued, their compressions becoming shallow and ineffective after just two minutes. In fact, according to the American Heart Association, the survival rate drops by 7–10% for every minute without CPR. After just 10 minutes, survival is nearly zero. Yet the average EMS response time in the United States is over 7 minutes in urban areas—and much longer in rural communities. We asked ourselves: what if a robot could be there instantly? What if a device never tires, never panics, and never forgets the rhythm? What if we could build a guardian that watches over loved ones and acts the moment their heart stops? That's why we built HeartStart—a name that captures both the urgency of cardiac response and the promise of a new beginning. An autonomous CPR robot that monitors a patient's heart, detects cardiac arrest within seconds, navigates to their location, and delivers consistent, high-quality chest compressions until help arrives. Immediate CPR can double or triple the chance of survival, and that is the impact we hope to deliver to society. What it does HeartStart is an autonomous mobile robot that continuously monitors a patient's heart rate via a wearable heart-rate sensor. When cardiac arrest occurs, HeartStart springs into action: 1) Immediate Alert: The system triggers an API call via Twilio, notifying emergency services with a custom message: "Cardiac arrest detected at [location]. Autonomous CPR robot is on-site and administering aid." (For our demo, we routed this to a friend's phone rather than actual 911.) 2) Autonomous Navigation: The robot navigates toward the patient using computer vision, tracking their body position and using depth sensing to approach safely. Once within range, it locks onto an AprilTag placed on the patient's chest for precise positioning. 3) Precision CPR: After positioning itself directly above the chest, HeartStart deploys its CPR mechanism to deliver consistent, high-quality chest compressions at the correct depth and rate—never tiring, never losing rhythm. 4) Real-Time Monitoring: Throughout the process, the robot's onboard display shows the patient's heart rate, IR signal, and medical history, keeping any human responders informed the moment they arrive. How we built it The Sensing System We used a sensor worn by the patient to continuously monitor heart activity. For our hackathon demo, we connected this sensor to an Arduino, which fed data via serial monitor to a laptop. Using PySerial, we streamed this data in real-time to a web application that displays the patient's heart rate and IR signal. Our ultimate aim is full wireless real-time data transfer, but this wired solution gave us the reliability needed for a working prototype. The Vision System The robot navigates using Arducam cameras and a depth-based computer vision pipeline built with ROS2. The process has two phases: Approach Phase: The robot tracks the patient's full body, maintaining a frame of reference to navigate toward them safely. By projecting the subject's bounding box onto the camera's image plane, we mapped their position to directional commands sent to the Raspberry Pi. The robot's speed was set proportional to log(r), where r is the ratio of bounding box area to total frame area, allowing faster approach when the subject was far away and gradual slowing as the robot drew near. Positioning Phase: Once closer, the robot detects an AprilTag placed on the patient's chest and switches to fine-tuned positioning, stopping precisely when correctly aligned above the sternum. The Control System Data flows from the laptop (running the monitoring and vision processing) to the Raspberry Pi onboard the robot. When the flatline trigger activates, the Pi receives the command and initiates navigation. After positioning is confirmed, the Pi activates the CPR mechanism. The User Interface We built a clean, informative web app using HTML and Python that displays: Real-time heart rate and IR signal Patient health history (accessible to responders) A custom 3D heart animation designed in Blender, which pulses with each detected heartbeat—making the interface both informative and approachable. The CPR Mechanism We manipulated cranker shaft to create linear motion from rotational motion in a highly cost-efficient way. 3D printed using PLA. Challenges we ran into Single-Camera Depth Perception Our most technically challenging problem was extracting depth information from a single Arducam. Without stereo vision or a LIDAR sensor, we had to estimate distance using only one camera. Getting the robot to accurately judge how far away the patient was proved unsurprisingly difficult. We experimented with ground plane estimation and size-based distance calculations, but each approach had limitations. In the end, we decided to treat the subject's location box as a projection of the frame of reference for the middle of the camera, and then use these mappings to send directions to the Raspberry Pi. The AprilTag solution worked well for final positioning, but first we needed to get within range to detect it. Calibrating the camera for reliable measurements took many iterations. System Integration The biggest challenge was getting all the components to work together reliably. The Arduino communicated with the laptop over serial, the laptop ran Python scripts to update the web interface and send commands to the Raspberry Pi, and the Pi ran ROS2 nodes for vision processing and motor control. Every part needed to stay synchronized. When something failed, debugging meant tracing through multiple systems written in different languages. We learned to implement comprehensive logging at every stage and to test components both individually and as a complete system. There were many late nights spent tracking down why the vision system would work perfectly in isolation but fail when connected to the motor controllers. Hardware Hardware was hard... especially with handling some soldered joints... Accomplishments that we're proud of We're incredibly proud of the technical foundation we built for HeartStart. On the sensing side, we integrated a BLE wearable sensor with an Arduino, streaming real-time heart rate data over serial. Using PySerial, we piped that data into a Python backend that continuously monitored for flatline conditions. The moment the signal crossed the 15-second threshold of flat line, our system triggered an automated Twilio API call, closing the loop from physiological event to emergency notification. For the web interface, we built a clean, informative dashboard using HTML and Python. It displays live heart rate, IR signal, and patient health history, all updating in real-time as data streams in. But the highlight is the custom 3D heart animation we designed in Blender, which pulses with each detected heartbeat. It turns a clinical monitoring screen into something more approachable and human. We built the entire navigation system on ROS2, using Arducams for vision and depth estimation. Getting the robot to track a person, approach them safely, and then lock onto an AprilTag for precise positioning required integrating computer vision, coordinate transforms, and motor control into a single coherent pipeline. The two-stage approach—full body tracking for approach, AprilTag for fine positioning—was something we figured out through experimentation. On the communication side, we established a reliable data pipeline from the laptop (running monitoring and vision) to the Raspberry Pi (controlling the robot). When the flatline trigger activates, commands flow through this pipeline to start navigation, and later to deploy the CPR mechanism. What makes us proudest is not a single component, but that the system flows smoothly. The Arduino talks to Python, Python talks to the web interface and the Pi, the Pi runs ROS2 nodes that process camera data and drive motors, and every piece stays synchronized enough to respond to a life-threatening event in real-time. Building a fully functional autonomous system feels like a genuine accomplishment. What we learned This project taught us the enormous gap between a concept and a working physical system. Software can be debugged with print statements; hardware requires patience, calibration, and often a complete rethink of assumptions. We also deepened our skills in ROS2, computer vision, and embedded systems. The biggest lesson was ultimately about impact. Medical technology isn't just about clever algorithms; it's about reliability, safety, and trust. A CPR robot that fails is not just a bug, but a life that could have been saved. That responsibility shaped every decision we made. What's next for HeartStart Multi-Room Navigation Currently, HeartStart assumes the patient is in the same room. Our next major goal is enabling true multi-room navigation using SLAM (Simultaneous Localization and Mapping), allowing the robot to monitor and respond to a patient anywhere in the home, like through doorways, around furniture, and across different spaces. Continuous Patient Tracking Rather than waiting for a flatline to locate the patient, we want HeartStart to maintain awareness of the patient's position at all times. This means integrating additional BLE beacons for coarse location tracking and using the robot's cameras to periodically update and remember where the patient is throughout the day. Enhanced Medical Capabilities CPR is just the beginning. We envision expanding HeartStart into a more comprehensive emergency response platform with integrated AED defibrillation, oxygen delivery, and additional vital sign monitoring like blood oxygen and respiratory rate, whilst maintaining the same autonomous response capabilities. Integration with Emergency Systems HeartStart could also work with smart home systems to trigger lights and unlock doors for arriving EMS, whilst also building telemedicine capabilities that give dispatchers and first responders real-time patient data, video feeds, and a complete log of events before they even arrive. <div