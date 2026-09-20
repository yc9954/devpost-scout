---
slug: "trabalenguas-cortos"
url: "https://devpost.com/software/trabalenguas-cortos"
title: "Trabalenguas Cortos"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 1109
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Trabalenguas Cortos

> A multimodal Alexa skill with more than 350 tongue twisters in Spanish to learn and have fun

[Devpost](https://devpost.com/software/trabalenguas-cortos) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

  <sub>weak: voice_speech</sub>
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** amazon-alexa, apl, lambda, node.js, s3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for trabalenguas cortos

## Body

Opening screen with a random hint Voice commands and touch buttons Tongue twisters have speech/text synchronization Echo Spot layout Good-bye screen Inspiration I wanted to do something for kids and about education because I think Alexa can help kids learn a lot of things in a fun way. Tongue twisters are a great (and fun) way for memorizing a new word and practice its pronunciation, so I thought that a skill that not only repeats the tongue twister but also could say it at slower and faster speeds would be really helpful. What it does It allows you to listen to tongue twisters in Spanish at normal, slower, and faster speeds. Users can choose tongue twisters with two options, the tongue twister of the day (there's one for every day of the year) or a random tongue twister. The slower speed option is great to learn the tongue twister. The faster speed option is great if the users want to test if they have mastered the tongue twister (in addition, some of them are funny to listen to at a fast speed). The voice experience is the same across all Alexa devices. The added value of screen devices is that users can see the tongue twister said by Alexa (with text/audio synchronization) and there are buttons for the most common options. How I built it Tech stack used Node.js ( ASK SDK v2 for Node.js ) AWS Lambda (as the backend) AWS S3 (to host the images) I used the Node.js. ASK CLI to build and deploy the project. I started with the voice experience (no visuals). I did a lot of iterations and put a lot of thought on the interaction model to make it as best as I could. I created 5 custom intents with all the utterances I could think of (that sounded natural or that I thought the user could say to activate the intent). At first, I was using the SSML tag <prosody rate="45%"> to make Alexa say the tongue twister slowly. However, it didn't sound good. So I thought that maybe I could insert a <break> with a 400/500 ms pause after every word to make it sound better. And there you have it, it's not perfect but it sounds a lot better. To say the tongue twister faster, I do use a prosody tag at a 130% rate. For almost every response Alexa says (or question Alexa asks) I have more than one alternative and so a random one can be chosen every time. Also, for variety, I made four background images with different colors. I also included some logic to avoid errors like asking Alexa to say a tongue twister faster when there's no tongue twister selected (for example, if the faster intent is invoked when the skill is opened, either by mistake or on purpose). For the Repeat intent, I implemented an interceptor that saves the last response of every intent (with the exception of the Repeat intent) in a session attribute. Only when I had the voice right, I started building the APL responses using the APL authoring tool. I have three APL templates: One for the main (first) screen. One for the tongue twister that uses a Pager component with two elements, one for the text and another one for the buttons. Using APL Commands ( Sequential , SpeakItem , and SetPage , in particular), I tell Alexa to say the text and show the next page of the Pager component when it finishes. One for the help and good-bye screens that just shows some text. After I had a first version of the screens, I tested on a device (Echo Spot) and fix all the errors (more about this on the next section). Next, I started gathering all the tongue twister. I didn't use a database, just a JavaScript file with an array. Finally, I tested the skill many times to fix errors, change responses (or add alternative responses), button labels, and even the title and invocation name of the skill (it was called "Trabalenguas Infantiles" at first or "Tongue Twisters for Children). Challenges I ran into Time. I learned about the contest early in January 2019, so I had to learn how to developed Alexa skills and APL in a proper way in about one week. It took me another week to build the skill. I have previously watched some talks about developing Alexa skills, but I had never tried building one until now. This is my first skill. The APL Authoring tool vs Real device. I started building the layout of the screens with the online authoring tool and just when I finished, I thought of buying an Echo Spot to test on a real device, the perfect excuse to buy one ;) (this device is the only one with a screen that is sold in Mexico at the moment). Thank God I did that. The layout was broken when I tested on the device. Apparently, the styles were the problem. I defined them in the styles section of the APL document and some of them were not being evaluated, so I had to define them inline, with the component. I don't know if this was because I'm doing something or it's a bug of the authoring tool, but it works fine on the device now. Using APL Commands and the Pager component. I had a hard time implementing the text/speech synchronization and changing the page displayed in a Pager component with a command. It wasn't working, I spent an afternoon trying to figure the error out. I was about to give up when at last, I discovered the problem by reading the pager documentation. When there are N pages in the pager, the first is index 0 and the last has index N-1. I was using 1 as the first index. Accomplishments that I'm proud of There's a lot of room for improvement, but I'm proud I overcame the challenges I run into to build the skill in a short period of time (one week). Also, my oldest kid (8 years old) has been trying the skill and he likes it, he said it was fun! What I learned Always test on the real device. Read the documentation more thoroughly. I discovered the Amazon Alexa Twitch channel . Office hours are great! What's next for Trabalenguas Cortos Add more tongue twisters. I'm not exactly sure how to make the skill available to other locales (like Spanish-ES), but publishing the skill to the Spain Skill store is definitely on this list. Pay attention to user's feedback to improve the functionality and the interaction model. <div