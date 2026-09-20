---
slug: "zenithlab-ai"
url: "https://devpost.com/software/zenithlab-ai"
title: "STEMLab AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 600
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# STEMLab AI

> Transforming STEM education through AI-powered virtual laboratories where every student can experiment, explore, and learn without physical limitations.

[Devpost](https://devpost.com/software/zenithlab-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** googlegemini3flash, localstorage, react19, recharts, shadcn/ui, tailwindcssv4, tanstackstart

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stemlab ai

## Body

Inspiration Many students around the world learn STEM subjects primarily through textbooks and lectures, with limited access to hands-on laboratory experiences. Physical laboratories can be expensive, inaccessible, or unavailable, especially in underserved communities. We wanted to create a solution that makes experimentation available to every student regardless of their location or resources. This inspired us to build STEMLab AI, an AI-powered virtual laboratory that allows students to explore scientific concepts through interactive simulations while receiving intelligent guidance and explanations. What it does STEMLab AI is an AI-powered STEM learning platform that combines virtual experiments with personalized educational support. Students can perform interactive experiments in Physics, Chemistry, and Engineering, observe outcomes in real time, and receive AI-generated explanations of the scientific principles behind each result. The platform includes: -Interactive virtual laboratory simulations -AI-powered STEM tutor -Real-time experiment analysis -Personalized quizzes and assessments -Progress tracking and learning insights -Accessible learning for students without physical lab access By transforming experimentation into an engaging digital experience, STEMLab AI helps students learn STEM concepts more effectively and confidently. How we built it We built STEMLab AI as a modern web application focused on accessibility, usability, and educational impact. The platform combines interactive simulation interfaces with AI-powered educational assistance. We designed an intuitive user experience that allows students to conduct experiments, modify variables, observe results, and immediately receive explanations from the AI tutor. The system was structured around three core components: Virtual experiment environments AI tutoring and concept explanation Learning analytics and progress tracking Together, these components create a complete digital STEM learning ecosystem. Challenges we ran into ----Gibberish quizzes: Early versions cheerfully generated a quiz on "pqoohqjolf" or random words which weren't topics. We taught the model to first classify the topic and return a structured {error} object, then handled it gracefully in the UI instead of throwing. ----Accurate chemistry without a real chem engine: Modeling every possible reaction is impossible, so we built a curated reaction graph for the most pedagogically valuable mixtures (acids + bases, metal + acid, halide + silver nitrate, peroxide + catalyst, etc.) with reaction-specific animations. ----Theme flicker: Dark mode would "snap" on page load. We fixed it with a blocking inline script in the document head that applies the theme class before React hydrates. ----Projectile accuracy: The original launch angle was off — we rewrote the kinematics using proper trig and validated against textbook ranges. Accomplishments that we're proud of We are proud of creating a platform that makes STEM experimentation more accessible and engaging. Key accomplishments include: -Building an interactive virtual laboratory experience -Integrating AI-powered educational support -Creating a user-friendly learning environment -Making hands-on STEM exploration available without expensive equipment -Demonstrating how AI can enhance education beyond traditional tutoring Most importantly, we developed a solution that has the potential to reduce barriers to quality STEM education. What we learned Through this project, we learned how AI can be used not only to answer questions but also to guide exploration and discovery. We gained valuable experience in educational technology, user experience design, AI integration, and creating learning-focused digital products. We also learned the importance of designing technology that is accessible, engaging, and capable of supporting diverse learning needs. What's next for STEMLab AI Our vision is to expand STEMLab AI into a comprehensive AI-powered STEM education platform. Future developments include: -Additional laboratory simulations across more STEM disciplines -Adaptive learning pathways personalized for each student -Teacher dashboards and classroom management tools -Collaborative group experiments -AR and VR laboratory experiences -Support for more languages and accessibility features Ultimately, we aim to make high-quality STEM experimentation accessible to every student, everywhere. <div