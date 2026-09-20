---
slug: "flock-figure-out-what-film-to-watch-with-friends"
url: "https://devpost.com/software/flock-figure-out-what-film-to-watch-with-friends"
title: "flock"
hackathon: "Hack the North 2020++"
winner: true
words: 514
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# flock

> Right swipe on films you are interested in watching, match films with friends and flock together

[Devpost](https://devpost.com/software/flock-figure-out-what-film-to-watch-with-friends) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]] [[video_visual]]

**stack** cockroachdb, dbeaver, expo.io, express.js, google-cloud, javascript, react-native, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flock: figure out what film to watch with friends

## Body

flock: figure out what film to watch with friends Swipe through movies. Right swipe for interest, left swipe to skip Inspiration Quarantine is a great time to watch movies online with friends, but it is often difficult to pick a film to watch. flock helps friend groups easily discover interests to share with each other. What it does flock is a mobile app that operates similarly to Tinder. Based on a user's genre preferences, they are given a list of films. For each film, they may indicate interest by right swiping. If another friend within the same group has also selected the same film, they will both be notified and prompted to set up a movie night. Users can join friend groups with a generated code. Additionally, they may create a friend group within the app simply by creating a join code. Users can find a list of all their matches with information on what film, and who they are watching the film with. How we built it We built the frontend of the application using react-native , and used expo to preview our work and debug. We implemented material design using react-native-paper . For the backend, we used CockroachDB to hold our data, and hosted it on the Google App Engine . We manipulated our data using SQL , and connected it to the frontend using Express.js . The backend acted as an API with a series of endpoints to allow for the frontend to grab data such as movies, users and groups. Overall, the database stored 6,860 movies across 27 genres with a total of ~25,000 rows for all of the data. Challenges we ran into Accomplishments that we're proud of This was a learning experience for all of us! Some of us worked with React Native and Expo for the first time, and some of us were introduced to backend and Express.js. We shared our knowledge over the entire weekend and have come out of it with new skills. Also, all designs, as well as the logo, are original works of art. What we learned What's next for flock: figure out what film to watch with friends For movie-picking Add more preference settings for users. For instance, allow users to select which streaming platforms are available to them. Allow the option to view all matches that are in a friend group so that a user can join the party even if they have previously shown disinterest for the movie Implement the ability to search for movies, so that fan favourites can be suggested to the group More than just movies flock doesn't have to be used just for deciding what film to watch. We hope to extend flock's functionality for more everyday decision-making dilemmas such as where to get takeout, what TV show to watch next, what book to read together... the possibilities are endless! A one-stop shop We can add texting and video calling into the app, using technologies such as the Vonage API, so that users can begin their movie watching parties without ever having to leave flock. <div