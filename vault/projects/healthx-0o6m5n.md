---
slug: "healthx-0o6m5n"
url: "https://devpost.com/software/healthx-0o6m5n"
title: "Rapha"
hackathon: "Web5: Building the Decentralized Web"
organization: "TBD"
winner: true
words: 605
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/developer"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Rapha

> Centralized HealthCare Platform

[Devpost](https://devpost.com/software/healthx-0o6m5n) · hackathon [[Web5- Building the Decentralized Web]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[developer]] [[government_staff]] [[patient_family]]
**substrate** [[medical_record]] [[structured_db]]

**stack** clerk, convex, javascript, openai, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for rapha

## Body

Homepage Convex dashboard data Convex dashboard functions (Solo Project) Inspiration The inspiration behind Rapha came from recognizing the need for a more efficient and accessible healthcare system. We observed the challenges people face in accessing timely medical consultations and managing their health records. Rapha aims to bridge these gaps by providing a seamless platform for connecting patients with medical practitioners and offering a comprehensive electronic health record system. What it does Rapha serves as a comprehensive healthcare platform that connects users with medical practitioners for consultations. It offers an electronic health record system where verified doctors can securely access and update patient records. Additionally, Rapha features a personal healthcare AI assistant, RaphaAI, to provide users with personalized health insights and assistance. How I built it Rapha was developed using ReactJS and TailwindCSS for the frontend, providing a user-friendly and responsive interface. For the backend, I utilized Convex, leveraging its server functions, real-time data updates, acid database, vector search, file storage, automatic caching, and type safety. This combination ensured a robust and scalable architecture for our platform. ReactJS for the User Interface Convex for the backend Clerk for user identity and authentication Convex for secure data storage, OpenAI for Rapha chat assistant Challenges I ran into Authentication with Clerk and storing users in the Convex database was an issue. I Had some issues updating data in the database as it was updating just a field and clearing other fields but was able to fix it as well as convex clears the fields and repopulates the data. Since I was coming from a decentralized perspective, I had some issues making authorization and roles work as intended but I was able to fix it using convex docs. Accomplishments that I am proud of Patients registration Users (Patients) have their dashboard where they can create, edit, and delete their profiles securely after being onboarded into the platform. Medical Practitioners registration Users (Doctors) have their dashboard where they can create, edit, and delete their profiles securely after being onboarded into the platform. Secure Electronic Health Record System A secure and efficient electronic health record system, providing a reliable means for storing and accessing patient data, keeps track of previous records and keeps getting updated on the go Manual Verification of Medical License We have an admin portal to verify the authenticity of medical practitioners that enables them to interact with patients. In the future, we will integrate with health organizations or government bodies that can verify and validate these credentials. Chat System: Real-time chat system to facilitate communication between patients and medical practitioners. Patients can consult with doctors, share medical records, and get prescriptions and medical certificates. Rapha AI: Personalized healthcare assistant, to enhance the user experience and deliver valuable health insights. What I learned As a Frontend Engineer mainly, I learned a lot about backend development and Convex made it super easy to integrate and work with even though I joined the hack late. I learned about leveraging Convex's advanced features to build a scalable and robust backend infrastructure for Rapha using Convex's real-time database updates, convex functions, actions scheduling and vector search. What's next for Rapha -Adding and onboarding Hospitals and Lab Test Centres, Private Hospitals and medical agencies Govt agencies to help facilitate verification -Patients can send out requests for doctors or care workers (Home service) -Appointment Booking: Develop a feature that allows patients to book appointments with doctors or hospitals. -Expansion of services to include additional healthcare specialities and functionalities, catering to a broader range of medical needs. -Integration of advanced AI capabilities to enhance RaphaAI's capabilities, such as predictive analytics and personalized treatment recommendations. <div