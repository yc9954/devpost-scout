---
slug: "fitness-voice"
url: "https://devpost.com/software/fitness-voice"
title: "Fitness Voice"
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 1025
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
---

# Fitness Voice

> AI voice-controlled trainer in your web browser, using NLP (wit.ai), body pose recognition and voice clone, with a privacy-based approach.

[Devpost](https://devpost.com/software/fitness-voice) · hackathon [[Facebook Hackathon- AI]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[video_visual]]

**stack** chart.js, html5, javascript, tensorflow, wit, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fitness voice

## Body

Welcome and help Home Doing sport Stats Yoga sample exercise Inspiration "Fitness Voice" was created to help all people who want to do sports at home, who now don't go to the gym for comfort or health. Normally when you're doing an exercise, you can't stop to touch the mobile screen or the computer screen, that's why I thought about using the voice in this project. In addition, "Fitness voice" checks your posture with artificial intelligence, to help you count the repetitions (example: surf training) and to help you do the posture well (example: yoga). Furthermore, "Fitness Voice" has been designed with privacy in mind from the beginning: webcam images aren't sent to the internet and voice is only sent after the wake-word "coach" has been detected offline. Finally, the app allows you to change the voice of the coach to be more customizable towards the user and so that the user is aware that technology currently allows doing this with the computer voice. What it does "Fitness Voice" is a fully voice-controllable webapp that helps you exercise. It allows: control the entire web application with your voice. choose the exercise you want to do: gym, surfing (arms) and yoga figure. helps you count the repetitions of the exercises, it uses deeplearning body pose recognition. helps you know if the yoga posture is correct. shows your total statistics by exercise. has a privacy-based approach. The web application is waiting offline to hear the wake-word "coach", and only when it hears that word then it sends the following words to wit.ai to do NLP. That is, this application will not mistakenly send conversations to the Internet, unless it hears the word "coach" first. In addition, the application allows to change the voice of the coach. These voices have been created with deeplearning. Change your voice for example and then do a surfing exercise. How I built it First I've used wit.ai to recognize the utterances of the user. I have trained the wit.ai model to understand these different intents: Lets go go home help me I want to train {gym, surfing, yoga} I want to change voice to {Bill, Her, Morgan, Joker ...} show me the stats Afterwards, I used tensorflowjs to detect the word "coach" offline. To do this, I have trained a model with different pronunciations of the word "coach". Then I used again the tensorflowjs library and the pretrained "posenet" model to detect the body in the webcam image, in realtime. Then I've tried to detect specific positions of the body and I've succeeded by looking at the relative position of the points of the body. After that, I used the "Real-Time-Voice-Cloning" library to modify the computer voice to allow the user to choose more familiar voices for the coach. This process wasn't totally realtime, so finally I've taken the most used sentences by the web application and I've cloned them for the 6 coach voices (clone voices created: Bill, Morgan, Morpheus, Her, Yellow and Joker). Finally, I've built the web application "Fitness Voice" that brings all this together. And I've added some fun details such as clapping sounds at the end of an exercise and the drawing of the sixpack on the webcam when the user reaches 10 repetitions in the surfing exercise. To indicate to the user when the web is listening, I've put the microphone animation. If the microphone animation is stopped, then "Fitness voice" is not listening. But if you say the wake-word "coach", then the microphone will start the animation until you finish saying the voice command, which will then be sent to wit.ai to "translate" it into something than the web application can understand. Also, to help the user discover what voice commands to say, "Fitness Voice" periodically suggests some. These suggestions can be read on screen (below the microphone animation) and suggestions can also be heard after some voice responses. Challenges I ran into The biggest challenge has been to synchronize the offline operation of the wake-word "coach" with the online operation of wit.ai recognition, with the main objective of guaranteeing the privacy of users. Now the code is very secure and only voice commands that are spoken after the word "coach" are sent to the internet. In addition to being more secure and offering greater privacy, this solution is also more efficient, because the number of requests to the wit.ai api is reduced. It has also been a challenge to work with other libraries that I hadn't used before, such as: offline speech recognition with tensorflow, posenet with tensorflow or Real-Time-Voice-Cloning for voice modification. I had not worked with wit.ai before either, but it was easy. Accomplishments that I'm proud of I am very proud of the product created, which is a totally usable webapp by voice, which is also useful (it is not comfortable to use a web/app with your hands while you are doing sport) and which is designed based on user privacy (using wake-word offline). Also, I'm very proud of all the technologies that I have used and that I didn't know before this project (wit.ai, posenet, speech recognition of tensorflow, clone voice, etc ...). What I learned I've learned that a web application can be made that is totally controlled by voice, and that the user and the web can have a conversation with natural language ("I want to train surfing", "show me the stats", "help me ", etc...). I have also learned to use wit.ai and other libraries that I didn't know before and that are very useful together in this project. What's next for Fitness Voice In the future, I want: Adding more different exercises. Detecting more different postures, such as yoga postures. Improving the statistics (so that they are not only global, but also statistics of progression and ranking among users). I want to continue training the wit.ai model. I have seen that the wit panel shows the phrases that the user says. I think this is very important to keep improving the application. I will periodically check this list to see what unsupported utterances users use. Thus, I will improve the model and add new features. <div