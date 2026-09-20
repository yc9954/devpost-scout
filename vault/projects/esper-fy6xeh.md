---
slug: "esper-fy6xeh"
url: "https://devpost.com/software/esper-fy6xeh"
title: "Epileptic Seizure Prevention and Early Response (ESPER)"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 379
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Epileptic Seizure Prevention and Early Response (ESPER)

> ESPER makes the Internet a safer place for those with epilepsy by dynamically adjusting the brightness of videos on the web to make rapid changes more gradual.

[Devpost](https://devpost.com/software/esper-fy6xeh) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chrome, digitalocean, java, javascript, snowflake, snowpark, streamlit, vert.x, youtube

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- what's next for esper

## Body

The ESPER logo :) What it does ESPER dynamically processes image frames from video HTML elements and analyzes their perceived luminosity. On a frame-by-frame basis, we adjust the brightness of the frame using CSS, ensuring that the change in perceived luminosity from frame to frame never exceeds a defined threshold. This helps mitigate rapid changes in brightness like flashes or strobing that may incur epileptic seizure. Additionally, we collect data on the characteristics of different videos the user views with the extension, and characteristics about the luminosity throughout the video, and upload them to a database. This data can be analyzed in an interactive dashboard to search for trends that may predict whether a given video would incur epileptic seizures. How we built it Extension - Chrome Extension API, JavaScript, Youtube API, CSS, HTML Backend - Java, Vert.x, Snowflake's Snowpark, Maven, DigitalOcean (hosting) Database - Snowflake Dashboard - Streamlit (through Snowflake), Python Challenges we ran into One of the biggest hurdles was choosing to create a Chrome extension instead of a Python script with OpenCV. To maintain accessibility and usability across all parts of the internet without needing to download videos, JavaScript was the preferred choice. However, this came with its own complexities, particularly around YouTube’s strict security policies. Our initial approach utilized iframes, which are often cross-origin, meaning they are served from a different domain (such as youtube.com) than the host page. This raised significant security challenges, like CORS (Cross-Origin Resource Sharing) and Content Security Policy (CSP), which limit interaction with iframe content. Due to these policies, we couldn't directly access or manipulate elements within the YouTube iframe, including the video player controls, individual frames, or the DOM itself. Unfortunately, this discovery came late in the process, after a significant portion of our frontend had been built on this method, leading to a major pivot. Beyond this, we also faced challenges in ensuring that luminosity adjustments were fast enough to stay in sync with video playback, and in finding the optimal threshold for luminosity changes to provide a smooth viewing experience as the math is rather complicated. What's next for ESPER More advanced solutions that can target certain areas of the screen or insert new frames rather than just filtering existing video Application of data for ML/AI <div