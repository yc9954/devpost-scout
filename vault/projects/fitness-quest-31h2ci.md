---
slug: "fitness-quest-31h2ci"
url: "https://devpost.com/software/fitness-quest-31h2ci"
title: "FitQuest"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 1064
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/mental_health"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# FitQuest

> FitQuest is an AI-powered fitness game that makes workouts fun, blending: AI Coach, Nutritionist AI, Real-Time Form Analysis, and RPG Progression. Level up your body, not just your character!

[Devpost](https://devpost.com/software/fitness-quest-31h2ci) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[mental_health]] [[transportation]]
  <sub>weak: researcher</sub>
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, express.js, figma, gemini, gimp, git, html, javascript, mediapipe, mongodb, node.js, railway, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitness quest

## Body

Home Page #1 Character pedestal Level Up Badge Quest Board Login tracker 365 About us Meet the team Profile #1 Profile #2 AI Form #1 AI Form Tracker Exercise Scientist PHD Gemini Chatbot Nutritionist Gemini Chatbot Motivational Trainer Gemini Chatbot Workout Dashboard Add Workout Social Hub Inspiration With a combined interest in fitness and AI, we decided to build a web application that would encourage Gen Z to approach their health and fitness differently. Recognizing June as Men's Mental Health Awareness Month, we wanted to emphasize how important physical fitness is to overall well-being while incorporating gaming, a hobby dear to people of all backgrounds. We noticed that traditional fitness apps often feel like chores, so we asked ourselves: what if working out felt more like playing your favorite RPG? This question sparked the creation of FitQuest, where we set out to transform fitness from an obligation into an adventure by combining cutting-edge AI technology with the engaging progression systems that make games so addictive. What it does FitQuest is a full-stack web application built with the MERN stack and hosted via Railway, utilizing the Gemini API to provide users with three specialized AI coaches covering nutrition, motivation, and exercise science. The platform features live form feedback powered by MediaPipe for exercises like squats and pushups, ensuring proper technique and safety. Real-time workout logging stores all user data in MongoDB, while an integrated XP system rewards users with experience points for each logged exercise. Players can choose from six unique characters and unlock skin customizations as they level up. The application also includes social features that allow users to connect with other members and compare stats, adding an extra layer of motivation through friendly competition. How we built it We chose the MERN stack for this project to compete for the MLH MongoDB prize tracks while leveraging React's capabilities to create an engaging UI that perfectly complements our RPG-themed design. Our implementation of the Gemini API powers three specialized chatbot trainers, each with intelligent filtering to keep conversations focused on their respective domains; nutrition, motivation, or exercise science. When users attempt to stray from these topics, the coaches redirect them back to relevant fitness discussions. We deployed the entire platform through Railway, which streamlined our process by hosting both frontend and backend from a single deployment point. React's component architecture enabled us to enhance the user experience using libraries like Lucide-React for icons and Framer Motion for smooth animations, creating immersive background imagery and dynamic glowing effects. The color scheme of purple and gold pays homage to our home institution, Wilfrid Laurier University. Challenges we ran into The MediaPipe implementation proved to be our most challenging technical hurdle. While other aspects of the project followed standard MERN stack protocols, we encountered significant difficulties when integrating our character system and ensuring our AI coaches remained focused on their specialized topics through effective conversation filtering. Time constraints added another layer of complexity—we finalized our concept just two hours after the 10 PM Friday kickoff and maintained an intense development pace with minimal rest. With numerous routes and pages to implement across the application, the tight timeline made it particularly challenging to ensure seamless integration and smooth user flow between components. We addressed these challenges by strategically dividing work based on our individual strengths and prioritizing the most complex features first. Emaad leveraged his MERN stack and full-stack development expertise to establish the core architecture and RPG-themed design foundation. Sebastian utilized his UI and AI experience to implement the Gemini API wrapper, design custom characters, and contribute to the live form validation system. Ahmad took ownership of the MediaPipe feature development, drawing on his AI and full-stack background, then transitioned to ensuring cohesive integration across all application components. The collaboration and chemistry amongst our group, the Algorithm Athletes, is the sole reason we were able to succeed in this 36 hour sprint. Accomplishments that we're proud of As a team, we are particularly proud of our UI design and character implementation, which seamlessly aligns with the RPG theme we envisioned from the start. The live form validator powered by MediaPipe and our custom AI coaches through Gemini API wrappers truly brought personality to the project, making the development process both engaging and collaborative as we bounced ideas off each other. The sprite designs and diverse skin customization options perfectly complement our RPG aesthetic, while our purple and gold color scheme proudly represents our home institution, Wilfrid Laurier University. Above all, we're most satisfied with how closely we adhered to the initial gameplan and architecture we established Friday night. In today's software engineering landscape, where AI is rapidly transforming development practices, we recognized the critical importance of understanding fundamental development principles and maintaining a solid architectural foundation throughout the entire project lifecycle. What we learned As a team, we entered this project with relatively similar skill sets, which we believe contributed significantly to our collaborative success. Sebastian's expertise in version control proved invaluable in standardizing our workflow and maintaining code quality throughout development. Individually, we all gained substantial knowledge about React's capabilities for UI customization and frontend development. We also discovered the nuanced power of AI in code generation; while not always reliable, it proved incredibly effective for rapid prototyping and idea execution under tight deadlines, particularly when combined with thorough research and understanding of the underlying technologies. Our collective knowledge of the MERN stack deepened considerably as we implemented MongoDB for user authentication, workout database logging, and activity tracking systems. Additionally, we enhanced our understanding of Git version control and developed stronger skills in collaborative development, learning to work effectively on shared projects and sometimes even the same files simultaneously. What's next for Fitness Quest We plan to expand this project by integrating Kaggle health datasets to deliver more accurate, AI-personalized workout recommendations and health advice. The comprehensive user data we've collected regarding general health and lifestyle metrics will enable our AI models to provide better predictions and forecasting on an individual basis. While we initially wanted to implement a dedicated machine learning model alongside our AI features, time constraints led us to prioritize this enhancement for future development cycles. Additionally, we're excited about the prospect of transforming FitQuest into a mobile application using React Native and Flutter, allowing us to reach users across both Android and iOS platforms and provide a more accessible fitness experience. <div