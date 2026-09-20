---
slug: "mod-recruit"
url: "https://devpost.com/software/mod-recruit"
title: "Mod Recruit"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 715
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Mod Recruit

> No Google Forms, no spreadsheets, no external links. Just recruit, review, and onboard your mod team right inside Reddit

[Devpost](https://devpost.com/software/mod-recruit) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**user** [[educator_student]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** css3, devvit, hono, react, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for mod recruit

## Body

Splash Screen GIF Application Flow GIF Mod Dashboard View Inspiration The initial pattern I noticed was how hectic the moderator recruitment process is. Mods were using Google Forms and spreadsheets to track applicants, and they often had to make separate posts telling users to message Modmail. Then, those modmails would get missed, tracking everything was a hassle, and they couldn't easily discuss candidates with the mod team. This caused huge delays in recruitment and forced mods to constantly copy-paste details to communication platforms like Discord. I wanted to build an app that gives a native experience and lets you manage everything on Reddit without leaving. It also solves the problem on the applicant's side, where they often feel ghosted because they have no idea what is happening with their application status, and lets them save their progress as a draft so they do not have to rush or lose their answers. What it does ModRecruit is a complete moderator recruitment tool that lives right inside your subreddit and makes recruiting way easier for mods: Custom Form Builder: It's not just boring questions. You can create 10 different types of questions, including choice-based scenario comments, scenario posts, and rating scales. Auto-Screening: Mods can customize who is allowed to apply based on account age, karma, and community karma. Draft Saving: Applicants don't have to rush. they can start their application, leave, and come back later without losing progress. Mod Dashboard: A single space for mods to review, vote, add notes about applications, and accept, reject, or request more info - all in just a few clicks. Smart Scoring: Mods can assign points to choice based answers. Applicants who reach a certain threshold score will be highlighted, helping mods find the perfect match. Discord Integration: No more hassle of copy-pasting to Discord to discuss candidates. Whenever someone applies, it automatically sends a copy to Discord so mods can talk about it there. Customized Modmails: Mods can customize modmail templates for accepting, rejecting, or requesting info, and can even send a moderator invite right from the dashboard. How we built it This app is built completely on the Devvit React template, which gave us everything we needed to build the app. For the backend, I used Hono for the API routing, and the frontend is built with React, CSS, and Devvit-specific components like forms and menu actions. For the database, everything is powered by Redis via Devvit's native Redis plugin. Accomplishments that we're proud of Sleek UI and UX: I love what I did with the UI. It's smooth, intuitive for users, fully responsive on all devices, and gives a truly native feel inside Reddit. Question Slides: I really like the different types of questions. They make answering much more engaging with choice-based image slides and scenarios that help mods find the right fit. The form builder is also super easy to use, allowing mods to create, reorder, or remove questions as they wish. Deep Customization: The app is highly customizable, including the landing screen, modmail templates, recruitment criteria, and reviewer permissions. Mods can easily tweak everything from the settings page. Recruitment Cycles: Usually, it's hard to remember what happened in previous recruitment drives. But in ModRecruit, everything is preserved in cycles, so if the same applicant applies again in a new cycle, mods can easily look back at their past answers. What we learned I learned a lot, particularly about Redis since I hadn't used it much outside of Devvit before. This was a great opportunity to dive deep into atomic transactions, watches, and other database concepts. I also learned a ton about the Devvit platform itself, how mods approach recruitment, what they actually look for in candidates, how crucial early feedback is, and the massive role that clean UI/UX plays in an app. What's next for Mod Recruit Interactive Analytics: I'm planning to make the dashboard analytics more interactive so mods can get better overall insights at a glance. Interactive Onboarding: I want to build an onboarding flow to get new mods ready for the sub, using training tutorials that help them understand the specific vibe and rules of the community. Refined Templates & Accessibility: Spend more time refining templates and accessibility so mods can get everything ready in just a few clicks without any hassle. <div