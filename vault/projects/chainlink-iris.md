---
slug: "chainlink-iris"
url: "https://devpost.com/software/chainlink-iris"
title: "Chainlink Iris"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 369
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Chainlink Iris

> Chainlink Iris is a tool that allows people to create custom, video-based data feeds to be used with Chainlink in smart contracts.

[Devpost](https://devpost.com/software/chainlink-iris) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chainlink, docker, flask, javascript, opencv, python, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink iris

## Body

Chainlink Iris Thumbnail Chainlink Iris Event Dashboard Chainlink Iris Logo Inspiration It is very difficult to get data about a live event onto the blockchain without having a custom solution build to either get that data from specific software/hardware or a trusted third party. I wanted to create a way for people who might not have a whole lot of technical experience to get data onto the blockchain without learning how to build a specific API for their use case. That is where the idea for Chainlink Iris came from. What it does Chainlink Iris uses computer vision to take data about real life events and turn it into on-chain data. Users can stream video of an event to the Chainlink Iris website, and the site will extract data from the video frames based on a defined policy. This data is then made available using an external adapter an chainlink oracles. How we built it The server was built in python using a flask server. The html page that streams the video sends a frame every few milliseconds to an endpoint that processes the image and saves the state of the event in a postgresql database. The computer vision is done using opencv and pytesseract. The frontend is a very simple react application that was styled using tailwind. All of this is orchestrated using docker and docker-compose Challenges we ran into I'm still working on the external adapter portion of the project so that the chainlink iris API can be called from smart contracts. This has been the most difficult part of the project aside from getting the computer vision to play nicely. Accomplishments that we're proud of I'm proud that the version of Chainlink Iris I am submitting actually is able to read text from the streamed video and make it available as JSON on an endpoint in real time! What we learned I've learned a whole lot about computer vision and edge detection in this project. I've also learned a lot about the basic chainlink infrastructure, very cool stuff! What's next for Chainlink Iris Getting a public external adapter up is currently the number one priority. I've included some other future milestones in my presentation slides <div