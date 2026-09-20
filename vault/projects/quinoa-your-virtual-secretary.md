---
slug: "quinoa-your-virtual-secretary"
url: "https://devpost.com/software/quinoa-your-virtual-secretary"
title: "Quinoa - Your Virtual Secretary"
hackathon: "Hack the Northeast"
winner: true
words: 743
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Quinoa - Your Virtual Secretary

> Quinoa is a personal assistant that learns to minimize the boring parts of life and maximize your free time to do the things that matter.

[Devpost](https://devpost.com/software/quinoa-your-virtual-secretary) · hackathon [[Hack the Northeast]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]

**stack** amazon-alexa, amazon-web-services, dart, flutter, kotlin, ktor, node.js, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for quinoa - your virtual secretary

## Body

Quinoa - Your Virtual Secretary Home - Check what's next or book your next event. New Event - Create a new event, all your details are already filled out with specially selected times. Schedule - Take a look at what's coming up. Dashboard - Where you can check on your progress. MiniApps - Interactive experiences tailored around managing your life. QExcercise Mini App Mini App Launcher Inspiration Technology promised to make our lives simpler, but in a lot of ways its made things more complicated. As high school students, lots of our time is spent organizing ourselves using existing management software, and often it doesn't live up to our complicated lives. Finding the best open space in our calendar can be difficultd time consuming. Sometimes the calendar needs to be reorganized when a new event, like an assignment, occurs that throws our existing schedule into chaos. It can be very overwhelming. So before we go off to university and in light of recent advancements to machine learning we had an idea. We sought to make a personal secretary that learns to minimize conflict with other events while saving you time looking at your calendar for free spots. What it does Quinoa will schedule events for you at times that it think will work out best for you. Scheduling is as simple as saying "book me some time to study with Jim" and forgetting about it. As you use it, Quinoa will achieve a deeper understanding of you and your schedule, and will get better and better at scheduling for you. Quinoa is also conveniently right where you need it, either via the mobile app or through the Alexa skill. What distinguishes Quinoa is it's mini apps platform, which allows first and third party "mini apps" that provide extended functionality to be accessed directly from within the Quinoa app, provide key information to the user integrated into the app's inbox, and interact with the users' schedule. How I built it The heart of our project is hosted locally on a ktor server, built with Kotlin. It handles most of the models and classification that are responsible for the reinforcement learning. Our mobile app interface is built with a cross platform framework called Flutter. It is also responsible for some tag classification which is done with a Tensorflow model running on the user's phone. Finally, our Alexa skill is built with the node.js Amazon Alexa skill kit. The skill is hosted on AWS's lambda functions servers. We also used axios and moment.js, two well known javascript libraries, to polish up the experience a bit more. Challenges I ran into While developing Quinoa, we ran into a few challenges, but were able to overcome them with time. Initially, we had trouble interfacing between our mobile and alexa clients. We decided to spend time creating proper api documentation to ensure that everyone was able to create their part properly and Quinoa would run smoothly. Another challenge we faced was optimizing our Tensorflow Model. Due to a lack of time, we were forced to train our model with less data than is usually used. As a result we spent time optimizing our hyper parameters for our data to achieve a working model. Accomplishments that I'm proud of We're really proud that we got our machine learning models working so well, as we are relatively new to some machine learning concepts. We're really happy with how our flutter app turned out, that strikes a new record in usability and intuitivity for our group. What I learned In this hackathon, we all experimented with features we were unfamiliar with, which initially caused issues, but inevitably helped us to become better programmers. Some of our members used Google Colab to train a Tensorflow Neural Network and run it with a flutter app. Some of our members worked with the Alexa Skill Kits, which was a surprisingly smooth and interesting, and even fun first experience. Some of our members experimented with creating a custom supervised learning algorithm (from scratch!) which is the basis of our learning scheduler. What's next for Quinoa - Your Virtual Secretary Moving forward we wish to publish the app. We'd like to improve our Natural Language Processor to increase the accuracy of our classifications, and also add more available tags. We're going to also improve our mini app selection and functionality, and integrate mini app content directly into the scheduler. This will make our flow more streamlined. <div