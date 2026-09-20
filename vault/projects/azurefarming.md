---
slug: "azurefarming"
url: "https://devpost.com/software/azurefarming"
title: "AzureFarming"
hackathon: "Azure AI Developer Hackathon"
organization: "Microsoft"
winner: true
words: 727
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/housing_homeless"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AzureFarming

> 🌱 Virtual Smart Farm — Grow real crops remotely with a game-style interface!No home equipment needed—get guidance and care tips.Harvest via delivery or pickup—easy, fun, and automated!

[Devpost](https://devpost.com/software/azurefarming) · hackathon [[Azure AI Developer Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[housing_homeless]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]
  <sub>weak: document_pdf</sub>

**stack** azure, cosmosdb, css, hardware, micropython, mongodb, node.js, react, terraform

## How they structured the write-up

- inspiration
- what it does
- tech stack
- challenges
- accomplishments
- what we learned
- what's next
- 📄 additional reference documents
- 🎥 iot virtual simulation demos

## Body

User Scenario Concept Art Project Overview Pitch 1 Pitch 2 Pitch 3 Pitch 4 Overall Service Architecture with IoT BackEnd Azure Architecture Main Dashboard (Example) Webpage layout 1 Webpage layout 2 Webpage layout 3 Details - Github Copliot Use Github Copliot Usage Examples Details - Azure AI Use & Plans 🌱 AzureFarming: Virtual Smart Farm Inspiration Smart farming today falls into two extremes: 🏠 Home IoT kits – costly and impractical for casual users 🌾 Industrial farms – built for large-scale professionals AzureFarming makes real farming accessible by combining IoT, AI, and gamification into a platform for everyone. What It Does AzureFarming is a virtual farming platform that allows users to remotely manage real crops in a rental smart farm unit . Key Features 📡 Monitor plants in real time via IoT sensors 🎭 Animated plant avatars show status and emotions 📋 Receive personalized tips from an AI care guide 🛠️ Remotely control watering, fertilization, and lighting 🎖️ Complete tasks to earn points and unlock rewards 🚚 Choose harvest delivery or on-site pickup (not implemented) Tech Stack Component Technology Frontend React, Tailwind CSS, DaisyUI Backend Node.js, Azure Functions IoT Connectivity ESP32 + MicroPython, MQTT, Azure IoT Hub Cloud & Storage Azure CosmosDB, Device Twin, Terraform Simulation Wokwi (virtual circuit simulator), Proteus 8 (PCB Validation) Challenges ⚙️ Hardware bottlenecks due to remote collaboration and limited access 🔄 Slow iterations with C++ , improved by switching to MicroPython ☁️ Adapting to Azure IoT services — implemented IoT Hub, Event Hub, and Functions 📦 Balancing between 3D prototype design and real circuit building. ⏳ Time limits led to virtual testing over physical deployment Accomplishments 🔗 Built a complete IoT-to-Cloud pipeline with MQTT and Azure IoT Hub ⚙️ Deployed serverless APIs on Azure Functions for IoT backend API. 🚀 Developed modular MicroPython firmware for ESP32 🌐 Created a React-based frontend app for IoT integration ☁️ Connected server logic to Azure IoT services for real-time device updates 🔧 Provisioned and deployed Node.js backend using Terraform on Azure 🧪 Simulated and validated devices using Wokwi virtual circuits 🎨 Designed an interactive plant care system with gamified UI/UX What We Learned MicroPython enables fast, flexible IoT development Azure's IoT architecture is powerful for real-time cloud integration Virtual simulation tools were key for remote hardware projects Learned to align gamification with user experience and service strategy What's Next 🤖 Add AI-powered automation for plant care with Camera support. 🌱 Expand avatar expressions and growth animations 🧩 Build admin tools for crop species tracking 📦 Finalize real-world hardware enclosure designs ⏰ Sync farming tasks with user calendars 🔗 Connect full backend API to live device control ✔️ How GitHub Copilot is Used in This Project GitHub Copilot in VSCode significantly accelerated frontend development by: Generating responsive React templates. Standardizing API structures and handlers. Optimizing layouts based on design references. Building reusable, parameterized UI components. It enhanced multi-file context awareness, enabled precise targeted edits, and reduced development time while maintaining UI consistency. (Related Image: Copilot-assisted code generation process and component standardization examples are attached.) ✔️ How Azure AI is Used in This Project A custom machine-learning based AI model predicts optimal light levels based on healthy-condition sensor data. The model will be deployed to Azure AI Studio and integrated with the IoT Function App through a Private API Gateway. IoT devices (ESP32) already automate Ring-LED lighting based on server-assigned C2D MQTT messages. Full AI API deployment and Azure integration are in progress as of April 4. OpenAI-based chatbot features are actively considered for future expansion. (Related Image: Azure AI Studio-based deployment plan, IoT-AI integration flow are attached.) ✔️ Azure Service Architecture Component Purpose Azure IoT Hub MQTT communication hub for D2C/C2D messaging with IoT devices. Azure Function App Processes IoT data and (planned) calls the AI model through a private gateway. Azure Cosmos DB Stores real-time sensor data and historical environment records. Azure AI Studio (Planned) Hosts and serves the predictive model for light control. Azure App Service Provides public APIs for frontend communication (React/Vite). Private API Gateway (Planned) Secures internal communication between Function Apps and AI services. Note: All Azure resources are managed and provisioned through Terraform scripts. 📄 Additional Reference Documents Web Page Composition (Shared) API Specification (Shared) Azure IoT Smart Farm System Documentation (Shared) Condition-Based Recommendation System (Shared) 🎥 IoT Virtual Simulation Demos Actuator Control Demo (C2D Command) Sensor Read & Actions Demo <div