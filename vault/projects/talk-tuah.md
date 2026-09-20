---
slug: "talk-tuah"
url: "https://devpost.com/software/talk-tuah"
title: "Talk Tuah"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 445
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Talk Tuah

> Ever struggled in social settings? Not knowing what to say next? Meet Talk Tuah, AR glasses with a built in AI chatbot trained in social etiquette, as long as a mobile app to review transcripts.

[Devpost](https://devpost.com/software/talk-tuah) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[transcript_audio]] [[video_visual]]

**stack** ar, arduino, c, deepgram, flask, hume, javascript, ngrok, python, raspberry-pi, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for talk tuah

## Body

Inspiration This idea came from one of our team members (who will remain unnamed) who struggles with talking to women. We wanted to build this product to help people who are introverts or socially awkward be able to find easy and positive responses to any conversation I person might face. What it does The AR glasses are built with a camera and microphone to capture the facial expressions and voice of anybody speaking to the user. Using an advanced algorithm our AI chatbot is able to determine the mood of the speaker based on audio and visual cues. This response is then transmitted back through an OLED display in the glasses and provides a response to which the user can say. All these interactions, including name, hobbies, likes, dislikes etc. are also stored in a server to train the AI in future conversations. Transcripts are stored in a separate mobile app which users can access to look back on previous conversations How we built it We used an openAI API to build and train our chatbot to determine the most socially responsible and positive response based on an input. We also used the Deepgram API to convert speech to text and determine the mood behind a secondary person's input. The mobile app was built using React Native and built the glasses using self bought parts. Challenges we ran into One major challenge we ran into was setting up the server to store personal data, of both the user and their chatters. We struggled to develop a secure inter-device connection between the data storage and the mobile app as speech data needed to be uploaded. We found a solution by using ngrok to allow the mobile device to connect. Accomplishments that we're proud of Our team is most proud of our implementation of the mobile app. We truly believe that the app was the perfect way to tie our product in and make it more accessible for people by allowing customization and including custom prompts. What we learned Many of us learned how to code in a language we didn't feel confident in or knew at all. This was a great learning experience that we all believe will carry us through our desired career paths and positions. What's next for Talk Tuah Creating a customizable chatbot brings a lot of creativity and opportunities for growth. We believe there are ample opportunities to apply this outside of simple day to day conversations, whether that is teachers determining what units their students are struggling on based vocal and facial expressions, to how to craft a speech on the fly based on your audience's response to certain topics/statements. <div