---
slug: "loroa-audible-translation-api"
url: "https://devpost.com/software/loroa-audible-translation-api"
title: "Loroa - Audio Translation API"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 633
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/developer"
---

# Loroa - Audio Translation API

> Generate dynamic audio translations on the fly using the power of Amazon Graviton2, Amazon Polly, and Amazon Translate! Use Loroa in your app to include multilingual functionality with ease.

[Devpost](https://devpost.com/software/loroa-audible-translation-api) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[media_journalism]]
**user** [[developer]]

**stack** amazon-ec2, amazon-web-services, php

## How they structured the write-up

- inspiration
- what it does
- how we built it
- practical use case
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for loroa - audio translation api

## Body

Front end for quick translations. Instructions on how to use the API in your projects. Screen from Roku Application used in the demo. Screen from Roku Application used in the demo. Inspiration "Loroa" is the Basque word for Parrot! With the ever increasing demand for applications around the world to be available in multiple languages, developers need a quick way to generate translations at any given moment. Solutions of the past would have required developers to install SDKs and tie them together to not only translate, but also generate spoken words. Loroa saves development time by providing an easy-to-use API that can be quickly called upon in any application to provide accurate, translated soundbites. What it does Loroa translates any given text into spoken words from one language to multiple other languages. An API service is provided that will allow developers to easily retrieve audio translations on the fly. Potential use cases: Translation or dictionary apps. Games that need to provide multilingual or accessible features. Applications for visually impaired people. eLearning platforms. There is a front-end side that can be used for demo purposes, but developers will want to send POST requests to experience the full functionality of the app. You can include multiple target languages in your requests to receive multiple simultaneous translations. For example, if your application's original language is English, simply include requests for Spanish, French, and Portuguese all in a single request to receive three separate audio files. The application is hosted on the Amazon Graviton2 EC2 instance accessible here: http://52.15.100.90/loroa/frontend.php A single translation can be obtained as an mp3 file, and multiple translations are packaged as a zip archive. Thanks to the next generation Graviton2 processors, these file operations are lightening fast! How we built it Loroa is hosted on an Amazon Linux t4g.micro instance, powered by Arm-based AWS Graviton2 processors. Using the AWS SDK for PHP, Loroa calls upon Amazon Translate and Amazon Polly to produce precise translations that are then used as sources to generate text-to-speech audio files. Encoding the sound data as mp3s and bundling multiple files into zip archives is handled by PHP file operations, which have increased speed and performance due to the Graviton2 processing power. And because the instance is hosted on the same region as the other Amazon technologies it relies upon, latency is extremely reduced. I've included a Postman collection that can be used to demo the service as well. Practical Use Case I created an app for Roku TV called "Translate Spanish" that is currently available on the platform. This app now uses Loroa to provide the translated audio, and has shown a remarkable increase in speed after migrating away from competing third-party TTS solutions. You can see this in action by watching the demo video! Challenges we ran into Installing all the components that I needed, such as a web server and the PHP libraries took a bit of time, but once these were configured, I was able to focus more on the coding side of this project. Accomplishments that we're proud of I'm proud of the different Amazon technologies used in this project: Amazon Translate, Amazon Polly, and EC2 instances combined are the foundation of Loroa. Because of all the amazing features that the AWS SDK provides, I was able to find less friction points that I probably would run into if I had used other third-party solutions. What we learned It was my first time using EC2 instances, so learning how to connect and configure was a bit of a learning curve, but well worth it. What's next for Loroa - Audio Translation API I'd like to incorporate more features of Amazon Polly, such as the "newscaster" style voice. I'd also like to integrate more languages, as the current selection is limited due to time. <div