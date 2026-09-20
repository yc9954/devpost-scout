---
slug: "smart-teacher"
url: "https://devpost.com/software/smart-teacher"
title: "Smart Teacher"
hackathon: "AWS Marketplace Developer Challenge: ML Powered Solutions"
organization: "Amazon"
winner: true
words: 652
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Smart Teacher

> Browser extension that uses NLP and Machine Learning to automatically generate MCQ based quizzes and smart notes for educational videos in youtube and other ed-tech websites.

[Devpost](https://devpost.com/software/smart-teacher) · hackathon [[AWS Marketplace Developer Challenge- ML Powered Solutions]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** amazon-ec2, amazon-marketplace-web-service, amazon-web-services, aws-comprehend, aws-transcriber, javascript, mphasis-summarizer-aws-market-place, nltk, python, s3, sagemaker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart teacher

## Body

NLP and AWS Machine Learning services are used to automatically generate smart quiz from video. Smart quiz helps a user in evaluating their understanding of the concepts explained in video. Smart notes is generated automatically from video using NLP and AWS Machine Learning services. This helps a user in revising the concepts. Inspiration In the midst of COVID-19, the whole world has realised the power of online learning and the impact it can have on millions of students. Be it K-12 or higher education, virtual learning is talk of the town. Although there are plenty of video lectures available online and usage is extravagant, often these lectures can get too long, monotonous and quite frankly, boring! People zone out frequently and lose track of what's going on. They end up rewinding the video and watch again which really is a waste of time. In this process, there is a lack of feedback; there is no one to test you if you've really understood what you've been listening to. What if there was a mechanism to evaluate the understanding? Also, not every student like to take notes. But all of us need something to refer to before an exam. What if there is someone who can automatically generate notes for you while you concentrate on listening to the lecture in the video? What it does We have built a web browser extension that automatically generates a quiz and smart notes for videos in YouTube and other EdTech websites using NLP (Natural Language Processing) and Machine Learning. A user can self-evaluate their understanding by taking the quiz while watching the video. Each question presents the user with an option to move back to the part of the video from where the question was generated. This will help the user in revising the concepts which they weren’t able to understand when they watched the video the first time. We also generate smart notes and summary for the video. Our smart notes also provide meanings and examples for certain key words in the notes so that a user can easily understand the overall content of the notes. User can also click on any sentence in the notes to navigate to the point in the video from where the concept summarized in the sentence is explained. How we built it We used AWS services such as AWS Sage Maker, AWS Transcriber, AWS Comprehend and AWS MarketPlace model 'Mphasis DeepInsignts Text Summarizer' along with python packages nltk and gensim to automatically generate MCQ based quiz and smart notes from the speech in the video. Backend code is deployed on a Linux EC2 instance. Challenges we ran into Initially, we were using open source speech-to-text converter which were not very efficient at generating high quality text output. We replaced this with AWS Transcribe due to which we are able to generate high quality notes and quizzes. We combined this with Market Place model and AWS Comprehend to choose most important sentences from the video. Accomplishments that we're proud of We consider every aspect of the project as an accomplishment as it was a new learning every step of the way. What we learned We were able to explore different NLP libraries, their capabilities and restrictions and different AWS market place solutions and how to use such already existing solution in our project to improve its efficiency. What's next for Smart Teacher We want to add several new features like the following: Capture screenshots of diagrams and formulae from the video using Computer Vision and add it to Smart Notes. From the notes generated automatically, user should be able to create their own notes or customize it. In smart notes section, we want show links to relevant websites to read more about the central topic of the video. Generate pre-requisites - add links to learn about most important sub-topics on the video as pre-requisites Generate Non MCQ based quiz <div