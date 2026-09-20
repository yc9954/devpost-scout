---
slug: "plastif-ai"
url: "https://devpost.com/software/plastif-ai"
title: "Plastif.ai"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 270
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Plastif.ai

> Use your phone to detect microplastics in water!

[Devpost](https://devpost.com/software/plastif-ai) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[video_visual]] [[web_dom]]

**stack** arduino, gemini, python, react, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Our project Microscope+LED setup Arduino stuff Our beautiful frontend Good water result Bad water result Inspiration I think we're all concerned about microplastics ; research shows that we can find these pesky chemicals in almost all parts of our bodies. So we wanted to find an accessible way to mitigate microplastic exposure. What it does We have hardware that can transform a phone camera into a makeshift microscope . Then, our website allows you to take pictures of water with your phone and uses an AI model to predict whether the water has microplastics . In order to obtain better results, we shine different colors through the water while taking our photos. It is very cost effective . How we built it We disassembled a laser pointer and used its lens to create a microscope We hooked up an LED strip to an Arduino UNO R3 We use Gemini API to pick the colors to shine through the water Our site once again uses Gemini API to predict the concentration of different contaminants in the water We have a python backend server to communicate with the Arduino ## Challenges we ran into Finding components Using a wide range of APIs(i.e. Gemini) Interfacing our website with the Arduino SPUR wifi network ## Accomplishments that we're proud of Being able to actually interface with our Arduino Implementing AI to predict contaminants in water ## What we learned How to use an Arduino Gemini API Resourcefulness ;) ## What's next for Plastif.ai Use a better AI model Use better lighting (Dollarama LED strips might not be the play) Adding in different sensors <div