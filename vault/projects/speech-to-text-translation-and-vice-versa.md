---
slug: "speech-to-text-translation-and-vice-versa"
url: "https://devpost.com/software/speech-to-text-translation-and-vice-versa"
title: "Speech to Text and Text to Speech Conversion"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 200
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/web_dom"
---

# Speech to Text and Text to Speech Conversion

> In the world of voice assistants, this API will help convert speech to text. Use the converted text for any of your code needs. This API is using IBM Watson's technology.

[Devpost](https://devpost.com/software/speech-to-text-translation-and-vice-versa) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[web_dom]]

**stack** api, ibm

## How they structured the write-up

- inspiration
- what it does
- pre-requisites

## Body

Inspiration I'm always amazed by how Siri, Alexa, and or Google listen to a command and execute it appropriately making our lives better. So, I've decided to consume IBM Watson's Speech to Text and Text to Speech API and expose it as a collection using Postman and hopefully people will be able to use this as an easy guide to build robust application. There are tons of API within these resources. I've only exposed the main ones. You can get the pronounciation of a specific word, add custom words, grammars, etc. What it does The main API can convert speech from different audio types to text. It can also convert your text to audio from your select voice. Pre-requisites You will need an account from IBM . When you are done creating an account, create a resource for both Speech to Text and Text to Speech. Save the API keys and URL for both resources. You will then need to create a postman environment to store this. I've used: {{s2t_apikey}} : Speech to Text API key {{s2t_urlpath}} : Speech to Text full URL path {{t2s_apikey}} : Text to Speech API key {{t2s_urlpath}} : Text to Speech full URL path <div