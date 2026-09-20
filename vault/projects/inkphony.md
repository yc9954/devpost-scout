---
slug: "inkphony"
url: "https://devpost.com/software/inkphony"
title: "Inkphony"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 465
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# Inkphony

> Everything around you becomes an instrument that you can use to make music and learn composition.

[Devpost](https://devpost.com/software/inkphony) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**substrate** [[video_visual]]

**stack** depth, meta, pca, quest, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- updates for this competition
- what we learned
- what's next for inkphony

## Body

Inspiration From our musical and XR backgrounds, we decided to create a highly creative tool to learn and experiment with instruments generated from your environment, the world becomes an instrument! What it does Inkphony allows you to write music on any surface around you and create endless instruments that you can play your music with until you find the right sound. Easily iterate using the handtracking note writing and scrubbing gesture to delete. How we built it Using the latest Meta PCA (v81), which features time-stamped and stereo camera access together with Gemini API, ElevenLabs, and our advanced filtering/cleaning system, we were able to build an asynchronous, continuous background recognition that seamlessly generates icons and instruments dynamically from your surroundings. Challenges we ran into The usual image recognition data-to-world aligning, which was solved by storing the depth frame together with the camera capture, to later align properly when the Gemini API result was ready. This allows us to get correct results aligned to the real world, even if we are moving our heads. Accomplishments that we're proud of The seamless background object detection system, the smooth hand-tracking implementation that opens up many possibilities compared to being limited to the Logitech pen. Updates for this competition We worked extensively on the PCA-AI implementation, bringing it to a production level. We used the newly released PCA (v81) that enables the use of time stamps and stereo video feed. New Features: AI Continuous asynchronous background object detection, with an advanced filtering/cleaning system that doesn't clutter the user's play space. The AI feature can be toggled on/off, but is enabled by default. Icon and sound effect generation in real-time allows for endless instruments and song possibilities. New stereoscopic shader effect that allows the user to "pinch" the real world and either "play" it or "extract" the sounds out of it to plug them into the music tool. Gameplay Major fixes to the note detection algorithm to work with index touches Ability to add or subtract extra measures to the staff (make looong songs) Ability to snap AI musical nodes in instrument slots Hand tracking Implementation: Tap to create notes "Scrub" the staff to erase notes Drag and rotate the staff for better placement. What we learned Depth-align a camera frame to a depth frame with timestamps, using stereo camera access to create mind-bending deformations in real time! What's next for Inkphony The top 1 next feature that we are implementing before publishing is saving and loading your songs and instruments. Then, have the capability to have multi-instrument compositions: "Make the bass with an apple sound, the rhythm with a bottle sound, and the melody with a cup!" After that, the ability to share songs with other users, and being able to listen to other people's compositions and instruments! <div