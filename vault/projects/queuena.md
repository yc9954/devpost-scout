---
slug: "queuena"
url: "https://devpost.com/software/queuena"
title: "QueueNA"
hackathon: "Hack the North 2019"
winner: true
words: 861
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# QueueNA

> QueueNA makes it easier for students to learn more effectively by removing communication barriers between students and their professors.

[Devpost](https://devpost.com/software/queuena) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** firebase, grommet, javascript, react, xe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for queuena

## Body

The QueueNA Logo Inspiration Our inspiration for creating QueueNA (pronounced "Q-n-A") came from our own experiences as students at university. Compared to high school classrooms, lecture halls are far larger, creating the first of the problems that we aim to solve: Students who do not want to ask questions simply because it would involve yelling across a large lecture hall, and even if they were able to catch up with the professor after the lecture, the information would not be as useful compared to if it was presented while discussion was still on the topic of the question. The second problem we aim to solve is to encourage students that are too nervous to ask a question simply because they think it is a silly question. By presenting the questions in a semi-anonymous fashion, these students will be able to ask questions while avoiding the shyness that some students feel when asking a question in front of a large class. Real-time answers make learning more efficient and help students succeed without having to worry about how loud they can shout or how silly their question may or may not be. What it does The main purpose of QueueNA is to forward any questions that students in a lecture think of during the course of the lecture to the professor, where they can answer the questions sooner rather than later. This is done through a system that gives students an input field to ask a question. As soon as a student sends a question, it gets put into a list of questions for the professor to answer. The professors see the student’s questions on an external display with our web app. They then have the choice to answer it on their own timing (in which case, the current focus question will be displayed to everyone) or dismiss it, in order to tell the student to come see the professor later if the question is too complicated. How we built it QueueNA’s frontend is built using a combination of React and Grommet. For hosting, database and authentication services, we chose to use Firebase because of the simplicity of adding the required functions into our web app with minimal time wasted. Challenges we ran into One of the largest challenges that we faced during our development process was getting React and Firebase to work together. Firebase hosting is generally meant for simpler types of websites, which we learned quite quickly when we had to configure Firebase’s settings to work with a separate build folder instead of a project folder, among many other configuration issues. Another challenge that we faced was designing the UI - Grommet, while it had the potential to make a very good looking UI, was not always consistent between devices - the usage of ‘small, medium and large’ settings instead of size settings that used units such as em or percent meant that some UI elements looked off on other devices. Accomplishments that we're proud of We are very proud of our work here at Hack the North this year. Through well-organized teamwork, we were able to develop an aesthetically pleasing web application in 36 hours while learning much about how to do it along the way. On top of that, for 3 out of the 4 members on our team, this was their first hackathon, making the challenge even more interesting yet fulfilling. What we learned Throughout the course of Hack the North, we gained many new skills. For all of us, this was our first major project using Firebase, so experimenting with how it worked and how to implement it was a big part of our learning here. Some of us also learned the basics of WebSockets and the potential uses for it, namely the ability to update screens in real time from external sources. Finally, for some of us, this was our first time working with a front-end framework such as React, which proved to be an entirely different and yet very interesting way to build a webpage. What's next for QueueNA Through brainstorming within our team as well as many conversations with both students and professors to see what our customer base desires, we have come up with several potential future additions to QueueNA. Firstly, a voting system. Without a system like this, the potential for duplicate questions is greatly increased, so by using a system where students can upvote other students questions that they are also wondering about, the professor can see which questions have the most interest. Secondly, we would like to add a classwide polling system to allow professors to poll the entire class to see how well the class understands a concept. Thirdly, the ability to determine whether or not a user is a student or a professor is currently being investigated. The easiest way would be to get a manifest of emails from the institutions that use our system, but we are also considering alternate methods. Finally, support for the LaTeX formatting language is being considered, as while there would be a slight learning curve, it would allow for far easier entry of mathematical expressions that are also easier to read. <div