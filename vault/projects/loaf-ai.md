---
slug: "loaf-ai"
url: "https://devpost.com/software/loaf-ai"
title: "loaf-ai"
hackathon: "BitRate: Machine Learning & Music Series"
winner: true
words: 436
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# loaf-ai

> Streaming lo fi hip hop in the browser with Tone.js and Magenta's Music RNN improvising on acoustic guitar. Produces unique 15-minute-long jams to study/work/relax to.

[Devpost](https://devpost.com/software/loaf-ai) · hackathon [[BitRate- Machine Learning - Music Series]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: immigration_refugee</sub>
  <sub>weak: educator_student</sub>
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, magentajs, p5, s3, tonejs

## Body

GIF loaf-ai in action loaf-ai allows the listener to assemble a lo fi hip hop track using piano, drum, and sound effect loops. While the tracks are loaded into Tone.js , Magenta's Music RNN generates 40 samples of acoustic guitar improvisations to play over the selected chord progressions. The resulting composition is a 15-minute-long jam to study / work / relax / to that is complex enough to be musically interesting, but not so unpredictable as to be a distraction. To add some visual interest and draw the listener's attention to the AI soloist's contributions, the guitar track is highlighted as a waveform at the bottom of the playing browser, adapted from Jason Sigal's p5-music-viz . Lo fi hip hop radio, a trend amongst music streamers on YouTube which gained prominence in 2017-2018 and has not abated in popularity, is fairly easy to reproduce. Numerous tutorials detail the genre's formula as it is distilled in this project: combine a jazzy sample, usually from a piano, with some 80-90bpm bedroom hip hop beats, with atmospheric sound effects like nostalgic movie clips and weather effects. Layering AI-generated music into this formula and making it sound true to genre was the main aesthetic challenge of this project. When first starting with Tone and Magenta, most of the MIDI-based music I created sounded like MIDI: tinny and flat. Using samples from libraries like Nicholaus Brosowsky's tonejs-instruments and Splice went a long way towards making it sound more like "real" music. The next challenge was reigning in Magenta's compositional power. I often find that while computer-generated music is interesting to listen to, it is not always pleasant due to its unpredictability. The model I chose for this project, MusicRNN , has a continueSequence function that can take chord progressions from the tonal library to guide its rampant creativity. The next step was to compose some chord progressions, mostly done in GarageBand, and a starting sample of acoustic guitar noodling over those chords. With these training inputs, the output from Magenta makes what would be a quickly boring 15 minutes of the same chords, beats, and atmospheric loops into a unique composition. I could see an expansion of this project allowing for the user to pick their own chord progressions from any number of chords, generating sequences of different lengths and tones, or to allow for more manipulation by Magenta of other elements like the drums. In the interest of making the compositions as instantly listenable as possible, this project may have compromised on flexibility, but as is, I have some pretty chill background music to train more AI to. 🎶 <div