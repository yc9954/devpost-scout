---
slug: "rekxare-dami-a-multilingual-study-time-organizer"
url: "https://devpost.com/software/rekxare-dami-a-multilingual-study-time-organizer"
title: "Rekxare Dami"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 538
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
---

# Rekxare Dami

> The first study timer and AI scheduler built for Kurdish students, in their own language.

[Devpost](https://devpost.com/software/rekxare-dami-a-multilingual-study-time-organizer) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** css, github, html, javascript, json, python, streamlit, streamlit-cloud, svg

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rekxare dami

## Body

Inspiration I noticed that Kurdish students, especially Badini speakers, have almost no study tools in their own language. Most apps are in English or Arabic. This means students have to translate while studying, which is tiring and slows them down. I wanted to build something that helps students organize their time, in the language they speak at home. I am a high school student from Kurdistan, Iraq, and I built this because no one else would. What it does Rekxare Dami is a study timer with a live countdown circle, daily and weekly statistics, a 7-day schedule planner, AI-powered scheduling, and dark mode. It is available in three languages: Badini, English, and Arabic. Students can pick a subject, set a timer, and track their progress over time. The AI scheduler generates a full weekly study plan from natural language goals like "I need to study math for 10 hours, physics for 5 hours." How we built it I built it using Python and Streamlit. The timer circle is drawn with SVG and CSS. User data is saved locally using JSON files, with each user having their own separate file for privacy. The AI scheduler uses Groq Llama 3 to generate study plans. I also built a second page for the weekly schedule, with tabs for each day, plus features to copy days, sort tasks, and mark them as done. The whole interface is responsive and works on mobile phones. It is also a Progressive Web App (PWA), so it can be installed and used offline. I hosted it on Streamlit Cloud and documented the code on GitHub. Challenges we ran into The timer circle did not fill up correctly after adding more features. I had to debug it several times. Making the schedule page work smoothly on mobile took many small CSS fixes. Translating every button, message, and label into three languages was slow, but necessary. The biggest challenge was building the AI scheduler to reliably generate valid schedules from user goals. I had to carefully design the prompt and handle edge cases. Accomplishments that we're proud of I am proud that the app is fully functional and looks professional. It works in three languages. The schedule planner and AI scheduler are built from scratch. I am especially proud that this is the first study tool in Badini Kurdish, something that did not exist before. I am also proud that I finished this project while still in 11th grade, with limited resources and no formal training. What we learned I learned how to build a real web app with Streamlit. I learned how to manage data with JSON, design a responsive UI with CSS, integrate an AI API, and solve problems by debugging step by step. Most importantly, I learned that I don't need to know everything before starting, I can figure it out along the way. What's next for Rekxare Dami I want to add a Pomodoro mode, sound notifications, and maybe a way for students to share their study stats with friends. I also plan to add more languages so even more students can use it. Most importantly, I want to keep improving it and make it a tool that Kurdish students can rely on. <div