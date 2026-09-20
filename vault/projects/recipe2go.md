---
slug: "recipe2go"
url: "https://devpost.com/software/recipe2go"
title: "Recipe2Go"
hackathon: "Hack the North 2020++"
winner: true
words: 650
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Recipe2Go

> A web app that auto-generates food recipe from your favourite cooking youtube video !

[Devpost](https://devpost.com/software/recipe2go) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[document_pdf]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** cockroachdb, css, figma, flask, google-cloud, html5, opencv, python, vultr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recipe2go

## Body

Landing Page 1 Final Page Loading Page Architecture Inspiration It's quarantine time, we all stuck in their place don't know what to eat for dinner, but we also had a hard time following the youtube cooking video where we have to keep track of each step and come back to the video for more info. Introducing the Recipe2Go! A fast and convenient way for you to cook your food during this unique time period by getting your fast recipe. Our goal is to let everyone conveniently cook their favorite food without spending too much time checking a specific time frame of a video. Most of the popular cuisine is complicated, so we want to build a system to automate the process of creating a single detailed recipe for everyone so that they can easily follow and enjoy the cooking experience. What it does Recipe2Go is a web application that uses computer vision and natural language processing tools to auto-generate a detailed recipe for anyone who wants to quickly start cooking! How we built it For Recipe2Go, we have separated the front end and back end. Our frontend was wireframed on Figma and developed with HTML, CSS, and javascript. Our backend was coded in python with flask as our back-end framework to implement our API and infrastructure. Our user info and processing history were stored in cockroachDB because it's resilient and scales fast. To improve our overall architecture, we use Redis as our metadata cache and Celery as our task queue to reduce the latency and increase the overall throughput. Our project is running on Kubernetes and we deployed the project on vultr which is our hosting service. Recipe2Go uses cutting edge technologies such as frames differences by OpenCV, and bayesian network to receive the keyframes, divide and separate videos into different keyframes. Furthermore, we leverage the functionalities of the fPDF library to publish these contents to the final generated recipe in PDF format.Recipe2Go also uses Youtube-transcript-API to extract the subtitles of a video and divide them into different steps based on the starting time of each keyframe. In addition, we leverage Google Cloud's Natural language APIs to extract keywords based on the analysis of entity sentiment and then filter out everything except ingredients and equipment so that we can publish them to the final file as well. Challenges we ran into We spent a lot of time trying to divide the video into the correct steps with the correlated contents. The core functionalities on how we divide and separate videos into different keyframes were the most challenging part out of all the components. How to get the correct procedures and ingredients from the video. We spent a lot of time on how we can use the entity sentiment analysis to determine some keywords and then filter out the correct ingredients. We also had a hard time with setting up Redis and Celery because they are new technologies Accomplishments that we're proud of The model that we used to find the frames differences within the video was a huge accomplishment. Also, our solution to make sure all the procedures are correct and aligned with the image is also a big one. What we learned We learn so much about OpenCV2 as a group and Google Cloud's APIs related to AI and NLP. We also learned about Kubernetes and Celery as a team which is new technologies for everyone. What's next for Recipe2Go We definitely need a more optimized model to improve the accuracy of our content. We also need to focus on the improvement of our existing algorithms in object detection and natural language processing. Security can also be improved where we build an additional authentication system for our users. Our product can also be improved by adding more features such as searching for a specific generated file from the past and share the recipe on the social network platform <div