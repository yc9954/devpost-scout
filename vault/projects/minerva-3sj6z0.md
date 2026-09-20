---
slug: "minerva-3sj6z0"
url: "https://devpost.com/software/minerva-3sj6z0"
title: "Minerva"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 504
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Minerva

> Accessible tutoring for everyone

[Devpost](https://devpost.com/software/minerva-3sj6z0) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** claude, heygen, next, react, render, zoom

## How they structured the write-up

- about the project
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for minerva

## Body

Desmos integration Generated on-the-fly Generated on-the-fly Auto MANIM video generation Geogebra Parent Dashboard Parent Dashboard Parent Dashboard Parent Dashboard About the Project Inspiration Public education in the United States is increasingly strained. Class sizes continue to grow, individualized attention is rare, and outcomes reflect this reality. Only about 22% of U.S. high school seniors meet expected proficiency in mathematics, and the country ranks outside the top 30 among developed nations. At the same time, private schools and private tutoring, solutions that do provide individualized learning, remain financially inaccessible for most families. As a tutor with eight years of experience, I’ve seen that students learn best in one-on-one environments that emphasize visualization, reinforcement through questioning, and clear analogies. This project was inspired by the question: can we scale high-quality, personalized education without scaling cost? Minerva is our attempt to answer that question. What We Built Minerva is an AI-powered virtual educator designed to provide structured, personalized, and non-judgmental one-on-one learning. She supports learners from elementary school through university and into workforce re-entry. Minerva can: Meet with you over zoom calls and act just as a real tutor would. Ingest curriculum, notes, or documentation and generate a personalized study plan Generate 3Blue1Brown style videos using Manim in realtime Visually explain concepts via: Integrated Desmos/Desmos 3D Integrated GeoGebra Generated mini-interactive applets Track learning progress over time and adapt future lessons accordingly Reinforce concepts using questions, visual explanations, and analogies Adjust teaching style based on learner engagement and emotional cues Summarize progress and facilitate communication with parents or guardians The system is designed to prioritize teaching, not just answering questions, by maintaining continuity and adapting to the learner over time. How we built it We used Next.js/React as our web framework, and connected HeyGen LiveAvatar to the Zoom Video SDK to display the avatar in the browser. We then used the Web Speech API to get realtime transcriptions of what the user says, and we feed this to a backend endpoint. Claude Haiku is then prompted with this to begin generating a response, which HeyGen then speaks out loud. Haiku is given a number of tools, including: Generate/display a Manim video This is done by delegating the task to a smarter model (Claude Opus) to generate and execute the python code. Use tools in Desmos, Desmos3D, and GeoGebra Generate a HTML + JS demo Challenges we ran into Ensuring low latency so everything flows smoothly in zoom calls. This was a big challenge. But by cutting down turn around time on many different systems we were able to achieve the consistent results we see now. Accomplishments that we're proud of Having a technically feasibly product that's usable by people right out of the box, no configuration required. What's next for Minerva We plan on working more on Minerva after the hackathon. Our next immediate goal is to drastically improve the latency between the model generating the output and the avatar speaking. Building further to handle at higher scale and start getting users to help revolutionize their growth. <div