---
slug: "barnacle"
url: "https://devpost.com/software/barnacle"
title: "Barnacle"
hackathon: "MLH Local Hack Day (2018)"
winner: true
words: 833
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Barnacle

> Augmentative and Alternative Communication App for Children With Autism

[Devpost](https://devpost.com/software/barnacle) · hackathon [[MLH Local Hack Day -2018-]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** ibm-watson, unity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- why #soyvisual?
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for barnacle
- licensing
- contact
- special thanks

## Body

Select your symbols Drag them into the slate to speak Speak entire sentences! Inspiration Children who are unable to speak, either voluntarily or not, have been using Augmentative and Alternative Communication (AAC) tools such as Picture Exchange Communication System (PECS) for years now. However, AACs tends to be traditionally paper-based and so, may require the child to organise an insurmountable collection of symbols for use. To address this problem, several assertive software solutions were developed such as Widgit and Proloquo2Go . However, these are incredibly expensive (probably because barely any EdTech startups are making money ). So it is reasonable to expect that most schools will never be in a position to pay for them (let alone parents). As I spent three years teaching students with Profound-to-Multiple Learning Difficulties (PMLD), I know first hand how much of a life changing difference such technologies can make. Therefore, I present a free app-based solution which leverages artificial intelligence to convert symbols to voice, and demonstrates a proof-of-concept for parents and schools a like. Why "Barnacle"? I took inspiration from Captain Haddock's favourite catch-phrase "Blisterin' Barnacles!". Captain Haddock's choice of words, much like AACs, are colourful (albeit for slightly different reasons). What it does Unlike traditional paper-based solutions, the symbol will talk in a trigram -like fashion! With Barnacle you can drag and drop your symbol into the slate, Barnacle will then voice what you just chose. This is effectively a picture-to-voice solution to AAC, which will end up giving a voice to the voiceless. Features! AAC to Speech powered by IBM Watson Beautiful Carousel/Slider user interface for quick and easy symbol search Drag and drop symbols for added development in fine-motor control (and because it's more fun!) How I built it In order to compile a trustworthy and free symbol library, I used #Soyvisual , an open-source AAC kindly provided by the Fundación Orange (Orange Foundation Spain). I imported all the images and grouped them into conversational categories such as 'verbs', 'objects', 'people', etc. I built a windows and mac standalone using the Unity engine using a simple UI system . Lastly, the symbol-to-voice feature was made possible through IBM Watson's text-to-speech service by taking the symbol's object name, converting it as speech, and playing the audio back whenever the symbol is dragged and dropped. Why #Soyvisual? So why this AAC in particular? I explored open-source alternatives such as Sclera , Mulberry Symbols , Picto-Selector , as well as the United Nations OCHA Humanitarian Symbols Set . However, #Soyvisual has a consistently beautiful design which makes use of 3D objects (this is helpful when comparing symbols to real-world objects). It is no surprise why #Soyvisual is a magnitude above the other options given that it was funded by the telecommunications giant, Orange. Therefore I was happy to adopt it for the project. Challenges I ran into Although #Soyvisual offers iOS and Android apps for its symbols, it has no English version at all. About 400 million people speak English as their first language. In addition to being widely spoken, English is by far the most commonly studied foreign language in the world with around 600 - 700 million English as a foreign language speakers. Therefore, with 1 billion total speakers of English, it seemed unfair to deprive AAC users of #Soyvisual due to a language-barrier. So the task was now to translate the images. All 3000 of them. Much to my relief, this was possible thanks to exporting a pre-compiled library on Picto-Selector . Furthermore, Barnacle goes beyond #Soyvisual's apps by using IBM Watson's speech services to make the symbols speak in English. Accomplishments that I'm proud of Changing someone else's life with the skills that I have. What I learned Competing in MLS Local Hack Day is really fun. I think I had more fun here than the other previous Hacks. What's next for Barnacle I want to expand the symbol library. Although the licensing terms of #Soyvisual also dictates that my project cannot be commercialised unless I negotiate with the Foundation. Stifling the ability to make money may cause a challenge for the long-term health of the project. Here's what I have in mind for future features: Games (play games and learn the #Soyvisual system by matching the symbols to the correct cue) Listening mode (Barnacle will listen to what is being said and convert audio->text, and then text->symbol) Conversation mode (The user can finally communicate with the outside world by using #Soyvisual to speak. Barnacle will then invoke the listening mode and present what is being said to the user in symbol form.) Contextual symbol groupings (perhaps we can leverage deeper AI features by grouping symbols in a contextual manner based on the conversation) Licensing Soyvisual ( BY-NC-SA ) Barnacle ( BY-NC-SA ) Contact Email Special thanks Although this project received no sponsorship, I would like to thank the following services and organisations for providing the free tools to make this project possible. © Copyright 2018-19 Celestial Interactive. All rights reserved. <div