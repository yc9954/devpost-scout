---
slug: "custom-job-interview-simulation"
url: "https://devpost.com/software/custom-job-interview-simulation"
title: "Custom Job Interview Simulation"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 253
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Custom Job Interview Simulation

> Our application is for anyone looking for that initial industry experience but don't know what to expect from job interviews. We allow custom simulations and detailed post-analysis of interviews.

[Devpost](https://devpost.com/software/custom-job-interview-simulation) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]

**stack** langchain, openai, python, tkinter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for custom job interview simulation

## Body

Inspiration We were inspired by our own interview experiences from trying to find summer internships. What it does The app allows you to add custom parameters for an interview (e.g. company, job title, job description, interview type, personal resumé). The AI Chatbot will then conduct a structured interview based on those parameters. Once the interview is finished, a summary and analysis of the interview is released for the user. How we built it We built the app in python. The backend uses LangChain for the LLM models, and the frontend is done through tkinter. Challenges we ran into The main challenge was getting the ChatBot to develop a structure to its interview, while retaining adaptability to user answers and the freedom to ask specific, personalized questions. Accomplishments that we're proud of We're proud of creating a 3-layer ChatBot. The first layer involves creating a structured outline for an interview determined by the parameters. The second layer involves the ChatBot itself, conversing with the user, while proceeding through the interview structure. The final layer is a third-party observer that considers the interview holistically and provides a final analysis. What we learned We learned how to use LLM models in practice, in particular the function of agents. What's next for Custom Job Interview Simulation Next, we plan on working on adding much greater detail to the interview analysis aspect of the project, making the frontend more user friendly, and adding more features such as a job search tool based on resumé and interview performance. <div