---
slug: "tiny-life-3d"
url: "https://devpost.com/software/tiny-life-3d"
title: "3D Game"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 148
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
---

# 3D Game

> Play every day!

[Devpost](https://devpost.com/software/tiny-life-3d) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**substrate** [[video_visual]]

**stack** ai, blender, lensstudio, photoshop

## How they structured the write-up

- how i built it
- what i learned

## Body

How I built it I built this using Lens Studio and complex JavaScript . I used AI to help generate the core logic and math for the script, while I handled the entire scene composition, 3D asset management, UI design, logic integration, and testing. The core technology is the Persistent Storage System . Instead of just saving a score, I save the exact Unix Timestamp of the user's last action. When the Lens is opened again, the script calculates the precise time difference (delta time) between "Now" and the "Last Save." What I learned I learned a huge amount about Lens Studio's capabilities. specifically: How to implement Persistent Storage for complex data. How to utilize the Character Controller and Camera Controller for third-person movement. How to manage a very saturated script with dozens of inputs and dependencies. How to integrate AI-assisted code into a manual workflow effectively. <div