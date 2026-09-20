---
slug: "bus-off"
url: "https://devpost.com/software/bus-off"
title: "Bus Off"
hackathon: "Junction 2016"
winner: true
words: 438
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# Bus Off

> An interactive mini-game pairing up bus stops around the world.

[Devpost](https://devpost.com/software/bus-off) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[video_visual]]

**stack** computer-vision, deezer, ejs, javascript, node.js, python, sass

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bus off

## Body

bus off Inspiration We've all seen the viral AD campaigns of Coca Cola, flash mobs around the world and cool tech used to sell products. We wanted to make the bus stop wait less boring and tedious, lets get people dancing with Bus Off! What it does Bus Off pairs you up with a random bus stop somewhere in the world and generates a random sequence of songs. You must then hit markers appearing on the screen in order to score points against your opponent. The player who gets the most points wins! How I built it We use computer vision to construct a skeleton of the player from a webcam feed, using this skeleton we can calculate the relative distances from the person to the point and calculate whether a person has hit a point. Node JS and socket sessions share game state between clients. Microservices Audio-Merge Using Python, Request and Flask to implement a genre and BPM based API for Deezer. Allowing us to generate full mix tracks from Deezer's 30 second previews using Pydub. Skel-Gen Using Python, OpenCV and Socket.IO we remove the background of a video stream based on optical flow. This data can then be abstracted into a skeleton and sent back to the frontend. Finally, the frontend can detect if the body intersects the current markers and give the user a point. State is stored on the server meaning many clients are supported (more bus stops woo!!) User-Match Using NodeJS, Express and Socket.IO we match users at bus stops around the world. The first person to hit 10 perfect moves wins the game and, I'm afraid, the other loses. Challenges I ran into Streaming HD video over Websockets is hard, especially with ~2.5Mbps upload. We instead segmented the video into important regions, reducing the data requirements by ~ 50x. We also send back a skeleton model that is significant smaller than a video feed, allowing a smooth gameplay experience. Accomplishments that I'm proud of Game state is shared between clients seamlessly, we've achieved relatively accurate skeletal tracking with only a single web cam, we've accounted for both portrait and landscape screens and webcams and we've generated BPM matched mix tapes using the free tier Deezer API. What I learned Websockets, EJS, Computer Vision, Python and a million other things! What's next for Bus Off Let's get integrated in billboards and bus stops around the world, why not integrate this with Twitter? Send an embarrassing video of you and your new best friend dancing. The advertising potential is huge and we'd love to work with a marketing agency to make this happen. <div