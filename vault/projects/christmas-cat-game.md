---
slug: "christmas-cat-game"
url: "https://devpost.com/software/christmas-cat-game"
title: "Christmas Cat Game"
hackathon: "AWS Game Builder Challenge "
organization: "Amazon"
winner: true
words: 631
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Christmas Cat Game

> Control Your Christmas Cat with Voice and Hands! 🎄🐾 In Christmas Cat Game, jump with high pitches, flatten with low pitches, and use hand detection to phase through walls.

[Devpost](https://devpost.com/software/christmas-cat-game) · hackathon [[AWS Game Builder Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** apigateway, cloudfront, cloudwatch, dynamodb, iam, lambda, react, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for christmas cat game

## Body

Welcome page Score Submittion Real-time Leaderboard Christmas Cat Game Inspiration I wanted to move beyond the usual mouse and keyboard controls to create something more engaging. My goal was to design a game that lets players use different parts of their body, like voice pitch and hand gestures , to control the character. This approach not only makes the gameplay unique but also challenges players' reaction abilities in an interactive and refreshing way. :joy: What it does The game offers a dynamic and immersive experience by challenging players to control a cat using their voice and hand gestures. The voice detection system distinguishes between pitch ranges to trigger specific actions: a low-pitch voice (50-150 Hz) at a defined intensity causes the cat to flatten and avoid obstacles, while a high-pitch voice (500-800 Hz) makes the cat jump to overcome challenges. Additionally, when the camera detects a hand gesture, the cat gains the ability to pass through walls, adding another layer of interactivity. To enhance the competitive experience, an AWS-powered leaderboard tracks players' scores in real time, creating an engaging and lively environment for players to compete and improve. How we built it We built the game using the following technologies and services: 1. DynamoDB : For storing player scores in a leaderboard table. 2. API Gateway : For managing GET and POST requests to update and retrieve scores. 3. Lambda : For executing backend logic to process leaderboard data. 4. IAM : To manage secure permissions for AWS resources. 5. S3 : For hosting static game assets and resources. 6. CloudFront : As a CDN to enhance performance and load times. 7. CloudWatch : For monitoring and debugging AWS services. 8. Frontend : Built with the React framework for an intuitive and visually engaging user interface. 9. Hand Detection : Implemented using MediaPipe's Hand Detect model to recognize and process real-time hand gestures for in-game interactions. 10. Pitch detection : The audio detection analyzes microphone frequencies and triggers actions if intensity in specific ranges (50-150 Hz or 500-800 Hz) exceeds a threshold. 11. Pixi.js : For rendering 2D graphics and creating visually engaging gameplay elements. 12. GSAP : For handling smooth animations and transitions, enhancing the overall game experience. Challenges we ran into 1. Time Constraints : With limited time during the Hackathon, reading and fully understanding the extensive AWS documentation was challenging. 2. First-Time AWS Usage : As a first-time user of several AWS services, the learning curve was steep. 3. Role of Amazon Q : Amazon Q was like a knowledgeable teacher , providing quick and clear answers to questions derived from the official documentation. Through interactive Q&A, it helped deepen my understanding of how to use AWS services, saving approximately 50% of development time . Accomplishments that we're proud of 1. Successfully integrating voice and hand-detection technologies into the game to create a unique and interactive experience. 2. Leveraging AWS services effectively to build a scalable and reliable backend. What we learned 1. Gained hands-on experience with AWS services, including DynamoDB, Lambda, API Gateway, IAM, S3, CloudWatch, and CloudFront. 2. Discovered the importance of optimizing workflows and utilizing tools like Amazon Q to overcome technical challenges efficiently. What's next for Christmas Cat Game Here are two potential directions for the future of Christmas Cat Game : 1. Multiplayer Mode : Introduce a real-time multiplayer mode where players can compete or collaborate with others. This could include features like team-based challenges or a global leaderboard to enhance the competitive and social aspects of the game. 2. Enhanced Interaction Features : Expand the range of voice and hand gestures the game can recognize, such as detecting more pitch variations or complex hand movements. This would add more depth and variety to gameplay, making it even more engaging and challenging. <div