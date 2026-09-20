---
slug: "prioritizer-higher"
url: "https://devpost.com/software/prioritizer-higher"
title: "Prioritizer Higher"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 555
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Prioritizer Higher

> A todo list that leverages AI to help you on which tasks to prioritize!

[Devpost](https://devpost.com/software/prioritizer-higher) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**substrate** [[structured_db]]

**stack** flask, nebius, openai-api, react, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prioritizer higher

## Body

Inspiration Throughout my daily life I had a lot of things I needed to get done over a certain time span. At times, there were many tasks with multiple different deadlines that I wanted to execute so I multi tasked, not completely focusing with a single task at hand and metaphorically splitting myself to do many things at once. On top of that, I received new tasks everyday that added up onto my plate, which created more deadlines for me to concentrate on. Not only was it overwhelming for me, but it was also stressful because I had no idea where to start. I usually questioned myself on how I would complete such a plethora of tasks, feeling disorganized. What it does Our web app is a to-do list. The user creates and adds as many tasks as they like. More so, the user can add a deadline for each task they create. Also, the user has the ability to check off a task, delete a task, and even edit the deadline of a certain task they so choose. After the user enters the tasks they need to do, the user clicks the ‘priortize’ button in which the AI analyses the user’s to-do list and returns a suggestion of what the user should prioritize based on three factors: deadline, difficulty, and duration. How we built it For the frontend we used React and Tailwind. As for the backend we used Flask with OpenAI API and Nebius. Challenges we ran into We tried getting the OpenAI API to work and link it to the frontend. Eventually my teammate built a Flask server to store the OpenAI API, getting it to run, and making sure the frontend can fetch the localhost link that the Flask server generated. Another challenge was filtering the AI's response. In the Flask server, the OpenAI API client returns the response in a JSON format. I had to filter out only what was relevant like how AI bots like ChatGPT would and disregard things such as status codes, token details, etc. Additonally another challenge was trying to make the AI response in the frontend more readable and formatted into a list rather than a crowded paragraph. I wrestled this challenge and created a React component that would slice certain strings and characters from the AI response and format them with Tailwind at the end. Accomplishments that we're proud of We're proud of getting the app finished and seeing that it had solid functionality. We were also proud of getting the AI to work and produce a well-thought response in the frontend. What we learned We learned how to set up and run OpenAI API with Nebius and being able format its response in JSON. Also we learned how to use Flask to host the OpenAI API client, run the localhost server for the backend, and connect it with React. What's next for Prioritizer Higher We plan on developing, enhancing, and training the model in the future, making responses better and precise than yesterday. Perhaps we might gather user data by users having to create their own accounts and having their information stored in a database in order to feed to the model. Also, we plan on adding more color (ex. red, green, blue, etc.) to make it aesthetic and adding color themes. <div