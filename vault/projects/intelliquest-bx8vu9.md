---
slug: "intelliquest-bx8vu9"
url: "https://devpost.com/software/intelliquest-bx8vu9"
title: "IntelliQuest"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 429
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# IntelliQuest

> Most quiz apps lock you into pre-written questions on fixed topics. IntelliQuest is different as you can type any topic and Perplexity AI instantly generates fresh, cited questions on demand.

[Devpost](https://devpost.com/software/intelliquest-bx8vu9) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[media_journalism]]
**substrate** [[structured_db]] [[web_dom]]

**stack** asp.net, auth0, bootstrap, c#, css, html, javascript, perplexity, signalr, sqlite, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for intelliquest

## Body

Logo Inspiration My inspiration was that I felt that not many quiz apps leverage the power of generative AI well, especially with its ability to become more transparent like Perplexity AI. As a result, I wanted to create an application that makes learning STEM and getting general knowledge fun while also using the power of AI to create questions, back them up with logical answers, and give the user its sources so that the user could fact-check the source if they would like, and they would be able to use the source to learn more. What it does IntelliQuest is an AI-powered knowledge platform that helps users learn about specific topics and build general and more in-depth knowledge in a fun way. How we built it This project was built with many technologies such as Auth0 for secure authentication purposes and Perplexity AI as the main backbone of the questions and answers part of the website. Along with this, SQLite was used as the main database which would be SQL Server in production. Along with this, for the frontend styling, Bootstrap 5 and Tailwind CSS were used. The programming languages used were HTML, CSS, JavaScript, and C# for the backend. Challenges we ran into Some challenges were integrating Perplexity with the application in the correct way along with other technologies we used. A challenge was also setting up the AI agent from Perplexity and making the functions run properly such as making the agent give the user coins coins when they are correct and avoid topics where it may hallucinate and instead reroute (such as mathematics where it should avoid arithmetic). Another challenge was setting up the SignalR for the multiplayer mode and ensuring a stable, dynamic connection between the server and the users that are playing the game so that forfeits do not accidentally happen and the game goes smoothly without any miscommunication. Accomplishments that we're proud of Some accomplishments that I am proud of are completing the website, having the multiplayer functionalities work, and being able to use my application! What we learned I learned how to integrate APIs that are more complex to use in various manners and to be able to configure features that are quite difficult to configure such as SignalR, Perplexity, and other technologies at the same time while also making it work smoothly. What's next for IntelliQuest The app is mostly production-ready and so I would like to configure the Auth0 service to make it ready for production, use SQL Server for the database instead of SQLite, and deploy the application! <div