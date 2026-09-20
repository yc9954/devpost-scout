---
slug: "factoreyes"
url: "https://devpost.com/software/factoreyes"
title: "Factoreyes"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 765
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Factoreyes

> AI based web app that detects whether or not homework assignments are too repetitive.

[Devpost](https://devpost.com/software/factoreyes) · hackathon [[Funathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, flask, html, python, pytorch, transformers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for factoreyes

## Body

Front page of the website Output of the application Input image Inspiration Our project was inspired by the many homework assignments that we felt were very unhelpful in our learning experience but rather only made to keep students busy, and other software that has the ability to analyze math problems with artificial intelligence, like WolframAlpha. What it does The idea for this project is for it to be a website where teachers can upload a homework assignment, and be able to get feedback on how many of the problems on the homework are “new.” In its current state, it’s able to take in images of latex-rendered quadratic factoring problems and give some reasonable output and feedback to the user. How we built it This project was mainly built using python, flask, PyTorch, and the transformer library by huggingface. There are a couple of parts to our project. First, we made a website that uses the flask framework for a frontend to our application. On the backend, there are three main parts. Number one is a text OCR which was capable of separating the math problems with bounding boxes around them. Number two is a model that can convert images to latex formatted strings. Number three is a model that computes information about the math problem, which will ultimately be used in our similarity calculation. For the former two models, we used pre-trained transformer-based models from huggingface, and for the latter model, we used a recursive neural network (not to be confused with a recurrent neural network). For the recursive neural network to be able to read the input, we had to convert the expression into a binary tree. Challenges we ran into We ran into a fair bit of problems during our project. Figuring out how to make and host a website was a big problem. Neither of us had prior experience in web development so, we were learning as we went. Also, due to a limited budget, it was difficult to find a good hosting service for our website. Another problem that still persists in our project is our application's inability to detect math expressions when the user inputs an image. For expression identification we used an open source OCR model. It didn’t prove very effective and had multiple issues with identifying the expressions properly. This caused our application to have very low accuracy, which we should be able to fix with more time. Accomplishments that we’re proud of We were both proud of the skills that we learned during the making of this project, as neither of us had any prior experience in web development. We were also both surprised by the accuracy of the model when we tested it with direct inputs. It was cool to see that our model had actually learned something from the data we gave it. What we learned Some skills that we improved on while making this project were our CSS and HTML skills, as prior to making this project, we had little knowledge of them. We also improved our skills with web development with python, as we were also relatively inexperienced in this matter. In addition to the extra practice we got in practical skills, a major lesson we learned when making this project was to not reinvent the wheel. When trying to convert rendered latex expressions back into latex, we tried making and training our own model, but we realized that it was hard to do given less than 2 days to do it. What's next for Factoreyes In our project, we focused on factoring problems. If we had more time we would have liked to include other types of repetitive math drills. This might consist of analyzing problems with rational functions, trig functions, logarithms, and the ability to manipulate transcendental constants like pi. The main accuracy bottleneck of our application was its inability to scrape the expression off the images. We used a computer vision model that we found online, and a lot of the time, it misinterpreted or didn’t recognize the expression, leading to a significant decrease in overall accuracy. In the future, it would be beneficial to create and train our own model instead, specifically for math problems. This would greatly improve the accuracy and performance of the overall application. In addition to the problems listed above, we also hope to incorporate Natural Language Processing into our application. Many math problems come in a word problem form, or with some set of instructions with natural language, so having the program be able to interpret word problems, etc. would be very helpful. <div