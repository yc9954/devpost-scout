---
slug: "handwritingboard"
url: "https://devpost.com/software/handwritingboard"
title: "HandWritingBoard"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 505
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# HandWritingBoard

> Instead of one-way communication like on-demand delivery, this product that can easily and interactively communicate in real time with anyone who has white paper, black pen, and smartphone.

[Devpost](https://devpost.com/software/handwritingboard) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** api, css3, html5, javascript, react, redax, stylus, webrtc, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for handwritingboard

## Body

Inspiration Sometimes I feel a challenge in taking classes online or holding a meeting online under the influence of corona. In face-to-face classes and meetings, you can see the process that someone is writing on the whiteboard, handwriting on the board, and have another student or colleague write a note on it and discuss it. Although it is a trivial matter, there are many scenes where it is very inconvenient to not be able to do this, and it tends to be one-way communication and it is hard to say that it is in the usual environment. What it does All you need is white paper, a black pen and a smartphone. Members in the same room can see what they are writing at hand in real time and edit them together. Assumed usage scene 1.You can check the process in real time to find out what process your students are struggling with in order to correct them. Remote tutors can also find out where they are stumbling, making feedback easier. 2.Classes and breast meetings like going around the whiteboard with several people will be able to be done online There are a variety of tools like boards that can be edited together in the world, but I thought that the most important thing was to be able to share handwritten items in real time and edit them on the spot, so we focused on that point. We were also stuck on running on a browser without installing an app so that anyone could easily achieve this. How we built it 1.Confirmation of current issues. 2.Narrow down solutions to issues and prioritize functions. 3.Create output design with sketch. 4.Creating templates using html5 and css3. 5.Try to start a camera using Device API in smartphone’s browser and display the image of its camera on browser. 6.Binarize the image which is captured camera. 7.Send a binarized image to all users who open same URL using websocket. 8.Transparentize the white part of binarized image and display camera image under the binarized image. 9.The camera capture is binarized again, and the two binarized images are overlaid. 10.Send images from your camera to users who open the same URL on WebRTC. 11.You can now control which images are displayed on your camera or on the other party’s camera. 12.Connect the template to those system. Challenges we ran into Rather than thinking about development methods, it was hell to take turns developing a couple while taking care of our one-year-old daughter. Accomplishments that we're proud of Instead of one-way communication like on-demand delivery, this product that can easily and interactively communicate in real time with anyone who has white paper, black pen, and smartphone. What we learned We learned that the process of thinking about what is the root cause of what people feel inconvenient and how to solve it in a minimum time in a limited amount of time. What's next for HandWritingBoard Additional implementation of functions removed from requirements in this development ・Account linkage on facebook ・Room Entry <div