---
slug: "greenlight-idnv6o"
url: "https://devpost.com/software/greenlight-idnv6o"
title: "GreenLight"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 796
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/financial_record"
---

# GreenLight

> GreenLight turns dashcam footage into a learning tool. Incidents become 3D simulations in Three.js with a quiz to boost your driving score, reinforce learning, plus tips on safe driving and insurance.

[Devpost](https://devpost.com/software/greenlight-idnv6o) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[financial_record]]

**stack** adk, firebase, gemini, google, python, react, shadcn, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for greenlight

## Body

Dashboard page - dark mode Dashboard -> help modal Incidents page - dark mode Incident Simulation + Summary Incident Question Incident Answer Quiz page - dark mode Quiz page - answers Mobile Live Dashcam Dashboard page - light mode Incidents page - light mode Quiz page - light mode Figma Finalizing Figma Brainstorming colors Inspiration Between 20 and 50 million people are injured or involved in road traffic accidents globally each year, highlighting the massive scale of reckless driving and other unsafe driving practices. We were inspired to create GreenLight after recognizing that many drivers develop unsafe habits; therefore, we reimagined how people can learn safer driving practices by combining AI, simulation, and gamification into one seamless experience. What it does GreenLight is an AI-powered educational platform that helps users become safer drivers through immersive, personalized learning. A user can upload a dashcam footage containing an instance of unsafe driving (e.g., following too closely, sudden lane change, failed stop). Then by using Gemini AI, we analyze the video as well as generate 3D simulations in Three.js that recreate the unsafe driving scenarios from the uploaded footage, allowing users to visualize the incident and understand how different actions could have mitigated or even prevented it. After each simulation, users complete targeted quiz questions specifically designed around the identified safety issues, reinforcing proper driving practices through active learning. We also included a dedicated quizzes section to further educate users on safe driving practices and insurance. Correct answers earn safe driving points, gamifying the learning experience and reinforcing positive driving behavior. How we built it We started by designing our user interface in Figma and researching the best technologies and libraries for our stack, including shadcn/ui components and an icon library for the frontend. We then developed a comprehensive web application using React and Tailwind for the frontend that interfaces with a Python backend integrated with Gemini AI to analyze dashcam footage and identify unsafe driving behaviors. For the backend we used Python with FastAPI as our server which made it really easy to connect logic to the frontend. Using python came as an advantage to us since it has so many libraries that we were able to use such as pydanic. We were also able to use Firebase which was able to store all the data we needed including user, incident, quiz data, and more. We also used Gemini with Gemini ADK for the three.js simulation generation. Challenges we ran into Project Scope: Our initial vision was overly ambitious, specifically including a feature that allowed a phone to be used as a live dashcam for instant analysis. We quickly realized the time constraint required us to pivot and focus purely on file upload and the core simulation logic. 3D Simulations: Creating smooth, realistic 3D simulations that accurately represent driving scenarios required careful optimization of Three.js performance, especially for complex traffic situations Google ADK: Navigated the complexities of integrating the new Google ADK framework, resolving a series of dependency conflicts and low-level errors between the asynchronous API and the library's transaction management. AI Analysis: The initial agent architecture created a significant performance bottleneck due to its slow, sequential processing, and the AI's inconsistent JSON and simulation outputs required extensive prompt refinement to ensure reliability. Accomplishments that we're proud of Developed a functional video analysis pipeline that transforms dashcam footage into educational content. Created an intuitive and fully responsive user interface that effectively teaches safe driving practices through simulations and personalized quizzes. Fostered collaboration and teamwork under tight deadlines, leading to a cohesive final product. Successfully engineered an end-to-end, AI-driven pipeline by Google's Agent Development Kit (ADK) that transforms raw dashcam video into interactive 3D driving simulations and personalized safety quizzes. Optimized the system's performance by re-architecting the agent's workflow from a multi-step process into a single, efficient command, reducing the total processing time by approximately 50%. What we learned Effective prompt engineering techniques to get consistent results from AI models like Gemini. The value of providing immediate feedback in educational applications to enhance user engagement and reinforce learning. The importance of setting clear milestones and checkpoints during development for efficient workflow The agent's architecture directly impacts performance, and that a single, highly-structured command (a "one-shot" prompt) is far more efficient than a multi-step, conversational approach. Correctly configuring Python versions and dependencies is critical to mitigating complex integration issues. What's next for GreenLight Some goals we have for the future include developing mobile integration with seamless upload capabilities for dashcam footage, and enhancing our 3D simulations by refining the accuracy, realism, and visual quality of our driving scenario recreations. Ultimately, our long-term vision is to transform GreenLight from a post-incident review tool into a proactive safety co-pilot, implementing real-time dashcam analysis that provides immediate preventative alerts during actual driving. <div