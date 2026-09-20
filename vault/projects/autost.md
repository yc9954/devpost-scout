---
slug: "autost"
url: "https://devpost.com/software/autost"
title: "AutOST"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 328
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# AutOST

> Real-Time music generation to accompany any scenario!

[Devpost](https://devpost.com/software/autost) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[video_visual]]

**stack** flstudio, groq, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autost

## Body

Being calm will calm the music down too Acting aggressive will generate aggresive music Smiles makes the music happy Inspiration Our idea was inspired by our group's shared interest in musical composition, as well as our interests in AI models and their capabilites. The concept that inspired our project was: " What if life had a soundtrack? " What it does AutOST generates and produces a constant stream of original live music designed to automatically adjust to and accompany any real-life scenario. How we built it We built our project in python, using the Mido library to send note signals directly to FL studio, allowing us to play constant audio without a need to export to a file. The whole program is linked up to a live video feed that uses Groq AI's computer vision api to determine the mood of an image and adjust the audio accordingly. Challenges we ran into The main challenge we faced in this project is the struggle that came with making the generated music not only sound coherent and good, but also have the capability to adjust according to parameters. Turns out that generating music mathematically is more difficult than it seems. Accomplishments that we're proud of We're proud of the fact that our program's music sounds somewhat decent, and also that we were able to brainstorm a concept that (to our knowlege) has not really seen much experimentation. What we learned We learned that music generation is much harder than we initially thought, and that AIs aren't all that great at understanding human emotions. What's next for AutOST If we continue work on this project post-hackathon, the next steps would be to expand its capabilities for recieving input, allowing it to do all sorts of amazing things such as creating a dynamic soundtrack for video games, or integrating with smart headphones to create tailored background music that would allow users to feel as though they are living inside a movie. <div