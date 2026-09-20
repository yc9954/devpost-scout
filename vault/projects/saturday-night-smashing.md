---
slug: "saturday-night-smashing"
url: "https://devpost.com/software/saturday-night-smashing"
title: "Tuesday Night Tempo"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 376
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Tuesday Night Tempo

> A fun interactive music game that uses a real drum set as the controller.

[Devpost](https://devpost.com/software/saturday-night-smashing) · hackathon [[Hack the North 2021]]

## Facets


**stack** arduino, c#, unity

## How they structured the write-up

- domain names
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tuesday night tempo

## Body

Domain names smashthdrum.tech tuesdaynighttempo.tech keepthetempo.tech Inspiration Our inspiration for creating this game came from video games such as Friday Night Funkin and Guitar Hero. These games tend to test the gamer's hand eye coordination and we wanted to create the same experience except with a real set of drums. What it does Tuesday Night Tempo is a fun interactive game. In order to control the game, the user will interact with a real drum kit but only these four parts: the hi-hat, the crash cymbal, the snare drum and the bass drum. The user will be able to choose whichever given songs there are. Once a song is selected, notes will begin to move from the bottom to top. In order to score points or do well, the user must hit the according part of the drum kit at the same time the notes hit the white line. Any earlier and it will be a miss and any later it'll be a miss so, don't rush, don't drag and be on tempo! How we built it In order to create this game, we used the Unity game engine (C#). For hardware, we used Arduino Leonardo hooked up to sound detectors in order to get the sounds for the different drum parts. Challenges we ran into One of the big challenges we ran into was being able to detect the hitting of acoustic drums without sound bleed (e.g. bass drum being detected in the snare mic). This is especially tough considering the big difference in amplitudes across the kit. We went through many methods including frequency processing, hardware filters, etc. In the end, getting it right at the source was the way to go by strategically attaching and isolating microphones. Accomplishments that we're proud of Creating a polished, working project that we think is really cool. Also, having tons of fun and getting to play the drums as part of our testing! What we learned Sometimes, it's better to not overcomplicate things :). There was a simple solution to our sound bleed problem and we definitely could have solved it earlier if we took the simple solution. What's next for Tuesday Night Tempo Adding more songs and harder beats, getting some more mics for the toms. <div