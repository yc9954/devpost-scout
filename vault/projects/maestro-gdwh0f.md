---
slug: "maestro-gdwh0f"
url: "https://devpost.com/software/maestro-gdwh0f"
title: "Maestro"
hackathon: "BitRate: Machine Learning & Music Series"
winner: true
words: 874
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Maestro

> An AI-guided vocal coach, combining music theory with practical lessons for music enthusiasts.

[Devpost](https://devpost.com/software/maestro-gdwh0f) · hackathon [[BitRate- Machine Learning - Music Series]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** flask, magenta, nexusui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maestro

## Body

Maestro practice session with target notes (teal) and users current pitch (purple). Maestro vocal range detection in order to customize the lesson plan for the span of notes the user can sing. Inspiration Most of our team members aren't musicians, but we were fascinated with the idea of integrating music and machine learning. We realized that even though we weren't musicians we could learn to be! So we started brainstorming how machine learning could help us learn to become better vocalists without the social pressures or presence of a teacher. What it does Maestro is a site dedicated to helping users learn while providing instant feedback on performance even in the absence of a teacher. There are a series of lessons to guide the user through learning different notes. We have a practice session that lets the user know if they are hitting their notes correctly. How we built it We have used ml5.js with the CREPE model in order to detect the notes the user sings and determine if they are hitting their target notes. Using the Nexus UI sequencer we were able to create a visualizer that shows the note the user needs to hit along with the pitch they are currently hitting. This acts as a form of active feedback to show the user how they are doing. We use the music_rnn model from magenta.js to auto generate different melodies that the user is required to correctly sing as a way of allowing them to test their abilities. Challenges we ran into Our visualizer needed to be able to show both target notes and detected notes based off of pitch detection. We chose to go with Nexus UI Sequencer since it allows us to set notes on the fly rather than being tied to a currently playing note sequence. However, it still only allowed us to use one color, so we had to manually dig into the HTML elements of the sequencer and add the different colors on our own. Furthermore, this was our first time using Magenta, ml5.js and tone.js. In the beginning it was a challenge to use these libraries to implement note generation and pitch detection. The documentation and source code often referenced musical concepts such as “quantized notes”, “tempo”, “MIDI”, etc that we weren’t as familiar with. We had to look at various tutorials and experiment with the different libraries before we were able to build an MVP concept of what we wanted. The time to get basic pitch detection and note generation working meant that we had to scale back our vision about what Maestro could be. Finally, we have two ML models we are trying to use on the front-end (the pitch detection model and the music_rnn model to generate notes).This makes our application have a slower load time while we wait for all our models to load up. This is a less than ideal user experience and an area for optimization in the future. Accomplishments that we're proud of We are proud of the user interface we created for Maestro. We wanted to create something that was usable and easy to follow for beginners learning to sing and did a lot of research to make this possible. We experimented with different visualizers to determine what the best option was for creating a seamless experience for the user to see which note they needed to hit and if they were on pitch. As well, we researched different vocal exercises to determine what would be a good first lesson to get students started and how to make sure that passive learning (watching videos) could be balanced with active learning (practice with pitch detection and feedback). What we learned Most team members didn't have a lot of existing musical knowledge so we used this as an opportunity to learn about music scales. For example, we had to research vocal ranges and scales to determine what a good first lesson could be. We also had to explore the connection between frequency, MIDI, and how that maps to different vocal notes in order to make sure we were doing the pitch detection correctly. We also had to become familiar with the Magenta Js endpoints, understanding quantized and unquantized sequences, and modifying the output of the model to play notes within a given vocal range, and for a longer duration. What's next for Maestro Currently we demonstrate the potential to leverage magenta to randomly generate tests for a student to practice their skills. In the future, we would like to integrate machine learning into the practice session as well. Maestro could generate practice sessions personalized for the user. So if there are certain skills a student is weak in, they will appear more often within the practice sessions. For example, if a student struggles to hit the D note, it would appear more often. We could create a progress section to allow users to see how they perform on various skills and allow them to track their progress. Furthermore, we see the potential of maestro being extended into a global platform for music teachers to upload their own lessons. This would allow users to find the teaching style that works best for them rather than following one predetermined path. <div