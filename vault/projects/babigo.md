---
slug: "babigo"
url: "https://devpost.com/software/babigo"
title: "Babigo"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 295
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/web_dom"
---

# Babigo

> An anime stylizer for just about any video ever.

[Devpost](https://devpost.com/software/babigo) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[web_dom]]

**stack** amazon-web-services, general-adversarial-network, moviepy

## How they structured the write-up

- inspiration
- what it does
- how it’s made©
- challenges we ran into
- accomplishments we’re proud of
- what we learned

## Body

High res link: https://youtu.be/cQZrp-UZsKg Inspiration Anime. You already know. It’s a larger-than-life, exhilarating roller coaster of emotions carried by intense and beautiful artwork. What if we could make anything into anime? What it does Babigo turns video clips into animes by transforming the video and audio. How it’s made© A general adversarial network (CartoonGAN) is used to style transfer anime onto the video. Then, the audio is fed through AWS Transcribe, Translate, and Polly to translate, caption, and dub video in Japanese. Audio clips are separated by pauses, then adjusted to prevent overlaps. Finally, they’re stitched together using moviepy, producing your very own anime. Challenges we ran into Getting dubbed audio to match original speech cadence. Balancing between detailed rendering and execution time. Installing dependencies with the appropriate versions. Imagemagick is hard to install the way you want to Accomplishments we’re proud of The videos are funny, and probably contain atrocious, embarrassing Japanese. Automated dubbing matches lip flaps What we learned How to style transfer, translate in the cloud, different approaches to syncing captions with speech - Josh I learned not to export the demo video 4 minutes before the deadline - Tim I learned why no one uses python to make videos - Quinn Babigo is the Japanese equivalent to Pig Latin - Andrew What’s next for Babigo We would have liked to merge the video and audio processing into a continuous pipeline so that we could put up a website to upload and convert videos. The video and audio processes took a significant amount of time to finetune, so the pipeline is one area for improvement in the next iteration. There are also other unique anime styles that could be added but require more complex methods. Ex. scene transitions, sound effects, etc. <div