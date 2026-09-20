---
slug: "copycat-ir98wa"
url: "https://devpost.com/software/copycat-ir98wa"
title: "CopyCat"
hackathon: "Hack the North 2020++"
winner: true
words: 694
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# CopyCat

> The pose memory multiplayer online game!

[Devpost](https://devpost.com/software/copycat-ir98wa) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** flask, html, javascript, numpy, opencv, posenet, python, tensorflow, tokbox, vonage

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for copycat

## Body

Intro Slide Demo Slide Logo for our project Our website's home page Inspiration Two of the most ubiquitous aspects of life in lockdown are video calls and online games, and we were inspired to create something that would bring the two together. CopyCat is based off of a teambuilding exercise, where players successively copy one another's actions, adding a new action each time. We thought it would be an interesting and rewarding challenge to use computer vision to recognize and detect similarities in these actions. What it does Players join the game by opening a web app and joining a room, which is similar to a video call. At the start of each round, the current player must correctly perform all previous actions in the correct sequence. The video is recorded and sent to the PoseNet OpenCV model, which calculates the similarity between the video and the previous sequence of actions. If the player successfully performs all previous actions, they get to add their own action to the sequence. Otherwise, the player is eliminated. In either case, the game moves on to the next player. The game continues until there is only 1 player remaining. How I built it Our game has two major components. It includes a front-end using the Flask web microframework. For user interfaces, we used HTML with integrated scripts written in JavaScript. The front end uses the Vonage Video API to integrate a video call into our website. Using this API, we obtain recordings of the current participant. This recording is passed to the back-end through a link. Our back-end consists of a Game class, which stores a video of the previous poses. It processes the video by downloading it from the link, unzipping it if necessary, and extracting the newest action before passing it to the computer vision model. The computer vision pose detection algorithm is built using Tensorflow and OpenCV in Python, alongside the Posenet dataset to establish the key points of the body. Calculation of deviation uses dynamic time warping library DTAIDistance to ensure that actions are compared accurately regardless of speed or time differences between videos. Challenges I ran into Our biggest challenge was connecting the various components of our application. While our front-end, back-end, and computer vision model work well individually, we had trouble sending messages between them. As such, the user experience is still unpolished. We also faced many issues with running our code, as the computer vision model in particular had many dependencies that were sometimes incompatible with those already installed on our computers. Some of us had to go as far as updating and restarting their laptop before they could run the code. Accomplishments that I'm proud of We were very proud of the algorithm we used to effectively calculate the similarity between actions. We experimented with several alternatives, such as cosine similarity and cross-correlation, but ultimately went with an algorithm that combined multiple approaches and normalized the images. This reduced the influence of body size, speed of movement, and location in the frame on the similarity of actions and improved accuracy. We were also proud of how we built a project that was both interesting to us and useful for other students during lockdown. University is tough and staying at home can get lonely, so forging connections between people through a game form their childhood is rewarding for us as well. What I learned We explored various algorithms that could be used to calculate the similarity between different poses. To get the most out of the algorithm, we learned how to use posenet to identify body parts and we experimented with preprocessing to ensure that the poses are centered in the images we used. Furthermore, we learned how to use the Vonage Video API as well as Flask. Finally, some of us were unfamiliar with using JavaScript purely in the form of embedded scripts. What's next for CopyCat Currently, we only support one game room. When using the website, all users join the same video call. In the future, we would like to let users create multiple rooms, so that more people can play our game at the same time. <div