---
slug: "adible"
url: "https://devpost.com/software/adible"
title: "Pochinki"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 814
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Pochinki

> A seamless way to integrate ads into podcasts, AI Voice agents and more.

[Devpost](https://devpost.com/software/adible) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**substrate** [[transcript_audio]] [[web_dom]]

**stack** elevenlabs, nextjs, openai, python, sql, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adible

## Body

ElvenLabs conversational agent Main Page: Ad crawling Extracted Ads from website Upload podcast/recording: Podcast Ad selection: Podcast Final audio with ads: Podcast Adible conversational agent Adible, by team Pochinki We have a drive link at the end with some examples (both conversational and recorded AI ad placements) Inspiration The inspiration comes from observing two major shifts in digital interaction. Firstly the transition from traditional text-based search to conversational AI interfaces becoming the primary way people access information and services. And secondly, the current limitations of traditional digital advertising, which can feel disruptive and impersonal. We want to make advertising natural and seamless. What it does Adible is a new advertising paradigm with a voice and conversation first approach that integrates promotional content through several innovative approaches. Adible supports two primarily approaches to ad integration: Conversational AI Ad placement - where we analyze context and place relevant ads in a conversation flow as and when you talk to a Voice AI in realtime! Recorded content Ad placement - we analyze recorded audio for a podcast, book reading, discussion, etc and then determine the best places to integrate an Ad along with the appropriate Ad for the recording. Then insert it in the conversation flow. Our aim with Adible is to do the following: Contextual Integration: -- Analyzes ongoing conversations to identify relevant moments for product mentions. -- Inserts recommendations that feel natural to the discussion flow. Multilingual support without the hassle -- Ads do not have to be built in every language known to man, we can adjust the grammar, tonality and conversational placement. Personalized Engagement -- Matches products with conversation context -- Uses appropriate influencer personas based on the topic (e.g., David Goggins for fitness) Marketing Applications -- Brand awareness through organic conversation mentions -- Product discovery through contextual recommendations How we built it Adible is built to be both a conversation AI Ad agent and a general platform for ad creation and placement in recorded content. So we have two services as a result that integrate into the core system. The core system does the following: Allows the user to provide their website We scrape and collect relevant part to generate ads Ads are stored in a central store. Then we have two services, one for the conversational AI Ad agent and the other for the recorded content Ad placement agent. The conversation AI Ad agent: The essence of effective advertising is subtlety—it shouldn’t feel intrusive. Instead, it should serve as a timely helping hand. Our aim is to craft audio advertisements that integrate seamlessly into key moments. Rather than the overt ads of today, these placements would be subtle, intuitive, and creative. Imagine hearing a trending meme sung by Tom Cruise, effortlessly woven into your conversation as he hints at his latest movie, or the iconic theme from Interstellar playing in the background as you discuss space sci-fi. The possibilities are endless. The recorded content Ad placement agent: Takes a audio file (podcast, book recording, discussion, etc) Creates transcription and stores in DB (OpenAI Whisper) We filter to determine relevant ad keywords based on the transcription (LLM) Using the filtered keywords and the transcription, we find relevant ads that can be placed in the recording We then naturally determine the placement of these ads in the recording along with a few variations of the ad text. (LLM) Using the relevant transcription segment and ad text, we determine the voice that should be used ( based on language, description, etc) (LLM) We then generate the audio for these ads (ElevenLabs text to speech with voice) Then based on the audio ads that the user selects, they are stitched into the main audio recording (ffmpeg) Challenges we ran into The main challenge we ran into was redesigning the ad experience. With the conversational agent , we would have loved more control or atleast the ability to hook into the different lifecycle steps of the conversational agents provided by 11labs. Accomplishments that we're proud of We are proud of the fact that we built both the use cases in the restricted time with multilingual support, voice determination and conversational placement. We deliver limited yet a seamless process to incorporate ad's in a way that has never been done before with voice agents! What we learned The nature of conversational interactions differ greatly from a textual interface and the speed and variety of ideas and topics a human runs through is vast and abstract. Being able to "INCEPT"(tion) ideas into the users everyday conversation is what every brand in the world wishes to achieve and we enable just that! What's next for Adible Auto crawling and better advert generation. support for custom audio injections and adding background music and sfx in conversation in realtime. Better sematic matching and targetting of keywords. Enable tracking and analytics for converted ads and how the user performed and converted. <div