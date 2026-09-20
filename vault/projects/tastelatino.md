---
slug: "tastelatino"
url: "https://devpost.com/software/tastelatino"
title: "TasteLatino"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 347
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# TasteLatino

> Ever wondered what delicious dish you could create with the ingredients you have on hand? TasteLatino uses image recognition tech to identify your ingredients and generate latin recipes in seconds.

[Devpost](https://devpost.com/software/tastelatino) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[video_visual]]

**stack** coreml, openai, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tastelatino

## Body

Inspiration We wanted to allow people to understand and explore latino food culture while also educating fellow latinos on possible different dish choices with certain ingredients. What it does Our mobile app has multiple features, the main one being a camera that captures a picture of an ingredient and uses a machine learning model to recognize the item. It then uses an Ai chatbot to generate multiple latin recipes using said item. It also offers a recipe of the day tab which highlights a popular dish everyday for inspiration. The profile feature allows you to favorite recipes you are interested for future use. The History feature allows you to look back on items you have previously scanned. How we built it Our team created the app mainly on xcode using swift, including all of the front-end and back-end development . We created our own machine learning model and trained it using CoreML which we then implemented into our xcode project. We also linked a chat-bot from OpenAi into our project using an API key. Challenges we ran into The major challenge we stumbled upon was a fault in our original machine learning model, that was providing inaccurate image detection results. We continued to make changes to the model code but eventually decided to switch from the model we were using: MobileNetV2 to a model we created that detects and processes pictures of food ingredients. Accomplishments that we're proud of Major accomplishment's we are holding our head high on are the machine learning model we created to predict the ingredients the camera picture was presenting and the AI recipe creation connectivity that links the image taken to the OpenAI API by converting the image into a JSON string that reads it to the API and generates the recipe for it. What we learned We learned how to create our own image detection model that will in future uses expand our possibilities in image processing. What's next for TasteLatino In the future we are ready to implement a history feature that provides the history of your recipe generations. <div