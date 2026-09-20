---
slug: "skytrace"
url: "https://devpost.com/software/skytrace"
title: "SkyTrace: Drone Detection and Localization in GPS-denied"
hackathon: "Google Cloud Vertex AI Agent Builder Hackathon"
organization: "Google"
winner: true
words: 476
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SkyTrace: Drone Detection and Localization in GPS-denied

> Imagine search and rescue missions in collapsed buildings or disaster zones where GPS is unavailable. Drones can be invaluable tools, but their effectiveness is hampered without location data.

[Devpost](https://devpost.com/software/skytrace) · hackathon [[Google Cloud Vertex AI Agent Builder Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[disaster_emergency]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** data, drone-fpv, gemini-experimental, github, google-cloud, imagery, inference, llm, maps, oss, other, radiant, real-world, sar

## Body

Inspiration 🌐 Imagine search and rescue missions in collapsed buildings or disaster zones where GPS is unavailable. Drones can be invaluable tools, but their effectiveness is hampered without location data. SkyTrace is a project that aims to leverage machine learning, specifically Google Cloud Platform's Vertex AI, to bridge this gap and enable drone tracking in GPS-denied environments using aerial footage. What it Does 🌍 SkyTrace utilizes Vertex AI's cutting-edge capabilities, particularly the Gemini family of models, to process aerial video captured by drones. By analyzing visual features within the video frames, the system aims to: Detect Drones: Identify the presence of drones within the video footage. Track Drone Movement: Monitor the movement of detected drones across consecutive video frames. Estimate Location: Employ machine learning models to predict the drone's approximate location based on the processed video data. How We Built It 🏗️ Data Collection: A crucial first step involves acquiring a diverse dataset of aerial videos featuring drones in various environments. Machine Learning Model Training: Vertex AI's Gemini models are trained on the curated video dataset, using labelled video frames with information about drone presence and location. Model Deployment: The trained model is deployed on Vertex AI, enabling real-time processing of aerial video streams captured by drones. Challenges We Ran Into ⚒️ Building a robust navigation system for challenging environments presented several hurdles: 1. Data Scarcity: Acquiring a comprehensive and diverse dataset of drone footage, particularly in challenging environments, can be a significant hurdle. 2. Occlusion and Ambiguity: Drones might be partially hidden by trees, buildings, or other objects in the video, making detection and localization difficult. 3. Computational Cost: Running real-time video processing on resource-constrained drones presents computational challenges. Accomplishments We're Proud Of 🏆 1. Proof of Concept: Successfully demonstrating the ability to detect and track drones in controlled environments using video analysis and machine learning. 2. Leveraging Vertex AI: Utilizing Vertex AI's powerful tools and infrastructure to expedite model development and deployment. 3. Potential Impact: Opening doors for the development of robust drone navigation and tracking systems in GPS-denied situations. What We Learned 🏫 The project highlighted the potential of machine learning for drone detection and localization. It also emphasized the importance of high-quality training data, efficient algorithms, and exploring techniques like transfer learning to address data limitations. What's Next for SkyTrace 🌐 1. Refining the Model: Further refining the machine learning model with a larger and more diverse dataset to improve accuracy and robustness in real-world scenarios. 2. Integration with Drone Systems: Exploring integration of SkyTrace with drone autopilots, enabling drones to leverage their location estimates for autonomous navigation. 3. Real-World Testing: Conducting field trials in controlled and eventually real-world GPS-denied environments to evaluate the system's effectiveness. By overcoming these challenges and building upon its initial success, SkyTrace has the potential to revolutionize drone operations in critical situations where GPS is unavailable. <div