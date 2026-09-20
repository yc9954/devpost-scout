---
slug: "science-buddy-hvf91r"
url: "https://devpost.com/software/science-buddy-hvf91r"
title: "Science Buddy"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 478
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/structured_db"
---

# Science Buddy

> Ready for a science challenge? Science Buddy is a fun quiz game that engagingly teaches kids science topics.

[Devpost](https://devpost.com/software/science-buddy-hvf91r) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**domain** [[developer_tools]] [[education]]
**substrate** [[structured_db]]

**stack** alexa, amazon-web-services

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for science buddy

## Body

Inspiration Science Buddy was inspired by competitions like the National Science Bowl that help foster an interest of science in children. However, since the National Science Bowl uses difficult, middle- to high-school level questions, Science Buddy attempts to use easier questions that might appeal to kids in elementary school, such as third, fourth, or fifth grade. What it does The skill asks the user a series of ten multiple-choice questions, each with three possible answer choices. It contains a database of over three hundred questions that it uses to generate these, and it tracks which ones you have practiced before to avoid repetition. Additionally, if the user exits in the middle of a set, they can pick up where they left off on another day. At any time during the skill, the user can ask Science Buddy for help, to repeat a question, give up, or interrupt and answer before the full question is read. How I built it I used the Node.js Alexa SDK to build Science Buddy. It is hosted using a AWS Lambda function with DynamoDB. Challenges I ran into I ran into quite a few gimmicks with transitioning between states (e.g. Help state, Trivia state, Returning state), especially when many states had to rely on the same methods being applied in different ways. Oftentimes the intent I was looking for was not found in the state the skill was in. Sometimes, the skill would crash for no apparent reason, and then I would have to debug it and finally find the problem in over ten minutes. Many times, all I needed was a good night’s sleep so I could refocus and resolve any issues with the skill. Accomplishments that I'm proud of I’m proud that I was able to create the skill and many of the questions, as I have not done much development with Alexa in the past. I also am really happy that I was able to pull through and incorporate some of the more advanced features, such as using DynamoDB to store user state information. What I learned I learned a lot about Alexa skill design as I went along, and hopefully I will be able to create more skills in the future using this knowledge. Of course, I also learned a lot of science when generating and sorting through past National Science Bowl questions to find ones that weren’t too tricky and would interest younger children. What's next for Science Buddy In the future, Science Buddy might support multiple users, with each user having personal scores and statistics. With the power of Echo Buttons, Science Buddy could also become a multiplayer game. I am also hoping that Science Buddy will incorporate user-submitted questions. It would also be nice to expand Science Buddy to different platforms, such as mobile devices. I can’t wait to keep developing and improving Science Buddy! <div