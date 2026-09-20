---
slug: "cueme"
url: "https://devpost.com/software/cueme"
title: "Cueme"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 649
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/video_visual"
---

# Cueme

> Cueme is a unified messaging application that lets you mail, message, WhatsApp on the same platform

[Devpost](https://devpost.com/software/cueme) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[video_visual]]

**stack** .xyzdomain, alan, android, android-studio, civo, dart, datree, docker, flutter, github, go, googledevlibrary, kubernetes, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into and accomplishments that we're proud of
- what we learned

## Body

GIF Inspiration This is for the lazy people, who are not able to keep up with their existing reminders and would like personal attention from their friends and family or even, themselves. Although we have got our good ol'reminders, the impact of a personal message makes a difference. Having to be reminded on our daily-use social media platforms, in our opinion, would be a safer bet than our usual reminder apps. For instance, we are likely to pay more attention to a Whatsapp (or your choice of social-app) message than a reminder that we snoozed ten times already. What it does Sends a message to your desired contact via (currently) three platforms - WhatsApp, SMS, Email. Can be scheduled for later too). This sounds simple but, imagine what it could do as a full-blown API. How we built it First, we decided to make this service accessible to all by making an API for it :D Golang is an ideal choice. Mainly for its simplicity and no hacky syntax but also for its lightweight threads (goroutines) as we have a lot of scheduling to do in our service. After deciding on the API we then proceeded towards incorporating more tech stacks by creating a client app for the API. Again, choosing Flutter was a no-brainer considering two of us were going to make their first-ever app. After making the MVPs for both API and client, it was time for deployment. This took more than half our time from the hackathon as none of us had any knowledge about it. A full night to make a docker image and push it to the hub! Through those tons and tons of YAML config files, we finally managed to deploy the image to our first cluster and it felt like a big deal. After the first patch, it was smooth sailing. Civo really helped with the effortless first-time setup but, wish it had better tooling (opensource here we come! :D). Finally, we added the Alan Ai assistant to our client app to give a good-presentable demo of our own API. which is quite underrated though. This was the part where all four of us spent a lot of time writing good scripts and testing, talking endlessly with a robot (it was hilarious at times). Challenges we ran into and Accomplishments that we're proud of 1. Team collaboration: Being our first team project, it was tough for us to divide jobs for micro-jobs because there were no actual micro jobs at the beginning point. Everything was a big task and dividing it seemed overcomplicated. 2. Choosing the right stacks for us: It's enticing when some technologies have kept such great prizes, but we couldn't add everything in-app. To keep control and maintain the boundary of our app was also one of the challenges we faced. 3. Tech-stack conflicts: We all had experience in different tech stacks. This is what we thought would be a challenge to us but we saw the power of a 3-day deadline at work. 4. Deployment: Kubernetes/docker was the most overwhelming part of this hackathon and we are proud to have survived the sea of YAML files. It will be much easier the next time we are going to deploy an app on the web. What we learned 1. DevOps: Although we just got an introduction to the world of containers, it is definitely helpful to have experienced it in a project. 2. Working in a team: How to manage tasks, keeping regular touch with our teammates so that we don't clash upon the tasks. Keeping a high spirit is equally important as staying productive in tough times. 3. Importance of documentation and writing clean code: Now that we actually had to work with each other's code, it really showed us the importance of writing readable code and the pain we give our colleagues of writing cool one-liners. <div