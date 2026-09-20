---
slug: "nurture-f5ht8x"
url: "https://devpost.com/software/nurture-f5ht8x"
title: "Nurture Ecopod"
hackathon: "MoonHacks By Moon Corp"
organization: "MoonCorp"
winner: true
words: 809
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Nurture Ecopod

> Nurture ecopod is an innovative agrotech solution that uses ML models and IOT devices to manage, maintain, and monitor plant, crop, and soil health, thus, improving produce yield and quality.

[Devpost](https://devpost.com/software/nurture-f5ht8x) · hackathon [[MoonHacks By Moon Corp]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[agriculture_food]] [[health_clinical]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, c#, esp, firebase, flutter, iot, python, react, scss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nurture ecopod

## Body

Team working over meet Ecopod design Ecopod demo Ecopod working Mobile App create task page demo Mobile app create post page demo Mobile app home page Inspiration Urbanization has drastically changed agriculture by reducing available land and distancing consumers from nature. This shift has left many newbie gardeners or plant enthusiasts with limited knowledge and resources for urban gardening. Ecopod offers real-time monitoring and personalized care recommendations, making gardening easy for urbanites regardless of their experience with plants. With EcoPod's guidance and Nurture's insights, users can cultivate thriving gardens at home, even in tight spaces and busy schedules. In urban life, where time and space are scarce, EcoPod and Nurture become essential tools for reconnecting with nature, growing fresh produce, and fostering a healthier environment. What it does It provides community support, Gemini chatbot integration, a crop recommendation model, platform-independent application support, and an IoT device. The IoT device fetches and analyzes data in real-time and monitors for any irregularities in temperature, moisture, and humidity readings. In case of any irregularity, the user receives a notification to check their plants. It also reminds users to water their plants and take optimal care of them. The app and webpage contain all information regarding any plants like their optimal temperature, moisture, humidity, soil NPK, diseases that can affect the plant, and how to cure those diseases. How we built it We built Ecopods in multiple phases, simultaneously designing the application and configuring DTH and Soil Moisture Sensors with our Node MCU (ISP 8266). Concurrently, we developed an ML model to recommend crops based on NPK values, humidity, rainfall, and temperature. On the IoT side, we configured it with Firebase to send real-time updates from the sensors through the microcontroller to the real-time database in Firebase. Ecopod suggests actions such as watering plants and provides other recommendations for plant care. Our application, based on Flutter, serves as the central point of the ecosystem. It connects with Ecopod, offers chatbot support with Gemini, and can predict crops suitable for specific NPK values, humidity, rainfall, and temperature. Our application will have a community support page tailored for interaction with other Ecopod users. It includes daily task tracking, plant care streaks that encourage users to care for plants every day, and pop-up reminders about watering plants, adding manure, and high temperatures, among other things. We have endeavored to build an ecosystem in the hackathon by combining IoT sensors, AI, and app and web development. Challenges we ran into We ran into multiple challenges related to: Dependencies and version mismatches in developing ML models Inaccuracy of ML models Improper configuration of hardware sensors to give readings Frontend not able to fetch data from Backend APIs Microcontrollers and Frontend not able to connect with Firebase Real-Time Database Accomplishments that we're proud of We're proud of the progress we have made during the duration of the hackathon. Initially, we only thought of how we were going to build an ecosystem around plant care, combining multiple domains to solve a noble cause, trying to evolve nature with the help of modern ideas and technology. Finally, we developed a functional solution that empowers users to cultivate thriving gardens in urban environments. We misunderstood the complexity in the beginning and feared implementing our idea, but in the end, what we can say is all you need is a little push, four hardworking teammates, and all challenges will disappear. What we learned We have learned a lot in this hackathon, in terms of being able to work on multiple tech stacks and being an effective team with proper communication to finish tasks on time or before time. In terms of tech stacks, we were able to learn: Arduino programming in C++ for managing the sensors Integrating Node MCU with Firebase for sending real-time data about temperature, soil moisture Integrating ML models with Flutter What's next for Nurture Ecopod Enhanced Crop Recommendation Model: Continuously refine and improve the ML model for crop recommendations by incorporating more data points, refining algorithms, and adding new features to increase accuracy and relevance. Expansion of Plant Database: Expand the database of plant information to include a wider variety of plants, along with detailed care instructions, optimal growing conditions, and common issues faced by each plant species. Integration of Image Recognition: Implement image recognition technology to allow users to easily identify plant species and diagnose common plant diseases simply by taking a photo using the Ecopod app. Advanced IoT Features: Introduce advanced IoT features such as automated nutrient dosing systems, smart lighting controls, and environmental controls to further optimize plant growth and health. User Feedback and Iterative Improvements: Continuously gather feedback from users to identify pain points, areas for improvement, and new features or functionalities desired by the community. Use this feedback to iteratively enhance the Ecopod platform and ensure it remains relevant and valuable to users. <div