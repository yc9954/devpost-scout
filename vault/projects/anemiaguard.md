---
slug: "anemiaguard"
url: "https://devpost.com/software/anemiaguard"
title: "AnemiaGuard"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 767
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AnemiaGuard

> Turning smartphones into early allies against childhood anemia.

[Devpost](https://devpost.com/software/anemiaguard) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[agriculture_food]] [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** android-studio, capacitor, figma, github, javascript, kaggle, python, react, tensorflow, typescript, visual-studio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for anemiaguard

## Body

Inspiration Anemia remains a critical public health problem in Peru and many regions of South America and Africa, especially in rural and low-resource communities. In many cases, anemia goes unnoticed until its effects on child development are already significant. We were inspired by the urgent need to provide families with accessible tools that support early risk identification, treatment adherence, and smart, evidence-based nutrition. Our goal was to empower patients and caregivers using resources they already have, such as smartphones, to foster prevention and awareness at home. What it does AnemiaGuard is a comprehensive support assistant for anemia prevention, monitoring, and recovery. The app estimates anemia risk probability by analyzing visual indicators such as pallor in fingernails and eye conjunctiva, combined with anthropometric data (weight, height, and age) and perceived clinical indicators like mood and energy levels. Additionally, it provides a strategic nutritional guide that classifies meals into heme and non-heme iron sources, helping users improve iron absorption through proper food combinations. The app also includes alerts about food interactions, education on side effects of iron supplementation, reminders for treatment adherence, and multilingual support. Our solution does not replace clinical diagnosis, but acts as an early alert and recovery support system. How we built it We began by researching major chronic health problems in our country and found that anemia was one of the most impactful and underserved conditions. We explored existing solutions and discovered the lack of tools focused on recovery and prevention, especially in areas with limited access to healthcare and internet connectivity. We designed the initial user experience in Figma to ensure accessibility for both parents and adults. While the prototype provided a strong foundation, we implemented and refined many key screens manually in React, improving usability, accessibility, and adapting the design to real-world constraints. We also curated a diverse nutritional database focused on affordable and regionally accessible ingredients. From a technical perspective, we developed the application using React and wrapped it into a standalone Android APK using Capacitor to ensure offline usability. We trained a machine learning model using a public dataset to estimate hemoglobin levels from eye images. The model achieved a Mean Absolute Error of 0.78 g/dL, which represents a relatively small deviation compared to laboratory measurements. We also implemented multilingual support, educational modules, and a system for tracking symptoms, mood, and recovery progress.. Challenges we ran into One of our biggest challenges was balancing accuracy and accessibility in image-based anemia risk detection. Integrating machine learning into a portable and offline environment was complex, especially due to compatibility issues when exporting models from Python frameworks. We had to retrain and adapt the model in TypeScript to ensure it could run directly on the device. Another challenge was designing a nutritional system that remained diverse while strictly focusing on iron bioavailability, identifying inhibitors and enhancers of iron absorption. We also initially built a web version, but limited internet access in rural communities forced us to redesign the solution into a fully offline mobile application. This required learning new tools and adapting our architecture. Accomplishments that we're proud of We are proud of creating a solution that goes beyond detection and actively supports treatment success. Our nutritional module helps break the cycle of monotonous diets and offers practical and culturally adaptable solutions. We also successfully developed a portable, offline-first application that can reach underserved communities. Additionally, our hemoglobin prediction model achieved strong performance and demonstrated the feasibility of non-invasive screening tools. Most importantly, we built an educational platform that empowers families, promotes early medical consultation, and monitors therapeutic failure through clinical and emotional indicators. What we learned Through this project, we learned the importance of applying clinical semiology in a digital environment. We discovered how mood, energy, and behavioral patterns are key indicators that patients often overlook. We also gained experience working with new technologies, including training machine learning models in TypeScript, building multilingual systems, and deploying mobile apps using Capacitor. This project reinforced the value of designing inclusive and accessible health technologies tailored to real-world constraints. What's next for AnemiaGuard Our next step is to further refine our AI image recognition to improve the precision of conjunctiva and fingernail analysis. We also plan to add laboratory result tracking, allowing physicians and patients to monitor hemoglobin levels and treatment progress directly in the app. We aim to expand language support, adapt nutritional recommendations to regional diets, and improve accessibility for diverse cultures and communities. Ultimately, our goal is to scale AnemiaGuard globally, ensuring that every child and adult has the opportunity to prevent anemia and recover with confidence, regardless of where they live. <div