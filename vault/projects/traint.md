---
slug: "traint"
url: "https://devpost.com/software/traint"
title: "traint"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 834
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# traint

> the.right.(and.intelligent).new.training method for customers and support agents

[Devpost](https://devpost.com/software/traint) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** css, genesys, groq, html, javascript, next.js, react, shadcn, tailwind, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for traint

## Body

Interface for dashboard with leaderboard and statistics interface for dashboard with analysis and ai generated feedback interface on Genesys with a call request interface on Genesys with a live chat Voiceflow process example Inspiration One of our teammates had an internship at a company where they were exposed to the everyday operations of the sales and customer service (SCS) industry. During their time there, they discovered how costly and time consuming it was for companies to properly train, manage and analyze the performance of their SCS department. Even current technologies within the industry such as CRM (Customer Relation Management) softwares were not sufficient to support the demands of training and managing. Our solution encompasses a gamified platform that incorporates an AI tool that’s able to train, analyze and manage the performance of SCS employees. The outcome of our solution provides customers with the best support tailored towards them at a low-cost for the business. What it does traint is used in 4 ways: Utilize AI to facilitate customer support agents in honing their sales and conflict resolution skills Provides feedback and customer sentiment analysis after every customer interaction simulation Ranks customer support agents on a leaderboard based on “sentiment score” Matches top performers within the leaderboard in their respective functions (sales and conflict) to difficult clients. traint provides businesses with the capability to jumpstart and enhance their customer service and sales at a low cost. traint also interfaces AI agents and analysis in a digestible manner for individuals of all technological fluency. How we built it traint was built using the following technologies: Next.js React, Tailwind and shadcn/ui Voiceflow API Groq API Genesys API The Voiceflow API was used mainly to develop the two customer archetypes. One of which being a customer looking to purchase something (sales) and the other being a customer that is unsatisfied with something (conflict resolution). Genesys API was utilized to perform the customer sentiment analysis - a key metric in our application. The API was also used for its live chat queue system, allowing us to requeue and accept “calls” from customers. \ The Groq API allowed us to analyze the conversation transcript to provide detailed feedback for the operator. Most of our features were interfaced through our web application which hosts action buttons and chat/performance analytics like the average customer sentiment score. Challenges we ran into There was a steep learning curve to Genesys’s extensive API. At first we were overwhelmed with the amount of API endpoints available, and where to begin. We went to the many workshops, including the Genesys workshop, which helped us get started, and we consulted with the teams when we ran into issues with the platform. Initially, we would run into issues with setting up and getting access to certain endpoints since they required us to be granted permissions explicitly from the Genesys team, but they were very prompt and friendly with getting us the access we need to build our app. We also ran into many issues with the prompt engineering for the AI agent on Voiceflow. When building the customer archetypes, the model wasn’t performing as expected so it took a lot of time to get it to work like we wanted. Although we had many challenges, we were all proud of the end product and the work we did despite the many roadblocks we faced :) Accomplishments that we're proud of In a short span of time, we were able to familiarize ourselves with several tools, namely the Genesys’ extensive API and the Voiceflow platform. We integrated these two tools together to create a product that serves both the customer as well as the customer service representatives. What we learned We learnt a lot about API integration, namely the Genesys API and Voiceflow software. Both the API’s were completely new to us and it took alot of research and trial and error to get our product to work. We also learned about the link between frontend and backend in Next.js, and how to transfer information between the both of them via API routes, client and server side components, etc. Our team came into this hackathon not really knowing much about each other. Coming from 4 different universities, we learnt a lot working with each other. What's next for traint We wish that we had more time to fully develop our leaderboard process through the gamification/employee performance API. We ran into some issues with accessing the API and given more time, we would have implemented this feature. Another feature we wanted to add was the ability to assign agents based off of client history. Although there may be some data concerns - providing clients with the ability to talk to the same agents that they preferred in the past would be very beneficial. Finally, we would love to take traint to the next level and see it incorporated in some real life businesses. We truly believe in the use case and hope it solves some key pain points for people. <div