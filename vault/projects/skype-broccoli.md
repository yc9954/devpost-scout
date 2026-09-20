---
slug: "skype-broccoli"
url: "https://devpost.com/software/skype-broccoli"
title: "Skype broccoli"
hackathon: "Junction 2016"
winner: true
words: 223
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Skype broccoli

> Seamless assistant for your Skype calls and chats

[Devpost](https://devpost.com/software/skype-broccoli) · hackathon [[Junction 2016]]

## Facets

  <sub>weak: voice_speech</sub>
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** azure, luis, natural-language-processing, node.js, python, skype, speech-to-text

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what's next for skype broccoli

## Body

Inspiration The inspiration came from just thinking about the future of AI assistants. What it does It is an interactive assistant that can join any Skype call and waits until it hears an intent in the discussion where it can help. For example when the users mention an email about a topic, it can go through a mailbox analyze the emails to understand which one the users were referring to and display the relevant one in chat. Similarly it is integrated with cloud storage and return images based on what is displayed on them. E.g. ‘Do you remember the email from last week about politics’, or ‘the picture with the design of bmw’. How we built it The platform is based on Microsoft bot framework, where it can record audio. This audio is then sent to Microsoft Bing STT, the text is analyzed using Microsoft LUIS for intent and entities. These can lead into an on-the-fly natural language analyzed emails or image pre-processed cloud storage. Challenges we ran into Working with speech from the ongoing Skype call, processing it on the fly, using technologies which just released and so far do not have much support (tutorial, etc.) on internet. Accomplishments that we are proud of Creating useful and sophisticated assistant What's next for Skype Broccoli Extending Broccoli capabilities, being even more cool! <div