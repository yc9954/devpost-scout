---
slug: "ludwig"
url: "https://devpost.com/software/ludwig"
title: "Ludwig"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 547
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Ludwig

> A physical robot to play any sheet music you want!

[Devpost](https://devpost.com/software/ludwig) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[elder_child_care]]
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** opencv, python, raspberry-pi, tkinter

## How they structured the write-up

- 💡 inspiration 💡
- ❓what it does ❓
- ⚙️ how we built it ⚙️
- challenges we ran into ⚔️
- accomplishments that we're proud of 🏆
- what we learned 📚
- what's next for ludwig 🤔

## Body

💡 Inspiration 💡 Have you ever wished you could play the piano perfectly? Well, instead of playing yourself, why not get Ludwig to play it for you? Regardless of your ability to read sheet music, just upload it to Ludwig and he'll scan, analyze, and play the entire sheet music within the span of a few seconds! Sometimes, you just want someone to play the piano for you, so we aimed to make a robot that could be your little personal piano player! This project allows us to bring music to places like elderly homes, where live performances can uplift residents who may not have frequent access to musicians. We were excited to combine computer vision, MIDI parsing, and robotics to create something tangible that shows how technology can open new doors. Ultimately, our project makes music more inclusive and brings people together through shared experiences. ❓What it does ❓ Ludwig is your music prodigy. Ludwig can read any sheet music that you upload to him, then convert it to a MIDI file, convert that to playable notes on the piano scale, then play each of those notes on the piano with its fingers! You can upload any kind of sheet music and see the music come to life! ⚙️ How we built it ⚙️ For this project, we leveraged OpenCV for computer vision to read the sheet music. The sheet reading goes through a process of image filtering, converting it to binary, classifying the characters, identifying the notes, then exporting them as a MIDI file. We then have a server running for transferring the file over to Ludwig's brain via SSH. Using the Raspberry Pi, we leveraged multiple servo motors with a servo module to simultaneously move multiple fingers for Ludwig. In the Raspberry Pi, we developed functions, key mappers, and note mapping systems that allow Ludwig to play the piano effectively. Challenges we ran into ⚔️ We had a few roadbumps along the way. Some major ones included file transferring over SSH as well as just making fingers strong enough on the piano that could withstand the torque. It was also fairly difficult trying to figure out the OpenCV for reading the sheet music. We had a model that was fairly slow in reading and converting the music notes. However, we were able to learn from the mentors in Hack The North and learn how to speed it up to make it more efficient. We also wanted to Accomplishments that we're proud of 🏆 Got a working robot to read and play piano music! File transfer working via SSH Conversion from MIDI to key presses mapped to fingers Piano playing melody ablities! What we learned 📚 Working with Raspberry Pi 3 and its libraries for servo motors and additional components Working with OpenCV and fine tuning models for reading sheet music SSH protocols and just general networking concepts for transferring files Parsing MIDI files into useful data through some really cool Python libraries What's next for Ludwig 🤔 MORE OCTAVES! We might add some sort of DC motor with a gearbox, essentially a conveyer belt, which can enable the motors to move up the piano keyboard to allow for more octaves. Improved photo recognition for reading accents and BPM Realistic fingers via 3D printing <div