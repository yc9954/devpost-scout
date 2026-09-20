---
slug: "qnx-raspi-setup-util"
url: "https://devpost.com/software/qnx-raspi-setup-util"
title: "QNX-RasPi-Setup-Util"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 442
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# QNX-RasPi-Setup-Util

> Configuring your QNX Raspberry Pi can be a long and boring process. Accelerate it with QNX-RasPi-Setup-Util, do all the essential steps through an interactive program in the simple way!

[Devpost](https://devpost.com/software/qnx-raspi-setup-util) · hackathon [[Hack the North 2025]]

## Facets


**stack** c++, cmake, ftxui, qnx

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for qnx-raspi-setup-util

## Body

Inspiration Manually configuring the QNX Raspberry Pi from scratch is a long and complicated process, and often require the users to have terminal and Linux/Unix related skill and experiences. Coming from a robotics development background, a lot of people working on the robot may not have such experiences, hence the need of a tool that makes the process simpler and quicker. What it does QNX-RasPi-Setup-Util is a easy to use interactive program that allows the user to easily configure all the essential stuff on a QNX Raspberry Pi, without having to mess around with different configuration files, terminal file editors, and other stuff, allowing everyone to quickly configure the Raspberry Pi with QNX OS on it in the way they need. How we built it The program is written in C++ with CMake as the build system. QNX Software Development Platform 8.0, QNX Toolkit, and Docker Build Environment for QNX on macOS are used to power the program development and building environment. FTXUI is used when the terminal supports UTF-8 to provide a more intuitive user interface when possible. Challenges we ran into QNX requires a unique set of tools (e.g. compilers) to have the software built for it. Which took me a relatively long time to properly configure and develop an efficient workflow to build, upload, and test the program. Accomplishments that we're proud of Since the environment I am using is not officially supported by QNX, I've developed some customized scripts to automate the development workflow that involves code compiling and executable uploading and testing that makes the workflow more efficient and usable. What we learned This is the first time I write any user application with C++, and alongside the extra C++ knowledges I gained that are more particular to building a program for a user to interact with, I also learned a lot about configuring C/C++ toolchain while tinkering with the project. What's next for QNX-RasPi-Setup-Util In the future, the terminal user interface of the program needs to be more polished. Also, looking back at what inspired this project, configuration export and snapshot features can be developed, as this program is meant to make the configuration process of the QNX Raspberry Pi easier, and these features allows the user to deploy multiple Raspberry Pi with the same configuration if needed, and if any faulty configuration changes is being done, the snapshot feature can be used to roll it back to a working state as long as the terminal is usable. A binary upload feature can also be done which could facilitate the process of uploading and/or updating programs written for QNX OS for it to be run. <div