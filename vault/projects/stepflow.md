---
slug: "stepflow"
url: "https://devpost.com/software/stepflow"
title: "StepFlow"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 1016
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# StepFlow

> StepFlow is a step forward in study. Focused on your rhythm, not your results.

[Devpost](https://devpost.com/software/stepflow) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** chromadb, css, fastapi, firebase, html, javascript, json, langchain, postcss, prose, pydantic, python, react, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stepflow

## Body

Inspiration University students are constantly juggling lectures, assignments, revision, and everything else life throws at them. Most of the time, the problem isn’t laziness. It’s having too many things to do and not knowing where to start. Most students struggle with three things: task indecision, putting too much pressure on yourself, and not knowing when to revise. That’s why we created StepFlow, a scheduler that keeps users engaged through gamified tasks and revision sessions, helping them stay on top of their tasks and revisit newly learned concepts exactly when it matters most. What it does StepFlow is a gamified study system designed to help students start tasks, stay focused, and improve how they revise, in a guilt-free environment. To get started, the user enters tasks and upcoming tests. If they enter upcoming tests, they also have to enter the topics included in the test. For each topic, they may upload study material and rate their confidence on the material from 1 to 10. When the user presses “Start Day”, StepFlow presents two interactive study modes: “Hit Me With Your Best Shot”: The day’s tasks appear as targets that the user shoots. The user completes the tasks in whichever order they like. “You Spin Me Right Round”: All of the user’s tasks for the day are placed on a spinning wheel, along with one “fun” task, like watching Netflix, and the wheel randomly selects the next task. This combats task indecision, and encourages the user to continue to spin, for the chance of getting the fun task. For both modes, each task includes a timer to help users stay focused and avoid distractions. If the task is a revision session, StepFlow generates a short quiz to test the user’s recall. The quiz results allow the system to track how well the user remembers each concept. Behind the scenes, these signals, including quiz performance, confidence ratings, and time since last review, are used by an unsupervised learning model to learn the user’s memory patterns and adjust future revision timing so the user reviews a concept when it matters most. At the end of the day, users complete a short reflection where they reflect on the biggest factors that prevented them from completing the tasks they missed that day. This encourages accountability and allows the user to reflect on their study habits, before reaching the point of overwhelm. By combining gamified task execution with adaptive revision tracking, StepFlow turns studying into something engaging while still improving how students retain knowledge. How we built it StepFlow combines gamified task execution, adaptive scheduling, and AI-generated quizzes into a single study system. Gamified study interface: We first designed the UI and interaction flows in Canva, then implemented the interface using Cursor AI to generate the front-end components, and other AI image generation tools to create assets.. Adaptive study scheduler: To optimise revision timing, we implemented a scheduler based on the Ebbinghaus forgetting curve using the formula: R(t) = e^(-t/S) where retention decreases over time depending on topic difficulty, confidence level, and quiz performance. Scheduling is optimised using Q-learning. When generating a weekly plan, the system produces up to 60 candidate schedules that distribute tasks across seven days. For each candidate, the system creates multiple deep-copied task states and simulates future study behaviour several weeks ahead. These simulations evaluate retention, workload balance, and deadline adherence. The results update a Q-table, and the schedule with the highest expected reward is selected. Retrieval-augmented quiz generation: After revision sessions, StepFlow generates quizzes using a RAG pipeline. Uploaded PDFs are split into text chunks and converted into vector embeddings. When a quiz is needed, the system retrieves the top-k semantically relevant chunks and provides them as context to an LLM running locally via Ollama with the Llama 3 model. A structured prompt instructs the model to generate quiz questions in JSON format. Quiz performance is recorded and fed back into the scheduler to refine future revision timing. Challenges we ran into One of the main challenges was connecting the backend and frontend, as different parts of the system were built using different languages and frameworks. This made integration more complex, especially when passing scheduling data and quiz results between components. Collaboration was another challenge since different team members were responsible for different parts of the stack. We had to ensure clear communication between the frontend and backend development to keep the system working together smoothly. We also spent significant time tuning the parameters of the Q-learning model, as small changes could greatly affect how tasks were scheduled and prioritised. Accomplishments that we're proud of One accomplishment we are particularly proud of was successfully integrating the Q-learning study scheduler with the front-end interface. This was the most technically complex part of the system, and seeing the adaptive schedule generated by the model reflected in the user interface was a major milestone for our team. We are also proud that we were able to combine gamified study sessions, adaptive scheduling, and AI-generated quizzes into a single cohesive platform. What we learned Through this project, we deepened our understanding of reinforcement learning concepts and retrieval-augmented generation (RAG). We also explored new tools and technologies, including Ollama for running local language models and the npmecosystem for managing project dependencies. Equally importantly, we learned how to communicate complex technical ideas to non-technical team members, which helped improve collaboration across the team. What's next for StepFlow In the future, we plan to introduce a reinforcement learning model that learns each user’s study habits and schedules tasks at times they are most likely to complete them. By adapting to individual behaviour patterns, the system can create study plans that feel more natural and easier to follow. We also aim to integrate users’ existing schedules, such as university timetables, work shifts, and upcoming events, so that study sessions are planned realistically around their daily commitments and also so that users can have their schedules in one place. Finally, we want to add accessibility features to ensure StepFlow is usable by a wider range of students, including those with different learning styles and accessibility needs. <div