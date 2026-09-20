---
slug: "studybuddy-qgdn7b"
url: "https://devpost.com/software/studybuddy-qgdn7b"
title: "StudyBuddy"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 607
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# StudyBuddy

> Improve your learning skills with an all-in-one education assistant with unlimited MCQ and flashcard generation. Practice for standardized test, difficult subjects, and active recall.

[Devpost](https://devpost.com/software/studybuddy-qgdn7b) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[web_dom]]

**stack** flask, nextauth, nextjs, openai-api, resend, tailwind, tesseract

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for studybuddy

## Body

Dashboard Inspiration We saw how students from low-income areas had fewer available learning resources and lacked one-on-one tutoring opportunities as they faced heavy economic barriers. To combat this issue, we decided to create StudyBuddy, an AI-powered flashcard generator, that helps these students get the high-quality learning they need. What it does StudyBuddy is a flashcard generator powered by the GPT language model in which students can give prompts to generate questions with multiple-choice answers. Students can also upload pictures of their notes to help the AI produce questions geared toward the curriculum they want to review. Through this, students can generate more unique questions and retain the information using active recall. We also built support for students that lets them review their flashcard sets and see what they got wrong and what to improve, as well as see how well they are doing over the week by showing how many cards they got correct. How we built it We built the front end of the website using NextJS, which helped us create a sleek design for our dashboard and question generator page. It also enabled us to abstract a lot of the code through components and allowed faster page generation. We used Tailwind CSS to style most of the components on the front end to make sure we had a responsive design and utilized MongoDB to store data on the back end. We used NextAuth for authentication which allowed us to create a secure login system as well as provide integration to Google and Discord accounts. We used Tesseract OCR to help upload pictures of syllabuses used during the flashcard generation process. We also used the GPT language model to generate the flashcards by using prompts the user provided through the front end (NextJS). Challenges we ran into Some challenges we ran into were installation issues with the Firebase auth system, but after switching to NextAuth we were able to get the login system up and working. When making the dashboard, we also had issues with the progress bars, which would bug out when there was a new month but the week was still the same. We fixed this by changing the sorter to use getTime() instead of getDate(). Another general issue we had was managing the complexity of the project, which was solved by assigning different team members to the frontend and backend and also focusing on the most important functionalities of the website first. Accomplishments that we're proud of We were proud of how we were able to quickly pick up NextJS, as well as a lot of libraries we incorporated into the website, at the beginning of the hackathon. We are also proud of how we were able to complete a big project on a tight deadline, considering everyone had different commitments throughout the week. What we learned Most of the team members learned how to effectively use NextJS to develop a dynamic frontend and easy-to-use UI for users even though it was the first time deploying it onto a project for some of us. We were also now more experienced with using AI tools on the backend including using GPT's APIs to generate content in flashcards, and all of us sharpened our skills in debugging and problem solving as we stumbled across errors and challenges throughout the hackathon. We learned to manage a project together as a team and communicate effectively with each other while working on the website. What's next for StudyBuddy Adding Group Chats and Voice Chats in which users can study together Chatbot that can answer your studying questions Expansion to the dashboard including stats page, more settings options <div