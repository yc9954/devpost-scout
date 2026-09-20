---
slug: "mockchain-learning-decentralized"
url: "https://devpost.com/software/mockchain-learning-decentralized"
title: "Mockchain: Learning, Decentralized"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 416
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
---

# Mockchain: Learning, Decentralized

> Mockchain: Learning, Decentralized. Be rewarded for teaching. Be rewarded for learning.

[Devpost](https://devpost.com/software/mockchain-learning-decentralized) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**user** [[educator_student]]

**stack** amazon-web-services, lambda, livestreaming, opentok, particlejs, react, serverless, tokbox, tsparticles, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mockchain: learning, decentralized

## Body

Landing/Login Page Event Dashboard when logged in Creating an event/lesson (for teachers) Attending a live lesson hosted on Mockchain (for students) Activities page to earn MTC Submitting answer to quiz activity Earning MTC from getting question correct LIVE AT mockcha.in ! Inspiration Teaching is one of the most valuable acts one can undertake, and therefore we had the idea of Mockchain, a blockchain-based educational platform. We wanted to build a platform where talented individuals and teachers can be compensated for teaching others their subject. In the fashion of online lessons, these teachers can share their knowledge through live-streamed lessons that students can only access by paying the required entry fee in MTC, almost like a ticket. What it does Upon logging in, each user is given a certain amount of MTC for free. MTC is our virtual currency (we wanted to implement this as a cryptocurrency). MTC can be earned by either engaging with lessons, or by completing regularly changing educational activities on the site. Teachers can create and host a lesson on Mockchain for free - without paying any MTC. This creates a lesson room; essentially a live streaming room where they can then present their lesson to students. They can also set an entry fee in MTC, corresponding to how much they believe their lesson is worth. This also gives an incentive for teachers to produce high quality lessons, as they can then charge a higher entry fee for access to it. Students can then browse Mockchain for a lesson/event that interests them, pay the required entry fee (which goes straight to the teacher), and access the live lesson at the scheduled time. How we built it TypeScript/React for the frontend, hosted on Netlify Serverless backend built on AWS using Lambda functions + other various services Tokbox API to build streaming service ParticlesJS/TSparticles to build landing page Challenges we ran into Implementing particles in landing page Implementing live streaming service using Tokbox Creating live streaming "rooms" for each individual lesson Accomplishments that we're proud of Getting the live streaming to ACTUALLY WORK, even with separate rooms for each lesson! Getting something functioning Not really a hard accomplishment, but getting the mockcha.in domain was really cool, fitting our name perfectly What we learned Live streaming is fairly difficult to implement ParticlesJS is still a finicky library What's next for Mockchain: Learning, Decentralized Implement an actual blockchain based currency called MTC Implement live chat + file sharing in lessons Teacher reviews Plenty of other stuff <div