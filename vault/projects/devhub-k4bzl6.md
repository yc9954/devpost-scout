---
slug: "devhub-k4bzl6"
url: "https://devpost.com/software/devhub-k4bzl6"
title: "DevHub"
hackathon: "Microsoft AI Classroom Hackathon"
organization: "Microsoft"
winner: true
words: 724
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/security_privacy"
  - "user/educator_student"
  - "substrate/structured_db"
---

# DevHub

> DevHub: AI-based web application focused on empowering students, offering career mentorship, chatbot to understand books, a roadmap for diverse domains, and internships to build real-world projects.

[Devpost](https://devpost.com/software/devhub-k4bzl6) · hackathon [[Microsoft AI Classroom Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[retrieval_grounding]]
**domain** [[education]] [[security_privacy]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** azure, flask, java, llm, ml, openai, python, web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devhub

## Body

Inspiration As a community person, I understand the shared struggle that my community is facing where many students are unsure about their career path, leading to unproductive time in college. Those with passion lack a structured roadmap for skill development that can make them job-ready. In my tier-3 colleges, internship opportunities are almost none to zero because of our remote location as well. To address these challenges, my friend and I built a solution to help students become job-ready. What it does DevHub is a machine learning-based web application that will empower students in their core skills and help them become job-ready. This platform will help students get mentorship through a machine learning model and professional community members, a well-structured roadmap for different domains, and an Internship to build real-world and complex projects. Our platform focuses on providing students with the latest learning opportunities and helping them build real-world projects, enhancing their technical and core skills. How we built it We built it using microservice architecture where I have expertise in Python, Flask and Azure Machine Learning while my friend has expertise in front-end along with Java. So we divide the task according to our expertise. Breakdown of the architecture of this project: ML/AI: Utilizing Azure ML and Azure AI services, I deployed my Random Forest machine learning model, registering it on Azure ML. Creating a Rest-Endpoint through Azure ML features, I employed it for API calls. In my application, user information for career mentorship is passed to the endpoint, providing results. For the Chatbot, I used GPT-3.5-Turbo which was used along with RAG and OpenAi embeddings to retrieve information from the book that students upload. Web Application: Flask and Springbot were used in the backend where our Internship and roadmaps were built using Java while the NoCodePortfolio was built using Python(Flask). And we used the MySQL database to store the information of roadmap entities to fetch them dynamically. Challenges we ran into Following are the challenges that we ran into: OpenAI key limitation where we can send only one query per minute and also a token limit for text generation. Deploying the model on Azure ML and implementing it in Java applications. Integrating ChatBot with the application. Dynamic fetching of Data from the Database in the roadmap application. Accomplishments that we're proud of We're proud of creating DevHub, a smart web app for students in smaller colleges. Our achievements include: Complete Solution: DevHub helps students with mentors, clear career paths, and internship opportunities. Smart Chatbot: Our chatbot quickly finds info from students' uploaded books. Teamwork: We utilized our expertise and collaborated as a team to build this solution. Real Impact: Our Azure ML services offer career guidance with a high accuracy of 96%. What we learned Throughout this project, we acquired valuable skills and experiences: Technical Proficiency: I personally learned a lot about Azure ML and AI during this project and feel very confident in this tech stack now. AI Integration: Successfully implemented GPT-3.5-Turbo, RAG, and OpenAI embeddings for efficient information retrieval. Azure ML Deployment: Gained expertise in deploying machine learning models on Azure ML, and then creating its endpoint for a quick response. Collaborative Excellence: This was the first time we have worked on a project as a professional team where team tasks were assigned and we kept a record of our work and integrated them on run time and solved various challenges together. Such feeling nowhere to be found. What's next for DevHub To expand the reach and impact of our project, we have identified the following next steps: Scale-Up Technology: Gathering more data and enhancing the accuracy of our machine-learning model across various domains is a priority. Additionally, we will explore infrastructure scalability and consider cloud-based solutions to handle increased usage. Build Partnerships: Establishing partnerships with organizations and software houses aligned with our goals will help us offer more internship opportunities to students and enhance their job prospects. Leverage Social Media and Digital Marketing: Increase marketing efforts through social media platforms and online advertising to reach a wider audience. Offer free trials or discounts to attract new users. Explore Funding Opportunities: Seek additional funding through grants, angel investment, and crowdfunding campaigns to support the expansion of our project. Ensure Security: Implement robust security measures to protect the application from common web vulnerabilities, ensuring user data and information are secure. <div