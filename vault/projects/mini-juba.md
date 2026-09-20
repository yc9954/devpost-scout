---
slug: "mini-juba"
url: "https://devpost.com/software/mini-juba"
title: "SpotifySocial"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 384
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# SpotifySocial

> Improve and expand user interaction and connectivity on Spotify

[Devpost](https://devpost.com/software/mini-juba) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets


**stack** gsql, python, spotifyapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mini juba

## Body

Inspiration Inspiration for this project came from our personal desire and interaction with the Spotify App. Music is inherently social, and we believe that this graph solution improves people’s quality of life by enhancing their musical experience through increased interaction and the ability to find people with similar music tastes. What it does This project aims to provide a framework, built on TigerGraph, which Spotify can implement to improve the interaction between their customers by determining how similar a user’s music taste is to their friends/other users. Potential features which Spotify could implement; user similarity scores, see common artists/genres between users, discord/subreddit style channels for people to share new music and interact, public user following recommendations. These features could be implemented by querying the network of users which has been built in TigerGraph. How we built it In this project, example user network data has been extracted from Spotify using the Spotify API and loaded into a TigerGraph instance. To determine the similarity of user’s music a query can be run which calculates the number of shortest paths (either length 2 or 4) between users, where the greater the number of paths, the more similar their music taste. In addition to this, a user’s song attributes (e.g., danceability, tempo, valance etc.) can be aggregated in order to determine what “type” of music they listen to. The design of our TigerGraph schema was focused on setting up nodes based on aspects we wanted to filter on. For example, we wanted to be able to filter track connections between users based on certain features of the track, and therefore, we split the features of tracks into separate nodes. Each edge then contains the elements that connect its nodes. Challenges we ran into The Spotify API gave us limited access to information. This meant that we could only access user information about our personal accounts which scaled down the data we could upload to our graph. Accomplishments that we're proud of The potential use case for this, we believe is significant. What we learned We interacted with the Spotify API for the first time. We expanded and developed upon our python skills and learnt GSQL. What's next for Mini Juba We will continue to use and improve upon the skills that we developed during this project <div