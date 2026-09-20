---
slug: "diy-alexa"
url: "https://devpost.com/software/diy-alexa"
title: "DIY Alexa With the ESP32 and Wit.ai"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 827
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DIY Alexa With the ESP32 and Wit.ai

> Learn how to build your own Alexa! This tutorial teaches you how to build a wake word detection system and then use Wit.ai to recognise a user's request.

[Devpost](https://devpost.com/software/diy-alexa) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** c++, esp32, python, tensorflow, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for diy alexa

## Body

The Hardware - ESP32, Microphone Board, Speaker Output The training data - Spectrograms of the word "Marvin" Generating a spectrogram from an audio signal The full tutorial is available in the GitHub repo - https://github.com/atomic14/diy-alexa Inspiration I wanted to see what was possible to achieve on a constrained environment such as the ESP32 microcontroller and had been doing a lot of investigation into how to get audio data into the device. This seemed to spark a lot of interest in the community and I had a number of people contact me about projects they were working on. I had the idea of building something that would inspire other people to build interesting projects and to showcase what is possible with these devices. What it does It's a home assistant called "Marvin" (I chose to use "Marvin" as my wake word in memory of the paranoid android from the Hitch Hikers Guide to the Galaxy). You can ask it to turn off and on lights, tell you a joke, and to tell you about life. How I built it For the wake word detection, I trained a TensorFlow model on a variety of audio data. This included the speech commands dataset which contains the word "Marvin" along with various samples of background noise and people talking. To create something that the neural network could learn I split the audio data into 1-second segments and created a Spectrogram . This turns the audio into an image that can then be fed into a convolutional neural network for recognition. The trained neural network was then converted to a TFLite model which can be run on a microcontroller. To get audio data into the ESP32 I used an I2S microphone board and streamed the audio data directly from this into the neural network to detect when the wake word occurs. Once the wake word is detected a connection the audio data is streamed to Wit.ai so that the user's command can be decoded. To train Wit.ai we feed it with a set of sample phrases - e.g. "Turn on the kitchen" and tell it how to interpret the phrase. Wit.ai learns to generalise this input and pull out the user intention along with the object they are trying to manipulate. Wit.ai sends the user's intention back to the ESP32 and the requested command is executed. Once that is complete the device goes back into listening mode, waiting to hear the wake word again. Challenges I ran into Generating sufficient training data for a machine learning project is always an issue. One of the biggest challenges on this side was dealing with the large amount of data that is required to get a sufficiently generalised model out of the training process. I had to keep the pre-processing of the audio data to the bare minimum to be able to implement the same process on the embedded device. Translating the code for this from TensorFlow into C++ involved considerable spelunking into the TensorFlow source code. Another issue I faced was dealing with the constraints on a small microcontroller. In particular, running out of memory was a constant issue - running both a neural network, buffering audio data, and making SSL connections to a server becomes almost impossible so you need to shut down portions of the code that are not needed in the different phases of operation. Accomplishments that I'm proud of I managed to get the wake word detection to run in around 100ms - this is pretty impressive given that it needs to run multiple Fast Fourier Transforms to generate the Spectrogram and run a convolutional neural network model as well. Being able to run this quickly means that the wake word can be recognised almost instantaneously making the system very responsive. What I learned Before this project, I had only looked at machine learning on images. This was the first time I had looked into audio data. I now have a good understanding of the different techniques involved in preparing audio data for a machine learning project and what kind of models work well on the problem. I learned a lot about getting data into and out of the microcontroller, in particular, I learned how to use the I2S audio interface and DMA to transfer audio data directly into the microcontroller's memory. After using Wit.ai I now have a better understanding of how intent recognition systems work and what their strengths and weaknesses are. What's next for DIY Alexa I'm building a custom circuit board and 3D printing an enclosure for the project so that it looks really good and would fit nicely in anyone's home. This is a project that anyone with programming skills could tackle. The electronics side of things is very straightforward and only involves connecting a few wires on some breadboard. I'm planning on expanding the capabilities of the device using more Wit.ai intentions. Mostly I'll be driven by the community and what they suggest! <div