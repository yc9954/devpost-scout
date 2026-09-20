---
slug: "getrecipe"
url: "https://devpost.com/software/getrecipe"
title: "GetRecipe"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 376
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# GetRecipe

> You bring the craving. We bring the Recipe!

[Devpost](https://devpost.com/software/getrecipe) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, flask, git, github, html, java, json, openai, python, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for getrecipe

## Body

Our start page Our logo Pizza example Inspiration We wanted to develop a Google Chrome extension. Our inspiration was the functionality of Chrome extensions and the simplicity behind it. We were also inspired by the idea of making cooking easier and more accessible for everyone, especially those who may not know what to make with the ingredients they have on hand. What it does GetRecipe is a Chrome extension that allows users to upload an image of food, and it returns a list of ingredients and a recipe to make that dish. This can be particularly useful when you see a dish you'd like to recreate but don't know what's in it or how to make it. How we built it We built GetRecipe using JavaScript for the Chrome extension's popup and background scripts. We used the Fetch API to send the image to a Flask server, which uses a computer vision model (YOLOv8) to identify the food. After we get the food we use the OpenAI and mealDb ( https://www.themealdb.com/ ) API in order to get ingredients and the recipe based on the food. The results are then sent to the client side and posted as a new tab. Challenges we ran into One of the main challenges we faced was getting the name of the food from the YOLOv8 library. Another challenge was ensursing constant communication between the flask server and the client side. Accomplishments that we're proud of We're proud of successfully integrating a computer vision library (YOLOv8) with a Chrome extension, which is not a common combination. We're also proud of the user-friendly interface we created, which makes it easy for anyone to use GetRecipe. Another thing we are proud of is our organization abilities and constant communication amongst each other. What we learned We learned a lot about developing Chrome extensions, including how to interact with the browser's API and how to handle file uploads. We also gained experience in integrating a computer vision model with a web application. What's next for GetRecipe In the future, we plan to improve the accuracy of the machine learning model and add support for more types of food. We also want to add features like saving favorite recipes and sharing recipes with others. <div