---
slug: "stemsense"
url: "https://devpost.com/software/stemsense"
title: "StemSense"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 301
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# StemSense

> StemSense is an online website that gives users the ability to scan objects they have access to and feed that information to the site to come up with creative science experiments!

[Devpost](https://devpost.com/software/stemsense) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[video_visual]] [[web_dom]]

**stack** gemini, googleaistudio, openrouter, python, uitralytics, vscode, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stemsense

## Body

Inspiration Underserved communities across the world have a lack of proper education, primarily due to limited resources. This website allows users to be able to be able to take advantage of what they had in a resourceful way that minimizes waste and fuels STEM growth. What it does The website first lets the user have 10 seconds to show their camera to the kinds of objects that they have. Then, the user can edit the list in case the AI recognition software misses any object or misidentifies anything. They can also choose which model they want to use and also add a custom prompt if needed. Then, the information is passed on to the LLM and a new page opens up with the resulting experiment for the user to try out! How we built it The website itself is built with React.js, HTML, and CSS, but many of the core fundamentals (including our YOLO model that runs locally) is built on Python. Running the model locally allows us to protect the user's privacy as well. Challenges we ran into Sometimes, the YOLO model would pick up on objects that wasn't there. Also, we sometimes struggled with the integration with Gemini. Accomplishments that we're proud of We are proud of being able to complete this project in such a way that its able to work with both forms of AI as a complete product! What we learned We learned that about how to use API keys and connect them so that they run effortlessly! We also got more experience with using GitHub and making apps. What's next for StemSense Improvements we hope to make include AI-generated diagrams for the experiments, step-by-step explanations for experiments, and support for other languages. Having more model options could help too, alongside tuning the YOLO model. <div