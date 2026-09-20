---
slug: "vmeet-4ar1x3"
url: "https://devpost.com/software/vmeet-4ar1x3"
title: "We connect"
hackathon: "Hack Quarantine"
organization: "Hackathons UK"
winner: true
words: 694
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# We connect

> A unique platform to Collaborate with your classmates and organizing virtual meetings.

[Devpost](https://devpost.com/software/vmeet-4ar1x3) · hackathon [[Hack Quarantine]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** bootstrap, css, flask, html, javascript, machine-learning, meetup, mongodb, node.js, php, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for we connect

## Body

Login Page Profile Page Meetings Detail Page Request for a meeting Email Sent Fellow Students Profile Begin the meeting WireFrames Technologies used Inspiration Our inspiration is to build a safe platform for all students, sometimes a student is hesitant to reach out for help in person or they cannot due to the size of their class. With We connect, all students can get the help they need. What it does Vconnect is a virtual platform, where a student can host virtual meetings as well as organize group studies. Initially, a student need to create a profile and after signing in to his/her profile page, a rundown of meetings will appear according to the interests or the skills or the abilities of the students . Users can see the details of a specific meeting as well as can connect with those students who have already joined that meeting. This feature of our website will completely assist a student in knowing others and in contacting them if they need any assistance. The greatest element of our site is that a student can likewise request a virtual meeting. We have embedded Zoom and Gmeet for virtual meeting Platforms. As soon as a virtual meeting is requested, the selected student receives an email informing them about the request and ask them to respond to the request. We have paid explicit enthusiasm to User experience, to make sure that no-one gets confused. The “begin meeting” button stays disabled until 30 minutes before the meeting starts. Even other students can request access to it as soon as a meeting is hosted. All meetings are sorted based on their time of hosting. Furthermore, 30 minutes before the meeting students will get another email and text reminder. It was achieved using Twilio, as well. Finally, we wanted to ensure all students are in a good mental space. We wanted to make this platform a source of relief from their stress and to create a safe environment for students. So we have also integrated an option to hold non-scholastic meetings which students can be a part of for some fun. These meetings are specially designed to deal with each students interests like LGBTQ+, and Happy Hour wherein students can have lunch together. We used over 200 articles from Studentsaffairs.duke.edu, for match and recommendations. We have also connected MongoDB as a database to save all the information and integrated Twilio, sendgird, Esri, meetup, zoom, and Calendly API. How I built it Front-End and Backend : Entire frontend was built using HTML, CSS and JavaScript, integrated with node.js for backend. Meeting notification and Reminders : After selecting the meeting they want to join, we used Twilio API so that attendees receive an email notifying that they have signed up for the meeting. Also, attendees will receive text and email reminder 30 minutes before meeting starts virtually. This was done using Twilio API Database : Mongodb atlas is used to handle the database operations like fetching user profile, skills, interests, location and email id. Recommended Meeting : Using meet up API, first we filter the meetings according to the user state and city. Secondly, we further filter out meet ups according to the previous and present classes of the student. For example: a student is currently taking taking Database class and Algorithm class and has taken Web design class before. So in the upcoming meeting in meetup it will look for keywords like Database, Web Design, Algorithm, Data Structure and also the our program will give student recommendations according to the meet ups that their peers have chose. Challenges I ran into Integrating front end and Machine Learning model with the back-end. Accomplishments that I'm proud of We were able to build a relevant working platform in such a short period of time. :) What I learned How to use Twilio API Learned MangoDB Atlas Combining the recommendation model with the front-end. What's next for We Connect To make our platform secure. Handling load when many students are using the website. To add a feature of having in person virtual meetings with professor. Improve it's design and layout. To host the platform on the server. <div