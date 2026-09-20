---
slug: "quiz-rush-ajeync"
url: "https://devpost.com/software/quiz-rush-ajeync"
title: "Quiz Rush"
hackathon: "Reddit Games and Puzzles Hackathon"
organization: "reddit"
winner: true
words: 567
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Quiz Rush

> 10 seconds, 1 answer. Can you keep up?

[Devpost](https://devpost.com/software/quiz-rush-ajeync) · hackathon [[Reddit Games and Puzzles Hackathon]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[educator_student]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, devvit, html, javascript, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for quiz rush

## Body

Home About Our Devvit Project Inspiration The inspiration for our project came from the desire to create something that enhances user engagement on Reddit while utilizing the capabilities of Devvit. With Reddit being a platform that thrives on communities, we wanted to build an app that could bring value to these communities, helping them interact with content in a more personalized and efficient way. Quiz Rush isn’t just a game; it’s a platform for user-generated content where Redditors create questions, build challenges, and fuel engagement. With time-based scoring and leaderboards, we turn Reddit's vibrant communities into arenas of knowledge and excitement. What it does Our project, Quiz Rush, is a quiz app designed to be integrated into Reddit, offering users an interactive way to test their knowledge on various topics related to their favorite subreddits. The app allows users to: Create and take quizzes created by subreddit members or the app itself. Compete for high scores and view rankings. It serves both as an entertaining tool and a way for users to engage deeper with their communities. How we built it Devvit Framework Setup : We started by exploring Devvit, setting up the environment, and reviewing the documentation to understand the available features and integration methods. The process of connecting the app to Reddit’s API was seamless after some initial setup, and we integrated the backend using Redis for storing user data and quiz results. Frontend and Interaction : The frontend was designed to be simple and intuitive, with easy navigation between quizzes and results. The app integrates directly with Reddit’s comment sections and voting mechanisms, allowing users to engage with quizzes without leaving the Reddit interface. Testing & Deployment : After building the core features, we spent significant time testing the app to ensure smooth operation. Debugging was crucial, especially when dealing with outdated code from the AI bot and performance issues related to Redis queries. Challenges we ran into Learning Curve with Devvit : As beginners to Devvit, we encountered some challenges understanding its structure and best practices. Limited tutorials and documentation required a lot of hands-on learning, making it slower to progress at first. Complexity of Post Messaging : The process of using post messages to communicate between the webview and the Reddit block became cumbersome over time. Simplifying this interaction to directly communicate with Reddit’s API would have made the app more streamlined. Accomplishments that we’re proud of Successfully built and deployed a functional app integrated with Reddit, offering a unique and engaging experience for users. Overcame the complexities of working with Redis and Devvit’s framework, learning new technologies and tools in the process. What we learned Devvit Framework : While the learning curve was steep, we gained valuable insights into how Devvit works and its potential to create dynamic applications within Reddit. Debugging and Problem Solving : We learned how to troubleshoot errors and adapt to new technologies, ultimately improving our debugging skills and our ability to find solutions independently. What’s next for Quiz Rush Support for Images : Ability to add images to questions for enhanced engagement. Bug Fixes : Addressing issues like information not loading properly and posts failing to load occasionally. More Events and Game Modes : Adding more events and new game modes, such as "Who Wants to Be a Millionaire?" Add Multiple Questions : Allow users to add multiple questions at once for easier quiz creation. <div