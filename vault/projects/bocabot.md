---
slug: "bocabot"
url: "https://devpost.com/software/bocabot"
title: "Bocabot"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 782
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "domain/legal_justice"
  - "user/developer"
---

# Bocabot

> Speak to anyone in the world, in any language, in real-time for FREE!

[Devpost](https://devpost.com/software/bocabot) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[housing_homeless]] [[immigration_refugee]] [[legal_justice]]
**user** [[developer]]

**stack** django, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bocabot

## Body

logo icon Inspiration As a child of immigrants, and a person whose first language is not English, I have never taken for granted the amazing gift my parents gave me of being bilingual. When I lived in Central America in 2006, the people overwhelmingly welcomed me into their countries with open arms and open hearts - often inviting me, a stranger, into their homes for food and shelter. When I saw the heartbreaking video of Central American children, separated from their parents at the border, defending themselves in court , I knew I had to do something. Ideally, of course, I would find a way to prevent the situation altogether. However, searching for immediate solutions within my abilities, my initial thoughts were to see if I could somehow volunteer as a translator. But knowing that my Spanish languages were probably not sufficient, and trying to brainstorms ways that I could help, I searched for viable, technical solutions utilizing my strongest skillsets - my technical abilities as a software engineer. In the video of the children in court, they are all wearing headphones, and I thought it would be great if they could communicate in real-time, in their native language. Enter Bocabot. What it does Bocabot is a webapp that can translate over 50+ languages. Bocabot also has Speech-To-Text (STT) and Text-To-Speech (TTS) capabilities in over 50+ languages. In order to use STT and TTS, you must enable your browser's microphone, and use a browser/device that allows access to the microphone. At time of press, iOS (iPhone, Safari) blocks the browser's access to the microphone and speakers, however, Chrome browser on MacBook works. Regardless of the platform/device you are using, Bocabot can be used like an ordinary text messenger, to send and receive messages. How I built it I always build all my applications as lightweight as possible, in an effort to make it available on more devices and platforms, and for faster runtimes, less overhead, easier maintenance, robustness, to minimize any costs, and hopefully be able to make it available for free! Bocabot is a Django/Python application, and the frontend is written entirely in vanilla Javascript and JQuery. The Speech-To-Text (STT) uses SpeechRecognition , the Text-To-Speech (TTS) uses SpeechSynthesisUtterance , and translation is accomplished using Googletrans - all free and/or open source services, available for unlimited use. Challenges I ran into Most of the challenges that I ran into were related to Speech-To-Text (STT) and Text-To-Speech (TTS), due to the varying levels of access allowed by different devices/browsers, and due to the fact that even those devices/browsers that do allow access to the microphone and speakers require SSL (https, versus http). Another challenge that Bocabot faces is scalability. Because I am currently self-funding the project, it is hosted on a simple webserver, which has limitations for the number of users and data it can hold. It is also a major bummer that iOS does not allow browser access to the microphone. Accomplishments that I'm proud of I am really proud to be able to offer Bocabot, free of charge to anyone who wishes to use it. In a world where over 90% of us can communicate with less than 10% of the rest of world, I am surprised that such services aren't more ubiquitous. Coincidentally, while building Bocabot, I came across a video presenting Google PixelBuds, a device that is similar to Bocabot's services. However, of course, Google's PixelBuds cost in excess of $150, which is not luxury that most of the world can afford. My dream is to have the opportunity to port Bocabot into a simple gadget, and offer it for free to those who need it. Porting Bocabot into an Arduino or RaspberryPi device, would be trivial and could be built for around $25. What I learned Demoing Bocabot to several of my friends, I learned about the many different use cases that Bocabot could be (have been) used for. Every person that I showed Bocabot to, told me how useful Bocabot would be (is) for them. Even in 2018, so many of us face obstacles related to language barriers and communication on a regular basis, but with Bocabot, we could change this, today! What's next for Bocabot I would love to have the resources to move Bocabot onto a more scalable platform (a larger server that could withstand a large number of users), have a UX/UI design expert to improve Bocabot's frontend (which I designed myself :), and to be able to port Bocabot onto a simple, hermetic platform and offer it to those in need, especially those in the midst of the horrific immigration situation, and anyone who faces a nightmare situation, due to language barriers. <div