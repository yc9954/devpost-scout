---
slug: "glados"
url: "https://devpost.com/software/glados"
title: "Glados"
hackathon: "Junction 2017"
winner: true
words: 671
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Glados

> Traffic sign maintenance requires lot of time and effort. Lets automate that with deep neural networks!

[Devpost](https://devpost.com/software/glados) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** docker, node.js, python, react-native, tensorflow, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for glados

## Body

Inspiration If walking around an area and judging the condition of traffic signs take most of your productive hours, your valued skills are wasted. This problem came up when we had a chat with Stara. We immediately felt that something could be done for this. What it does People from Stara work with their phones. We built an app that streams live video from the user's phone to our traffic sign detection server. User films the streets, from her car, while driving around the city. We process the video live and when a traffic sign is recognized we save it with its GPS coordinate. Later, from all the stored pictures of traffic signs user determines which ones need repairing and which not. When pictures of traffic signs are processes we generate suggestion which could be the optimal route for the repairman to go. This means also that user can see from the map the most problematic areas that have a lot of work. For proof of concept we only detect stop signs. Other traffic signs are discarded. So all in summary: Improve efficiency by allowing user to just drive through areas while our service automatically detects and records signs with GPS coordinates. Enable user to check detected signs and mark them if some of them need further actions - like maintenance. Show optimize route for user so that maintenance work can be done as efficiently as possible. How we built it Our mobile app is built with React Native. It enables quick prototyping and cross-platform support (it means it can be used with iOS and Android!). Behind the app, we have lightweight server solution with a convolutional neural network for traffic sign recognition. Our backend is written in Node and deployed with docker images. Challenges we ran into We were able to scope the problem well on service level (app, image recognition, backend). The unfortunate part was the integration which turned out to be a bit trickier than we thought. We tried image recognition first with pre-trained model. It was promising but eventually turned out to be a big disappointment due heavy overfitting. Because of these problems, we ended up building our own model from scratch. Eventually it turned out to be a good model but a lot of time was wasted on the implementation challenges of the tool, Tensorflow, that we used. Eventually, limitations of that framework made other parts of our architecture hard to implement as well. Accomplishments that we're proud of Our mobile app. Beautiful, solid UX and great visuals. Definitely the eyecatcher of our project. Our focus and endurance. Our team literally worked from dusk till dawn without losing its spirit for a moment. Image recognition. Being able to build up a model that recognizes traffic signs with thin background on deep learning truly gave us a confidence boost. Even though we had little experience on deep learning we were able to scope problem wisely and got good results. There were many setbacks, but we always found a solution or some alternative way to overcome those. Innovativeness. This is embedded in our team. There where many sudden challenges that we couldn't estimate. We still found a way to go forward. Pain-free cloud environment with Docker images and Terraform. Proper DevOps is a thing that you don't want to neglect, even if you are in a high-speed hackathon. When you have solid foundation it feels safer to develop on it. What we learned We all wanted to learn something new and we truly had that experience. Diving deep into neural networks was a scary and challenging. Developing mobile after years of web development wasn't a walk in a park. With the right attitude and hard work we outdid the learning curves of CNN, React Native and many other tools that were not that familiar to us. What's next for Glados We feel ambitious and want to take SignVision to the next level. Now we know this can be done... all we need is time and hard work. <div