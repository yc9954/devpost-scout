---
slug: "jump-ar5890"
url: "https://devpost.com/software/jump-ar5890"
title: "Jump!"
hackathon: "Hack the North 2020++"
winner: true
words: 1002
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Jump!

> A competitive multiplayer exercise game that makes it fun and easy to stay fit with friends through the internet.

[Devpost](https://devpost.com/software/jump-ar5890) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** flask, gcp, ios, posenet, python, swift, swiftui, vonage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jump!

## Body

Jump! logo Compete to win! Rewatch past matches Game join screen Workout selection screen Leaderboard screen Inspiration Since the start of 2020, it's become increasingly difficult to get into shape. Gyms around the world have been closing, and a higher degree of social isolation has made it hard to stay motivated to keep fit. Unfortunately, if you're forced to stay home, it can be tough to stay on track with your fitness schedule, get feedback from friends and trainers, maintain proper form during exercises, and have fun while exercising! Recognizing that exercise is much more engaging when you do it with friends, we decided to create a fun multiplayer exercise experience, called Jump!. What it does We've built a real-time multiplayer competitive exercise game powered by computer vision where you compete by staying healthy. Two users can compete with each other to complete a sequence of exercises (ex. push ups, squats, etc.) via a live link, and our app detects their current pose and analyzes this data to determine when they have correctly completed the exercise. Think Just Dance, but with exercise and you don't need to be in the same room. How we built it The iOS app was built with Swift, primarily using the SwiftUI framework to create our views, animations, and menus. We made extensive use of the Vision framework to apply the PoseNet pose estimation model to track the users' movement in realtime with six degrees of freedom. This data was used to track when users performed the correct exercise move (ex. a push-up). The Vonage API was used to create a video/audio link to the other player, which enabled users to work out together online in realtime as well as to store recordings of the exercise section. We also built a backend with Python and Flask that we hosted on Google Cloud. Google Cloud allowed us to use continuous deployment for a seamless development workflow and provided fast and reliable hosting. The primary purpose the backend served was to coordinate running games and synchronize the current game state with the phones in real-time, and to allow the phones to communicate with each other. The Vonage API was used extensively here as well, in Vonage session management for the frontend, game state sharing through the signal API, and video/audio archiving for each exercise game, allowing users to rewatch and analyze their past matches. Challenges we ran into Building a real-time, online multiplayer component: due to the large amount of information we needed to quickly communicate between the two devices, it was a significant challenge to coordinate the video calls from the backend, and then connect both iOS apps to a single connection, while also recording the stream and transferring state information about scores and exercises between the two devices. This necessitated a lot of work with websockets to enable the constant stream of communication that was necessary. Optimizing performance while running both a video call stream and pose estimation/tracking: It took a significant amount of effort to get both running simultaneously in an efficient manner. We had to dig deep into iOS's AVFoundation API to enable non-standard functionality that was necessary for our use case. Furthermore, we also delved into the Vonage API's extensibility as we had to implement some protocols with custom implementation to have both our computer vision pipeline and our video calls work off the same video capture session. Accomplishments that we're proud of UI Design and Tactile Feedback: We spent a significant amount of time designing and then refining our user interface, incorporating haptic feedback, sound and a slate of animations to create the best possible user experience. We also implemented special effects during exercise routines using particle systems to create confetti when a user finished a stage of the routine. Exercise Motion Detection: To enable our core feature of detecting users' exercise movements, we built a highly extensible system that enables the rapid definition of any exercise movements by specifying the angles and relative distances between key joints on a users' body. This enabled us to transfer the work done on enabling one exercise movement to many others, and makes the system far more generally applicable. What we learned Computer Vision: We learned how to effectively apply PoseNet, a computer vision model for six degrees of freedom (6DOF) body pose tracking to track the users' movements during their exercise routine. This was the first time we'd worked with real-time computer vision inference, so it was an interesting experience to work on optimizing performance, visualizations and more. Reactive + Declarative Programming: We used SwiftUI, a reactive and declarative framework for building user interfaces based on application state. For some of us, this was the first time we'd worked with SwiftUI (and iOS development in general) so it was a great learning opportunity that helped us expand our skillsets. Video Calling: While we'd worked with video in apps before, this was the first time we used a live 2-way stream to enable video chat between two users. Thankfully, the Vonage API helped us enable a high fidelity stream, and we had the opportunity to go in depth with the AVFoundation API to capture and display these streams. CI/CD: We decided to take advantage of Google Cloud's CI/CD tools with our backend to allow us to constantly have the latest version of the backend deployed whenever the code was pushed to GitHub. This significantly accelerated our development workflow and helped us iterate rapidly. What's next for Jump! We've envisioned a couple of improvements for the app that we think can further improve the experience. Foremost amongst these is adding support for groups larger than 2 players. This would create an even more entertaining experience and help larger groups spend time together. Another improvement would be to give users editing tools for their clips, to integrate information like the final score and special effects. Finally, we'd like to integrate caloric tracking and interface with the HealthKit API so that users can log their exercise over time. <div