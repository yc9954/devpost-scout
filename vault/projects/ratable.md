---
slug: "ratable"
url: "https://devpost.com/software/ratable"
title: "RaTable"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 475
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# RaTable

> Helping students choose educators, one rating at a time

[Devpost](https://devpost.com/software/ratable) · hackathon [[Funathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** dotenv, ejs, express-session, express.js, html/css, mongodb, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ratable

## Body

Inspiration A study conducted on over 400,000 students found that only 30% of students felt that their teachers made school an exciting place to learn. In college, this isn't as big of a problem, because students can rate their teachers using websites such as ratemyprofessor.com , but in high school, middle school, online school, tutoring, and homeschool co-ops (learning centers for homeschoolers), there are no such tools to help students choose the right classes and teachers. That's why I created RaTable. What it does RaTable uses a simple 1-10 rating system (measuring overall effectiveness, clarity, organization, accessibility, and difficulty). To submit a review a user can create an account then rate the professor in the five categories. This is averaged with other user's reviews, stored in a database (MongoDB), and retrieved when a user searches for a teacher. To search for reviews on a teacher, a user just has to submit the instructor's name into the search bar. Then the server will get the information on the teacher from the database, and display it for the user to see. How we built it I made the front end using HTML/CSS, and the backend was primarily created using Express.js and MongoDB. For communication between the client and server, I used the templating engine Ejs for the HTML, and Express.js was used to receive information from the client. For the accounts I stored the information in MongoDB, and used express-sessions for the cookies to keep users logged in as they navigate around the website. Challenges we ran into It's my first time using Express.js, so I had a few issues with figuring out the POST and GET requests. Another issue was the sign in and sign out system. This is because when you navigate to a different part of the website (ie. contact form, reviews on a teacher, etc.) the client side isn't able to keep track of whether or not you're logged in. To fix this issue, I used cookies so that throughout the website I was able to keep a user signed into their account or signed out. Accomplishments that we're proud of I'm happy that I was able to make a working back-end, considering that it's my first time using Express.js. What we learned I learned about how to have MongoDB to interact with the Express.js and front end of the server using Ejs templating. I also discovered how to use POST and GET requests to interact with HTML forms to get information from the client side to the server side. What's next for RaTable Adding a written comment system so instead of just rating instructors on a 1-10 scale, users can add reviews that contain text Add an email verification system for users so that when they first create their account, our website can verify whether or not it's actually their email <div