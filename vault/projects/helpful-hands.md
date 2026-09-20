---
slug: "helpful-hands"
url: "https://devpost.com/software/helpful-hands"
title: "HelpfulHands"
hackathon: "PennApps XII"
winner: true
words: 649
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/structured_db"
---

# HelpfulHands

> Volunteer Mentoring for anyone, at anytime, anywhere.

[Devpost](https://devpost.com/software/helpful-hands) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** canvas, css3, express.js, github, html, html5, jade, jasmine, javascript, linux, mongodb, mongoose, nginx, node.js

## How they structured the write-up

- what is helpfulhands?
- how does helpfulhands work?
- that's great! but how does that work?
- challenges we ran into... oh no!
- helpfulhands' greatest accomplishments
- what's next for helpful hands

## Body

What is HelpfulHands? Let's face it. Tutoring is often times more difficult to set up and organize than intended. From setting a proper date to meeting at a certain location, along with the various logistics of planning a tutoring session, the process is simply (or maybe not so simply) too complicated. So we created HelpfulHands. This is an online tool that can connect tutors with tutees via a point-based system. Now, people can tutor others in the fields they think they're most proficient in, while receiving help in the subjects they find hard to grasp. With HelpfulHands, it is now possible to receive tutoring at any time of the day and from anywhere in the world. How does HelpfulHands work? HelpfulHands is a web-based application that allows users to search for mentors in whatever subject they desire, where the app then connects the tutor and student via live chat (powered by WebRTC and Twilio Video). Additionally, to accompany their tutoring session, the app features a "collaborative drawing pad" in the same window! That way, both student and teacher can communicate easily with one another and both learn and teach effectively. That's great! But how does that work? This was built on the MEAN stack (but without Angular, substituted for Jade). That means that it runs on a node.js server with MongoDB as its database. It then uses WebRTC (supplied by Twilio Video, which is currently in a beta-phase) to connect tutors and students in a real-time video chat. Each chat room has a max of two users, and we can track which user enters which room using Socket.io, which allows for real-time and live-updating applications. We used Socket.io to build the collaborative drawing pad so that any changes to the view in a chat room are propagated between the mentor and mentee. Challenges we ran into... Oh no! If anyone can go through a hackathon without hitting a bug, then we commend them. We first ran into issues with Facebook's OAuth because we were redirecting to a page (but only some of the time, which was the mistake). Thus, we would get "HTTP 302 Redirects" for the homepage with no indicator as to why that was occurring. Then, setting up WebRTC, we almost gave up. We had no idea how to couple the live-stream chat system with Socket.io to create multiple chat rooms. Eventually, we got something to work. I think we're in the phase of "My code works and I don't know why." Finally, we had to get the collaborative drawing pad to work and that was a pain because we had to create everything ourselves. There wasn't any public API we could use for that interface. HelpfulHands' greatest accomplishments Hi, my name is Donna Yu. I wrote this blurb on HelpfulHands and I helped build the web app! This was my first hackathon and it was more intense than I had imagined. I wanted to build an app that I thought could really benefit my community, as well as change the face of education. And I thought to myself, "I wish tutoring was easier," since I like to do community service work by tutoring underprivileged kids in my neighborhood. So it was my idea to create HelpfulHands. This has been an unforgettable hackathon and I really want to continue working on this app after this hackathon, to see it grow and possibly be used by other communities as I push for mine to adopt the technology. It's also humbling to be around all of these amazing coders, and to still be a high-schooler. What's next for Helpful Hands In the future, we hope to connect with community service tutoring organizations for underprivileged students and have them match up their students with mentors on Helpful Hands. We would like to implement a community service hour counter so mentors can receive credit for the hours they have tutored. <div