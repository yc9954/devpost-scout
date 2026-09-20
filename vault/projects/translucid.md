---
slug: "translucid"
url: "https://devpost.com/software/translucid"
title: "Transparify"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 789
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Transparify

> Take advantage of Transparify to get additional contextual information (fact-checking & emotional information) about the facts presented to you in real-time when watching videos.

[Devpost](https://devpost.com/software/translucid) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**domain** [[media_journalism]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[financial_record]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** ellm, groq, hume, javascript, llama, next.js, react, tailwind, websockets, whisper, you.com

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for transparify

## Body

drawing Inspiration As citizens who care deeply about the integrity of information that is being fed to the public, we were troubled by the rampant spread of misinformation and disinformation during (often political) live streams. Our goal is to create a tool that empowers viewers to discern truth from falsehood in real-time , ensuring a more informed and transparent viewing experience. Problem: Misinformation and disinformation through livestreams is incredibly rampant. What it does Transparify provides real-time contextual information and emotional analysis for livestream videos, enhancing transparency and helping viewers make informed decisions. It delivers live transcripts, detects emotional tone through voice and facial analysis, and fact-checks statements using you.com. How we built it The Tech-Stack : Next.js / TailwindCSS / shadcn/ui: For building a responsive and intuitive web interface. Hume.ai: For emotion recognition through both facial detection and audio analysis. Groq: For advanced STT (speech-to-text) transcription. You.com: For real-time fact-checking. Pipeline Overview : (see image for more details) Transcription: We use Groq’s whisper integration to transcribe the video’s speech into text. Emotion Analysis: Hume AI analyzes facial cues and vocal tones to determine the emotional impact and tone of the speaker’s presentation. Fact-Checking: The transcribed and analyzed content is checked for accuracy and context through you.com. Web App Integration: All data is seamlessly integrated into the web app built with Next.js for a smooth user experience. We use Groq and its new whisper integration to get STT transcription from the video. We used Hume AI to provide context about the emotional impact of the presentation of the speaker through facial cues and emotion present in the voice of the speaker to inform the viewer of the likely tone of the address. which is then also checked for likely mistakes, and fed to you.com to verify the information presented by the speaker, providing additional context for whatever is being said. The web app was built using Next.js. Challenges we ran into We originally used YouTube’s embed via iframe, but this didn’t work because many embeds don’t allow recording via HTML MediaRecorders We devised a hack: use the audio from the computer, but this isn’t that helpful because it means users can’t talk + it’s not super accurate Our solution: a temporary workaround had to be used in the form of sharing the user's tab with the video and sound playing. LLM fact-checking being too slow: our solution was to use groq as the first-layer and then fetch you.com query and display it whenever it had loaded (even though this was often times slower than the real-time video) Integrating both audio and video for Hume: Hume requires a web socket to connect to in order to process emotions (and requires separate tracks for audio and video). This was challenging to implement, but in the end we were able to get it done. Logistic problems: how does this try to fix the problem we set out to solve? We had to brainstorm through the problem and see what would really be helpful to users and we ultimately decided on the final iteration of this. Accomplishments that we're proud of We are proud of many things with this project: Real-time analysis: from a technical standpoint, this is very difficult to do. Seamless Integration: Successfully combining multiple advanced technologies into a cohesive and user-friendly application. User Empowerment: Providing viewers with the tools to critically analyze livestream content in real-time, enhancing their understanding and decision-making. What we learned We learned a lot, mainly in three areas: Technical: we learned a lot about React, web sockets, working with many different APIs (Groq, You, Hume) and how these all come together in a working web application. Domain-related: we learned a lot about how politicians are trained in acting/reacting to questions, as well as how powerful LLMs can be in this space, especially those that have access to the internet. Teamwork: developed our ability to collaborate effectively, manage tight deadlines, and maintain focus during intensive work periods. What's next for Transparify We think this idea is just a proof-of-concept. Although it may not be the best, there is definitely a future in which this service is extremely impactful. Imagine opening up your TV and there is real-time information like this on the side of news broadcasts, where there is important information that could change the trajectory of your life. It’s very important to keep the general public informed and stop the spread of misinformation/disinformation, and we think that Transparify is a proof-of-concept for how LLMs can curb this in the future. Some future directions: We want to work on the speed. We want to work on making it more reliable. We want to increase support to other sources besides YouTube. We want to build a better UI. <div