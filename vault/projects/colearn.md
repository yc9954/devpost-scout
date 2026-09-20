---
slug: "colearn"
url: "https://devpost.com/software/colearn"
title: "Colearn"
hackathon: "Hack Quarantine"
organization: "Hackathons UK"
winner: true
words: 368
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Colearn

> A low-bandwidth, accessible-for-all web based collaborative whiteboard!

[Devpost](https://devpost.com/software/colearn) · hackathon [[Hack Quarantine]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** node.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what i learned
- what's next for colearn

## Body

Video Inspiration I was inspired to create this project by the closure of my public school. I saw this affecting all schools in the United States, and wanted to do something to solve the issues with existing eLearning platforms. Additionally, my math teacher (who is almost 70!) had tremendous trouble using the Zoom platform and was very frustrated with technology based learning systems. This inspired me to look into building a platform that anyone could use to upload learning material and teach with (anyone can send MMS!) What it does It allows teachers and students to learn collaboratively on a whiteboard. The whiteboard has support for allowing teachers to "text-in" images that they would like to teach with through the Twilio SMS library. Teachers can write on and highlight imported images (eg. PowerPoint slides) and teach over low-bandwidth connections that traditional applications like Zoom and Google Meets would be unapplicable and unusable in. How I built it I built colearn with: React.js Express.js React Konva Firebase Bulma CSS I first wireframmed the UI. Then, I built the framework for the authentication system, which uses firebase, firebase-react, and firebase-web-buttons to keep users signed in. I built the whiteboard system with React Konva. Lines and highlights on the whiteboard are stored as objects, which means that the bandwidth consumed when using this platform is much less significant than that of audio/video streaming (max 100kb/min vs max 9mb/min). This allows the platform to be more widely used in low-bandwidth streams in rural America or isolated/low reception areas. What I learned I learned a lot about Firebase and React.js, as I had to become more familiar with data structures, data querying, and other manipulative operations. I also became very familiar with "state" in web applications. The project was a great learning tool and portfolio project :) What's next for Colearn In the future, I hope to implement the system on a wider scale through school districts. I also hope to add Video/Audio channel support through the respective Twilio libraries. There is a lot of room to grow with this project, so I hope I am able to have time to continue working on it! Thank you for your time! Video: https://vimeo.com/402055452 <div