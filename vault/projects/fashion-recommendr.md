---
slug: "fashion-recommendr"
url: "https://devpost.com/software/fashion-recommendr"
title: "Fashion Recommendr"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 308
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Fashion Recommendr

> Discover your wardrobe!!!

[Devpost](https://devpost.com/software/fashion-recommendr) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[retail_commerce]]
**substrate** [[video_visual]] [[web_dom]]

**stack** dart, flask, gemini, python, tensorflow

## How they structured the write-up

- inspiration:
- what it does
- how i built it
- accomplishments that i'm proud of
- what i learned
- what's next for fashion recommendr

## Body

Discover Your Wardrobe!!! Inspiration: I had to go through an awkward phase of fashion in my life where I did not know what clothes looked good on me. What it does Uses computer vision to find out the body measurements of a person from their webcam footage or pictures. Then it uses these measurements to show clothes recommended by the model. How I built it Using python backend and flutter frontend. In python, I initially used mediapipe, a python library, to identify body joint points. Later, I used deeplabv3, an image segmentation model, to find the outline of the person in the image. Using the points from mediapipe, the algorithm draws a line on the axis of the shoulder and hip points that extends across the image. I then find out the intersections with the contour drawn from the deeplabv3 model and the mediapipe lines. This gives the length in pixels, using a pixel to cm ratio, I find out the actual length in cm. After this, I use Google's AI model, gemini, and ask it for the clothing recommendations. Finally, I run these items through a web scrapping program and show the results on flutter. Accomplishments that I'm proud of Found an efficient method to find body measurements. In my case, I integrated Image segmentation and Posture detection. Furthermore, made an extremely aesthetically pleasing website. Lastly, used algorithmic thinking to build the recommendation model. What I learned I learned about Image segmentation and how it works, using prompts using API(gemini). Along with this, I got knowledge about extracting information from an e-commerce scrapping algorithm. What's next for Fashion Recommendr Reducing user friction Use a Smaller language model for faster and more personalised results Use a more efficient program than the current e-commerce scrapping program. The new program will search the whole internet instead of only amazon. <div