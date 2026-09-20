---
slug: "unmute-speak-even-when-you-can-t"
url: "https://devpost.com/software/unmute-speak-even-when-you-can-t"
title: "Unmute: Speak, Even When You Can’t."
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 359
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
---

# Unmute: Speak, Even When You Can’t.

> Unmute is designed for those private moments during video calls when you can't speak out loud, yet still want to fully participate in the conversation.

[Devpost](https://devpost.com/software/unmute-speak-even-when-you-can-t) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[video_visual]]

**stack** figma, flask, react, symphonic, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- next steps

## Body

Inspiration We've all been there - racing to find an empty conference room as your meeting is about to start, struggling to hear a teammate who's decided to work from a bustling coffee shop, or continuously muting your mic because of background noise. As the four of us all conclude our internships this summer, we’ve all experienced these over and over. But what if there is a way for you to simply take meetings in the middle of the office… What it does We like to introduce you to Unmute, your solution to clear and efficient virtual communication. Unmute transforms garbled audio into audible speech by analyzing your lip movements, all while providing real-time captions as a video overlay. This means your colleagues and friends can hear you loud and clear, even when you’re not. Say goodbye to the all too familiar "wait, I think you're muted". How we built it Our team built this application by first designing it on Figma. We built a React-based frontend using TypeScript and Vite for optimal performance. The frontend captures video input from the user's webcam using the MediaRecorder API and sends it to our Flask backend as a WebM file. On the server side, we utilized FFmpeg for video processing, converting the WebM to MP4 for wider compatibility. We then employed Symphonic's API to transcribe visual cues. Challenges we ran into Narrowing an idea was one of the biggest challenges. We had many ideas, including a lip-reading language course, but none of them had a solid use case. It was only after we started thinking about problems we encountered in our daily lives did we find our favorite project idea. Additionally, there were many challenges on the technical side with using Flask and uploading and processing videos. Accomplishments that we're proud of We are proud that we were able to make this project come to life. Next steps Symphonic currently does not offer websocket functionality, so our vision of making this a real-time virtual meeting extension is not yet realizable. However, when this is possible, we are excited for the improvements this project will bring to meetings of all kinds. <div