---
slug: "maria-primachenko-legacy-15-puzzle"
url: "https://devpost.com/software/maria-primachenko-legacy-15-puzzle"
title: "Maria Prymachenko legacy puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 292
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Maria Prymachenko legacy puzzle

> We wanted to showcase Flutter's exceptional cross-platform capabilities, as well as tell the world about Maria Prymachenko (Ukrainian naïve artist), whose museum was recently destroyed by Russians.

[Devpost](https://devpost.com/software/maria-primachenko-legacy-15-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets


**stack** dart, flutter, wikiart-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maria primachenko legacy 15 puzzle

## Body

Launch screen Artworks selection About an author Puzzle screen Puzzle screen variation 2 Puzzle screen variation 3 Win screen Inspiration Inspired by incredible works of Ukrainian favorite naïve artist — Maria Prymachenko. We are a fully Ukrainian team, no wonder that the recent loss of works saddened us deeply. We decided to commemorate her legacy in this small puzzle challenge. What it does Our 15 puzzle allows users to browse a selection of Prymachenko's paintings and play a 15 puzzle with the one that the user chooses. App also has sections about the artist and basic info about each painting to educate users who know nothing of Maria's legacy. How we built it We revamped key elements of the sample code while adding more animations, extra screens, and designs on top of it. Challenges we ran into All artworks are provided by WikiArt(under the fair use license ). Naturally, we wanted to use its API. However, for the web platform, we ran into the CORS security problem, which is unsolvable without backend API modification. We decided to save all the artworks as JSON and ship them in the app bundle. Accomplishments that we're proud of Overall project UI/UX, especially on mobile. Support for drag user gestures, which was a bit tricky to implement. What we learned We learned a ton about Flutter web and mobile differences, a few new widgets, and of course, we learned a lot about the artist. What's next for Maria Primachenko legacy 15 puzzle We want to fix the CORS issue by adding a proxy server that would communicate both with WikiArt API and Puzzle App in the correct way to make the app more dynamic. Also, we want to polish animations and UX for the puzzle. <div