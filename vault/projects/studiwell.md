---
slug: "studiwell"
url: "https://devpost.com/software/studiwell"
title: "StudiWell"
hackathon: "Accelerate App Development with GitHub Copilot"
organization: "Microsoft"
winner: true
words: 700
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# StudiWell

> An academic companion app, powered by Azure software with AI.

[Devpost](https://devpost.com/software/studiwell) · hackathon [[Accelerate App Development with GitHub Copilot]]

## Facets

**domain** [[education]] [[mental_health]]
**user** [[educator_student]] [[researcher]] [[social_worker]]
**substrate** [[video_visual]] [[web_dom]]

**stack** azure, azureai, css, express.js, firebase, github, github-copilot, html, javascript, node.js, phi-3, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- 1/ ai study assistant
- 2/ mental health
- 3/ companion hub
- 4/ smart management hub (coming soon)
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for studiwell

## Body

Home Page (Demo Version) Welcome Page With Functionality Features Page AI Assistant Chatbot Mental Health Tracker Companion Hub for Specialists Advising Smart Management Panel (coming soon) Inspiration This project was inspired by the idea of an AI academic tutor (Khanmigo) and a problem trying to find a way to study better in a new academic era/setting. After my university transition, I wasn't in great academic standing and was nervous about my plan to improve my academic performance. I also experienced pressures coming into my life and not knowing how to talk or set up a meeting with my Mental Health counselor. I want to create a web application that combines the power of Azure software & AI integration with the idea of helping students find a better way to study and a way to simplify the process of connecting with advisors and mental health specialists. What it does Operating in a demo version, our app contained these Features : 1/ AI Study Assistant Using our AI Study Assistant to find the suggestions they need. Built-in Phi-3 Mini from Microsoft and deployed using Azure AI foundry , students can find the information related to the lectures and notes. 2/ Mental Health Tracking your mental health with features for mood detection, and suggestions on how to improve your well-being when studying. 3/ Companion Hub Connect with Mental Health Advisors and specialists to support students in their learning journey. 4/ Smart Management Hub (coming soon) Helping student to keep their study task manageable, and keep track of important events (midterms, exams, and quizzes. How we built it We have built this app with a Front End and Back End Architecture: 1/ Our Front-End interface consists of HTML, Tailwind CSS, JavaScript, and Node.Js with Express.Js . I have done the web interface and design with Figma, and implemented with the help of Github Copilot. 2/ Our Backend Chatbot Assistant feature integrated with Microsoft Phi 3.0 Mini 4k-instruct model, deployed from the Azure AI Foundry and contained with Docker Image and Azure Container Imagery for backend deployment. 3/ Other Features ( Mental Health Tracker, Companion Hub, Smart Management Panel ) were built with JavaScript, and Mental Health Tracker added Chart.js and Local Storage For Built-in Trends Monitor and web storage (JSON). Challenges we ran into Our challenges mainly ran into the idea of creating an education platform with mental health tracking and AI support. I've planned to prioritize and only focus on 2 features: AI Study Assistant and Mental Health Tracker, but I also expand on my ideas to build the Companion Hub and Smart Management Hub, adding more functionalities and more time to build these features. We didn't have much time to try other Azure solutions and services, but it is sufficient for our backend to host using Azure Container Imagery and Docker. We also convert our idea building with React to building with Node.Js and Express.js for easy management and deployment. Accomplishments that we're proud of We were proud to complete the Accelerated App Development on Github Copilot Learning Challenge on Microsoft Learn and integrated Github Copilot with Azure Software to help me understand the platform we're building. This is my first personal project, and Github Copliot not only helped me fix my codes but also provided suggestions on how to deploy the Azures Software (AI Model, Container Imagery) on our VS Code Build. We also used Azure Extensions on VS Code to monitor our build for this app. What we learned Deployment with a good idea in mind would be greater than sophisticated ourselves with more problems. Our building journey have a lot problems on deploying solutions to build our backends, but with the Image Containery we're able to run the program without needing to use other services (Kubernates...). We also learned about the right way to build a chat application using Azure AI Foundry library. What's next for StudiWell I will continue to integrate the smart management hub for task management and integrate other Azure software (Logic App) to complete our build feature. While the app operating in the demo version, I will also integrate our Welcome page to have our user page, and the user can experience these features. <div