---
slug: "baseline-status-for-video"
url: "https://devpost.com/software/baseline-status-for-video"
title: "Baseline Status for Video"
hackathon: "Baseline Tooling Hackathon"
organization: "Google"
winner: true
words: 591
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# Baseline Status for Video

> A handy online tool that will let you easily show Baseline Status in your videos.

[Devpost](https://devpost.com/software/baseline-status-for-video) · hackathon [[Baseline Tooling Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** chakraui, ffmpeg, next.js, react, typescript, vitest

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what's next for baseline status for video

## Body

Baseline Status for Video app Baseline Status widget overlaid over a video on YouTube Inspiration I’m publishing video guides focused on CSS, mainly on YouTube. One of the challenges when talking about web platform features is explaining whether the feature works across different browsers. Simply mentioning browser support is often not enough, as some people are visual and process information better in this way. Additionally, sometimes when talking about certain features, the presenter (or me in this example) doesn’t realize that viewers might not be aware that the feature is supported in all major browsers and safe to use in production—so pulling up the Baseline Status widget at that point in video, even if it’s not mentioned specifically, would provide viewers with additional valuable information. What it does The app displays the Baseline Status widget on the screen and allows you to record it with animation in and animation out. The result is a video file that can be easily imported into video editing software. That file can then be easily tweaked using the Green Screen Removal (or Chroma Key) filter, so that only the Baseline Status is overlayed on the screen, thus massively simplifying the process of showing Baseline Status in tech videos and courses. How I built it I used the Next.js framework with Chakra UI, along with a number of other libraries and tools, most prominently FFmpeg.wasm, to put everything together. I’ve used this project as an opportunity to experiment with AI-assisted workflows, which have allowed me to learn about AI-assisted development in real-world projects, which taught me how I can accelerate and simplify my development workflow. Challenges I ran into The biggest challenge I ran into was related to video processing. The idea behind the app was to simplify the process as much as possible and provide users with a video that they can drag and drop into video editing software. As different browsers work with different video codecs and capture screen using MediaRecorder API differently, I needed to make a number of compromises and ensure solid fallbacks for browsers that don’t handle everything perfectly. Google Chrome’s implementation of screen capture works best, as it’s the only browser that allows the user to capture just the contents of the webpage—other browsers also capture the browser interface, including tabs, which isn’t ideal for this use case. Additionally, I wanted the end result (video) to be as smooth as possible, but processing the video directly in the browser using FFmpeg.wasm turned out to be too time-consuming and impractical. Therefore, I ended up mainly relying on the browser APIs and MediaRecorder options to achieve the best possible result, while using FFmpeg mainly to ensure the video is compatible with video editing software. Accomplishments that I’m proud of I’ve spoken with a few prominent tech video creators before publicly releasing the project, and the feedback I received was overwhelmingly positive. They found Baseline Status for Video useful and plan to use it in their videos, meaning many more developers will be exposed to Baseline Status. This, in my opinion, could help with the adoption of Baseline, as from my experience, there are still quite a few developers who are not aware of it. What's next for Baseline Status for Video I will continue updating the app, adding new features to make it more usable and user-friendly. Additionally, I plan to create a new section where I will showcase videos that utilize the Baseline Status for Video feature, thereby promoting guides that discuss web platform features and raising awareness about Baseline. <div