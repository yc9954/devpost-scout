---
slug: "skibidifier"
url: "https://devpost.com/software/skibidifier"
title: "Skibidifier"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 378
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
---

# Skibidifier

> Skibidify your video!

[Devpost](https://devpost.com/software/skibidifier) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[voice_speech]]

**stack** ffmpeg, flask, google-gemini, nextjs, python, shadcn, tailwind, typescript

## How they structured the write-up

- tracks
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skibidifier

## Body

Dark Mode Light Mode Skibidified video Skibidi Link to app! (I know you want to try it) Tracks best overall yay :3 would blow up on tiktok lowkey actually kind of good most likely meme startup skibidi ai swag Inspiration A few months ago I saw this video on YouTube about brainrot js by Noah Solomon and how he built it. I proposed the idea to my teammate and we started working on it. Like brainrot js, we were building this with the intention of generating videos for TikTok and free What it does Take a video and "skibidifies" it. Basically makes the video you put into a brainrot version of your video. Google gemini generates a brainrot script based on the video and Microsoft's free text to speech api makes the audio. You can select from the various voices available and the level of brainrot you want your video to be. How we built it We used NextJs , React and Typescript for the frontend, Flask and Python for the backend. We used various libraries like ffmpeg, lucid react, shadcn and google generative ai to aid the process. Challenges we ran into We ran into many challenges. We had to learn how to integrate ffmpeg to make videos programmatically. When hosting the flask server, we had first hosted on python anywhere which blocked the api call to Microsofts tts api. Finally we were able to host the flask server on render earlier today. Accomplishments that we're proud of Hosting! We did not think a project like this would even get shipped for people to use but we did it. It is so cool to show people what you have been working on for the past few days. This is something we can keep showing to our friends for a while 😂 What we learned How to programmatically make videos and How to host a flask server on the web What's next for Skibidifier Right now, Skibidifier only works for mp4 files. The video files on your phone are stored in an .mov file, so we plan to add support for more types of files. We would also like to add a preview of the voices, so that users will not have to experiment with each voice. <div