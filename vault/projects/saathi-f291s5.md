---
slug: "saathi-f291s5"
url: "https://devpost.com/software/saathi-f291s5"
title: "Saathi"
hackathon: "CS Girlies November Hackathon - Make Learning Cool Again! "
organization: "Computer Science Girlies"
winner: true
words: 958
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Saathi

> An AI-powered web that helps students develop problem solving skills. Saathi reduces AI dependency by guiding you through the problem, making quizzes using study materials, and visualizing progress.

[Devpost](https://devpost.com/software/saathi-f291s5) · hackathon [[CS Girlies November Hackathon - Make Learning Cool Again-]]

## Facets

**domain** [[education]] [[transportation]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** chart.js, django, gemini-api, javascript, postgresql, pymupdf, python, python-docx, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for saathi

## Body

Inspiration With the rise of vibe coding, almost everyone—including me, at some point—are or have been stuck in this AI hell where the lines of knowing something and actually being able to do it blur. It's like you know the content, the code, the logic, but actually writing it...just feels impossible. Saathi was built not to show you the destination or to drag you to the finish line, but to keep you walking. Something like this could save me—and probably many others—a lot of the hours wasted begging LLMs to teach instead of handing over full answers. Automating learning isn't about taking away the mental strain, because that is how you learn. What it does At first glance, Saathi may seem just another chatbot that can generate quizzes. But what if it actually reduces cognitive dependency on AI and can help humans grow? From calculus to code, Saathi is built to guide you, nudge you, and explain to you the fundamental concepts, not solve the problem for you and hamper your learning. It pushes you to apply STEM concepts through quizzes that test active recall, not passive reading. And when you see your progress visualized over time, the momentum builds, making you actually want to keep going. How I built it Frontend: Built with Tailwind CSS. The static HTML/CSS layouts were generated using Stitch to speed up UI development, allowing me to focus on the logic. Chart.js was used to make the beautiful and interactive charts. Backend: I chose Django as the Python framework for this project as I am the most comfortable with it. Along with that, libraries like Markdown It, PyMuPdf, Python-docx, and Functools have been utilized for displaying the LLM's response in a structured manner, reading and extracting text from pdf and .docx files, and making wrapper functions for views where login is required respectively. The authentication is handled using Supabase whereas the user's profile and quizzes are stored in a local Postgres DB. AI: Saathi itself is powered by a Gemini 2.5 flash model with a system prompt that ensures customizability and reliability in answers. For the quiz generation, a Gemini 2.5 flash lite model is being utilized to ensure speed. Challenges I ran into * Supabase's RLS policies: * It prevent unauthenticated users from inserting data into tables like profiles. But new users need a profile row created before they can authenticate. This meant new users couldn't create profiles because they weren't authenticated, but couldn't authenticate without a profile existing. -> Instead of using Supabase for cloud storage, I connected Postgres SQL to Django, and made a local database with the tables "Profiles" and "Quizzes". This allowed for hassle-free row inserts and smooth authorization * Quiz Parsing: * No matter what prompt was used, Gemini did not always follow it and occasionally returned textual response which broke the quiz generation since using json.loads() failed instantly. Manually parsing and structuring into dictionary containing lists could be done, but there still wouldn't be surety about the structure of the response. -> After a LOT of googling, I came across the documentation that actually gave me what I needed. Now, the model returns only and only a JSON object every time. Accomplishments that I'm proud of Building all of this solo: Of course the project making could be way smoother if I had a teammate, but looking back and realizing I did all of this (code, documentation, demo, filling out the Devpost project details, etc.) all by myself actually makes me proud. * Participating: * Yes, even participating was a really huge challenge for me as I was so nervous about this hackathon, people seemed way more experienced and skilled, a lot of people had a clear idea and strong team and initially it was all just so intimidating, especially participating solo, but I am glad that I did it:) ** Deployement: ** It was my first time deploying a web app and I had no idea what I was doing, but with a little bit of Youtube tutorials and asking Claude to explain me the bits and pieces I didn't get, I DID IT. I DEPLOYED MY FIRST EVER WEBSITE, WHICH IS THIS ONE. I'll never forget this hackathon now:) What I learned * Find a team, with the same timezone: * Time zone, no matter what you do, always is a bit of a barrier sometimes when it comes to meetings and ideation, regardless a team helps a lot. Not only with coding but also with ideating and the emotional support that comes along with one. * Use Flask: * As much as I love Django and am really comfortable with it, it is such a pain to set it up sometimes, of course the database management and authentication gets really easy, but in a hackathon where you have to build and present in 48 hours, Django might not always be the best choice. * Write a script for the demo: * I thought I could just record the demo video without any script or prep and say what comes to mind, then I ended up re recording like 15 times and realized why I need one. * How to deploy a website using railway: * I never did it before but now I learnt so many things, I always heard things are drastically different in production vs local host but this time, I lived it. It made me smash my laptop but I was very giddy when it deployed without any bugs (I think) after some time What's next for Saathi Spaced repetition, flashcard generation, automatic resource finder, and integration with FocusAI, another EdTech project I have that can go well with Saathi. For more information, make sure to read the documentation <div