---
slug: "into-the-galaxy"
url: "https://devpost.com/software/into-the-galaxy"
title: "Into the galaxy"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 341
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
---

# Into the galaxy

> API for the stars

[Devpost](https://devpost.com/software/into-the-galaxy) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]]

**stack** postman, rest, sia, skynet

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for into the galaxy

## Body

GIF cat_intranet.gif Inspiration We may be living in the decade where people are sent to Mars, with the first unmanned SpaceX Starship scheduled to leave for Mars in 2024, and a tourist mission around Moon in 2023. Without a direct connection to Earth's internet backbone, viral Tik Tok videos will likely not be streaming on your phones, even if you turn off airplane mode. What it does However, the technology exists today to make these apps work again in space. It is my pleasure to present to you the REST APIs to build apps for space. The first example will upload a cat meme to Skynet by Sia, a decentralized storage network. The second example will download the cat meme. The important mechanics happening behind the scenes is that during the upload and download, your device does not need to talk to big tech or telco servers. Allow me to elaborate. Below are 2 links. When you click link #1, it has to request the file from Google's servers. However, when you click link #2, Sia looks for the nearest computer that has the file. In fact, if you have a node in your home, the digital communication may not even have to leave your home to fulfill this request. https://drive.google.com/file/d/1-O3ZXy-V9xSoaJJfkJwUvXIbWfQFA7ms/view?usp=sharing https://siasky.net/vAM2RL1TlUx_gkkdj8LKnH2OAFgbLzbOLw3lPU69kA7SIQ So what are the implications. Sure, it can be built to power apps to work in space, airplanes, offshore ships. But it can also power IoT. Imagine all the devices can function within the bounds of the property, rather than depending on a server on the other side of the world. How we built it Postman, Sia Skynet Challenges we ran into If time permits, I would like to start up my Skynet node locally, and show you how I can still access data after unplugging from the internet. Accomplishments that we're proud of What we learned Cat meme from: https://gph.is/2Hs9JO6 What's next for Into the galaxy Please support the incredible people at Nebulous, Inc. and Sia Foundation, and enjoy the speed and freedom of Galaxy APIs! https://blog.sia.tech/skynet-bdf0209d6d34 <div