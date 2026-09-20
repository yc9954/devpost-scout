---
slug: "coach-bob"
url: "https://devpost.com/software/coach-bob"
title: "Coach Bob!"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 471
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/video_visual"
---

# Coach Bob!

> Get warmed up at the gym with this interactive AR experience!

[Devpost](https://devpost.com/software/coach-bob) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**substrate** [[video_visual]]

**stack** c++, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

(IMU) Registers hits and calculates force off of wobbles~ Video frame rate is much smoother in camera then recording! Inspiration One of our teammates had to sit out of Taekwondo Nationals due to a strain injury. The cause? A rushed 5-minute warm-up that just wasn’t enough. It was a harsh reminder: skimping on warm-ups (Even if it's boring) is a common mistake, but it leads to real consequences...injury, lost training time, and missed opportunities. It's also a great way for people to get active and stay healthy! What it does We set out to turn that mundane yet critical step into something athletes actually look forward to: an interactive AR warm-up game. By combining guided drills, live feedback, and playful challenges, our system makes proper warm-ups engaging, adaptive, and fun—so athletes are ready to perform and stay safe. Once you put on our glasses and wear our helmet, Coach Bob will shout playful insults to encourage you to get into shape and warm up! He'll also highlight with coloured nodes on the punching bag from the AR glasses whether to do a kick, knee, hook, jab, or straight to the head or body to add variance to the routine. Lastly, performance data such as speed, force, and time are all relayed onto a dashboard which can be viewed after warming up. (Keep in mind that frame rate is much smoother when wearing glasses and not streaming the live feed!) How we built it Used XReal1 glasses to project targets onto Bob with open CV Used OAK 1 AF Camera to get first person footage Used Gemini and Eleven Labs to give Coach Bob a voice Used a MPU-6050 and Bob's wobbles after impact to calculate force of hits and to register them Pulled everything together :) Challenges we ran into We ran into a few big challenges during the build. Since we started later than most teams, we didn’t have specialized sensors to log hit force, so we had to get creative with how we handled impact registration using only the materials we had on hand. On top of that, the AR experience initially suffered from lag and jitter, which meant we had to spend extra time refining performance and smoothing out visuals to keep it engaging. Finally, because the setup would be actively struck and moved around, we had to reinforce and secure all the hardware to make sure it stayed intact during real use. Accomplishments that we're proud of We’re proud that, despite starting later than other teams, we delivered a working AR warm-up game that athletes actually enjoyed using! What we learned NEVER GIVE UP! PLEASE WARM UP BEFORE TRAINING! In the future we want to build a robust teaching feature which can hopefully help people sharpen their martial arts techniques! (Also a multiplayer mode / leaderboard). <div