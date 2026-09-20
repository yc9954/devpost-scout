---
slug: "roman-road"
url: "https://devpost.com/software/roman-road"
title: "Roman Road"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 806
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Roman Road

> Type faster with less mistakes using bigram latency data

[Devpost](https://devpost.com/software/roman-road) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[health_clinical]] [[labor_employment]] [[legal_justice]] [[transportation]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** claude, next.js, node.js, react19, typescript, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for roman road

## Body

Typical predetermined diagnostic typing test AI feedback and grading from 1 written diagnostic Free Flow screen, ready to capture keystrokes across the entire system Drill interface, gives intuitive suggestions as well as targeted practice WPM line graphs comparing progress of Free Flow writing, predetermined diagnostics, and drills Inspiration While every popular LLM seems to be trying to make typing obsolete, we believe that for those who build a good foundation in their craft, typing will continue to bring value even in light of innovation. Just as many roads leading to Rome stay true and solid to this day. The new challenge presented is to make typing accessible and efficient to as many people as possible. What it does Roman Road is the most attentive typing tutor on the internet. Mainstream competitors like Monkeytype don't serve the functional purpose of making you a better typer in the real world. This is because they cherry pick a word database that is purposefully easier than normal writing, inflating numbers significantly. Some other sites include more complex words but don't offer anything beyond that. Roman Road pays attention to minute details, including which words are typically performed poorly on by the user, but also which bigrams (two letter combinations) tend to have the most latency. Using this data, Roman Road provides drills that specifically target these weak points with words the user has historically struggled with, as well as words generated from batches containing their weakest bigrams. By focusing on personalized pain points in typing, we made sure that users would experience a leveling in their general typing ability rather than a few shiny "personal fastest WPMs." Just like how potholes cause hiccups and traffic on roads, we realized that these "potholes" of difficult words should be prioritized in order to firstly make the user typing experience as smooth as possible, to facilitate incremental increases in overall speed as time passes. How we built it We used Windsurf to build the app full-stack in TypeScript, using React 19 for certain UI components as well as Next.js for some App Router conventions. We used a Python script and a Node.js Websocket bridge to record whole system keystrokes. Bigram and word data is processed live using Claude's Sonnet 4.6 to generate intuitive summaries and actionable steps for users. Challenges we ran into We realized that realistically, people may not want to stay on our platform long term to do diagnostics, especially not over and over again to inform our drills of what to work on next. This came from the overall issue that typing apps in general do not retain their audience especially well, since people rarely sit on a site typing in a box completely voluntarily. This is actually the reason behind the cherry-picked inflation strategy seen in popular sites. We wondered how to retain the people we were trying to help and keep them filling out diagnostics, but we realized that many ways to do so go against our principles. Accomplishments that we're proud of We're very proud of our response to the challenge of retention, which ended up being the opposite: letting people live their lives outside of the website and collecting their keystroke data to inform drills in the background as they complete tasks in their daily life. By introducing an automatic activation using a minimum word count of 5 words within 5 seconds, we were able to capture many sessions of the user typing completely apart from our web app, be it writing on Google Docs, sending an email, or even responding to a DM on Slack. We're also very proud of our drill system to begin with. It grabs the most recent data of struggle words and bigrams from the last 3 eligible sessions, making sure that the issues worked on and addressed are not stale, but instead always changing and dynamic. What's next for Roman Road Personally, I genuinely believe in the utility of Roman Road. I will personally be grinding on Roman Road to try and reach a consistently 100+ WPM as a lifetime 75 WPM typer. Furthermore, I want to see just how helpful and intuitive the site can be for those just starting out typing, as well as whether it can help break plateus for those typers who are already very proficient. Roman Road's potential doesn't stop at individual users either. In professional settings where writing speed and accuracy directly affect output, such as software engineers, writers, data entry, and those in legal work--Roman Road could be deployed at an organizational level, aggregating weak points across teams to inform targeted training. The passive keystroke collection means onboarding requires almost no friction. People just work, and Roman Road works in the background. Fewer slowdowns, more output, and a workforce that actually improves over time rather than just getting used to being slow. <div