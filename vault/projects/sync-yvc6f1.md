---
slug: "sync-yvc6f1"
url: "https://devpost.com/software/sync-yvc6f1"
title: "Sync"
hackathon: "hack:now"
winner: true
words: 682
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Sync

> Sync up with friends while doing the same tasks to keep yourself accountable. Just as if you were working beside each other at the library.

[Devpost](https://devpost.com/software/sync-yvc6f1) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[video_visual]]

**stack** go, hasura, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for sync

## Body

private task feed in a sync create new task Inspiration Last September, a group of my friends and I were living in the same house, perched on a really tall hill in San Francisco. Recruiting season was coming up, and we all needed to update our resumes, and practice interview problems. Whenever a few of us were working at the dining table, others would notice and join and work as well. Just the action of sitting by each other and working at the same thing at the same time somehow made us all more productive. In the age of social distancing, there is a lack of social pressure from peers to get work done. We waste away hours lavishing in the endless content from streaming providers and scrolling the infinite feeds of social media. We sought to create a platform that allows students to sync up and work on upcoming shared tasks together virtually. Specifically, we wanted to recreate the library environment in which students work together and face social pressure to get work done. This environment will be beneficial to current students adjusting to their new virtual lives and the incoming class of 2024. What it does Sync enables students to plan to do tasks at a specific time and invite your friends who are also doing it to join you. When the time comes up to do the task, all participating members can join the voice call to work as if they were physically together. There will be checkpoints in the sync call so that when students finish, then can mark them as done and the members of the sync can see who has completed the task and who has not. The home feed will be a list of upcoming tasks that you planned or that your friends invited you to ( Private Syncs ) and a list of public tasks open to everyone in that community ( Public Syncs ). Since you join using your school email, you are automatically added to your school community and you can add other communities later (such as your program, specific courses, etc.) Likely, the incoming class of 2024 will be online. It'll be difficult for students to find people to study with given the remote classes. Public Syncs will allow students to make friends within their communities (classes) similar to how they would in the usual classroom setting. Current students who've adjusted to the at home Zoom lecture lifestyle also need accountability in finishing their tasks. We, the creators of Sync, all voice call each other using Zoom or Discord to keep ourselves free of other distractions and get work done - since the mentality is "if other people are working, so should I". This is an individual productivity tool that uses social presence and pressure. Collaboration and socializing are not our core focus. How we built it We built our backend using Go, Hasura and Postgres, and built our frontend using React and Typescript. Our main web server is deployed on Google Cloud Platform using Docker. Challenges we ran into WebRTC, which we initially thought couldn't be too hard to get working well enough for a demo, turned out to be a nightmare of complexity. In the end, we opted to forgo writing our own signaling server and use the SimpleWebRTC API, whose statement of purpose is exactly to "eliminate all this pain for [us] so [we] can focus on [our] product". Accomplishments that we're proud of Our experience has allowed us to choose the right technologies for maximizing the development speed. For example, we have successfully avoided most of backend grunt work by using the Hasura GraphQL Engine, allowing us to focus our attention on the code that really mattered. What's next for Sync We're looking to finish up features in our product such as public tasks from communities and admin accounts to host communities. In addition, since we currently generate our cover photo randomly, we want to leverage the the Unsplash API to generate the image based on what the user inputs as the title (got rate limited!). <div