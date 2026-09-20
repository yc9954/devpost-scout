---
slug: "lecours-interactive-e-learning-web-app-for-students-0hb6ga"
url: "https://devpost.com/software/lecours-interactive-e-learning-web-app-for-students-0hb6ga"
title: "LeCours - Interactive E-Learning Web App for Students"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 617
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# LeCours - Interactive E-Learning Web App for Students

> Beautiful UI & UX E-Learning App where Students Can Have Live Chat with Other Learners While Watching Educational Video Courses. With Deep Learning Based Assignment Proofing System for Instructors.

[Devpost](https://devpost.com/software/lecours-interactive-e-learning-web-app-for-students-0hb6ga) · hackathon [[Funathon]]

## Facets

**domain** [[developer_tools]] [[education]]
  <sub>weak: media_journalism</sub>
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]] [[video_visual]]

**stack** api, bcrypt, deep-learning, ejs, express.js, google-gmail-oauth, html5, mongodb, node.js, passport, socket.io, tailwind

## How they structured the write-up

- problem-1
- problem-2
- problem-3
- problem-4
- challenge-1
- challenge-2
- challenge-3:
- challenge-4:

## Body

Highly Secure Registration Page Beautiful Homepage Dynamically Changing Courses Archive Page Course View Page with Live Chat and Notes Taking Functionality Deep Learning Based Image Similarity Result Page Problem-1 Most of the times, students get bored while watching recorded video lectures. After the COVID-19 situation, most of the schools and educational institutes have started giving a set of videos to the students which the students need to watch. Solution to Problem-1: The web app contains a live chat feature with custom room for each course. This would help students watch the recorded lectures while chatting with their friends. Problem-2 Due to everything online now-a-days, teachers now require the students to submit their assignment in a digital format. Due to this, students have started taking the exact same solution photo from their friends, and submit it. Solution to Problem-2: A deep learning-based image similarity processing API is implemented to check if two assignments submitted by different students are similar or not. Problem-3 The students need to take notes while watching a video course. What if there’s no physical notebook with you. Solution to Problem-3: The web app contains a note taking feature, with which, the students can take notes while learning the course. Problem-4 Most of the times, due to a cyber-attack, the passwords of the users get stolen, because they are not encrypted using the industry standards Solution to Problem-4: The app is implemented with industry best password protection strategy with multiple salt rounds and hashing function implemented internally using bcrypt. It also contains Google OAuth2.0 Authentication Implementation for faster and secure logins. Last but not least, the web app is completely responsive and a very beautiful UI is crafted. Challenge-1 Implementing a Live Chat Feature requires a cloud service such as Firebase or AWS. I was not familiar with such services. My web app also doesn’t require such an expensive feature for a noble task. How we tackled challenge-1: Researched a bit and got to know about the Live Chat Node Package known as Socket.io which can be used to integrate Live Chat, and that’s too without the need of a separate database. Challenge-2 Implementing a Deep Learning Algorithm to check if two images are similar or not, requires an extensive knowledge of Machine Learning. I don’t know much about it. I got to know that, we need to create a Machine Learning Model, and train it with sample data set, and implement it using the flask and python libraries. All these things were going above my mind. How we tackled challenge-2: I researched about it, and got to know that we can use external APIs for such services, moreover, we are supposed to use external APIs, which are made to be used for such projects. I got to know about such an API provider DeepAI, which served my purpose. Challenge-3: The web app requires a solid database at the backend for various database operations. There are many database services such as MySQL, MongoDB, Redis, etc. The biggest task was to choose the best one, which could provide the best performance and faster development. How we tackled challenge-3: Since I was already familiar with MongoDB and as it is a NoSQL based database and doesn’t allow the developer to relate data sets easily. This project also doesn’t require any data inter-relation. MongoDB being the fastest Database CRUD operations provider, I used it in my project. Challenge-4: I needed to create a beautiful UI for the application users, since most of the engaging rate depends upon the UI/UX and performance of the app. How we tackled challenge-4: I used the Tailwind for the same, as it provides an easy-to-use CSS framework, extended with Flowbite’s premade blocks. <div