---
slug: "tyodor"
url: "https://devpost.com/software/tyodor"
title: "TyodorAI"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 526
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# TyodorAI

> Tyodor is a 10-year-old AI that students teach to, reinforcing learning while giving teachers real-time insights, powered by Google Gemini API for interactive learning.

[Devpost](https://devpost.com/software/tyodor) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** css, flask, googleai, html, javascript, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tyodor

## Body

Tydor Lesson Edit Screen Inspiration We are always learning. Formal education starts at schools and continues on the job through onboarding and new skills development. Education is a multibillion-dollar economy, and learning can be expensive. This begs the question: how do we learn best? Richard Feynman, Nobel Prize-winning physicist and professor, believed that we’ve truly learned when we’re able to explain a concept to a child in plain English. One of our team mates is a teacher for 22 years, and she often challenges her students to teach their little brothers and sisters calculus in plain English. This inspired us to create Tyodor, a teaching and learning tool. What it does Tyodor is the AI of a 10-year-old who’s enthusiastic about learning. After a student studies a topic, they can gauge their understanding by teaching Tyodor what they’ve learned. Teachers and instructional designers then use data and AI to gather insights about their teaching and students’ learning progress. How we built it Tyodor was built using a modern web application stack, combining Python, Flask, and both SQLite and MySQL databases for flexible data management. We integrated Google Gemini AI via its OpenAI-compatible interface to power the AI learning assistant, with sophisticated prompts and NLP capabilities to ensure context-aware student interactions. On the frontend, we used HTML, CSS, and JavaScript with Jinja2 templates for a responsive, interactive experience, including real-time analytics with Chart.js to visualize student performance. The platform supports secure authentication, session management, and modular, maintainable code following MVC architecture and RESTful API design. To deploy and manage the system, we leveraged virtual environments, dependency management, and cloud deployment on Heroku, ensuring the app is accessible online for students and teachers alike. Overall, Tyodor combines AI, data analytics, and user-centric design to make teaching and learning more engaging and measurable. Challenges we ran into One of the major challenges that we ran into is the storing of the information. While at FIU we were unable to connect to any of the database servers that we were setting up, that forced us to adapt and choose a local SQLite to save all of the info and upload it to the server when we got home. Accomplishments that we're proud of Some of the things that we are proud of includes: Integrating AI with Flask and Python Saving AI chat history so we can have a running conversation Learning SQLite to be able to save the needed information having a login screen for both the teachers and the students. What we learned One of the major things that we learned is how to integrate OpenAI with Python Flask to be able to create a stunning front end experience that is able to have a conversation with AI. Something else that we have learned in relation to this is how to save the chat history using sqlite to be able to have a running conversation with AI. What's next for Tyodor By publishing it online, students in a teacher’s class can access it anytime for homework and studying. This makes learning more flexible and interactive. It also allows teachers to see how students are engaging with the material <div