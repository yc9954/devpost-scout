---
slug: "mobu-your-personal-movie-buddy"
url: "https://devpost.com/software/mobu-your-personal-movie-buddy"
title: "Mobu - your personal movie buddy"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 573
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/climate_energy"
  - "substrate/video_visual"
---

# Mobu - your personal movie buddy

> a cute movie bot that knows your mood and movie preferences, sees and speaks and even recites Shakespeare!

[Devpost](https://devpost.com/software/mobu-your-personal-movie-buddy) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**domain** [[climate_energy]]
**substrate** [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** amazon-dynamodb, amazon-ec2, amazon-web-services, android, ar, arcore, arkit, c#, ios, lambda, lex, mongodb, node.js, polly

## How they structured the write-up

- directions
- tech
- aws usage:

## Body

Mobu is your friendly empathy-powered movie buddy robot. Mobu is pocket-sized, but you can also "unbox" him and let him hang out in the real world with you! You can chat with him to find out the perfect movie for your mood. (Don't worry, he can also give you movie suggestions if you're not feeling moody. Mobu's chat is powered by Amazon Lex and his manly robot voice is Amazon Polly Matthew. You can download what he said to listen to it later. You can also touch the chat bubble to pop it and play 8-bit random piano! Mobu is connected to a movie database to pull synopsis, genre, posters and other structured data about the perfect film for you. Amazon Rekognition is used to extract people from the images you send to him, so that Mobu can play queer eye for you! We've strongly integrated Amazon Lex with persistence - Mobu doesn't just understand what you're saying. Mobu also remembers your preferences. Like, if I need to omit Colin Farrel movies - Lex knows that! Though, when you grow tired of movies and the slings and toils of life, you can always ask Lex to travel back in time, to the beginning of modern theatre. Mobu provides classic entertainment and can quote Shakespeare... with an Indian-English accent, powered by Amazon Polly. Mobu sounds so real, sometimes you forget that Mobu isn't strong AI, but just a bot made in the year 2018 for the AWS AI Competition. See you at the Singularity! Directions Grab the Android app (or iOS app) and load! The app starts in AR mode but you can easily turn it off to pocket mode using the top round box button. AR mode uses ARKit/ARCore like ground plane tracking, so wave your phone around like a magic wand to have it recognize where the ground is to place the robot there! Tap on the box to open it. Converse with mobu naturally to find out great movie recommendations. Mobu remembers your preferences and can even recommend movies based on your mood! Press the photo button and submit a celebrity photo to discover movies with that celebrity. You can also send the robot a selfie so mobu will know your mood and better recommend another movie. Tickle mobu. Press the box on the Shakespeare flap for Shakespeare. Be sure to turn your sound on! mobu sounds good, even great! Tech We developed the app to scale - just in case this humble robot gets more popular than its extents. The general philosophy is that most users have a supercomputer with an enormous amount of storage in their pockets, viz., their phone! As much common audio and AI content as possible is cached locally, to avoid hitting server surges and help with our AWS carbon footprint! Some local processing using iOS/Android speech to text is also done for speech input mode. Most bot logic is done through Lex. AWS Usage: Rekognition - celebrity rekognition, mood recognition for non-celebrities (your own selfie) Lex & Lambda - Lex was used to process user input whereas Lambda was used to process all the invocations from Lex NodeJs server sitting in an EC2 instance process all user requests. It will process incoming movie searched from Lambda Process incoming requests from the user and relay messages to Lex for processing Relay photo rekognition from user to AWS Rekognition service Store preferences from users using MongoDB <div