---
slug: "pomodora"
url: "https://devpost.com/software/pomodora"
title: "Pomodora"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 850
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# Pomodora

> Track your time and remember to take breaks with Pomodora.

[Devpost](https://devpost.com/software/pomodora) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** forge, github, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pomodora

## Body

Pomodora's mascot, Dora Pomodora banner and tagline Inspiration Pomodora was built as a celebration of rest and productivity, and was inspired by the Pomodoro Technique. The Pomodoro Technique is a method of timing your work. With this method, you alternate short bursts of work with short breaks (and eventually a longer rest!) so that you can stay focused and motivated. It's also the favoured productivity tool of my friend group; though we all work in different sectors (and from different countries nowadays), we find value in doing work at the same time as one another. One way we've managed this despite physical distance is through Pomodoro timers. Essentially, one of us announces that they need to get work done, we set a timer, and we all work on our respective projects. We find it really helpful, and I thought that Jira users might think so as well! But what good is a timer without some motivation? Enter Dora, Pomodora's mascot and your new coworker. Dora is designed to keep you on track while you work, as well as remind you when to take a break. She can also collect the time you and your coworkers spend working and add it together into her dashboard, so you can see your progress and celebrate the progress you're making towards your goals. What it does Pomodora has two formats: On the Jira Issue Panel, it's a timer that tells you when it's time to work and when it's time to take a break. On the dashboards section of Jira, you can add the Pomodora Dash! gadget to any of your existing dashboards to see information about your current Pomodoros, as well as your team's collective progress. How we built it Pomodora is built in Atlassian Forge. I'd never used Forge before Codegeist, and it had been a while since I'd touched Javascript, so a lot of Pomodora's early development was making small iterations on small pieces of code, until that code became bigger and more robust. Naturally, I had a Jira board set up on my developer account! I went through a cycle of planning out work in Epics and creating Stories of necessary features, and then creating those features in mini-sprints. When an Epic was complete, I would reevaluate the current status of Pomodora (and how well it met the Codegeist expectations). Depending on how the last sprint progressed, I would create a new batch of stories and get going coding again! Challenges we ran into There were a few challenges that I ran into when creating Pomodora: There were some things I wanted to be able to do with Forge that were not implemented features yet: Things like creating a dashboard from within a custom UI application or sharing data between user instances (without an external API). It was a challenge to code within the restraints of a set framework! I started Pomodora as a UI Kit application, when it really needed to be a Custom UI application from the start. This meant I spent some time re-building the code in Custom UI. Audio. Just, audio. Between permissions issues on the Forge side, to browsers not wanting to “autoplay” sounds (and outdated guides for how to get around that fact!), getting Dora’s bark to play was one of the hardest parts. Accomplishments that we're proud of The moment I first saw the timer ticking down in real time! I'm incredibly proud of how the bar gets smaller as times goes down. Interfacing with time tracking! I was so pleased to see that Pomodora could add time spent on a work timer into the Time Tracking field on a Jira issue. Creating a dashboard that could use data from other users. While the Storage API seems to keep unique data between user instances, I found a way to utilise work logs to see what other users had been doing. This meant that Dora could aggregate time logged between users! Dora’s bark to signal the end of a timer. It was such a moment of triumph to hear that little soundbite (lovingly collected from my own dog, Lucy) playing through my Macbook speakers. What we learned I learned a lot creating Pomodora (and I don't just mean javascript syntax!). I learned how to reach for finished instead of perfect when creating something on a time limit, and I learned a lot about managing sprints in Jira in order to maximise my productivity. At the same time, I learned that dreaming big can be a good thing. Part of me didn't believe I'd get Pomodora to the state it's in today, but because I chose to reach outside my comfort zone, it's turned out better than I ever could have imagined. What's next for Pomodora Dashboard expansion! I'd like Dora to have even more reports available to the user. More active collaboration! I would love it if teams could start a work pomodoro together. Cleaner, more commented code. Nothing fancy here, I just want to make the code a little easier to read! I want Pomodora to be available on the Atlassian Marketplace. <div