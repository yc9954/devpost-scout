---
slug: "speed-scribble"
url: "https://devpost.com/software/speed-scribble"
title: "Speed Scribble"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 753
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Speed Scribble

> Drawing game where players compete 1-on-1 to replicate a picture on a virtual whiteboard, judged by AI

[Devpost](https://devpost.com/software/speed-scribble) · hackathon [[Hack the North 2021]]

## Facets

**domain** [[health_clinical]] [[transportation]]
**user** [[frontline_worker]] [[legal_professional]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** cockroachdb, flask, google-cloud, google-compute-engine, javascript, opencv, python, react, tailwindcss, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- business viability
- what's next for speed scribble

## Body

Winning! Drawing a masterpiece Waiting for an opponent to join Inspiration This game was inspired by Scribble.io, which is an implementation of online Pictionary. We made the game unique by adding a 1-on-1 competitive element, providing players with a reference image that they need to remember, and judging the drawings using machine learning. What it does Allows users from anywhere around the globe to play against each other in a fast-paced battle of drawing an object by memory, only to be judged by a cold hard machine 🤖 Quick and simple match-making by sharing a link that opponents can simply open to join the game Players are also able to replay the game as many times as they please! Replays will automatically connect to the same opponent if both players choose to play again. How we built it Used a pre-trained TensorFlow machine learning model, ImageNet, for feature extraction to identify patterns and shapes in the reference image and compared those features to our drawn images. A cosine similarity function was used to calculate the similarity between the two lists of features, i.e. reference image compared to drawing #1 and reference image compared to drawing #2. For the frontend, we created a React single-page application with TailwindCSS for style and layout. We also used Vercel’s SWR library for data fetching on the frontend, which reduced the time spent developing the React app. The backend API server was built with Python, Flask, and SQLAlchemy with a CockroachDB driver. It also uses Tensorflow and OpenCV for image similarity comparison. We are hosting the Python REST API backend on Google Compute Engine and we leveraged Google Cloud Storage solution to host doodles drawn by players. We are also using CockroachDB to store the game state, including games, players, and drawing details. We prototyped the UI design and overall game flow using Figma, which allowed us to plan the flow out in advance and thus lead to a lower-friction experience. Challenges we ran into When processing reference images, we found that some images that had more texture (such as feathers on a bird) produced a lot of noise in the image showing an edge map. While we did implement filters such as the Canny Filter and attempted to use the Median filter to minimize ‘salt and pepper’ noise on our edge map, the thresholds for more detailed images was different from the simpler cases. We had to diagnose why the image similarity comparison was performing poorly in order to identify noise as the main cause, but we also explored updating to a newer machine learning model that could potentially produce better results. The new model did not work initially, so we had to debug it by examining the data as it traveled through the pipeline and adding a missing transformation. Accomplishments we're proud of Successfully implemented a similarity comparator for two images which enabled us to evaluate the accuracy of user-submitted drawings Getting a full-stack app working decently well in a short amount of time, especially coordination between the backend and frontend What we learned Learned how to use filtering algorithms to denoise an image Some of us learned how to use Flask and/or React Learned about the powerful tools available as part of Google Cloud Platform for both object storage and compute VMs Learned how to create a simple CockroachDB database cluster Business Viability This game is likely interesting to people who want to play a quick competitive game with their friends and/or improve their drawing skills on a computer. Premium users could be offered perks such as priority matching on a global leaderboard, the ability to create games with large numbers of players, more advanced drawing tools, and other convenient features such as built-in voice chat (for premium hosts). By adding user accounts and premium features, the game could be monetized while simultaneously improving the experience significantly for premium users. Companies could also sponsor us by providing reference images related to their characters and products (e.g. Mickey Mouse for Disney), banner advertisements, and other links that can be presented in-game. Sponsored reference images can be used more often and weighted depending on the sponsor amount, so more generous sponsors will get more exposure. What's next for Speed Scribble Improve similarity calculations by improving the model and exploring more advanced noise reduction algorithms Support for multiple players Global leaderboard with automatic match-making Adjustable time limit and more advanced drawing tools, so players can opt for a quick and easy game or an intense drawing session <div