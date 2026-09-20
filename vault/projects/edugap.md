---
slug: "edugap"
url: "https://devpost.com/software/edugap"
title: "EduGap"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 746
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# EduGap

> EduGap enhances the AI models Students can use by automating the integration of class-specific materials in Google Classroom while Teachers gain insight on student problem-areas.

[Devpost](https://devpost.com/software/edugap) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** api, chroma, chromadb, chrome, css, dbscan, gemini, google-cloud, html, huggingface, javascript, json, langchain, machine-learning

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for edugap

## Body

Inspiration Students will use AI for their school work anyway, so why not bridge the gap between students and teachers and make it beneficial for both parties? 1 All of us experienced going through middle school, high school, and now college surrounded by AI-powered tools that were strongly antagonizedantagonized in the classroom by teachers by teachers. As the prevalence of AI and technology increases in today’s world, we believe that classrooms should embrace AI to enhance the classroom which acts very parallel to when calculators were introduced to the classroom. Mathematicians around the world believed that calculators would stop math education all-together, but instead it enhanced student education allowing higher level math such as calculus to be taught earlier. Similarly, we believe that with the proper tools and approach AI can enhance education and teaching for both teachers and students. . 2 In strained public school systems where the student-to-teacher ratio is low, such educational models can make a significant difference in a young student’s educational journey by providing individualized support when a teacher can’t with information specific to their classroom. One of our members who attends a Title 1 high school particularly inspired this project. 3 Teachers are constantly seeking feedback on how their students are performing and where they can improve their instruction. What better way to receive this direct feedback than machine learning analysis of the questions students are asking specifically about their class, assignments, and content? We wanted to create a way for AI model education support to be easily and more effectively integrated into classrooms especially for early education, providing a controlled alternative to using already existing chat models as the teacher can ensure accurate information about their class is integrated into the model. What it does Students will use AI for their school work anyway, so why not bridge the gap between students and teachers? EduGap, a Chrome Extension for Google Classroom, enhances the AI models students can use by automating the integration of class-specific materials into the model. Teachers benefit from gaining machine learning analytics on what areas students struggle with the most through the questions they ask the model. How we built it Front End: Used HTML/CSS to create deploy a 2-page chrome extension 1 page features an AI chatbot that the user can interact with The second page is exclusively for teacher users who can review trends from their most asked prompts Back End: Built on Javascript and python scripts Created custom api endpoints for retrieving information from the Google Classroom API, Google User Authentication, prompting Gemini via Gemini API, Conducting Prompt Analysis Storage and vector embeddings were created using Chroma DB for the Student Experience AI/ML LLM: Google Gemini 1.5-flash ChromaDB for vector embeddings and semantic search as it relates to google classroom documents/information Langchain for vector embeddings as it relates to prompts; DBSCAN algorithm to develop clusters for the embeddings via Sklearn using PCA to downsize dimensionality via sklearn General themes of largest cluster are shared with teacher summarized by Gemini Challenges we ran into We spent a significant portion of our time trying to integrate sponsor technologies with our application as resources on the web are sparse and some of the functionalities are buggy. It was a frustrating process but we eventually overcame it by improvising. We also spent some time to choose the best clustering method for our project, and hyperparameter tuning in the constrained time period was also highly challenging as we had to create multiple scripts to cater for different types of models to choose the best ones for our use case Accomplishments that we're proud of Creating a fully functioning Chrome Extension linked to Google Classroom while integrating multiple APIs, machine learning, and database usage. Working with a team we formed right at the Hackathon! What we learned We learned how to work together to create a user-friendly application while integrating a complex backend. For most of us, this was our first hackathon so we learned how to learn fast and productively for the techniques, technology, and even languages we were implementing. What's next for EduGap 1 Functionality for identifying and switching between different classes. 2 Handling separate user profiles from a database perspective 3 A more comprehensive analytic dashboard and classroom content suggestion for teachers + more personalized education support tutoring according to the class content for students. 4 Pilot programs at schools to implement! 5 Chrome Extension Deployment 6 Finalize Google Classroom Integration and increase file compatibility <div