---
slug: "visionary-bzvo5p"
url: "https://devpost.com/software/visionary-bzvo5p"
title: "Visionary"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 586
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/clinician"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Visionary

> Protect your eyes with automatic eye analysis and reminders

[Devpost](https://devpost.com/software/visionary-bzvo5p) · hackathon [[Hack the North 2023]]

## Facets

**domain** [[developer_tools]]
**user** [[clinician]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** adhawk, firebase, flask, javascript, python, react, sqlite

## How they structured the write-up

- inspiration 💡
- what it does 💻
- how we built it 🛠️
- challenges we ran into ⛰️
- accomplishments that we're proud of 🏅
- what we learned 📚
- what's next for visionary 🥅

## Body

Landing Landing Carousel Timer for an eye break! Eye exercise game Inspiration 💡 Do your eyes ever feel strained and dry after hours and hours spent staring at screens? Has your eye doctor ever told you about the 20-20-20 rule? Good thing we’ve automated it for you along with personalized analysis of your eye activity using AdHawk’s eye tracking device. The awesome AdHawk demos blew us away, and we were inspired by its seemingly subtle, but powerful features: it could track the user's gaze in three dimensions, recognize blink events, and has an external camera. We knew that our goal to remedy this healthcare crisis could be achieved with AdHawk. What it does 💻 Poor eye health has become an increasingly important issue in today’s digital world and we want to help. While you’re working at your desktop, you’ll wear the wonderful Adhawk glasses. Every 20 minutes or so, our connected app will alert you to look away for a 20 second eye break. With the eye tracking, you’ll be forced to look at least 20 feet–otherwise, the timer pauses. We also made an eye exercise game available to play where you move a ball around to hit cubes randomly placed on the screen using your eyes. This engages the eye muscles in a fun and exciting way to improve eye tracking, eye teaming and myopia. How we built it 🛠️ Our frontend uses React.js & Styled Components and React Three Fiber for the eye exercise game. Our backend uses Python via AdHawk's SDK with Flask and Firebase for our database. Challenges we ran into ⛰️ Setting up the glasses to detect the depth of our sight accurately was difficult as this was the key metric to ensure the user was taking a 20 feet eye break for 20 seconds. As well, connecting this data to the frontend was a bit of a challenge. However, with our Flask and React tech stack, it was an easy, streamlined integration. As well, we wanted to record analytics of our user’s screen time by taking any instances where their viewing distance was closer than a certain amount. It would give a user a chance to gauge their eye health and better understand their true viewing habits. This was a bit of a challenge as it was our first time using CockroachDB. Accomplishments that we're proud of 🏅 As coders and avid tech users, we are proud to have built a functioning app that we would actually use in our lives. Many of us personally struggle with vision problems and Visionary makes it so easy to help reduce these issues, whether it's myopia or eye strain. We’re super proud of the frontend, and the fact that we were able to incorporate the incredible Adhawk glasses into our project successfully. What we learned 📚 Start small and dream big. We ensured that the glasses would be able to track viewing distance and send that data to our frontend first before moving on to other features, like a landing page, data analytics, and our database setup. What's next for Visionary 🥅 We would love to incorporate other use cases for the Adhawk glasses, including more guided eye exercises with eye tracking, focus tracking by ensuring that the user’s eyes stay on screen, and so much more. Customized settings are also a next step. Visionary would also make for an awesome mobile app so that users can further reduce eye strain on their phones and tablets. The possibilities are truly, truly endless. <div