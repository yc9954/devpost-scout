---
slug: "fall-detection-with-a-gyro-sensor"
url: "https://devpost.com/software/fall-detection-with-a-gyro-sensor"
title: "Fall detection with a gyro sensor"
hackathon: "InnovateHacks 2.0"
organization: "Dublin Hack Club"
winner: true
words: 370
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# Fall detection with a gyro sensor

> One of the most common injuries is a simple Fall. While sounding simple, this can be a huge concern for older and younger humans. With our AI driven device we can detect falls and take needed actions.

[Devpost](https://devpost.com/software/fall-detection-with-a-gyro-sensor) · hackathon [[InnovateHacks 2.0]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[elder_child_care]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** cnn, lstm, optuna, python, tkinter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for fall detection with a gyro sensor

## Body

confusion matrix Model_stats gyro sensor Set up of the gyro sensor Inspiration As avid skiers, we’ve witnessed the dangers of backcountry skiing where falls can leave skiers injured and unable to get help in time. Friends might not notice a fall, leading to tragic outcomes. This inspired us to create a solution that alerts first responders when someone remains down after a heavy fall. Beyond skiing, this device has potential everyday applications, such as assisting elderly individuals living alone by notifying caregivers or family when a fall occurs. What it does Our AI processes gyro sensor data to detect falls with high accuracy. It identifies when a fall occurs and distinguishes it from regular movement. Additionally, the user interface allows manual entry of gyro sensor values to simulate and test the fall detection system in real-time. How we built it We developed a neural network combining CNN and LSTM layers, enhanced by an attention mechanism for accurate fall detection. The data is preprocessed through scaling, smoothing, and segmentation into rolling windows. The model was fine-tuned using hyperparameter optimization with Optuna. The user interface was built with Python’s Tkinter library to allow interaction with the system. Challenges we ran into Reducing false negatives, where actual falls were misclassified as non-falls. Preparing and preprocessing realistic data to match real-world scenarios. Integrating a user-friendly interface with backend AI predictions. Ensuring scalability for future deployment on microcomputers like Raspberry Pi. ## Accomplishments that we're proud of Successfully developed a robust AI model capable of detecting falls with high precision and recall. Created a functional and user-friendly UI for testing and demonstrating the system. Extended the system's potential beyond skiing to everyday use cases, such as elderly care. What we learned Data quality and preprocessing in training machine learning models. Balancing simplicity and functionality in user interface design. Exploring real-world applications of AI and addressing edge cases. What's next for Fall detection with a gyro sensor Hardware Integration: Deploy the system on microcomputers like Raspberry Pi for real-world testing. Real-Time Monitoring: Enable live data collection and prediction from wearable devices. Enhanced Features: Add GPS tracking and alert systems for emergencies. Broader Applications: Expand use cases to include extreme sports, workplace safety, and healthcare monitoring. <div