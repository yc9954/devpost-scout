---
slug: "voicenoted"
url: "https://devpost.com/software/voicenoted"
title: "voicenoted."
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 507
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# voicenoted.

> Listen, write, share. Save and transcribe audio clips from their podcasts and audiobooks, and write notes on them in just a few clicks.

[Devpost](https://devpost.com/software/voicenoted) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** adobe-illustrator, bootstrap, express.js, ffmpeg, figma, firebase, google-cloud, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- accomplishments
- what we learned
- what's next for voicenoted

## Body

Introducing voicenoted! Editing audio clip Home page Onboarding Inspiration More and more people are turning to audio-based mediums such as podcasts and audiobooks for their content consumption 🎙️. In fact, 74% of users state that they go to podcasts as a resource for learning new things. Note taking has long been an integral part of the learning process, however, there has not been a convenient way for people to take notes on audio format of information. Most platforms simply do not have a way for users to record meaningful clips of audio content, nor to integrate these clips into their customized notes 🤔. This pain point became the starting point for Voicenoted , an audio notetaking mobile application. What it does Voicenoted allows users to save and transcribe audio clips from their podcasts and audiobooks, as well as create customized notes about them with just a few clicks. Moreover, users can also choose to make their clips public and browse through other people's notes, which in turn facilitates community-based learning. How We Built It We started by prototyping the app in Figma and creating visual assets in Adobe Illustrator. For the front-end, we used React to create an app that can be accessed from both a computer and a mobile phone. We set-up a custom domain name with domain.com. For the backend, we used Node.js to create an API the front-end calls to do various tasks like translate speech to text, retrieve notes, and save notes. We used firebase for our database and user authentication services. We used ffmpeg to parse audio and Google Cloud AI to transcribe audio. Challenges We Faced Finding a podcast API: we had trouble finding a free podcast API for our project, and went through applying for an access token and even trying to learn GraphQL for the first time. We eventually settled on using a .flac copy of an audio file for the demo, but to improve voicenoted we would definitely look into expanding to a larger database of podcasts and other audio resources! Accomplishments We worked as a team for the first time this weekend! We’re happy that we were able to delegate the work according to our different strengths and build a project over such a short period of time. After designing a thorough prototype of the app, we managed to complete all our core functionalities, such as recording the voicenote, transcribing it, and adding it into a note-taking document. What We Learned CORS errors are no fun :( What's next for voicenoted We hope to conduct additional user research to streamline the voicenote creation, editing, and sharing functionalities. Laptops and desktops are popular note-taking devices, so we also want to refine our desktop app. Additionally, we want expand our potential use cases beyond podcasts and audiobooks, such as lectures and videos. Lastly, we also want to look into potential ways to integrate voicenoted into other podcast and audiobook platforms, such as Apple Podcasts, Spotify, and Audible. Check out our demo at voicenotedvotednoice.tech and vote 'noice' for voicenoted! <div