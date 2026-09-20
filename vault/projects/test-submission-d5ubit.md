---
slug: "test-submission-d5ubit"
url: "https://devpost.com/software/test-submission-d5ubit"
title: "eyeServant"
hackathon: "Junction 2016"
winner: true
words: 578
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# eyeServant

> Get your stuff in the blink of an eye! The eyeServant will pick up and deliver whatever you look at.

[Devpost](https://devpost.com/software/test-submission-d5ubit) · hackathon [[Junction 2016]]

## Facets


**stack** arduino-uno, baxter-robot, tobii-eyex, unity

## How they structured the write-up

- sales pitch
- inspiration
- what it does
- challenges we ran into
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for eyeservant

## Body

Sales Pitch Ever felt too lazy to pick up your stuff from across the room? Ever dreamt of having your own personal butler? Are you tired of robots having complex interfaces with scary buttons and crave something simpler? Well, dream no more – the future is here! With the help of our eyeServant you can grab something and have it delivered to you with just a glance of an eye. Look at the object you need and then look again at the place where you want it delivered – and the eyeServant will do all your work for you. You will never need to leave your comfy couch again! Inspiration We were inspired by the eternal human laziness. Nothing to be ashamed of, we just say it as it is. Humans go the great lengths to save themselves some unwanted effort – and we aim to help them to do so. But jokes aside, the main purpose of the solution is to help people with limited mobility in their everyday lives in a truly simple and unintimidating way. What it does The goal was to control the Baxter robot with the Tobii EyeX eyetracker and make it move objects from one place to another. The user would look at the object and then look at the destination where the object should be placed – and consequently the robot would do all the work for the user and move the object. Challenges we ran into However, we ran into some challenges while trying to communicate with the robot. It turned out that the robot we were using came with the wrong firmware (the manufacturing firmware instead of the research firmware) and ultimately we could not control the robot via commands from the computer. How we built it Instead we pre-programmed sequence of movements via the robot interface. Then we created the Unity program that reads the data from the eyetracker and checks what is the user looking at. If the user looks at one of the marked spots (marked specially in the Unity app for the purpose of the presentation), the signal is sent from the computer, via the Arduino board, to the Baxter robot, and as a result Baxter performs the next movement from the sequence. Accomplishments that we're proud of We’re very proud of the effects of our work – even though we ran into some technical difficulties while connecting to the robot, we managed to find a workaround allowing us to create the demo of the system. Those dirty hacks are what you are usually the most proud of at the end of any hackaton. :) What we learned We learned that if you see the biggest, the most expensive toy/hardware on the hackaton, always dare to ask to work with it – someone might just say yes. But seriously, we learned a lot about the Baxter robot (and about its different firmware variants) and how it can be programmed. Even though we didn’t get to actually write any software in ROS, there’s still a lot we learned about the Baxter and what are its capabilities. What's next for eyeServant We already have the Unity program that properly reads user’s gaze and transforms it onto the 2D plane of the table. The next step would be to actually connect the program with other Baxter robot – the one that has research firmware preinstalled. Although, this might not happen for us in the nearest future. ;) <div