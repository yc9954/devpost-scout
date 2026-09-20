---
slug: "world-of-vulcan"
url: "https://devpost.com/software/world-of-vulcan"
title: "World of Vulcan"
hackathon: "Chroma Awards: AI Film, Music Videos, and Games"
organization: "ElevenLabs"
winner: true
words: 952
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# World of Vulcan

> A poetic visualization of a fantasy world from thousands of years in the past. Set in the Greek myth of Hephaestus, a god who was cast out of the heavens to live among mortals on earth.

[Devpost](https://devpost.com/software/world-of-vulcan) · hackathon [[Chroma Awards- AI Film- Music Videos- and Games]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[supply_logistics]]
**substrate** [[video_visual]]

**stack** comfyui, python

## How they structured the write-up

- inspiration
- how i built it
- challenges
- accomplishments

## Body

Between Heaven and Earth A Hidden Island The Boy and the Scorpion An Island held up by Pillars The Boy and the Pit of Fire A Shrine of Mother Hera Underwater Ruins Inspiration A poetic visualization of a fantasy world from thousands of years in the past. The ancient Greek story of Hephaestus. It’s not the usual narrative of conquest or romance, it’s about melancholic patience and how pain can be turned into creativity. I love imagery that blurs the line between fantasy and reality; I keep imagining this mini story living inside the bigger Greek literature, and I wanted to create a location-based tour-style film as a music video to guide the viewer through the world without too much narrative context, letting the music and atmosphere convey the flavor that its environments create. The Music from Eleven Labs was created first, I generated a few hundred songs, once I found the one I liked I put it on repeat and let the sounds inspire my imagination. How I built it I did the creative writing without the use of LLM's, on a blank journal page while riding the train. The music was created with ElevenLabs, here, I went back and forth with a custom text-to-music LLM I created since I don't have much sound-based vocabulary. I was not only surprised with the results of the scores and how mailable the editing was, but also with the language that was added to my own personal dictionary through the LLM assisted text-to-music process. I used a multi-modal image-to-video setup in ComfyUI, using a cross of open and closed source tools to create the still imagery with base models, as well as fine-tuning with a model that was trained on my body of 35mm photography to achieve the analog aesthetic. I've included a link to the free-to-download LoRA at the bottom of this page. Videos were animated with Kling using 2.5 Turbo I2I as well as First and Last Frame. What I like about making images with AI is the same thing that pulls me to a camera or to scribble on a napkin. Observing, iterating, and repeating like a slow sculpt where the compositional intuition is the chisel. Nudging colors and shapes inside a flat frame until it starts to feel like something, even before I know what that something is. It can take anywhere from 500-2000 stills to get an image that is ready to be processed into a video. Making these images in high volume feels like setting things on fire and watching how they burn, each image is its own fleeting, unique flame. Challenges It's difficult to reframe my default method of thinking, releasing the production-based boundaries I've known for so long in the world of filmmaking to open the space for AI and allow myself to imagine anything. Most of how I learned to think had been tied to lenses, blocking, crew, gear, the whole machine. I love that part, because it shapes the images. Here the work is less about physical craft and logistics and more about output-focused design and sequential imagery. The process requires staring at and sorting through a ridiculous amount of frames, often thousands in a single day. Frankly, it's a less glamours way of making films, but anything is possible and so it is more imaginative. I usually think about environments in production terms, like set dressing and props, what the locations need and what people do inside the production hierarchy. When writing shot concepts for the purpose of using AI I was able to see two groups of enviormental categories: the natural and the man-built, crashing into each other in different ways. I had never thought about writing about locations in this way until now. A challenge I continue to face with AI film is deciding what to spend time to make; anything is possible, and so intention becomes more important when execution becomes quickly scalable with fewer resources. Accomplishments Genearting images that feel gritty and alive is hard because the textural-average of all the data in the larger base models is plastic; it's like mixing all the paint and getting grey. I'm happy with the image characteristics I was able to pull out: heavy foreground occlusions, frames shrouded in shadow, edge aberrations, and compositions that maintain balance and asymmetry I tuned a multi-LoRA setup that I created just for this project, generating thousands of test images until the texture, halation, bloom, color, and contrast ratio felt right. There are a lot of moving parts, from how the LoRAs are trained to how different sub models are combined, to how the base models are chained together so they create patterns that are both cohesive and emotive. It's a delicate mix and I'm happy with the patterns in style that are a result of it. What I learned New words and New ways to think about what I’m looking at and what I'm listening to. With generating music, I learned to write about what I like, ask for breakdowns of tracks, and use word lists almost like mirrors. This process taught me that sounds that I previously couldn't identify. The text side of the tools became like a translator to see behind the mysterious curtain of sound, as somebody who comes from an image background. What's next for World of Vulcan I’m currently developing a full-length film for "Vulcan" and will continue to use AI-generated imagery for its visualization. I'm interested in using Elevenlabs in the future to both create score and transcribe an English language film into every language with voice clones of real actors and making films in a modern way that transcends traditional landscapes. Thanks for watching and reading. Calvin <div