---
slug: "groupshot"
url: "https://devpost.com/software/groupshot"
title: "groupShot"
hackathon: "Hack the North 2020++"
winner: true
words: 674
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/agriculture_food"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# groupShot

> Take group selfies from the safety of lockdown. Try it out at https://groupshot.xyz

[Devpost](https://devpost.com/software/groupshot) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[agriculture_food]]
**substrate** [[video_visual]] [[web_dom]]

**stack** google-app-engine, javascript, tensorflowjs, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for groupshot

## Body

Gotta love groupShot! Star Filter! Woooahhh! Join/Create Room Mobile UI/UX Tired of Zoom? Wish you could celebrate in-person instead of seeing everyone in small-boxes on your screen? Then groupShot is the app for you. Capture memories together; apart. Inspiration As we continue to social-distance, family and friends celebrate milestones over Zoom instead of over the dinner table. As a result, it’s not surprising that photo albums have been slimming over the pandemic, with screenshots of "gallery mode" being the only group picture you can take. groupShot solves that problem by letting groups rediscover the fun of taking selfies together; even in a lock-down. What it does groupShot is the photo-booth of 2020. Have some fun and start a realtime photo-booth with your friends, colleagues, or loved ones. Join/create a room, pick your virtual background and filters, then strike a pose with your group. When you're happy with how it looks on your screen, capture the moment with a simple click. It's that simple. The photo will then be saved on your local desktop and in the app so that you can always look back at it. Since a picture is worth 1000 words, please see the image gallery below for details. How we built it Hosted on the Google App Engine, groupShot was created using WebRTC peer-to-peer communications. This lets groupShot users pose, position and preview their photos in live time. In combination with TensorFlow’s human segmentation models, all photos are fully customizable with backgrounds, filters, and mobility for users (they can move to the front, back, left or right of other users). Challenges we ran into The first challenge we ran into was finding a platform where this type of technology could even work. Spark AR and Snap Lens Studio were off the table since neither currently support network requests as part of their API. Looking to open source AR was the only way forward, and we're happy that we learned a new skill from it too. The biggest challenge we faced was combining the bodypix tfjs model with WebRTC connections. We were tasked with balancing three primary objectives: speed – the frame rate at which we can render the video accuracy – how well the model is able to crop you out from your background CPU efficiency – how loud your fan is going to be when you run this website (we startled a lot of beta testers this way!) We experimented with: Using a server as an MCU (Multipoint Control Unit) that mixes all of the streams into one by applying the ML model to each one as they come in, then sending back one feed to each of the clients. Running the ML model locally and then sending the resulting segmentation data over a P2P network Sending only video feeds over the P2P network, and running the ML model N times Unfortunately latency and costs made the first two completely unusable/infeasible, so we ended up compromising some accuracy and efficiency for acceptable speeds and an okay user experience. Accomplishments that we're proud of Proud that we were able to incorporate TensorFlow's human segmentation model into our app. While difficult, it was a great learning experience in understanding how adjustments and deployments are a large part in the dev process when working with any deep learning model. It was that model which was crucial in supporting our other key features (backgrounds, filters, layering) so we're happy we got it working in the end. What we learned Working with video is difficult; both in the size of data you need to process and the complexity of the requests sent. Leveraging existing tools and platforms can greatly expedite the development process however, and continual testing is a must to ensure the best user experience. What's next for groupShot Improve functionality on mobile. Continue to update with more backgrounds and filters. Work on optimizing load time and fine-tuning the model for human segmentation for greater precision. Expand groupShots capabilities to include more features common in video conferencing apps (i.e. screenshare, mute/unmute, on/off video). <div