---
slug: "project-horus-prejc4"
url: "https://devpost.com/software/project-horus-prejc4"
title: "Project Horus"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 485
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Project Horus

> Civilians accounted for 95% of all cluster munition casualties in 2022. We developed an autonomous system for detecting cluster munitions in post-war zones using a Parrot Drone and a custom CNN.

[Devpost](https://devpost.com/software/project-horus-prejc4) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]]
**substrate** [[structured_db]] [[video_visual]]

**stack** parrot, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for project horus

## Body

Inspiration Driven by the harrowing reality that civilians comprised a staggering 95% of all cluster munition casualties in 2022, we were impassioned to devise a solution that could confront this pressing humanitarian crisis head-on. With up to 40% of these munitions failing to explode upon impact, the threat to civilian lives persists long after conflict ceases. In regions like Laos, where between 1964 and 1973, 260 million cluster bomblets were dropped, and a chilling 80 million failed to detonate, the urgency of our mission became abundantly clear. Inspired by the imperative to safeguard innocent lives in post-war zones, we embarked on the development of Project Horus. What it does Project Horus utilizes cutting-edge technology to detect and localize unexploded cluster munitions in conflict-affected areas. Using a Parrot drone equipped with a custom-trained Convolutional Neural Network (CNN), our system autonomously scans vast territories, identifying potential threats. The drone's onboard Inertial Measurement Unit (IMU) aids in precisely localizing the detected munitions, even in electronic warfare or GPS-denied environments. Results are visualized in real-time as a heatmap, providing actionable insights to demining teams and enabling targeted removal of these deadly remnants of war. How we built it We started by creating a robust training dataset by printing out images of cluster munitions, placing them on the ground, and capturing a video to partition into frames. Our CNN, built using TensorFlow, achieved an impressive 98% validation accuracy after rigorous training. Integration with the Parrot drone involved deploying grid search algorithms to autonomously search for munitions, leveraging the drone's capabilities for real-time bomb detection. Overcoming challenges such as uploading custom assets into the simulator and optimizing the model to run efficiently on non-hardware accelerated systems, we created a streamlined solution ready for deployment in the field. Challenges we ran into Throughout the development process, we encountered several challenges, including difficulties uploading custom assets into the simulator and optimizing the CNN to run efficiently on hardware-constrained systems. Despite these hurdles, we adapted our approach, moving the computer vision processing off the drone and onto a separate system, ensuring our solution remained viable and effective. Accomplishments that we're proud of We're proud to have successfully implemented grid search and bomb-detection capabilities on the Parrot drone, as well as leveraging the IMU for precise localization of munitions. Additionally, visualizing the detection results in a heatmap provides actionable intelligence for demining teams, marking a significant achievement in our mission to save civilian lives. What's next for Project Horus Moving forward, we aim to enhance the robustness of our model by incorporating synthetic and real-world data for fine-tuning. Furthermore, we envision implementing multi-agent reinforcement learning techniques to enable collaborative scanning by fleets of drones, enhancing efficiency in covering large areas. Ultimately, we aspire to deploy Project Horus alongside demining teams in regions such as Ukraine, Israel, Afghanistan, and Southeast Asia, contributing to the safe removal of cluster munitions and the protection of civilian populations. <div