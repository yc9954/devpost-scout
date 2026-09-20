---
slug: "memory-coach"
url: "https://devpost.com/software/memory-coach"
title: "memory-coach"
hackathon: "HackVortex Codestorm 5"
organization: "HackVortex"
winner: true
words: 534
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# memory-coach

> Every 3 seconds, someone in the world develops dementia.But with patience, understanding, and gentle reminders, tomorrow can be kinder.

[Devpost](https://devpost.com/software/memory-coach) · hackathon [[HackVortex Codestorm 5]]

## Facets

  <sub>weak: deterministic_policy</sub>
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** flask, mui, python, react, sqlite, webspeech

## How they structured the write-up

- inspiration--for a long time alzheimer’s placed a heavy burden on patients and families. memories fade but patients easy tools to preserve them, and caregivers often struggle with a lack of clear guidance. we’re building a project that helps patients rebuild and manage memories and helps everyone learn more about alzheimer’s,so day-to-day care feels more informed and humane.
- what it does--memory coach is a comprehensive wellness web application designed specifically for individuals with mild to moderate alzheimer's disease and their caregivers. it helps users capture life memories through voice and text, manage gentle reminders for medications and daily activities, and engage in cognitive exercises through interactive quizzes.
- how we built it--we built a react (vite) frontend with material ui and a flask backend using sqlalchemy and alembic on sqlite. the client calls rest endpoints under link , and cors connects the two during local dev.
- challenges we ran into--initial registration flow had a typical email + password login, though later we realized that demanding alzheimer’s patients to set a password was not very inclusive. finally, we decided to switch to the password-less login systems via one-time pins over email. here the snag would not unfreeze: some phones always threw an ‘ascii’ codec error for our mailer. after following headers and bytes, we discovered the source of the problem – non-ascii (e.g., an account name containing chinese characters) characters began sneaking into the from/to headers. we added a safety net that basically automatically converts any non-ascii characters in email addresses and headers to some safe representation before dispatching-the device would then not crash when it encountered an email having non-english account names.improved with sanitation + logging,pin emails can be delivered reliably across locales and devices without affecting any; that is, the login process itself remains simple and less memory-demanding for our users.
- accomplishments that we're proud of--we’re proud to have shipped the polished experience end-to-end. we implemented a dashboard hero on the ui side with subtle image overlay/fade so that the text is still readable without losing the warmth of the photo. on the backend, we fought through sqlite/alembic upgrades in testing and on production, made a small cleanup script to drop stray alembic_tmp * tables before re-running migrations, which were blocking our schema updates.
- what we learned--we now know how to implement the design of a clean, stateful quiz flow from one end to another: a start-session route, per-question answering with answer-locking, and an automatic “wrong-answer notebook” for later review. what’s backbreaking is that wrestling with migrations made us realize we should be treating data modeling like ops—be careful with alembic, keep test data deterministic and build small utilities (e.g. a cleanup script for temp tables) to keep upgrades reliable. most importantly, collaborating across an 8-hour time difference made us write clearer issues, define crisp ownership, and hand off work intentionally—skills that sped us up far more than any single library.
- what's next for memory-coach--we are developing an ai chatbot which focuses on four things: memory preservation and organization, transforming conversations into spaced memory prompts, providing calm, supportive language during emotionally charged situations, and memory retrieval and reconstruction using minimal clues like a name, address, or photo.

## Body

Dashboard Memory Management Reminders Caregiver quiz Dashboard Inspiration--For a long time Alzheimer’s placed a heavy burden on patients and families. Memories fade but patients easy tools to preserve them, and caregivers often struggle with a lack of clear guidance. We’re building a project that helps patients rebuild and manage memories and helps everyone learn more about Alzheimer’s,so day-to-day care feels more informed and humane. What it does--Memory Coach is a comprehensive wellness web application designed specifically for individuals with mild to moderate Alzheimer's disease and their caregivers. It helps users capture life memories through voice and text, manage gentle reminders for medications and daily activities, and engage in cognitive exercises through interactive quizzes. How we built it--We built a React (Vite) frontend with Material UI and a Flask backend using SQLAlchemy and Alembic on SQLite. The client calls REST endpoints under link , and CORS connects the two during local dev. Challenges we ran into--Initial registration flow had a typical email + password login, though later we realized that demanding Alzheimer’s patients to set a password was not very inclusive. Finally, we decided to switch to the password-less login systems via one-time PINs over email. Here the snag would not unfreeze: some phones always threw an ‘ascii’ codec error for our mailer. After following headers and bytes, we discovered the source of the problem – non-ASCII (e.g., an account name containing Chinese characters) characters began sneaking into the From/To headers. We added a safety net that basically automatically converts any non-ASCII characters in email addresses and headers to some safe representation before dispatching-the device would then not crash when it encountered an email having non-English account names.Improved with sanitation + logging,PIN emails can be delivered reliably across locales and devices without affecting any; that is, the login process itself remains simple and less memory-demanding for our users. Accomplishments that we're proud of--We’re proud to have shipped the polished experience end-to-end. We implemented a dashboard hero on the UI side with subtle image overlay/fade so that the text is still readable without losing the warmth of the photo. On the backend, we fought through SQLite/Alembic upgrades in testing and on production, made a small cleanup script to drop stray alembic_tmp * tables before re-running migrations, which were blocking our schema updates. What we learned--We now know how to implement the design of a clean, stateful quiz flow from one end to another: a start-session route, per-question answering with answer-locking, and an automatic “wrong-answer notebook” for later review. What’s backbreaking is that wrestling with migrations made us realize we should be treating data modeling like ops—be careful with Alembic, keep test data deterministic and build small utilities (e.g. a cleanup script for temp tables) to keep upgrades reliable. Most importantly, collaborating across an 8-hour time difference made us write clearer issues, define crisp ownership, and hand off work intentionally—skills that sped us up far more than any single library. What's next for memory-coach--We are developing an AI chatbot which focuses on four things: memory preservation and organization, transforming conversations into spaced memory prompts, providing calm, supportive language during emotionally charged situations, and memory retrieval and reconstruction using minimal clues like a name, address, or photo. <div