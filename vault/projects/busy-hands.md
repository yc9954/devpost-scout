---
slug: "busy-hands"
url: "https://devpost.com/software/busy-hands"
title: "Busy Hands"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 475
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Busy Hands

> Ever wanted to make slime? Busy hands can step you through the process along with four other fun science projects

[Devpost](https://devpost.com/software/busy-hands) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]]

**stack** amazon-dynamodb, ask, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for busy hands

## Body

Slime Inspiration In my previous career I was fortunate to spend some time working with younger students on science and engineering projects. In doing this I saw first hand how engaged and interested the students were in STEM subjects. Since leaving that role I have had less opportunities to provide support but hopefully the Busy Hands skill can help inspire an interest in science. What it does The Busy Hands skill currently includes 5 science projects each of which have step by step instructions, equipment required and facts. You can ask the skill to start a project and it will take you through the steps one by one by saying next to proceed to the next instruction. If you don't fancy working on a project at that time you can simply ask for a science fact. How I built it I used AWS Lambda and the Alexa Skills Kit Developer Console to build the skill using the command line. I based the skill on the recipe example provided in the Alexa Cookbook but had to expand on this to provide multiple projects and more content. Challenges I ran into I had problems trying to expand to provide multiple projects. I was unsure of the best or most efficient way to output the content of the array so I spent a lot of time researching how arrays work with node.js and playing around with the code. In the end I created an array for each project containing three more arrays for steps, facts and instructions. Accomplishments that I'm proud of I had very little access to internet whilst trying to develop this skill so I had to find a method where I was testing and modifying code offline before I uploaded and tested with the Alexa Developer Console test environment. In doing so I learned how to use the ASK command line interface to manage my skills. What I learned I learned how to use the function cardRenderer so I can add a title, some text and an image to users using an Alexa with a display. What's next for Busy Hands The first thing would be to expand the content including the addition of more projects and facts. I would also like to develop a function so items can be added to a users cart so the equipment can be easily ordered for their project. Another thing I plan on introducing is a score chart where the status of each project can be tracked and points can be received. Along with this I will also implement a quiz game where the students can receive extra points by answering the questions correctly. I would also like to create videos for each of the projects and add them so users with an Alexa show can view them or they can be viewed via a web application. <div