---
slug: "fitfeed"
url: "https://devpost.com/software/fitfeed"
title: "FitFeed"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 484
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/agriculture_food"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# FitFeed

> Fuel your victory: Elevate performance with AI-crafted nutrition meal plans

[Devpost](https://devpost.com/software/fitfeed) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[agriculture_food]]
**substrate** [[code_repository]] [[video_visual]]

**stack** express.js, figma, node.js, openai, react.js, supabase

## How they structured the write-up

- inspiration 💡
- what it does 🍽️
- how we built it 🛠️
- challenges we ran into 🚧
- accomplishments that we're proud of 🏆
- what we learned 📚
- what's next for fitfeed 🌟

## Body

Inspiration 💡 Nutrition plays a critical role in athletes' sports performance and injury recovery. Observing the struggle of maintaining consistent, optimized meal plans and nutrition led us to develop the “FitFeed”. This app leverages the power of GPT-3 and GPT-4 vision technology to provide personalized, easy-to-follow nutrition plans, based on the ingredients in athletes' fridge itself. The AI generated meal suggestion would be verified from nutrition specialists before recommending it to the athletes. What it does 🍽️ The “FitFeed” app offers a comprehensive solution for athletes to manage their nutrition based on their specific sport, physical attributes, and dietary preferences. Utilizing GPT-3, it generates personalized meal plans, while GPT-4 vision assists in identifying ingredients from refrigerator, estimating portion sizes, and suggesting meals accordingly. Athletes can track their adherence to the plan and earn rewards, whereas coaches can monitor their team’s progress, send reminders, and facilitate communication. How we built it 🛠️ We initiated the project with a clear vision of the features essential for athletes and coaches. Our development journey encompassed: Brainstorming functionalities to include in the app Designing interactive questionnaires for personalized user profiles. Developing app design in Figma Integrating GPT-3 for generating dynamic meal plans. Employing GPT-4 vision for ingredient recognition and meal suggestions. Developing a robust platform for coach-athlete interaction and progress tracking. The app is built with a React frontend for a responsive user experience and a Node.js backend for API integration. Challenges we ran into 🚧 Since we decided to build a functional prototype, we committed to creating a realistic experience for the athlete. The athlete signup questionnaire took some time to get right, and we went through a couple of different versions before figuring out a way to dynamically generate the questions given data from the backend. We also had some trouble saving base64-encoded images on Supabase, until we discovered that the metadata had to be removed prior to storing the base64 string for Supabase to recognize the content as an image file. Accomplishments that we're proud of 🏆 We are proud of creating a fully functional prototype that not only meets the nutritional needs of athletes but also enhances the coaching process. The integration of cutting-edge AI technology to provide real-time, personalized nutrition advice stands out as our key achievement. What we learned 📚 Our biggest findings were: Building a fully-functional prototype is challenging and can be made easier by using pre-built UI components such as Material UI Deployment issues can be challenging to debug quickly How to create effective prompts for both OpenAI GPT3 and GPT4V models to write customized meal plans and recognize items visible in an image (while leaving out extraneous details that the models often provide) What's next for FitFeed 🌟 We would like AI algorithms for more accurate meal suggestions, enhancing the social functionality for broader community engagement, and expanding the app’s capabilities to cater to various sports and dietary needs. <div