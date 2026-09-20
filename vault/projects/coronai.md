---
slug: "coronai"
url: "https://devpost.com/software/coronai"
title: "CoronAI"
hackathon: "hack:now"
winner: true
words: 434
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# CoronAI

> Using Electrical Impedance Tomography to create a portable, (much) cheaper and instantaneous lung scanning band to help doctors monitor patients without human interaction

[Devpost](https://devpost.com/software/coronai) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]

**stack** keras, machine-learning, opencv, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coronai

## Body

Inspiration When all of us watched a viral video of a nurse in NYC sharing her experience having to see so many patients lose their lives in front of her, we knew there had to be something we can do. It's so hurtful to think that while the whole world is social distancing, doctors and nurses have no option but to face the coronavirus, battling all odds only to save humankind. This was our inspiration - if there was some way for them to be able to monitor these patients without having to interact with them, they, too, could social distance. What it does CoronAI is a band that one can wear around their limbs and chest. In these times, this band is worn around the chest, and the electrodes extract real-time images of the lungs, connected to a monitor. This monitor is then connected to a dashboard for access by a doctor, who is able to analyze this live scan, and even compare them. How we built it This is done by using numerous electrodes, and sending small frequencies of current from each one. When this is done, the other electrodes experience a changing equipotential, and at the intersections of the frequencies from each electrode, a tomographic image is created. Coupled with machine learning models we wrote, we are able to extract these images into real-time footage of the lung, which expands and contracts as the user breathes. Challenges we ran into It was incredibly tough for us to be able to come up with a successful model of this, given that we did not have much background. For this reason, we each split up to handle one aspect, with one of us doing the machine learning research, two of us experimenting with the hardware available and one of us researching the feasibility of this technology and creating the demo. Accomplishments that we're proud of In the end, we are so excited to share that we were able to create fully functioning technology! Our technology actually works, and can easily be integrated into hospitals. What we learned We learnt the importance of "if there is a will, there is a way" - we all had a passion to help those who are helping us, so we put in blood (figuratively), sweat (literally) and tears (literally) to make this happen. We are so excited to see what this does! What's next for CoronAI We hope to pitch this to investors to get funding and mentorship so that we can actually see it in action in hospitals, helping doctors and nurses around the world. <div