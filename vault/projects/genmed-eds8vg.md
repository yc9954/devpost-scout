---
slug: "genmed-eds8vg"
url: "https://devpost.com/software/genmed-eds8vg"
title: "GenMed"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 487
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# GenMed

> GenMed AI uses AI to decode prescriptions, guide medicine usage, answer health questions, suggest cheaper alternatives, and locate nearby pharmacies for smarter healthcare decisions.

[Devpost](https://devpost.com/software/genmed-eds8vg) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** ai, api, apis, css, generative, github, google, javascript, maps, node.js, react, rest, tailwind, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for genmed

## Body

Homepage Floating chatbot Chatbot answers all users queries Daily medicine guide Prescription Analyser Prescription Inspiration Healthcare affordability is a silent struggle for many people, especially in India, where patients often end up paying more for branded medicines without knowing that cheaper alternatives with the same composition exist. We were inspired by this real-world gap—where lack of awareness leads to unnecessary financial burden. We wanted to build a solution that empowers common people to understand their prescriptions, make smarter cost-effective healthcare decisions, and find nearby pharmacies where their medicines are available using real-time mapping data. What it does GenMed AI is an AI-powered healthcare companion that: Analyzes uploaded prescriptions (image/PDF) Extracts medicine names, dosage, and details Explains each medicine in simple, human-friendly language Suggests cheaper alternatives with the same composition Shows nearby pharmacies with the selected medicine using Google Maps integration Provides a smart chatbot (HealthBuddy) to answer medicine and health-related queries Generates a daily medicine guide (when and how to take medicines) It transforms complex medical information into clear, actionable insights for everyday users while also helping users locate the medicines quickly in nearby stores. How we built it We built GenMed AI as a modern web application using a modular and scalable approach: Frontend developed with React + Vite for fast performance Styled using Tailwind CSS for a clean and responsive UI Integrated Generative AI APIs to power: Prescription understanding Medicine explanation Chatbot responses Implemented intelligent input handling and fuzzy matching to understand user queries like “dolo650” or “fever tablet” Integrated Google Maps API to show nearby pharmacies stocking the medicines Designed a component-based architecture for easy feature expansion Challenges we ran into Handling unstructured prescription data from images and PDFs Making the chatbot understand natural, imperfect user input Avoiding unsafe or misleading medical advice while still being helpful Ensuring responses feel real and not like dummy/static data Designing a UI that is both simple for common users and visually appealing Integrating real-time pharmacy availability data and handling dynamic location updates Accomplishments that we're proud of Built a real-world usable healthcare tool, not just a demo Successfully integrated GenAI for practical problem-solving Created a chatbot that feels natural, helpful, and context-aware Designed a clean, modern UI that enhances usability Addressed both cost reduction and awareness, making real impact Added real-time nearby pharmacy tracking to help users find medicines instantly What we learned How to apply Generative AI beyond basic use cases Importance of user experience over feature overload Handling real-world constraints like data variability and safety Building systems that are not just functional, but trustworthy and usable Integrating third-party APIs (like Google Maps) can greatly enhance practical usability What's next for GenMed Integrating real-time pharmacy price APIs for accurate pricing Adding multilingual support (regional languages like Tamil) Enhancing AI to detect drug interactions and risks Expanding nearby pharmacy tracking to include stock availability and route guidance Expanding into a full AI-driven digital health assistant ecosystem <div