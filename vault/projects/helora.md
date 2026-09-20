---
slug: "helora"
url: "https://devpost.com/software/helora"
title: "Healora"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 1107
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/code_repository"
---

# Healora

> "Healora, powered by Nurse Joy, uses empathetic AI for symptom tracking and predictive analysis, helping patients receive faster care while easing the workload for healthcare professionals."

[Devpost](https://devpost.com/software/helora) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[health_clinical]] [[labor_employment]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[code_repository]]

**stack** fastapi, fetch.ai, figma, framermotion, github, groq, hume.ai, next.js, shadcn, supabase, tailwindcss

## How they structured the write-up

- background
- what is healora?
- features
- planning
- system architecture
- to run the project
- use cases
- takeaways

## Body

Healora Background Why should nurses and doctors have to rely solely on manual inputs when modern healthcare technology has so much more potential? In hospitals and healthcare settings, medical professionals are often overwhelmed , managing complex workflows, multiple patients, and endless data inputs, often missing key details that could improve patient care. But what if technology could alleviate this burden , helping healthcare workers make quicker, more accurate decisions? In today’s world, we have empathetic AI, predictive models , and vast amounts of data at our disposal. Yet, many hospital systems continue to rely on outdated methods for managing symptoms, diagnoses, and patient interactions. Healthcare workers lose valuable time manually entering and interpreting data when AI could be working alongside them . Healora was created to bridge that gap . Empowering medical staff with AI-driven tools , Helora leverages Nurse Joy , a virtual assistant, to intelligently track symptoms , perform predictive analysis , and provide emotional understanding in patient interactions. With Helora, hospitals can streamline workflows , allowing nurses and doctors to focus more on what truly matters— saving lives and improving patient outcomes . What is Healora? Healora is an AI-powered healthcare platform designed to streamline patient care by integrating real-time health monitoring, virtual assistance, and efficient data management for healthcare providers. The pre-screening page allows patients to enter their initial health data and symptoms, which helps healthcare providers assess their condition quickly before moving forward with more detailed examinations. The treatment page is where Nurse Joy, Healora's AI assistant, interacts with patients. This page also displays vital signs, such as respiratory rate, blood pressure, and heart rate, allowing medical staff to monitor patient health in real-time. The patient list provides healthcare professionals with an overview of all patients currently under care, including their basic health details and treatment status. The staff table offers a detailed view of the healthcare team, enabling easy management of roles and responsibilities within the medical staff. Features Symptom Tracking : Nurse Joy, Helora's virtual assistant, allows patients to log symptoms efficiently. These symptoms are recorded and analyzed to help healthcare workers make data-driven decisions. Predictive Analysis Helora uses AI models to perform predictive analysis on the collected data, offering potential diagnoses and next steps for treatment based on the symptoms entered. Agentic Backend Helora uses AI agents for majority of its backend tasks, powered by Fetch.AI Empathetic AI : Helora incorporates emotional intelligence to provide compassionate, context-aware responses, ensuring that patients feel understood and supported during their care, powered by Hume AI AI-Generated Feedback : Nurse Joy provides real-time feedbackafter each interaction, helping healthcare professionals review patient information, track symptoms, and make informed decisions quickly. Real-Time Data Analysis Helora processes patient data in real-time, providing medical staff with up-to-date information on patient vitals and symptoms. Voice Interaction Helora supports voice input, giving patients flexible communication options based on their preferences. Planning We began by thoroughly researching the current state of hospital workflows, particularly focusing on how AI could alleviate the pressures faced by healthcare workers. From understanding existing tools to studying user needs, our research laid the foundation for building Helora. Once we had a clear understanding of the problem space, we created user personas and developed user flows to guide our design. Using Figma, we designed prototypes to rapidly iterate and refine the user experience. Our focus was on creating a system that is intuitive for both healthcare workers and patients, with a clean, user-friendly interface that reflects the needs of medical professionals. System Architecture Frontend Helora is a responsive desktop and mobile-friendly web application built using Next.js, with Tailwind CSS for streamlined and highly customizable styling. We use shadcn components to provide a cohesive design system and Framer Motion to add smooth, engaging animations for improved user experience. Our frontend efficiently manages real-time communication between healthcare professionals and Nurse Joy, ensuring seamless interaction. Data flows between users and the backend are handled securely, providing healthcare workers with immediate feedback from the AI and allowing for effortless tracking of symptoms, analysis, and patient interactions. Backend Our project's backend is a robust and scalable architecture designed to deliver advanced AI capabilities. Our backend employs Fetch AI agents orchestrated through FastAPI to manage workflows and interactions efficiently. We use Supabase with PostgreSQL for real-time data storage and management. For language-based analysis, we have integrated Llama and Mixtral models via Groq , while Hume AI powers our conversational tasks with advanced sentiment and emotional analysis. The technologies that we used to power Healora. To run the project Clone the repository at Healora Create a .env file, place it in the root directory and fill in with api keys of your configuration: NEXT_PUBLIC_SUPABASE_URL= NEXT_PUBLIC_SUPABASE_KEY= SESSION_SECRET= SESSION_EXPIRES_IN= NEXT_PUBLIC_DEVELOPMENT= NEXT_PUBLIC_BASE_LOCAL_URL= NEXT_PUBLIC_BASE_PROD_URL= HUME_API_KEY= HUME_API_SECRET= HUME_CONFIG_ID= NEXT_PUBLIC_HUME_CONFIG_ID_SUK= HUME_API_KEY_SUK= HUME_SECRET_KEY_SUK= Run the following commands(terminal) in the root directory: npm install npm run dev Use cases Takeaways What we learned Through building Healora, we discovered the complexities of integrating AI into healthcare workflows. We learned how crucial it is to blend advanced technology with empathy to enhance patient care. We also deepened our understanding of AI agents and language models, realizing their potential to make a real difference in medical workflow management and Nurse Assisstant settings Accomplishments We’re incredibly proud of what we achieved during this hackathon. Not only did we integrate a wide range of features like symptom tracking, AI-powered predictive analysis, and real-time empathetic feedback, but we also managed to design a clean, user-friendly interface tailored for healthcare professionals. This project also gave us the opportunity to apply research in meaningful ways by reading research papers and using user personas to ensure Helora meets the specific needs of both nurses and patients. On the design side, we’re proud of the consistent and intuitive UI built using Tailwind CSS and Framer Motion for smooth interactions. Helora’s design language prioritizes clarity and accessibility, catering to both healthcare workers and patients alike. What's Next Moving forward, we plan to focus on scaling Helora’s AI capabilities. While we’ve implemented empathetic AI and predictive analysis, we see room for improvement in terms of diagnosis accuracy and real-time feedback. Additionally, we aim to expand Helora’s capabilities by incorporating more comprehensive datasets to improve symptom recognition and predictive healthcare outcomes. We also want to refine Helora’s security and privacy features, ensuring patient data is handled with the utmost care and confidentiality. Our next steps include conducting more user testing, enhancing multilingual support, and refining Helora's user experience for different healthcare roles (nurses, doctors, HR personnel). Helora’s journey is just beginning, and we believe it has the potential to revolutionize how healthcare professionals interact with patients, improving both workflow efficiency and patient care. <div