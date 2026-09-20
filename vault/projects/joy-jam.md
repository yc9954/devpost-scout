---
slug: "joy-jam"
url: "https://devpost.com/software/joy-jam"
title: "Joy Jam"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 618
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Joy Jam

> A skill for musicians. Jam along with your own virtual band! Isolate and mute instruments while you play along with songs from all genres and moods.

[Devpost](https://devpost.com/software/joy-jam) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: web_dom</sub>

**stack** apla, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for joy jam
- a bit more info

## Body

Check out https://www.joyjam.me to create your own custom track. You must provide URLs to isolate mp3 files for each instrument. Inspiration As a professional musician myself, I was inspired by the new APL for Audio capabilities provided by Amazon. The Mixer component offers the ability to play multiple simultaneous tracks, which inspired this project. I quickly realized that this new feature set would allow for a new field of tools that could greatly benefit musicians. I've worked as a touring musician as well as a self-employed developer, which I believe gives me a unique perspective on what musicians expect from technology. What it does Joy Jam is a rehearsal tool for musicians, developed by a musician. It plays backing tracks which can be used to practice along with, or write new music. The key feature is that it allows the user to mute or isolate specific instrumental tracks. So for example, if you are a guitarist, you might just want to hear bass and drums and do not want to hear the current guitar track in a song. Joy Jam will allow you to turn off that guitar track so you can play along with your own. How I built it I composed 10 demo tracks in all different moods and genres (blues, country, rock, jazz, etc). I programmed the skill to play songs by track name, number, genre, and musical key. I also developed a playback method using the new Alexa Presentational Language for Audio Mixer component to allow for the muting of select tracks. **UPDATE: 5 new tracks have been added in the genres of Electronica, Indie Rock, Garage Rock, Chill Hop, and Reggaeton. Challenges I ran into There was a bit of a learning curve with this project being my first Alexa skill. Some things were intuitive, coming from experience with JavaScript, but learning how intents and utterances work alongside code proved to be challenging at first as this was all new territory for me. Accomplishments that I'm proud of I'm proud of how quickly I was able to put this project together after being inspired. Despite a few technical limitations that I discovered along the way, I was able to adapt to the conditions as they are to create a skill that I believe pushes the boundaries of what is possible with Alexa. I look forward to other developers being inspired by this endeavor, which may lead to bigger and greater projects in the future. What I learned I learned a great deal about the intricacies of the new beta APLA capabilities. I found a few limitations that I hope will be addressed by Amazon in the future. For example, there is a limit to how long an audio message can be, and there can only be up to 4 tracks at a time being played back using the Mixer component. If we could increase this number, there would be opportunities to include more robust tracks in this skill such as a 20 piece orchestra, which would require simultaneous playback of 20 tracks. What's next for Joy Jam I plan to expand the amount of tracks offered and I'm currently working on the ability to add user custom tracks. This will greatly increase the value of Joy Jam, with users being able to contribute to this project. **UPDATE: I was able to implement the custom track feature in the most recent update (as of Dec 24, 2020). Currently, you must provide your own hosted mp3 links, but I will eventually very soon allow direct file uploads. A bit more info In the video link, you can watch me try out the skill and jam along on electric guitar, acoustic guitar and bass guitar. <div