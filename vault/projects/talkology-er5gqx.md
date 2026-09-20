---
slug: "talkology-er5gqx"
url: "https://devpost.com/software/talkology-er5gqx"
title: "Talkology"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 488
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Talkology

> Cracking the Behavioral Interview by Practicing with Talkology

[Devpost](https://devpost.com/software/talkology-er5gqx) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** flask, javascript, natural-language-processing, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for talkology

## Body

Inspiration Many people feel unconfident, shy, and/or awkward doing interview speaking. It can be challenging for them to know how to improve and what aspects are key to better performance. With Talkology, they will be able to practice in a rather private setting while receiving relatively objective speaking feedback based on numerical analysis instead of individual opinions. We hope this helps more students and general job seekers become more confident and comfortable, crack their behavioral interviews, and land that dream offer! What it does Gives users interview questions (behavioural, future expansion to questions specific to the job/industry) Performs quantitative analysis of users’ responses using speech-to-text & linguistic software package praat to study acoustic features of their speech Displays performance metrics with suggestions in a user-friendly, interactive dashboard How we built it React/JavaScript for the frontend dashboard and Flask/Python for backend server and requests My-voice-analysis package for voice analysis in Python AssemblyAI APIs for speech-to-text and sentiment analysis MediaStream Recording API to get user’s voice recordings Figma for the interactive display and prototyping Challenges we ran into We went through many conversations to reach this idea and as a result, only started hacking around 8AM on Saturday. On top of this time constraint layer, we also lacked experience in frontend and full stack development. Many of us had to spend a lot of our time debugging with package setup, server errors, and for some of us even M1-chip specific problems. Accomplishments that we're proud of This was Aidan’s first full-stack application ever. Though we started developing kind of late in the event, we were able to pull most of the pieces together within a day of time on Saturday. We really believe that this product (and/or future versions of it) will help other people with not only their job search process but also daily communication as well. The friendships we made along the way is also definitely something we cherish and feel grateful about <3 What we learned Aidan: Basics of React and Flask Spark: Introduction to Git and full-stack development with sprinkles of life advice Cathleen: Deeper dive into Flask and React and structural induction Helen: Better understanding of API calls & language models and managing many different parts of a product at once What's next for Talkology We hope to integrate computer vision approaches by collecting video recordings (rather than just audio) to perform analysis on hand gestures, overall posture, and body language. We also want to extend our language analysis to explore novel models aimed at performing tone analysis on live speech. Apart from our analysis methods, we hope to improve our question bank to be more than just behavioural questions and better cater to each user's specific job demands. Lastly, there are general loose ends that could be easily tied up to make the project more cohesive, such as integrating the live voice recording functionality and optimizing some remaining components of the interactive dashboard. <div