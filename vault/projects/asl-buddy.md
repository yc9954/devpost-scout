---
slug: "asl-buddy"
url: "https://devpost.com/software/asl-buddy"
title: "ASL Buddy"
hackathon: "Hack the Northeast"
winner: true
words: 496
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ASL Buddy

> Challenge yourself and learn some ASL in a fun, new way.

[Devpost](https://devpost.com/software/asl-buddy) · hackathon [[Hack the Northeast]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[structured_db]] [[video_visual]]

**stack** opencv, pygame, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for asl buddy

## Body

Inspiration Effective communication is important in all aspects of our lives. There are currently about 600,000 people in the United States who are deaf or hard of hearing. With the increased prevalence of accessibility options such as sign language interpreters at public events and concerts, our team realized that the basics of ASL, such as the alphabet, could easily be taught to anyone that was interested. Our goal is to give users a fun and interactive way to learn the alphabet while also promoting greater acceptance of the language. What it does ASL Buddy is a game that provides a new way to learn the ASL alphabet through the help of machine learning. The objective of the game is to obtain the highest score by correctly signing the most amount of letters in a row. The correctness of the user’s sign is determined by the neural network. Once incorrect, the game displays how to correctly sign the letter, and the user may start over to compete for the high score. How we built it We built ASL Buddy using Tensorflow, OpenCV, and Pygame. To train the neural network, we used Inception , a pre-trained deep learning convolutional neural network developed by Google AI’s team. We trained the neural network with a dataset containing hundreds of images of each letter in the ASL alphabet. We then developed our gaming interface, and used OpenCV to denote the image area, extract it, and process it before it is handled by the neural network. Externally, our gaming interface generates random letters, and keeps track of the user’s score based off of their accuracy in signing the random letters. Challenges we ran into The primary issue we ran into was setting up the model provided by Inception. Once we figured out how to test, it became clear that creating an accurate machine learning model would be difficult and time consuming. After reading a lot of documentation and trial and error, we were able to create a mostly consistent neural network. Nevertheless, because many of the letters in the ASL alphabet look similar, further training optimizations are necessary to create a more accurate model. Accomplishments that we're proud of We are proud of completing our first Pygame/Computer Vision/Neural Network project. We were able to finish the project we had planned, and also learn a lot on the way. What we learned We learned how to use Pygame and OpenCV, and Tensorflow. While learning each of these components was already a tough task, we as well learned how to integrate these frameworks together to create a working game. Also, we learned the ASL alphabet. What's next for ASL Buddy We would like to continue developing this project by increasing accuracy of our machine learning model by obtaining training data from the user. We could also begin integrating ASL phrases and words into the gaming platform. In addition, we would like to develop other game modes to further foster the learning of ASL. <div