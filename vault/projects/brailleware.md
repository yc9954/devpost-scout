---
slug: "brailleware"
url: "https://devpost.com/software/brailleware"
title: "FifthSense"
hackathon: "PennApps XII"
winner: true
words: 382
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# FifthSense

> Opening up smart devices to the visually impaired

[Devpost](https://devpost.com/software/brailleware) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** android, arduino, flask, hardware, internet-of-things, java, linode, python

## How they structured the write-up

- what we made
- background
- solutions
- down the road

## Body

What we made FifthSense is an assistive platform designed to make the features of smart devices accessible to the visually impaired based on a unique, simplified, and user-friendly way to communicate using braille. Background Braille is fundamentally a 6-bit character representation using a 3x2 matrix. In current technology, a sequence of these 3x2 grids allows words and longer passages to be read by moving one’s fingers over these bumps. Specifically, actuators raise or lower these bumps to create characters, hence requiring users to move their hand across a platform each time they want to read something. Users also need separate keyboards and mechanisms for input and output. Solutions Instead, FifthSense takes the approach of presenting these characters through a single 3x2 keyboard grid and reuniting input and output. Placing six fingers on the grid of vibrating motors, users would simply hold the device and feel the pattern for a given letter. To support writing in braille, FifthSense combined these output devices with input buttons, allowing a user to simply to press the pattern for a given letter back into the device- without moving their hands. This combined input-and-output approach allows users to move around while using the device and lowers the risk of fumbling around and dropping the device. FifthSense also sidesteps the downsides of audio-based solutions (e.g., a loss of privacy, background noise issues, the limitations of current speech recognition technology). The rest of FifthSense was designed to make our device braille portable and easy to use while on the go. Featuring a custom-designed 3D-printed case, FifthSense was designed to be durable and ergonomic. The electronics are managed by an Arduino; the device communicates with a synchronized smartphone using Bluetooth. We built FifthSense with an Android-based personal assistant: ask it a question and you will feel the response! Our custom Android app features calls to an API enabling a responsive Q&A system. Since the device requires both hands to operate, it also features a distance sensor to replace the need for a walking stick. Down the road In the future, we hope to extend the abilities of FifthSense both by supporting additional smartphone features (using the onboard IMU and GPS to provide safety features, fully integrating web browsing) while also making the physical device more efficient and easy to use. <div