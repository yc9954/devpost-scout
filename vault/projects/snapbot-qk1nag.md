---
slug: "snapbot-qk1nag"
url: "https://devpost.com/software/snapbot-qk1nag"
title: "SnapBot"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 283
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# SnapBot

> Snapbot is a robotics platform that allows you to control robots through Snapchat.

[Devpost](https://devpost.com/software/snapbot-qk1nag) · hackathon [[Snap AR Lensathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[video_visual]]

**stack** arduino, lenscloud, syncframework

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for snapbot

## Body

Arduino Wiring Inspiration I have loved building robots ever since I was a kid. Now as an adult, I wonder how Augmented Reality could interface with robots in the future. I was inspired by my high school robotics teacher and SciFi movies for this project. What it does This Lens is the SnapBot Controller to drive the robot. It uses the Sync Framework to connect 2 phones together. One phone acts as the controller, the other phone acts as the driver for the robot. The robot has 2 photoresistor sensors which allow the robot to detect commands on the screen. In addition, an Image Tracker can be placed on SnapBot to visualize a 3D character while you drive it! The goal with SnapBots are to educate students how to build robots, while also learning how to use Lens Studio. How I built it I used a standard robotics kit for the hardware and use Lens Cloud for realtime communication between the phones. Hardware Specs: Arduino Nano 4 DC Motors 1 L298N Motor Driver 2 Photoresistor Sensors 4 Toy Wheels Wires, batteries, and mounting hardware. Challenges I ran into Simple issues with wiring and electronics caused minor delays. Understanding the Sync Framework and Lens Cloud was challenging at first, but the live streams helped. Accomplishments that we're proud of This may be one of the first robots that can be controlled with a Snapchat Lens :P Combining technologies (electronics, AR, and Cloud computing) was very rewarding. What we learned Remember to ground your wires correctly. What's next for SnapBot I plan on further improving the UX, hardware design, and accessibility. I would love for kids to use this robotics platform in the classroom. <div