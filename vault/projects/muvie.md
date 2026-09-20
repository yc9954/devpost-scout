---
slug: "muvie"
url: "https://devpost.com/software/muvie"
title: "Muvie"
hackathon: "Junction 2017"
winner: true
words: 331
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/structured_db"
---

# Muvie

> Do you struggle to choose a good movie? Can't you find the right movie for tonight? We have the solution: Muvie!

[Devpost](https://devpost.com/software/muvie) · hackathon [[Junction 2017]]

## Facets

**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** api, flask, html, javascript, python, pythonanywhere, sqlite

## How they structured the write-up

- inspiration: sometimes, when you don't know how to express your emotions, feelings: you play songs that correspond to your status. so we thought, why don't we choose a movie based on the last few songs we heard?
- what it does
- how we built
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for muvie

## Body

Muvie Inspiration: Sometimes, when you don't know how to express your emotions, feelings: you play songs that correspond to your status. So we thought, why don't we choose a movie based on the last few songs we heard? What it does Muvie gets your recent played songs on Spotify and reads your mood; then it recommends movies based on these moods. How we built First, we train our movies database to cluster them based on emotions. Second, we select the last listened user's songs using Spotify API. Third, we search and analyze songs' lyrics and we discover the most relevant emotions. Forth, we compare emotional vectors of songs with those of movies in the database. Fifth, we suggest and show a list of movies corresponding the mood. When you click on the poster, you can also watch the trailer. Challenges we ran into It was hard to find a good emotional dictionary and then a perfectly match between emotions and movies/songs. Users may also listen to weird songs or songs with no lyrics. Accomplishments that we're proud of Clustering algorithm: we managed to find a good match between emotions and songs/movies. User Interface: interactive webapp in which user can login with his/her Spotify account and see the list of suggested movies. Functioning prototype that could explain our basic idea. What we learned How to build app using different API, e.g., Spotify; implement a clustering algorithm utilizing emotional dictionary; help each others, work under-pressure, but also have a lot of fun together. What's next for Muvie Our next steps are: analyzing songs not only based on lyrics, but also on Audio properties and user preferences (movie already seen or corresponding to overall taste profile: mix or usual suggestion with emotions and current moods); improving the quality of the algorithm by analyzing words based on their meaning within the context of the sentence; adding buttons for appreciating how is the matching between the mood and the movies. suggesting songs based on movie. <div