---
slug: "spellcam-fpvlhm"
url: "https://devpost.com/software/spellcam-fpvlhm"
title: "SpellCam"
hackathon: "XHacks 2021"
organization: "XHacks Organization"
winner: true
words: 667
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# SpellCam

> SpellCam changes ASL education by leveraging computer vision to teach ASL in a fun, interactive way, offering its users real-time feedback on progress and correctness through a custom-built CNN.

[Devpost](https://devpost.com/software/spellcam-fpvlhm) · hackathon [[XHacks 2021]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** python, swift, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spellcam

## Body

Inspiration To many, American Sign Language, or ASL, is just another language. But to a deaf community of 430 million people globally or at least 5% of the world’s population, ASL is not just another language, but a necessity in life to be able to communicate with their loved ones. Yet, less than 1% of the US population are able to use ASL, and in many ways, the language is dying as funding for ASL education falls steadily. Soum and I, have long wanted to learn more about the language to better support our local deaf community and raise awareness of this issue to our friends and family, some of whom themselves suffer from hearing loss. However, we found several issues with existing solutions. First, existing tutorials are expensive. Some comprehensive courses we found online for ASL cost over 600 USD! Second, as students who underwent extensive online learning, we found existing teaching methods to be unintuitive. Namely, almost all courses online were taught through video lectures, with no real-time feedback to the learner on technique or correctness despite these being very important for proper ASL communication. Thirdly, the lack of interactive learning software was widespread. In fact, in our own search on the App Store, we found exactly ZERO applications offering any form of teaching beyond basic video lectures, much less any applications built and designed like SpellCam. What it does SpellCam leverages our own custom convolutional neural network trained and derived from the MobileNetV2 architecture to be able to classify in real-time ASL fingerspell signs being held up by the user. In this way, users know immediately whether the sign they are currently holding up is correct or not, giving them the real-time feedback and interaction missing from video lectures. Furthermore, we were inspired by Quizlet and flashcards, building in such functionality for flashcards to help our users more quickly and effectively learn ASL components. How we built it We used TensorFlow and Python to create the convolutional neural network derived through transfer learning on the MobileNetV2 trained on ImageNet. Following this, the model was converted to a CoreML model, which when combined with the Swift front-end inspired by flashcards and Quizlet, allows for real-time classification of signs held up by the user, and a fun and effective learning strategy! Challenges we ran into We ran into many unexpected bugs and errors in our conversion and use of the CoreML model from TensorFlow to Swift. For example, one such bug failed to be able to scale images and frames to the 224x224 requirement of the model. To handle some of these, we even had to custom re-write some existing Swift functions to allow them to work successfully in our application! Accomplishments that we're proud of Our machine learning model worked very well, achieving over 99% accuracy on our cross-validation and test sets! We are also happy with our UI designed and built from scratch on Swift, and how we were able to ultimately merge both the model written in Python/TensorFlow and the front-end written in Swift successfully. What we learned Soum and I both learned tons on applications of machine learning and mobile app development through building for XHacks, and also developed our skills working with many libraries on these fronts. More importantly, we learned how to communicate and collaborate effectively as a team despite the challenges of COVID hampering the possibility of in-person work! What's next for SpellCam We are already thinking up ideas of gamification into the application, and now plan to work further on developing a real-time multiplayer racing game within the application where users can compete against other players in a speed competition for fingerspelling different words and sentences correctly! Also, while we believe fingerspelling is a great start by offering users the ability to quickly communicate to the deaf community and to raise awareness of the language, we are also looking into adding more components of the ASL language to the application to create an even fuller learning experience! <div