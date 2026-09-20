---
slug: "dockerc"
url: "https://devpost.com/software/dockerc"
title: "dockerc"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 418
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# dockerc

> Software distribution solved.

[Devpost](https://devpost.com/software/dockerc) · hackathon [[TreeHacks 2024]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** zig

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for dockerc
- accomplishments that we're proud of
- what we learned

## Body

Inspiration Distributing software is difficult. A lot of projects end up getting their users to run docker run to make things simpler. However relying on docker makes things complicated. Users need to have docker installed, users need to have the correct docker version. Installing docker is often a pain, you need to setup permissions correctly (docker needs to run as root). There are other ways of distributing software but they require a lot more investment. Writing Dockerfile s is just so easy! Dockerc solves this problem: Builders can continue writing Dockerfile s Users can just download a single executable and run it, no need to have 10 thousand setup steps What it does Dockerc takes existing docker images and a single executable file from them which can be distributed to your users. For 0 setup, you get the best possible form of software distribution: a single file to download. How we built it The compiler and runtime are written in zig. In order to have incredibly fast startup times no copying is done at runtime. The image is stored as a squashfs file and so the startup is near instant. (a squashfs file is a file that represents a file system and that can be mounted in the directory structure) Challenges we ran into Avoiding the copying of data was a difficult task. Most docker files are hundreds of megabytes large so we cannot afford to copy! The most difficult part was finding a way to mount the squashfs because it required identifying the offset of the squashfs file within a file that the squashfs-mounter could use. Things I tried: Using the /proc filesystem to identify how the executable was mapped into memory and to then deduce the location in the physical file based on that. (/proc/self/maps) Using /proc/self/mem so that I can just directly use the pointer to the embedded file. Unfortunately, I didn't realize that processes couldn't access each other's memory until I implemented this... Overall the biggest challenge was using Zig. I had never used the language before and because the language has so little documentation it made things very challenging. What's next for dockerc Make a paid web platform on which people can generate executables with the click of a button! Add MacOS support using QEMU Add support for ARM64 (currently a lot of the binaries are just hardcoded) Accomplishments that we're proud of What we learned Zig How containers work internally Example projects that make use of docker for distribution: https://github.com/oven-sh/bun https://github.com/shepherdjerred/macos-cross-compiler <div