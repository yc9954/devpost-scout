---
slug: "sakshatkar"
url: "https://devpost.com/software/sakshatkar"
title: "Sakshatkar-Your Interview Buddy"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 446
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "substrate/web_dom"
---

# Sakshatkar-Your Interview Buddy

> Unlock your software engineering career with Sakshatkar! Get personalized help with LeetCode, HackerRank challenges, and interview prep. Build skills, boost confidence, and land your dream job!

[Devpost](https://devpost.com/software/sakshatkar) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[mental_health]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** css, html, javascript, python

## How they structured the write-up

- inspiration
- what we learned
- how we built sakshatkar
- challenges faced

## Body

demo Sakshatkar - Your Interview Buddy Inspiration The software industry is projected to grow 31% globally in the next few years. The number of opportunities for budding developers is very high. Yet, the competition for getting into top tech companies is very stiff. Technical interviews form a big challenge. Therefore, we are inspired to come up with a solution that would help them prepare for interviews but also helps solve the problem that candidates usually face: no proper guidance, limited time, and anxiety about interviews. What We Learned During the development of Sakshatkar , we gained insights into the nuances of interview preparation and the potential of AI in personalizing the learning experience. We learned: The importance of real-time doubt clearing to mimic actual interview scenarios. Techniques to manage and reduce interview anxiety through guided practice. The value of context-aware responses in AI to make the preparation more relevant and efficient. How We Built Sakshatkar Sakshatkar is built to facilitate a seamless, distraction-free experience for interview preparation. Here is how it is done: Fetch Question : A facility was designed for users to input links from the likes of LeetCode or CodeChef. Applying web scraping methods and using DevTools, the relevant HTML elements containing the question details were determined, and these could be fetched in a recursive manner. Integrated Code IDE : For making the preparation smoother, we added a text editor in which a user can write and test the code while being assisted by our AI Chatbot. AI-Powered Interaction : Our advanced NLP model powered AI chatbot interacts with users by giving hints, answering questions, or giving feedback to them. To make sure the chatbot preserves context across sessions, we gave responses tailored according to the requirements of the users. Challenges Faced Challenge #1: Preserving Chat Sessions Problem : Maintaining chat history between various sessions and questions. Solution : We used localStorage to store messages, and each conversation was tied to the question title and platform URL to make unique storage objects. Challenge #2: Designing Good Prompts Problem : Creating prompts that will encourage the AI model to produce the desired responses without giving away full solutions when only hints are required. Solution : Through research and experimentation, we fine-tuned our prompts, using public resources and creating placeholder texts to enhance user experience. Conclusion Sakshatkar - Your Interview Buddy is designed to be a holistic solution for software developers preparing for technical interviews. It integrates question fetching, a code IDE, and AI-driven guidance to deliver a personalized and efficient preparation experience. Our journey in building Sakshatkar has taught us a lot about problem-solving, user experience design, and the potential of AI in education. <div