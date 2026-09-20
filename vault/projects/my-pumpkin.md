---
slug: "my-pumpkin"
url: "https://devpost.com/software/my-pumpkin"
title: "My Pumpkin"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 552
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# My Pumpkin

> Users can design a pumpkin carving using their voice and see their design updates in real-time on-screen enabled devices. An in-skill purchase will allow them to email their design as a PDF template.

[Devpost](https://devpost.com/software/my-pumpkin) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** alexa, alexa-apl, ask-sdk, audacity, aws-lambda-layers, canvas, inkscape, javascript, lambda, node-canvas, node-canvas-lambda, node-lambda, serverless

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for my pumpkin

## Body

Landing screen on an Echo Show Complete pumpkin Inspiration My inspiration was pumpkin carving for Halloween with my kids. Scenes from the Ironman films where Tony Stark interfaces with the computer by voice to design and modify the Ironman suit were also an inspiration. Last, but not least, Stuart Packlington's awesome Loop It! skill. What it does My Pumpkin allows the user to create a custom pumpkin carving by voice. When the user initiates the "design pumpkin" intent, they will be prompted to choose from a variety of options for the eyes, the nose, the mouth, and teeth. If the user has a screen, they will see their pumpkin design change in real-time as they provide each answer. When the user finishes their design, Alexa will summarize it vocally and send them a card with a picture to their Alexa mobile app. How I built it I used the Alexa Skills Kit SDK for Node.js primarily to develop the skill along with AWS Lambda Layers to bring in node-canvas capabilities. To create the pumpkin eyes, noses, and mouths, I use Inkscape so I could easily reuse the vector shapes to create a display and template version of each. Each time the user answers a question about the pumpkin's characteristics a series of operations occur to update the image on Echo devices with a screen: The Lambda function draws a background image with a pumpkin matching the user's device resolution to the canvas. It then opens and brings in PNG image elements for the eyes, nose, and mouth to predetermined locations on the canvas, so they line up nicely over the empty pumpkin. It outputs the canvas with the composite pumpkin face and background to a JPEG file in S3. An APL template is then dynamically updated to reference the newly created JPEG image in S3 and output as part of the response. Since the face is generated dynamically at run-time, the skill can easily be expanded without needing to pre-bake every combination of facial characteristics. Challenges I ran into I couldn't find good vector shapes of pumpkin face parts so I had to learn how to use Inkscape to draw them myself. I couldn't find a good stock photo of an uncarved pumpkin with light matching the background I wanted to use so I had to light and shoot my own pumpkin to overlay on the background. The ASK SDK/API wouldn't allow me to render a new APL document on each slot completion so I had to re-work things so that when the user provides an answer, they are actually initiating and completing an intent. I then keep track of where the user is in the process using session attributes so I know what question they are answering and what I need to ask for next. Accomplishments that I'm proud of I am proud and super excited that I got the image of the pumpkin to update in real-time on Echo devices with a screen. What I learned Lambda layers APL documents Inkscape New dialog management techniques What's next for My Pumpkin "Alexa, tell my pumpkin to talk like a pirate!" "Alexa, tell my pumpkin to talk like a witch!" "Alexa, animate my pumpkin!" Use Echo Buttons to light the pumpkin with colored lighting and synchronize to a voice or soundtrack. <div