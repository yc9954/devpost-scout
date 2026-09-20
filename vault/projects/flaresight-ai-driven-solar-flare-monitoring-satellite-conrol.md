---
slug: "flaresight-ai-driven-solar-flare-monitoring-satellite-conrol"
url: "https://devpost.com/software/flaresight-ai-driven-solar-flare-monitoring-satellite-conrol"
title: "FlareSight:AI-Driven Solar Flare Monitoring&Satellite Conrol"
hackathon: "AmpliCode Hackathon 2025"
organization: "AmpliCode"
winner: true
words: 806
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# FlareSight:AI-Driven Solar Flare Monitoring&Satellite Conrol

> Our AI system uses two CNN models—Continuum (optical) and Magnetogram (magnetic)—to forecast space weather. Using API data, it predicts risks early, triggering satellite panels to close during threats

[Devpost](https://devpost.com/software/flaresight-ai-driven-solar-flare-monitoring-satellite-conrol) · hackathon [[AmpliCode Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[climate_energy]]
**user** [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** gradio, json, jupyter, keras, lego, mindstorms, nasa, noaa, numpy, pybricks, python, sdo, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flaresight ai

## Body

How Does It Work? Flow Diagram FlareSight AI: AI-Based Autonomous Satellite Defense System Inspiration The inspiration for FlareSight AI originated from the critical need to protect satellite systems and technological infrastructure from the unpredictable impacts of solar flares and coronal mass ejections (CMEs) . As solar activity follows an 11-year cycle and with the upcoming Solar Maximum in 2025 , the frequency and intensity of solar storms are expected to peak. These solar events can severely disrupt communication networks , GPS systems , energy grids , and satellite operations . Recognizing this global threat, we aimed to develop an AI-powered autonomous defense system capable of early solar flare detection and real-time satellite protection without human intervention. What it does FlareSight AI is an AI-driven system that forecasts space weather and protects satellites from the damaging effects of solar flares. It integrates two advanced Convolutional Neural Network (CNN) models trained to classify solar activity based on different data sources: Continuum Model – Analyzes optical images of the Sun’s surface to detect sunspots and predict solar activity. Magnetogram Model – Processes magnetic field data to assess the complexity of sunspots and predict the likelihood of solar flares. Using real-time data from APIs ( NASA’s Solar Dynamics Observatory and NOAA ), the system continuously monitors solar activity. When a high-risk event is detected, the AI autonomously triggers defensive actions such as closing satellite solar panels to prevent damage. Key Features Real-time space weather forecasting Autonomous decision-making without human intervention Integration with LEGO Mindstorms for satellite behavior simulation Gradio-powered user interface for model interaction and data visualization How we built it Data Collection Utilized the Solar Storm Recognition Dataset from NASA , containing over 20,000 images including continuum and magnetogram data. Labeled the data into Alpha (low risk) and Beta (high risk) categories. AI Model Development Developed two 20-layer CNN models : Continuum Model achieved 93% accuracy . Magnetogram Model achieved 91% accuracy . Implemented masking algorithms to clean irrelevant data and improve prediction precision. API Integration Integrated real-time data from: NASA’s SDO for solar imaging (continuum & magnetogram). NOAA’s API for geomagnetic activity data ( Kp index ). Interface Design Created a user-friendly interface using Gradio to display real-time predictions and visual data for end-users. Satellite Simulation Built a LEGO-based satellite model using LEGO Mindstorms and programmed it with Pybricks . Simulated defensive behaviors, such as automatic solar panel closure during high-risk solar flare events. Challenges we ran into Model Accuracy Issues: Initial 9-layer CNNs achieved only 67% accuracy . We expanded the model to 20 layers and applied masking algorithms to enhance performance. Real-Time Data Processing: Integrating real-time solar data through APIs required extensive data formatting and handling to ensure system stability and reliability. Satellite Integration: Creating a functional simulation of satellite behavior using LEGO Mindstorms required complex coding and hardware testing to ensure smooth integration with the AI models. Kp Index Correlation: Establishing a reliable correlation between AI predictions and the geomagnetic activity measured by the Kp index was challenging but essential for model validation. Accomplishments that we're proud of Developed two high-accuracy CNN models ( 93% and 91% ). Successfully integrated real-time solar data into the prediction pipeline. Created a fully autonomous simulation where the satellite reacts to AI predictions in real time. Designed an intuitive user interface for data visualization and interaction. Pioneered the use of both continuum and magnetogram data combined with geomagnetic indices for enhanced prediction accuracy. What we learned Space Weather Dynamics: Gained a deep understanding of solar flares, CMEs, sunspots, and their impacts on Earth's technological systems. AI in Astronomy: Enhanced skills in CNN design and optimization, especially in the context of astronomical data analysis. API Integration: Learned how to integrate multiple data sources in real time, ensuring the AI system continuously updates its predictions. Robotics and Simulation: Acquired hands-on experience in using LEGO Mindstorms and Pybricks for hardware simulation of satellite behaviors. The Importance of Solar Cycles: The upcoming Solar Maximum in 2025 highlights the urgency for systems like FlareSight AI , as solar activity will peak, increasing the risk to satellites and technological infrastructure. What's next for FlareSight AI Data Expansion: Incorporate additional data sources, such as coronal mass ejections (CME) data, to enhance prediction capabilities. Algorithm Optimization: Apply advanced AI techniques like transfer learning and reinforcement learning to improve model adaptability and accuracy. CubeSat Integration: Adapt the system for deployment on CubeSats using Arduino , enabling real-space testing of FlareSight AI in future missions. Cloud-Based Platform: Develop a cloud-accessible platform for global users, including space agencies, telecommunication companies, and researchers. Commercial Partnerships: Establish collaborations with industries most affected by space weather, such as aerospace , telecommunications , and energy sectors . Educational Outreach: Utilize FlareSight AI as a tool for STEM education , promoting AI applications in space sciences and fostering the next generation of space researchers. <div