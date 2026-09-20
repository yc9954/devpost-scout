---
slug: "quickmark-arjq6v"
url: "https://devpost.com/software/quickmark-arjq6v"
title: "QuickMark"
hackathon: "Hack the North 2020++"
winner: true
words: 545
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# QuickMark

> Marking tests shouldn't be slower online than in person. QuickMark uses computer vision to split test questions into groups that can be marked efficiently.

[Devpost](https://devpost.com/software/quickmark-arjq6v) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** computer-vision, css3, html5, javascript, node.js, opencv, python, socket.io

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quickmark

## Body

A minimalist design website that focuses on easy, reliable usage. Super simple UI that allows for hassle-free marking, one question at a time. QuickMark Logo Inspiration In general, teachers are having difficulty teaching online during COVID-19, especially when marking digital tests. This is a result of many file types in different places, no good way to record scores or comments for each individual question, and even harder to return the students’ test back to them with the feedback. What it does Our solution to this problem is QuickMark , a fast , easy and reliable website that allows teachers to upload and mark all their students’ tests into one convenient place. After uploading all the tests, it uses computer vision to split test questions into groups. The teachers can then input a score below each test question, and can give comments if necessary. After they finish marking, the website takes all the data and puts it all in one convenient CSV file or table below, where it is categorized by each student’s name, the mark they got for each question, and then a total score. How we built it Using the OpenCV module in Python, our application automatically crops each question for the teacher to mark, saving them a lot of time and unnecessary stress. We also used Node.js and Socket.io as a middle man to connect the front-end with the image processing program written in Python. And lastly, our UI is built with vanilla HTML/CSS/JS to provide a minimalistic yet powerful experience for teachers. Challenges we ran into One of the major challenges we ran into was the connectivity between the various aspects of our project- from connecting the Node.js backend to the OpenCV functionality in Python, all the way to displaying it on our frontend in HTML/CSS/JS. Another challenging aspect was using OpenCV as a solution to identifying and cropping the questions. Although it required a lot of researching and reading at first, we were able to figure it out in the end. Accomplishments that we're proud of One of our main goals was to crop each question from the test so when we got the box detection and cropping to work, it was a huge moment of success. We even tested it with many worst-case scenarios such as faint box outlines, irregularly shaped boxes, and writing going over the boxes and it still worked effectively. What we learned Many of us were not entirely familiar with many of the frameworks/modules used in this project. OpenCV and the use of Node.js are just a few examples of new technologies we learned while building up our project. What's next for QuickMark In the future, we hope to implement OCR (using the Google Cloud Vision API) to detect each question in case they are not in order. We also would like to add in the ability to comment on each question and to create a system to send the scores and comments back to the students. Finally, we would like to incorporate QuickMark with the Google Classroom API as many tests are turned in on that platform and to make it compatible with the Google Education Suite. Special thanks to our teachers for allowing us to use their test questions for the sample test! <div