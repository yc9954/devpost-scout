---
slug: "port-judgement-legacy"
url: "https://devpost.com/software/port-judgement-legacy"
title: "[PORT] Judgement Legacy"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 463
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "user/legal_professional"
---

# [PORT] Judgement Legacy

> PORT of Praw bot of r/AmITheAsshole

[Devpost](https://devpost.com/software/port-judgement-legacy) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**user** [[legal_professional]]

**stack** devvit, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for [port] judgement legacy

## Body

User Flair Awarded by Devvit App User Flair Awarded by Devvit App - Showing Progession to next Levels in user Flair Post Flair Awarded by Devvit App Inspiration r/AmITheAsshole Mod Team was looking to migrate their Judgement bot to Devvit and I helped them to do that while respecting their old scores and levels user's had. What it does It is a bot that gives judgement , Members of AmITheAsshole ask in post are they wrong or not , In comment members reply them with verdict YTA(You the Asshole) , NTA(Not The Asshole) and some more other verdicts like Everyone Sucks Here(ESH) & INFO (Need more information). Bot starts working after OP make the post. Bot will check if post exist or user is banned or deleted after 18hour , If user is no more on reddit it will lock the post and close the thread. If Post is still active it fetches what Top comment(Most upvoted) says and update the post flair with verdict & Award the Comment Author with +1 point which helps them climb the levels of r/AmITheAsshole . If post doesn't have any verdict means no one gave verdict to OP , It will be send to Moderators for Pass the Judgement How we built it I built it with Devvit and Typescript Challenges we ran into Handling the verdict as user can say the verdict anywhere in their comment , So Making sure It doesn't detect verdict from words containing short form of verdicts like NTA , ESH , INFO . Maintaining the old scores was difficult , as one mistake and all old user's score will be gone which they worked so much hard for. First thought of grabbing all existing data and pushing it to reddit but that can break so I implemented in such way that it will grab existing flairs and based on that it will upgrade user's score. It was hard as grabbing their score and updating it with new one took some time due to failure in detection of score inside the flair for various levels. Accomplishments that we're proud of Bot was successfully ported and now working in https://www.reddit.com/r/AITA_Relationships/ , After Successful month of testing it will be moved on to their network to serve millions of reddit users. Glad i could be helpful to their Community What we learned I learned more about the handling of user flairs and how to handle the schedule jobs to act on the verdicts and making sure everything is connected well to make sure every scenario is already thought of and was ready to be tackled. What's next for [PORT] Judgement Legacy I'll keep maintaining the bot for r/AmITheAsshole for any future updates as well or if they want new features in it. <div