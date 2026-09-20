---
slug: "studying-with-hack-the-north"
url: "https://devpost.com/software/studying-with-hack-the-north"
title: "StudySync"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 394
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# StudySync

> With so many amazing sponsors giving away free API keys at Hack the North, our team wondered, "What if we combined all of them to help us study or work?" And that is exactly what we did.

[Devpost](https://devpost.com/software/studying-with-hack-the-north) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]]
**substrate** [[structured_db]] [[web_dom]]

**stack** auth0, cohere, css, hakra, html, javascript, mongodb, openai, python, symphonic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for studying with hack the north

## Body

Inspiration Our project was inspired by people who don't learn the "old school" way. Some people learn best by reciting things out loud, but the problem with that is sometimes it's too quiet to talk, and sometimes it's too loud to talk. What it does Our project is a website that allows you to create a group with your classmates/coworkers, in which you can record video of yourself silently mouthing out whatever lecture or book you're reading, allowing you to pay full attention without worrying about writing notes, a loud environment, or an environment in which you're not allowed to talk. Our project reads your lips and puts it into text, creating notes for the video you take. Then, with your notes, we summarize your key points and build a quiz so you can focus on the important parts of your work. How we built it For the front end of our website, we used React JS and Chakra. We used Auth0 to create an account system for our project. We used Symphonic Labs' API to read your lips and convert your silent words to text. We used MongoDB to save all your notes to a database in your group. We then used a Cohere API to summarize the key points of the text and make a quiz out of it. We also used an Open AI API to convert mp3 files to text, in case you wanted to record a lecturer or friend speaking, and then convert it to notes and quizzes. Challenges we ran into We tried to get live video transcribing with Symphonic Lab's API using Open CV, but since Open CV was giving us frames of the video, Symphonic Lab's API wasn't able to transcribe it. Instead, we switched to allowing users to record their videos on the site, immediately download them and upload it for transcribing. Accomplishments that we're proud of We are very proud of combining all the complicated API's to create a complete and flowing product, something that all of us will definitely be using for school. What we learned This was our group's first time using more than one API for a project, but it ended up with a website that performs a useful and complicated function, and we will be using multiple APIs in the future! What's next for Studying with Hack the North <div