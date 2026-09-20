---
slug: "hanq"
url: "https://devpost.com/software/hanq"
title: "HANQ"
hackathon: "Hack the North 2019"
winner: true
words: 456
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "substrate/structured_db"
---

# HANQ

> A new kind of voice assistant. Always listening, zero boundaries, and ready to help.

[Devpost](https://devpost.com/software/hanq) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**substrate** [[structured_db]]

**stack** azure, beautiful-soup, pyglet, python, requests, simpleaudio, xenon

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hanq

## Body

What it does The market is crowded with "smart assistants" like Siri, Alexa and Google Assistant that try to be helpful, or tools to help your productivity, even though they can be annoying, slow robots with a limited understanding of human vocabulary. We decided to take the opposite approach with HANQ, creating a helpful bot designed to drive you crazy. Always listening, HANQ will interject interesting facts into your daily conversations, and convert currency for you so you're always up to date on the exchange rate. He's fun for the whole family! How we built it We used the Azure Cognitive Services API to create a speech interface, with voice recognition, named entity recognition, key phrase finding and text to speech. Since there isn't really any sort of public fun fact database available on the interwebs, we decided to get our fun facts by scraping the little instant answer boxes at the top of Google search results. We also used the XE API so that HANQ can arbitrarily convert random currencies whenever he feels like it. Challenges we ran into The whole process, from speech recognition to named entity recognition to Google search scraping to text-to-speech, used up so much time that HANQ's reaction time isn't that great. We've improved it a lot by locally caching Google search results, skipping some steps of the process in certain conditions (decreasing Internet-dependent “think” time), and customizing the Azure speech-to-text API, but there's still a lot to improve. Accomplishments that we're proud of The first big milestone was figuring out how to stream audio from the Internet directly from Python, which was crucial to reducing the response time, and how to convert from text to speech and vice versa. Once we could play back the audio, we figured out how to separate important and meaningful words from the rest of the sentences, using NLP APIs from Azure Cognitive Services. Finally, we incorporated the Xenon APIs by playing back a random currency exchange when hearing certain keywords. What we learned We learned how to use a lot of the Azure Cognitive Services and Xenon APIs, got a bit more familiar with web scraping and multiprocess Python, and learned the importance of coming up with a feasible idea before half of the hackathon has already gone by. What's next for HANQ After Hack the North, we hope to use what we learned from HANQ and how smart assistants work to create an actually helpful assistant. We can train the bot by giving it different keywords, and we can increase the reaction time of the web scraping. HANQ is just the beginning; even though it may seem annoying, it can be tweaked to make it much more helpful in the future. <div