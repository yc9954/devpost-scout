---
slug: "hackthenorth2020-02khts"
url: "https://devpost.com/software/hackthenorth2020-02khts"
title: "Tabular"
hackathon: "Hack the North 2020++"
winner: true
words: 374
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# Tabular

> A program that allows you to run any keystroke combination through facial recognition and the magic of the Raspberry Pi.

[Devpost](https://devpost.com/software/hackthenorth2020-02khts) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** python

## How they structured the write-up

- tabular

## Body

The Raspberry Pi HackTheNorth2020 Tabular What inspired us? Imagine. You live in a family where you have strict parents who hate video games and only want you to study. They believe them to a complete waste of time. However, you love them but you have to play secretly. One day, while you're studying, you have this massive urge to play League of Legends that you just can't get rid of. You give in. You open the application, queue up and get into a game. While you're playing, you hear footsteps outside your door. You panic. You reach for the alt-tab keys but it's too late. Next thing you know, you're banned from your computer for a year. Some of us on the team know how it feels to be caught playing video games and we want to make sure that those who are just like us don't have to be worried about being caught anymore with our creation. How we made Tabular Raspberry Pi Zero W to make the wireless camera module. Python to create the customization software. Used OpenCV, Tkinter and Pynput libraries. How does Tabular work? We first created a wireless camera module with Raspberry Pi Zero W that takes frames. These frames are then sent to the computer wirelessly. the frames are then scanned for faces. If a known face is detected then the customization software performs a preset keystroke. The customization software allows users to add faces and change the keybind. Technical Difficulties Our Raspberry Pi had limited computing power and memory, which affected both our ability to process faces and our ability to install large Python libraries. We ended up streaming the video to a server to process it on a more powerful machine. The famous alt-tab keybind (aka the namesake of Tabular) did not work with our code. After a bit of troubleshooting, we were able to get it working. Use Cases Never let your parents catch you playing video games again! More Seriously: Proof of concept of a low cost, open source, smart camera system that can be placed anywhere. Accessibility tool for those who have trouble using a mouse/keyboard. Our easy to use keybind system makes Tabular perfect as an accessibility program. DOMAIN.COM SUBMISSION: DiscreteTabbing.tech <div