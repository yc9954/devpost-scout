---
slug: "learnlive"
url: "https://devpost.com/software/learnlive"
title: "LearnLive"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 394
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# LearnLive

> Learn live together through video chatting and push notifications

[Devpost](https://devpost.com/software/learnlive) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[structured_db]] [[web_dom]]

**stack** asp.net, azure, blazor, css, efcore, javascript, sqlserver, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for learnlive

## Body

Inspiration Learning to code and get better at it is a huge part of my life. Taking advantage of the technological possibilities and trying to make the process of learning to code as convenient and motivating as possible for other people and myself was my inspiration for the project. I also want to emphasize on the community factor of learning to code. It is a great way to meet-up with people from allover the globe. What it does Users can sign up either with their Google or GitHub accounts. They can create learning groups themselves or join groups that have already been created. When they subscribe to a group they receive push notifications over WhatsApp whenever a learning note is created in that group. A learning note is a very useful thing to learn about the topic of the group and can be created by a user of a group. The users can and are encouraged to enable their webcam and join. Per audio and video they can discuss which learning note should be created next. Because they are on video this also creates a community feel and members can encourage each others. How we built it The backend is build with ASP.NET Core. Entity Framework Core is used as an ORM and Azure SQL as the database. Blazor WebAssembly is used for the frontend. JavaScript is also in use in the frontend to make Twilio programmable video work. Twilio programmable video works on top of WebRTC and is needed to make the video livestream work. The application is hosted on Azure with Azure App Service. GitHub Actions are used for the CI/CD pipeline. Twilio programmable text is used to send the text messages. Challenges we ran into The use of Twilio programmable video was overwhelming at first. Good documentation on Twilios site made it convenient to work with. The website is not responsive. Making it responsive was too hard for me. Accomplishments that we're proud of It was a very cool feeling seeing the livestream feature working the first time! What we learned Working with Twilio programmable video and Twilio programmable text. What's next for LearnLive I will continue working on the project. First I give my best to make LiveLearn as responsive as possible. Then I want to expand its features so that also quizzes can be created in a group. <div