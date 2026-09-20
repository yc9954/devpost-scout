---
slug: "pkd-compass-mgt16j"
url: "https://devpost.com/software/pkd-compass-mgt16j"
title: "PKD Compass"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 688
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# PKD Compass

> PKD Compass simplifies managing Polycystic Kidney Disease by turning complex health data into clear insights, helping users track labs, nutrition, and daily health in one place.

[Devpost](https://devpost.com/software/pkd-compass-mgt16j) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[agriculture_food]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[medical_record]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** codex, html, netlify, supabase, usdcapi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what we learned
- what's next for pkd compass

## Body

Logo Inspiration PKD Compass was inspired by my personal connection to Polycystic Kidney Disease. My mom and uncle have both dealt with the disease for years, and I’ve seen how deeply it affects everyday life. I also lost my grandfather to PKD, which brought a deeper sense of urgency to everything I’d already seen. Through this, I saw how difficult it is to manage the condition: not just medically, but logistically. There are over 12 million people worldwide living with PKD , yet there is no comprehensive app that truly helps patients manage their condition. The only existing tool on the market is overly generic and cannot track and organize meaningful health data. This gap became clear to me: patients are expected to monitor lab values, diet, medications, and symptoms, but they are left without a system designed specifically for that purpose. I built PKD Compass to solve this problem. What it does PKD Compass is a patient-centered health management platform designed specifically for individuals living with PKD. It allows users to: Track key lab values such as eGFR, creatinine, sodium, potassium, and blood pressure Monitor nutrition with a focus on kidney-relevant nutrients Manage medications with reminders Log symptoms and daily health patterns Store and organize medical records and appointments Find nearby nephrologists, dialysis centers, and support resources Add their lab reports to an encrypted vault and, using AI, get a fully detailed summary of the document and possible future steps the user may want to take The platform transforms fragmented health data into structured, easy-to-understand insights that help users better manage their condition over time. How I built it PKD Compass was built using a modern full-stack architecture focused on scalability and usability. Frontend: A responsive, intuitive interface designed to simplify complex health data Backend: A structured database and API system to store, retrieve, and process user data (Supabase and CloudKit) Deployment: Designed to run beyond local environments, making it accessible across devices Special emphasis was placed on clean UI/UX design to ensure that even complex data remains clear and approachable. For example, lab trends such as kidney function can be visualized over time: $$ \text{eGFR trend} = f(t) $$ where $t$ represents time, helping users understand progression rather than isolated values. Challenges we ran into One of the main challenges was balancing medical complexity with simplicity . Health data can easily become overwhelming, so it was critical to design an interface that presents meaningful information without clutter. Another challenge was integrating multiple systems, such as lab tracking, nutrition, medications, and resources, into a single cohesive experience without making the app feel disjointed. I also faced challenges in transitioning from a local prototype to a scalable application, requiring careful consideration of data structure, performance, and security. Accomplishments that I am proud of Building a fully functional, PKD-specific health management platform from the ground up Designing a system that consolidates multiple aspects of disease management into one unified experience Creating a clean, intuitive interface that makes complex health data easier to understand Addressing a real-world gap affecting millions of people with a practical, usable solution Developing a project rooted in personal experience with meaningful real-world impact What we learned This project reinforced the importance of user-centered design , especially in healthcare. I learned that: Clarity is more important than complexity when presenting data Real-world problems require thoughtful, structured solutions Building scalable systems requires planning beyond initial prototypes Good design is just as important as strong technical implementation I also gained experience in full-stack development, data structuring, and designing interfaces for long-term usability. What's next for PKD Compass The next steps for PKD Compass focus on expanding functionality and improving user experience. Future plans include: Enhancing data visualization and trend analysis Adding deeper personalization based on user health profiles Expanding the resource database globally Improving performance and scalability for a growing user base Continuing to refine the platform based on real user feedback Submitting the app to the app store, so people can use it worldwide The long-term goal is to create a tool that makes managing PKD more structured, accessible, and less overwhelming for patients and families. <div