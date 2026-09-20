---
slug: "mashme"
url: "https://devpost.com/software/mashme"
title: "mashme"
hackathon: "Hack the North 2020++"
winner: true
words: 405
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# mashme

> Pick two songs and mash them together! mashme uses intelligent stem-splitting to isolate the vocals, drums, and rhythm of each song, allowing the user to mash them together however they want.

[Devpost](https://devpost.com/software/mashme) · hackathon [[Hack the North 2020-]]

## Facets

**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** bootstrap, domain.com, flask, google-compute-engine, google-storage, mysql, python, spotify

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mashme

## Body

Inspiration We're a team of 'music people' who are in a band together. We wanted to listen to our favorite songs in new ways, and we had the idea for mashme during a jam session. We decided that Hack The North was the perfect time to implement it. What it does mashme allows the user to select two songs, and isolates the stems (vocals, drums, bass, accompaniment) of each song, and matches their key and BPM. Then, the user can put stems together however they want to create songs that have never been heard before. How I built it Backend: Python, Flask Front-end: HTML, CSS, JavaScript, Bootstrap APIs: Spotify, Youtube Platforms: Google Compute Engine, nginx Audio Technology: Spleeter, Rubberband, pydub Storage: MySQL, Google Cloud Storage Source Code: https://github.com/Richardyang510/hackthenorth2021 Challenges I ran into The primary challenge is insufficient processing capacity, because this is expensive! Currently, the site is fully funnctional, but a user must wait two or more minutes for the mashup to begin playing after clicking 'Submit'. For the same reason, there can only be a few users at a time. However, as a workaround to expensive processing which is inaccessible to us, we have cached all songs that have been processed previously. If you begin typing a song and see it appear in the dropdown, click it. With two pre-cached songs, the mashup will begin playing immediately. Large file sizes with large processing times. Splitting the song into stems and performing audio transforms were costly operations, taking several minutes. We implemented caching using a database and Google Cloud Storage, so subsequent runs for a mashup is available instantly. Synchronizing the audio on the front end was a challenge, as the default HTML audio player was designed for one track at a time. We utilized the webaudio library to build an audio buffer with all the tracks synchronized. Accomplishments that I'm proud of Succeeded in making working mashups with a clean user experience! What I learned File transfer has unexpected pitfalls that are often expensive. This requires creative thinking to reduce the load on both the front-end and back-end. What's next for Mashme ML training for chorus and verse separation! Currently, mashme separates different stems in a song, but through ML training it could allow the user to mashup song parts in addition to track types. Think of the verse from one song, with the chorus from another song, recognized through intelligent machine analysis. <div