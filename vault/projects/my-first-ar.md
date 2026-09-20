---
slug: "my-first-ar"
url: "https://devpost.com/software/my-first-ar"
title: "My First AR"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 652
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# My First AR

> Teaching kids about the wonderful world around them.

[Devpost](https://devpost.com/software/my-first-ar) · hackathon [[Snap AR Lensathon]]

## Facets

**substrate** [[document_pdf]] [[video_visual]]

**stack** api, javascript, lensstudio, machine-learning, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for my first ar

## Body

GIF Preview of scan game GIF Preview of shapes game GIF Preview of balloon game Home screen mock up GIF User flow GIF Try again prompt GIF Correct prompt GIF Well done prompt Inspiration I’ve just had a baby boy and his mom and I want to provide him with the tools to ensure the best possible chance of healthy, dynamic brain development. But right now I see children around the world being entertained by watching Cocomelon on iPads. Studies show active content consumption is better than passive viewing for early childhood development. We’re inspired by traditional kids toys, but wish to push into new frontiers. Lenses open up a wonderful new world of interactive adventure. With lenses your child is actively participating in their own stimulation (a relief for all parents everywhere) and learning actively as they consume. What it does We’ve built three games for kids ages 1-4. Fascinating, interactive games helps your child to recognize colors. The AR experience helps them recognize and make sense of shapes. Children will now have the essential building blocks to scan their home and experience the joy and rewards of finding/ discovering shapes and colors. Their learning is magically expanded. How we built it The entire lens was set up with an audio and text component that guides the user through each one of the three games. The team used a local API and Javascript to set up two of the games, testing the users knowledge of colors and shapes. Our in-house graphic department designed custom 3D balloons and shapes that will appeal to younger users. We used the 3D world objects controller to place them within the users environment. The code used helped the lens recognise if the correct color or shape corresponding to the voice prompt had been tapped or touched by the user. It also randomizes the order in which the shapes/colors are asked for, meaning no two plays are the same. For the final game, we used Python and over 1000 images of household objects to train the SNAP ML on recognizing shapes within household objects in the home. The user will be tasked to identify a rectangle or a circle within their home and the ML application allows the lens to scan the selected objects to identify if the user is correct or not. Challenges we ran into The training of the ML took time as there are so many variations of one shape in a household environment. With a larger capacity for development we’d train the ML on more shapes and colors so the user could test all of their knowledge from the previous two games. Due to the nature of the 3D objects floating, we had a couple of design issues in which they overlapped and caused issues for the user when selecting. We solved this by spacing the items out and allowing the user to move closer to each object to select it. Accomplishments that we're proud of Firstly, we’re really happy with the intuitive and simple UX. The app requires no onboarding. Secondly the ML component recognising shapes and colors in your real world is really innovative. What we learned AR is for all ages. And even the simplest games can be fun for the adults too! What's next for My First AR So much more! We see three key components: Engage My Baby. That’s the educational/play element which we’ve started with this submission Check my baby. ML offers very exciting healthcare elements. There is a health component to scan the baby’s diaper poo with Snap ML to see if it’s the right color, and we can even use voice ML to observe and monitor the baby’s cry, play, sleep and interactive patterns. Snap My Baby. This is a series of weekly lenses that capture your kid with graphics and filters to document the stages of their life as you share cross platform. <div