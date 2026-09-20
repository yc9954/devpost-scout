---
slug: "sonic-pi-drumrnn-gui"
url: "https://devpost.com/software/sonic-pi-drumrnn-gui"
title: "Sonic Pi DrumRNN GUI"
hackathon: "BitRate: Machine Learning & Music Series"
winner: true
words: 805
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/web_dom"
---

# Sonic Pi DrumRNN GUI

> This project uses ML in a real time live coding performance context with a GUI that sends ML generated Drum Patterns into Sonic Pi and allows the user to react and collaborate with the ML model output

[Devpost](https://devpost.com/software/sonic-pi-drumrnn-gui) · hackathon [[BitRate- Machine Learning - Music Series]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[web_dom]]

**stack** css, html, javascript, magenta.js, nexusui, p5js-osc, sonic-pi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for sonic pi drumrnn gui

## Body

Sonic Pi DrumRNN GUI Inspiration I've always been interested in finding a way to incorporate Machine Learning into a real time performance scenario where the user can react in real time to the model output which will help influence the path of the performance. It is somewhat akin to Jazz in that you have to react in real time to what the model does since you do not necessarily know what it will do until it has done it. This puts the user and the model into a more collaborative situation and the shape of the music and performance is influence both by the model output and how the user reacts and builds on what the model has done. What it does The project was made to be a tool to use in a real time live coding performance setting. It allows you to create drum patterns and generated extensions of those drum patterns using the Magenta DrumRNN model. These drum patterns are sent to Sonic Pi via OSC messages and can be changed, modified and updated in real time. There is also the ability to live code additional sounds and patterns in Sonic Pi to go along wit those generated drum patterns. How I built it I have done several projects involving the p5js-OSC library to send messages to Sonic Pi, so I was familiar with the working of that library. I had experimented with creating drumbeats in Sonic Pi and sending them as input for the Magenta DrumRNN model and sending the output back into Sonic Pi, so I had the code needed to convert the Magenta output into something that Sonic Pi could play. For this project, I only needed the code to send model output to Sonic Pi. From there, I was inspired to make the interface from Tero's workshop where he introduced us to the NexusUI library and the drum grid. This seemed like a very accessible way to make this project more interactive. Challenges I ran into I do not have much experience with frontend web development, so it took some time to get the GUI to work the way I wanted it to as well as coordinating each OSC message. I tried live coding with it several times and each time got a better sense of features I wanted to make the experience feel more natural to a live coding performance. I had made a version with a tempo slider as well but since the timing is all handled in Sonic Pi, it made the code in Sonic Pi a bit more difficult when it was time to start live coding other loops. It worked okay but I felt if I want to make this available to other users, that would be a considerable drawback. The tempo can still be set in Sonic Pi. Accomplishments that I'm proud of I am very happy that this project works well in a real time performance setting. I have done several live coding sessions with it and really feel that it does a great job of incorporating ML output into a performance setting where the user is able to use and modify the output in real time. I really feel that this project can make ML more accessible and be seen as a clear tool in the music making process instead of something that could be seen as replacing the human element of creating music. Something to assist and collaborate with, like a member of a band. People I speak with, when told about how AI can create music, it is often viewed as opposition or a threat to the human element of the creative process. This project shows that we can work with the model and allow it to assist us, provide us with new ideas to react to and steer us into directions we may not have gone on our own. It really allows the flow and direction of the music to be influenced by the user and the model in an organic back and forth that feels very similar to playing with another person. What I learned I learned more about using HTML and CSS to help design more interactive projects. I also learned a lot more about Tone.js from Rachel and Tero's workshops, even though I didn't really use it in this particular project, I intended to do more with it in the future. What's next for Sonic Pi DrumRNN GUI I plan on incorporating this tool into my own live coding performances. I would also like to try and find a way to set this up on the web where the OSC part is taken care off on the backend, so the user doesn't need to download additional libraries or run a local server to make it more readily available for people to play with. <div