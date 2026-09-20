---
slug: "soteria-lrpsm9"
url: "https://devpost.com/software/soteria-lrpsm9"
title: "Soteria"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 513
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/disaster_emergency"
  - "substrate/video_visual"
---

# Soteria

> Approaching Search & Rescue with edge computing

[Devpost](https://devpost.com/software/soteria-lrpsm9) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[disaster_emergency]]
**substrate** [[video_visual]]

**stack** adafruit, circuit-python, matplotlib, numpy, programmable-leds, python, raspberry-pi, scipy

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for soteria

## Body

Thermal camera in action Thermal Camera first look LED Setup Completed SAR Jacket Inspiration I came up with a proof of concept for this project at a previous hackathon where the challenge I was working on had a Cyberpunk theme. Putting everything together produced a very interesting model but unfortunately that's as far as I was able to get. Still, I found the idea incredibly interesting, so I decided to tackle the Search & Rescue aspect again, with greater focus. What it does This is Search & Rescue using edge computing . While these edge devices may be small, they are only getting more and more powerful. Nowadays we have devices like Nvidia's Jetson series and of course the Raspberry Pi Foundation's series of Raspberry pi computers, with the recent Pi5 boasting incredibly performance. Both in Industry and at home, edge computing is only becoming more capable. With all that in mind, why not apply it to Search & Rescue? Search and Rescue teams may be limited in budget and size, but thanks to the existence of edge devices like the Raspberry Pi we can create powerful tools that can help even the smallest of teams. Challenges we ran into Individually the components that make up this project aren't hard to work with. However, combining them all together in a fleshed out and practical experience is a different story entirely. To begin with, powering all of these devices with just the Raspberry Pi 4 is simply not practical, we need external power supplies for the LEDs, and if we were to add more, we'd need a more centralized power system for everything. Since we are juggling a lot of hardware through Python, some libraries may end up conflicting, especially since we are introducing computer vision and machine learning. This only highlights the importance of managing our environment variables well and keeping track of all of our libraries. There's also the fact that many of the guides for setting up the devices we used are somewhat outdated and niche, so the documentation leaves much to be desired for a beginner. This was my first time working with sensors and programmable LED's, which was an interesting experience. We were unfortunately unable to get TensorFlow running on the raspberry pi, so we were unable to perform object recognition. Accomplishments that we're proud of I'm always a bit intimidated when it comes to working with sensors and accessories, but I did much better this time around. While I managed to create an interesting hardware setup, I was unable to make any of the software integrations I had in mind. What we learned The importance of dependencies for frameworks like TensorFlow and PyTorch, if I want to work with them in the future I will have to carefully plan out the necessary resources. What's next for Soteria I learned quite a lot about hardware this time around, especially the world of programmable LEDs which opens up quite a few possibilities. I also developed a greater interest in computer vision so I'd like to study more about that. <div