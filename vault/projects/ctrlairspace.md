---
slug: "ctrlairspace"
url: "https://devpost.com/software/ctrlairspace"
title: "Ctrl+Air+Space"
hackathon: "Hack the North 2020++"
winner: true
words: 549
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Ctrl+Air+Space

> Swipe This™

[Devpost](https://devpost.com/software/ctrlairspace) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[video_visual]] [[web_dom]]

**stack** azure, electron, javascript, mediapipe, opencv, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ctrl+air+space

## Body

Logo You can play osu! Turn that SOUNDTRACK UPPP! Inspiration We've all been in that position where we're sitting at our desk in a leaned back, comfortable position watching something on our computers, especially now when we're stuck at home more than ever before. This is all great until when something suddenly demands a physical user interaction, whether it's to pause the video, scroll down a webpage, or even adjust the volume, forcing you to reluctantly leave that position of comfort to sit up and do what's demanded through the keyboard or mouse. Our team members know this struggle all too well and so we were inspired to resolve this problem by creating Ctrl+Air+Space. What it does Ctrl+Air+Space grants you control over the systems most commonly used and important functions literally at your fingertips and in the palm of your hand using just the webcam. Through different hand signals and motions, you can perform functions that include moving the mouse and clicking, switching between windows by swiping horizontally or vertically, adjusting the volume, scrolling up and down a page, and even entering text using your voice all the while sitting in the comfortable position you desire. Need to search something but don't want to get up? No problem, just signal the cursor to the search bar and tell it what to search! Someone walked in to ask you something but it's too loud? Easy, put up a rockstar sign and drag that volume slide down! How we built it In the back, we used both the MediaPipe API and machine learning to detect the gestures. The Hand Landmark Model of the API provided locations of key points on a hand in an image. The key points were then used as features inputted to a K-Nearest Neighbours model that is trained on custom-generated data. The data consisted of examples of keypoints for each gesture that was used. We created a python script that we can run anytime we want to add gestures to the knowledge base; this script allows us to easily and quickly generate data that is automatically used by the main program without additional modifications. The voice interaction feature was implemented using the Microsoft Azure Speech to Text APIs . We built the user interface using React with Electron . The boilerplate code for this integration was provided by the electron-react-boilerplate repo by Jerga99 on GitHub. From this, we created a prototype settings UI that allows users to select their preferred computer action for each gesture and to select their preferred mouse and scroll sensitivity. This was then connected to the python backend via a Flask server. Challenges we ran into • Devising the transitions from one gesture-action pair to another • Learning Electron and implementing with React.Js Accomplishments that we're proud of • Creating a streamlined machine learning process where we can easily add/remove gestures • Team perseverance • Learning Electron What we learned • That Google Mediapipe is an AWESOME tool • Sometimes a simple solution is all that is needed to solve the problem (we used a simple machine learning model since more complex ones were not needed) What's next for Ctrl+Air+Space Adding more gestures and tweaking our gesture pipeline for more seamless interaction! Also adding a download link to our current domain: http://ctrlair.space <div