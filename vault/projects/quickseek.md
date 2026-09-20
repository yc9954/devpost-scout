---
slug: "quickseek"
url: "https://devpost.com/software/quickseek"
title: "QuickSeek AI"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 485
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# QuickSeek AI

> QuickSeek is a browser extension that lets you easily search YouTube videos using AI.

[Devpost](https://devpost.com/software/quickseek) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[voice_speech]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** amazon-comprehend, amazon-transcribe, amazon-web-services, aws-lambda, css, html, javascript, machine-learning, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for quickseek

## Body

Transcribing Video Search Sentiment Analysis Inspiration When watching tutorials, lectures or any video on YouTube, I usually come across long videos, sometimes I don't need to watch the entire video but only specific parts of it. If I want to find when a word was mentioned in a video, I could use the seek bar to guess the position, but that becomes very hard especially on really long videos. What if there was a way to search the video and quickly find what you're looking for? That's where QuickSeek comes in. What it does QuickSeek is a chrome extension that allows you to easily search and navigate through a YouTube video, you can quickly find and watch only parts of the video that contain words you are looking for. The Chrome extension uses Amazon Transcribe to make the audio searchable and Amazon Comprehend to perform sentiment analysis on the transcript. How I built it I started with the Chrome extension which was built with Javascript, HTML, and CSS. The backend is a set of Lambda functions written in python. The Chrome extension sends the video ID from the browser through an API gateway which triggers the first Lambda function. The Lambda function gets the download URL from YouTube using a Python library called Pytube, the Lambda function will also send the video directly to an S3 bucket. The Chrome extension will call another API gateway to start the transcription process on the video using Amazon Transcribe. The transcription process can take a while, so the Chrome extension will check to see if the transcription process is complete or still in progress. When the transcription process completes the Chrome extension will call an API gateway which will trigger another Lambda function to get the transcription data. The function will also perform sentiment analysis on the video and return the data back to the Chrome extension. The video file gets automatically deleted after the process completes. Challenges I ran into I ran into a lot of small challenges while building this app, one big challenge was figuring out how to get the video from YouTube directly to an S3 bucket and figuring out which two A.I services to use. Another challenge I ran into was the 5000-byte text limitation of Amazon Comprehend. Accomplishments that I'm proud of I'm glad it actually works! when I started this project I wasn't even sure if it would be possible to implement such an idea within a short period of time. What I learned I learned a lot about the AWS machine learning services. What's next for QuickSeek Next, I plan to make it possible to save the transcript data locally on your PC so that you can search the same video without going through the transcribing process again. It would also be cool to try out Amazon video Rekognition to allow label, activity and celebrity detection in YouTube videos. <div